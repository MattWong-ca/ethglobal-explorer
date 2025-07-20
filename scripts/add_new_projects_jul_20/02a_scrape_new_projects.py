# This script scrapes all 391 pages of the ETHGlobal Showcase page 
# and saves the project data to a JSON file (ethglobal_projects.json).
# It was originally supposed to both scrape + upload, but ran into issues.
# Separating the scraping + uploading scripts is more reliable.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json

def scrape_ethglobal_showcase():
    print("Starting scraper...")
    
    # Configure Chrome options for faster loading
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-images')
    options.add_argument('--disable-javascript')
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    
    driver.implicitly_wait(2)
    
    total_pages = 50
    total_projects = 0
    projects = []  # List to store all project data
    
    for page in range(1, total_pages):
        print(f"\n=== Processing page {page}/{total_pages} ===")
        driver.get(f"https://ethglobal.com/showcase?page={page}")
        
        try:
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href^="/showcase/"]'))
            )
        except:
            print(f"Warning: Page {page} might not have loaded completely")
            
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        print("\nChecking page content...")
        
        all_links = soup.find_all('a')
        count = 0
        project_position = 0
        
        for link in all_links:
            if link.get('href') and link.get('href').startswith('/showcase/'):
                if project_position == 32:
                    project_position += 1
                    continue
                
                count += 1
                total_projects += 1
                project_url = f"https://ethglobal.com{link.get('href')}"
                
                # Extract project data
                title = description = event = None
                prizes = []
                
                h2 = link.find('h2')
                if h2:
                    title = h2.text.strip()

                p = link.find('p')
                if p:
                    description = p.text.strip()
                
                div = link.find('div')
                if div:
                    event = div.text.strip()
                
                # Extract prize images
                spans = link.find_all('span', class_='inline-flex items-center -space-x-2 absolute right-6 transform -translate-y-1/2')
                for span in spans:
                    images = span.find_all('img')
                    for img in images:
                        img_src = img.get('src')
                        if img_src:
                            prizes.append(img_src)
                
                # Create project object and append to list
                if title:
                    project_data = {
                        'title': title,
                        'description': description,
                        'event': event,
                        'url': project_url,
                        'prizes': prizes
                    }
                    projects.append(project_data)
                    print(f"Scraped project: {title}")
                
                project_position += 1

        print(f"Total links found on page {page}: {count}")
        print(f"Total projects found: {total_projects}")
    
    driver.quit()
    
    # Save to JSON file
    with open('new_projects_jul_14.json', 'w', encoding='utf-8') as f:
        json.dump({'projects': projects}, f, indent=2, ensure_ascii=False)
    
    print(f"\nScraping complete! Saved {len(projects)} projects to new_projects_jul_14.json")

if __name__ == "__main__":
    scrape_ethglobal_showcase()