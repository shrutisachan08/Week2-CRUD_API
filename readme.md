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

# AI vs Me

## Full AI Prompt

```text
Build a FastAPI Task API that supports CRUD operations on an in-memory list. Include GET, POST, PUT, DELETE endpoints, Pydantic validation, appropriate HTTP status codes, and Swagger documentation.
```

---

## Comparison

### 1. What did the AI do better?

- The AI generated a complete CRUD API in a single response with clean formatting and consistent code style.
- It configured the FastAPI application with metadata such as `title`, `description`, and `version`, making the generated Swagger documentation more polished.
- It consistently used named HTTP status constants (e.g., `status.HTTP_404_NOT_FOUND`) instead of numeric status codes, which improves readability.

---

### 2. What did the AI get wrong or quietly ignore?

- My prompt did not explicitly require endpoint summaries and descriptions, so the AI generated only minimal Swagger documentation, whereas my implementation includes descriptive summaries for every endpoint.
- The AI accepted any non-null string as a task title and did not validate that the title must be non-empty.
- The home (`/`) endpoint returned a generic welcome message instead of listing API information and available endpoints like my implementation.

---

### 3. What did my prompt forget to specify?

While reviewing the AI-generated solution, I realized my prompt did not explicitly mention:

- The exact HTTP status code expected for each endpoint (especially `204 No Content` for DELETE).
- Validation rules such as rejecting empty task titles.
- The exact JSON response format for the home endpoint.
- That every endpoint should include Swagger summaries and descriptions.
- The desired structure of the home endpoint response.

Because these details were missing, the AI made its own implementation decisions.

---

## Improved Prompt

```text
Build a FastAPI Task API using an in-memory list for storage.

Requirements:
- Implement the following endpoints:
  - GET /
  - GET /health
  - GET /tasks
  - GET /tasks/{task_id}
  - POST /tasks
  - PUT /tasks/{task_id}
  - DELETE /tasks/{task_id}
- Use Pydantic for request validation.
- Return appropriate HTTP status codes:
  - 200 OK
  - 201 Created
  - 204 No Content for DELETE
  - 404 Not Found for missing tasks
- Reject empty task titles.
- Add Swagger summaries and descriptions for every endpoint.
- Do not use a database; store tasks only in an in-memory list.
```

---

## One Rematch – What Changed?

After improving the prompt, the regenerated code was closer to my implementation. It included clearer API documentation, followed the required status codes more closely, and better matched the assignment requirements because the prompt removed several ambiguities.

---

## Reflection

Building the API manually before using AI made it much easier to evaluate the generated code. Instead of accepting the AI's solution blindly, I was able to identify missing requirements, compare implementation choices, and understand why certain design decisions were better suited to the assignment. This exercise showed me that the quality of AI-generated code depends heavily on the quality and completeness of the prompt.

# Author

**Shruti Sachan**

B.Tech Electronics & Communication Engineering  
IIITDM Jabalpur

GitHub: https://github.com/<your-username>

---

## License

This project is developed for educational purposes as part of a FastAPI backend assignment.

