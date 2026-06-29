---
title: Relational (SQL) vs. Non-Relational (NoSQL)
description: Compare Relational (SQL) databases against Non-Relational (NoSQL) systems, covering schema constraints, joins, scaling, and use cases.
order: 17
tags: [architecture, database, sql, nosql, relational, schemas]
---

# Chapter 17: Relational (SQL) vs. Non-Relational (NoSQL)

> **Compare database engines, analyze schema flexibility, compare joins and relations, and evaluate scaling architectures.**

---

## The Database Selection Dilemma

One of the most critical decisions in system design is choosing between a Relational (SQL) database and a Non-Relational (NoSQL) database.

---

## Core Differences

| Feature | Relational (SQL) | Non-Relational (NoSQL) |
|---------|------------------|------------------------|
| **Data Model** | Structured tables (rows and columns). | Flexible documents, key-values, columns, or graphs. |
| **Schema** | Rigid, predefined schema. Modifying tables requires migration scripts. | Dynamic schema. Documents can store arbitrary fields. |
| **Relationships** | Handles complex JOINs natively using Foreign Keys. | Denormalized data. Relationships are nested or handled in application code. |
| **Scaling** | Typically scales **Vertically** (replicates for reads, hard to shard). | Scales **Horizontally** natively (shards data across clusters easily). |
| **Transaction Model** | Strict **ACID** compliance. | Typically **BASE** (eventual consistency), though some support ACID. |

---

## SQL: When to Use
Relational databases (e.g. PostgreSQL, MySQL) are best when:
*   Your data has a clear, predictable structure.
*   Data relationships are highly connected and require complex joins.
*   You require strict transactional integrity (e.g., billing, ERP).

---

## NoSQL: When to Use
Non-Relational databases (e.g. MongoDB, Cassandra, DynamoDB) are best when:
*   You store unstructured, semi-structured, or rapidly changing data (e.g. user events, sensor feeds).
*   You handle extreme write/read volumes that require horizontal scaling across multiple servers.
*   You prefer a denormalized database structure (nested JSON) that maps directly to object-oriented code.

---

## Best Practices & Pitfalls

| Best Practice | Common Pitfall |
|---------------|----------------|
| Choose PostgreSQL as a solid default database for general projects unless you have specific scaling or data-model needs. | Designing a NoSQL document database like a SQL database by creating multiple collections and running slow, manual joins in your backend code. |

---

## Interview Points

> **📌 Interview Point 1: What does Denormalization mean in NoSQL?**
> Denormalization is the practice of duplicating data across records to optimize read speeds. Instead of storing a `user_id` and running a JOIN to fetch their name, you store the user's name directly inside the document. This makes reads fast but makes updates complex because you must write to multiple records to keep data in sync.

---

## Exercises

### Exercise 1: Choose the Database ⭐
**Task:** Select the database model for a medical prescription tracker requiring strict audit compliance and foreign-key links between doctors, patients, and medicines.

<details>
<summary>✅ Solution (click to reveal)</summary>
**Relational (SQL) Database** (like PostgreSQL). The relationships are highly structured, and medical regulations require strict transactional integrity (ACID) to ensure prescriptions are never orphaned or modified incorrectly.
</details>

---

## Next Chapter

Continue to [Special Purpose Storage (Key-Value, Document, Graph, Vector)](./ch18-special-purpose-storage.md) to explore specialized databases.
