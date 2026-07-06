from google.adk.agents import Agent

from agent.resume_agent import ResumeReviewAgent


resume_agent = ResumeReviewAgent()


def analyze_resume_tool(resume_text: str):
    """
    Analyze a resume and return a structured report.
    """
    return resume_agent.analyze_resume(resume_text)


root_agent = Agent(
    name="resume_review_agent",
    model="gemini-2.5-flash",
    description="AI Resume Review Agent",
    instruction="""
You are an AI Resume Review Agent.

Whenever the user provides resume text,
use the analyze_resume_tool to generate
a structured ATS report.
""",
    tools=[analyze_resume_tool],
)