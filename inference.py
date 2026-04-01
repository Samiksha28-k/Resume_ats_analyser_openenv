import pdfplumber
import docx
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    return text


def calculate_ats_score(resume_text, job_description):
    resume = clean_text(resume_text)
    jd = clean_text(job_description)

    text = [resume, jd]

    cv = CountVectorizer()
    matrix = cv.fit_transform(text)

    similarity = cosine_similarity(matrix)[0][1]

    ats_score = round(similarity * 100, 2)

    return ats_score


def reset_env():
    return {"status": "reset successful"}


def predict(data):
    
    resume_text = data.get("resume_text", "")
    job_description = data.get("job_description", "")

    score = calculate_ats_score(resume_text, job_description)

    return {
        "ATS_score": score,
        "message": "prediction successful"
    }
