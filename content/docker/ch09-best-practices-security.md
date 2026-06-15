---
title: Best Practices & Security
description: Advanced Docker safety, .dockerignore setup, vulnerability scanning (Trivy), layer optimization, and secure secrets handling.
order: 9
tags: [docker, security, best-practices, optimization, vulnerability]
---

# Chapter 9: Best Practices & Security

> **Secure your containers, optimize build performance, write clean configuration templates, and scan for software vulnerabilities.**

---

## Table of Contents

1. [Understanding .dockerignore](#understanding-dockerignore)
2. [Vulnerability Scanning with Trivy](#vulnerability-scanning-with-trivy)
3. [Optimizing Caching and Layer Reduction](#optimizing-caching-and-layer-reduction)
4. [Preventing Secret Leaks (BuildKit Secrets)](#preventing-secret-leaks-buildkit-secrets)
5. [Linting Dockerfiles](#linting-dockerfiles)
6. [Best Practices](#best-practices)
7. [Common Mistakes](#common-mistakes)
8. [Interview Points](#interview-points)
9. [Exercises](#exercises)
10. [Chapter Summary](#chapter-summary)

---

## Understanding .dockerignore

When you run `docker build .`, the Docker client packages all files in the directory (the **build context**) and uploads them to the Docker daemon. If you have large directories like `node_modules`, `.venv`, or large log files, this upload can take minutes and bloats the build.

> **Definition:** A `.dockerignore` file works like a `.gitignore` file. It prevents specified files and directories from being sent to the Docker build context.

### Example `.dockerignore`
Place this in the root directory alongside your Dockerfile:

```text
# Exclude source control
.git
.gitignore

# Exclude dependencies (let container install its own)
node_modules/
.venv/
env/
venv/

# Exclude system configs and local logs
*.log
.DS_Store
dist/
build/

# Exclude secrets
.env
.env.*
secrets.json
```

---

## Vulnerability Scanning with Trivy

Even if your own code is secure, the base image (like `ubuntu` or `node`) or third-party packages you install might contain known security vulnerabilities (CVEs).

### Using Trivy
[Trivy](https://github.com/aquasecurity/trivy) is a popular, open-source vulnerability scanner for containers. You can run it locally or in your CI/CD pipelines:

```bash
# Scan a local Docker image for vulnerabilities
trivy image my-app:latest
```

### Reading Scan Results
Trivy classifies vulnerabilities into severity levels: **UNKNOWN**, **LOW**, **MEDIUM**, **HIGH**, and **CRITICAL**.
You can configure your CI pipeline to block deployment if any **HIGH** or **CRITICAL** vulnerabilities are found:

```bash
trivy image --severity HIGH,CRITICAL --exit-code 1 my-app:latest
```

---

## Optimizing Caching and Layer Reduction

Each `RUN`, `COPY`, and `ADD` instruction creates a layer. To optimize:

### 1. Clean Up Package Manager Cache in the Same Layer
If you install packages and clean the cache in separate `RUN` commands, the cache files are still saved in the intermediate layer, bloating the image.
- **Incorrect:**
  ```dockerfile
  RUN apt-get update
  RUN apt-get install -y git
  ```
- **Correct (combining and purging):**
  ```dockerfile
  RUN apt-get update && apt-get install -y --no-install-recommends \
      git \
      && rm -rf /var/lib/apt/lists/*
  ```

---

## Preventing Secret Leaks (BuildKit Secrets)

If you need secrets (like NPM tokens or private SSH keys) *during build time* to install private packages, do **not** use `ARG` or `ENV` because they remain visible in image metadata.

### Using Docker BuildKit Secrets
BuildKit allows you to mount secrets temporarily during compilation without saving them in the final image:

```dockerfile
# syntax=docker/dockerfile:1
FROM node:20-alpine
WORKDIR /app

# Mount the secret key temporarily to install dependencies
RUN --mount=type=secret,id=npmrc_token \
    npm config set //registry.npmjs.org/:_authToken $(cat /run/secrets/npmrc_token) && \
    npm ci
```

To build this:
```bash
docker build --secret id=npmrc_token,src=~/.npmrc -t my-app .
```

---

## Linting Dockerfiles

Use [Hadolint](https://github.com/hadolint/hadolint), a smart Dockerfile linter, to check for style violations and security flaws:

```bash
# Lint a Dockerfile
hadolint Dockerfile
```

It warns you about issues like missing version pins, raw `apt-get` commands, or not running as non-root.

---

## Best Practices

- **Enable BuildKit:** Ensure `DOCKER_BUILDKIT=1` is set in your environment (it is enabled by default in modern Docker versions) for faster builds and secret mounts.
- **Pin base images to digests:** For extreme security, pin base images by their SHA256 digest so you get the exact same byte-for-byte image:
  `FROM python:3.11-slim@sha256:d8c0b58e721a...`

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Not using `.dockerignore` | Huge build contexts, slow upload, security exposure of local files | Always copy a standardized `.dockerignore` file before building. |
| Using outdated dependencies | Pushes vulnerabilities straight to production servers | Regularly run image scanning tools in your pipeline and rebuild base images weekly. |

---

## Interview Points

> **📌 Interview Point 1: What is the purpose of a `.dockerignore` file?**
> It excludes files (like `.git`, `node_modules`, and local secrets) from the build context. This speeds up builds by reducing context size and protects security by preventing local config leaks.

> **📌 Interview Point 2: Why should you clean up package manager caches in the same `RUN` layer?**
> Docker layers are read-only stackable filesystems. If you clean the cache in a separate command, the cache files are already stored permanently in the previous layer. They must be cleaned in the exact same command.

> **📌 Interview Point 3: How can you build images containing dependencies from private Git repositories safely?**
> Use Docker BuildKit's `--mount=type=ssh` or `--mount=type=secret` features to mount temporary credentials that are not committed to the image layers.

---

## Exercises

### Exercise 1: Write a `.dockerignore` file ⭐
**Task:** Write a `.dockerignore` file that ignores git metadata, python virtual environment folders, and local environment files.

<details>
<summary>💡 Hint (click to reveal)</summary>
Ignore `.git`, `.venv`, and `*.env`.
</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```text
.git
.venv
venv
*.env
.env
```
</details>

---

## Chapter Summary

- **`.dockerignore`** reduces build context payload size.
- **Trivy** scans built container filesystems for security CVEs.
- Combine **`RUN`** instructions and purge installation caches inside the same step to save space.

---

## Previous / Next Chapter

**⬅️ [Previous: Deployment Environments](./ch08-deployment-environments.md)**

**➡️ [Next: Interview Preparation](./ch10-interview-prep.md)**

---

*Chapter 9 of the Docker & Containerization Guide | CodeShelf*
