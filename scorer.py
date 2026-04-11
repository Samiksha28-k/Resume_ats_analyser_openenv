from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def calculate_score(matched, missing, similarity):

    skill_score = (len(matched) / (len(matched) + len(missing) + 1)) * 60
    similarity_score = similarity * 40
    total_score = skill_score + similarity_score

    return round(total_score, 2)


def score_resume(resume_text, job_description):

    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    job_embedding = model.encode(job_description, convert_to_tensor=True)

    similarity = util.cos_sim(resume_embedding, job_embedding)[0][0]

    matched = []
    missing = []

    score = calculate_score(matched, missing, float(similarity))

    return score
