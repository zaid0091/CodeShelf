---
title: "Cryptographic Failures: Hashing vs. Encryption"
description: Learn about the differences between one-way hashing and reversible encryption, symmetric vs asymmetric ciphers, and legacy cryptographic algorithms to avoid.
order: 14
tags: [security, cryptography, hashing, encryption, legacy-algorithms]
---

# Chapter 14: Cryptographic Failures: Hashing vs. Encryption

> **Distinguish between one-way math ciphers and reversible encryption, identify symmetric vs asymmetric keys, and retire broken legacy algorithms.**

---

## What is Cryptographic Failure?

Cryptographic Failures (formerly "Sensitive Data Exposure") occur when data at rest or in transit is inadequately secured, exposing private keys or sensitive credentials to compromises.

---

## Hashing vs. Encryption

| Property | Hashing | Encryption |
|----------|---------|------------|
| **Type** | One-way function (mathematically irreversible). | Two-way function (reversible). |
| **Purpose** | Verifies integrity (checking if data was modified). | Guarantees confidentiality (hiding data content). |
| **Inputs** | Arbitrary data size yields a fixed-size checksum hash. | Text payloads yield encrypted ciphertext blocks. |
| **Keys** | None (runs algorithm directly). | Requires key(s) (Symmetric or Asymmetric). |
| **Use Case** | Password storage, file integrity validation. | Storing database credit cards, securing HTTPS traffic. |

---

## Symmetric vs. Asymmetric Encryption

### Symmetric Encryption (Shared Secret)
Both sender and receiver share the same secret key.
*   **Standard**: **AES (Advanced Encryption Standard)** using 256-bit keys in GCM mode (Galois/Counter Mode), which provides both confidentiality and integrity authentication.

### Asymmetric Encryption (Key Pair)
Uses a Public Key (to encrypt) and a Private Key (to decrypt).
*   **Standard**: **RSA** (minimum 2048-bit keys, preferably 4096-bit) or **ECC (Elliptic Curve Cryptography)**.
*   *Use Case:* Secure key exchange over public channels.

---

## Broken Cryptographic Standards (Do Not Use)

Never use outdated algorithms that are vulnerable to collision attacks or brute forcing:

*   **MD5 / SHA-1**: Collision vulnerability. Attackers can forge files yielding identical hashes.
*   **DES / 3DES**: Small key sizes easily cracked by modern computing power.
*   **RC4**: Vulnerable cipher streams that leak key patterns.

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Use authenticated encryption ciphers (like AES-GCM) that verify both data secrecy and signature integrity. | Using obsolete algorithms (like ECB mode for AES ciphers, which leaks image/data outlines). |

---

## Interview Points

> **📌 Interview Point 1: Why is AES-CBC mode vulnerable to Padding Oracle Attacks?**
> In CBC (Cipher Block Chaining) mode, if the decryption engine returns detailed padding error descriptions, attackers can systematically alter ciphertext blocks and decrypt them byte-by-byte without knowing the key. Mitigation: Switch to authenticated encryption modes (like AES-GCM).

---

## Exercises

### Exercise 1: Classify the operation ⭐
**Task:** When storing credit cards in a database, should you hash them or encrypt them?

<details>
<summary>✅ Solution (click to reveal)</summary>
You must **encrypt** them. Hashing is irreversible, which would prevent you from recovering the credit card numbers to charge customers.
</details>

---

## Next Chapter

Continue to [Password Hashing (Bcrypt, Argon2, PBKDF2)](./ch15-password-hashing.md) to study secure password storage ciphers.
