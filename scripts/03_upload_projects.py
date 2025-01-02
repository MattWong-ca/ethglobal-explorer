# This script uses the JSON file created by 02_scrape_projects.py
# to upload the projects to Supabase. It iterates through each project,
# and for each project, it iterates through each prize image.
# It then creates a new prize if it doesn't exist, and creates a relationship
# in the junction table between the project and the prize(s).

import json
from supabase import create_client
import os
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Initialize Supabase client
supabase = create_client(
    os.getenv('SUPABASE_URL'),
    os.getenv('SUPABASE_SERVICE_KEY')
)

def get_or_create_prize(img_url):
    # Find existing prize
    result = supabase.table('prizes').select('id').eq('img_url', img_url).execute()
    if result.data and len(result.data) > 0:
        return result.data[0]['id']

def upload_projects():
    print("Starting upload process...")
    
    # Read the JSON file
    with open('ethglobal_projects.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    projects = data['projects'] 
    total = len(projects)
    success_count = 0
    error_count = 0
    
    print(f"Found {total} projects to upload")
    
    for index, project in enumerate(projects, 1):
        try:
            print(f"\nProcessing project {index}/{total}: {project['title']}")
            
            # Insert project into Supabase
            project_result = supabase.table('projects').insert({
                'title': project['title'],
                'description': project['description'],
                'event': project['event'],
                'url': project['url']
            }).execute()
            
            project_id = project_result.data[0]['id']
            
            # Process each prize image
            for prize_url in project['prizes']:
                try:
                    # Get or create prize
                    prize_id = get_or_create_prize(prize_url)
                    
                    # Create relationship in junction table
                    supabase.table('project_prizes').insert({
                        'project_id': project_id,
                        'prize_id': prize_id
                    }).execute()
                except Exception as prize_error:
                    print(f"Error processing prize {prize_url}: {str(prize_error)}")
            
            success_count += 1
            print(f"Successfully uploaded: {project['title']}")
            
        except Exception as e:
            error_count += 1
            print(f"Error uploading {project['title']}: {str(e)}")
    
    print(f"\nUpload complete!")
    print(f"Successfully uploaded: {success_count}")
    print(f"Errors: {error_count}")

if __name__ == "__main__":
    upload_projects()
