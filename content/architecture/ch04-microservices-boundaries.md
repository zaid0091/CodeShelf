---
title: Microservices & Service Boundaries
description: Learn about Microservices architecture, defining service boundaries using Domain-Driven Design (DDD), and handling service discovery.
order: 4
tags: [architecture, microservices, ddd, bounded-context, service-discovery]
---

# Chapter 4: Microservices & Service Boundaries

> **Break apart applications into independent services. Define logical boundaries using Domain-Driven Design and implement service discovery.**

---

## What is Microservices Architecture?

A Microservices architecture decomposes an application into a collection of small, autonomous, loosely coupled services. Each service represents a specific business capability, is deployed independently, and owns its private database.

---

## Defining Service Boundaries: DDD

A common mistake is making microservices too small (nano-services) or splitting them along technical lines (e.g., UI service, Backend service, DB service). Instead, align services with business domains using **Domain-Driven Design (DDD)** concepts:

### Bounded Context
A Bounded Context defines a boundary within which a specific domain model applies. For example:
*   **Users Context**: Deals with registration, logins, and profiles.
*   **Billing Context**: Deals with payments, subscriptions, and invoices.
*   **Shipping Context**: Deals with addresses, carriers, and tracking.

*Each bounded context runs as a separate microservice. If billing needs user data, it queries the Users Service API or listens to its events; it never queries the Users database directly.*

---

## Service Discovery

In microservice environments, service instances spin up and down dynamically, changing their IP addresses. Hardcoding IPs in configs is impossible.

**Service Discovery** uses a central registry (e.g., Consul, Netflix Eureka, or Kubernetes DNS) to track service locations:
1. **Registration**: When a service starts, it sends its IP/port to the registry.
2. **Lookup**: When Service A wants to call Service B, it queries the registry for Service B's active IPs.

---

## Advantages & Disadvantages

| Advantages | Disadvantages |
|------------|---------------|
| **Independent Scaling**: Scale only the resources that need it. | **Network Latency**: Direct memory calls are replaced by slow network requests. |
| **Fault Isolation**: If the Billing service crashes, users can still browse products. | **Distributed Transactions**: Ensuring data integrity across multiple databases is hard (No 2-Phase Commits). |
| **Tech Agility**: Write the search service in Go and the ML service in Python. | **Operational Overhead**: Requires complex CI/CD, Kubernetes, and monitoring. |

---

## Best Practices & Pitfalls

| Best Practice | Common Pitfall |
|---------------|----------------|
| **Database-per-Service**: Each microservice must own its database. No service can access another's database directly. | The **Distributed Monolith**: Microservices that share a single database, creating tight coupling and database lock issues. |

---

## Interview Points

> **📌 Interview Point 1: What is Conway's Law?**
> "Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations." If your team is split into Frontend, Backend, and DBA, you will build a 3-tier monolith. If you have cross-functional domain teams, you will build microservices.

---

## Exercises

### Exercise 1: Identify boundary errors ⭐
**Task:** Why is sharing a database table between two microservices a violation of microservices principles?

<details>
<summary>✅ Solution (click to reveal)</summary>
It breaks loose coupling. If Service A changes a database column type, Service B breaks immediately without any API contract negotiation, leading to deployment dependencies.
</details>

---

## Next Chapter

Continue to [SOA vs. Microservices vs. Serverless](./ch05-soa-serverless.md) to compare cloud compute paradigms.
