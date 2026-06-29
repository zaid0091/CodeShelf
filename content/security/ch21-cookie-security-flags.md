---
title: HTTPS-Only Cookie Flag Attributes
description: In-depth analysis of cookie attributes including HttpOnly, Secure, SameSite, and modern security prefixes like __Host- and __Secure-.
order: 21
tags: [security, cookies, httponly, secure-cookie, host-prefix, session]
---

# Chapter 21: HTTPS-Only Cookie Flag Attributes

> **Lock down session cookies, prevent JavaScript access, enforce transit over HTTPS, and implement modern host prefixes.**

---

## Cookie Security Flags

Cookies are the primary mechanism for session state storage. To secure them, servers use specific attributes in the `Set-Cookie` header.

```http
Set-Cookie: session_id=abc123xyz; Secure; HttpOnly; SameSite=Lax
```

---

## Flag Breakdown

### 1. `HttpOnly`
Prevents client-side scripts (JavaScript) from reading the cookie value (e.g. `document.cookie`).
*   **Defense**: Mitigates **XSS** session-id theft. Even if an attacker executes code, they cannot read the cookie string.

### 2. `Secure`
Ensures the cookie is only transmitted over encrypted connections (HTTPS).
*   **Defense**: Mitigates **Man-in-the-Middle** sniffing on unencrypted HTTP networks.

### 3. `SameSite`
Controls cookie transmission on cross-site requests.
*   **`Strict`**: Cookie is never sent on cross-site requests.
*   **`Lax`**: Cookie is blocked on cross-site sub-requests (like image embeds or AJAX), but sent when users click links navigating to the site.
*   **`None`**: Cookie is always sent (Requires the `Secure` flag to be set).

---

## Modern Cookie Prefixes

To prevent cookies from being domain-shadowed, overwritten by subdomains, or switched to insecure connections, use modern browser prefixes in the cookie name:

### 1. `__Secure-` Prefix
Enforces that the cookie must be set with the `Secure` attribute.
```http
Set-Cookie: __Secure-sess=id123; Secure; ...
```

### 2. `__Host-` Prefix
Enforces maximum constraints:
1. Must contain the `Secure` attribute.
2. Must *not* contain a `Domain` attribute (binds it strictly to the current host, ignoring subdomains).
3. Must specify `Path=/`.
```http
Set-Cookie: __Host-sess=id123; Secure; Path=/
```
*If a subdomain attempts to set or override a `__Host-` cookie, the browser rejects it, protecting against cookie hijacking from vulnerable subdomains.*

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Use the `__Host-` prefix for all sensitive session identifiers. | Omitting `HttpOnly` on sensitive session cookies, leaving them vulnerable to XSS thefts. |

---

## Interview Points

> **📌 Interview Point 1: What is Cookie Toss/Shadowing?**
> An attack where a compromised subdomain (e.g., `vulnerable.example.com`) sets a cookie with the parent domain scope (`domain=example.com`). The browser will send this cookie to the main app (`example.com`), shadowing (overwriting) the genuine session cookie. Using the `__Host-` prefix blocks subdomains from doing this.

---

## Exercises

### Exercise 1: Identify valid prefix configurations ⭐
**Task:** Identify the error in:
`Set-Cookie: __Host-id=123; Path=/`

<details>
<summary>✅ Solution (click to reveal)</summary>
It is missing the `Secure` attribute. The `__Host-` prefix requires the cookie to be set with `Secure` or the browser will reject it.
</details>

---

## Next Chapter

Continue to [Server-Side Request Forgery (SSRF)](./ch22-ssrf-attacks.md) to study backend query attacks.
