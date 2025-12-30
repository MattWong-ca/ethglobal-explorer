# This script scrapes prizes from multiple ETHGlobal event pages
# and saves new prizes (not already in the database) to a JSON file (new_prizes_multiple_events.json)

import requests
from bs4 import BeautifulSoup
from supabase import create_client
import os
from dotenv import load_dotenv
import json
import time

# Load environment variables
load_dotenv()

# Initialize Supabase client
supabase = create_client(
    os.getenv('SUPABASE_URL'),
    os.getenv('SUPABASE_SERVICE_KEY')
)

def get_existing_prize_urls():
    """Get all existing prize URLs from the database"""
    result = supabase.table('prizes').select('img_url').execute()
    return {prize['img_url'] for prize in result.data}

def scrape_prizes_from_event(event_slug):
    """Scrape prizes from a specific ETHGlobal event page"""
    print(f"Scraping prizes from event: {event_slug}")
    
    # Fetch the page
    url = f'https://ethglobal.com/events/{event_slug}'
    print(f"Fetching: {url}")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find prize sections
    prize_sections = soup.find_all('a')
    
    new_prizes = []
    existing_urls = get_existing_prize_urls()
    
    print(f"Found {len(existing_urls)} existing prizes in database")
    
    for section in prize_sections:
        # Only process if it's a prize link
        if section.get('href') and section.get('href').startswith(f'/events/{event_slug}/prizes/'):
            # Find image and prize name
            img_element = section.find('img')
            name_element = section.find('h4')
            
            # Only process if both image and name are found
            if img_element and name_element:
                img_url = img_element['src']
                prize_name = name_element.text.strip()
                
                print(f"Found prize: {prize_name} -> {img_url}")
                
                # Check if this prize already exists in database
                if img_url not in existing_urls:
                    new_prizes.append({
                        'name': prize_name,
                        'img_url': img_url,
                        'event': event_slug
                    })
                    print(f"  -> NEW PRIZE (not in database)")
                else:
                    print(f"  -> Already exists in database")
    
    return new_prizes

def save_new_prizes_to_json(new_prizes, filename='new_prizes.json'):
    """Save new prizes to a JSON file"""
    if new_prizes:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({'prizes': new_prizes}, f, indent=2, ensure_ascii=False)
        print(f"\nSaved {len(new_prizes)} new prizes to {filename}")
    else:
        print("\nNo new prizes found!")

def update_prizes_from_event(event_slug):
    """Main function to scrape and save new prizes from an event"""
    print(f"=== Processing event: {event_slug} ===")
    
    # Scrape new prizes
    new_prizes = scrape_prizes_from_event(event_slug)
    
    # Save to JSON file
    filename = f'new_prizes_{event_slug}.json'
    save_new_prizes_to_json(new_prizes, filename)
    
    print(f"\nSummary for {event_slug}:")
    print(f"- Found {len(new_prizes)} new prizes")
    print(f"- Saved to: {filename}")
    
    return new_prizes

def update_prizes_from_multiple_events(event_slugs, delay_seconds=3):
    """Process multiple events with delays between each"""
    print(f"=== Processing {len(event_slugs)} events ===")
    
    all_new_prizes = []
    seen_prize_urls = set()  # Track unique prize URLs
    
    for i, event_slug in enumerate(event_slugs, 1):
        print(f"\n{'='*50}")
        print(f"Processing event {i}/{len(event_slugs)}: {event_slug}")
        print(f"{'='*50}")
        
        # Scrape prizes from this event
        new_prizes = scrape_prizes_from_event(event_slug)
        
        # Filter out duplicates and add event info
        unique_prizes = []
        for prize in new_prizes:
            if prize['img_url'] not in seen_prize_urls:
                seen_prize_urls.add(prize['img_url'])
                prize['event'] = event_slug
                unique_prizes.append(prize)
                print(f"  -> Added new prize: {prize['name']}")
            else:
                print(f"  -> Skipped duplicate prize: {prize['name']} (already seen)")
        
        all_new_prizes.extend(unique_prizes)
        
        print(f"Found {len(new_prizes)} prizes from {event_slug}, {len(unique_prizes)} were unique")
        
        # Add delay between events (except for the last one)
        if i < len(event_slugs):
            print(f"Waiting {delay_seconds} seconds before next event...")
            time.sleep(delay_seconds)
    
    # Save all new prizes to a combined JSON file
    if all_new_prizes:
        filename = f'new_prizes_dec_29.json'
        save_new_prizes_to_json(all_new_prizes, filename)
        
        print(f"\n{'='*50}")
        print(f"SUMMARY:")
        print(f"- Processed {len(event_slugs)} events")
        print(f"- Found {len(all_new_prizes)} unique new prizes (duplicates removed)")
        print(f"- Saved to: {filename}")
        print(f"{'='*50}")
    else:
        print(f"\nNo new prizes found across all {len(event_slugs)} events!")
    
    return all_new_prizes

if __name__ == "__main__":
    # Example usage for multiple events:
    event_slugs = [
        "newdelhi",
        "ethonline2025",
        "buenosaires"
        # Add more event slugs here
    ]
    
    # Process multiple events with 3-second delays
    update_prizes_from_multiple_events(event_slugs, delay_seconds=10)
    
    # Or for a single event:
    # update_prizes_from_event("spacewarp") 