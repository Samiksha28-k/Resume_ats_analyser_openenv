from fastapi import FastAPI
from pydantic import BaseModel
import inference

app = FastAPI()


class InputData(BaseModel):
    resume_text: str = ""
    job_description: str = ""


@app.get("/")
def home():
    return {"message": "OpenEnv API Running"}


@app.post("/reset")
def reset():
    return {"status": "reset successful"}


@app.post("/predict")
def predict(data: InputData):
    return inference.predict(data.dict())
