---
title: Interview Preparation
description: 15 high-yield interview questions and answers covering FastAPI, async Python, Starlette, Pydantic validation, dependency injection, and deployment strategies.
order: 9
tags: [fastapi, interview-prep, python, async, architecture]
---

# Chapter 9: Interview Preparation

> **Master 15 key questions and answers commonly asked during technical interviews for FastAPI and async Python developer roles.**

---

## 1. What are the core technologies behind FastAPI?
FastAPI is built on top of two major libraries:
*   **Starlette**: A lightweight ASGI framework/toolkit that handles routing, request/response lifecycles, and WebSocket support.
*   **Pydantic**: A data validation and settings management library using Python type annotations. It parses, validates, and serializes request and response data.

---

## 2. What is the difference between ASGI and WSGI?
*   **WSGI (Web Server Gateway Interface)**: A synchronous specification (e.g. Django, Flask). It allocates a thread per request, making it block on slow I/O calls.
*   **ASGI (Asynchronous Server Gateway Interface)**: An asynchronous specification (e.g. FastAPI, Sanic). It runs on a single-threaded event loop (using servers like Uvicorn), handling thousands of concurrent connections concurrently via non-blocking I/O.

---

## 3. When should you use `async def` vs `def` for routes in FastAPI?
*   **Use `async def`**: When calling libraries that support async/await syntax (e.g., async database drivers, HTTPX).
*   **Use `def` (sync)**: When calling blocking libraries or synchronous I/O operations (e.g. `time.sleep()`, synchronous SQLAlchemy, `requests`). FastAPI automatically runs these standard `def` routes in a separate thread pool so they do not block the main event loop.

---

## 4. How does FastAPI validate request data?
FastAPI uses standard Python type hints. When you declare path, query, or body parameters with types (like `int`, `str`, or a Pydantic `BaseModel`), FastAPI automatically:
1. Parses incoming data into the specified type.
2. Returns a `422 Unprocessable Entity` JSON response with detailed error locations if data fails validation.

---

## 5. What is the role of `response_model` in FastAPI route decorators?
The `response_model` argument defines the schema used to format outgoing data:
1. **Filtering**: It strips out sensitive or unwanted fields (like passwords or database IDs) that exist in the database model but are omitted from the response schema.
2. **Validation**: It type-checks outgoing data.
3. **Documentation**: It updates the auto-generated Swagger schema to show the correct output format.

---

## 6. How does Dependency Injection work in FastAPI?
FastAPI uses `Depends()` to inject dependencies. You define a callable (function or class) that returns a resource (like a database session or authorized user), and inject it as a function parameter. FastAPI builds a dependency resolution graph at startup and resolves dependencies before executing the route logic.

---

## 7. How do you handle database connection lifecycles (cleanup) in dependencies?
By using the `yield` keyword instead of `return` in a try-finally block:
```python
async def get_db():
    db = SessionLocal()
    try:
        yield db # Delivers the db session
    finally:
        await db.close() # Closes the session after the request finishes
```
Any exception raised in the route propagates back to the dependency, allowing transactions to roll back in the `finally` block before closure.

---

## 8. What is `APIRouter` and why is it used?
`APIRouter` is a routing class used to split large APIs into smaller, logically separated modules (e.g., grouping `/users` routes in one file and `/items` routes in another). These routers are later registered in the main application instance using `app.include_router()`.

---

## 9. How do you override dependencies during testing?
Use the `app.dependency_overrides` dictionary. During testing, you map the original dependency function to a mock function:
```python
app.dependency_overrides[get_db] = mock_get_db
```
After testing, clear it using `app.dependency_overrides.clear()`.

---

## 10. What is the difference between `model.dict()` and `model.model_dump()`?
*   `model.dict()` is deprecated and was used in **Pydantic v1**.
*   `model.model_dump()` is the standard method in **Pydantic v2** to convert a model instance into a Python dictionary.

---

## 11. How do you handle background tasks in FastAPI?
FastAPI provides a built-in `BackgroundTasks` class. You add a parameter of type `BackgroundTasks` to your route and call `.add_task()`:
```python
from fastapi import BackgroundTasks

@app.post("/send-email")
def send_email(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, "email_sent")
    return {"message": "Notification in progress"}
```
The task runs in a background thread or loop *after* the HTTP response has been sent back to the client.

---

## 12. How do you configure CORS in FastAPI?
By adding `CORSMiddleware` to the application's middleware stack and declaring an explicit list of allowed domains (`allow_origins`):
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 13. What is `pydantic-settings` and why is it preferred for configurations?
`pydantic-settings` is a library that extends Pydantic to read configuration from environment variables and `.env` files. It validates types (e.g., checking if a port is an integer) on application startup, ensuring missing or malformed environment variables crash the app immediately rather than failing silently later.

---

## 14. Why is a combination of Gunicorn and Uvicorn used in production?
*   **Uvicorn** is a high-performance ASGI server, but it lacks advanced process management features.
*   **Gunicorn** is a robust WSGI process manager. By running Gunicorn with Uvicorn worker processes (`uvicorn.workers.UvicornWorker`), you get the best of both: Uvicorn handles the fast async loop, while Gunicorn manages workers, handles failures, and spins up new processes to balance CPU load.

---

## 15. How do you handle HTTP exceptions in FastAPI?
By raising `HTTPException` from `fastapi`:
```python
from fastapi import HTTPException

raise HTTPException(status_code=404, detail="Item not found")
```
This halts further code execution and returns a structured JSON payload with the specified status code to the client.

---

## Next Steps

**⬅️ [Previous: Deployment & Production](./ch08-deployment-best-practices.md)**

**➡️ [Back to Course Overview](./ch00-course-overview.md)**

---

*Chapter 9 of the FastAPI Guide | CodeShelf*
