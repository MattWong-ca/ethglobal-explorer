from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from supabase import create_client
from dotenv import load_dotenv
import os
import json

#TO-DO: separate scraping + inserting into supabase scripts
# Load environment variables
load_dotenv()

# Initialize Supabase client
supabase = create_client(
    os.getenv('SUPABASE_URL'),
    os.getenv('SUPABASE_SERVICE_KEY')
)

def insert_project(title, description, event, url):
    try:
        # Insert project and return the inserted row
        response = supabase.table('projects').insert({
            'title': title,
            'description': description,
            'event': event,
            'url': url
        }).execute()
        
        # Return the project id from the inserted row
        return response.data[0]['id'] if response.data else None
    except Exception as e:
        print(f"Error inserting project: {e}")
        return None

def get_prize_id(img_url):
    try:
        # Query prizes table to find the prize id based on img_url
        response = supabase.table('prizes').select('id').eq('img_url', img_url).execute()
        return response.data[0]['id'] if response.data else None
    except Exception as e:
        print(f"Error finding prize: {e}")
        return None

def insert_project_prize(project_id, prize_id):
    try:
        # Insert into junction table
        response = supabase.table('project_prizes').insert({
            'project_id': project_id,
            'prize_id': prize_id
        }).execute()
        return True
    except Exception as e:
        print(f"Error inserting project_prize relation: {e}")
        return False

def scrape_ethglobal_showcase():
    print("Starting scraper...")
    
    # Configure Chrome options for faster loading
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-images')  # Don't load images
    options.add_argument('--disable-javascript')  # Disable JavaScript
    options.add_argument('--headless')  # Run in headless mode (no GUI)
    driver = webdriver.Chrome(options=options)
    
    # Reduce implicit wait time
    driver.implicitly_wait(2)
    
    total_pages = 391
    total_projects = 0
    unique_images = set()  # Using a set to automatically handle duplicates
    
    for page in range(1, total_pages + 1):
        print(f"\n=== Processing page {page}/{total_pages} ===")
        driver.get(f"https://ethglobal.com/showcase?page={page}")
        
        # Replace static sleep with dynamic wait
        try:
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href^="/showcase/"]'))
            )
        except:
            print(f"Warning: Page {page} might not have loaded completely")
            
        # Get page source and parse with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        print("\nChecking page content...")
        
        # Try to find any links
        all_links = soup.find_all('a')
        count = 0
        project_position = 0  # Track position on page
        for link in all_links:
            if link.get('href') and link.get('href').startswith('/showcase/'):
                # Skip if it's the 33rd project on the page
                if project_position == 32:  # 33rd item (0-based index)
                    project_position += 1
                    continue
                
                count += 1
                total_projects += 1
                project_url = f"https://ethglobal.com{link.get('href')}"
                
                # Initialize variables
                title = description = event = None
                
                # Extract title
                h2 = link.find('h2')
                if h2:
                    title = h2.text.strip()

                # Extract description
                p = link.find('p')
                if p:
                    description = p.text.strip()
                
                # Extract event
                div = link.find('div')
                if div:
                    event = div.text.strip()
                
                # Insert into Supabase if we have at least a title
                if title:
                    project_id = insert_project(title, description, event, project_url)
                    if project_id:
                        print(f"Inserted project: {title}")
                        
                        # Find and process prizes
                        spans = link.find_all('span', class_='inline-flex items-center -space-x-2 absolute right-6 transform -translate-y-1/2')
                        for span in spans:
                            images = span.find_all('img')
                            for img in images:
                                img_src = img.get('src')
                                if img_src:
                                    # Get prize_id and create relationship
                                    prize_id = get_prize_id(img_src)
                                    if prize_id:
                                        if insert_project_prize(project_id, prize_id):
                                            print(f"   - Added prize relation for project: {title}")
                                        else:
                                            print(f"   - Failed to add prize relation for project: {title}")
                    else:
                        print(f"Failed to insert project: {title}")
                
                project_position += 1

        print(f"Total links found on page {page}: {count}")
        print(f"Total projects found: {total_projects}")
    print("\n=== Summary ===")
    print(f"Total unique images found: {len(unique_images)}")
    print("\nUnique image sources:")
    for img in sorted(unique_images):  # sorted() for cleaner output
        print(img)
    
    driver.quit()

if __name__ == "__main__":
    scrape_ethglobal_showcase()