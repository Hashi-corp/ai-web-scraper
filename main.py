import streamlit as st
from ai_util import ai_parser
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
    
    api_key = st.text_input(
        "Enter your Gemini API Key",
        type="password"
    )

    if st.button("Parse Content"):
        if parse_description and api_key:
            st.write("Parsing content with AI...")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            prompt = f"{parse_description}\n\n{dom_chunks[0]}"
            response = ai_parser(prompt, api_key)
            st.write("AI Response:")
            st.write(response)
