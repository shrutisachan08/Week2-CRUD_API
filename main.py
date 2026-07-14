from fastapi import FastAPI,HTTPException
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
@app.get("/")
def home():
    return {
        "name": "FastAPI",
        "version":"1.0",
        "endpoints": ["/tasks"]
    }
@app.get("/health")
def health():
    return{
        "status":"ok"
    }
@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id:int):
    for task in tasks:
        if task["id"]==task_id:
            return task
    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )