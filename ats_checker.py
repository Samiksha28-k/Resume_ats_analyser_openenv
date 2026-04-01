def calculate_ats_score(resume):

    keywords = [
        "experience",
        "project",
        "skills",
        "education",
        "internship",
        "certification"
    ]

    resume_text = resume.lower()

    score = 0

    for word in keywords:
        if word in resume_text:
            score += 10

    return score