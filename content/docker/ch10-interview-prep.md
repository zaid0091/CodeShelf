---
title: Interview Preparation
description: Top 15 Docker & Containerization technical interview questions and answers, quick-revision cheat sheet, and study prep.
order: 10
tags: [docker, interview, devops, study-guide]
---

# Chapter 10: Interview Preparation

> **Study these high-frequency interview questions and answers on Docker and Containerization. Answer out loud in 60-90 seconds during prep.**

---

## Table of Contents

1. [Top 15 Interview Questions & Answers](#top-15-interview-questions--answers)
2. [Quick-Revision Command Cheat Sheet](#quick-revision-command-cheat-sheet)
3. [Key Concepts Matcher](#key-concepts-matcher)
4. [Course Wrap-Up](#course-wrap-up)

---

## Top 15 Interview Questions & Answers

---

### Q1: What is the difference between Virtualization and Containerization?
**Answer:** 
- **Virtualization** isolates hardware resources using a Hypervisor. Each Virtual Machine (VM) includes its own guest operating system, virtual CPU, memory, and storage, making it resource-heavy (GBs in size, minutes to boot).
- **Containerization** isolates processes at the operating system level. Containers share the host OS kernel and run inside isolated user spaces using Linux namespace and cgroup primitives. They are lightweight (MBs in size, start in seconds).

---

### Q2: What is the difference between a Docker Image and a Container?
**Answer:** 
- An **Image** is a read-only, immutable template containing the application code, libraries, dependencies, and configuration layers. It is built from a Dockerfile. (Analogous to a *Class* in OOP).
- A **Container** is a live, running instance of an image. It adds a thin, writeable layer on top of the image's read-only layers. (Analogous to an *Instance* of a class).

---

### Q3: Explain the difference between `RUN`, `CMD`, and `ENTRYPOINT`.
**Answer:** 
- **`RUN`** executes commands during the image *build* process (e.g., `RUN apt-get install`). It creates a new layer in the final image.
- **`CMD`** sets the default command and arguments to run when the container *starts*. It can be easily overridden by passing arguments in the CLI (e.g., `docker run my-image echo "hello"`).
- **`ENTRYPOINT`** configures a container to run as an executable. Arguments passed in the CLI are appended to it. It requires the `--entrypoint` flag to override.

---

### Q4: What are Multi-Stage builds and why are they used?
**Answer:** 
Multi-stage builds use multiple `FROM` instructions in a single Dockerfile. They allow developers to use a heavy, tool-rich image to build/compile the application (e.g., Node, SDKs, GCC), and then copy only the compiled binaries or static assets into a lightweight runtime image (e.g., Alpine, Nginx). This minimizes final image size and reduces security vulnerabilities in production.

---

### Q5: How does Docker build caching work and how do you optimize it?
**Answer:** 
Docker caches the result of each step (layer) during a build. If an instruction or any file it relies on changes, Docker invalidates the cache for that step and all subsequent steps.
To optimize, order instructions from least-frequently-changing to most-frequently-changing. For example, copy dependency configurations (e.g., `package.json`, `requirements.txt`) and run installations *before* copying the application source code.

---

### Q6: What is the difference between a Bind Mount and a Named Volume?
**Answer:** 
- **Bind Mount:** Direct mapping of a folder on the host machine to a folder inside the container. Best for local development to sync code changes instantly.
- **Named Volume:** A directory managed completely by Docker inside its private storage directory on the host (`/var/lib/docker/volumes/`). Best for persistent database storage in production.

---

### Q7: Why does reloading pages in a React SPA containerized with Nginx return a 404 error?
**Answer:** 
This happens because Single Page Applications (SPAs) use client-side routing. When you reload a page like `/dashboard`, Nginx looks for a physical directory or file named `/dashboard` inside `/usr/share/nginx/html`. Since it doesn't exist, Nginx returns a 404. 
The fix is to configure Nginx to route all unmatched requests back to `index.html` using the `try_files $uri $uri/ /index.html;` directive.

---

### Q8: How do containers communicate with each other in Docker?
**Answer:** 
Containers on the same Docker user-defined network communicate with each other using their container or service names as hostnames. Docker runs an internal DNS server that automatically translates service names to private container IP addresses. Containers on the default bridge network cannot use DNS resolution and must communicate via IP addresses.

---

### Q9: Why shouldn't you run database migrations inside a Dockerfile?
**Answer:** 
A Dockerfile defines the build phase of an image. The target database is typically not running or accessible during compilation. Running migrations in a Dockerfile would fail. Migrations must be run during the *runtime* phase (startup) using an entrypoint script or as a separate release phase in your deployment pipeline.

---

### Q10: How do you secure Docker containers for production?
**Answer:** 
1. Run application processes as a **non-root user** (`USER` instruction).
2. Set resource limits (CPU and Memory) to prevent denial of service.
3. Keep the file system read-only using the `--read-only` flag at runtime.
4. Mount secrets dynamically at runtime; never write credentials into the Dockerfile or `.env` files.
5. Use small, stripped-down base images (like Alpine or distroless) to reduce vulnerabilities.

---

### Q11: What is the OOM Killer and what is Docker exit code 137?
**Answer:** 
The Out-of-Memory (OOM) Killer is a Linux kernel feature. If the host machine runs out of memory, the kernel starts terminating processes to free up RAM. If a container exceeds its memory limits (or host memory is exhausted), the kernel kills the container process. Docker reports this with **exit code 137** (which indicates the process was terminated by signal 9, SIGKILL, due to OOM).

---

### Q12: What is the purpose of the `.dockerignore` file?
**Answer:** 
It tells the Docker CLI to ignore specific files and folders when preparing the build context (the payload uploaded to the Docker daemon). It prevents bloating build times with files like `node_modules` or `.venv`, and prevents leaking local configuration files or secrets (like `.env`) into the container image.

---

### Q13: Explain Docker networking drivers (Bridge vs Host vs None vs Overlay).
**Answer:** 
- **Bridge:** The default driver. Creates an isolated private network on the host machine.
- **Host:** Removes network isolation. The container shares the host's networking namespace and ports directly.
- **None:** Completely isolates the container with no network interface.
- **Overlay:** Links multiple Docker hosts (Docker Swarm) together, allowing containers on different machines to communicate directly.

---

### Q14: How does the shell form differ from the exec form in Dockerfile instructions?
**Answer:** 
- **Shell form (e.g. `CMD python app.py`):** Runs the command inside a shell (`/bin/sh -c`). The container process runs as a child of the shell. It does not receive OS signals (like SIGTERM), preventing graceful shutdowns.
- **Exec form (e.g. `CMD ["python", "app.py"]`):** Runs the executable directly without invoking a shell. The program runs as PID 1 and receives OS signals directly, allowing graceful termination.

---

### Q15: What is the purpose of the `exec "$@"` statement in an entrypoint script?
**Answer:** 
`exec "$@"` replaces the running shell script process with the command specified in the container's `CMD` or CLI arguments. This ensures that the application process (e.g. Gunicorn) inherits PID 1 and receives system signals (SIGTERM/SIGKILL) directly for clean shutdowns, rather than running as a subprocess of the shell.

---

## Quick-Revision Command Cheat Sheet

```bash
# Clean up dangling images, containers, and networks
docker system prune -f

# Clean up EVERYTHING including unused volumes and images
docker system prune -a --volumes -f

# Tail logs of a specific container
docker logs -f <container_name>

# Inspect a running container's resource usage in real-time
docker stats

# Save a running container's state to a new image
docker commit <container_id> <new_image_name>
```

---

## Key Concepts Matcher

| Term | Matches |
|------|---------|
| **Namespaces** | Isolate processes, network interfaces, mounts |
| **cgroups** | Limit hardware resources (CPU, Memory, IO) |
| **BuildKit** | Modern build engine with advanced caching and secrets mounts |
| **Hadolint** | Static analysis linter for Dockerfiles |

---

## Course Wrap-Up

Congratulations! You have completed the Docker & Containerization revision notes. You now understand how to containerize Django and React apps efficiently, optimize builds, and secure containers for production.

---

## Previous / Next Chapter

**⬅️ [Previous: Best Practices & Security](./ch09-best-practices-security.md)**

---

*Chapter 10 of the Docker & Containerization Guide | CodeShelf*
