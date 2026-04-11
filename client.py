import requests

BASE_URL = "https://sam28ksha-resume-ats-analyser-openenv.hf.space"

def reset():
    response = requests.post(f"{BASE_URL}/reset")
    return response.json()

def predict(resume_text, job_description):
    data = {
        "resume_text": resume_text,
        "job_description": job_description
    }

    response = requests.post(
        f"{BASE_URL}/predict",
        json=data
    )

    return response.json()


if __name__ == "__main__":
    print("Reset:", reset())

    result = predict(
        "Python developer with FastAPI and ML experience",
        "Looking for Python FastAPI developer"
    )

    print("Prediction:", result)