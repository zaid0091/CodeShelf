---
title: Automated Security Testing
description: Integrate security testing into development pipelines. Understand the differences between SAST, DAST, and SCA, and how to write lint checks.
order: 28
tags: [security, testing, sast, dast, cicd, semgrep, bandit]
---

# Chapter 28: Automated Security Testing

> **Automate checks in pipelines. Integrate Static Application Security Testing (SAST) and Dynamic Application Security Testing (DAST) scanners.**

---

## Security Testing Methodologies

Security testing should be automated and integrated directly into developer workflows (Shift-Left Security).

| Methodology | Definition | Stage | Example Tools |
|-------------|------------|-------|---------------|
| **SAST (Static)** | Scans source code files for dangerous patterns without running the app. | Commit / PR | Semgrep, Bandit, SonarQube |
| **DAST (Dynamic)** | Scans a running application by sending malicious payloads (simulating an attacker). | Staging / QA | OWASP ZAP, Burp Suite |
| **SCA (Composition)** | Analyzes third-party packages for known vulnerabilities. | Build | Snyk, Dependabot, npm audit |

---

## 1. Implementing SAST

SAST scanners find bugs like hardcoded secrets, weak hash algorithms, or raw SQL queries before code gets merged.

### Python: Auditing with Bandit
Bandit is a security scanner for Python code.
```bash
pip install bandit
# Scan the app directory
bandit -r app/
```

### Multilanguage: Auditing with Semgrep
Semgrep is a fast, open-source static analysis engine:
```bash
# Run Semgrep rules on your repository
semgrep --config=auto
```

---

## 2. Implementing DAST

DAST scanners find runtime issues like missing security headers, session cookie vulnerabilities, or unhandled input pathways.

### OWASP ZAP (Zed Attack Proxy)
An open-source web application vulnerability scanner. In CI/CD pipelines, ZAP can run automated baseline scans:
```bash
# ZAP Docker baseline scan of a staging URL
docker run -t ghcr.io/zaproxy/zaproxy:stable zap-baseline.py -t https://staging.example.com
```

---

## CI/CD Pipeline Integration

A standard secure deployment pipeline runs checks sequentially:

```text
Developer PR -> Run Linter/SCA -> Run SAST (Semgrep) -> Build Docker -> Run DAST -> Deploy
```
*If any stage returns critical vulnerability warnings, the pipeline fails, blocking the code from merging into master.*

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Establish baselines for SAST scanners so teams focus on *new* security issues without being overwhelmed by legacy flags. | Relying on SAST/DAST tools as a replacement for human manual code reviews and penetration tests. |

---

## Interview Points

> **📌 Interview Point 1: What is the difference between SAST and DAST?**
> **SAST** has access to the source code (white-box testing) and finds issues early without requiring a deployment. **DAST** tests the running application externally (black-box testing). DAST finds runtime configurations issues (like SSL settings, CORS, headers) that SAST cannot detect.

---

## Exercises

### Exercise 1: Evaluate scanner coverage ⭐
**Task:** Which security issue is a SAST tool likely to miss, but a DAST tool will easily catch?

<details>
<summary>✅ Solution (click to reveal)</summary>
Missing security headers (like HSTS or CSP) or weak SSL/TLS cipher configurations on the production hosting server.
</details>

---

## Next Chapter

Continue to [Interview Preparation: Web Security & OWASP Top 10](./ch29-security-interview-prep.md) to test your knowledge with mock interview questions.
---

*Chapter 28 of the Web Security Guide | CodeShelf*
