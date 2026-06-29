---
title: Rate Limiting & Denial of Service (DoS) Prevention
description: Learn about application-level rate limiting algorithms (Token Bucket, Sliding Window), using Redis for distributed rate limiting, and mitigating DoS vectors.
order: 26
tags: [security, rate-limiting, dos, redis, algorithms]
---

# Chapter 26: Rate Limiting & Denial of Service (DoS) Prevention

> **Harden APIs against automated abuse, implement token bucket and sliding window rate limiting, and write Redis-backed rate controls.**

---

## The Risk: Automated API Abuse

Without rate limiting, APIs are vulnerable to abuse:
*   **Brute-Force Attacks**: Attackers submit thousands of credentials to login endpoints.
*   **Data Scraping**: Automated crawlers harvest public user databases.
*   **Resource Exhaustion**: Triggering complex, slow queries (like heavy search terms) to overload databases, causing a Denial of Service (DoS).

---

## Rate Limiting Algorithms

1. **Token Bucket**: The bucket has a maximum capacity of tokens. Every request consumes a token. Tokens refill at a steady rate. If the bucket is empty, requests are dropped.
2. **Leaky Bucket**: Requests enter a queue and are processed at a constant, steady rate. Good for smoothing out bursts of traffic.
3. **Sliding Window Log**: Tracks request timestamps in a sorted set (log). Computes requests in real-time within the last $N$ seconds, providing maximum precision.

---

## Distributed Rate Limiting with Redis

When running multiple backend servers behind a load balancer, local in-memory rate limiting fails because count data is not shared. Use a shared **Redis** cache to coordinate rates.

### Redis Sliding Window Logic (Python Concept)
```python
import time
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def is_rate_limited(user_id: str, limit: int = 100, window: int = 60) -> bool:
    current_time = time.time()
    key = f"rate_limit:{user_id}"
    
    # Use a Redis transaction (pipeline) to keep atomic operations
    pipe = r.pipeline()
    # 1. Remove timestamps older than current window
    pipe.zremrangebyscore(key, 0, current_time - window)
    # 2. Retrieve remaining count
    pipe.zcard(key)
    # 3. Add current timestamp to sorted set
    pipe.zadd(key, {str(current_time): current_time})
    # 4. Set expiration on key to clean up disk space
    pipe.expire(key, window)
    
    _, count, _, _ = pipe.execute()
    
    if count >= limit:
        return True # Limit exceeded
    return False # Request allowed
```

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Return an HTTP `429 Too Many Requests` status code with a `Retry-After` header when rate limits are exceeded. | Using client IP addresses as the sole rate limit identifier (this groups all users behind a corporate proxy or public NAT firewall together). Use authenticated User IDs instead. |

---

## Interview Points

> **📌 Interview Point 1: What is a Distributed Denial of Service (DDoS) attack and how does it differ from DoS?**
> A **DoS** attack originates from a single source IP. A **DDoS** attack uses a distributed network of thousands of compromised devices (botnets) to flood servers. Application-level rate limiters block single-client abuse, but DDoS mitigation requires network-edge scrubbing systems (like Cloudflare or AWS Shield).

---

## Exercises

### Exercise 1: Evaluate rate limits ⭐
**Task:** Why should your `/api/login` route have a much stricter rate limit than your `/api/products` route?

<details>
<summary>✅ Solution (click to reveal)</summary>
Login endpoints are prime targets for automated credential stuffing and brute-force attacks. They are also CPU-heavy because password hashing ciphers (Bcrypt/Argon2) are intentionally slow.
</details>

---

## Next Chapter

Continue to [Security Logging & Monitoring](./ch27-security-logging-monitoring.md) to explore auditing controls.
