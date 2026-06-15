---
title: Git Course Overview
description: Complete Git & GitHub course — from repository initialization and branching to interactive rebasing, workflows, and CI/CD pipelines.
order: 0
tags: [git, github, vcs, overview]
---

# Git & GitHub Course Overview

Master the industry-standard version control system — from local commits and branching to advanced history rewriting, remote collaborations, and automated GitHub Actions pipelines.

## Course structure

### Part 1: Foundations
| Chapter | Topic |
|---------|--------|
| [Git Basics](./ch01-git-basics.md) | Version control concepts, three git states, commit lifecycle, and basic commands |
| [Branching & Merging](./ch02-branching-and-merging.md) | Isolated workflows, fast-forward vs 3-way merges, resolving merge conflicts |

### Part 2: Working with History
| Chapter | Topic |
|---------|--------|
| [Saving & Undoing Changes](./ch03-saving-and-undoing-changes.md) | Undoing edits, restoring files, soft/mixed/hard resets, reverts, and stashing |
| [Rebasing & Rewriting History](./ch04-rebasing-and-history.md) | Git rebase, interactive rebasing (squash/reword), cherry-pick, and git reflog recovery |

### Part 3: Remote Collaborations & Workflows
| Chapter | Topic |
|---------|--------|
| [GitHub Fundamentals](./ch05-github-fundamentals.md) | SSH keys, remotes, Pull Requests, code review workflows, Git branching strategies |
| [GitHub Actions (CI/CD)](./ch06-github-actions-cicd.md) | Automation pipelines, workflows, triggers, runners, jobs, and build verification |

### Part 4: Advanced Git
| Chapter | Topic |
|---------|--------|
| [Git Internals](./ch07-git-internals.md) | Objects (blobs, trees, commits, tags), refs representation, inside the `.git` folder |
| [Git Best Practices](./ch08-git-best-practices.md) | Conventional commits, gitignore patterns, Git LFS for assets, and release tags |
| [Interview Preparation](./ch09-interview-prep.md) | 15 essential Git & GitHub interview questions with detailed answers |

## Prerequisites

| Requirement | Notes |
|-------------|--------|
| Operating System | Windows, macOS, or Linux |
| Software | Git CLI installed, GitHub account created |
| Shell Basics | Running basic commands in terminal/cmd |

## How to use these notes

1. **Run the commands:** Git is a muscle-memory tool. Open a terminal and run the commands on a dummy directory as you read along.
2. **Break things:** Create conflicts, delete branches, and practice recovering them using `reflog` in a safe sandbox repository.
3. **Set up SSH:** Follow the GitHub chapter to link your machine securely to GitHub.

## Learning path diagram

```text
ch01 Basics → ch02 Branching/Merging → ch03 Undoing Mistakes
                                             ↓
ch06 CI/CD ← ch05 GitHub ← ch04 Rebasing/History
    ↓
ch07 Internals → ch08 Best Practices → ch09 Interview
```

## Key definitions

> **Definition — Version Control System (VCS):** A software tool that tracks and manages changes to files over time, allowing developers to revert files to previous states, compare changes, and collaborate on a single codebase.

> **Definition — Commit:** A snapshot of your project's files at a specific point in time, stored permanently in the Git repository history with a unique SHA-1 hash.

> **Definition — Staging Area (Index):** A preparation area that holds the changes that will be included in the next commit.

## Quick start

Check your Git installation and configure your identity:

```bash
# Verify installation
git --version

# Set global developer identity (run once)
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# Check configurations
git config --list
```

## Study tips

| Tip | Detail |
|-----|--------|
| Check status constantly | Run `git status` before and after almost every command to see the current state of files. |
| Keep commits atomic | A commit should do one thing. Avoid bundling unrelated changes in a single commit. |
| Use graphical logs | Use `git log --oneline --graph --all` to visualize branching histories directly in the terminal. |

## Common mistakes to avoid

- **Committing directly to main:** Avoid making commits directly on the default branch when working in a team. Always use feature branches.
- **Committing node_modules or .env:** Ensure you add dependencies and secret keys to `.gitignore` *before* staging files.
- **Force pushing shared branches:** Never run `git push --force` on public, shared branches like `main` or `dev`. It rewrites history and disrupts coworkers.

## Time estimate

| Part | Chapters | Approx. hours |
|------|----------|---------------|
| Part 1 — Foundations | ch01–ch02 | 2–3 hours |
| Part 2 — History & Collaboration | ch03–ch05 | 3–5 hours |
| Part 3 — Advanced & CI/CD | ch06–ch09 | 4–6 hours |

## Exercises

1. Install Git and run `git config --global user.name` to verify your name is saved.
2. Create a folder named `git-sandbox`, navigate into it, and initialize it with `git init`.
3. Skim the chapters above and identify which Git workflows you use daily vs. which ones are new to you.

## Next chapter

Continue to [Git Basics](./ch01-git-basics.md) to understand commits, staging, and repositories.
