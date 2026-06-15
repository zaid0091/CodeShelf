---
title: Interview Preparation
description: Top 15 Git & GitHub technical interview questions and answers, quick-revision cheat sheet, and study prep.
order: 9
tags: [git, interview, devops, study-guide]
---

# Chapter 9: Interview Preparation

> **Study these high-frequency interview questions and answers on Git and GitHub. Practice explaining them out loud during prep.**

---

## Table of Contents

1. [Top 15 Interview Questions & Answers](#top-15-interview-questions--answers)
2. [Quick-Revision Command Cheat Sheet](#quick-revision-command-cheat-sheet)
3. [Key Concepts Matcher](#key-concepts-matcher)
4. [Course Wrap-Up](#course-wrap-up)

---

## Top 15 Interview Questions & Answers

---

### Q1: What is the difference between `git fetch` and `git pull`?
**Answer:**
- **`git fetch`** downloads remote branches, commits, and tags to your local `.git` repository. It does **not** alter your local working files. It is a read-only metadata update.
- **`git pull`** downloads the changes (`git fetch`) and immediately tries to merge them into your current checked-out branch (`git merge`). It alters your working directory and can cause merge conflicts.

---

### Q2: What is the difference between `git merge` and `git rebase`?
**Answer:**
- **`git merge`** combines branches by creating a new **merge commit** (if histories have diverged). It preserves the exact chronological history of all commits, showing branches branching and merging.
- **`git rebase`** re-applies commits from your branch on top of a target branch, creating a completely **linear** history. It rewrites history by generating new commit hashes.

---

### Q3: Explain the difference between `git reset` and `git revert`.
**Answer:**
- **`git reset`** moves the branch pointer (`HEAD`) backward to a previous commit, removing newer commits from history. This is destructive and should only be run on local, unpushed branches.
- **`git revert`** creates a **new commit** that does the exact opposite of a target commit. It does not alter history, making it safe for public, shared branches.

---

### Q4: What are the differences between `git reset --soft`, `--mixed`, and `--hard`?
**Answer:**
- **`--soft`:** Moves HEAD to the target commit. Preserves all changes in the **Staging Area**.
- **`--mixed` (default):** Moves HEAD. Preserves changes in the **Working Directory** but unstages them.
- **`--hard`:** Moves HEAD and **deletes** all changes in both the Staging Area and Working Directory, reverting your files on disk.

---

### Q5: What is a detached HEAD state and how do you recover from it?
**Answer:**
A detached HEAD state occurs when `HEAD` points directly to a specific commit hash rather than a branch pointer. Commits made here are not saved to any branch. 
To recover, you can create a new branch from this commit using `git switch -c new-branch-name` or return to a branch using `git switch main` (discarding the detached commits).

---

### Q6: What is `git reflog` and when would you use it?
**Answer:**
`git reflog` (reference log) is a local log that records every movement of `HEAD` and branch references. It tracks when you checkout, reset, commit, or merge. You use it to find the hashes of commits or deleted branches that are no longer referenced, allowing you to recover lost work.

---

### Q7: How does Git store data under the hood? Explain Blobs, Trees, and Commits.
**Answer:**
Git is a content-addressable key-value store.
- **Blob:** Stores raw file data. No filenames or metadata.
- **Tree:** Represents directories. Maps filenames and permissions to Blob or other Tree hashes.
- **Commit:** Points to a root Tree, parent commit hashes, author metadata, and the commit message.

---

### Q8: How do you remove a file from tracking without deleting it from your local disk?
**Answer:**
Use the command **`git rm --cached <filename>`**. This removes the file from Git's index (so it won't be tracked in the next commit) but preserves it on your local hard drive. Remember to add the file path to `.gitignore` to prevent tracking it again.

---

### Q9: What is Git LFS and why is it used?
**Answer:**
Git Large File Storage replaces large binary files (like images, video, datasets) with tiny text pointer files in Git's database. The actual heavy files are stored on a remote server. This keeps the Git repository database light, speeding up `git clone` and `git fetch` operations.

---

### Q10: What is the Golden Rule of rebasing?
**Answer:**
**Never rebase commits that have been pushed to a public, shared repository branch.** Rebasing rewrites history, changing commit hashes. If you force-push a rebased public branch, you break the history for other developers, causing painful duplicate merge conflicts.

---

### Q11: What is the difference between `git merge --ff` and `git merge --no-ff`?
**Answer:**
- **`--ff` (Fast-Forward):** If the destination branch has no diverging commits, Git simply moves the branch pointer forward without creating a new commit.
- **`--no-ff` (No Fast-Forward):** Forces Git to create a new merge commit even if a fast-forward is possible. This preserves the historical record of feature branch isolations.

---

### Q12: How do you resolve a merge conflict?
**Answer:**
1. Run `git status` to identify conflicted files.
2. Open the files in an editor and search for conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
3. Edit the code to keep the correct version and delete the conflict markers.
4. Run `git add <filename>` to mark it resolved, and execute `git commit` to complete the merge.

---

### Q13: How does `git cherry-pick` work?
**Answer:**
`git cherry-pick <commit_sha>` allows you to copy a single commit from another branch and apply it to your current checked-out branch. This is useful for pulling isolated bug fixes or features without merging the entire source branch.

---

### Q14: Explain Conventional Commits.
**Answer:**
Conventional Commits is a specification for commit messages. It formats commits as `<type>(<scope>): <description>` (e.g., `feat(auth): add MFA`). Types like `feat`, `fix`, `docs`, and `refactor` make commit history machine-readable, enabling automated changelogs and version bumps.

---

### Q15: How do you pull a remote branch that you don't have locally?
**Answer:**
First run `git fetch` to download remote branches. Then, checkout the branch by name using `git checkout <branch_name>` or `git switch <branch_name>`. Git automatically creates a local branch tracking the remote branch.

---

## Quick-Revision Command Cheat Sheet

```bash
# Display linear commit graph
git log --oneline --graph --all

# Create and switch to a feature branch (modern)
git switch -c feature-name

# Unstage a file (modern)
git restore --staged filename.js

# Discard local unstaged edits (modern)
git restore filename.js

# Shelve local edits
git stash && git stash pop

# Clean remote tracking references
git fetch --prune
```

---

## Key Concepts Matcher

| Term | Matches |
|------|---------|
| **Plumbing** | Low-level Git utility commands (e.g. `cat-file`) |
| **Porcelain** | User-friendly high-level Git commands (e.g. `commit`) |
| **index** | The internal name for the Staging Area |
| **reflog** | Local history logs of HEAD movements |

---

## Course Wrap-Up

Congratulations! You have completed the Git & GitHub revision notes. You now understand how Git works under the hood, how to manage branches, rewrite history, collaborate on GitHub, and automate workflows.

---

## Previous / Next Chapter

**⬅️ [Previous: Git Best Practices](./ch08-git-best-practices.md)**

---

*Chapter 9 of the Git & GitHub Guide | CodeShelf*
