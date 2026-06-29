---
title: Design & Architecture Overview
description: Course roadmap and study guide for System Design and High-Level Architecture Patterns.
order: 0
tags: [architecture, system-design, scaling, overview]
---

# Design & Architecture Course Overview

Welcome to the **Design & Architecture** course. This developer-friendly guide covers core scaling concepts, architectural structures, distributed data management, message brokers, caching mechanisms, fault tolerance, and observability patterns.

## Course Structure

The course is split into 30 chapters across 7 distinct parts:

### Part 1: Course Foundations
*   [Ch 0: Course Overview](./ch00-course-overview.md)
*   [Ch 1: Client-Server & Communication Protocols](./ch01-client-server-protocols.md)
*   [Ch 2: Vertical vs. Horizontal Scaling](./ch02-vertical-horizontal-scaling.md)

### Part 2: Monoliths, Microservices & APIs
*   [Ch 3: Monolithic Architecture: Pros, Cons, and Use Cases](./ch03-monolithic-architecture.md)
*   [Ch 4: Microservices & Service Boundaries](./ch04-microservices-boundaries.md)
*   [Ch 5: SOA vs. Microservices vs. Serverless](./ch05-soa-serverless.md)
*   [Ch 6: API Gateways & Reverse Proxies](./ch06-api-gateways.md)
*   [Ch 7: REST vs. gRPC vs. GraphQL](./ch07-rest-grpc-graphql.md)

### Part 3: High Availability & Performance
*   [Ch 8: Load Balancers: L4 vs. L7](./ch08-load-balancers.md)
*   [Ch 9: DNS Routing & Global Load Balancing](./ch09-dns-routing-gslb.md)
*   [Ch 10: Caching Strategies & Eviction](./ch10-caching-strategies.md)
*   [Ch 11: CDN (Content Delivery Networks)](./ch11-cdn-edge-caching.md)
*   [Ch 12: Edge Computing & Serverless Edge](./ch12-edge-computing.md)

### Part 4: Data Layer Scaling & Consistency
*   [Ch 13: Database Scaling: Replication](./ch13-database-scaling.md)
*   [Ch 14: Database Sharding & Partitioning](./ch14-database-sharding.md)
*   [Ch 15: CAP Theorem & PACELC](./ch15-cap-theorem-pacelc.md)
*   [Ch 16: ACID vs. BASE Properties](./ch16-acid-base-transactions.md)
*   [Ch 17: Relational (SQL) vs. Non-Relational (NoSQL)](./ch17-sql-nosql-databases.md)
*   [Ch 18: Special Purpose Storage](./ch18-special-purpose-storage.md)

### Part 5: Asynchronous Systems & Event-Driven Patterns
*   [Ch 19: Message Queues vs. Event Streams (Kafka vs. RabbitMQ)](./ch19-queues-vs-streams.md)
*   [Ch 20: Publish-Subscribe & Event-Driven Architecture](./ch20-pub-sub-patterns.md)
*   [Ch 21: Event Sourcing & CQRS](./ch21-event-sourcing-cqrs.md)
*   [Ch 22: Saga Distributed Transactions](./ch22-saga-distributed-transactions.md)
*   [Ch 23: Outbox Pattern & Idempotency](./ch23-outbox-pattern-idempotency.md)

### Part 6: Fault Tolerance & Resiliency
*   [Ch 24: Circuit Breaker & Retry Patterns](./ch24-circuit-breaker-retry.md)
*   [Ch 25: Rate Limiting & Backpressure](./ch25-rate-limiting-backpressure.md)
*   [Ch 26: Disaster Recovery (Active-Active, Active-Passive)](./ch26-disaster-recovery.md)
*   [Ch 27: Distributed Consensus (Paxos, Raft, ZooKeeper)](./ch27-distributed-consensus.md)

### Part 7: Observability & Interview Prep
*   [Ch 28: Distributed Observability: Tracing, Logs, Metrics](./ch28-distributed-observability.md)
*   [Ch 29: System Design Blueprint & Mock Cases](./ch29-system-design-blueprint.md)

---

## Core Systems Roadmap

```text
               +--------------------------------------+
               |          Clients / CDN Edge          |
               +--------------------------------------+
                                  |
                                  v (DNS Geo-Routing)
               +--------------------------------------+
               |          L4/L7 Load Balancers        |
               +--------------------------------------+
                                  |
                                  v
               +--------------------------------------+
               |             API Gateways             |
               +--------------------------------------+
                                  |
            +---------------------+---------------------+
            |                     |                     |
            v                     v                     v
     +--------------+      +--------------+      +--------------+
     | Microservice |      | Microservice |      | Microservice |
     +--------------+      +--------------+      +--------------+
            |                     |                     |
            +----------+----------+                     v
                       |                         [Message Broker]
                       v                         (Kafka/RabbitMQ)
               +---------------+                        |
               | Shared Cache  |                        v
               +---------------+                 +--------------+
                       |                         | Worker Nodes |
                       v                         +--------------+
         +---------------------------+
         | Relational / NoSQL DBs    |
         | (Replicated & Sharded)    |
         +---------------------------+
```

---

## Next Chapter

Continue to [Client-Server & Communication Protocols](./ch01-client-server-protocols.md) to explore network communication layers.
