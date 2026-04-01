# inference.py

import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -------- Clean Text --------
def clean_text(text):
    if text is None:
        return ""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', ' ', text)
    return text


# -------- ATS Score --------
def calculate_ats_score(resume_text, job_description):

    resume = clean_text(resume_text)
    jd = clean_text(job_description)

    if resume.strip() == "" or jd.strip() == "":
        return 0

    text = [resume, jd]

    cv = CountVectorizer()
    matrix = cv.fit_transform(text)

    similarity = cosine_similarity(matrix)[0][1]

    ats_score = round(similarity * 100, 2)

    return ats_score


# -------- Missing Keywords --------
def missing_keywords(resume_text, job_description):

    resume_words = set(clean_text(resume_text).split())
    jd_words = set(clean_text(job_description).split())

    missing = jd_words - resume_words

    return list(missing)[:20]


# -------- Reset --------
def reset_env():
    return {
        "status": "environment reset successful"
    }


# -------- Predict --------
def predict(data):

    try:

        resume_text = data.get("resume_text", "")
        job_description = data.get("job_description", "")

        score = calculate_ats_score(resume_text, job_description)

        missing = missing_keywords(resume_text, job_description)

        return {
            "ATS_score": score,
            "missing_keywords": missing,
            "message": "prediction successful"
        }

    except Exception as e:
        return {
            "ATS_score": 0,
            "missing_keywords": [],
            "message": str(e)
        }
