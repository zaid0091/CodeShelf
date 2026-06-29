---
title: SQL Injection (SQLi) - Identification & Remediation
description: Understand how SQL Injection (SQLi) works, union-based and blind SQLi techniques, and how to defend using parameterized queries.
order: 3
tags: [security, sqli, injection, database, sql]
---

# Chapter 3: SQL Injection (SQLi) - Identification & Remediation

> **Learn how attackers inject malicious statements into SQL queries, evaluate classifications of SQLi, and remediate using prepared statements.**

---

## What is SQL Injection?

SQL Injection occurs when untrusted user input is concatenated directly into a database query string instead of being treated as a separate parameter. This allows the input to alter the structure of the SQL query.

---

## Classifications of SQLi

1. **In-Band SQLi (Classic)**: The attacker uses the same channel to launch the attack and gather results (e.g., Union-based SQLi where query outputs are joined to the results).
2. **Inferential (Blind) SQLi**: The database does not output data directly to the web page. The attacker must ask True/False questions:
    *   **Boolean-based**: The page loads differently depending on if the statement evaluates to true or false.
    *   **Time-based**: The attacker injects commands (like `SLEEP(5)`) to measure server latency.
3. **Out-of-Band SQLi**: The database triggers network requests (e.g., DNS or HTTP requests) to send data back to the attacker.

---

## Vulnerable vs Secure Implementation

### Vulnerable Code (Python / Flask)
```python
# Raw concatenation allows input 'admin' OR '1'='1' to bypass login
cursor.execute(f"SELECT * FROM users WHERE username = '{user_input}'")
```

### Remediation: Parameterized Queries (Prepared Statements)
Prepared statements compile the SQL query template *before* inserting parameter values. The database engine parses variables strictly as values, never as executable SQL commands.

```python
# The database treats input strictly as a literal value
cursor.execute("SELECT * FROM users WHERE username = %s", (user_input,))
```

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Always use parameterized queries or trusted ORMs. | Using ORM features that support raw strings (like Django's `.extra()` or SQLAlchemy's `text()`) with unsanitized parameters. |

---

## Interview Points

> **📌 Interview Point 1: Does escaping special characters completely prevent SQL Injection?**
> Escaping (like using `addslashes()`) is not 100% reliable and can be bypassed depending on database encoding states (e.g., multi-byte character injection like GBK). Parameterized queries are the only secure mitigation.

---

## Exercises

### Exercise 1: Spot the vulnerability ⭐
**Task:** Is this query vulnerable?
`cursor.execute("SELECT * FROM products WHERE category = " + category_id)`

<details>
<summary>✅ Solution (click to reveal)</summary>
Yes. String concatenation of `category_id` bypasses parameter binding, allowing SQL injection.
</details>

---

## Next Chapter

Continue to [NoSQL & ORM Injection Attacks](./ch04-nosql-orm-injection.md) to explore database security beyond SQL.
