---
title: Rebasing and Rewriting History
description: Learn Git rebase, merge vs rebase trade-offs, interactive rebase (squashing, editing commits), cherry-picking commits, and recovering lost work with git reflog.
order: 4
tags: [git, rebase, history, reflog, cherry-pick]
---

# Chapter 4: Rebasing and Rewriting History

> **Maintain a clean, linear git history using rebase, squash commits with interactive rebasing, and recover deleted work with reflog.**

---

## Table of Contents

1. [What is Git Rebase?](#what-is-git-rebase)
2. [Merge vs Rebase: The Trade-Offs](#merge-vs-rebase-the-trade-offs)
3. [Interactive Rebasing (Squashing History)](#interactive-rebasing-squashing-history)
4. [Git Cherry-Pick: Selective Committing](#git-cherry-pick-selective-committing)
5. [Git Reflog: The Ultimate Safety Net](#git-reflog-the-ultimate-safety-net)
6. [Best Practices](#best-practices)
7. [Common Mistakes](#common-mistakes)
8. [Interview Points](#interview-points)
9. [Exercises](#exercises)
10. [Chapter Summary](#chapter-summary)

---

## What is Git Rebase?

Rebasing is the process of moving or combining a sequence of commits to a new base commit.

```text
Before Rebase:
main:      A <--- B <--- C
feature:   A <--- B <--- D <--- E

After Rebase (git switch feature; git rebase main):
main:      A <--- B <--- C
feature:                  \___ C <--- D' <--- E'
```
Instead of creating a merge commit, Git re-applies commits `D` and `E` on top of commit `C`, creating new commits `D'` and `E'` with brand new hashes.

---

## Merge vs Rebase: The Trade-Offs

| Action | Pros | Cons |
|--------|------|------|
| **`git merge`** | - Non-destructive: commits are never modified.<br>- Preserves actual chronological history. | - Merging branches frequently clutters history with dozens of "merge commits".<br>- Hard to trace changes in a non-linear graph. |
| **`git rebase`** | - Yields a clean, perfectly linear commit history.<br>- Simplifies code audits and git bisects. | - Destructive: rewrites history by creating new commit hashes.<br>- **Golden Rule:** Never rebase commits that have been pushed to public shared branches. |

---

## Interactive Rebasing (Squashing History)

Interactive rebasing lets you edit, combine, or delete commits in your branch history before merging them into `main`.

```bash
# Start interactive rebase for the last 4 commits
git rebase -i HEAD~4
```

This opens your default text editor showing a list of commits in **reverse chronological order** (oldest at the top):

```text
pick a1b2c3d feat: add forms
pick e4f5g6h fix: resolve form typo
pick i7j8k9l feat: connect form to backend
pick m0n1o2p refactor: clean form helper files

# Rebase commands (instructions)
# p, pick = use commit
# r, reword = use commit, but edit the commit message
# e, edit = use commit, but stop for amending
# s, squash = use commit, but meld into previous commit
# f, fixup = like "squash", but discard this commit's log message
# d, drop = remove commit
```

### Squashing Commits Example
To combine the bug fix and refactor commits into the main feature commit:

```text
pick a1b2c3d feat: add forms
squash e4f5g6h fix: resolve form typo
pick i7j8k9l feat: connect form to backend
fixup m0n1o2p refactor: clean form helper files
```
Save and close the editor. Git combines the commits and prompts you to edit the consolidated commit message.

---

## Git Cherry-Pick: Selective Committing

If you want to copy a single, specific commit from another branch (e.g. an urgent bugfix committed on `feature-payment`) onto your current branch without merging the entire branch:

```bash
# Apply a specific commit to the active branch
git cherry-pick 7a2b9d4
```

---

## Git Reflog: The Ultimate Safety Net

Have you ever executed `git reset --hard` and accidentally deleted several uncommitted features? Or deleted a branch containing valuable work?

> **Definition:** `git reflog` tracks every single update made to reference pointers (`HEAD`, branch pointers) on your local machine. It is a local log of *where your HEAD has been*.

Even if a commit is no longer referenced by any branch (a "dangling commit"), it remains in Git's database for about 30 days before being garbage collected. You can find its hash in the reflog and recover it.

```bash
# 1. View local reference log history
git reflog
```
Output:
```text
7a2b9d4 HEAD@{0}: reset: moving to HEAD~1
b9c8d7e HEAD@{1}: commit: feat: complete database integration
a1b2c3d HEAD@{2}: checkout: moving from dev to main
```

To undo the accidental reset and recover the database integration commit:
```bash
git reset --hard b9c8d7e
```

---

## Best Practices

- **Clean up before PRs:** Perform an interactive rebase locally to squash debug commits ("fix typo", "wip") before submitting a Pull Request.
- **Do not force-push blindly:** If you must update a rebased remote branch, use `git push --force-with-lease` instead of `--force`. It prevents you from overwriting coworkers' commits if they pushed changes after your last pull.

---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Rebasing shared public branches | Rewrites commit hashes, breaking git histories for all developers pulling from that branch | Only rebase branches that you own locally. |
| Forgetting conflict resolutions during rebase | Git pauses rebase; users get stuck in a looping state | Resolve conflicts, run `git add .`, then run `git rebase --continue` (never commit manually during rebase). |

---

## Interview Points

> **📌 Interview Point 1: What is the Golden Rule of Git Rebasing?**
> Never rebase commits that have been pushed to a public, shared repository branch (like `main` or `develop`). It rewrites history, forcing other developers to merge conflict-ridden duplicates of the same commits.

> **📌 Interview Point 2: What is the difference between `squash` and `fixup` in interactive rebasing?**
> Both combine a commit into the preceding one. `squash` prompts you to edit and merge the commit messages together, whereas `fixup` automatically discards the squashed commit's message.

> **📌 Interview Point 3: How can you recover a deleted branch?**
> Run `git reflog` to locate the SHA-1 hash of the commit that was at the tip of the deleted branch right before it was deleted. Then, run `git checkout -b <branch_name> <commit_sha>` to recreate it.

---

## Exercises

### Exercise 1: Recover a lost commit ⭐⭐
**Task:** You ran `git reset --hard HEAD~1` and lost your latest commit. Write the commands to find and recover it.

<details>
<summary>💡 Hint (click to reveal)</summary>
Use `reflog` to locate the commit hash, then hard reset back to it.
</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```bash
# View HEAD history
git reflog

# Find the hash right before the reset (e.g. a8b9c2d) and restore:
git reset --hard a8b9c2d
```
</details>

---

## Chapter Summary

- **`git rebase`** moves a branch base to achieve linear histories.
- Squash developer commits using **`git rebase -i`**.
- Extract single commits from other branches with **`git cherry-pick`**.
- Local commit reference history is archived in **`git reflog`**.

---

## Previous / Next Chapter

**⬅️ [Previous: Saving & Undoing Changes](./ch03-saving-and-undoing-changes.md)**

**➡️ [Next: GitHub Fundamentals](./ch05-github-fundamentals.md)**

---

*Chapter 4 of the Git & GitHub Guide | CodeShelf*
