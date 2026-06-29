---
title: Password Hashing (Bcrypt, Argon2, PBKDF2)
description: Master the implementation of secure password hashing using Bcrypt, Argon2, and PBKDF2. Learn about salting, peppering, and work factors.
order: 15
tags: [security, hashing, password, bcrypt, argon2, salts]
---

# Chapter 15: Password Hashing (Bcrypt, Argon2, PBKDF2)

> **Understand why standard quick ciphers fail for passwords, implement secure salting and peppering, and evaluate Bcrypt vs. Argon2.**

---

## Why Standard Hashes Fail

Fast hashing algorithms like MD5, SHA-1, and SHA-256 are designed to calculate checksums for large files in milliseconds. This speed is a vulnerability for passwords: an attacker who compromises a database can guess billions of passwords per second using GPUs or ASIC hardware.

---

## Salts and Peppers

### 1. Salting (Unique per User)
A random string added to the password before hashing.
*   **Purpose**: Prevents lookup/rainbow table attacks. If two users choose the same password, they still get unique database hashes.

### 2. Peppering (Shared Secret)
A secret key stored outside the database (e.g., in environment variables) added to all passwords.
*   **Purpose**: Protects hashes even if the database is leaked.

```text
Hash(Password + Salt + Pepper) -> DB Hash
```

---

## Key Stretching & Modern Hashing Standards

Key stretching algorithms are CPU and memory-intensive, slowing down brute force attacks.

### 1. Bcrypt (Classic Standard)
Adaptive hashing algorithm based on Blowfish.
*   **Work Factor**: A parameter that controls CPU cost. Incrementing the work factor doubles hashing runtime.

### 2. PBKDF2 (NIST Approved)
Applies a pseudorandom function (like HMAC-SHA256) repeatedly (e.g., 600,000+ iterations).
*   *Limitation:* Easily parallelized on GPU hardware, making it less secure than memory-hard ciphers.

### 3. Argon2 (The Modern Champion - OWASP Recommended)
Winner of the Password Hashing Competition (PHC).
*   **Argon2id**: Memory-hard and CPU-hard. Limits GPU attack efficiency because it requires large memory blocks. It also protects against side-channel timing attacks.

---

## Code Example: Argon2 in Python

```python
from argon2 import PasswordHasher

ph = PasswordHasher()

# Hash a password
hashed = ph.hash("my-secret-password")

# Verify password
try:
    ph.verify(hashed, "my-secret-password")
    print("Password matches!")
except Exception:
    print("Invalid password!")
```

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Configure Bcrypt work factors to take around 100–300 milliseconds per hash to balance UX and security. | Implementing custom hashing functions (e.g. `md5(sha1(pass))`). |

---

## Interview Points

> **📌 Interview Point 1: What is a Rainbow Table?**
> A precomputed database mapping common passwords to their corresponding hash values. Salting completely mitigates rainbow table attacks because the salt changes the output hash even for identical input strings.

---

## Exercises

### Exercise 1: Choose the algorithm ⭐
**Task:** Why is SHA-256 not recommended for hashing user passwords?

<details>
<summary>✅ Solution (click to reveal)</summary>
SHA-256 is too fast. Attackers can brute force it at scale on modern GPUs (billions of hashes per second). Password ciphers must be slow.
</details>

---

## Next Chapter

Continue to [Managing Secrets & API Keys](./ch16-managing-secrets.md) to study credential storage security.
