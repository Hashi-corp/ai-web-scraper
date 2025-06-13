import streamlit as st
from scraper import (
    scrape_website,
    scrape_body_content,
    clean_body_content,
    split_dom_content
)

st.title("Smart Web Scraper")
url = st.text_input("Enter URL")

if st.button("Scrape Site"):
    st.write("Scraping website...")
    
    result = scrape_website(url)
    body_content = scrape_body_content(result)
    clean_body_content = clean_body_content(body_content)

    st.session_state.dom_content = clean_body_content

    with st.expander("View DOM Content"):
        st.text_area(
            "DOM Content",
            clean_body_content,
            height=300
        )

if "dom_content" in  st.session_state:
    parse_description = st.text_area(
        "describe what you want to parse"
    )

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing content...")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            