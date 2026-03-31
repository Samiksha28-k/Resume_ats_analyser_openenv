from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
import os
import pdfplumber

from server.skill_matcher import match_skills
from server.scorer import calculate_score
from server.ats_checker import calculate_ats_score
from server.suggestion_engine import get_suggestions

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/analyze", response_class=HTMLResponse)
def analyze(
    request: Request,
    resume: UploadFile = File(...),
    job: str = Form(...)
):

    resume_text = ""

    if resume.filename.endswith(".pdf"):
        with pdfplumber.open(resume.file) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    resume_text += text.lower()

    job_text = job.lower()

    matched_skills, missing_skills, similarity = match_skills(
        resume_text,
        job_text
    )

    score = calculate_score(
        matched_skills,
        missing_skills,
        similarity
    )

    ats_score = calculate_ats_score(resume_text)

    suggestions = get_suggestions(missing_skills)

    result = {
        "score": score,
        "ats_score": ats_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "suggestions": suggestions
    }

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": result
        }
    )


if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)