
from fastapi import FastAPI,status
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to TeamFlow API"}

# Define the structure of a task
class Task(BaseModel):
    title: str
    description: str
    completed: bool = False


# Create a new task
@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: Task):

    return {
        "message": "Task created successfully",
        "task": task
    }
