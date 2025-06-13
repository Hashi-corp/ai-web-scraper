from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By


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
        html = driver.page_source
        return html

if __name__ == '__main__':
    scrape_website()