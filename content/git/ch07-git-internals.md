---
title: Git Internals
description: Deep dive into Git architecture under the hood, the structure of the .git directory, blobs, trees, commits, tags, and ref pointers.
order: 7
tags: [git, internals, architecture, objects]
---

# Chapter 7: Git Internals

> **Understand Git under the hood — how it uses Directed Acyclic Graphs, stores data in blobs and trees, and manages references.**

---

## Table of Contents

1. [Git as a Content-Addressable Storage System](#git-as-a-content-addressable-storage-system)
2. [Anatomy of the .git Directory](#anatomy-of-the-git-directory)
3. [The Four Core Git Objects](#the-four-core-git-objects)
4. [How Blobs, Trees, and Commits Link Together](#how-blobs-trees-and-commits-link-together)
5. [How Reference Pointers Work (refs & HEAD)](#how-reference-pointers-work-refs--head)
6. [Calculating Hashes (SHA-1)](#calculating-hashes-sha-1)
7. [Best Practices](#best-practices)
8. [Common Mistakes](#common-mistakes)
9. [Interview Points](#interview-points)
10. [Exercises](#exercises)
11. [Chapter Summary](#chapter-summary)

---

## Git as a Content-Addressable Storage System

At its core, Git is a simple key-value database. 
- **The Value:** Any file content, commit, or directory tree.
- **The Key:** A unique 40-character hexadecimal SHA-1 hash calculated from the file contents and a header.

If you write some data into Git, it returns a hash. You can retrieve that exact data using only the hash at any point.

---

## Anatomy of the .git Directory

When you run `git init`, Git creates a hidden directory named `.git/` at your project root. Here is its standard structure:

```text
.git/
├── HEAD           # Points to the currently checked-out branch (e.g., ref: refs/heads/main)
├── config         # Repository-specific configuration settings
├── description    # Used by Gitweb to describe the project
├── hooks/         # Client-side or server-side scripts run on lifecycle events
├── index          # The binary Staging Area file
├── info/          # Contains global exclude patterns
├── objects/       # The database storing all Blobs, Trees, Commits, and Tags
└── refs/          # Pointers to commits (branches, tags, remotes)
```

---

## The Four Core Git Objects

Git stores all content inside `.git/objects/`. Files are compressed (using zlib) and categorized into four object types:

| Object Type | Description |
|-------------|-------------|
| **Blob** | Stores raw file data (bytes). It does **not** store metadata like filename, path, or permissions. |
| **Tree** | Represents a directory. It maps filenames, file modes, and paths to corresponding Blob hashes or other Tree hashes. |
| **Commit** | Represents a snapshot. It points to a root **Tree** object, list of parent commit hashes, author, committer, and commit message. |
| **Tag** | A persistent reference pointing to a specific commit, containing tagger name, date, and message (annotated tag). |

---

## How Blobs, Trees, and Commits Link Together

When you make a commit, Git creates a linked structure:

```text
[ Commit Object ] ---> points to ---> [ Root Tree Object ]
  - Author: Alice                       - mode 100644 blob a1b2... (index.js)
  - Message: "initial"                  - mode 040000 tree c3d4... (src/ folder tree)
  - Parent: none                                         |
                                                         v
                                                [ Src Tree Object ]
                                                  - mode 100644 blob e5f6... (utils.js)
```

- If a file does **not** change between commits, Git does not copy it. The new commit's tree simply points to the existing, pre-existing Blob hash, making Git extremely storage-efficient.

---

## How Reference Pointers Work (refs & HEAD)

In Git, branches and tags are **not** folders or copies of files. They are simple text files containing a single 40-character SHA-1 commit hash.

### 1. Branches (`refs/heads/`)
If you open `.git/refs/heads/main` in a text editor, you will see exactly one line:
`b9c8d7e6f5a4c3b2a1...` (the hash of the latest commit on main).
When you commit, Git updates this hash file.

### 2. HEAD Pointer
The `.git/HEAD` file points to the active branch reference:
`ref: refs/heads/main`
When you switch branches, Git rewrites the `HEAD` file to point to the new branch path (e.g. `ref: refs/heads/dev`).

### 3. Detached HEAD
If you checkout a specific commit directly (instead of a branch):
`git checkout b9c8d7e`
The `.git/HEAD` file changes to contain the raw commit hash directly:
`b9c8d7e6f5a4c3b2a1...`
This means you are no longer on a branch. Commits made here are orphaned once you switch branches.

---

## Calculating Hashes (SHA-1)

Git prefixes content with a header formatted as `type space size null-byte`:
`"blob 12\0hello world\n"`

It then calculates the SHA-1 hash of this combined string:
`sha1("blob 12\0hello world\n") => 557db03de997c86a4a028e1ebd3a1ceb225be238`

Git stores this object in `.git/objects/55/7db03de997c86a4a028e1ebd3a1ceb225be238` (using the first 2 characters as the directory name, and the remaining 38 as the filename to keep directories readable).

---

## Best Practices

- **Avoid modifying `.git` manually:** Never edit files inside the `.git` folder directly (with the exception of `.git/config` or hooks) as you risk corrupting the object database.
- **Use plumbing commands for scripts:** If writing scripts, use Git's plumbing commands (like `git cat-file`, `git hash-object`) instead of parsing standard user porcelain commands (like `git log`, `git status`).

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Working in Detached HEAD | New commits made in this state are lost when you switch branches | Create a branch immediately from the detached state: `git switch -c new-branch-name`. |
| Corrupting the ref files | Fails git checkouts and commands | Recover branch pointers using `git reflog` to get hashes, and manually overwrite branch ref text files. |

---

## Interview Points

> **📌 Interview Point 1: What are the four main object types stored in Git's object database?**
> Blobs (file contents), Trees (directories), Commits (metadata and root tree pointers), and Tags (annotated references).

> **📌 Interview Point 2: What is a detached HEAD state?**
> A state where the `HEAD` pointer points directly to a specific commit SHA-1 hash rather than a symbolic branch reference file (e.g. `refs/heads/main`).

> **📌 Interview Point 3: How does Git handle identical files in different folders?**
> Because Git hashes files based solely on content (blobs), two identical files in different folders will share the exact same Blob object hash. Only the Tree objects representing the directories will differ by pointing to the same Blob with different filenames.

---

## Exercises

### Exercise 1: Inspect a Git object ⭐⭐
**Task:** Run the low-level Git commands to inspect the type and content of a commit object.

<details>
<summary>💡 Hint (click to reveal)</summary>
Use `git cat-file -t` for type and `git cat-file -p` for printing content.
</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```bash
# Print type (outputs: commit)
git cat-file -t HEAD

# Print content (outputs: tree, parent, author, message)
git cat-file -p HEAD
```
</details>

---

## Chapter Summary

- Git is a **content-addressable storage** database keyed by SHA-1 hashes.
- **Blobs** store data; **Trees** map names/paths; **Commits** store snapshot states.
- **Branches** are lightweight text files containing a single commit hash.

---

## Previous / Next Chapter

**⬅️ [Previous: GitHub Actions (CI/CD)](./ch06-github-actions-cicd.md)**

**➡️ [Next: Git Best Practices](./ch08-git-best-practices.md)**

---

*Chapter 7 of the Git & GitHub Guide | CodeShelf*
