---
title: Publish-Subscribe & Event-Driven Architecture
description: Learn about the Publish-Subscribe (Pub/Sub) pattern, routing strategies (fan-out, topics), and the benefits of event-driven architectures.
order: 20
tags: [architecture, pub-sub, event-driven, loose-coupling, fan-out, messaging]
---

# Chapter 20: Publish-Subscribe & Event-Driven Architecture

> **Decouple distributed microservices. Implement Publish-Subscribe topologies, manage fan-out event routing, and design event-driven networks.**

---

## The Publish-Subscribe (Pub/Sub) Pattern

In traditional architectures, Service A calls Service B directly via HTTP (Request-Response). This creates tight coupling: if Service B is slow or down, Service A fails too.

**Pub/Sub** decouples systems:
*   **Publishers**: Emit events (e.g. `OrderCreated`) to a central broker, without knowing who consumes them.
*   **Subscribers**: Register interest in specific event types and process them asynchronously when they arrive.

---

## Event Routing Strategies

Brokers route published events using specific exchange types:

### 1. Fan-out Exchange
Clones and routes the message to *all* bound queues.
*   *Use Case:* An `OrderPlaced` event needs to go to the Billing Service, Shipping Service, and Email Service simultaneously.

```text
Publisher -> [Fan-Out Exchange]
                 |
                 +-------> [Billing Queue]  -> Billing Service
                 +-------> [Shipping Queue] -> Shipping Service
                 +-------> [Email Queue]    -> Email Service
```

### 2. Topic/Direct Exchange
Routes messages based on matching routing keys (e.g. `log.error.billing` goes to the Alerts queue, but `log.info.billing` is ignored).

---

## Benefits of Event-Driven Systems

*   **Loose Coupling**: Services don't need to know the IPs or existence of other services. You can add a new `AnalyticsService` that consumes existing events without modifying the publishing service.
*   **Temporal Decoupling**: If the Email Service is down, events pile up in the queue. When the service recovers, it processes the backlogged events without losing data.
*   **Better Performance**: The primary service (e.g., checkout) returns a response to the user immediately, offloading secondary tasks (sending confirmation emails) to background subscribers.

---

## Challenges of Event-Driven Systems

*   **Distributed Tracing**: Hard to track requests as they flow asynchronously across multiple queues and services.
*   **Eventual Consistency**: Data across services is not updated instantly, requiring users to accept delayed state changes.

---

## Best Practices & Pitfalls

| Best Practice | Common Pitfall |
|---------------|----------------|
| Make event schemas backwards-compatible using serialization formats like Avro or Protobuf with a Schema Registry. | Publishing internal database row states directly as events. Publish clean, high-level business events (`OrderCompleted`) instead. |

---

## Interview Points

> **📌 Interview Point 1: What is Eventual Consistency in Pub/Sub?**
> Since services update their databases asynchronously in response to events, different microservices will have temporarily inconsistent states (e.g., the order service says "paid", but the shipping service hasn't processed the payment event yet). The system is guaranteed to reach a consistent state *eventually* once all events are processed.

---

## Exercises

### Exercise 1: Evaluate event architectures ⭐
**Task:** If a user cancels an order, why should the order service publish an `OrderCancelled` event instead of directly making HTTP calls to the Billing, Shipping, and Inventory services?

<details>
<summary>✅ Solution (click to reveal)</summary>
Using HTTP calls couples the order service to the availability of three other services. If the Inventory service is down, the cancellation request fails. An event allows the order service to process the cancellation instantly and offload updates.
</details>

---

## Next Chapter

Continue to [Event Sourcing & CQRS](./ch21-event-sourcing-cqrs.md) to explore state replay architectures.
