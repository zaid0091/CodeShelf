---
title: NoSQL & ORM Injection Attacks
description: Learn how NoSQL databases (like MongoDB) and object-relational mapping (ORM) systems can be vulnerable to query injection, and how to write secure queries.
order: 4
tags: [security, nosql, orm, mongodb, database, injection]
---

# Chapter 4: NoSQL & ORM Injection Attacks

> **Understand how attackers exploit NoSQL operator parsing and bypass ORM abstractions to execute malicious queries.**

---

## NoSQL Injection (MongoDB example)

NoSQL databases do not use SQL, but they are still vulnerable to injection. In MongoDB, queries are represented as JSON objects. If user inputs are parsed directly as JSON, attackers can inject query operators (like `$gt`, `$ne`, `$where`).

### Vulnerable Code (Express / Node.js)
```javascript
// Input: { "username": {"$gt": ""}, "password": {"$gt": ""} }
// Result: Matches all records where username and password are not empty strings (bypasses login!)
db.collection('users').find({
    username: req.body.username,
    password: req.body.password
});
```

### Remediation
1. **Type Constraint**: Enforce input parameters to be strings, not objects.
2. **Schema Sanitization**: Use libraries like `mongo-sanitize` to strip keys beginning with `$`.
3. **Mongoose Schemas**: Define strict schemas which auto-cast properties.

```javascript
// Mongoose auto-casts input to defined Schema types
const UserSchema = new mongoose.Schema({
    username: { type: String, required: true },
    password: { type: String, required: true }
});
```

---

## ORM Injection

Developers assume using an ORM (like Hibernate, SQLAlchemy, Django ORM) automatically prevents SQL injection. However:
1. **Raw SQL methods**: Methods like `.raw()`, `.extra()`, or `text()` bypass safe ORM parameterization.
2. **Order By injection**: Unsanitized column names passed to `order_by()` can trigger injection.

```python
# VULNERABLE Django ORM usage:
column = request.GET.get('sort')
# Input: "username; DROP TABLE users;--"
User.objects.all().extra(select={'custom_sort': f"ORDER BY {column}"})
```

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Validate sorting parameters against a strict whitelist (allowlist) of database column names. | Assuming database-layer queries written using ORM helpers are always safe from injection. |

---

## Interview Points

> **📌 Interview Point 1: Can NoSQL Injection lead to Remote Code Execution (RCE)?**
> Yes, in MongoDB, the `$where` operator accepts JavaScript string statements. If an attacker can inject custom code into a `$where` query, they can execute JavaScript on the database server.

---

## Exercises

### Exercise 1: Remediate the MongoDB query ⭐
**Task:** Secure the Express endpoint parameter from NoSQL injection.
`const username = req.body.username;`

<details>
<summary>✅ Solution (click to reveal)</summary>
Ensure it is a string:
```javascript
const username = String(req.body.username);
// or use mongo-sanitize
const sanitize = require('mongo-sanitize');
const cleanUsername = sanitize(req.body.username);
```
</details>

---

## Next Chapter

Continue to [Command Injection & Path Traversal](./ch05-command-injection-traversal.md) to explore system-level injection attacks.
