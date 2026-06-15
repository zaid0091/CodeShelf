---
title: Multi-Stage Builds
description: Master multi-stage builds to dramatically reduce image size and improve container security in production.
order: 3
tags: [docker, multi-stage, optimization, security]
---

# Chapter 3: Multi-Stage Builds

> **Dramatically optimize your production images by separating the build-time environment from the runtime environment.**

---

## Table of Contents

1. [The Problem with Single-Stage Builds](#the-problem-with-single-stage-builds)
2. [What is a Multi-Stage Build?](#what-is-a-multi-stage-build)
3. [Multi-Stage Build Syntax](#multi-stage-build-syntax)
4. [Standard Multi-Stage Template: React (Vite)](#standard-multi-stage-template-react-vite)
5. [Standard Multi-Stage Template: Python (Django)](#standard-multi-stage-template-python-django)
6. [Why Multi-Stage Builds Improve Security](#why-multi-stage-builds-improve-security)
7. [Best Practices](#best-practices)
8. [Common Mistakes](#common-mistakes)
9. [Interview Points](#interview-points)
10. [Exercises](#exercises)
11. [Chapter Summary](#chapter-summary)

---

## The Problem with Single-Stage Builds

In a single-stage build, all tools required to build or compile your code (such as Node.js, devDependencies, gcc, git, build utilities) remain in the final image. 

For example, when building a React app, you need Node.js to download `node_modules` and run `npm run build` to compile the app into static HTML, JS, and CSS. However, at runtime, all you need is a web server (like Nginx) to serve those static files. Having Node.js and a 500MB `node_modules` directory in production is a waste of space and a security risk.

---

## What is a Multi-Stage Build?

> **Definition:** Multi-stage builds utilize multiple `FROM` instructions in a single Dockerfile. Each `FROM` begins a new stage of the build using a different base image. You can selectively copy files (artifacts) from one stage to another, leaving behind everything you don't need.

---

## Multi-Stage Build Syntax

We define stages by naming them using `AS <name>` in the `FROM` instruction, then copying files from that stage using the `--from=<name>` flag:

```dockerfile
# Stage 1: Build-stage
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build # Outputs files to /app/dist

# Stage 2: Production-stage
FROM nginx:alpine
# Copy compiled build output from the builder stage
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

---

## Standard Multi-Stage Template: React (Vite)

In this layout, Node.js compiles the code, and Nginx serves it. The final image size drops from **~800MB** (Node container with source files) to **~25MB** (Nginx + static HTML/JS/CSS).

```dockerfile
# ==========================================
# Stage 1: Compile application source code
# ==========================================
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci --silent
COPY . .
RUN npm run build

# ==========================================
# Stage 2: Serve application static assets
# ==========================================
FROM nginx:1.25-alpine
# Copy production build folder
COPY --from=build /app/dist /usr/share/nginx/html
# Copy custom Nginx configuration (handles client routing)
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

---

## Standard Multi-Stage Template: Python (Django)

In Python, we compile wheels and install dependencies in a build stage, then copy the virtual environment to a clean runtime stage. This leaves behind headers and compilation packages like `gcc`.

```dockerfile
# ==========================================
# Stage 1: Build dependencies
# ==========================================
FROM python:3.11-slim AS builder
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# ==========================================
# Stage 2: Final lightweight runtime
# ==========================================
FROM python:3.11-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy wheels and install them from builder stage
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache --no-dir /wheels/*

COPY . .
EXPOSE 8000
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
```

---

## Why Multi-Stage Builds Improve Security

- **Smaller Attack Surface:** With fewer packages, there are fewer dependencies that could have security vulnerabilities (CVEs).
- **No Compilers in Production:** If an attacker exploits your web application, they will not have compilers (like `gcc`, `make`) or command-line utilities (like `git`) inside the container to compile malicious payloads.
- **Hidden Source Code:** For compiled languages (Go, Java) or build assets (React), the original source code is completely omitted from the final running image.

---

## Best Practices

- **Name your stages:** Use `AS builder` or `AS build` instead of using indexes like `--from=0`. It makes Dockerfiles readable and easier to maintain.
- **Stop at a specific stage:** You can build up to a specific stage for debugging or development purposes:
  ```bash
  docker build --target builder -t my-app:dev .
  ```

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Copying too much from the builder stage | Defeats the purpose of the multi-stage build, bloating size | Only copy the built assets or binaries (`dist`, `build`, `.venv`, etc.). |
| Missing runtime libraries | Rebuilt wheels or executables might fail if system dependencies (e.g. `libpq-dev` equivalent runtime libraries) are missing in the final stage | Ensure shared system libraries (like `libpq` for Postgres) are installed in the final stage. |

---

## Interview Points

> **📌 Interview Point 1: What is the main advantage of a multi-stage Docker build?**
> It allows you to build highly optimized, secure, and small production images by separating the build toolchain from the runtime environment.

> **📌 Interview Point 2: How do you copy files from a stage in a multi-stage build?**
> You name the source stage with `AS stage_name` in the `FROM` instruction, and then use `COPY --from=stage_name /src/path /dest/path` in the subsequent stage.

> **📌 Interview Point 3: Can you copy files from external images in a COPY instruction?**
> Yes! You can use `--from` with an external image name:
> `COPY --from=rclone/rclone:latest /usr/local/bin/rclone /usr/local/bin/rclone`

---

## Exercises

### Exercise 1: Build a Go Application using Multi-Stage Builds ⭐⭐
**Task:** Write a Dockerfile for a Go application. Stage 1 should use `golang:1.21-alpine` to compile the app (`go build -o server .`). Stage 2 should use `alpine:latest` to run the compiled `server` executable.

<details>
<summary>💡 Hint (click to reveal)</summary>
Name the first stage `builder`. In the second stage, copy the `/app/server` file from `builder` to `/bin/server`.
</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```dockerfile
# Stage 1: Build binary
FROM golang:1.21-alpine AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN go build -o server .

# Stage 2: Lightweight runtime
FROM alpine:latest
WORKDIR /root/
COPY --from=builder /app/server .
EXPOSE 8080
CMD ["./server"]
```
</details>

---

## Chapter Summary

- **Multi-stage builds** use multiple `FROM` instructions.
- They allow you to compile assets in a fully-equipped **build stage** and run them in a clean, minimal **runtime stage**.
- This yields smaller, faster-to-deploy, and more secure production images.

---

## Previous / Next Chapter

**⬅️ [Previous: Dockerfile Fundamentals](./ch02-dockerfile-fundamentals.md)**

**➡️ [Next: Docker Compose](./ch04-docker-compose.md)**

---

*Chapter 3 of the Docker & Containerization Guide | CodeShelf*
