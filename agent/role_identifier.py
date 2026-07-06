def get_target_role(analysis):
    """
    Returns the detected target role.
    """

    return analysis.get("target_role", "Unknown")