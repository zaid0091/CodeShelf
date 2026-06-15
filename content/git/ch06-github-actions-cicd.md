---
title: GitHub Actions (CI/CD)
description: Master GitHub Actions automation pipelines, YAML workflow schemas, triggers, jobs, runners, and secrets management.
order: 6
tags: [github, actions, cicd, devops, yaml]
---

# Chapter 6: GitHub Actions (CI/CD)

> **Automate code compilation, linting, testing, and deployment directly on code push using GitHub Actions.**

---

## Table of Contents

1. [What is CI/CD?](#what-is-cicd)
2. [Introduction to GitHub Actions](#introduction-to-github-actions)
3. [Workflow File Structure (.github/workflows/)](#workflow-file-structure-githubworkflows)
4. [Anatomy of a Workflow YAML](#anatomy-of-a-workflow-yaml)
5. [Understanding Runners, Jobs, and Steps](#understanding-runners-jobs-and-steps)
6. [Managing Secrets and Variables](#managing-secrets-and-variables)
7. [Best Practices](#best-practices)
8. [Common Mistakes](#common-mistakes)
9. [Interview Points](#interview-points)
10. [Exercises](#exercises)
11. [Chapter Summary](#chapter-summary)

---

## What is CI/CD?

- **Continuous Integration (CI):** Automating the process of building, linting, and testing code whenever a developer pushes commits to a repository. This catches bugs early.
- **Continuous Deployment (CD):** Automatically deploying code to production servers or hosting environments once it passes all validation steps.

---

## Introduction to GitHub Actions

> **Definition:** GitHub Actions is an API-integrated automation platform that executes event-driven workflows directly inside your GitHub repository.

Workflows are defined as YAML files and stored in the **`.github/workflows/`** directory in your codebase.

---

## Workflow File Structure (.github/workflows/)

```text
Repository Root/
├── .github/
│   └── workflows/
│       ├── test-pipeline.yml
│       └── deploy.yml
```

---

## Anatomy of a Workflow YAML

Here is a standard CI workflow that runs tests on every push to `main` and all Pull Requests:

```yaml
# 1. Name of the workflow
name: Node.js CI

# 2. Events that trigger the workflow
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

# 3. List of jobs to execute
jobs:
  build-and-test:
    # 4. OS environment the job runs on
    runs-on: ubuntu-latest

    # 5. Sequence of tasks to execute
    steps:
      # Step A: Checkout source code to runner filesystem
      - name: Checkout Code
        uses: actions/checkout@v4

      # Step B: Setup Node.js version environment
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      # Step C: Install packages
      - name: Install Dependencies
        run: npm ci

      # Step D: Run code linter
      - name: Run Linter
        run: npm run lint

      # Step E: Run unit tests
      - name: Run Tests
        run: npm test
```

---

## Understanding Runners, Jobs, and Steps

```text
+-----------------------------------------------------------+
|                      WORKFLOW RUN                         |
+-----------------------------------------------------------+
       /                                             \
+-------------------+                          +-------------------+
|    JOB 1 (Build)  |  (Runs in parallel)      |    JOB 2 (Lint)   |
|  Runner: Ubuntu   |                          |  Runner: macOS    |
+-------------------+                          +-------------------+
  Step 1: checkout                               Step 1: checkout
  Step 2: compile                                Step 2: run linter
```

- **Event:** A specific activity that triggers a workflow run (e.g. `push`, `pull_request`, `issue_comment`, or schedule `cron`).
- **Runner:** A virtual machine hosted by GitHub (or self-hosted) containing the Docker Engine, Git, and system libraries.
- **Job:** A group of steps running on the *same runner*. By default, multiple jobs run in **parallel**, but you can configure dependencies using `needs: job_name` to run them sequentially.
- **Step:** An individual task within a job. It can be a raw shell command (`run`) or an action (`uses` - reusable pre-written package).

---

## Managing Secrets and Variables

Never hardcode credentials (API keys, SSH keys, passwords) in your workflow YAML files.

### Using Encrypted Secrets
1. Go to **GitHub -> Repository Settings -> Secrets and variables -> Actions**.
2. Add a new secret (e.g., `DOCKER_PASSWORD`).
3. Reference the secret in your YAML using `${{ secrets.NAME }}` syntax:

```yaml
- name: Log in to Docker Hub
  run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u username --password-stdin
```

---

## Best Practices

- **Use dependency caching:** Use setup actions with built-in caching (like `cache: 'npm'` or `cache: 'pip'`) to avoid downloading packages from scratch on every run.
- **Limit runner permissions:** Restrict default `GITHUB_TOKEN` permissions to read-only inside the workflow file for better security:
  ```yaml
  permissions:
    contents: read
  ```

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Running heavy tasks in parallel sequentially | Slows down CI pipeline feedback loops | Split independent tasks (like building vs linting) into separate parallel jobs. |
| Hardcoding secrets | Anyone with read access to the repo can steal credentials | Use GitHub Encrypted Secrets exclusively for keys and tokens. |

---

## Interview Points

> **📌 Interview Point 1: What is a Runner in GitHub Actions?**
> A Runner is a virtual machine hosted by GitHub (or configured as self-hosted) that listens for available jobs, runs the job's steps, and reports the results back to GitHub.

> **📌 Interview Point 2: How can you make one job run only after another job completes?**
> By default, jobs run in parallel. You can force sequential execution by adding the `needs` keyword:
> ```yaml
> jobs:
>   test:
>     runs-on: ubuntu-latest
>   deploy:
>     needs: test
>     runs-on: ubuntu-latest
> ```

> **📌 Interview Point 3: What is the difference between `run` and `uses` in a workflow step?**
> `run` executes a raw terminal command on the runner's shell. `uses` calls a pre-built, reusable action block shared on the GitHub Actions Marketplace (e.g. `actions/checkout@v4`).

---

## Exercises

### Exercise 1: Build a manual trigger ⭐
**Task:** Identify the event keyword in YAML used to trigger a workflow manually from the GitHub UI.

<details>
<summary>💡 Hint (click to reveal)</summary>
It stands for "workflow dispatch".
</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```yaml
on:
  workflow_dispatch:
```
</details>

---

## Chapter Summary

- Save workflows in **`.github/workflows/`** as YAML.
- **Events** trigger workflows, **Jobs** run on virtual **Runners**, and **Steps** execute actions.
- Securely store API credentials in **GitHub Encrypted Secrets**.

---

## Previous / Next Chapter

**⬅️ [Previous: GitHub Fundamentals](./ch05-github-fundamentals.md)**

**➡️ [Next: Git Internals](./ch07-git-internals.md)**

---

*Chapter 6 of the Git & GitHub Guide | CodeShelf*
