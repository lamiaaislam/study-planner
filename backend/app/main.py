from fastapi import FastAPI

app = FastAPI(
    title="Study Planner API",
    description="Backend API for the Study Planner application.",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Study Planner API is running!"
    }