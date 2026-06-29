---
title: Vertical vs. Horizontal Scaling
description: Compare Scaling Up (Vertical) vs Scaling Out (Horizontal), resource limits, state management, and cost implications in system design.
order: 2
tags: [architecture, scaling, stateless, horizontal-scaling, systems]
---

# Chapter 2: Vertical vs. Horizontal Scaling

> **Understand how to scale applications as traffic grows, compare vertical vs. horizontal limits, and transition to stateless architectures.**

---

## What is Scaling?

Scaling is the process of expanding system capacity to handle increasing workloads (requests, data volume, concurrent users).

---

## Vertical Scaling (Scale Up)

Vertical scaling increases the capacity of an individual machine by adding more power (faster CPU, more RAM, SSD storage, or network cards).

### Pros
*   **Simple**: Code does not need modifications; database setups remain unified.
*   **Low Latency**: No network overhead between nodes.

### Cons
*   **Hard Ceiling**: Hardware limits exist. You cannot buy a server with infinite RAM or CPU.
*   **Single Point of Failure (SPOF)**: If the single server goes down, the entire system crashes.
*   **Exponential Cost**: High-end enterprise servers cost disproportionately more than multiple consumer-grade nodes.

---

## Horizontal Scaling (Scale Out)

Horizontal scaling adds more machines (nodes) to the system pool, routing incoming traffic across them via a Load Balancer.

### Pros
*   **No Ceiling**: You can add thousands of cheap nodes.
*   **High Availability**: If one node fails, others handle the traffic.
*   **Cost-Efficient**: Relies on commodity hardware.

### Cons
*   **High Complexity**: Requires load balancers, service discovery, and stateless code.
*   **Data Consistency**: Syncing databases and states across multiple nodes is difficult (CAP Theorem).

---

## Stateless vs. Stateful Architecture

To scale horizontally, application servers should be **Stateless**.

```text
Stateful: Client -> [App Server (stores Session in local memory)] (Client must stick to this server)
Stateless: Client -> Load Balancer -> [Any App Server] -> [Shared Database / Redis Session Store]
```

*   **Stateful**: The server stores client session data in its local memory. If that server fails or the load balancer routes the next request to another server, the user's session is lost.
*   **Stateless**: The server stores no session state. It queries a shared database or caching cluster (like Redis) for session data. Any application server can process any incoming request.

---

## Best Practices & Pitfalls

| Best Practice | Common Pitfall |
|---------------|----------------|
| Make application servers stateless from day one. Store states in central distributed caches (Redis) or client-side tokens (JWT). | Using local file systems to store user uploads (like avatars) on individual web servers. If a load balancer routes a user to another server, their file will be missing. Use object storage (like AWS S3) instead. |

---

## Interview Points

> **📌 Interview Point 1: When is Vertical Scaling preferred over Horizontal Scaling?**
> In early-stage startups or prototype phases where traffic is low, engineering resources are limited, and simplicity is critical. It is also common for databases to start with vertical scaling (primary-replica) before transitioning to complex sharding schemas.

---

## Exercises

### Exercise 1: Evaluate scaling models ⭐
**Task:** If a system experiences database bottleneck issues, why is horizontal database scaling harder than horizontal web server scaling?

<details>
<summary>✅ Solution (click to reveal)</summary>
Web servers are stateless, so adding more is simple. Databases contain state (data), which must be replicated, kept in sync, and partitioned across nodes without violating consistency rules.
</details>

---

## Next Chapter

Continue to [Monolithic Architecture: Pros, Cons, and Use Cases](./ch03-monolithic-architecture.md) to explore structural code layouts.
