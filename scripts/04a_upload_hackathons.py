from supabase import create_client
import os
import json
from dotenv import load_dotenv

load_dotenv()

# The initial version, which only contains the name of the hackathon
supabase = create_client(
    os.getenv('SUPABASE_URL'),
    os.getenv('SUPABASE_SERVICE_KEY')
)

# Read the JSON file
with open('ethglobal_hackathons.json', 'r') as file:
    data = json.load(file)
    events = data['allEvents']

# Insert each event into the Supabase table
for event_name in events:
    try:
        # Insert the event into the 'events' table
        data = supabase.table('events').insert({
            "name": event_name
        }).execute()
        print(f"Successfully added: {event_name}")
    except Exception as e:
        print(f"Error adding {event_name}: {str(e)}")

print("Finished adding events to Supabase!")