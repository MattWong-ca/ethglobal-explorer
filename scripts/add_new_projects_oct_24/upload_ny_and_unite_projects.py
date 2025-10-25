# This script uploads projects from new_projects_jul_14.json where event = "new_event_name"
# Based on 03_upload_projects.py

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
    
    # For unknown prizes, skip them and log a warning
    print(f"Warning: Unknown prize image URL: {img_url}")
    print("Skipping this prize to avoid creating unnamed prize entries.")
    return None

def upload_new_projects():
    print("Starting upload of new projects...")
    
    # Read the JSON file
    with open('new_ny_and_unite_projects.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Filter projects for "new_event_name" event
    all_projects = data['projects']
    new_projects = [project for project in all_projects if project['event'] == 'ETHGlobal New York 2025']
    
    total = len(new_projects)
    success_count = 0
    error_count = 0
    
    print(f"Found {total} new projects to upload")
    
    for index, project in enumerate(new_projects, 1):
        try:
            print(f"\nProcessing project {index}/{total}: {project['title']}")
            
            # Check if project already exists
            existing = supabase.table('projects').select('id').eq('url', project['url']).execute()
            if existing.data and len(existing.data) > 0:
                print(f"Project already exists: {project['title']}")
                continue
            
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
                    
                    # Only create relationship if prize was found
                    if prize_id:
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
    upload_new_projects() 