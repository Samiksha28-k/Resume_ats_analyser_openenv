from fastapi import FastAPI
import uvicorn

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


def main():
    uvicorn.run(
        "server.app:app",
        host="0.0.0.0",
        port=7860,
        reload=False
    )


if __name__ == "__main__":
    main()
