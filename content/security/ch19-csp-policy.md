---
title: Content Security Policy (CSP) - Designing & Implementing
description: Design and implement a robust Content Security Policy (CSP) to mitigate Cross-Site Scripting (XSS) and data exfiltration.
order: 19
tags: [security, csp, xss, browser-headers, policy]
---

# Chapter 19: Content Security Policy (CSP) - Designing & Implementing

> **Mitigate XSS using browser-enforced resource policies, configure strict directives, and deploy script nonces.**

---

## What is Content Security Policy (CSP)?

CSP is a security standard declared via an HTTP response header. It controls which resources (scripts, styles, images, connections) the browser is allowed to load and execute for your site.

```http
Content-Security-Policy: default-src 'self'; script-src 'self' https://trusted.com
```

### Why it matters
If an attacker successfully injects an XSS payload (e.g., `<script src="http://attacker.com/steal.js">`), the browser blocks the script from downloading because it violates the declared policy.

---

## Core CSP Directives

*   **`default-src`**: Fallback policy for other resource types.
*   **`script-src`**: Restricts JavaScript sources.
*   **`style-src`**: Restricts CSS stylesheet sources.
*   **`img-src`**: Restricts image sources.
*   **`connect-src`**: Restricts destinations for AJAX, Fetch, WebSockets, and EventSource connections.
*   **`frame-ancestors`**: Specifies which sites can embed your page in iframes (replaces `X-Frame-Options` to prevent Clickjacking).

---

## Mitigating XSS with strict CSPs

A weak CSP allows inline scripts (`'unsafe-inline'`), which undermines XSS defenses. A strong CSP restricts execution to explicitly trusted scripts.

### 1. Script Nonces (Number Used Once)
On every request, the server generates a unique, cryptographically random base64 string (a nonce) and includes it in the CSP header. Only scripts containing the matching `nonce` attribute are executed by the browser:

```http
# CSP Header
Content-Security-Policy: script-src 'nonce-RGFuZG9tMTIz'
```
```html
<!-- Valid Script -->
<script nonce="RGFuZG9tMTIz">console.log("Safe script runs");</script>

<!-- Invalid Script (Blocked because nonce is missing or incorrect) -->
<script>alert("Malicious script blocked");</script>
```

### 2. Script Hashes
For static scripts, declare the SHA-256 hash of the script contents directly in the policy:
```http
Content-Security-Policy: script-src 'sha256-qznLcsROHAZ...'
```

---

## Report-Only Mode

Deploying CSP without testing can break your site's functionality. Use `Content-Security-Policy-Report-Only` to monitor violations in real-time without blocking execution:

```http
Content-Security-Policy-Report-Only: default-src 'self'; report-uri /csp-violation-report-endpoint/
```

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Set `object-src 'none'` to block Flash and other legacy browser plugins. | Using `'unsafe-inline'` or `'unsafe-eval'` in production policies, neutralizing XSS mitigations. |

---

## Interview Points

> **📌 Interview Point 1: What is the purpose of `strict-dynamic` in CSP?**
> The `strict-dynamic` directive allows a trusted script (validated by a nonce or hash) to dynamically load downstream scripts. This simplifies CSP management on sites that load third-party widgets or dependencies.

---

## Exercises

### Exercise 1: Evaluate policy safety ⭐
**Task:** Identify the vulnerability in:
`Content-Security-Policy: default-src 'self'; script-src *`

<details>
<summary>✅ Solution (click to reveal)</summary>
The wildcard `*` allows the browser to load and execute JavaScript from any external server, leaving the site vulnerable to XSS.
</details>

---

## Next Chapter

Continue to [Essential Security Headers](./ch20-security-headers.md) to explore other critical HTTP defense headers.
