import os

API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

def predict(input_data):

    print("[START] ATS Prediction")

    resume = input_data.get("resume_text", "")
    job = input_data.get("job_description", "")

    resume_words = set(resume.lower().split())
    job_words = set(job.lower().split())

    matched = resume_words.intersection(job_words)

    score = len(matched) / len(job_words) if job_words else 0

    missing = list(job_words - resume_words)

    print("[STEP] Matching completed")
    print("[END] Prediction finished")

    return {
        "score": score,
        "missing_keywords": missing
    }
