---
title: CORS (Cross-Origin Resource Sharing) Misconfigurations
description: Understand the Same-Origin Policy (SOP) and how Cross-Origin Resource Sharing (CORS) misconfigurations allow malicious websites to steal private data.
order: 18
tags: [security, cors, sop, browser-security, configuration]
---

# Chapter 18: CORS (Cross-Origin Resource Sharing) Misconfigurations

> **Master the Same-Origin Policy, examine how incorrect CORS configurations expose data to external origins, and write secure CORS rules.**

---

## Same-Origin Policy (SOP)

The Same-Origin Policy is a fundamental browser security control. It prevents a script loaded from one origin (domain) from reading data from another origin. Two URLs have the same origin if their **Protocol**, **Domain (Host)**, and **Port** match exactly.

| URL 1 | URL 2 | Same Origin? | Reason |
|-------|-------|--------------|--------|
| `https://example.com/api` | `https://example.com/data` | **Yes** | Protocol, host, and port match. |
| `https://example.com` | `http://example.com` | **No** | Protocol mismatch (HTTPS vs. HTTP). |
| `https://example.com` | `https://sub.example.com` | **No** | Host mismatch (subdomain). |

*SOP only blocks **reading** data cross-origin. It does not block **sending** data (which is why CSRF attacks are possible).*

---

## What is CORS?

CORS is an HTTP-header-based mechanism that relaxes the Same-Origin Policy. It allows servers to explicitly declare which external origins are authorized to read their API responses.

Key Headers:
*   **`Access-Control-Allow-Origin`**: Specifies allowed domains.
*   **`Access-Control-Allow-Credentials`**: Set to `true` to allow requests to include cookies and authorization headers.

---

## Vulnerable CORS Configurations

### 1. Reflected Origin (Wildcard implementation)
If an application wants to allow multiple domains but also support cookies (credentials), they cannot use `Access-Control-Allow-Origin: *` (browsers block credentials with wildcard origins). To bypass this, developers sometimes write logic that reads the request's `Origin` header and echoes it back:

```http
# Request
GET /api/user-data HTTP/1.1
Host: api.example.com
Origin: https://evil.com

# Vulnerable Response
HTTP/1.1 200 OK
Access-Control-Allow-Origin: https://evil.com
Access-Control-Allow-Credentials: true
```
*Impact: Any website (like `evil.com`) can make credentialed requests to your API and read the victim's private user data.*

### 2. Regex parsing vulnerabilities
Configuring origins using weak regular expressions can allow bypasses:
```regex
# Intended: https://example.com
# Regex: .*example\.com
# Vulnerable match: https://attacker-example.com
```

---

## Remediation: Secure CORS Setup

1. **Explicit Whitelists**: Maintain a strict list of allowed origin strings.
2. **Handle Null Origin**: Never trust `Access-Control-Allow-Origin: null`, which can be spoofed using iframe sandboxes.

```python
# Secure FastAPI example
origins = [
    "https://example.com",
    "https://admin.example.com",
]
```

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Restrict CORS headers to public APIs only. If your API is purely internal, disable CORS entirely. | Reflecting the incoming `Origin` request header dynamically without validating it against a strict whitelist. |

---

## Interview Points

> **📌 Interview Point 1: What is a Preflight request?**
> A preflight request is an HTTP `OPTIONS` request sent automatically by the browser before the actual request. It checks if the server supports the requested HTTP method and headers, preventing unauthorized state-changing operations on target endpoints.

---

## Exercises

### Exercise 1: Evaluate CORS validity ⭐
**Task:** Is this response valid in a modern browser?
```http
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
```

<details>
<summary>✅ Solution (click to reveal)</summary>
No. Modern browsers reject CORS responses that combine a wildcard origin (`*`) with the `Allow-Credentials: true` flag.
</details>

---

## Next Chapter

Continue to [Content Security Policy (CSP) - Designing & Implementing](./ch19-csp-policy.md) to explore client resource controls.
