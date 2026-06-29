---
title: Distributed Consensus (Paxos, Raft, ZooKeeper)
description: Master distributed consensus mechanics. Understand Paxos, Raft states, ZooKeeper/etcd roles, and quorum requirements.
order: 27
tags: [architecture, consensus, raft, paxos, zookeeper, etcd, quorum]
---

# Chapter 27: Distributed Consensus (Paxos, Raft, ZooKeeper)

> **Coordinate distributed nodes. Master Paxos and Raft consensus protocols, configure etcd/ZooKeeper registries, and prevent split-brain states.**

---

## The Consensus Problem

In a distributed system, nodes must agree on specific states (e.g. "Which node is the leader?", "Has Transaction 55 committed?"). Achieving this is difficult because network packets can be lost, delayed, or out of order, and nodes can crash.

**Distributed Consensus** is the mathematical protocol that guarantees nodes reach a single, unified agreement despite these failures.

---

## Consensus Protocols

### 1. Paxos
The classic consensus protocol. It is mathematically robust but notoriously complex to understand and implement.

### 2. Raft (The Readable Protocol)
Designed as an alternative to Paxos, Raft decomposes consensus into three sub-problems:
1.  **Leader Election**: If the current leader fails, a new leader is elected.
2.  **Log Replication**: The leader receives commands from clients, appends them to its log, and forces other nodes to replicate them.
3.  **Safety**: Ensures that if a node has applied a log entry to its state machine, no other node can apply a different value for that entry.

#### Raft Node States
*   **Leader**: Manages all client writes and coordinates replication.
*   **Follower**: Passive nodes that respond to requests from leaders and candidates.
*   **Candidate**: A follower that times out waiting for leader heartbeats, starts an election, and requests votes.

---

## Quorums & Split-Brain Mitigation

Consensus systems require a **Quorum** (majority) to make decisions (elect leaders, commit logs):
```text
Quorum Size = (N / 2) + 1  (where N is the total number of nodes)
```
If a 5-node cluster partitions into a group of 3 and a group of 2:
*   The group of 3 can achieve quorum ($3 > 5/2+1$) and elect a leader.
*   The group of 2 cannot achieve quorum ($2 < 3$) and remains read-only.
*   *Why it works:* This prevents **Split-Brain** (having two active leaders writing conflicting data).

---

## Coordination Engines (ZooKeeper, etcd, Consul)

Distributed systems offload consensus to specialized, highly available key-value coordination engines:
*   **ZooKeeper**: Used by Kafka (previously) and Hadoop.
*   **etcd**: Uses the Raft protocol. The configuration backbone of Kubernetes.
*   **Consul**: Used for service discovery and configuration.

---

## Best Practices & Pitfalls

| Best Practice | Common Pitfall |
|---------------|----------------|
| Deploy consensus clusters with an **odd number of nodes** (3, 5, or 7) to optimize quorum efficiency. | Deploying 4 nodes, which has the same fault tolerance (survives 1 failure) as a 3-node cluster but adds network coordination overhead. |

---

## Interview Points

> **📌 Interview Point 1: Why does a 4-node cluster have the same fault tolerance as a 3-node cluster?**
> A 3-node cluster needs 2 nodes for quorum, tolerating 1 failure ($3 - 2 = 1$). A 4-node cluster needs 3 nodes for quorum, also tolerating only 1 failure ($4 - 3 = 1$). Adding the 4th node adds network overhead without increasing reliability.

---

## Exercises

### Exercise 1: Calculate Quorum ⭐
**Task:** How many node failures can a 5-node cluster tolerate while remaining operational?

<details>
<summary>✅ Solution (click to reveal)</summary>
**2 failures**. A 5-node cluster requires 3 nodes for quorum ($5/2 + 1 = 3$). If 2 nodes crash, 3 remain, which is sufficient to operate.
</details>

---

## Next Chapter

Continue to [Distributed Observability: Tracing, Logs, Metrics](./ch28-distributed-observability.md) to explore monitoring patterns.
