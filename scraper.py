import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_website(website):
    print("Launching web browser...")
    
    chrome_driver_path = ChromeDriverManager().install()
    Options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(
        service=Service(chrome_driver_path),
        options=Options
    )

    try:
        driver.get(website)
        print("page loaded.")
        time.sleep(5)
        
        html = driver.page_source
        return html
    
    finally:
        driver.quit()

