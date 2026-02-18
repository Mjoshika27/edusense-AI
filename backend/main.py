from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "EduSense AI backend running"}
