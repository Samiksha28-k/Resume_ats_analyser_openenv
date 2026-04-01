from fastapi import FastAPI
<<<<<<< HEAD
from inference import predict

app = FastAPI()

=======
from pydantic import BaseModel
import inference

app = FastAPI()

class InputData(BaseModel):
    resume_text: str = ""
    job_description: str = ""

>>>>>>> d89e674387131ac4a6df1aba512450ec1da38eb1
@app.get("/")
def home():
    return {"message": "OpenEnv API Running"}

@app.post("/reset")
def reset():
<<<<<<< HEAD
    return {"status": "environment reset successful"}

@app.post("/predict")
def predict_api(input_data: dict):
    result = predict(input_data)
    return result
=======
    return inference.reset_env()

@app.post("/predict")
def predict(data: InputData):
    return inference.predict(data.dict())
>>>>>>> d89e674387131ac4a6df1aba512450ec1da38eb1
