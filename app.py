from fastapi import FastAPI
from inference import predict

app = FastAPI()

@app.get("/")
def home():
    return {"message": "OpenEnv API Running"}

@app.post("/reset")
def reset():
    return {
        "status": "success",
        "message": "environment reset successful"
    }

@app.get("/state")
def state():
    return {
        "status": "running"
    }

@app.post("/predict")
def predict_api(input_data: dict):
    result = predict(input_data)

    return {
        "status": "success",
        "result": result
    }
