---
title: Dockerfile Fundamentals
description: Understand Dockerfile instructions, layered architecture, build caching, base images, and optimization strategies.
order: 2
tags: [docker, dockerfile, architecture, caching]
---

# Chapter 2: Dockerfile Fundamentals

> **Learn how to build your own custom Docker images from scratch, write efficient Dockerfiles, and leverage build caching.**

---

## Table of Contents

1. [What is a Dockerfile?](#what-is-a-dockerfile)
2. [Essential Dockerfile Instructions](#essential-dockerfile-instructions)
3. [CMD vs ENTRYPOINT](#cmd-vs-entrypoint)
4. [COPY vs ADD](#copy-vs-add)
5. [Layered Architecture and Build Caching](#layered-architecture-and-build-caching)
6. [Choosing the Right Base Image](#choosing-the-right-base-image)
7. [Best Practices](#best-practices)
8. [Common Mistakes](#common-mistakes)
9. [Interview Points](#interview-points)
10. [Exercises](#exercises)
11. [Chapter Summary](#chapter-summary)

---

## What is a Dockerfile?

> **Definition:** A Dockerfile is a text document containing a sequential list of instructions used by the Docker client to assemble a Docker image.

### Why it matters

Instead of manually configuring a server, a Dockerfile defines your environment as code. This makes the environment entirely reproducible and shareable across your team.

---

## Essential Dockerfile Instructions

Here is a standard Dockerfile for a Node/Express application:

```dockerfile
# 1. Base image
FROM node:20-alpine

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy package files first (for dependency caching)
COPY package*.json ./

# 4. Run commands (installs dependencies)
RUN npm install

# 5. Copy the rest of the application files
COPY . .

# 6. Set environment variables
ENV PORT=8080

# 7. Document the container port
EXPOSE 8080

# 8. Default execution command
CMD ["node", "src/index.js"]
```

### Key Instructions Explained

- **`FROM`:** Initializes a new build stage and sets the Base Image.
- **`WORKDIR`:** Sets the directory where all subsequent `RUN`, `CMD`, `ENTRYPOINT`, `COPY`, and `ADD` instructions will be executed.
- **`COPY`:** Copies local files from the host into the container's filesystem.
- **`RUN`:** Executes commands *during* the image build process (creates a new layer).
- **`ENV`:** Defines environment variables accessible during both build and runtime.
- **`EXPOSE`:** Acts as documentation, informing users which ports the container intends to listen on.
- **`CMD`:** Defines the default command to execute when the container is *run*.

---

## CMD vs ENTRYPOINT

Both instructions define the container startup command, but they behave differently when arguments are passed:

| Instruction | Behavior | Overridability |
|-------------|----------|----------------|
| **`CMD`** | Sets default command and arguments. Can be overridden completely by CLI arguments. | Easily overridden: `docker run image echo "hello"` overrides `CMD`. |
| **`ENTRYPOINT`** | Sets the main executable. Arguments passed at run-time are appended to it. | Harder to override. Requires `--entrypoint` flag. |

### Recommended Pattern: Combined Usage
Use `ENTRYPOINT` to define the binary and `CMD` for the default flags/arguments.

```dockerfile
ENTRYPOINT ["ping"]
CMD ["localhost"]
```
Running `docker run my-image` executes `ping localhost`.
Running `docker run my-image google.com` executes `ping google.com` (overriding the `CMD` argument).

---

## COPY vs ADD

| Command | Usage | Feature Set | Recommendation |
|---------|-------|-------------|----------------|
| **`COPY`** | Copies local files/folders. | Basic, secure file copy. | **Use by default** for all files. |
| **`ADD`** | Copies local files, remote URLs, and auto-extracts `.tar` archives. | Remote downloading, auto-unpacking. | Only use when you explicitly need to auto-extract local `.tar` archives into the image. |

---

## Layered Architecture and Build Caching

Docker images are made of read-only stackable layers. Each instruction in a Dockerfile creates a layer:

```text
+------------------------------------+
|  Writeable Container Layer         | (Added when running the container)
+------------------------------------+
|  Layer 4: CMD ["node", "index.js"] | (Dockerfile line)
+------------------------------------+
|  Layer 3: COPY . .                 | (Dockerfile line)
+------------------------------------+
|  Layer 2: RUN npm install          | (Dockerfile line)
+------------------------------------+
|  Layer 1: Base node:20-alpine      | (From base image)
+------------------------------------+
```

### Build Caching Rule
Docker caches layers during a build. If an instruction's dependencies change (e.g., source files modified), that instruction's cache and all subsequent layers' caches are invalidated.

**Optimization Trick:** Copy package configuration files and install dependencies *before* copying the application source code. Because source code changes frequently but dependencies do not, this avoids running slow installs on every build.

---

## Choosing the Right Base Image

Choosing the base image dictates your image's size, security surface, and package compatibility:

1. **Ubuntu/Debian (`python:3.11` or `node:20`):** Full OS environment. Large size (800MB+), but highly compatible and contains debugging tools.
2. **Slim (`python:3.11-slim`):** Stripped-down version of Debian. Small (150MB+), faster builds, ideal for python backend deployments.
3. **Alpine (`node:20-alpine`):** Security-focused, extremely lightweight Linux distribution (5MB base size). Excellent for Node/React, but uses `musl libc` which can cause compilation issues in some Python/compiled languages.
4. **Distroless:** Contains only your application and runtime dependencies. No shell, package managers, or common utilities. Highly secure but harder to debug.

---

## Best Practices

- **Order layers logically:** Place instructions that change frequently (like `COPY . .`) as low as possible in the Dockerfile.
- **Combine RUN instructions:** Instead of multiple `RUN apt-get update` and `RUN apt-get install`, chain them with `&&` and `\` to avoid creating unnecessary intermediate layers:
  ```dockerfile
  RUN apt-get update && apt-get install -y \
      git \
      curl \
      && rm -rf /var/lib/apt/lists/*
  ```
- **Use `.dockerignore`:** Prevent copying `node_modules`, local python virtual environments (`.venv`), logs, or secrets into the build context.

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Copying `node_modules` or `.venv` | Inflates build size; conflicts with architecture-specific dependencies compiled inside Docker | Exclude them using a `.dockerignore` file. |
| Using `latest` tag | Builds are non-deterministic and can break unexpectedly | Pin specific version tags (e.g., `node:20.11.0-alpine`). |

---

## Interview Points

> **📌 Interview Point 1: What is the build context in Docker?**
> The build context is the directory specified in the `docker build` command (typically `.`). All files in this directory are sent to the Docker daemon. A large build context slows down builds.

> **📌 Interview Point 2: How can we reduce Docker image size?**
> Use smaller base images (like Alpine/slim), combine commands in a single `RUN` instruction, leverage `.dockerignore` to exclude files, and use multi-stage builds.

> **📌 Interview Point 3: What happens if you run `COPY . .` before `RUN pip install -r requirements.txt`?**
> Every single time you make a minor change to any file in your source code, the Docker build cache is invalidated at the `COPY` step, forcing a slow rebuild of `pip install` on subsequent layers.

---

## Exercises

### Exercise 1: Build a Dockerfile for Python ⭐
**Task:** Write a simple Dockerfile for a Python app running `app.py` on port 5000 using `python:3.11-slim` as the base image. Make sure dependencies are installed efficiently.

<details>
<summary>💡 Hint (click to reveal)</summary>
Copy `requirements.txt` first, run `pip install -r requirements.txt`, copy `app.py`, expose 5000, and run using `python app.py` (represented as CMD list array).
</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```dockerfile
FROM python:3.11-slim

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
```
</details>

---

## Chapter Summary

- **Dockerfile instructions** execute in order and create stackable layers.
- **Layer caching** is broken at the first line where files change; organize instructions from least-frequently-changing to most-frequently-changing.
- Prefer **`COPY`** over `ADD` for security and simplicity.

---

## Previous / Next Chapter

**⬅️ [Previous: Introduction to Docker](./ch01-introduction-to-docker.md)**

**➡️ [Next: Multi-Stage Builds](./ch03-multi-stage-builds.md)**

---

*Chapter 2 of the Docker & Containerization Guide | CodeShelf*
