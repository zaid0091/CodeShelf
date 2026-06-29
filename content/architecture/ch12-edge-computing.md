---
title: Edge Computing & Serverless Edge
description: Explore Edge Computing architectures, Serverless at the Edge (Cloudflare Workers), reducing RTT, and edge storage concepts.
order: 12
tags: [architecture, edge-computing, serverless, cloudflare-workers, latency]
---

# Chapter 12: Edge Computing & Serverless Edge

> **Run logic at the network boundary. Explore serverless edge runtimes, minimize round-trip times, and configure edge Key-Value storage.**

---

## What is Edge Computing?

Edge computing moves logic and compute resources away from centralized cloud data centers (like AWS `us-east-1`) and runs them directly inside CDN Points of Presence (POPs) located globally, right next to the user.

---

## Serverless at the Edge

Traditional serverless functions (like standard AWS Lambda) run in centralized zones. **Edge Functions** (like Cloudflare Workers, Vercel Edge Middleware, or Fastly Compute) run directly on CDN nodes:

*   **Technology**: Instead of booting heavy containers (Node.js/Docker), edge runtime platforms use lightweight **V8 Isolates** (compiled JavaScript engines).
*   **Startup Speed**: Boot times are virtually zero (sub-millisecond), eliminating cold starts.

---

## Use Cases for Edge Logic

*   **A/B Testing**: Randomly route users to different page versions at the edge without causing layout shifts or loading delay flashes.
*   **Header Manipulation**: Inject security headers (like HSTS or CSP) or filter cookies before requests reach the origin.
*   **Geo-Customization**: Detect user country and automatically redirect them to `/fr` or `/de` instantly.
*   **Authentication Gates**: Validate JWT signatures at the edge, blocking unauthorized requests before they consume origin CPU resources.

---

## Edge Storage

Edge runtimes have access to globally replicated, low-latency databases (like Cloudflare KV or Durable Objects). These are highly optimized for reads but have slow write speeds because changes must propagate globally.

---

## Best Practices & Pitfalls

| Best Practice | Common Pitfall |
|---------------|----------------|
| Keep edge functions small and lightweight. Focus on routing, cookies, redirects, and basic authentication. | Querying a centralized SQL database (like PostgreSQL in Oregon) from an edge function in Tokyo. The network round-trip latency defeats the purpose of running code at the edge. |

---

## Interview Points

> **📌 Interview Point 1: Why do V8 Isolates eliminate cold starts compared to Docker containers?**
> Docker containers require booting an entire virtual operating system kernel and runtime stack. V8 Isolates run multiple isolated code execution contexts inside a single, shared operating system process, avoiding container boot overhead.

---

## Exercises

### Exercise 1: Evaluate latency trade-offs ⭐
**Task:** Explain why running a heavy PDF generator at the edge is not recommended.

<details>
<summary>✅ Solution (click to reveal)</summary>
PDF generation is CPU-intensive. Edge runtimes have strict memory limits (e.g. 50MB-128MB) and CPU timeout constraints. Heavy processing should be offloaded to centralized cloud servers or background queues.
</details>

---

## Next Chapter

Continue to [Database Scaling: Replication](./ch13-database-scaling.md) to explore database scaling.
