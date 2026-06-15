---
title: Git Best Practices
description: Master git commit hygiene, write conventional commits, configure .gitignore patterns, manage large files with Git LFS, and use SemVer tagging.
order: 8
tags: [git, best-practices, conventional-commits, git-lfs, semver]
---

# Chapter 8: Git Best Practices

> **Write expressive conventional commits, manage large binaries with Git LFS, configure complex gitignores, and tag releases.**

---

## Table of Contents

1. [Conventional Commit Messages](#conventional-commit-messages)
2. [Advanced .gitignore Patterns](#advanced-gitignore-patterns)
3. [Managing Large Assets with Git LFS](#managing-large-assets-with-git-lfs)
4. [Semantic Versioning and Git Tags](#semantic-versioning-and-git-tags)
5. [Cleaning Local Branches (prune)](#cleaning-local-branches-prune)
6. [Best Practices](#best-practices)
7. [Common Mistakes](#common-mistakes)
8. [Interview Points](#interview-points)
9. [Exercises](#exercises)
10. [Chapter Summary](#chapter-summary)

---

## Conventional Commit Messages

Conventional Commits is a lightweight convention on top of commit messages, providing a set of rules for creating clean, machine-readable histories.

### Format
```text
<type>(<optional scope>): <description>

[optional body]

[optional footer(s)]
```

### Common Types:
- **`feat`:** A new feature introduced (corresponds to `MINOR` version).
- **`fix`:** A bug fix (corresponds to `PATCH` version).
- **`docs`:** Documentation changes only.
- **`style`:** Code formatting changes (missing semi-colons, whitespace adjustments - no functional logic change).
- **`refactor`:** Code changes that neither fix a bug nor add a feature.
- **`perf`:** Code changes that improve performance.
- **`test`:** Adding or correcting test suites.
- **`chore`:** Updating build scripts, dependencies, tool configurations.

### Example
```text
feat(auth): support multi-factor authentication

Users can now configure TOTP codes inside dashboard settings.

Closes #142
```

---

## Advanced .gitignore Patterns

A `.gitignore` file specifies intentionally untracked files that Git should ignore.

### Pattern Rules
- **`#`**: Comment.
- **`logs/`**: Ignores the `logs` folder and all contents recursively.
- **`*.log`**: Ignores any file ending with `.log` in any directory.
- **`!important.log`**: Re-tracks (includes) `important.log` even if `*.log` is ignored.
- **`**/config/`**: Ignores `config` directories located anywhere in the repository structure.
- **`temp/*.txt`**: Ignores `temp/notes.txt`, but not subdirectories like `temp/docs/notes.txt`.

---

## Managing Large Assets with Git LFS

Git tracks every modification of every file in history. If you commit a **100MB video**, Git saves a copy of that video in the database. If you modify it and commit again, another copy is stored. This makes clone payloads massive and slows down repository performance.

> **Definition:** Git Large File Storage (LFS) replaces large files (like audio, video, graphics, datasets) with tiny text pointer files inside Git, while storing the actual large binaries on a remote cloud server.

```text
Local Repository                Remote Host (GitHub)
+-----------------------+      push      +-----------------------+
| Git commits (small)   |  ----------->  | Git commits (small)   |
| LFS Pointers (150b)   |                | LFS Pointers (150b)   |
+-----------------------+                +-----------------------+
| LFS Binary assets     |  ----------->  | LFS Storage Bucket    |
| (100MB video)         |                | (100MB video)         |
+-----------------------+                +-----------------------+
```

### Using Git LFS
```bash
# 1. Install LFS extension locally (run once)
git lfs install

# 2. Track specific large file types
git lfs track "*.mp4"
git lfs track "*.psd"

# 3. Commit the tracking configuration file (mandatory)
git add .gitattributes
git commit -m "chore: setup git lfs tracking configurations"

# 4. Stage and commit files normally
git add presentation.mp4
git commit -m "media: add introduction video"
```

---

## Semantic Versioning and Git Tags

Git tags are pointers to specific commits, typically used to mark release milestones (e.g. `v1.0.0`).

### 1. Tag Types
- **Lightweight Tag:** A simple pointer to a commit (just a branch-like file without metadata).
  `git tag v1.0.0`
- **Annotated Tag:** Stored as a full object in the database, containing author name, email, date, and a custom tag message. **Recommended** for formal releases.
  `git tag -a v1.0.0 -m "release version 1.0.0"`

### 2. Semantic Versioning (SemVer)
Version numbers follow the pattern **`MAJOR.MINOR.PATCH`**:
- **`MAJOR` (1.0.0 -> 2.0.0):** Incompatible API changes (breaking changes).
- **`MINOR` (1.0.0 -> 1.1.0):** Backward-compatible new features.
- **`PATCH` (1.0.0 -> 1.0.1):** Backward-compatible bug fixes.

---

## Cleaning Local Branches (prune)

When coworkers delete merged feature branches on GitHub, your local repository still retains remote-tracking pointers to them (e.g., `origin/feature-login` still shows in `git branch -a`).

To clean up stale tracking pointers:
```bash
# Fetch and remove local references to deleted remote branches
git fetch --prune
```

---

## Best Practices

- **Never track secrets:** Always include API keys, passwords, and `.env` files in your `.gitignore` from day one.
- **Write meaningful commits:** Follow the Conventional Commits specification to allow release automation tools (like Semantic Release) to auto-generate changelogs and bump versions automatically.

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Untracking files after they were committed | Files already recorded in history remain in Git's index database even if added to `.gitignore` later | Run `git rm --cached <file>` to remove it from tracking, then commit the change. |
| Forgetting to push tags | Running `git push` does not push local tags to remote servers automatically | Run `git push origin --tags` to upload your release tags. |

---

## Interview Points

> **📌 Interview Point 1: What is Git LFS and why is it used?**
> Git Large File Storage replaces large binary files (like media, datasets, ZIPs) with lightweight text pointer files in Git's database, while uploading the actual binaries to external servers. This keeps clone payloads small.

> **📌 Interview Point 2: What is the difference between a lightweight tag and an annotated tag?**
> A lightweight tag is a simple pointer to a commit. An annotated tag is stored as a full Git database object containing author metadata, timestamp, and a custom tag message (ideal for releases).

> **📌 Interview Point 3: How do you ignore a file that has already been tracked and committed?**
> You must run `git rm --cached <file_name>` to remove it from Git's tracking index while preserving the file locally, then commit that deletion and add the path to `.gitignore`.

---

## Exercises

### Exercise 1: Write a conventional commit ⭐
**Task:** Write a conventional commit message for a bug fix in the payment module correcting checkout currency rounding.

<details>
<summary>💡 Hint (click to reveal)</summary>
Use `fix(scope): message` format.
</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```text
fix(payment): resolve currency rounding issues on checkout
```
</details>

---

## Chapter Summary

- Write structured histories using **Conventional Commits**.
- Exclude large binaries from bloating clone payloads using **Git LFS**.
- Tag release milestones using **Annotated Tags** matching **SemVer** specifications.

---

## Previous / Next Chapter

**⬅️ [Previous: Git Internals](./ch07-git-internals.md)**

**➡️ [Next: Interview Preparation](./ch09-interview-prep.md)**

---

*Chapter 8 of the Git & GitHub Guide | CodeShelf*
