import streamlit as st
from scraper import scrape_website

st.title("Smart Web Scraper")
url = st.text_input("Enter URL")

if st.button("Scrape Site"):
    st.write("Scraping website...")
    result = scrape_website(url)
    print(result)