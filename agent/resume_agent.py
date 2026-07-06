from google import genai
import os
from agent.prompts import ANALYZE_RESUME_PROMPT
import json
from agent.role_identifier import get_target_role
from agent.ats_analyzer import get_ats_report
from agent.interview_generator import get_interview_questions


class ResumeReviewAgent:

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env file")

        self.client = genai.Client(api_key=api_key)

    def say_hello(self):

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Say hello! You are the AI Resume Review Agent."
        )

        return response.text
    
    def clean_json_response(self, text):

        text = text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "", 1)

        if text.endswith("```"):
            text = text[:-3]

        return text.strip()
    
    def analyze_resume(self, resume_text):

        prompt = ANALYZE_RESUME_PROMPT.format(
            resume=resume_text
        )

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        cleaned_response = self.clean_json_response(
        response.text
        )

        analysis = json.loads(cleaned_response)

        analysis["target_role"] = get_target_role(analysis)

        analysis["ats_report"] = get_ats_report(analysis)

        analysis["interview_questions"] = get_interview_questions(analysis)

        return analysis