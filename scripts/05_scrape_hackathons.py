from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json

def scrape_hackathons():
    print("Starting scraper...")
    
    # Configure Chrome options for faster loading
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-images')
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    
    driver.get(f"https://ethglobal.com/events/hackathons")
    
    # Initialize array to store hackathons
    hackathons = []
    
    # Wait for the specific div to be present
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "divide-y-2"))
        )
    except:
        print("Timeout waiting for content to load")
        driver.quit()
        return
        
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    target_div = soup.find('div', class_="divide-y-2 border-t-2 border-b-2 border-black")
    if target_div:
        for link in target_div.find_all('a'):
            # Create hackathon object
            hackathon = {}
            
            # Get name from h3
            h3 = link.find('h3')
            hackathon['name'] = h3.text.strip() if h3 else None
            
            # Get URL
            hackathon['url'] = link['href']
            
            # Get logo URL
            img = link.find('img')
            hackathon['logo_url'] = img['src'] if img and img.get('src') else None
            
            # Get type
            status_div = link.find('div', class_="inline-flex overflow font-semibold items-center space-x-2 uppercase py-1 bg-green-300 text-xs border-black px-3 border-2 rounded-sm")
            if not status_div:
                status_div = link.find('div', class_="inline-flex overflow font-semibold items-center space-x-2 uppercase py-1 bg-purple-300 text-xs border-black px-3 border-2 rounded-sm")
            hackathon['type'] = status_div.text.strip() if status_div else None
            
            # Get dates
            time_tags = link.find_all('time')
            if len(time_tags) >= 2:
                hackathon['start_date'] = time_tags[0].text.strip()
                hackathon['end_date'] = time_tags[1].text.strip()
            else:
                hackathon['start_date'] = None
                hackathon['end_date'] = None
            
            # Add hackathon to array
            hackathons.append(hackathon)
        
        # Print all hackathons
        print("\nAll Hackathons:")
        for hackathon in hackathons:
            print(json.dumps(hackathon, indent=2))
            print("---")
        
        # Create JSON object with hackathons property
        data = {
            "hackathons": hackathons
        }
        
        # Write to JSON file
        with open('all_hackathons.json', 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"\nTotal hackathons saved to hackathons.json: {len(hackathons)}")
    else:
        print("Target div not found")
    
    driver.quit()

if __name__ == "__main__":
    scrape_hackathons()