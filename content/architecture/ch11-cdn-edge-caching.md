---
title: CDN (Content Delivery Networks)
description: Master Content Delivery Networks (CDNs), Points of Presence (POPs), Push vs. Pull models, and static/dynamic edge caching strategies.
order: 11
tags: [architecture, cdn, edge-caching, caching, performance, infrastructure]
---

# Chapter 11: CDN (Content Delivery Networks)

> **Cache content at the internet's edge. Compare Push vs. Pull CDNs, manage cache purging, and serve assets with minimal latency.**

---

## What is a CDN?

A Content Delivery Network is a globally distributed network of proxy servers called **Points of Presence (POPs)**. CDNs cache static assets (and sometimes dynamic content) geographically close to users, reducing page load times and saving origin server bandwidth.

```text
User (Paris) -> [CDN Edge Server (Paris POP)] -> Cache Hit (Loads in 10ms)
                               | (Cache Miss)
                               v
                     [Origin Server (New York)] (Loads in 250ms)
```

---

## Push vs. Pull CDNs

### 1. Pull CDN (Standard)
The developer configures the CDN to point to their origin server.
*   **Request Flow**: When a user requests an asset, the CDN checks its local cache. If it is a cache miss, the CDN pulls the asset from the origin server, caches it locally, and returns it to the user.
*   **Use Case**: Highly popular sites with changing static files. Requires minimal management.

### 2. Push CDN
The developer uploads (pushes) assets directly to the CDN storage.
*   **Request Flow**: The CDN serves content directly from its storage. It never queries the origin server.
*   **Use Case**: Large file downloads, video libraries, or rarely updated archives. Requires active deployment workflows.

---

## Caching Strategies: Static vs. Dynamic

*   **Static Assets (Images, JS, CSS)**: Cache with long TTLs (e.g. 1 year).
*   **Dynamic Assets (APIs, User Pages)**: Generally bypassed (`Cache-Control: private, no-store`). However, you can cache API responses at the edge with short TTLs (e.g. 5 seconds) to handle sudden viral traffic spikes (micro-caching).

---

## Cache Invalidation (Purging)

When files update, the CDN must discard outdated copies:
1. **URL Purging**: Purges specific file paths.
2. **Tag-Based Purging**: Assigns HTTP headers (`Cache-Tag: articles`) and purges entire groups.
3. **Cache Busting**: Versioning assets in the HTML (e.g., `main.js?v=2` or `main.a1b2c3.js`). This changes the request URL, forcing the CDN to fetch a new file without requiring manual purge executions.

---

## Best Practices & Pitfalls

| Best Practice | Common Pitfall |
|---------------|----------------|
| Configure wildcard SSL certificates at the CDN edge to enable HTTPS handshakes close to the user, reducing connection latency. | Forgetting to set a proper `Cache-Control` header on files, allowing CDNs to cache private user dashboards or billing endpoints. |

---

## Interview Points

> **📌 Interview Point 1: What is the Origin Shield pattern?**
> An extra caching layer placed between CDN edge servers and the origin server. If 50 different edge servers experience cache misses for the same file, they query the Origin Shield server instead of overloading the origin server with 50 duplicate requests.

---

## Exercises

### Exercise 1: Choose the CDN model ⭐
**Task:** Select the best CDN pattern for a media blog that publishes 50 new images every day and wants setup simplicity.

<details>
<summary>✅ Solution (click to reveal)</summary>
**Pull CDN**. The setup is automatic: when an image is first requested, the CDN pulls it from the blog server, caching it for subsequent users. No custom upload scripts are needed.
</details>

---

## Next Chapter

Continue to [Edge Computing & Serverless Edge](./ch12-edge-computing.md) to explore compute at the internet's periphery.
