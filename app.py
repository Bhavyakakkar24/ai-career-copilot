import streamlit as st
from resume_parser import extract_text_from_pdf
from skill_analyzer import extract_skills

st.title("AI Career Copilot 🚀")

st.write("Upload your resume to analyze your skills")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file is not None:

    text = extract_text_from_pdf(uploaded_file)

    skills = extract_skills(text)

    st.subheader("Detected Skills")

    if skills:
        for skill in skills:
            st.write("✅", skill)
    else:
        st.write("No skills detected")
