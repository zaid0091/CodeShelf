---
title: Saving and Undoing Changes
description: Master undoing changes in Git, using git restore, git reset soft/mixed/hard modes, git revert, and managing local work in progress with git stash.
order: 3
tags: [git, undo, reset, revert, stash]
---

# Chapter 3: Saving and Undoing Changes

> **Recover from mistakes, unstage accidental edits, revert public commits safely, and stash work in progress.**

---

## Table of Contents

1. [Undoing Uncommitted Local Edits](#undoing-uncommitted-local-edits)
2. [Unstaging Staged Files](#unstaging-staged-files)
3. [Git Reset: Soft, Mixed, and Hard](#git-reset-soft-mixed-and-hard)
4. [Git Revert: The Safe Public Reset](#git-revert-the-safe-public-reset)
5. [Git Stash: Temporary Shelving](#git-stash-temporary-shelving)
6. [Best Practices](#best-practices)
7. [Common Mistakes](#common-mistakes)
8. [Interview Points](#interview-points)
9. [Exercises](#exercises)
10. [Chapter Summary](#chapter-summary)

---

## Undoing Uncommitted Local Edits

If you make modifications to a file in your Working Directory but haven't staged them yet, you can discard those modifications:

- **Classic command:** `git checkout -- filename.js`
- **Modern command:** `git restore filename.js`

This overwrites your working file with the latest version matching the index (last stage or commit). **Caution:** This action is irreversible.

---

## Unstaging Staged Files

If you accidentally staged a file using `git add` but do not want it to be included in the next commit:

- **Classic command:** `git reset HEAD filename.js`
- **Modern command:** `git restore --staged filename.js`

This removes the file from the Staging Area, but keeps the physical code modifications safe in your Working Directory.

---

## Git Reset: Soft, Mixed, and Hard

The `git reset` command moves the current branch pointer (`HEAD`) to a previous commit, rewriting local history. It has three primary modes:

```text
[ Commit History ] ---> [ Staging Area ] ---> [ Working Directory ]
     HEAD moves           Soft Reset           Mixed Reset           Hard Reset
  (moves pointer)      (keeps staged)       (unstages edits)     (wipes all edits)
```

### 1. `git reset --soft <commit_sha>`
- Moves branch pointer back.
- **Result:** Keeps all your changes in the **Staging Area**. Ready for a new commit.

### 2. `git reset --mixed <commit_sha>` (Default)
- Moves branch pointer back.
- **Result:** Keeps all changes in the **Working Directory** but removes them from the **Staging Area** (unstages files).

### 3. `git reset --hard <commit_sha>`
- Moves branch pointer back.
- **Result:** **Destroys** all changes in the Staging Area and Working Directory. Files are reverted physically on disk. **Caution:** Any uncommitted work is lost forever.

---

## Git Revert: The Safe Public Reset

If you have already pushed a commit to a public remote branch (e.g., `main`), using `git reset` is dangerous because it alters history, causing conflicts for other developers.

Instead, use **`git revert <commit_sha>`**:
- It does **not** erase the commit from history.
- It calculates the exact inverse of the target commit and creates a **brand-new commit** applying those inverse changes.

```text
History:
Commit A <--- Commit B (introduced bug) <--- Commit C (revert Commit B changes)
```

---

## Git Stash: Temporary Shelving

Sometimes you need to switch branches to fix an urgent bug, but you have half-finished work in your current branch. You cannot checkout another branch with conflicts, and you don't want to make a messy "wip" commit.

> **Definition:** `git stash` takes your uncommitted modifications (staged and unstaged) and saves them on an internal stack, returning your working directory to a clean state.

```bash
# 1. Save local changes to stash stack
git stash

# 2. Save stash with a custom descriptive name
git stash save "wip: authentication form layout"

# 3. List all saved stashes on the stack
git stash list

# 4. Re-apply the top stash to working directory (keeps stash on stack)
git stash apply

# 5. Apply the top stash AND remove it from stack (recommended)
git stash pop

# 6. Apply a specific stash from index list (e.g. stash@{1})
git stash pop stash@{1}

# 7. Discard a specific stash from stack
git stash drop stash@{0}

# 8. Clear all stashes on the stack
git stash clear
```

---

## Best Practices

- **Never `reset --hard` public commits:** Only use `git reset` on local commits that have not been pushed to GitHub. Use `git revert` for pushed history.
- **Provide stash descriptions:** Always use `git stash save "message"` if you have multiple stashes to avoid confusing them in `stash list`.

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Running `git reset --hard` on unsaved edits | Overwrites all local changes on disk; cannot be undone easily | Always verify files with `git status` or copy code snippets before executing hard resets. |
| Forgetting stashed items | Stashes compile on stack, creating stale code conflicts later | Clean up stashes with `git stash pop` or `git stash clear` once they are no longer needed. |

---

## Interview Points

> **📌 Interview Point 1: What is the difference between `git reset` and `git revert`?**
> `git reset` rewrites history by moving the branch pointer back (dangerous for public branches). `git revert` creates a new commit that undoes the changes of an older commit, keeping history intact (safe for public branches).

> **📌 Interview Point 2: What is the difference between `git reset --soft` and `git reset --hard`?**
> `--soft` moves HEAD but preserves your modifications in the staging area. `--hard` moves HEAD and completely deletes all staged and unstaged modifications on disk.

> **📌 Interview Point 3: How can you stash untracked files?**
> By default, `git stash` only saves tracked files (modified files). To stash new, untracked files as well, use the `-u` (or `--include-untracked`) flag: `git stash -u`.

---

## Exercises

### Exercise 1: Safely revert a commit ⭐
**Task:** Identify the command to undo the changes of commit `a1b2c3d` in a public repository without changing history.

<details>
<summary>💡 Hint (click to reveal)</summary>
Use the command that creates a new "reverted" commit.
</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```bash
git revert a1b2c3d
```
</details>

---

## Chapter Summary

- Discard unstaged changes with **`git restore`**.
- Unstage files with **`git restore --staged`**.
- **`git reset`** rewrites local history; **`git revert`** creates safe public rollback commits.
- Save temporary work on a stack with **`git stash`**.

---

## Previous / Next Chapter

**⬅️ [Previous: Branching & Merging](./ch02-branching-and-merging.md)**

**➡️ [Next: Rebasing & Rewriting History](./ch04-rebasing-and-history.md)**

---

*Chapter 3 of the Git & GitHub Guide | CodeShelf*
