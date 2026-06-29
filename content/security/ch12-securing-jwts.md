---
title: Securing JSON Web Tokens (JWT) in Development & Prod
description: Master the security aspects of JSON Web Tokens (JWT), including the none algorithm exploit, key selection, and token storage options.
order: 12
tags: [security, jwt, signature-verification, symmetric-asymmetric, tokens]
---

# Chapter 12: Securing JSON Web Tokens (JWT) in Development & Prod

> **Deconstruct JWT architecture, examine the classic none algorithm exploit, select signing keys, and analyze secure client-side storage options.**

---

## What is a JWT?

A JSON Web Token is a compact, URL-safe method for representing claims transferred between two parties. Unlike stateful sessions, JWTs are stateless—all user permissions are encoded inside the token itself, which is signed by the server.

```text
Header.Payload.Signature
```
*   **Header**: Declares token type and hashing algorithm (e.g. HS256).
*   **Payload**: Contains claim statements (user ID, expiration, roles).
*   **Signature**: Cryptographic checksum verifying token integrity.

---

## The "none" Algorithm Vulnerability

In early JWT library implementations, servers respected the `alg` header parameter. An attacker could alter the JWT payload (e.g., changing `"role": "user"` to `"role": "admin"`), modify the header to `"alg": "none"`, remove the signature segment, and submit the token. The server would accept it as valid without validating any signature.

### Remediation
Always explicitly declare the allowed algorithms when decoding tokens, rather than reading the `alg` parameter from the header dynamically:

```python
# VULNERABLE decoding (Python / PyJWT)
# Danger: trusts whatever algorithm is specified in the token header
data = jwt.decode(token, verify=True)

# SECURE decoding
# Enforces algorithm check
data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
```

---

## Signature Algorithms: HS256 vs. RS256

*   **HS256 (Symmetric)**: A single secret key is used to sign and verify tokens. Both the authorization server and receiving microservices must know the secret. If one server is compromised, the entire system is breached.
*   **RS256 (Asymmetric)**: Uses a Private/Public key pair. The authorization server signs with the private key; consuming microservices verify using the public key. Compromising a consuming service does not expose the signing key.

---

## Secure Token Storage: LocalStorage vs. Cookies

| Storage Option | Vulnerability Exposure | Mitigation |
|----------------|------------------------|------------|
| **`LocalStorage`** | Vulnerable to **XSS**. Any injected script can read all values in LocalStorage. | Strict input validation, CSP headers. |
| **`HttpOnly Cookie`** | Vulnerable to **CSRF**. Browser automatically attaches cookies to outbound requests. | SameSite attributes, Anti-CSRF tokens. |

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Use short lifetimes (e.g., 15 mins) for Access Tokens, and store long-lived Refresh Tokens in secure, database-tracked database tables. | Storing sensitive information (like user passwords or internal IP addresses) in the JWT payload, which is only Base64 encoded and readable by anyone. |

---

## Interview Points

> **📌 Interview Point 1: Can you decode a JWT without knowing the secret key?**
> Yes. The Header and Payload of a JWT are only Base64URL-encoded, not encrypted. Anyone can decode and read the JSON content. The secret key is only used to generate the Signature to verify that the claims have not been tampered with.

---

## Exercises

### Exercise 1: Spot the vulnerability ⭐
**Task:** Identify the risk of sending a JWT in the URL query parameters:
`https://example.com/dashboard?token=eyJhbG...`

<details>
<summary>✅ Solution (click to reveal)</summary>
Tokens in URL queries are logged in browser history, server access logs, and HTTP Referer headers when linking to external sites, exposing them to capture.
</details>

---

## Next Chapter

Continue to [OAuth 2.0 & OIDC Security Best Practices](./ch13-oauth2-oidc-security.md) to study delegated authentication protocols.
