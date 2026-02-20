from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "EduSense AI backend running"}
from pydantic import BaseModel

class Topic(BaseModel):
    topic: str

@app.post("/generate-quiz")
def generate_quiz(data: Topic):
    return {
        "topic": data.topic,
        "questions": [
            f"What is {data.topic}?",
            f"Explain {data.topic}",
            f"Why is {data.topic} important?"
        ]
    }
