import streamlit as st
from parser.extract_info import extract_text_from_pdf, extract_resume_info
from parser.suggestions import suggest_improvements

st.set_page_config(page_title="Resume Parser & Enhancer", layout="centered")
st.title("📄 Resume Parser & Enhancer")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    st.info("Parsing your resume...")
    text = extract_text_from_pdf(uploaded_file)
    info = extract_resume_info(text)
    suggestions = suggest_improvements(info)

    st.subheader(" Extracted Info")
    st.json(info)

    st.subheader(" Enhancement Suggestions")
    for s in suggestions:
        st.write(f"- {s}")
