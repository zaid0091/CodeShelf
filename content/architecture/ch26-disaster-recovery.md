---
title: Disaster Recovery (Active-Active, Active-Passive)
description: Master disaster recovery strategies. Compare Active-Active and Active-Passive configurations, and understand RTO and RPO metrics.
order: 26
tags: [architecture, disaster-recovery, rto, rpo, active-active, active-passive, cloud]
---

# Chapter 26: Disaster Recovery (Active-Active, Active-Passive)

> **Design systems that survive regional outages. Analyze RTO and RPO metrics, compare active-active and active-passive deployments, and manage failovers.**

---

## RTO and RPO: The DR Metrics

Before designing a Disaster Recovery (DR) plan, you must define the target metrics:

*   **RTO (Recovery Time Objective)**: The maximum acceptable target time to restore the application after an outage (e.g. "The site must be back online within 10 minutes").
*   **RPO (Recovery Point Objective)**: The maximum acceptable age of data that can be lost due to the outage (e.g. "We can tolerate losing at most 1 hour of transaction data").

---

## Disaster Recovery Deployment Models

To recover from region-wide outages (e.g. AWS data center fire), systems are deployed across multiple regions:

### 1. Active-Passive (Failover Model)
One primary region handles all traffic. A secondary region remains idle or in a standby state:
*   **Pilot Light**: The database is replicated to the passive region, but application servers are shut down. During failover, you boot the servers (low cost, high RTO).
*   **Warm Standby**: Application servers are running in the passive region but scaled down. During failover, you scale up servers and route traffic (medium cost, medium RTO).
*   *Pros:* Simple consistency; lower hosting costs.
*   *Cons:* Failover takes time; the standby region is wasted capacity during normal operations.

### 2. Active-Active (Multi-Region Model)
Both regions are active and handle user traffic concurrently:
*   **Replication**: Databases must be replicated bidirectionally (Multi-Leader or Dynamo-Style).
*   *Pros:* Near-zero RTO/RPO; highest availability; users are routed to their closest region automatically.
*   *Cons:* Extremely complex and expensive; data conflicts are difficult to resolve.

---

## GSLB Failover Routing
During a disaster, Global Server Load Balancers (GSLB) detect the primary region failure via health checks and automatically update DNS records to route traffic to the secondary region.

---

## Best Practices & Pitfalls

| Best Practice | Common Pitfall |
|---------------|----------------|
| Conduct regular, simulated disaster recovery drills (Chaos Engineering) to verify failover steps work. | Having an RPO of 0 (zero data loss) with asynchronous database replication, which is physically impossible over long distances. |

---

## Interview Points

> **📌 Interview Point 1: What is the difference between RTO and RPO?**
> **RTO** measures *downtime duration* (how long the system was down). **RPO** measures *data loss duration* (how much data was lost, represented by the age of the latest backup restored).

---

## Exercises

### Exercise 1: Evaluate DR costs ⭐
**Task:** A company requires an RTO of under 30 seconds and an RPO of under 5 seconds. Which DR model is required?

<details>
<summary>✅ Solution (click to reveal)</summary>
**Active-Active (Multi-Region)**. Both regions must be active and synchronized constantly in near-real-time to allow instant failover with minimal data loss.
</details>

---

## Next Chapter

Continue to [Distributed Consensus (Paxos, Raft, ZooKeeper)](./ch27-distributed-consensus.md) to explore distributed coordinator mechanics.
