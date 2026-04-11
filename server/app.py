from fastapi import FastAPI
from pydantic import BaseModel
from scorer import score_resume

app = FastAPI()


class ResumeRequest(BaseModel):
    resume_text: str
    job_description: str


@app.get("/")
def home():
    return {"message": "Resume ATS Analyser API is running"}


@app.post("/predict")
def predict(data: ResumeRequest):
    score = score_resume(data.resume_text, data.job_description)
    return {"score": score}


# OpenEnv web interface
@app.get("/web")
def web():
    return {
        "message": "Resume ATS Analyser Web Interface Running",
        "endpoint": "/predict"
    }


@app.post("/reset")
def reset():
    return {"status": "reset done"}