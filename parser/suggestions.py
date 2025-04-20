def suggest_improvements(info):
    suggestions = []

    if len(info["Skills"]) < 5:
        suggestions.append("Consider adding more technical or soft skills.")
    if not any("Python" in s for s in info["Skills"]):
        suggestions.append("Adding Python as a skill can be beneficial.")
    if len(info["Education"]) == 0:
        suggestions.append("Add at least one educational qualification.")
    if len(info["Experience"]) == 0:
        suggestions.append("Add past work or internship experience to strengthen your resume.")
    if info["Phone"] == "Not found":
        suggestions.append("Include a reachable phone number.")
    if info["Email"] == "Not found":
        suggestions.append("Include a valid email address.")

    return suggestions if suggestions else ["Your resume looks good! Just keep it updated."]
