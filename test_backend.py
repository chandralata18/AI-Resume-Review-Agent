# import os
# import google.generativeai as genai
# from dotenv import load_dotenv

# load_dotenv()

# api_key = os.getenv("GEMINI_API_KEY")

# genai.configure(api_key=api_key)

# model = genai.GenerativeModel("gemini-2.5-flash")

# response = model.generate_content(
#     "Say hello to my AI Resume Review Agent project."
# )

# print(response.text) 



# import os

# from dotenv import load_dotenv

# from agent.resume_agent import ResumeAgent


# load_dotenv()


# agent = ResumeAgent()

# print(agent.say_hello())



# from tools.pdf_reader import PDFReader

# reader = PDFReader()

# resume = reader.extract_text("resumes/sample_resume.pdf")

# print(resume)


from dotenv import load_dotenv

from tools.pdf_reader import PDFReader
from agent.resume_agent import ResumeReviewAgent

load_dotenv()

reader = PDFReader()
agent = ResumeReviewAgent()

resume_text = reader.extract_text(
    "resumes/sample_resume.pdf"
)

analysis = agent.analyze_resume(
    resume_text
)

#print(analysis)

print(type(analysis))

print()

print(analysis)