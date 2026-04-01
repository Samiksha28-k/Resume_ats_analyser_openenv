from fastapi import FastAPI
from inference import predict

app = FastAPI()

@app.get("/")
def home():
    return {"message": "OpenEnv API Running"}

@app.post("/reset")
def reset():
    return {"status": "environment reset successful"}

@app.post("/predict")
def predict_api(input_data: dict):
    result = predict(input_data)
    return result