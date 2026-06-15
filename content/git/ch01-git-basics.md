---
title: Git Basics
description: Learn the core concepts of Git version control, the three states (working, staging, repo), and essential commands like add, commit, diff, status, and log.
order: 1
tags: [git, basics, commits, version-control]
---

# Chapter 1: Git Basics

> **Understand version control principles, the three Git filesystems states, and master foundational Git commands.**

---

## Table of Contents

1. [What is Version Control?](#what-is-version-control)
2. [Centralized vs Distributed VCS](#centralized-vs-distributed-vcs)
3. [The Three Git States](#the-three-git-states)
4. [Basic Commands & Lifecycle](#basic-commands--lifecycle)
5. [Staging Files (git add)](#staging-files-git-add)
6. [Committing Changes (git commit)](#committing-changes-git-commit)
7. [Comparing Code (git diff)](#comparing-code-git-diff)
8. [Viewing History (git log)](#viewing-history-git-log)
9. [Best Practices](#best-practices)
10. [Common Mistakes](#common-mistakes)
11. [Interview Points](#interview-points)
12. [Exercises](#exercises)
13. [Chapter Summary](#chapter-summary)

---

## What is Version Control?

Version Control Systems (VCS) are tools that record modifications made to files over time. It allows developers to revert projects to previous versions, compare changes over time, track who made changes, and recover deleted code.

---

## Centralized vs Distributed VCS

- **Centralized VCS (e.g. SVN, Perforce):** A single server contains all versioned files. Clients check out files from this single place. If the server goes down, collaboration halts; if the disk crashes, history is lost.
- **Distributed VCS (e.g. Git, Mercurial):** Clients don’t just check out the latest snapshot of the files; they fully mirror the entire history database of the repository locally. If the main server crashes, any developer's local repository can be used to restore it.

---

## The Three Git States

Git manages your project files in three distinct locations or states:

```text
[ Working Directory ]   ---------->   [ Staging Area ]   ---------->   [ Git Repository ]
(Files you are editing)   git add    (Index preparation)  git commit  (Snapshot DB - .git)
```

1. **Working Directory:** The physical folder on your computer's filesystem. Here, files are modified, created, or deleted. They are *untracked* or *modified* in Git's eyes.
2. **Staging Area (Index):** A virtual staging area (managed as a file inside `.git/`) that records what changes will be packaged in your next snapshot commit.
3. **Git Repository (Repository):** The directory (stored in `.git/`) where Git permanently stores metadata and the compressed snapshot database of the project commits.

---

## Basic Commands & Lifecycle

To start tracking code:

```bash
# 1. Initialize a new local Git repository
git init

# 2. Clone an existing repository from a remote host
git clone https://github.com/user/repo.git

# 3. Check status of files in working and staging area
git status
```

---

## Staging Files (git add)

The `git add` command moves files from the Working Directory to the Staging Area.

```bash
# Stage a single file
git add index.js

# Stage all modified and new files in the current folder
git add .

# Stage files interactively (allows staging individual code lines/hunks)
git add -p
```

---

## Committing Changes (git commit)

Committing takes the staged files and writes a permanent snapshot to the Git history database.

```bash
# Commit with a short message
git commit -m "feat: add user login handler"

# Stage all modified files and commit in one command
git commit -am "fix: correct port alignment"

# Open default editor to write a multi-line commit message
git commit
```

### Writing Good Commit Messages
Always follow the **imperative mood** (e.g., "Fix layout crash", not "Fixed layout crash" or "Fixes layout crash"). Think of it as completing the sentence: *"If applied, this commit will..."*

---

## Comparing Code (git diff)

Inspect changes before committing them:

```bash
# Show differences between Working Directory and Staging Area
git diff

# Show differences between Staging Area and your last commit
git diff --cached

# Compare changes between two specific commits
git diff commit_sha1 commit_sha2
```

---

## Viewing History (git log)

Explore the commit history:

```bash
# Show full commit history
git log

# Show compact, one-line-per-commit graph
git log --oneline --graph --all

# Show commits limit to last 5 entries
git log -n 5
```

---

## Best Practices

- **Run `git status` constantly:** Always confirm what is staged before committing.
- **Do not commit raw generated files:** Use `.gitignore` to exclude log files, packages, and compiler outputs.

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Committing node_modules | Blows up repository size and slows down clones | Add `node_modules/` to `.gitignore` before runing `git add .`. |
| Writing vague commit messages | "Wip", "update", "fix bug" makes it impossible to audit history | Use conventional commits style: `feat: ...`, `fix: ...`, `refactor: ...`. |

---

## Interview Points

> **📌 Interview Point 1: What is the Staging Area in Git?**
> The staging area (or index) is a file in the `.git/` folder that prepares changes for the next commit. It allows you to commit fine-grained, selective changes instead of committing all file edits on disk.

> **📌 Interview Point 2: What is the difference between `git diff` and `git diff --cached`?**
> `git diff` shows modifications in the Working Directory that have not been staged yet. `git diff --cached` shows modifications in the Staging Area that are ready for the next commit.

> **📌 Interview Point 3: How does a distributed version control system differ from centralized?**
> Distributed systems clone the entire database history to every developer's local computer, enabling offline operations and backup redundancy. Centralized systems require a constant connection to a single server containing the database history.

---

## Exercises

### Exercise 1: Create first commit ⭐
**Task:** Initialize a folder `sample-project`, create a file `README.md` containing "hello world", stage it, and commit it.

<details>
<summary>💡 Hint (click to reveal)</summary>
Use `git init`, `git add README.md`, and `git commit -m "..."`.
</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```bash
mkdir sample-project
cd sample-project
git init
echo "hello world" > README.md
git add README.md
git commit -m "initial commit"
```
</details>

---

## Chapter Summary

- Git is **Distributed**; your local machine has a full database duplicate.
- Files transition: **Working Directory** (editing) → **Staging Area** (git add) → **Git Repository** (git commit).
- Check repository state at any time with **`git status`**.

---

## Previous / Next Chapter

**⬅️ [Previous: Course Overview](./ch00-course-overview.md)**

**➡️ [Next: Branching & Merging](./ch02-branching-and-merging.md)**

---

*Chapter 1 of the Git & GitHub Guide | CodeShelf*
