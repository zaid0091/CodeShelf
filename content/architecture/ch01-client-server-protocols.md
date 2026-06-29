---
title: Client-Server & Communication Protocols
description: Explore HTTP/1.1, HTTP/2, HTTP/3, WebSockets, gRPC, and the OSI model (Layer 4 vs Layer 7) in system design.
order: 1
tags: [architecture, networking, protocols, http, grpc, websockets]
---

# Chapter 1: Client-Server & Communication Protocols

> **Master the mechanisms clients and servers use to transmit data, compare transport layers, and select optimal communication protocols.**

---

## Client-Server Communication Models

In web architecture, systems talk using specific request-response or streaming models. Selecting the correct model affects latency, throughput, and connection overhead.

---

## Key Protocols Compared

### 1. HTTP Evolution
*   **HTTP/1.1**: Simple, text-based. Requires opening a new TCP connection for concurrent requests (or queuing via Head-of-Line blocking).
*   **HTTP/2**: Binary-based. Introduces **Multiplexing** (multiple requests stream concurrently over a single TCP connection) and Header Compression (HPACK).
*   **HTTP/3**: Replaces TCP with **QUIC** (UDP-based). Eliminates TCP-level Head-of-Line blocking and makes connection handshakes faster.

### 2. WebSockets (Duplex)
Provides a persistent, bi-directional, full-duplex TCP connection. The client initiates a connection handshake over HTTP and upgrades it to WebSockets.
*   *Use Case:* Real-time chat apps, live dashboards, multiplayer games.

### 3. gRPC (Remote Procedure Call)
A high-performance framework developed by Google. It runs on HTTP/2 and uses **Protocol Buffers (protobuf)** as its binary serialization format (much smaller and faster than JSON).
*   *Use Case:* Microservice-to-microservice backend communication.

### 4. Polling vs. Long Polling vs. SSE
*   **Polling**: Client regularly requests updates (high overhead).
*   **Long Polling**: Server holds the request open until new data is available.
*   **Server-Sent Events (SSE)**: Persistent, one-way connection where the server pushes updates to the client.

---

## The OSI Model: Layer 4 vs. Layer 7

In system design, load balancing and routing are classified by OSI (Open Systems Interconnection) layers:

*   **Layer 4 (Transport Layer - TCP/UDP)**: Routes traffic based on IP addresses and ports. It does not inspect the message payload. Extremely fast, low overhead.
*   **Layer 7 (Application Layer - HTTP/HTTPS)**: Routes traffic based on message content (headers, cookie data, URL paths). Allows smart routing but requires decrypting TLS, increasing CPU load.

---

## Best Practices & Pitfalls

| Best Practice | Common Pitfall |
|---------------|----------------|
| Use gRPC for internal backend microservices to minimize payload sizes and enable strict contract typing. | Using WebSockets for simple, occasional updates, which wastes server resources maintaining idle TCP connections. Use Long Polling or SSE instead. |

---

## Interview Points

> **📌 Interview Point 1: What is HTTP/2 Head-of-Line (HoL) Blocking?**
> In HTTP/1.1, HoL blocking occurs when a slow request blocks subsequent requests in the queue. HTTP/2 solves this with multiplexing, but TCP-level HoL blocking remains: if a single TCP packet is dropped, the entire connection freezes until the packet is retransmitted. HTTP/3 resolves this by running on UDP/QUIC.

---

## Exercises

### Exercise 1: Choose the Protocol ⭐
**Task:** Select the best protocol for a stock price dashboard requiring sub-second updates from server to client.

<details>
<summary>✅ Solution (click to reveal)</summary>
**Server-Sent Events (SSE)** or **WebSockets**. Since stock prices require one-way streaming from server to client, SSE is lighter and simpler than WebSockets. If the client also needs to send rapid updates back, WebSockets is preferred.
</details>

---

## Next Chapter

Continue to [Vertical vs. Horizontal Scaling](./ch02-vertical-horizontal-scaling.md) to explore how systems grow.
