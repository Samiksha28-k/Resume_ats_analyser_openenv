from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', ' ', text)
    return text


def match_skills(resume, job_description):

    resume_text = clean_text(resume)
    job_text = clean_text(job_description)

    resume_words = resume_text.split()
    job_words = job_text.split()

    matched = list(set(resume_words) & set(job_words))
    missing = list(set(job_words) - set(resume_words))

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_text])

    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

    similarity_percent = round(similarity * 100, 2)

    return matched, missing, similarity_percent