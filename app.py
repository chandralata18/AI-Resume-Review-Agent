import os
import tempfile

import streamlit as st
from dotenv import load_dotenv

from tools.pdf_reader import PDFReader
from agent.resume_agent import ResumeReviewAgent


load_dotenv()

st.set_page_config(
    page_title="AI Resume Review Agent",
    page_icon="🤖",
    layout="wide"
)

with st.sidebar:

    st.header("🤖 About")

    st.write(
        """
This AI Resume Review Agent analyzes resumes using Google's Gemini model.

### Features

- 🎯 Role Detection
- 📊 ATS Score
- 💪 Strength Analysis
- ⚠ Weakness Detection
- 📚 Missing Skills
- 💼 Interview Questions
"""
    )

    st.divider()

    st.markdown("""
    ### 🚀 Built for Kaggle AI Agents Capstone

    **Tech Stack**

    - 🤖 Google Gemini
    - ⚡ Streamlit
    - 🐍 Python
    """)

st.title("🤖 AI Resume Review Agent")

st.caption(
    "Analyze your resume using AI and receive ATS insights in seconds."
)

st.divider()

st.subheader("📂 Upload Resume")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

st.caption("Supported format: PDF")

if uploaded_file is not None:

    st.info("📄 Resume uploaded successfully")

    if st.button("🚀 Analyze Resume"):

        with st.spinner("🤖 AI Agent is analyzing your resume..."):

            # Create a temporary PDF file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                temp_file.write(uploaded_file.getvalue())
                temp_path = temp_file.name

            # Read PDF
            reader = PDFReader()
            resume_text = reader.extract_text(temp_path)

            # Analyze Resume
            agent = ResumeReviewAgent()
            analysis = agent.analyze_resume(resume_text)

            # Delete temporary file
            os.remove(temp_path)

        st.toast(
            "Analysis Complete!",
            icon="🎉"
        )

        col1, col2 = st.columns([2,1])

        with col1:
            st.metric(
                "🎯 Target Role",
                analysis["target_role"]
            )

        with col2:
            score = analysis["ats_report"]["ats_score"]

            st.metric(
                "📊 ATS Score",
                f"{score}/100"
            )

            st.progress(score / 100)

            if score >= 80:
                st.success("Excellent ATS compatibility!")

            elif score >= 60:
                st.warning("Good resume. Some improvements recommended.")

            else:
                st.error("Resume needs significant improvement.")

        st.divider()

        st.divider()

        st.subheader("📄 Professional Summary")

        st.info(analysis["resume_summary"])

        st.divider()

        tab1, tab2, tab3 = st.tabs(
            [
                "📈 ATS Report",
                "📚 Missing Skills",
                "💼 Interview Questions"
            ]
        )

        with tab1:

            st.subheader("💪 Strengths")

            for strength in analysis["ats_report"]["strengths"]:
                st.success(strength)

            st.subheader("⚠ Weaknesses")

            for weakness in analysis["ats_report"]["weaknesses"]:
                st.warning(weakness)

        with tab2:

            st.subheader("📚 Skills to Improve")

            st.info(
                "Learning these skills can improve your ATS score for the detected role."
            )

            for skill in analysis["ats_report"]["missing_skills"]:
                st.markdown(f"🔹 **{skill}**")

        with tab3:

            st.subheader("💼 Personalized Interview Questions")

            for i, question in enumerate(
                analysis["interview_questions"],
                start=1
            ):

                with st.expander(f"Question {i}"):
                    st.write(question)