import streamlit as st
from scrape import scrape_website, split_dom_content,clean_body_content,extract_body_content
from parse import parse_with_groq
from dotenv import load_dotenv
import os
load_dotenv()
url=os.getenv("URL")

st.title("MILLARD AYO NEWS WITH AI 🤖")
parse_descriptions=st.text_area("What you need to know?",height=100)




if st.button("Submit"):
    result=scrape_website(url)
    body_content=extract_body_content(result)
    cleaned_content=clean_body_content(body_content)
    st.session_state.dom_content=cleaned_content
    # with st.expander("View DOM Content"):
    #     st.text_area("DOM Content",cleaned_content,height=300)
    if "dom_content" in st.session_state:
        st.success("successful",icon="⚡")
        if parse_descriptions:

            dom_chunks=split_dom_content(st.session_state.dom_content)
            result=parse_with_groq(dom_chunks,parse_descriptions)
            st.write(result,unsafe_allow_html=True)
            st.error("_Response may be incorrect as the app is still under development and undergoing testing._")
            st.write(f'news source:  {url}')