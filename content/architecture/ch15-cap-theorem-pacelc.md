---
title: CAP Theorem & PACELC
description: Master the CAP Theorem (Consistency, Availability, Partition Tolerance) and the PACELC theorem. Learn how databases navigate latency vs consistency trade-offs.
order: 15
tags: [architecture, cap-theorem, pacelc, distributed-systems, consistency, availability]
---

# Chapter 15: CAP Theorem & PACELC

> **Deconstruct distributed trade-offs. Compare CP and AP architectures under network partitions, and analyze latency vs. consistency constraints using PACELC.**

---

## The CAP Theorem

Formulated by Eric Brewer, the CAP Theorem states that a distributed data store can simultaneously provide at most two of the following three guarantees:

*   **Consistency (C)**: Every read receives the most recent write or an error. (All nodes return the identical data simultaneously).
*   **Availability (A)**: Every non-failing node returns a non-error response (without guarantee that it contains the latest write).
*   **Partition Tolerance (P)**: The system continues to operate despite an arbitrary number of messages being dropped or delayed by the network between nodes.

---

## The CAP Choice: CP vs. AP

In a distributed system, network partitions (P) are inevitable. Therefore, you must choose between:

### 1. CP (Consistency + Partition Tolerance)
If a network partition occurs, the system blocks writes or reads to nodes that cannot communicate with the leader, preserving data consistency at the expense of availability.
*   *Use Case:* Banking ledgers, booking systems.

### 2. AP (Availability + Partition Tolerance)
If a network partition occurs, all nodes accept write and read requests. Nodes that are isolated return stale data. The system remains available at the expense of consistency.
*   *Use Case:* Social media comments, like counters.

*Note: **CA** is impossible in distributed systems because network partitions are physical realities you cannot prevent.*

---

## PACELC Theorem (The Extension)

CAP only describes system behavior when a network Partition (P) occurs. The **PACELC** theorem extends this by describing normal operation (Else):

*   **If there is a Partition (P)**: How does the system choose between **Availability (A)** and **Consistency (C)**?
*   **Else (E)**: When the system is running normally (no partition), how does it choose between **Latency (L)** and **Consistency (C)**?

```text
               +-----------------------------+
               |      PACELC Theorem         |
               +-----------------------------+
                /                           \
       If Partition (P)                 Else (E)
        /           \                  /        \
 Availability Consistency          Latency  Consistency
    (A)         (C)                  (L)        (C)
```

### Examples
*   **MongoDB (PC/EC)**: Under partitions, it chooses Consistency. In normal operation, it also chooses Consistency (wait for replica acknowledgments, increasing latency).
*   **Cassandra (PA/EL)**: Under partitions, it remains Available. In normal operation, it optimizes for low Latency (returns local copy without waiting for global replication).

---

## Best Practices & Pitfalls

| Best Practice | Common Pitfall |
|---------------|----------------|
| Select database consistency settings based on specific transaction types (e.g. choose AP for product views, but CP for checkout operations). | Assuming a database advertised as "highly available" is automatically consistency-safe during network cuts. |

---

## Interview Points

> **📌 Interview Point 1: What does "Consistency" mean in the CAP Theorem vs. ACID database transactions?**
> In the **CAP Theorem**, Consistency means *Linearizability* (all replica nodes return the identical latest write value). In **ACID**, Consistency means *Schema Integrity* (the transaction transitions the database from one valid state to another, respecting all constraints like foreign keys).

---

## Exercises

### Exercise 1: Map the database to PACELC ⭐
**Task:** If a database is configured to return reads instantly using local cache and replicate asynchronously in background threads, how is it classified under the PACELC theorem?

<details>
<summary>✅ Solution (click to reveal)</summary>
**PA/EL**. Under partitions, it remains Available (PA). During normal operation, it chooses low Latency over Consistency (EL).
</details>

---

## Next Chapter

Continue to [ACID vs. BASE Properties](./ch16-acid-base-transactions.md) to explore transaction models.
