def get_ats_report(analysis):
    """
    Returns ATS related information.
    """

    return {
        "ats_score": analysis.get("ats_score", 0),
        "strengths": analysis.get("strengths", []),
        "weaknesses": analysis.get("weaknesses", []),
        "missing_skills": analysis.get("missing_skills", [])
    }