---
title: "Database Scaling: Replication"
description: Master database replication patterns. Compare Leader-Follower, Multi-Leader, and Leaderless replication, and mitigate replication lag.
order: 13
tags: [architecture, database, replication, leader-follower, consistency, replication-lag]
---

# Chapter 13: Database Scaling: Replication

> **Scale database reads. Compare Leader-Follower, Multi-Leader, and Leaderless replication models, and mitigate replication lag.**

---

## Replication: The Read-Scaler

To scale database capacity and prevent data loss during hardware failures, we copy the database across multiple servers (nodes). This is **Replication**.

---

## Replication Models

### 1. Leader-Follower (Single Leader / Master-Slave)
One node is designated as the **Leader**. All write operations (insert, update, delete) must go to the leader. The leader applies changes and streams them to **Follower** nodes. Read operations can go to any node:

```text
Client Writes -> [Leader DB]
                    | (Sync or Async Replication)
                    +------------+
                    |            |
                    v            v
            [Follower DB]   [Follower DB] <- Client Reads
```
*   *Pros:* Simple consistency model (only one source of truth for writes).
*   *Cons:* Followers can experience replication lag; writes cannot scale beyond the capacity of the single leader node.

### 2. Multi-Leader (Active-Active)
Multiple nodes act as leaders, accepting write operations concurrently.
*   *Pros:* Writes are scaled; system survives data center outages.
*   *Cons:* Conflict resolution is extremely complex (e.g. what happens if two users modify the same record in different data centers simultaneously?).

### 3. Leaderless (Dynamo-Style)
No single node owns writes. The client writes to multiple replica nodes concurrently.
*   *Key Concept:* **Quorums**. A write or read is successful only if a majority of nodes acknowledge it. Used by Apache Cassandra and Amazon Dynamo.

---

## Replication Lag & Consistency Issues

Most replication is **Asynchronous** (to prevent writes from waiting on network latency). This introduces **Replication Lag**: a delay between a write on the leader and its appearance on a follower.

### Key Anomalies & Solutions
*   **Read-Your-Own-Writes Consistency**: If a user updates their profile and immediately refreshes the page, the read might hit a lagging follower showing old data.
    *   *Solution:* Always route the user's reads to the *leader* for a set duration (e.g., 5 seconds) after they perform a write operation.
*   **Monotonic Reads**: Prevents a user from "moving backward in time" (e.g., refreshing and seeing updates disappear because the load balancer routed them to an even slower follower).
    *   *Solution:* Bind users to specific follower nodes based on their User ID hash.

---

## Best Practices & Pitfalls

| Best Practice | Common Pitfall |
|---------------|----------------|
| Set up automated failover (e.g., using Sentinel in Redis or Orchestrator in MySQL) to quickly promote a follower to leader during outages. | Using Multi-Leader replication for standard CRUD apps, introducing write conflicts that are difficult to debug. |

---

## Interview Points

> **📌 Interview Point 1: What is Split-Brain in Database Failover?**
> Split-brain occurs when the primary leader node loses network connectivity but remains running. The system detects a timeout, assumes the leader is dead, and promotes a follower to be the new leader. When the network heals, the system has *two* active leaders accepting writes, corrupting the database.

---

## Exercises

### Exercise 1: Evaluate replication modes ⭐
**Task:** In a Leaderless system with 3 replicas, if a write requires 2 acknowledgements and a read requires 2 acknowledgements, is the system guaranteed to read the latest write?

<details>
<summary>✅ Solution (click to reveal)</summary>
Yes. This is a **Quorum** ($R + W > N$). Since $2 + 2 > 3$, the read set and write set must overlap by at least one node, guaranteeing that the client reads from the updated replica.
</details>

---

## Next Chapter

Continue to [Database Sharding & Partitioning](./ch14-database-sharding.md) to scale database writes.
