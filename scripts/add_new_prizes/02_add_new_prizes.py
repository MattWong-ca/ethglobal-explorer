# This script uploads new prizes from the JSON file to the Supabase prizes table

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

def add_new_prizes(filename='new_prizes_dec_29.json'):
    """Upload new prizes from JSON file to Supabase"""
    print(f"Uploading prizes from: {filename}")
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File {filename} not found!")
        return
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {filename}: {e}")
        return
    
    prizes = data.get('prizes', [])
    if not prizes:
        print("No prizes found in JSON file!")
        return
    
    print(f"Found {len(prizes)} prizes to upload")
    
    success_count = 0
    error_count = 0
    skipped_count = 0
    
    for i, prize in enumerate(prizes, 1):
        try:
            print(f"\nProcessing prize {i}/{len(prizes)}: {prize['name']}")
            
            # Check if prize already exists
            existing = supabase.table('prizes').select('id').eq('img_url', prize['img_url']).execute()
            if existing.data and len(existing.data) > 0:
                print(f"  -> Already exists in database, skipping")
                skipped_count += 1
                continue
            
            # Insert new prize
            result = supabase.table('prizes').insert({
                'name': prize['name'],
                'img_url': prize['img_url']
            }).execute()
            
            success_count += 1
            print(f"  -> Successfully uploaded: {prize['name']}")
            
        except Exception as e:
            error_count += 1
            print(f"  -> Error uploading {prize['name']}: {str(e)}")
    
    print(f"\n{'='*50}")
    print(f"UPLOAD SUMMARY:")
    print(f"- Total prizes processed: {len(prizes)}")
    print(f"- Successfully uploaded: {success_count}")
    print(f"- Already existed (skipped): {skipped_count}")
    print(f"- Errors: {error_count}")
    print(f"{'='*50}")

if __name__ == "__main__":
    # Upload from the default file
    add_new_prizes()
    
    # Or specify a different file:
    # add_new_prizes('new_prizes_spacewarp.json') 