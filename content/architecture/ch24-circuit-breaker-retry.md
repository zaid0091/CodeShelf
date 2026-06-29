---
title: Circuit Breaker & Retry Patterns
description: Learn how to build resilient systems using Circuit Breaker states (Closed, Open, Half-Open) and Retries with Exponential Backoff and Jitter.
order: 24
tags: [architecture, circuit-breaker, retries, jitter, backoff, resiliency]
---

# Chapter 24: Circuit Breaker & Retry Patterns

> **Prevent cascading failures. Implement Circuit Breaker states, write retries with exponential backoff and jitter, and isolate service resources.**

---

## Cascading Failures in Microservices

In a microservice network, services call other services. If Service C is running slowly or failing, Service B's threads will block waiting for responses. Soon, Service B exhausts its thread pool, causing Service A (the API Gateway) to fail as well. A single minor node failure cascades upstream, bringing down the entire application.

---

## The Retry Pattern with Backoff & Jitter

When a transient network error occurs, clients should retry the call. However, retrying immediately can overload the failing service (Thundering Herd).

### Secure Retry Logic
1.  **Exponential Backoff**: Increase the delay between retries exponentially (e.g. 1s, 2s, 4s, 8s).
2.  **Jitter**: Add a random variable (noise) to the delay to prevent all clients from retrying at the exact same millisecond.

```python
# Retry with Backoff and Jitter (Python)
import time
import random

def call_with_retry(api_func, max_retries=5):
    for attempt in range(max_retries):
        try:
            return api_func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise e
            # Exponential backoff: 2^attempt
            delay = (2 ** attempt) + random.uniform(0, 1) # Jitter
            time.sleep(delay)
```

---

## The Circuit Breaker Pattern

The Circuit Breaker pattern acts like an electrical fuse. It wraps client calls and blocks requests to a failing service instantly if the failure rate crosses a threshold, preventing resource exhaustion.

```text
       +------------------------------------+
       |                                    | (Success rate returns to normal)
       v                                    |
  +--------+    Failures > Threshold    +------+
  | Closed | -------------------------> | Open |
  +--------+                            +------+
       ^                                    |
       |                                    | (Cooldown timeout expires)
       |            Test fails              v
       +------------------------------ +-----------+
                                       | Half-Open |
                                       +-----------+
```

### Circuit Breaker States
1.  **Closed (Normal State)**: Requests flow freely to the target service. The circuit breaker monitors error rates.
2.  **Open (Tripped State)**: The target service is failing. The circuit breaker intercepts calls and returns errors or fallback data *instantly* without forwarding requests, saving network threads.
3.  **Half-Open (Testing State)**: After a cooldown timeout, the circuit breaker allows a limited number of test requests to pass through:
    *   If the test requests succeed, it returns to the **Closed** state (healed).
    *   If any test request fails, it returns to the **Open** state (cooldown resets).

---

## Best Practices & Pitfalls

| Best Practice | Common Pitfall |
|---------------|----------------|
| Configure meaningful fallbacks (like cached static profiles or empty shopping carts) when a circuit breaker trips. | Retrying operations that are not idempotent (like a charge payment request), resulting in duplicate transactions. |

---

## Interview Points

> **📌 Interview Point 1: What is the difference between Open and Closed states in a Circuit Breaker?**
> In the **Closed** state, the circuit is complete, and traffic flows normally. In the **Open** state, the circuit is broken, and all traffic is blocked and failed immediately to prevent resource exhaustion.

---

## Exercises

### Exercise 1: Evaluate Jitter ⭐
**Task:** If 1,000 client instances retry a database connection every 2 seconds without jitter, what is the impact on the recovering database?

<details>
<summary>✅ Solution (click to reveal)</summary>
The database experiences severe spikes of 1,000 concurrent connection requests at exact 2-second intervals (Thundering Herd), crashing it again. Jitter spreads out these requests, smoothing the load.
</details>

---

## Next Chapter

Continue to [Rate Limiting & Backpressure](./ch25-rate-limiting-backpressure.md) to explore traffic control.
