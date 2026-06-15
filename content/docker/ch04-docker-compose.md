---
title: Docker Compose
description: Learn how to manage multi-container applications, write docker-compose.yml, configure networks, volumes, and environment variables.
order: 4
tags: [docker, compose, orchestration, devops]
---

# Chapter 4: Docker Compose

> **Manage multi-container applications seamlessly, configure networking, persistence, and service dependencies with a single YAML config.**

---

## Table of Contents

1. [Why Docker Compose?](#why-docker-compose)
2. [Anatomy of a docker-compose.yml File](#anatomy-of-a-docker-composeyml-file)
3. [Service Discovery and DNS](#service-discovery-and-dns)
4. [Managing Lifecycle with Compose CLI](#managing-lifecycle-with-compose-cli)
5. [Environment Variables in Compose](#environment-variables-in-compose)
6. [Mounting Volumes and Networks](#mounting-volumes-and-networks)
7. [Controlling Startup Order (depends_on)](#controlling-startup-order-depends_on)
8. [Best Practices](#best-practices)
9. [Common Mistakes](#common-mistakes)
10. [Interview Points](#interview-points)
11. [Exercises](#exercises)
12. [Chapter Summary](#chapter-summary)

---

## Why Docker Compose?

Running a modern web application involves multiple containers (e.g., a React frontend, a Django backend, a PostgreSQL database, and a Redis cache). Running them using raw `docker run` commands requires long, complex shell scripts to handle port mapping, networks, volume mounting, and container linking.

> **Definition:** Docker Compose is a tool for defining and running multi-container Docker applications. It uses a single YAML file (`docker-compose.yml`) to configure all application services, networks, and volumes.

---

## Anatomy of a docker-compose.yml File

Here is a standard compose configuration for a web application and a database:

```yaml
version: '3.8'

services:
  web:
    build:
      context: .
      dockerfile: Dockerfile.dev
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      - DATABASE_URL=postgres://postgres:secret@db:5432/mydb
    depends_on:
      - db

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:
```

### Key Keywords Explained:
- **`services`:** Defines the containers to start.
- **`build`:** Builds an image from a local Dockerfile instead of pulling from a registry.
- **`ports`:** Maps host ports to container ports (`"host:container"`).
- **`volumes`:** Configures data persistence or bind mounts (syncing host files into the container).
- **`environment`:** Sets environment variables inside the container.
- **`depends_on`:** Specifies dependency order (starts `db` container before starting `web`).

---

## Service Discovery and DNS

When you run `docker compose up`, Docker automatically creates a default **bridge network** and joins all services to it. 

### Hostname Resolution
Each container can reach any other container on the same network using the **service name** defined in the `docker-compose.yml` file as the hostname.

For example, in the YAML config above, the `web` container connects to the database using the host `db`:
`postgres://postgres:secret@db:5432/mydb`

Docker's internal DNS resolver automatically translates `db` to the container's private IP address on the virtual bridge network.

---

## Managing Lifecycle with Compose CLI

All compose commands must be run from the directory containing the `docker-compose.yml` file:

```bash
# 1. Start all containers in the background (detached)
docker compose up -d

# 2. Rebuild images and start containers (force rebuild of changes)
docker compose up -d --build

# 3. View running compose containers and their states
docker compose ps

# 4. Tail real-time aggregated logs of all services
docker compose logs -f

# 5. Stop and remove containers, networks, and volume definitions
docker compose down

# 6. Stop and delete everything, including volumes (wipes database data)
docker compose down -v

# 7. Execute command in a running compose service
docker compose exec web python manage.py migrate
```

---

## Environment Variables in Compose

Compose automatically loads environment variables from a `.env` file in the same directory:

```bash
# .env file
DB_PASSWORD=supersecret
DEBUG=True
```

You can reference these variables in your `docker-compose.yml` using `${VARIABLE_NAME}`:

```yaml
services:
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
```

---

## Controlling Startup Order (depends_on)

The `depends_on` property controls the startup order. However, it only waits until the dependency container **starts**, not until it is fully **healthy** or ready to accept connections.

For databases, you can use the long-form syntax with `condition: service_healthy`:

```yaml
services:
  web:
    build: .
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:15-alpine
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5
```

---

## Best Practices

- **Use Named Volumes:** Always use named volumes (e.g. `postgres_data`) instead of host bind mounts for database storage in local development, as it yields much better performance.
- **Keep `.env` out of VCS:** Commit `.env.example` to Git, but never commit your production `.env` containing database passwords and API keys.

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Overwriting db directories with bind mounts | Destroys database initialization files and prevents the DB from booting up | Avoid mapping raw host folders directly to `/var/lib/postgresql/data`. Use named volumes. |
| Port conflicts | Running compose up errors out because port is already bound | Check if other local processes or other docker containers are using the host port, and alter the host side of mapping (e.g. `8081:80`). |

---

## Interview Points

> **📌 Interview Point 1: What is the purpose of Docker Compose?**
> It is an orchestration tool for defining and running multi-container applications. It simplifies networking, volume mapping, and startups using a single declarative YAML file.

> **📌 Interview Point 2: How do containers communicate under Docker Compose?**
> Docker Compose sets up a single default network. Containers join this network and resolve other containers' IP addresses using their defined service names as hostnames.

> **📌 Interview Point 3: What is the difference between `docker compose up` and `docker compose start`?**
> `up` builds, creates, starts, and attaches containers for a service (creating them if they don't exist). `start` only restarts stopped containers that have already been created.

---

## Exercises

### Exercise 1: Run Web + Redis Cache ⭐⭐
**Task:** Write a `docker-compose.yml` defining two services: `app` (built from the current directory `.`) and `cache` (running the `redis:7-alpine` image). Expose `app` on host port `3000`.

<details>
<summary>💡 Hint (click to reveal)</summary>
Map port `3000:3000` or whatever port `app` runs on. Name the redis service `cache` so that the app can connect to `redis://cache:6379`.
</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    depends_on:
      - cache

  cache:
    image: redis:7-alpine
```
</details>

---

## Chapter Summary

- **Docker Compose** reads `docker-compose.yml` to launch multi-container stacks.
- Services share a **default network**, enabling communication via service name hostnames.
- Use **`docker compose down -v`** when you want a clean slate (deletes volumes).

---

## Previous / Next Chapter

**⬅️ [Previous: Multi-Stage Builds](./ch03-multi-stage-builds.md)**

**➡️ [Next: Django Containerization](./ch05-django-containerization.md)**

---

*Chapter 4 of the Docker & Containerization Guide | CodeShelf*
