---
title: Django Containerization
description: Complete guide to containerizing Django applications with PostgreSQL, Gunicorn, static file collection, database migrations, and health checks.
order: 5
tags: [docker, django, python, postgres, production]
---

# Chapter 5: Django Containerization

> **Learn how to package Python/Django applications with PostgreSQL, run migrations automatically, serve static assets, and use Gunicorn for production.**

---

## Table of Contents

1. [Django Production Container Architecture](#django-production-container-architecture)
2. [Production Dockerfile for Django](#production-dockerfile-for-django)
3. [Docker Compose for Local Django Development](#docker-compose-for-local-django-development)
4. [Handling Migrations and Static Files](#handling-migrations-and-static-files)
5. [The Database Readiness Problem (Entrypoint Script)](#the-database-readiness-problem-entrypoint-script)
6. [Best Practices](#best-practices)
7. [Common Mistakes](#common-mistakes)
8. [Interview Points](#interview-points)
9. [Exercises](#exercises)
10. [Chapter Summary](#chapter-summary)

---

## Django Production Container Architecture

In production, Django is never served directly with `runserver`. Instead, the stack looks like this:

```text
+-------------------+      Reverse Proxies      +------------------+      WSGI Server      +------------------+
|   Client Browser  |  ---------------------->  |  Nginx Container |  ------------------>  | Gunicorn (Django)|
+-------------------+                           +------------------+                       +------------------+
                                                         |
                                                         | (serves static/media directly)
                                                         v
                                                +------------------+
                                                |  Static Volumes  |
                                                +------------------+
```

1. **Nginx:** Serves static and media files directly from shared volumes and forwards app requests to Gunicorn.
2. **Gunicorn (WSGI Server):** Runs the Python Django application process.
3. **PostgreSQL:** The database container, communicating with Django on a private network.

---

## Production Dockerfile for Django

Here is a robust, secure `Dockerfile` using `python:3.11-slim`. It creates a non-root system user and separates build concerns:

```dockerfile
# ==========================================
# Stage 1: Build virtual environment
# ==========================================
FROM python:3.11-slim AS builder
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies needed to compile Postgres adapters
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies into virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ==========================================
# Stage 2: Final lightweight runtime
# ==========================================
FROM python:3.11-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/opt/venv/bin:$PATH"

# Install postgres runtime client library (libpq)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Copy virtual environment and source code
COPY --from=builder /opt/venv /opt/venv
COPY . .

# Create non-root user for security
RUN useradd -u 8888 django && chown -R django:django /app
USER django

EXPOSE 8000

# Script to wait for db, run migrations, and start Gunicorn
ENTRYPOINT ["/app/entrypoint.sh"]
```

---

## Docker Compose for Local Django Development

For local development, we want hot-reloading (syncing code changes instantly) and standard sqlite/postgres configurations:

```yaml
version: '3.8'

services:
  web:
    build:
      context: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    environment:
      - DB_HOST=db
      - DB_NAME=postgres
      - DB_USER=postgres
      - DB_PASSWORD=devpassword
    depends_on:
      - db

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: postgres
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: devpassword
    volumes:
      - pgdata:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  pgdata:
```

---

## Handling Migrations and Static Files

When deploying a Django container, you must run migrations and compile static assets. 

- **Migrations:** Must run during deployment or runtime initialization. *Never* run migrations during the `docker build` phase because the database container is not accessible during building.
- **Static files:** `python manage.py collectstatic` compiles static files. You can run this during the `docker build` phase since it doesn't require database connections (as long as dummy secret key settings are handled).

---

## The Database Readiness Problem (Entrypoint Script)

If the Django container starts and immediately tries to run migrations before the PostgreSQL database is ready to accept connections, Django will crash.

We solve this using an `entrypoint.sh` startup script:

```bash
#!/bin/sh

# exit immediately if a command exits with a non-zero status
set -e

echo "Waiting for postgres..."

# Loop until port 5432 is responsive on the 'db' host
while ! nc -z $DB_HOST 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

# Apply database migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Start the web server (Gunicorn or runserver depending on command)
exec "$@"
```
> **Note:** Make the script executable on the host before building: `chmod +x entrypoint.sh`.

---

## Best Practices

- **Set `PYTHONUNBUFFERED=1`:** Ensures console logs are flushed immediately to stdout/stderr, so you can see Django errors in real-time using `docker logs`.
- **Use `PYTHONDONTWRITEBYTECODE=1`:** Prevents Python from writing `.pyc` files inside the container, saving space and avoiding file sync noise.

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Running `manage.py runserver` in production | Low performance, lacks security features, crashes under load | Use a production WSGI server like `gunicorn` or ASGI equivalent `uvicorn`. |
| Putting migrations in the Dockerfile | Fails compile time because the database does not exist yet | Always run migrations at runtime using an entrypoint script or CI/CD job. |

---

## Interview Points

> **📌 Interview Point 1: Why shouldn't we run `collectstatic` or migrations in a Dockerfile `RUN` command?**
> Migrations require an active database connection which isn't available during image compilation. `collectstatic` can run in the Dockerfile, but only if Django does not need a DB connection to load settings (or you mock the environment).

> **📌 Interview Point 2: What is the purpose of the `exec "$@"` command at the end of the entrypoint shell script?**
> It replaces the shell process with the main container command (the arguments passed to the container). This ensures that OS signals (like SIGTERM for graceful shutdown) are forwarded directly to Gunicorn instead of being absorbed by the shell script wrapper.

---

## Exercises

### Exercise 1: Write a Django docker-compose command ⭐
**Task:** Write the command to run database migrations inside the running Django container defined in Docker Compose.

<details>
<summary>💡 Hint (click to reveal)</summary>
Use `docker compose exec` followed by the service name (`web`) and the python command.
</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```bash
docker compose exec web python manage.py migrate
```
</details>

---

## Chapter Summary

- **Django in production** should run under Gunicorn/Uvicorn, behind a reverse proxy like Nginx.
- Use **`entrypoint.sh`** to block Django initialization until PostgreSQL is fully listening.
- Avoid running containers as **root** (use `useradd`).

---

## Previous / Next Chapter

**⬅️ [Previous: Docker Compose](./ch04-docker-compose.md)**

**➡️ [Next: React Containerization](./ch06-react-containerization.md)**

---

*Chapter 5 of the Docker & Containerization Guide | CodeShelf*
