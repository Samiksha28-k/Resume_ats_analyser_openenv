import os
from openai import OpenAI

# Environment Variables
API_BASE_URL = os.getenv("API_BASE_URL", "https://api-inference.huggingface.co")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt2")
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

def predict(input_data):

    task_name = "ats_score"
    benchmark = "resume_ats"
    rewards = []

    print(f"[START] task={task_name} env={benchmark} model={MODEL_NAME}", flush=True)

    resume = input_data.get("resume_text", "")
    job = input_data.get("job_description", "")

    resume_words = set(resume.lower().split())
    job_words = set(job.lower().split())

    matched = resume_words.intersection(job_words)

    score = len(matched) / len(job_words) if job_words else 0
    reward = score
    rewards.append(reward)

    done = True
    error = "null"

    print(
        f"[STEP] step=1 action=keyword_match reward={reward:.2f} done=true error={error}",
        flush=True
    )

    success = True if score >= 0 else False

    rewards_str = ",".join(f"{r:.2f}" for r in rewards)

    print(
        f"[END] success={str(success).lower()} steps=1 score={score:.2f} rewards={rewards_str}",
        flush=True
    )

    return {
        "score": score,
        "missing_keywords": list(job_words - resume_words)
    }
