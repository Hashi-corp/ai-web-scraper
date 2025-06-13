from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def scrape_website(website):
    print("Launching web browser...")
    AUTH = 'brd-customer-hl_1107a4c1-zone-scraping_browser1:f3owe6qho4un'
    SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'
    
    print('Connecting to Browser API...')
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver: 
        print('Connected! Navigating...')
        driver.get(website) 
        print('Navigated! Scraping page content...')
        time.sleep(2)
        print('HTML content scraped successfully.')
        html = driver.page_source
        return html

def scrape_body_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.find('body')
    if body_content:
        for script in body_content(['script', 'style']):
            script.decompose()
        return body_content.get_text(strip=True)
    return None

def clean_body_content(body_content):
    if body_content:
        cleaned_content = body_content.replace('\n', ' ').replace('\r', '').strip()
        return cleaned_content
    return None

def split_dom_content(dom_content, max_length = 6000):
    return [
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]