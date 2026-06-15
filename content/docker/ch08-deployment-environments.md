---
title: Deployment Environments
description: Production-grade container deployment concerns including non-root security, memory/CPU resources, registries, restart policies, and secrets.
order: 8
tags: [docker, deployment, security, production, cloud]
---

# Chapter 8: Deployment Environments

> **Transition containers from development to production securely — configuring resource limits, non-root users, registries, and restart policies.**

---

## Table of Contents

1. [Production Deployment Checklist](#production-deployment-checklist)
2. [Running as a Non-Root User](#running-as-a-non-root-user)
3. [Restricting Container Resources (CPU & Memory)](#restricting-container-resources-cpu--memory)
4. [Container Restart Policies](#container-restart-policies)
5. [Managing Secrets and Env Vars Safely](#managing-secrets-and-env-vars-safely)
6. [Publishing Images to Registries (Docker Hub / AWS ECR)](#publishing-images-to-registries-docker-hub--aws-ecr)
7. [Best Practices](#best-practices)
8. [Common Mistakes](#common-mistakes)
9. [Interview Points](#interview-points)
10. [Exercises](#exercises)
11. [Chapter Summary](#chapter-summary)

---

## Production Deployment Checklist

Before exposing containers to live production traffic, ensure:
- [ ] Application does **not** run as root inside the container.
- [ ] Resource limits (Memory, CPU) are configured to prevent host crashes.
- [ ] Secrets (passwords, tokens) are excluded from the Docker image.
- [ ] Restart policies are enabled for automatic recovery.
- [ ] Production-grade servers (Gunicorn, Nginx) are utilized instead of dev servers.

---

## Running as a Non-Root User

By default, Docker runs container processes as the root user. If an attacker gains remote execution inside your container, they will have root privileges, allowing them to potentially break out to the host system.

### Creating and Switching Users
You should always create a non-root system user inside the Dockerfile:

```dockerfile
# Create system user group and user
RUN groupadd -r appgroup && useradd -r -g appgroup -u 10001 appuser

# Set working directory
WORKDIR /app

# Copy files and change ownership
COPY --chown=appuser:appgroup . .

# Switch user
USER appuser

CMD ["python", "app.py"]
```

---

## Restricting Container Resources (CPU & Memory)

Without limits, a single compromised or poorly written container (e.g. infinite loop, memory leak) can consume all CPU and RAM on the host machine, crashing other applications.

### 1. Docker CLI Limits
```bash
# Run container with maximum 512MB RAM and 1.5 CPU cores
docker run -d --name api-server --memory="512m" --cpus="1.5" my-app:latest
```

### 2. Docker Compose Limits
Under Compose, we define resource limits inside the `deploy` configuration block:

```yaml
services:
  api:
    image: my-app:latest
    deploy:
      resources:
        limits:
          cpus: '0.50'
          memory: 512M
        reservations:
          memory: 128M
```

---

## Container Restart Policies

Restart policies dictate how Docker recovers containers when they crash or when the Docker daemon restarts:

| Restart Policy | Behavior | Use Case |
|----------------|----------|----------|
| **`no`** | Do not restart the container automatically (default). | Standard scripts or one-off tasks. |
| **`on-failure`** | Restart only if the container exits with a non-zero exit code. | Batch jobs or critical background scripts. |
| **`always`** | Always restart the container regardless of exit code. | Production servers, proxies, databases. |
| **`unless-stopped`** | Restart always, unless explicitly stopped by the user. | Production systems (keeps containers down if stopped on purpose). |

---

## Managing Secrets and Env Vars Safely

Never bake environment variables or credentials directly into your Docker image. 

- **Incorrect (Leaks secrets in layers):**
  `ENV DATABASE_PASSWORD="supersecretpassword"`
- **Correct (Loads at runtime):**
  Inject environment variables during container startup:
  ```bash
  docker run -d --env-file .env.production my-app:latest
  ```

---

## Publishing Images to Registries (Docker Hub / AWS ECR)

To deploy containers to cloud servers (AWS, GCP, DigitalOcean), you must push the image to a container registry:

```bash
# 1. Log in to the Docker Hub registry
docker login --username myusername

# 2. Tag your image to match your registry repository name
docker tag my-local-image:1.0.0 myusername/my-prod-repo:1.0.0

# 3. Push the image
docker push myusername/my-prod-repo:1.0.0
```

---

## Best Practices

- **Use `unless-stopped`:** It prevents containers from booting up on system reboot if you deliberately stopped them for maintenance.
- **Implement Health Checks:** Let Docker monitor if the internal web service is actually responsive:
  ```dockerfile
  HEALTHCHECK --interval=30s --timeout=5s \
    CMD curl -f http://localhost:8000/health/ || exit 1
  ```

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Running out of memory (OOM Kill) | The OS kernel terminates the container process if it exceeds hard memory limits | Allocate a safety buffer (`reservations`) and monitor memory consumption during load tests. |
| Storing API keys in the Dockerfile | Anyone with pull permissions or access to image history can view secret keys | Read credentials from runtime environments or mounting files. |

---

## Interview Points

> **📌 Interview Point 1: What is an OOM Killer?**
> Out-Of-Memory Killer is an OS kernel mechanism. If a container exceeds its allocated memory limit, the host kernel stops the main process inside that container with exit code **137** (OOMKilled) to protect host system stability.

> **📌 Interview Point 2: Why is `unless-stopped` preferred over `always` restart policy?**
> Both restart containers automatically on crashes or reboot. However, if a developer manually stops an `always` container, it will start up again automatically on host reboot. `unless-stopped` respects manual stops.

> **📌 Interview Point 3: Can you extract environment variables from built Docker images?**
> Yes! Anyone can run `docker inspect image_name` or use reverse-engineering tools like `dive` to inspect variables set with `ENV`. That is why secrets must be injected at runtime, not build time.

---

## Exercises

### Exercise 1: Define CPU Limits ⭐
**Task:** Write a docker run command to launch an Nginx container named `web` limited to `0.5` CPU cores and `256` Megabytes of RAM.

<details>
<summary>💡 Hint (click to reveal)</summary>
Use the `--cpus` and `--memory` flags.
</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```bash
docker run -d --name web --cpus="0.5" --memory="256m" nginx:alpine
```
</details>

---

## Chapter Summary

- **Non-root execution** limits security exposure inside host servers.
- **Resource limits** prevent resource starvation and noisy neighbor scenarios.
- **Runtime environment injection** is mandatory for database secrets.

---

## Previous / Next Chapter

**⬅️ [Previous: Volumes & Networks](./ch07-volumes-and-networks.md)**

**➡️ [Next: Best Practices & Security](./ch09-best-practices-security.md)**

---

*Chapter 8 of the Docker & Containerization Guide | CodeShelf*
