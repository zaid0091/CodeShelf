---
title: Volumes and Networks
description: Deep dive into Docker data persistence (bind mounts vs named volumes) and networking drivers, ports, and container DNS resolution.
order: 7
tags: [docker, volumes, networks, storage, security]
---

# Chapter 7: Volumes and Networks

> **Configure data persistence and secure container-to-container communication using Docker Volumes and Networking drivers.**

---

## Table of Contents

1. [Docker Storage: Bind Mounts vs Named Volumes](#docker-storage-bind-mounts-vs-named-volumes)
2. [Managing Volumes with Docker CLI](#managing-volumes-with-docker-cli)
3. [Docker Networking Drivers](#docker-networking-drivers)
4. [Custom Bridge Networks](#custom-bridge-networks)
5. [Container DNS and Service Discovery](#container-dns-and-service-discovery)
6. [Port Publishing vs Exposing](#port-publishing-vs-exposing)
7. [Best Practices](#best-practices)
8. [Common Mistakes](#common-mistakes)
9. [Interview Points](#interview-points)
10. [Exercises](#exercises)
11. [Chapter Summary](#chapter-summary)

---

## Docker Storage: Bind Mounts vs Named Volumes

By default, files created inside a container are stored in a writable container layer. When the container is deleted, **all data is lost**. Docker offers two main mechanisms for persistent storage:

```text
       [ Host Machine Filesystem ]
+----------------------------------------+
|  /home/user/project  (Host Directory)  | <--- Bind Mount (syncs host files directly)
+----------------------------------------+
|  /var/lib/docker/volumes (Docker Dir)  | <--- Named Volume (managed completely by Docker)
+----------------------------------------+
```

### 1. Bind Mounts
- **What it is:** Directly maps a physical directory on the host computer to a path inside the container.
- **When to use:** Local development (e.g., syncing code changes instantly to the container without rebuilding the image).
- **Syntax:** `docker run -v /absolute/path/on/host:/app/path`

### 2. Named Volumes
- **What it is:** Docker creates and manages a folder inside Docker's own storage directory on the host (`/var/lib/docker/volumes/`). Non-Docker processes should not touch this folder.
- **When to use:** Production databases, persistent logs, or sharing files between multiple containers.
- **Syntax:** `docker run -v my_data:/app/data`

### 3. tmpfs Mounts
- **What it is:** Mounts a folder in the host's system memory (RAM).
- **When to use:** Storing transient state or highly sensitive credentials that should never be written to disk.

---

## Managing Volumes with Docker CLI

Useful commands for managing Docker volumes:

```bash
# 1. Create a named volume
docker volume create pg_data

# 2. List all local volumes
docker volume ls

# 3. Inspect details of a volume (shows mount point on host)
docker volume inspect pg_data

# 4. Remove a volume (fails if container is still using it)
docker volume rm pg_data

# 5. Delete all unused volumes (helps recover disk space)
docker volume prune
```

---

## Docker Networking Drivers

Docker uses networking drivers to control how containers interact with the host and other containers:

| Driver | Description | Use Case |
|--------|-------------|----------|
| **`bridge`** | The default network driver. Creates an isolated network space on the host. | Standalone containers or multi-container stacks running on a single host. |
| **`host`** | Removes network isolation between container and host. The container uses host's IP/ports directly. | High-performance apps or routing debugging (e.g. running proxy tools). |
| **`overlay`** | Connects multiple Docker daemons across different machines. | Docker Swarm or multi-node container orchestrators. |
| **`none`** | Disables all container networking. Completely isolates the container. | Secure batch processing or offline tasks. |

---

## Custom Bridge Networks

The default bridge network (which standalone containers join) does **not** support DNS service discovery. Containers can only talk to each other via direct IP addresses, which change whenever containers restart.

To enable name-based resolution, you must create a **custom bridge network**:

```bash
# 1. Create a custom network
docker network create my-custom-net

# 2. Run containers on the custom network
docker run -d --name database --network my-custom-net postgres:alpine
docker run -d --name webserver --network my-custom-net -p 8080:80 nginx:alpine
```

---

## Container DNS and Service Discovery

Inside the custom network `my-custom-net`, you can ping or connect to the database using its container name:

```bash
# Run inside the webserver container
docker exec -it webserver ping database
```
Docker's internal DNS resolver answers requests for the hostname `database` with the database container's private IP.

---

## Port Publishing vs Exposing

- **`EXPOSE` (Dockerfile):** Merely serves as documentation between the image author and container runner. It does **not** map ports.
- **`ports:` / `-p` (CLI/Compose):** Maps a port on the host machine to a port inside the container (`-p 8080:80`). This makes the container accessible from the host network or public internet.

---

## Best Practices

- **Clean up volumes:** When removing containers, pass the `-v` flag to delete anonymous volumes associated with them:
  `docker rm -v container_name`
- **Use dedicated networks:** Isolate components. For example, keep your database on a back-end network only accessible to the backend app, while the reverse proxy stays on a front-end network.

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Sharing default bridge network for DNS | Named resolution fails; containers cannot connect to each other by name | Always create custom networks with `docker network create` or use Docker Compose. |
| Using relative paths for bind mounts | Docker CLI parses relative paths without a leading `./` as named volumes instead | Always use absolute paths or prefix with `${PWD}`/`./` (e.g. `-v ${PWD}:/app`). |

---

## Interview Points

> **📌 Interview Point 1: What is the difference between a bind mount and a volume?**
> Bind mounts map a physical path on the host to the container (good for dev files sync). Volumes are managed entirely by Docker, isolated from host OS processes, and perform better on virtualized systems (good for production data/databases).

> **📌 Interview Point 2: Does the default bridge network support DNS container name resolution?**
> No. The default bridge network only allows communication via IP addresses. You must create a custom user-defined bridge network to enable Docker's built-in DNS service discovery.

> **📌 Interview Point 3: What is a dangling volume, and how do you remove it?**
> A dangling volume is a volume that is no longer referenced by any active container. You can delete them all using the command `docker volume prune`.

---

## Exercises

### Exercise 1: Share Data Between Containers ⭐⭐
**Task:** Create a named volume `shared_logs`. Run an Alpine container that writes `hello` to `/logs/app.log`, and run another Alpine container that reads the file.

<details>
<summary>💡 Hint (click to reveal)</summary>
Mount the volume `shared_logs` to `/logs` in both containers.
</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```bash
# Create volume
docker volume create shared_logs

# Writer container
docker run --rm -v shared_logs:/logs alpine sh -c "echo 'Docker is fun' > /logs/app.log"

# Reader container
docker run --rm -v shared_logs:/logs alpine cat /logs/app.log
# (Outputs: Docker is fun)
```
</details>

---

## Chapter Summary

- **Named Volumes** persist database files; **Bind Mounts** sync local code files.
- **User-defined bridge networks** enable container-to-container DNS hostname resolution.
- Port mapping **`-p host_port:container_port`** makes containers accessible outside the Docker environment.

---

## Previous / Next Chapter

**⬅️ [Previous: React Containerization](./ch06-react-containerization.md)**

**➡️ [Next: Deployment Environments](./ch08-deployment-environments.md)**

---

*Chapter 7 of the Docker & Containerization Guide | CodeShelf*
