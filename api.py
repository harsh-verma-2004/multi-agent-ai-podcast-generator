from fastapi import FastAPI
from datetime import datetime
from podcaster.crew import Podcaster

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Podcast Generator API is running 🚀",
        "usage": "Go to /docs to test the API"
    }

@app.post("/generate-podcast")
def generate_podcast(topic: str):
    inputs = {
        "topic": topic,
        "current_month": str(datetime.now().month),
        "current_year": str(datetime.now().year)
    }

    Podcaster().crew().kickoff(inputs=inputs)

    return {
        "status": "success",
        "message": f"Podcast generated for topic: {topic}"
    }
