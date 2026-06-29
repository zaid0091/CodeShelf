---
title: "Load Balancers: L4 vs. L7"
description: Master load balancing in system design. Learn about Layer 4 vs. Layer 7 routing, load balancing algorithms, health checks, and active-passive HA.
order: 8
tags: [architecture, load-balancing, network-routing, proxy, algorithms]
---

# Chapter 8: Load Balancers: L4 vs. L7

> **Scale traffic across servers. Compare Layer 4 and Layer 7 routing strategies, evaluate load balancing algorithms, and implement active-passive high availability.**

---

## What is a Load Balancer?

A Load Balancer is a hardware or software system that sits in front of your server pool. It distributes incoming client requests across multiple backend application servers, ensuring no single server becomes overloaded.

---

## Layer 4 vs. Layer 7 Load Balancing

Load balancers inspect different packets of network data to route requests.

### 1. Layer 4 Load Balancing (Transport Layer)
*   **Routing Source**: IP addresses and TCP/UDP port numbers.
*   **Inspection**: The load balancer does *not* read HTTP headers, cookies, or request bodies.
*   **Performance**: Fast and low CPU overhead (no packet decryption needed).
*   **Limitation**: Cannot route traffic based on URL paths or user session cookies.

### 2. Layer 7 Load Balancing (Application Layer)
*   **Routing Source**: HTTP/HTTPS headers, cookie data, URL paths, and query string values.
*   **Inspection**: The load balancer decrypts SSL/TLS traffic and reads the HTTP content.
*   **Performance**: Higher CPU overhead (requires computational power to handle SSL handshakes and read payloads).
*   **Benefit**: Smart routing (e.g. `/images` -> Image Server pool, `/checkout` -> Checkout Server pool).

---

## Load Balancing Algorithms

*   **Round Robin**: Sends requests sequentially (Server 1, Server 2, Server 3, repeat). Assumes all servers have equal capacity.
*   **Weighted Round Robin**: Routes traffic based on assigned server weights (e.g., Server A has 2x CPU, gets 2x requests).
*   **Least Connections**: Routes requests to the server with the fewest active TCP connections. Ideal for long-running queries or sessions.
*   **IP Hash**: Hashes the client's IP address to determine the target server. Ensures a client is consistently routed to the same server (useful for **Sticky Sessions**).

---

## Health Checks & High Availability

Load balancers regularly send request checks (pings or HTTP GET queries) to backend servers. If a server fails to respond within a threshold (e.g., returns 500 or times out), the load balancer flags it as unhealthy and stops routing traffic to it.

### Scaling the Load Balancer
To prevent the load balancer itself from becoming a single point of failure (SPOF):
*   **Active-Passive HA**: Run two load balancers sharing a virtual IP (VIP) address using **Keepalived** or CARP. If the active node crashes, the passive node takes over the VIP instantly.

---

## Best Practices & Pitfalls

| Best Practice | Common Pitfall |
|---------------|----------------|
| Configure L7 load balancers to append the original client IP to the `X-Forwarded-For` header before forwarding requests. | Using IP Hash algorithms as a replacement for centralized session stores (Sticky Sessions violate stateless architecture principles). |

---

## Interview Points

> **📌 Interview Point 1: What happens to a client request if the load balancer has SSL Termination enabled?**
> The load balancer completes the SSL/TLS handshake with the client, decrypts the request, and forwards it to the backend server as unencrypted HTTP. This saves backend server CPU capacity but requires securing internal networks.

---

## Exercises

### Exercise 1: Choose the balancing algorithm ⭐
**Task:** A system runs background PDF generators. Some PDFs take 10 seconds to generate; others take 0.1 seconds. Which load balancing algorithm is best?

<details>
<summary>✅ Solution (click to reveal)</summary>
**Least Connections**. Round Robin would overload a server if it randomly received multiple slow PDF generation requests in a row. Least Connections ensures tasks go to servers with the lowest current workload.
</details>

---

## Next Chapter

Continue to [DNS Routing & Global Load Balancing](./ch09-dns-routing-gslb.md) to explore global traffic routing.
