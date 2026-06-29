---
title: SOA vs. Microservices vs. Serverless
description: Compare Service-Oriented Architecture (SOA), Microservices, and Serverless (FaaS) computing paradigms, covering ESBs and cold starts.
order: 5
tags: [architecture, soa, microservices, serverless, faas, cold-start]
---

# Chapter 5: SOA vs. Microservices vs. Serverless

> **Evaluate different distributed computing architectures, contrast ESBs with dumb pipes, and understand serverless cold starts.**

---

## Evolution of Compute Paradigms

As software scaled, systems moved from large, centralized networks to highly distributed, event-driven functions.

---

## SOA vs. Microservices

**Service-Oriented Architecture (SOA)** and **Microservices** are both service-based architectures, but they differ in scale and integration design.

| Metric | SOA | Microservices |
|--------|-----|---------------|
| **Integration** | Centralized via an **Enterprise Service Bus (ESB)**. | Decentralized (APIs, Message Brokers). |
| **Philosoply** | "Smart pipes, dumb endpoints" (ESB handles routing, translation, logic). | "Smart endpoints, dumb pipes" (Services handle logic, pipes only transfer raw data). |
| **Database** | Services often share a large enterprise database. | Database-per-service (strictly isolated). |
| **Size** | Larger, enterprise-level services. | Small, single-responsibility services. |

---

## Serverless (Function as a Service - FaaS)

Serverless compute (e.g. AWS Lambda, Google Cloud Functions) allows developers to write code as individual functions that run in response to events (HTTP requests, database changes, file uploads). The cloud provider dynamically manages server provisioning, scaling, and resource allocation.

### Pros
*   **No Server Management**: No patching OS, provisioning nodes, or setting up load balancers.
*   **Scale to Zero**: Pay only for execution time. If zero requests arrive, costs are $0.
*   **Instant Scaling**: Functions spin up automatically to handle concurrent traffic spikes.

### Cons
*   **Cold Starts**: If a function has not been called recently, the provider must boot a new container environment, causing a latency spike (up to several seconds).
*   **Execution Time Limits**: Functions are forced to terminate after a set duration (e.g., max 15 minutes on AWS Lambda).
*   **Vendor Lock-in**: Code is tied to provider-specific SDKs and event triggers.

---

## Best Practices & Pitfalls

| Best Practice | Common Pitfall |
|---------------|----------------|
| Choose Serverless for event-driven, intermittent tasks (like thumbnail generation or cron exports). | Using Serverless for long-running, continuous compute tasks (like websocket connections or video streaming), which is more expensive than running dedicated virtual machines (EC2/ECS). |

---

## Interview Points

> **📌 Interview Point 1: What is a Cold Start in Serverless?**
> A cold start occurs when a serverless function is triggered after being idle. The cloud provider must locate server resources, boot a container, load the runtime environment (Python, Node, Java), and initialize the code. This adds latency to the initial request.

---

## Exercises

### Exercise 1: Evaluate cold start mitigations ⭐
**Task:** Why do Java and Go functions experience longer cold starts than Python and Node.js functions?

<details>
<summary>✅ Solution (click to reveal)</summary>
Java requires starting the JVM (Java Virtual Machine), and Go compiles to large binary configurations, requiring longer initialization times than interpreted, lightweight scripts like Python and Node.js.
</details>

---

## Next Chapter

Continue to [API Gateways & Reverse Proxies](./ch06-api-gateways.md) to explore request routing systems.
