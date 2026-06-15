---
title: Branching and Merging
description: Learn how Git branches work, create and switch branches, merge styles (Fast-Forward vs Three-Way), and resolve merge conflicts step-by-step.
order: 2
tags: [git, branching, merging, conflicts]
---

# Chapter 2: Branching and Merging

> **Work in parallel without disrupting the main codebase using Git branches, and master conflict resolution.**

---

## Table of Contents

1. [What is a Branch?](#what-is-a-branch)
2. [Branch Lifecycle Commands](#branch-lifecycle-commands)
3. [Fast-Forward vs Three-Way Merges](#fast-forward-vs-three-way-merges)
4. [What is a Merge Conflict?](#what-is-a-merge-conflict)
5. [Resolving Merge Conflicts Step-by-Step](#resolving-merge-conflicts-step-by-step)
6. [Best Practices](#best-practices)
7. [Common Mistakes](#common-mistakes)
8. [Interview Points](#interview-points)
9. [Exercises](#exercises)
10. [Chapter Summary](#chapter-summary)

---

## What is a Branch?

> **Definition:** In Git, a branch is simply a lightweight, movable pointer to a specific commit. The default branch name is typically `main` or `master`.

Every time you commit, the active branch pointer moves forward automatically to point to the new commit. Git knows which branch is currently active using a special pointer called **`HEAD`**.

```text
                  [ HEAD ]
                     |
                     v
                 [ main ]
                     |
                     v
A  <---  B  <---  C (Latest Commit)
```

---

## Branch Lifecycle Commands

```bash
# 1. List all local branches (active branch is marked with *)
git branch

# 2. Create a new branch
git branch feature-login

# 3. Switch to a branch (classic)
git checkout feature-login

# 4. Switch to a branch (modern/recommended)
git switch feature-login

# 5. Create and switch to a new branch in one command
git checkout -b feature-payment
git switch -c feature-payment    # modern equivalent

# 6. Delete a branch (fails if contains unmerged work)
git branch -d feature-login

# 7. Force delete a branch (discards unmerged work)
git branch -D feature-login
```

---

## Fast-Forward vs Three-Way Merges

When you merge branch `B` into branch `A`, Git determines the merge strategy based on the commit history structure:

### 1. Fast-Forward Merge (FF)
Occurs when the target branch history has not diverged. The source branch pointer is simply moved directly forward to the destination commit pointer. No new merge commit is created.

```text
Before Merge:
main:      A <--- B
feature:   A <--- B <--- C <--- D

After Merge (git merge feature):
main, feature: A <--- B <--- C <--- D
```

### 2. Three-Way Merge (No Fast-Forward)
Occurs when the history has diverged (commits were made to both `main` and `feature` independently). Git finds a common ancestor commit and merges the histories, creating a new **merge commit** containing two parent commits.

```text
Before Merge:
main:      A <--- B <--- C
feature:   A <--- B <--- D <--- E

After Merge (git merge feature):
main:      A <--- B <--- C <--- F (Merge Commit)
                               /
feature:   A <--- B <--- D <--- E
```

---

## What is a Merge Conflict?

A merge conflict happens when Git cannot automatically merge code changes. This usually occurs when two developers modify the **same line** of the **same file** on different branches, or if one developer deletes a file that another developer is editing.

---

## Resolving Merge Conflicts Step-by-Step

If a conflict occurs, Git halts the merge process, modifies the affected files to show conflict markers, and asks you to resolve them:

### Step 1: Identify the Conflicted Files
Run `git status` to see list of unmerged paths.

### Step 2: Open Conflicted Files
Open the file in your code editor. Git inserts conflict markers:

```text
<<<<<<< HEAD
const apiUrl = "https://api.production.com";
=======
const apiUrl = "https://api.staging.com";
>>>>>>> feature-staging
```
- **`<<<<<<< HEAD`**: Commits on the active branch you are merging *into*.
- **`=======`**: The divider line between the two conflicting versions.
- **`>>>>>>> feature-staging`**: Commits on the branch you are *merging*.

### Step 3: Resolve the Code
Delete the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) and keep the correct code.

### Step 4: Stage and Commit Resolves
```bash
# Stage the resolved files
git add path/to/file.js

# Finish the merge commit
git commit -m "merge: resolve API endpoint conflict"
```

---

## Best Practices

- **Keep branches short-lived:** Merge branches back into `main` frequently to avoid massive, complex merge conflicts later.
- **Use `git merge --no-ff`:** Forces Git to create a merge commit even if a Fast-Forward merge is possible. This preserves the historical record of feature branch isolations.

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Deleting branches containing active work | Discards uncommitted or unmerged history | Only use `git branch -D` if you are absolutely sure you want to discard the work. |
| Leaving conflict markers in code | Causes compilation errors in applications | Search your workspace for `<<<<<<<` before staging and committing. |

---

## Interview Points

> **📌 Interview Point 1: What is the difference between a Fast-Forward merge and a Three-Way merge?**
> A Fast-Forward merge simply moves the branch pointer forward because there are no diverging commits. A Three-Way merge merges two diverging histories using a common ancestor, creating a new merge commit.

> **📌 Interview Point 2: What is HEAD in Git?**
> `HEAD` is a reference pointer pointing to the currently checked-out branch or commit. In a "detached HEAD" state, `HEAD` points directly to a specific commit instead of a branch.

> **📌 Interview Point 3: How do you abort a merge in progress due to conflicts?**
> You can run `git merge --abort`. This stops the merge process and returns the working directory to its pre-merge state.

---

## Exercises

### Exercise 1: Create a conflict ⭐⭐
**Task:** Create a repo, commit a file `app.js` with `const x = 1`. Create branch `dev` and change it to `const x = 2` and commit. Switch back to `main`, change it to `const x = 3` and commit. Try merging `dev` into `main` and resolve the conflict.

<details>
<summary>💡 Hint (click to reveal)</summary>
Follow the command sequence: checkout -b dev, modify file, commit, switch main, modify same line, commit, git merge dev.
</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```bash
git init
echo "const x = 1" > app.js
git add app.js
git commit -m "initial"

git switch -c dev
echo "const x = 2" > app.js
git commit -am "change on dev"

git switch main
echo "const x = 3" > app.js
git commit -am "change on main"

# Trigger conflict
git merge dev
# Open app.js, resolve conflict, then:
git add app.js
git commit -m "resolve conflict"
```
</details>

---

## Chapter Summary

- A **branch** is a movable pointer to a commit.
- Use **`git switch`** (modern) to navigate between branches.
- Conflicts must be resolved by **editing conflict markers** manually, staging, and committing.

---

## Previous / Next Chapter

**⬅️ [Previous: Git Basics](./ch01-git-basics.md)**

**➡️ [Next: Saving & Undoing Changes](./ch03-saving-and-undoing-changes.md)**

---

*Chapter 2 of the Git & GitHub Guide | CodeShelf*
