# Resume ATS Analyzer - OpenEnv API

This project is built for Meta PyTorch OpenEnv Hackathon.

It provides an API that analyzes resume text and job description and returns ATS score and missing keywords.

## Features

- ATS Score Calculation
- Missing Keywords Detection
- FastAPI based API
- Docker container support
- OpenEnv compatible

## API Endpoints

### Home

GET /

Response:

{
  "message": "OpenEnv API Running"
}

### Reset

POST /reset

Response:

{
  "status": "environment reset successful"
}

### Predict

POST /predict

Input:

{
  "resume_text": "python machine learning data analysis",
  "job_description": "python deep learning data analysis"
}

Output:

{
  "ATS_score": 75.5,
  "missing_keywords": ["deep", "learning"],
  "message": "prediction successful"
}

## Tech Stack

- Python
- FastAPI
- Scikit-learn
- Docker

## Author

Samiksha Sengar
