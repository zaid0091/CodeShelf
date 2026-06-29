---
title: Database Sharding & Partitioning
description: Master database sharding (horizontal partitioning). Learn about sharding keys, range-based, hash-based, and consistent hashing strategies.
order: 14
tags: [architecture, database, sharding, partitioning, hashing, consistent-hashing]
---

# Chapter 4: Database Sharding & Partitioning

> **Scale database writes. Compare horizontal and vertical partitioning, evaluate sharding keys, and implement consistent hashing.**

---

## Sharding: The Write-Scaler

Replication scales database reads but does not help with writes: all writes must go to the single leader. To scale write throughput beyond a single server's limits, we partition the dataset across multiple independent database servers. This is **Sharding**.

---

## Partitioning Types

### 1. Vertical Partitioning (Column-Based)
Splitting a table by columns.
*   *Example:* Moving large, rarely accessed columns (like a binary blob `user_avatar`) to a separate table/database, keeping the main table (`user_id`, `username`) small and fast.

### 2. Horizontal Partitioning (Row-Based / Sharding)
Splitting a table by rows. Every shard contains the same table schema but holds a different subset of the rows.

```text
Table Users:
Shard 1: IDs 1 to 1,000,000
Shard 2: IDs 1,000,001 to 2,000,000
```

---

## Sharding Strategies

To distribute rows, you must choose a **Sharding Key** and a distribution algorithm:

### 1. Range-Based Sharding
Data is partitioned based on value ranges of the sharding key.
*   *Example:* Shard 1 gets users with names starting A-M; Shard 2 gets N-Z.
*   *Con:* Uneven distribution. If most users have names starting with J, Shard 1 becomes overloaded (Hot Spot).

### 2. Hash-Based Sharding
Apply a hash function to the sharding key and use modulo to find the target shard ID:
```text
Shard ID = Hash(ShardingKey) % NumberOfShards
```
*   *Pro:* Even distribution.
*   *Con:* If you add a new shard, the modulo divisor changes, requiring you to re-hash and move almost all existing data (expensive).

### 3. Consistent Hashing
A hashing technique where nodes and keys are mapped onto a circular ring. Adding or removing a database node requires moving only a fraction of the keys ($K/N$), making scaling dynamic.

---

## The Costs of Sharding

*   **No Cross-Shard Joins**: SQL queries cannot perform JOIN operations across different physical database shards. If needed, the application must query each shard and perform the join in memory (slow).
*   **Referential Integrity**: Databases cannot enforce foreign key constraints across shards.
*   **Operational Complexity**: Backups, schema updates, and monitoring become highly complex.

---

## Best Practices & Pitfalls

| Best Practice | Common Pitfall |
|---------------|----------------|
| Select a sharding key (like `user_id` or `tenant_id`) that matches your application's primary query access patterns. | Choosing a sharding key that creates hot spots (e.g., sharding by `created_at` date, which routes all new writes to the single current date shard). |

---

## Interview Points

> **📌 Interview Point 1: What is a Hotspot in Sharding?**
> A hotspot occurs when a single database shard receives a disproportionate amount of write or read requests. This happens due to poor sharding key selection (e.g., sharding by popular user accounts or sequential keys).

---

## Exercises

### Exercise 1: Evaluate sharding keys ⭐
**Task:** Identify the problem with sharding a message database by `timestamp`.

<details>
<summary>✅ Solution (click to reveal)</summary>
All new messages have the current timestamp, so all incoming writes will hit the exact same shard representing the current time window, overloading it.
</details>

---

## Next Chapter

Continue to [CAP Theorem & PACELC](./ch15-cap-theorem-pacelc.md) to explore distributed consistency.
