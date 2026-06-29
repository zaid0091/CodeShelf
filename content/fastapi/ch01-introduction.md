---
title: Introduction to FastAPI
description: Learn about the core features of FastAPI, the difference between ASGI and WSGI architectures, installation, building your first endpoint, and running Uvicorn.
order: 1
tags: [fastapi, python, asgi, uvicorn, installation]
---

# Chapter 1: Introduction to FastAPI

> **Understand ASGI vs. WSGI architectures, install FastAPI, create your first application, and explore the auto-generated documentation.**

---

## Table of Contents

1. [What is FastAPI?](#what-is-fastapi)
2. [ASGI vs WSGI Architecture](#asgi-vs-wsgi-architecture)
3. [Installation](#installation)
4. [Creating Your First API Endpoint](#creating-your-first-api-endpoint)
5. [Running with Uvicorn](#running-with-uvicorn)
6. [Auto-Generated Interactive Documentation](#auto-generated-interactive-documentation)
7. [FastAPI vs Django](#fastapi-vs-django)
8. [Best Practices](#best-practices)
9. [Common Mistakes](#common-mistakes)
10. [Interview Points](#interview-points)
11. [Exercises](#exercises)
12. [Chapter Summary](#chapter-summary)

---

## What is FastAPI?

FastAPI is a modern, high-performance web framework for building APIs with Python 3.9+. It is built on top of two major foundations:
1. **Starlette**: A lightweight ASGI framework/toolkit, which handles routing, middleware, and WebSockets.
2. **Pydantic**: A data validation library that handles data serialization, deserialization, and validation.

### Key Features
*   **High Performance**: On par with NodeJS and Go, thanks to Starlette and async support.
*   **Fast to Code**: Type safety and editor autocomplete reduce development time.
*   **Fewer Bugs**: Auto-validation reduces human errors by up to 40%.
*   **Auto-Docs**: Interactive API documentation (Swagger UI & ReDoc) is generated automatically.

---

## ASGI vs WSGI Architecture

Traditional Python frameworks (like Django and Flask) utilize **WSGI** (Web Server Gateway Interface). Modern async frameworks (like FastAPI) utilize **ASGI** (Asynchronous Server Gateway Interface).

| Metric | WSGI (e.g., Gunicorn + Django) | ASGI (e.g., Uvicorn + FastAPI) |
|--------|------------------------------|------------------------------|
| **Execution Model** | Synchronous, blocking. One thread per request. | Asynchronous, non-blocking. Single-threaded event loop. |
| **Concurrency** | Limited by thread pool size. | High concurrency. Thousands of requests handled concurrently. |
| **Protocols** | Standard HTTP/1.1 only. | HTTP/1.1, HTTP/2, WebSockets, Server-Sent Events (SSE). |
| **Use Case** | CPU-bound or traditional relational DB apps. | I/O-bound (APIs, microservices, real-time chat, scraping). |

---

## Installation

Install `fastapi` and an ASGI server like `uvicorn` (which will run the application):

```bash
pip install fastapi uvicorn
```

---

## Creating Your First API Endpoint

Create a file named `main.py`:

```python
from fastapi import FastAPI

# Initialize the application
app = FastAPI(title="My First FastAPI App")

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/status")
async def get_status():
    return {"status": "healthy", "database": "connected"}
```

---

## Running with Uvicorn

To run the application, execute the following command in your terminal:

```bash
uvicorn main:app --reload
```

### Breakdown of the command:
*   `main`: Refers to the Python file `main.py`.
*   `app`: Refers to the variable `app = FastAPI()` inside that file.
*   `--reload`: Enables hot-reloading (the server restarts automatically when code changes).

Once running, navigate to `http://127.0.0.1:8000/` in your browser to see the JSON output.

---

## Auto-Generated Interactive Documentation

FastAPI automatically generates interactive documentation for your endpoints. You do not need to configure anything.

*   **Swagger UI**: Access at `http://127.0.0.1:8000/docs`. Allows you to test endpoints directly from the browser.
*   **ReDoc**: Access at `http://127.0.0.1:8000/redoc`. A clean, search-optimized representation of your API schema.

---

## FastAPI vs Django

| Feature | Django | FastAPI |
|---------|--------|---------|
| **Philosophy** | Batteries-included (ORM, Admin GUI, Auth, Templates). | Micro-framework (APIs only, select your own DB/auth tools). |
| **Routing & Logic** | Sync by default (async support is secondary). | Native Async first. |
| **Validation** | Django Forms/Serializers (custom structure). | Standard Python Type Hints + Pydantic. |
| **Learning Curve** | High (large codebase, specific architecture). | Low (standard Python, clean code). |

---

## Best Practices

*   **Use `async def` when calling async operations**: Only use `async def` if you are using an asynchronous library (like async database drivers). If your code performs synchronous blocking operations (e.g. `time.sleep()`), define it using standard `def` so FastAPI can run it in a separate thread pool.
*   **Set Page Title and Version**: Provide explicit titles and descriptions to `FastAPI(title="...", description="...")` to make auto-generated docs professional.

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Running Uvicorn in production with `--reload` | High overhead, memory leaks, and performance drop. | Remove `--reload` in production. |
| Blocking the event loop | Using `time.sleep()` in an `async def` function freezes the entire server. | Use `await asyncio.sleep()` or define the route with standard `def`. |

---

## Interview Points

> **📌 Interview Point 1: What makes FastAPI faster than traditional frameworks?**
> FastAPI runs on ASGI (using Starlette and Uvicorn) which allows non-blocking asynchronous request handling. It also uses Pydantic, which compiles fast validation rules based on Python type hints.

> **📌 Interview Point 2: What is the difference between declaring a route with `def` vs `async def` in FastAPI?**
> If you declare a route with standard `def`, FastAPI runs it in an external thread pool to prevent blocking the event loop. If you use `async def`, FastAPI executes it directly on the main event loop, assuming all I/O calls inside use `await`.

---

## Exercises

### Exercise 1: Create a Dynamic Welcome Endpoint ⭐
**Task:** Create a new GET endpoint `/greet` that returns `{"message": "Hello, Developer!"}`. Run uvicorn, open Swagger UI, and test it.

<details>
<summary>💡 Hint (click to reveal)</summary>
Define a new routing function under `app.get("/greet")`.
</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
# Add this to main.py
@app.get("/greet")
def greet_developer():
    return {"message": "Hello, Developer!"}
```
Run `uvicorn main:app --reload` and visit `http://127.0.0.1:8000/docs` to test it.
</details>

---

## Chapter Summary

*   FastAPI is built on **Starlette** (ASGI) and **Pydantic** (Validation).
*   Use **ASGI** servers like Uvicorn to run applications.
*   Get instant interactive Swagger docs at `/docs`.

---

## Previous / Next Chapter

**⬅️ [Previous: Course Overview](./ch00-course-overview.md)**

**➡️ [Next: Path & Query Parameters](./ch02-path-query-parameters.md)**

---

*Chapter 1 of the FastAPI Guide | CodeShelf*
