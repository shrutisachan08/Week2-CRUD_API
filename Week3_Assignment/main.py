from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel
import sqlite3
conn=sqlite3.connect("tasks.db",check_same_thread=False)
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY,
    title TEXT,
    done BOOLEAN
)""")
conn.commit()
cursor.execute("SELECT COUNT(*) FROM tasks")
count=cursor.fetchone()[0]
if count==0:
    cursor.executemany(
        "INSERT INTO tasks (title,done) VALUES (?,?)",
        [
            ("Study FastAPI",False),
            ("Complete Assignment",False),
            ("Go For a walk",True)
            
        ]
    )
    conn.commit()
app=FastAPI()
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
    cursor.execute("SELECT * from tasks")
    rows=cursor.fetchall()
    tasks=[]
    for row in rows:
        tasks.append({
            "id":row[0],
            "title":row[1],
            "done":bool(row[2])
        })
    return tasks

@app.get("/tasks/{task_id}",
    summary="Get task by ID",
    description="Returns a single task by its ID.")
def get_task(task_id:int):
    cursor.execute("SELECT * FROM tasks where id=?",
    (task_id,)               
    )
    row=cursor.fetchone()
    if row is None:
        raise HTTPException(
            status_code=404,
            detail="task not found"
        )
    return{
        "id":row[0],
        "title":row[1],
        "done":bool(row[2])
    }
@app.post("/tasks",status_code=status.HTTP_201_CREATED,   summary="Create a task",
    description="Creates a new task.")
def create_task(task:Task):
   cursor.execute("INSERT INTO tasks (title,done) VALUES (?,?)",
    (task.title,task.done)              
    )
   conn.commit()
   task_id=cursor.lastrowid
   return {
       "id":task_id,
       "title":task.title,
       "done":task.done
   }
@app.put("/tasks/{task_id}" ,summary="Update task",
    description="Updates an existing task.")
def update_task(task_id:int,updated_task:Task):
    cursor.execute("UPDATE tasks SET title=?,done=? WHERE id=?",
    (updated_task.title,updated_task.done,task_id)
    )
    conn.commit()
    if cursor.rowcount==0:
        raise HTTPException(
            status_code=404,
            detail="task not found"
        )
    return {
        "id":task_id,
        "title":updated_task.title,
        "done":updated_task.done
        }
@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT,summary="Delete task",
    description="Deletes a task.")
def delete_task(task_id:int):
   cursor.execute("DELETE FROM tasks WHERE id=?",
    (task_id,)              
    )
   conn.commit()
   if cursor.rowcount==0:
       raise HTTPException(
           status_code=404,
           detail="Task not found"
       )