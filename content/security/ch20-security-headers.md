---
title: Essential Security Headers
description: Learn how to configure HTTP security headers like X-Frame-Options, X-Content-Type-Options, Referrer-Policy, and Permissions-Policy to harden your site.
order: 20
tags: [security, headers, clickjacking, mime-sniffing, configurations]
---

# Chapter 20: Essential Security Headers

> **Configure HTTP response headers to prevent clickjacking, block MIME-type sniffing, restrict referrer leaks, and lock down browser permissions.**

---

## 1. X-Frame-Options (Clickjacking Protection)

Clickjacking is an attack where a user is tricked into clicking an invisible element on a page they trust. The attacker loads the target site inside an invisible iframe overlaying a malicious page.

```http
# Blocks all framing attempts
X-Frame-Options: DENY

# Allows framing only by pages on the same domain
X-Frame-Options: SAMEORIGIN
```
*Note: Modern browsers prefer the CSP `frame-ancestors` directive, but keeping `X-Frame-Options` is recommended for backward compatibility.*

---

## 2. X-Content-Type-Options (MIME Sniffing)

Browsers sometimes ignore the server's declared `Content-Type` header and attempt to guess (sniff) the file content. For example, if an attacker uploads a malicious JavaScript file disguised as an image (`avatar.png`), the browser might execute it as JS anyway.

**Remediation**: Force strict adherence to declared mime types:
```http
X-Content-Type-Options: nosniff
```

---

## 3. Referrer-Policy

When a user clicks an outbound link, the browser sends the current page's URL in the `Referer` header to the destination site. This can leak private data (like reset tokens or IDs) embedded in the URL query.

**Remediation**: Set a strict referrer policy:
```http
Referrer-Policy: strict-origin-when-cross-origin
```
*   *Behavior:* Sends the full URL when navigating same-origin, but only sends the domain (origin) when linking to external domains, and sends nothing when downgrading from HTTPS to HTTP.

---

## 4. Permissions-Policy (Feature-Policy)

Restricts which browser features and hardware APIs (camera, microphone, geolocation) can be accessed by your page and any embedded third-party iframes:

```http
Permissions-Policy: camera=(), microphone=(), geolocation=(self)
```

---

## Configuration Example: Nginx

Add these headers to your server blocks in `nginx.conf`:

```nginx
server {
    add_header X-Frame-Options "DENY" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;
    add_header Permissions-Policy "camera=(), microphone=(), geolocation=(self)" always;
}
```

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Use security scanning sites like `securityheaders.com` to analyze your domain and verify header configurations. | Omitting the `always` parameter in Nginx, which prevents headers from being sent on error responses (like 404 or 500 pages). |

---

## Interview Points

> **📌 Interview Point 1: How does MIME sniffing lead to XSS?**
> If a user is allowed to upload files (e.g. images) and the server returns them without setting `X-Content-Type-Options: nosniff`, the browser may sniff a text file containing HTML/JS payload and execute it as client-side script, triggering XSS.

---

## Exercises

### Exercise 1: Identify Clickjacking risk ⭐
**Task:** If your site does not return `X-Frame-Options` or CSP `frame-ancestors` headers, what is the impact?

<details>
<summary>✅ Solution (click to reveal)</summary>
Any website can embed your application inside an iframe and execute a Clickjacking attack.
</details>

---

## Next Chapter

Continue to [HTTPS-Only Cookie Flag Attributes](./ch21-cookie-security-flags.md) to explore session cookie protection.
