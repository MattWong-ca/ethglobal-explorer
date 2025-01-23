from supabase import create_client
import os
import json
from dotenv import load_dotenv

load_dotenv()

supabase = create_client(
    os.getenv('SUPABASE_URL'),
    os.getenv('SUPABASE_SERVICE_KEY')
)

# Read the JSON file
with open('hackathon_slugs.json', 'r') as file:
    data = json.load(file)
    slugs = data['slugs']

# Insert each slug into the Supabase table
for slug in slugs:
    try:
        # Insert the slug into the 'events' table
        data = supabase.table('events').insert({
            "slug": slug
        }).execute()
        print(f"Successfully added: {slug}")
    except Exception as e:
        print(f"Error adding {slug}: {str(e)}")

print("Finished adding slugs to Supabase!")