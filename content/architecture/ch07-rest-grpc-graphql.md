---
title: REST vs. gRPC vs. GraphQL
description: Compare REST, gRPC (Protocol Buffers), and GraphQL. Learn about serialization overhead, schemas, streaming, and choosing the right API pattern.
order: 7
tags: [architecture, api, rest, grpc, graphql, serialization]
---

# Chapter 7: REST vs. gRPC vs. GraphQL

> **Analyze API architectural patterns, compare serialization overheads, examine client query flexibility, and select optimal transfer layers.**

---

## 1. REST (Representational State Transfer)

REST is the standard API architecture for public web services. It is stateless, resource-oriented, and relies on standard HTTP methods (GET, POST, PUT, DELETE).

*   **Format**: Plain text JSON or XML.
*   **Pros**: Highly cacheable, universally understood by browsers, human-readable payloads.
*   **Cons**: Over-fetching (server returns fields the client doesn't need) or Under-fetching (client must make multiple API calls to gather associated data).

---

## 2. gRPC (gRPC Remote Procedure Call)

Developed by Google, gRPC is a high-performance framework designed for backend microservices.

*   **Format**: Binary serialization using **Protocol Buffers (Protobuf)** over **HTTP/2**.
*   **Key Features**:
    *   **Strict Contract**: APIs are defined in `.proto` files, which auto-generate client/server code in multiple languages.
    *   **Streaming**: Supports client streaming, server streaming, and bi-directional streaming natively.
*   **Pros**: Minimal CPU overhead, tiny payload sizes, type safety.
*   **Cons**: Hard to debug (binary format), poor browser support (requires proxies).

---

## 3. GraphQL

Developed by Facebook, GraphQL is a query language for APIs that allows clients to define the exact shape of the response data.

*   **Format**: Single endpoint accepting query strings over HTTP.
*   **Key Features**:
    *   **Schema Definition**: Strongly typed schema defining all queries, mutations, and types.
    *   **No Over-fetching**: Client requests only the required fields.
*   **Pros**: Minimizes roundtrips to the server, ideal for complex frontend apps with nested relationships.
*   **Cons**: Complex query parsing, difficult to cache at the HTTP level (uses POST for queries), risk of N+1 database query issues.

---

## Comparison Table

| Metric | REST | gRPC | GraphQL |
|--------|------|------|---------|
| **Data Format** | JSON / XML (Text) | Protocol Buffers (Binary) | JSON (Text) |
| **Transport** | HTTP/1.1 or HTTP/2 | HTTP/2 (Multiplexed) | HTTP/1.1 or HTTP/2 |
| **Schema** | Optional (OpenAPI/Swagger) | Required (`.proto`) | Required (GraphQL Schema) |
| **Streaming** | Request/Response only | Bidirectional Streaming | Subscriptions (WebSockets) |
| **Caching** | Native HTTP caching | Non-cacheable | Complex (requires custom client caches) |

---

## Best Practices & Pitfalls

| Best Practice | Common Pitfall |
|---------------|----------------|
| Use REST for public-facing developer APIs; use gRPC for high-throughput internal microservice networks; use GraphQL for frontend web/mobile clients. | Allowing clients to write arbitrary nested GraphQL queries without implementing query depth limits, opening paths for Denial of Service CPU crashes. |

---

## Interview Points

> **📌 Interview Point 1: What is the N+1 problem in GraphQL and how do you solve it?**
> The N+1 problem occurs when a client requests a list of parent items and their nested child relationships, causing the server to execute one query for the list and then $N$ separate queries to fetch children. It is resolved using **DataLoader** patterns, which batch and cache database operations during the request execution lifecycle.

---

## Exercises

### Exercise 1: Choose the API architecture ⭐
**Task:** Select the best API model for an internal chat service that needs to stream message blocks constantly between microservices with minimal payload size.

<details>
<summary>✅ Solution (click to reveal)</summary>
**gRPC**. It natively supports bidirectional streaming over HTTP/2 and uses compressed binary Protocol Buffers, minimizing CPU and network latency.
</details>

---

## Next Chapter

Continue to [Load Balancers: L4 vs. L7](./ch08-load-balancers.md) to explore traffic routing.
