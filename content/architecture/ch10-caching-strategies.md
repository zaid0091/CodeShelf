---
title: Caching Strategies & Eviction
description: Master caching architectures in system design. Learn about Cache-Aside, Write-Through, Write-Behind, eviction policies (LRU, LFU), and stampede mitigation.
order: 10
tags: [architecture, caching, cache-aside, lru, redis, cache-stampede]
---

# Chapter 10: Caching Strategies & Eviction

> **Speed up operations. Implement Cache-Aside and Write-Through patterns, configure eviction policies, and mitigate cache stampedes.**

---

## Caching Patterns

Caching stores copies of frequently accessed data in fast, in-memory storage (like Redis or Memcached).

### 1. Cache-Aside (Lazy Loading)
The application code coordinates cache operations directly:
1. Try to read from cache (Cache Hit -> return).
2. If missing (Cache Miss), read from database.
3. Write database result back to cache and return.
*   *Pros:* Cache only stores queried data; DB failures don't crash cache.
*   *Cons:* Triple network round-trips on miss; data can become stale if updated in DB without cache invalidation.

### 2. Read-Through / Write-Through
The application treats the cache as the main data store. A cache library/module handles reading and writing database transactions synchronously.
*   *Pros:* Simplifies application code; ensures cache is never stale.
*   *Cons:* High write latency (waits for database write to complete).

### 3. Write-Behind (Write-Back)
The application writes data to the cache, which returns immediately. The cache writes the data to the database asynchronously in background batches.
*   *Pros:* Extremely high write performance (non-blocking).
*   *Cons:* Risk of data loss if the cache server crashes before flushing updates to the database.

---

## Cache Eviction Policies

When the cache memory is full, the server must discard old keys to free up space:

*   **LRU (Least Recently Used)**: Discards the keys that haven't been accessed for the longest time. The standard default for most systems.
*   **LFU (Least Frequently Used)**: Tracks access counts and discards keys with the lowest query frequency.
*   **FIFO (First In, First Out)**: Discards keys based on creation order.
*   **TTL (Time To Live)**: Expires keys automatically after a set duration.

---

## Mitigating Cache Failures

### 1. Cache Avalanche
Occurs when multiple cached keys expire at the exact same time, or the cache cluster fails, forcing all traffic to hit the database concurrently.
*   *Mitigation:* Add random jitter (e.g. +/- 5 minutes) to TTL values so keys expire at different times.

### 2. Cache Penetration
Occurs when queries request keys that exist neither in the cache nor in the database (e.g. ID `-999`). The database is queried on every request.
*   *Mitigation:* Cache null values or deploy a **Bloom Filter** (a space-efficient probabilistic data structure) in front of the cache to quickly reject non-existent keys.

### 3. Cache Stampede (Thundering Herd)
Occurs when a highly popular key (e.g., trending news) expires. Multiple app servers execute database queries concurrently to regenerate the cache key.
*   *Mitigation:* Implement locking (mutex) so only one thread regenerates the cache key while others wait or return stale data.

---

## Best Practices & Pitfalls

| Best Practice | Common Pitfall |
|---------------|----------------|
| Set explicit TTLs on all cached keys to prevent memory leaks from forgotten data. | "There are only two hard things in Computer Science: cache invalidation and naming things." (Phil Karlton). Updating the database without invalidating the matching cache key, causing stale data renders. |

---

## Interview Points

> **📌 Interview Point 1: What is a Bloom Filter?**
> A probabilistic data structure used to check if an element is a member of a set. It never returns false negatives (if it says the key does not exist, it definitely does not), but can return false positives (might say it exists when it doesn't). It prevents Cache Penetration with minimal memory overhead.

---

## Exercises

### Exercise 1: Choose the write pattern ⭐
**Task:** Select the best write caching pattern for a highly active logging platform that wants to capture millions of user logs with minimal database write bottlenecks.

<details>
<summary>✅ Solution (click to reveal)</summary>
**Write-Behind (Write-Back)**. Writing to memory (cache) is extremely fast, and the batch processing asynchronously flushes data to the database in background threads, neutralizing database write IOPS limits.
</details>

---

## Next Chapter

Continue to [CDN (Content Delivery Networks)](./ch11-cdn-edge-caching.md) to explore static edge caching.
