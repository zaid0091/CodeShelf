---
title: Vulnerable and Outdated Components (SCA)
description: Explore Software Supply Chain security and Software Composition Analysis (SCA). Learn about typosquatting, dependency auditing, and using security scanners.
order: 25
tags: [security, dependencies, sca, supply-chain, pip-audit, npm-audit]
---

# Chapter 25: Vulnerable and Outdated Components (SCA)

> **Secure your software supply chain. Learn about dependency vulnerabilities, identify risk factors like typosquatting, and configure automated package scanners.**

---

## Software Supply Chain Security

Modern applications rely heavily on open-source libraries. If you run `npm install` or `pip install`, you pull code written by third-party developers directly into your codebase. If a library you import has a vulnerability (or gets compromised by an attacker), your application is immediately compromised.

---

## Supply Chain Threat Vectors

1. **Known Vulnerabilities**: Open-source code containing security bugs reported as **CVEs** (Common Vulnerabilities and Exposures).
2. **Typosquatting**: Attackers upload malicious packages with names similar to popular ones (e.g. `reqeusts` instead of `requests`), hoping developers misspell them.
3. **Developer Account Compromise**: Attackers hijack NPM or PyPI credentials of a package maintainer to publish a malicious update containing backdoors.
4. **Dependency Confusion**: Tricking internal build managers into downloading malicious public packages instead of private internal libraries of the same name.

---

## Software Composition Analysis (SCA)

SCA is the process of auditing your dependency tree for known vulnerabilities.

### 1. Auditing Node.js Projects
NPM includes built-in security scans:
```bash
# Check dependencies
npm audit

# Auto-fix minor version vulnerabilities
npm audit fix
```

### 2. Auditing Python Projects
Use `pip-audit` to scan Python environments:
```bash
pip install pip-audit
pip-audit -r requirements.txt
```

### 3. Automated Scanning in CI/CD
Integrate scanners into your code repositories to automatically block PRs that introduce vulnerable libraries:
*   **Dependabot**: Scans lockfiles and opens PRs to upgrade dependencies.
*   **Snyk / OWASP Dependency-Check**: Scan repositories and Docker files for vulnerabilities.

---

## Enforcing Deterministic Builds

Always commit lockfiles (`package-lock.json`, `bun.lock`, `poetry.lock`, `requirements.txt` with strict hashes) to Git. This guarantees that your local development code matches production dependencies exactly.

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Set up alerts to notify development teams immediately when a new vulnerability is disclosed in existing production packages. | Installing packages using dynamic wildcards (e.g., `requests=*` or `requests>=2.0`) without lockfiles, causing servers to fetch unchecked versions during builds. |

---

## Interview Points

> **📌 Interview Point 1: What is the difference between Direct and Transitive dependencies?**
> **Direct dependencies** are packages you import explicitly in your configuration files. **Transitive dependencies** are packages imported by your direct dependencies. A vulnerability in any transitive dependency compromises your application just as severely.

---

## Exercises

### Exercise 1: Evaluate lockfile risks ⭐
**Task:** Why is running `npm install` in production builds without a lockfile risky?

<details>
<summary>✅ Solution (click to reveal)</summary>
NPM might download newer, unchecked versions of dependencies that could contain breaking bugs, API changes, or malicious code injections.
</details>

---

## Next Chapter

Continue to [Rate Limiting & Denial of Service (DoS) Prevention](./ch26-rate-limiting-dos.md) to explore application-level rate controls.
