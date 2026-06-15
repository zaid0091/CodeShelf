---
title: Introduction to Docker
description: Learn the core concepts of Docker, difference between containers and VMs, architecture of Docker Engine, and basic lifecycle commands.
order: 1
tags: [docker, introduction, architecture, virtualization]
---

# Chapter 1: Introduction to Docker

> **Understand how containers work under the hood, how they differ from virtual machines, and the basic architecture of Docker.**

---

## Table of Contents

1. [What is Containerization?](#what-is-containerization)
2. [Containers vs Virtual Machines](#containers-vs-virtual-machines)
3. [Docker Architecture](#docker-architecture)
4. [Docker Images vs Containers](#docker-images-vs-containers)
5. [Basic Container Lifecycle Commands](#basic-container-lifecycle-commands)
6. [Best Practices](#best-practices)
7. [Common Mistakes](#common-mistakes)
8. [Interview Points](#interview-points)
9. [Exercises](#exercises)
10. [Chapter Summary](#chapter-summary)

---

## What is Containerization?

> **Definition:** Containerization is a form of operating system virtualization where applications are run in isolated user spaces called containers, sharing the host OS kernel.

### Why it matters

Before containers, developers faced the "it works on my machine" problem due to differences in libraries, OS versions, and configurations between development, staging, and production environments. Containers pack the application code together with its dependencies, configurations, and runtime environment, ensuring consistency everywhere.

---

## Containers vs Virtual Machines

Virtual Machines (VMs) and Containers isolate environments, but at different layers.

| Metric | Virtual Machines (VMs) | Containers |
|--------|------------------------|------------|
| **Architecture** | App + Guest OS + Hypervisor + Host OS | App + Container Engine (Docker) + Host OS |
| **Size** | Large (GBs) due to full guest OS | Small (MBs), packages only app + libraries |
| **Startup Time** | Minutes (boots guest OS) | Seconds (starts a process) |
| **Resource Usage** | High (memory & CPU pre-allocated) | Low (shares host OS kernel resources) |
| **Isolation** | Strong (hardware level) | Process-level (using namespaces and cgroups) |

---

## Docker Architecture

Docker uses a client-server architecture:

```text
+-------------------+      REST API      +-----------------------+      Pull/Push      +--------------------+
|   Docker Client   |  --------------->  |  Docker Daemon (Host) |  ---------------->  |  Docker Registry   |
| (docker CLI commands) |                | (manages containers,  |                     | (Docker Hub, ECR)  |
+-------------------+                    |  images, networks,    |                     +--------------------+
                                         |  and volumes)         |
                                         +-----------------------+
```

1. **Docker Client (`docker`):** The primary command-line tool developers use to interact with Docker. When you run `docker run`, the client sends this command to the Docker daemon.
2. **Docker Host (Docker Daemon - `dockerd`):** A persistent background process that listens for Docker API requests and manages Docker objects (Images, Containers, Networks, and Volumes).
3. **Docker Registry:** A storage system for sharing Docker images (e.g., Docker Hub, AWS ECR).

---

## Docker Images vs Containers

To understand Docker, you must know the difference between an Image and a Container:

> **Docker Image:** An immutable (read-only) blueprint or snapshot containing the application code, libraries, runtime, and configurations. Think of it as a **Class** in Object-Oriented Programming.

> **Docker Container:** A runnable, isolated instance of an image. It adds a thin, writeable layer on top of the read-only image layers. Think of it as an **Instance** of a Class.

---

## Basic Container Lifecycle Commands

Here are the essential commands for managing containers:

```bash
# 1. Pull an image from Docker Hub without running it
docker pull nginx:alpine

# 2. Run a container (runs in detached/background mode '-d' and maps port 8080 of host to 80 of container)
docker run -d -p 8080:80 --name my-web-server nginx:alpine

# 3. List running containers
docker ps

# 4. List all containers (including stopped ones)
docker ps -a

# 5. Stop a running container
docker stop my-web-server

# 6. Start a stopped container
docker start my-web-server

# 7. Execute a command inside a running container (opens interactive terminal 'sh')
docker exec -it my-web-server sh

# 8. Remove a stopped container
docker rm my-web-server

# 9. List local images
docker images

# 10. Remove a local image
docker rmi nginx:alpine
```

---

## Best Practices

- **Specify tags:** Never run or build images without a tag (e.g., do not use `nginx`, use a specific tag like `nginx:1.25-alpine`).
- **Clean up:** Use `docker system prune -f` to clear out unused containers, networks, and dangling images to save disk space.

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Confusing `rm` and `rmi` | Errors out or deletes the wrong object | Use `docker rm` to remove containers, and `docker rmi` to remove images. |
| Forgetting to publish ports | The container runs, but you cannot access it from the browser | Always use the `-p host_port:container_port` option (e.g., `-p 8080:80`). |

---

## Interview Points

> **📌 Interview Point 1: What is the difference between an Image and a Container?**
> An image is a read-only template containing the software package. A container is a running instance of that image, containing a writeable layer.

> **📌 Interview Point 2: How does Docker achieve container isolation?**
> Docker leverages Linux kernel features: **Namespaces** (for isolation of processes, network interfaces, mounts) and **Control Groups (cgroups)** (for resource limiting like CPU/memory).

> **📌 Interview Point 3: What does the `-it` flag stand for in `docker exec` or `docker run`?**
> `-i` (interactive) keeps `stdin` open, and `-t` (tty) allocates a pseudo-TTY terminal. Together, they let you interact with the shell inside a container.

---

## Exercises

### Exercise 1: Run and Inspect a Container ⭐
**Task:** Run an Alpine Linux container in interactive mode, inspect its hostname, and exit.

<details>
<summary>💡 Hint (click to reveal)</summary>
Use `docker run` with the `-it` flag on the `alpine` image, and run the `sh` command. Inside, run `hostname`.
</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```bash
# Start container and get interactive shell
docker run -it alpine sh

# Inside the shell:
/ # hostname
# (Outputs a random string representing the container ID)
/ # exit
```
</details>

---

## Chapter Summary

- **Containers** share the host kernel and start instantly, whereas **VMs** run a heavy guest OS.
- **Docker Client** talks to the **Docker Daemon** to download images and run containers.
- Always map ports correctly using `-p <host_port>:<container_port>` when running web servers.

---

## Previous / Next Chapter

**⬅️ [Previous: Course Overview](./ch00-course-overview.md)**

**➡️ [Next: Dockerfile Fundamentals](./ch02-dockerfile-fundamentals.md)**

---

*Chapter 1 of the Docker & Containerization Guide | CodeShelf*
