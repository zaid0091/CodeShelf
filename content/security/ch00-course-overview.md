---
title: Web Security Course Overview
description: Course roadmap and study guide for Web Security and the OWASP Top 10 vulnerabilities.
order: 0
tags: [security, owasp, web-security, overview]
---

# Web Security & OWASP Top 10 Course Overview

Welcome to the **Web Security and OWASP Top 10** course. This developer-focused resource is designed to teach you how to write resilient web applications, identify vulnerabilities, apply security controls, and defend against modern cyber threats.

## Course Structure

The course is split into 30 chapters across 7 distinct parts:

### Part 1: Course Foundations
*   [Ch 0: Course Overview](./ch00-course-overview.md)
*   [Ch 1: The Security Mindset & Threat Modeling](./ch01-security-mindset.md)
*   [Ch 2: Introduction to the OWASP Top 10](./ch02-owasp-top-10-overview.md)

### Part 2: Injection & Input Validation (A03:2021)
*   [Ch 3: SQL Injection (SQLi) - Identification & Remediation](./ch03-sql-injection.md)
*   [Ch 4: NoSQL & ORM Injection Attacks](./ch04-nosql-orm-injection.md)
*   [Ch 5: Command Injection & Path Traversal](./ch05-command-injection-traversal.md)
*   [Ch 6: Cross-Site Scripting (XSS) - Reflected & Stored](./ch06-xss-reflected-stored.md)
*   [Ch 7: Cross-Site Scripting (XSS) - DOM-Based & Prevention](./ch07-xss-dom-prevention.md)
*   [Ch 8: HTML Sanitization & Safe Output Encoding](./ch08-html-sanitization-encoding.md)

### Part 3: Access Control & Sessions (A01:2021)
*   [Ch 9: Cross-Site Request Forgery (CSRF) & SameSite Cookies](./ch09-csrf-samesite-cookies.md)
*   [Ch 10: Broken Access Control & IDOR](./ch10-broken-access-control-idor.md)
*   [Ch 11: Session Management: Hijacking, Fixation, and Timeouts](./ch11-session-management.md)
*   [Ch 12: Securing JSON Web Tokens (JWT) in Development & Prod](./ch12-securing-jwts.md)
*   [Ch 13: OAuth 2.0 & OIDC Security Best Practices](./ch13-oauth2-oidc-security.md)

### Part 4: Cryptography & Sensitive Data (A02:2021)
*   [Ch 14: Cryptographic Failures: Hashing vs. Encryption](./ch14-cryptographic-failures.md)
*   [Ch 15: Password Hashing (Bcrypt, Argon2, PBKDF2)](./ch15-password-hashing.md)
*   [Ch 16: Managing Secrets & API Keys](./ch16-managing-secrets.md)
*   [Ch 17: Securing Transit: TLS, HSTS, and Certificate Pinning](./ch17-securing-transit.md)

### Part 5: Browser Security & Headers
*   [Ch 18: CORS (Cross-Origin Resource Sharing) Misconfigurations](./ch18-cors-misconfigurations.md)
*   [Ch 19: Content Security Policy (CSP) - Designing & Implementing](./ch19-csp-policy.md)
*   [Ch 20: Essential Security Headers](./ch20-security-headers.md)
*   [Ch 21: HTTPS-Only Cookie Flag Attributes](./ch21-cookie-security-flags.md)

### Part 6: Server & Infrastructure (A05:2021)
*   [Ch 22: Server-Side Request Forgery (SSRF)](./ch22-ssrf-attacks.md)
*   [Ch 23: XML External Entity (XXE) Injection](./ch23-xxe-injection.md)
*   [Ch 24: Secure Defaults & Hardening Web Servers](./ch24-hardening-web-servers.md)
*   [Ch 25: Vulnerable and Outdated Components (SCA)](./ch25-dependency-vulnerabilities.md)

### Part 7: Logging, Monitoring, & Testing (A09:2021)
*   [Ch 26: Rate Limiting & Denial of Service (DoS) Prevention](./ch26-rate-limiting-dos.md)
*   [Ch 27: Security Logging & Monitoring](./ch27-security-logging-monitoring.md)
*   [Ch 28: Automated Security Testing](./ch28-automated-security-testing.md)
*   [Ch 29: Interview Preparation: Web Security & OWASP Top 10](./ch29-security-interview-prep.md)

---

## Study Guide & Methodology

1. **Shift Left**: Focus on writing secure code during early design rather than trying to patch bugs in production.
2. **Never Trust User Input**: Consider all incoming data (cookies, query inputs, payloads, headers) hostile and validate it.
3. **Defense in Depth**: Implement multi-layered controls (e.g. database parameterized queries AND input sanitization AND strict CSP headers).

---

## Next Chapter

Continue to [The Security Mindset & Threat Modeling](./ch01-security-mindset.md) to understand CIA principles and basic threat modelling.
