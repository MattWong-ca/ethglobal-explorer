# This script updates projects that have prizes from the new_prizes_oct_25.json file
# It only processes projects that contain any of the new prize URLs

import json
from supabase import create_client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Supabase client
supabase = create_client(
    os.getenv('SUPABASE_URL'),
    os.getenv('SUPABASE_SERVICE_KEY')
)

def load_new_prize_urls():
    """Load the prize URLs from new_prizes_oct_25.json"""
    with open('../add_new_prizes/new_prizes_oct_25.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    prize_urls = [prize['img_url'] for prize in data['prizes']]
    print(f"Loaded {len(prize_urls)} new prize URLs:")
    for url in prize_urls:
        print(f"  - {url}")
    
    return prize_urls

def get_prize_id(img_url):
    """Get the prize ID from Supabase"""
    result = supabase.table('prizes').select('id').eq('img_url', img_url).execute()
    if result.data and len(result.data) > 0:
        return result.data[0]['id']
    return None

def update_projects_with_new_prizes():
    print("Starting update of projects with new prizes...")
    
    # Load new prize URLs
    new_prize_urls = load_new_prize_urls()
    
    # Read the projects JSON file
    with open('new_ny_and_unite_projects.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Filter projects for "ETHGlobal New York 2025" event
    all_projects = data['projects']
    target_projects = [project for project in all_projects if project['event'] == 'ETHGlobal New York 2025']
    
    print(f"\nFound {len(target_projects)} projects for ETHGlobal New York 2025")
    
    # Find projects that have any of the new prize URLs
    projects_to_update = []
    for project in target_projects:
        project_prize_urls = project.get('prizes', [])
        if project_prize_urls:
            # Check if any of the project's prizes are in our new prizes list
            matching_prizes = [url for url in project_prize_urls if url in new_prize_urls]
            if matching_prizes:
                projects_to_update.append({
                    'project': project,
                    'matching_prizes': matching_prizes
                })
    
    print(f"Found {len(projects_to_update)} projects with new prizes to update:")
    for item in projects_to_update:
        print(f"  - {item['project']['title']}: {len(item['matching_prizes'])} new prizes")
    
    if not projects_to_update:
        print("No projects need updating!")
        return
    
    success_count = 0
    error_count = 0
    
    for index, item in enumerate(projects_to_update, 1):
        project = item['project']
        matching_prizes = item['matching_prizes']
        
        try:
            print(f"\nProcessing project {index}/{len(projects_to_update)}: {project['title']}")
            
            # Find existing project in Supabase
            existing = supabase.table('projects').select('id').eq('url', project['url']).execute()
            if not existing.data or len(existing.data) == 0:
                print(f"Project not found in database: {project['title']}")
                error_count += 1
                continue
            
            project_id = existing.data[0]['id']
            
            # Process each matching prize
            prizes_added = 0
            for prize_url in matching_prizes:
                try:
                    # Get prize ID
                    prize_id = get_prize_id(prize_url)
                    
                    if prize_id:
                        # Check if relationship already exists
                        existing_relation = supabase.table('project_prizes').select('id').eq('project_id', project_id).eq('prize_id', prize_id).execute()
                        
                        if not existing_relation.data or len(existing_relation.data) == 0:
                            # Create the relationship
                            supabase.table('project_prizes').insert({
                                'project_id': project_id,
                                'prize_id': prize_id
                            }).execute()
                            prizes_added += 1
                            print(f"  Added prize relationship: {prize_url}")
                        else:
                            print(f"  Prize relationship already exists: {prize_url}")
                    else:
                        print(f"  Warning: Prize not found in database: {prize_url}")
                        
                except Exception as prize_error:
                    print(f"  Error processing prize {prize_url}: {str(prize_error)}")
            
            if prizes_added > 0:
                success_count += 1
                print(f"Successfully added {prizes_added} prize relationships to: {project['title']}")
            else:
                print(f"No new prize relationships added for: {project['title']}")
            
        except Exception as e:
            error_count += 1
            print(f"Error updating {project['title']}: {str(e)}")
    
    print(f"\nUpdate complete!")
    print(f"Successfully updated: {success_count}")
    print(f"Errors: {error_count}")

if __name__ == "__main__":
    update_projects_with_new_prizes()
