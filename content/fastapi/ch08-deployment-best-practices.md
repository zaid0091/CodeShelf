---
title: Deployment & Production Best Practices
description: Structure large FastAPI applications using APIRouter, manage configuration with pydantic-settings, set up CORS, write production Dockerfiles, and configure Uvicorn/Gunicorn.
order: 8
tags: [fastapi, production, docker, apirouter, deployment, uvicorn, config]
---

# Chapter 8: Deployment & Production Best Practices

> **Structure large codebases with APIRouter, configure application settings, secure CORS, package with Docker, and run ASGI servers under production constraints.**

---

## Table of Contents

1. [Structuring Large Applications (APIRouter)](#structuring-large-applications-apirouter)
2. [Configuration Management (Pydantic Settings)](#configuration-management-pydantic-settings)
3. [CORS (Cross-Origin Resource Sharing)](#cors-cross-origin-resource-sharing)
4. [Running Under Production Servers](#running-under-production-servers)
5. [Dockerizing FastAPI](#dockerizing-fastapi)
6. [Best Practices](#best-practices)
7. [Common Mistakes](#common-mistakes)
8. [Interview Points](#interview-points)
9. [Exercises](#exercises)
10. [Chapter Summary](#chapter-summary)

---

## Structuring Large Applications (APIRouter)

For small apps, a single `main.py` is fine. As the codebase grows, split routes into modules using `APIRouter` to maintain readability:

```text
my_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── routers/
│   │   ├── users.py
│   │   └── items.py
│   └── models/
│       ├── user.py
│       └── item.py
```

### Example: Declaring sub-routes inside `app/routers/users.py`:
```python
from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/")
def list_users():
    return [{"username": "alice"}]
```

### Example: Mounting routers inside `app/main.py`:
```python
from fastapi import FastAPI
from app.routers import users

app = FastAPI()

# Include sub-routes
app.include_router(users.router)
```

---

## Configuration Management (Pydantic Settings)

Manage application settings and read `.env` configurations safely using `pydantic-settings`.

```bash
pip install pydantic-settings
```

Create a `config.py` file:

```python
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "FastAPI App"
    admin_email: str
    database_url: str
    secret_key: str

    # Read from a .env file if available
    model_config = SettingsConfigDict(env_file=".env")

# Instantiate settings
settings = Settings()
```

---

## CORS (Cross-Origin Resource Sharing)

If a frontend application (e.g. React/Vite running on port `5173`) requests data from your API (running on port `8000`), the browser blocks it unless CORS is enabled.

Enable CORS via middleware inside `main.py`:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173", # React app
    "https://myproductiondomain.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allow all methods (GET, POST, PUT, etc.)
    allow_headers=["*"], # Allow all headers
)
```

---

## Running Under Production Servers

Do not use `uvicorn main:app --reload` in production. Instead, configure multiple worker processes. A common setup uses **Gunicorn** to manage workers, and **Uvicorn** to run the ASGI loop inside them.

```bash
pip install gunicorn
```

Run from terminal:
```bash
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000
```
*   `-w 4`: Runs 4 worker processes.
*   `-k uvicorn.workers.UvicornWorker`: Instructs Gunicorn to use Uvicorn class workers.

---

## Dockerizing FastAPI

Create a multi-stage production-ready `Dockerfile`:

```dockerfile
# Stage 1: Build
FROM python:3.11-slim AS builder

WORKDIR /app

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final lightweight image
FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy source code
COPY . .

# Create a non-privileged system user for security
RUN useradd -u 8888 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

CMD ["gunicorn", "main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000"]
```

---

## Best Practices

*   **Prefix router paths**: Always use the `prefix` argument in `APIRouter` (e.g., `prefix="/items"`) rather than writing it in every route path.
*   **Tags**: Group routes using `tags` so they appear clustered together in the Swagger documentation.
*   **Keep docker images small**: Use `python-slim` base images and separate dependencies build steps to keep sizes minimal.

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Allowing `allow_origins=["*"]` in production with credentials enabled | Security risk (cross-site credential leaks) | List explicit domain origins in production. |
| Hardcoding settings variables | Harder to scale or swap configuration across staging environments | Use `BaseSettings` to load environment variables dynamically. |

---

## Interview Points

> **📌 Interview Point 1: What is the purpose of Gunicorn when Uvicorn is already running?**
> Gunicorn acts as a process manager. It monitors worker health, handles restarts, and routes incoming sockets. Uvicorn executes the actual ASGI asynchronous loop inside those workers.

> **📌 Interview Point 2: How do you handle configuration validation in FastAPI?**
> By using Pydantic's `BaseSettings`. On initialization, it automatically reads environment variables, type-checks them, and throws a validation error on startup if variables are missing or incorrect.

---

## Exercises

### Exercise 1: Create a scoped APIRouter ⭐
**Task:** Create a router file `items.py` with a prefix `/items` containing a GET route `/` returning list of items. Register it in `main.py`.

<details>
<summary>💡 Hint (click to reveal)</summary>
Instantiate `APIRouter(prefix="/items")` and run `app.include_router(items_router)` in `main.py`.
</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
# app/routers/items.py
from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/")
def get_items():
    return [{"item_name": "Book"}]

# app/main.py
from fastapi import FastAPI
from app.routers import items

app = FastAPI()
app.include_router(items.router)
```
</details>

---

## Chapter Summary

*   Organize endpoints using `APIRouter` structures.
*   Validate configurations and load environment files with `BaseSettings`.
*   Wrap FastAPI using multi-stage lightweight Dockerfiles.

---

## Previous / Next Chapter

**⬅️ [Previous: Testing FastAPI Applications](./ch07-testing-fastapi.md)**

**➡️ [Next: Interview Preparation](./ch09-interview-prep.md)**

---

*Chapter 8 of the FastAPI Guide | CodeShelf*
