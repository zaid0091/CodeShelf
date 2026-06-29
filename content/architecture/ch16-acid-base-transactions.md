---
title: ACID vs. BASE Properties
description: Compare ACID relational transaction guarantees against BASE eventual consistency models. Master isolation levels and read phenomena.
order: 16
tags: [architecture, database, acid, base, transactions, isolation-levels]
---

# Chapter 16: ACID vs. BASE Properties

> **Deconstruct transaction constraints. Compare relational ACID properties with distributed BASE eventual consistency, and analyze database isolation levels.**

---

## Transaction Models

Data consistency models fall into two main categories: strict transactional guarantees (relational databases) or relaxed, eventual consistency models (distributed NoSQL databases).

---

## ACID Properties (Relational DBs)

ACID guarantees that all database transactions are processed reliably:

*   **Atomicity**: "All or nothing". If one query in a transaction fails, the entire transaction rolls back.
*   **Consistency**: A transaction can only transition the database from one valid state to another, preserving all schemas and constraints.
*   **Isolation**: Concurrent transactions execute without interfering with one another.
*   **Durability**: Once a transaction is committed, it remains saved even during power outages or system crashes.

### Database Isolation Levels
To balance performance and consistency, databases allow developers to select isolation levels:

| Isolation Level | Dirty Reads | Non-Repeatable Reads | Phantom Reads |
|-----------------|-------------|----------------------|---------------|
| **Read Uncommitted** | Yes | Yes | Yes |
| **Read Committed** | No | Yes | Yes |
| **Repeatable Read** | No | No | Yes |
| **Serializable** (Strict) | No | No | No |

*   **Dirty Read**: Reading uncommitted updates from another transaction.
*   **Non-Repeatable Read**: A transaction reads the same row twice and gets different values because another transaction committed an update in between.
*   **Phantom Read**: A transaction executes a query returning a set of rows, and upon re-running, finds new rows inserted by another transaction.

---

## BASE Properties (NoSQL DBs)

BASE is the opposite of ACID, designed for highly available horizontal systems:

*   **Basically Available**: The system remains operational during failures, but some nodes might return stale data or errors.
*   **Soft State**: The state of the system can drift or change over time without user interaction because of replica sync lag.
*   **Eventual Consistency**: The system guarantees that if no new writes occur, all replicas will eventually sync and contain identical data.

---

## Best Practices & Pitfalls

| Best Practice | Common Pitfall |
|---------------|----------------|
| Use ACID databases (PostgreSQL/MySQL) for transactions requiring zero toleration for inconsistencies (like payments). | Using Serializable isolation levels everywhere, which causes severe transaction locks and performance bottlenecks. |

---

## Interview Points

> **📌 Interview Point 1: What is a Write-Skew anomaly?**
> A concurrency anomaly that can occur under Repeatable Read isolation. Two concurrent transactions read the same data, make decisions based on it, and write updates that violate a business rule (e.g., preventing checking accounts from going negative, but both withdraw concurrently, resulting in a negative balance). It requires Serializable isolation to prevent.

---

## Exercises

### Exercise 1: Identify the anomaly ⭐
**Task:** Transaction A updates a user's address but has not committed. Transaction B reads the address and displays it. What anomaly occurred?

<details>
<summary>✅ Solution (click to reveal)</summary>
**Dirty Read**. Transaction B read uncommitted data. If Transaction A later rolls back, Transaction B's read is invalid.
</details>

---

## Next Chapter

Continue to [Relational (SQL) vs. Non-Relational (NoSQL)](./ch17-sql-nosql-databases.md) to compare database paradigms.
