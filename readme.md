# Task API using FastAPI

A simple RESTful Task Management API built using **FastAPI**. This project demonstrates the implementation of CRUD (Create, Read, Update, Delete) operations using an in-memory data structure and automatic API documentation with Swagger UI.

## Features

- FastAPI-based REST API
- CRUD operations for tasks
- Automatic Swagger/OpenAPI documentation
- Request validation using Pydantic
- Proper HTTP status codes
- Health check endpoint

---

## Tech Stack

- **Python 3**
- **FastAPI**
- **Uvicorn**
- **Pydantic**

---

## Project Structure

```text
task-api/
│── main.py          # FastAPI application
│── README.md        # Project documentation
│── requirements.txt # Project dependencies (optional)
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/task-api.git
```

### 2. Navigate to the project

```bash
cd task-api
```

### 3. Create a virtual environment (Recommended)

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install fastapi uvicorn
```

---

## Running the API

Start the development server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

## API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# API Endpoints

| Method | Endpoint | Description | Success Status |
|----------|-----------------|--------------------------|---------------|
| GET | `/` | API information | 200 OK |
| GET | `/health` | Health check | 200 OK |
| GET | `/tasks` | Get all tasks | 200 OK |
| GET | `/tasks/{task_id}` | Get task by ID | 200 OK |
| POST | `/tasks` | Create a new task | 201 Created |
| PUT | `/tasks/{task_id}` | Update an existing task | 200 OK |
| DELETE | `/tasks/{task_id}` | Delete a task | 204 No Content |

---

# Sample Request

### Create Task

**POST** `/tasks`

```json
{
    "title": "Learn FastAPI",
    "done": false
}
```

### Response

```json
{
    "id": 4,
    "title": "Learn FastAPI",
    "done": false
}
```

---

# Example cURL Commands

### Get all tasks

```bash
curl -i http://127.0.0.1:8000/tasks
```

### Get task by ID

```bash
curl -i http://127.0.0.1:8000/tasks/1
```

### Create a task

```bash
curl -i -X POST http://127.0.0.1:8000/tasks ^
-H "Content-Type: application/json" ^
-d "{\"title\":\"Learn FastAPI\",\"done\":false}"
```

### Update a task

```bash
curl -i -X PUT http://127.0.0.1:8000/tasks/1 ^
-H "Content-Type: application/json" ^
-d "{\"title\":\"Learn Backend\",\"done\":true}"
```

### Delete a task

```bash
curl -i -X DELETE http://127.0.0.1:8000/tasks/1
```

---

# Swagger UI

After running the application, open:

```
http://127.0.0.1:8000/docs
```

Replace the section below with a screenshot of your Swagger UI.

```
docs/swagger-ui.png
```

---

# HTTP Status Codes Used

| Status Code | Meaning |
|--------------|---------|
| 200 | Request successful |
| 201 | Resource created successfully |
| 204 | Resource deleted successfully (No Content) |
| 404 | Task not found |

---

# Future Improvements

- SQLite / PostgreSQL integration
- Persistent data storage
- User authentication
- Pagination and filtering
- Unit testing with Pytest
- Docker support
- Deployment on Render/Railway

---

# Author

**Shruti Sachan**

B.Tech Electronics & Communication Engineering  
IIITDM Jabalpur

GitHub: https://github.com/<your-username>

---

## 📄 License

This project is developed for educational purposes as part of a FastAPI backend assignment.