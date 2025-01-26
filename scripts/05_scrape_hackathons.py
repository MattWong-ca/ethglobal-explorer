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
    # Find the specific div first
    target_div = soup.find('div', class_="divide-y-2 border-t-2 border-b-2 border-black")
    if target_div:
        for link in target_div.find_all('a'):
            h3 = link.find('h3')
            print(f"URL: {link['href']}")
            print(f"Title: {h3.text.strip() if h3 else 'No title found'}")
            
            # Find and print image src
            img = link.find('img')
            if img and img.get('src'):
                print(f"Image: {img['src']}")
            else:
                print("No image found")
            
            # Find and print the status div
            status_div = link.find('div', class_="inline-flex overflow font-semibold items-center space-x-2 uppercase py-1 bg-green-300 text-xs border-black px-3 border-2 rounded-sm")
            if not status_div:
                status_div = link.find('div', class_="inline-flex overflow font-semibold items-center space-x-2 uppercase py-1 bg-purple-300 text-xs border-black px-3 border-2 rounded-sm")
            if status_div:
                print(f"Type: {status_div.text.strip()}")
            else:
                print("No status found")
            
            # Find and print all time tags
            time_tags = link.find_all('time')
            if time_tags:
                for i, time in enumerate(time_tags, 1):
                    print(f"Time {i}: {time.text.strip()}")
            else:
                print("No time tags found")
            print("---")
    else:
        print("Target div not found")
    # for page in range(1, total_pages + 1):
    #     print(f"\n=== Processing page {page}/{total_pages} ===")
    #     driver.get(f"https://ethglobal.com/events/hackathons")
        
    #     # try:
    #     #     WebDriverWait(driver, 3).until(
    #     #         EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href^="/showcase/"]'))
    #     #     )
    #     # except:
    #     #     print(f"Warning: Page {page} might not have loaded completely")
            
    #     # soup = BeautifulSoup(driver.page_source, 'html.parser')
    #     # print("\nChecking page content...")
        
    #     all_links = soup.find_all('a')
    #     count = 0
    #     project_position = 0
        
    #     for link in all_links:
    #         if link.get('href') and link.get('href').startswith('/showcase/'):
    #             if project_position == 32:
    #                 project_position += 1
    #                 continue
                
    #             count += 1
    #             total_projects += 1
    #             project_url = f"https://ethglobal.com{link.get('href')}"
                
    #             # Extract project data
    #             title = description = event = None
    #             prizes = []
                
    #             h2 = link.find('h2')
    #             if h2:
    #                 title = h2.text.strip()

    #             p = link.find('p')
    #             if p:
    #                 description = p.text.strip()
                
    #             div = link.find('div')
    #             if div:
    #                 event = div.text.strip()
                
    #             # Extract prize images
    #             spans = link.find_all('span', class_='inline-flex items-center -space-x-2 absolute right-6 transform -translate-y-1/2')
    #             for span in spans:
    #                 images = span.find_all('img')
    #                 for img in images:
    #                     img_src = img.get('src')
    #                     if img_src:
    #                         prizes.append(img_src)
                
    #             # Create project object and append to list
    #             if title:
    #                 project_data = {
    #                     'title': title,
    #                     'description': description,
    #                     'event': event,
    #                     'url': project_url,
    #                     'prizes': prizes
    #                 }
    #                 projects.append(project_data)
    #                 print(f"Scraped project: {title}")
                
    #             project_position += 1

    #     print(f"Total links found on page {page}: {count}")
    #     print(f"Total projects found: {total_projects}")
    
    driver.quit()
    
    # Save to JSON file
    # with open('ethglobal_projects.json', 'w', encoding='utf-8') as f:
    #     json.dump({'projects': projects}, f, indent=2, ensure_ascii=False)
    
    # print(f"\nScraping complete! Saved {len(projects)} projects to ethglobal_projects.json")

if __name__ == "__main__":
    scrape_hackathons()