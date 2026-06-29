---
title: Introduction to the OWASP Top 10
description: Overview of the Open Web Application Security Project (OWASP) Top 10 critical security risks for web applications.
order: 2
tags: [security, owasp, vulnerabilities, standards]
---

# Chapter 2: Introduction to the OWASP Top 10

> **Get a high-level overview of the OWASP Top 10, the industry-standard classification of the most critical security vulnerabilities.**

---

## What is OWASP?

The **Open Web Application Security Project (OWASP)** is a non-profit foundation dedicated to improving software security. Their most famous project is the **OWASP Top 10**, a periodically updated report mapping out the ten most critical security risks faced by web applications.

---

## The OWASP Top 10 Categories (2021 Update)

Below is the current list of vulnerabilities, ordered by prevalence and impact:

| Category | Title | Core Threat |
|----------|-------|-------------|
| **A01** | Broken Access Control | Users accessing resources or performing actions beyond their authorized scope (e.g. IDOR). |
| **A02** | Cryptographic Failures | Weak encryption, cleartext storage of secrets, or exposing sensitive data in transit. |
| **A03** | Injection | Parsing untrusted user input directly as commands or query variables (e.g. SQLi, XSS, Command Injection). |
| **A04** | Insecure Design | Architectural design flaws and lack of threat modeling during the initial phase. |
| **A05** | Security Misconfiguration | Default credentials, verbose error logs exposing stack traces, and unhardened ports. |
| **A06** | Vulnerable & Outdated Components | Relying on open-source dependencies or libraries with known, unpatched vulnerabilities. |
| **A07** | Identification & Auth Failures | Missing multi-factor auth (MFA), weak password requirements, or session hijacking vulnerabilities. |
| **A08** | Software & Data Integrity Failures | Loading unverified plugins, deserializing untrusted objects, or unsecured CI/CD pipelines. |
| **A09** | Security Logging & Monitoring Failures | Lack of real-time alerts or logging that allows attackers to operate undetected. |
| **A10** | Server-Side Request Forgery (SSRF) | Forcing backend servers to trigger arbitrary requests to internal or external systems. |

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Perform security audits on open-source packages before building. | Assuming that using popular frameworks automatically protects against all top 10 risks. |

---

## Interview Points

> **📌 Interview Point 1: Why did Injection move down to A03 in the 2021 list?**
> Historically, Injection was A01. It moved down because frameworks have adopted secure-by-default patterns (like ORMs and templating engines). However, access control issues (A01) have increased due to microservice growth and complex routing layouts.

---

## Exercises

### Exercise 1: Map the Vulnerability ⭐
**Task:** If a site leaks detailed database connection strings in public error logs, which OWASP Top 10 category is violated?

<details>
<summary>✅ Solution (click to reveal)</summary>
This falls under **A05:2021-Security Misconfiguration** and causes **A02:2021-Cryptographic Failures** due to information disclosure of sensitive credentials.
</details>

---

## Next Chapter

Continue to [SQL Injection (SQLi) - Identification & Remediation](./ch03-sql-injection.md) to drill down into injection attacks.
