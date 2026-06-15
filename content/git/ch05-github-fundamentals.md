---
title: GitHub Fundamentals
description: Understand remote repositories, secure SSH authentication setups, Pull Requests (PRs), code reviews, Forking workflows, and Gitflow branching strategies.
order: 5
tags: [git, github, remote, ssh, workflow]
---

# Chapter 5: GitHub Fundamentals

> **Collaborate with developers globally — configuring remote servers, secure SSH access, Pull Requests, and team branching models.**

---

## Table of Contents

1. [Remote Repositories (remotes)](#remote-repositories-remotes)
2. [git fetch vs git pull](#git-fetch-vs-git-pull)
3. [Secure Authentication: SSH Keys Setup](#secure-authentication-ssh-keys-setup)
4. [The Pull Request (PR) Workflow](#the-pull-request-pr-workflow)
5. [Forking Workflow: Upstream vs Origin](#forking-workflow-upstream-vs-origin)
6. [Branching Strategies: Gitflow vs Trunk-based](#branching-strategies-gitflow-vs-trunk-based)
7. [Best Practices](#best-practices)
8. [Common Mistakes](#common-mistakes)
9. [Interview Points](#interview-points)
10. [Exercises](#exercises)
11. [Chapter Summary](#chapter-summary)

---

## Remote Repositories (remotes)

A remote repository is a version of your project hosted on the internet or network (e.g. GitHub, GitLab, Bitbucket).

```bash
# 1. List configured remote server aliases (typically 'origin')
git remote -v

# 2. Link a local repository to a remote server
git remote add origin git@github.com:user/project.git

# 3. Rename a remote connection alias
git remote rename origin upstream

# 4. Remove a remote connection
git remote remove origin
```

---

## git fetch vs git pull

```text
               +-----------------------------+
               |  Remote Server (GitHub)     |
               +-----------------------------+
                       /             \
            git fetch /               \ git pull
                     v                 v
            [ Local Index Refs ]  [ Staging & Working ]
             (origin/main pointer   (Code updated
              is updated on disk)    physically on disk)
```

### 1. `git fetch`
Downloads all history, branches, and tags from the remote repository to your local `.git` directory. It does **not** modify or merge changes into your working files. It is completely safe.

### 2. `git pull`
Combines two commands: `git fetch` followed immediately by `git merge`. It downloads the changes and merges them into your active branch, potentially triggering merge conflicts.

---

## Secure Authentication: SSH Keys Setup

SSH (Secure Shell) keys allow you to connect and authenticate to GitHub without entering your username and password on every command.

### Step 1: Generate a New SSH Key
Open your terminal and run:
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```
Press Enter to accept default storage locations and enter a secure passphrase.

### Step 2: Add SSH Key to the ssh-agent
```bash
# Start ssh-agent in background
eval "$(ssh-agent -s)"

# Add key
ssh-add ~/.ssh/id_ed25519
```

### Step 3: Add the Key to GitHub
Copy the public key content to your clipboard:
```bash
cat ~/.ssh/id_ed25519.pub
```
Go to **GitHub Settings -> SSH and GPG keys -> New SSH Key**, paste the content, and save.

---

## The Pull Request (PR) Workflow

A Pull Request is a feature on platforms like GitHub that lets you tell others about changes you've pushed to a branch.

```text
1. Create branch -> 2. Push to remote -> 3. Open PR -> 4. Code Review -> 5. Merge
```
Once a PR is opened, teammates can review the diff, comment on specific lines of code, trigger automated testing pipelines, and approve the merge.

---

## Forking Workflow: Upstream vs Origin

Common in open-source projects:
1. **Fork:** You clone the main project repository (the **`upstream`**) to your own GitHub account (the **`origin`**).
2. **Clone:** You clone `origin` to your local machine.
3. **Link upstream:** You add a remote pointing to the main project:
   `git remote add upstream https://github.com/original-owner/project.git`
4. **Sync:** To sync changes from upstream:
   `git fetch upstream && git merge upstream/main`

---

## Branching Strategies: Gitflow vs Trunk-based

```text
Gitflow Workflow:
[ main ]     ============================= (Production Release)
               \                       /
[ develop ]   =========================   (Integration/Test)
                \         /     \     /
[ feature ]      =========       =====    (Developer tasks)

Trunk-based Workflow:
[ main ]     ============================= (Constant Prod Deployment)
               \     /     \     /
[ feature ]     =====       =====         (Short-lived features <24h)
```

### 1. Gitflow
Features parallel branches: `main` (production), `develop` (testing/pre-prod), `feature/*` (tasks), `release/*` (deployment prep), and `hotfix/*`. Good for release-cycle software but slow for continuous deployment.

### 2. Trunk-based Development
Developers merge small, frequent commits into a single central branch (`main` or `trunk`). Features are short-lived (less than a day), avoiding large merge conflict integrations.

---

## Best Practices

- **Fetch before merging:** Always fetch metadata (`git fetch`) before pulling, so you can inspect incoming history using `git log origin/main` first.
- **Configure default pull behavior:** Use `rebase` on pulls to keep your local commit history clean:
  `git config --global pull.rebase true`

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Committing SSH private keys | Exposes complete server credentials publicly | Never add files in `~/.ssh/` to a Git repository. Add private key names to global gitignore. |
| Pulling into modified working trees | Causes complex local merge conflict trees | Run `git stash` or commit local changes before running `git pull`. |

---

## Interview Points

> **📌 Interview Point 1: What is the difference between git fetch and git pull?**
> `git fetch` downloads remote metadata and branches without altering your working directory. `git pull` downloads remote metadata and immediately attempts to merge it into your active branch.

> **📌 Interview Point 2: What is the difference between origin and upstream remotes?**
> `origin` refers to your personal fork of a repository on GitHub. `upstream` refers to the original, main repository from which you forked.

> **📌 Interview Point 3: What is Trunk-based development?**
> It is a branching strategy where all developers merge short-lived feature branches directly into a single central branch (`main`) frequently, reducing long integration conflicts and supporting CI/CD.

---

## Exercises

### Exercise 1: Sync a Fork ⭐⭐
**Task:** Write the commands to pull the latest changes from the `upstream` remote's `main` branch and merge them into your local active branch.

<details>
<summary>💡 Hint (click to reveal)</summary>
Fetch upstream and merge `upstream/main`.
</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```bash
# Fetch remote branches
git fetch upstream

# Merge changes into active branch
git merge upstream/main
```
</details>

---

## Chapter Summary

- **`git remote`** manages connections to servers.
- **`git fetch`** is non-destructive; **`git pull`** fetch-and-merges.
- Connect securely using **SSH keys**.
- **Trunk-based** development emphasizes fast, linear merges into `main`.

---

## Previous / Next Chapter

**⬅️ [Previous: Rebasing & Rewriting History](./ch04-rebasing-and-history.md)**

**➡️ [Next: GitHub Actions (CI/CD)](./ch06-github-actions-cicd.md)**

---

*Chapter 5 of the Git & GitHub Guide | CodeShelf*
