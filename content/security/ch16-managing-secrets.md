---
title: Managing Secrets & API Keys
description: Learn how to manage application secrets, API keys, database credentials, and certificates securely without hardcoding them in git.
order: 16
tags: [security, secrets, env-vars, vault, credentials]
---

# Chapter 16: Managing Secrets & API Keys

> **Retire hardcoded credentials. Learn how to store variables in local environments, deploy secrets vaults, and scrub credentials from git history.**

---

## The Hardcoded Secret Risk

Hardcoding database passwords, OAuth client secrets, or private keys directly in your codebase is a critical vulnerability. Once committed, these credentials persist in the Git history, making them visible to anyone with access to the repository (or the public if pushed to public hubs). Attackers run automated crawlers to scan repository hosts for exposed keys.

---

## 1. Local Configuration (.env Files)

The baseline mitigation is to isolate configurations from source code using environment variables.

### The Setup
1. Define keys in a local configuration file named `.env`:
   ```bash
   DATABASE_URL=postgresql://db_user:my_secret_pass@localhost:5432/mydb
   JWT_SECRET=super_secret_string_123
   ```
2. **CRITICAL**: Add `.env` to your `.gitignore` file to ensure it is never committed to Git.
3. Access these keys in your code using libraries like `dotenv` or Pydantic.

---

## 2. Dedicated Secrets Managers

For production environments, use centralized Secrets Managers (e.g. AWS Secrets Manager, HashiCorp Vault, Doppler, GCP Secret Manager).

### Benefits
*   **Centralization**: Multiple servers read configurations dynamically from a single source.
*   **Access Audits**: Detailed logs indicating *which* service accessed *which* secret and when.
*   **Dynamic Rotation**: Automatically rotates API keys and database credentials periodically without service downtime.

---

## 3. Scrubbing Leaked Secrets from Git History

If you accidentially commit a secret, changing the code in a new commit does *not* delete it from past Git commit logs.

### Remediation
1. Immediately **revoke and rotate** the leaked secret (it must be considered compromised).
2. Clean the git history using specialized tools:
   ```bash
   # Using git-filter-repo
   git-filter-repo --path my-secrets.txt --invert-paths
   ```
   *(Avoid using basic `git filter-branch`, which is legacy and easily corrupts history).*

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Set up secrets scanning tools (like `git-secrets`, `TruffleHog`, or GitHub Secret Scanning) in your CI/CD pipelines. | Committing templates like `.env.example` containing active production keys. |

---

## Interview Points

> **📌 Interview Point 1: Why is changing code in a new commit insufficient to secure a leaked credential?**
> Git records the state of your codebase at every commit. Anyone checking out the repository can run `git log -p` or inspect past commit objects to read the deleted lines containing the credentials.

---

## Exercises

### Exercise 1: Evaluate gitignore safety ⭐
**Task:** If you add `.env` to `.gitignore` *after* you have already committed `.env` to the repository, does git ignore it?

<details>
<summary>✅ Solution (click to reveal)</summary>
No. Git tracks files that are already indexed. You must untrack the file first using `git rm --cached .env` before git respects the `.gitignore` rule.
</details>

---

## Next Chapter

Continue to [Securing Transit: TLS, HSTS, and Certificate Pinning](./ch17-securing-transit.md) to explore networking encryption.
