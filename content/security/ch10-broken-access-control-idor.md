---
title: Broken Access Control & IDOR
description: Learn how Insecure Direct Object References (IDOR) and privilege escalation vulnerabilities occur, and how to write secure authorization checks.
order: 10
tags: [security, access-control, idor, authorization, privilege-escalation]
---

# Chapter 10: Broken Access Control & IDOR

> **Understand how attackers bypass access checks by tampering with resource identifiers, and implement robust object-level access controls.**

---

## What is Broken Access Control?

Access control enforces policies so that users cannot act outside their intended permissions. Broken Access Control is the #1 security risk in the OWASP Top 10. It leads to unauthorized information disclosure, data modification, or destruction.

---

## Insecure Direct Object References (IDOR)

IDOR occurs when an application exposes a direct reference to an internal database object (e.g., an ID in a URL or parameter) and fails to perform authorization checks to ensure the logged-in user owns that object.

### IDOR Attack Scenario
A user logs in and views their account profile page:
```text
URL: https://example.com/api/invoices/9924
```
The user changes the URL ID value:
```text
Tampered URL: https://example.com/api/invoices/9925
```
If the backend returns the invoice details of user 9925, an IDOR vulnerability exists.

---

## Privilege Escalation

*   **Horizontal Privilege Escalation**: A user accesses resources belonging to another user of the *same* role (e.g., User A viewing User B's billing records).
*   **Vertical Privilege Escalation**: A lower-privileged user executes actions reserved for higher-privileged roles (e.g., a standard customer accessing an administrator endpoint `/api/admin/delete-user`).

---

## Remediation

### 1. Object-Level Access Control (Ownership Checks)
Always check if the authenticated user has access rights to the specific record before returning or modifying database data.

```python
# VULNERABLE backend (Python / FastAPI)
@app.get("/invoices/{invoice_id}")
def get_invoice(invoice_id: int, db: Session = Depends(get_db)):
    # Missing verification check!
    return db.query(Invoice).filter(Invoice.id == invoice_id).first()

# SECURE backend
@app.get("/invoices/{invoice_id}")
def get_invoice_secure(invoice_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
        
    # Check ownership
    if invoice.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to view this invoice")
    return invoice
```

### 2. Use Non-Guessable Identifiers (UUIDs)
While not a replacement for authorization checks, using random string UUIDs (v4) instead of sequential integers (`1`, `2`, `3`) makes it impossible for attackers to guess or scan sequential records.

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Establish a centralized authorization handler rather than manually writing `if` checks in every single endpoint. | Assuming that using UUIDs in URLs removes the need for ownership validation checks. |

---

## Interview Points

> **📌 Interview Point 1: What is the difference between Role-Based Access Control (RBAC) and Attribute-Based Access Control (ABAC)?**
> **RBAC** grants permissions based on a user's role (e.g. `Admin`, `Editor`). **ABAC** evaluates context-aware properties (e.g. "Only allow user if they are the owner of the document and accessing it during business hours"). ABAC is often needed to solve IDORs.

---

## Exercises

### Exercise 1: Identify the privilege escalation type ⭐
**Task:** If a user accesses a URL `/edit-profile?id=other-user-id` and changes the email, what type of privilege escalation is this?

<details>
<summary>✅ Solution (click to reveal)</summary>
This is **Horizontal Privilege Escalation** because the attacker acts as another user with equivalent privilege levels.
</details>

---

## Next Chapter

Continue to [Session Management: Hijacking, Fixation, and Timeouts](./ch11-session-management.md) to explore session security controls.
