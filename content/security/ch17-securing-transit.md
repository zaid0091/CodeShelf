---
title: "Securing Transit: TLS, HSTS, and Certificate Pinning"
description: Understand how to secure data in transit using HTTPS, TLS configurations, HTTP Strict Transport Security (HSTS), and Certificate Pinning.
order: 17
tags: [security, tls, hsts, https, transit, network]
---

# Chapter 17: Securing Transit: TLS, HSTS, and Certificate Pinning

> **Prevent Man-in-the-Middle (MITM) snooping, configure secure TLS channels, implement HSTS policies, and evaluate certificate pinning.**

---

## The Risk: Unencrypted HTTP Traffic

If an application uses unencrypted HTTP protocols, all requests and responses flow in clear text over intermediate routers. Attackers on the same network (e.g. public Wi-Fi) can perform a **Man-in-the-Middle (MITM)** attack to sniff passwords, capture session cookies, and modify response HTML.

---

## 1. TLS (Transport Layer Security)

**HTTPS** is HTTP encapsulated in TLS. It provides three guarantees:
1. **Confidentiality**: Encrypts data to prevent sniffing.
2. **Integrity**: Verifies that data has not been modified in transit.
3. **Authentication**: Uses SSL certificates to verify the server's identity.

### Secure TLS Settings
*   Disable old protocols: Retire **SSLv3**, **TLS 1.0**, and **TLS 1.1** (they have known cryptographic vulnerabilities).
*   Enforce **TLS 1.2** and **TLS 1.3** exclusively.

---

## 2. HSTS (HTTP Strict Transport Security)

If a user types `http://example.com`, the browser first executes an unencrypted HTTP request before the server redirects them to `https://example.com`. This redirect transition can be intercepted by attackers (e.g., using toolsets like `sslstrip`).

**HSTS** is an HTTP response header that instructs browsers to convert all future HTTP requests for that domain to HTTPS automatically:

```http
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```
*   `max-age=31536000`: Applies the rule for 1 year.
*   `includeSubDomains`: Extends the rule to all subdomains.
*   `preload`: Submits your site to a browser-hardcoded registry of HTTPS-only sites, protecting users during their *very first* visit.

---

## 3. Certificate & SSL Pinning

Typically, browsers trust any certificate signed by a recognized Certificate Authority (CA). If a CA is compromised, attackers can issue forged certificates for your domain to execute MITM attacks.

**Certificate Pinning** hardcodes the server's specific certificate public key inside client applications (like iOS/Android mobile apps). The client rejects any connection if the server's certificate signature does not match the pinned public key.

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Set HSTS headers with long lifetimes and request inclusion in browser preload registries. | Redirecting HTTP to HTTPS without setting HSTS headers, leaving the initial redirect step insecure. |

---

## Interview Points

> **📌 Interview Point 1: What is a Padding Oracle Attack on TLS?**
> A cryptographic attack targeting CBC cipher modes. Attackers exploit padding response behaviors in server negotiations to decrypt data byte-by-byte. This risk is resolved by enforcing TLS 1.3, which restricts supported ciphers to secure AEAD-based alternatives.

---

## Exercises

### Exercise 1: Analyze HSTS configurations ⭐
**Task:** Identify the risk of configuring HSTS without the `includeSubDomains` directive.

<details>
<summary>✅ Solution (click to reveal)</summary>
Attackers can still spoof subdomains (e.g. `http://api.example.com`) over HTTP, intercepting requests or cookies.
</details>

---

## Next Chapter

Continue to [CORS (Cross-Origin Resource Sharing) Misconfigurations](./ch18-cors-misconfigurations.md) to explore browser resource sharing.
