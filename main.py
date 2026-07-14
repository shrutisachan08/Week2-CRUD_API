from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel
app=FastAPI()
tasks=[
    {
        "id":1,
        "title":"study FastAPI",
        "done":False
    },
    {
        "id":2,
        "title":"Complete Assignment",
        "done":False
    },
    {
        "id":3,
        "title":"Go for a walk",
        "done":True
    }
]
class Task(BaseModel):
    title:str
    done:bool
@app.get("/",summary="Home",
    description="Returns API information.")
def home():
    return {
        "name": "FastAPI",
        "version":"1.0",
        "endpoints": ["/tasks"]
    }
@app.get("/health",
    summary="Health Check",
    description="Checks if the API is running.")
def health():
    return{
        "status":"ok"
    }
@app.get("/tasks",
    summary="Get all tasks",
    description="Returns a list of all tasks.")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}",
    summary="Get task by ID",
    description="Returns a single task by its ID.")
def get_task(task_id:int):
    for task in tasks:
        if task["id"]==task_id:
            return task
    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
@app.post("/tasks",status_code=status.HTTP_201_CREATED,   summary="Create a task",
    description="Creates a new task.")
def create_task(task:Task):
    new_task={
        "id":len(tasks)+1,
        "title":task.title,
        "done":task.done
    }
    tasks.append(new_task)
    return new_task

@app.put("/tasks/{task_id}" ,summary="Update task",
    description="Updates an existing task.")
def update_task(task_id:int,updated_task:Task):
    for task in tasks:
        if task["id"]==task_id:
            task["title"]=updated_task.title
            task["done"]=updated_task.done
            return task
    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT,summary="Delete task",
    description="Deletes a task.")
def delete_task(task_id:int):
    for task in tasks:
        if task["id"]==task_id:
            tasks.remove(task)
            return
    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )