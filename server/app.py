from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Resume ATS Analyser Running"}

@app.post("/predict")
def predict():
    return {"score": 85}

@app.post("/reset")
def reset():
    return {"message": "reset done"}
