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
import time

def scrape_ethglobal_showcase():
    print("Starting scraper...")
    
    # Configure Chrome options for faster loading
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-images')
    # options.add_argument('--disable-javascript')  # Comment this out - we need JS for dynamic content
    # options.add_argument('--headless')  # Comment out headless mode temporarily
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    # Add user agent to appear more like a real browser
    options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    
    # Add additional headers to avoid detection
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    driver = webdriver.Chrome(options=options)
    
    # Execute script to remove webdriver property
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    driver.implicitly_wait(5)  # Increased wait time
    
    total_pages = 20
    total_projects = 0
    projects = []  # List to store all project data
    
    for page in range(1, total_pages):
        print(f"\n=== Processing page {page}/{total_pages} ===")
        driver.get(f"https://ethglobal.com/showcase?page={page}")
        
        # Add a small delay to let the page load
        time.sleep(2)
        
        # Check if we're being blocked by Cloudflare
        if "Just a moment" in driver.title or "cloudflare" in driver.current_url.lower():
            print(f"WARNING: Page {page} is being blocked by Cloudflare!")
            print("Current title:", driver.title)
            print("Current URL:", driver.current_url)
            print("Waiting longer and trying again...")
            time.sleep(10)  # Wait longer
            driver.refresh()  # Refresh the page
            time.sleep(5)
        
        try:
            print(f"Waiting for showcase links on page {page}...")
            WebDriverWait(driver, 10).until(  # Increased timeout to 10 seconds
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href^="/showcase/"]'))
            )
            print(f"Successfully found showcase links on page {page}")
        except Exception as e:
            print(f"Warning: Page {page} might not have loaded completely")
            print(f"Error: {e}")
            
            # Debug: Let's see what's actually on the page
            print("Current page title:", driver.title)
            print("Current URL:", driver.current_url)
            
            # Check if there are any links at all
            all_links = driver.find_elements(By.TAG_NAME, 'a')
            showcase_links = driver.find_elements(By.CSS_SELECTOR, 'a[href^="/showcase/"]')
            print(f"Total links found: {len(all_links)}")
            print(f"Showcase links found: {len(showcase_links)}")
            
            # Print first few links for debugging
            for i, link in enumerate(all_links[:5]):
                href = link.get_attribute('href')
                text = link.text.strip()
                print(f"Link {i}: href='{href}', text='{text}'")
            
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
    with open('new_delhi_online_arg_projects.json', 'w', encoding='utf-8') as f:
        json.dump({'projects': projects}, f, indent=2, ensure_ascii=False)
    
    print(f"\nScraping complete! Saved {len(projects)} projects to new_cannes_projects.json")

if __name__ == "__main__":
    scrape_ethglobal_showcase()