---
title: API Gateways & Reverse Proxies
description: Understand the difference between forward and reverse proxies, and learn about the responsibilities of API Gateways (routing, SSL termination, auth offloading).
order: 6
tags: [architecture, proxy, reverse-proxy, api-gateway, routing, ssl-termination]
---

# Chapter 6: API Gateways & Reverse Proxies

> **Deconstruct proxy configurations, compare forward vs. reverse proxies, and implement centralized API Gateways to offload security and routing chores.**

---

## Forward Proxy vs. Reverse Proxy

Proxies act as intermediaries between clients and servers.

### 1. Forward Proxy (Client-Side)
A proxy that sits in front of clients. The server does not know the specific client IP (it only sees the proxy IP).
*   *Use Case:* Bypassing geo-restrictions, monitoring employees' web traffic, or hiding client identity.

### 2. Reverse Proxy (Server-Side)
A proxy that sits in front of web servers. Clients talk to the reverse proxy, which routes requests to internal backend servers.
*   *Use Case:* Load balancing, SSL/TLS termination, and caching.

```text
Forward Proxy: Clients -> [Proxy] -> Internet
Reverse Proxy: Internet -> [Proxy] -> Backend Servers
```

---

## What is an API Gateway?

An **API Gateway** is a specialized reverse proxy that serves as a single entry point for all client requests in a microservice architecture. It routes requests, orchestrates services, and offloads common cross-cutting concerns:

```text
Client -> [API Gateway (Auth / Rate Limit / SSL)] -> Internal Services (/users, /orders)
```

### Key Responsibilities

1. **Routing**: Matches URL paths to internal services (e.g. `/api/v1/users` -> Users Service).
2. **Authentication & Authorization**: Validates incoming JWT tokens or API keys once at the gateway level, passing user context headers to internal services. This prevents each service from writing custom auth logic.
3. **SSL Termination**: Decrypts incoming HTTPS requests at the gateway, routing unencrypted HTTP traffic to internal networks (saves CPU load on microservices).
4. **Rate Limiting**: Throttles abusive requests before they reach backend logic.
5. **Protocol Translation**: Translates incoming HTTP JSON requests into internal gRPC payloads.

---

## Common Tools

*   **Reverse Proxies / Load Balancers**: Nginx, HAProxy, Envoy.
*   **Centralized API Gateways**: Kong (Kong Gateway), AWS API Gateway, Apigee, Traefik.

---

## Best Practices & Pitfalls

| Best Practice | Common Pitfall |
|---------------|----------------|
| Configure high availability for your API Gateway (run multiple instances behind a Layer 4 load balancer) to prevent it from becoming a **Single Point of Failure (SPOF)**. | Putting heavy business logic inside the gateway. The gateway should remain lightweight and focus solely on routing, auth, and traffic control. |

---

## Interview Points

> **📌 Interview Point 1: What is the difference between an API Gateway and a Reverse Proxy?**
> A reverse proxy handles basic layer 4/7 routing, SSL termination, and caching. An API Gateway is application-aware: it handles user authentication, orchestrates request mapping across multiple microservices, and manages developer API keys.

---

## Exercises

### Exercise 1: Evaluate SSL Termination ⭐
**Task:** Why does terminating SSL at the API Gateway level reduce security within the internal network?

<details>
<summary>✅ Solution (click to reveal)</summary>
Because traffic between the API Gateway and internal microservices is sent in unencrypted HTTP. If an attacker gains access to the internal network, they can sniff database queries and API payloads.
</details>

---

## Next Chapter

Continue to [REST vs. gRPC vs. GraphQL](./ch07-rest-grpc-graphql.md) to compare API protocols.
