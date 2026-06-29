---
title: The Security Mindset & Threat Modeling
description: Understand the fundamental pillars of information security (CIA Triad), threat modeling using STRIDE, and core design principles like Defense in Depth.
order: 1
tags: [security, threat-modeling, stride, cia-triad, basics]
---

# Chapter 1: The Security Mindset & Threat Modeling

> **Learn the core design principles of web application security: the CIA Triad, the STRIDE threat modeling framework, and Defense in Depth.**

---

## The CIA Triad

The cornerstone of security architecture consists of three pillars:
*   **Confidentiality**: Ensuring sensitive data is only accessible to authorized users (achieved via Encryption, Access Control, MFA).
*   **Integrity**: Guaranteeing data is not tampered with, modified, or deleted in transit or storage (achieved via Hashes, Digital Signatures, database constraints).
*   **Availability**: Ensuring systems and data are consistently accessible to authorized users when needed (achieved via Redundancy, Backups, DoS protection).

---

## Threat Modeling: STRIDE

Threat modeling is the process of identifying potential security threats in an application architecture before writing code. Microsoft's **STRIDE** model classifies threats into six categories:

| Threat | Description | Security Property Violated | Mitigation Example |
|--------|-------------|----------------------------|--------------------|
| **S**poofing | Pretending to be someone else | Authenticity | Strong passwords, MFA, signature checks |
| **T**ampering | Modifying data in transit or database | Integrity | Parameterized queries, HTTPS, hashes |
| **R**epudiation | Claiming an action was not performed | Non-Repudiability | Secure logging, audit trails |
| **I**nformation Disclosure | Exposing private data | Confidentiality | Encryption, access control lists (ACL) |
| **D**enial of Service | Exhausting resources to disable service | Availability | Rate limiting, CDNs, load balancing |
| **E**levation of Privilege | Gaining unauthorized admin permissions | Authorization | Role checks, input validation |

---

## Defense in Depth

> **Core Concept:** Do not rely on a single line of defense. If one security control fails, other layers must protect the application.

For example, when preventing SQL Injection:
1. Validate inputs on the client (for UX).
2. Validate inputs on the backend (first line of security).
3. Use parameterized database queries (second line of security).
4. Run the database using a non-root service account with read-only access to needed tables (principle of least privilege).

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Apply the **Principle of Least Privilege** (restrict access by default). | Granting admin credentials to standard database connection scripts. |
| Assume all client inputs are compromised or malicious. | Trusting front-end validation limits without duplicating checks on the backend. |

---

## Interview Points

> **📌 Interview Point 1: What is the difference between Authentication and Authorization?**
> **Authentication** is verifying *who* a user is (e.g. usernames, passwords, tokens). **Authorization** is verifying *what* permissions the authenticated user has (e.g. roles, permissions, ACLs).

---

## Exercises

### Exercise 1: Apply STRIDE to a Login Form ⭐
**Task:** Identify which STRIDE threat occurs if login passwords are sent over HTTP in clear text.

<details>
<summary>✅ Solution (click to reveal)</summary>
This is an **Information Disclosure** threat (violating Confidentiality) because anyone eavesdropping on the network (MITM attack) can capture the plain text passwords. Mitigation: Enforce HTTPS.
</details>

---

## Next Chapter

Continue to [Introduction to the OWASP Top 10](./ch02-owasp-top-10-overview.md) to explore the industry standard list of critical vulnerabilities.
