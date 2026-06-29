---
title: Rate Limiting & Backpressure
description: Explore traffic flow control patterns. Compare rate limiting against backpressure, and implement producer-consumer stream throttling.
order: 25
tags: [architecture, rate-limiting, backpressure, flow-control, streams]
---

# Chapter 25: Rate Limiting & Backpressure

> **Control data flow. Compare rate limiting and backpressure, implement stream throttling, and prevent buffer overflows.**

---

## Traffic Flow Control

In distributed systems, data flows between producers and consumers. If a producer generates data faster than a consumer can process it, the consumer's buffers overflow, causing memory leaks, thread starvation, or system crashes.

Two main patterns handle this: **Rate Limiting** (usually server-side enforcement) and **Backpressure** (feedback-driven stream control).

---

## Rate Limiting vs. Backpressure

*   **Rate Limiting**: The server defines a threshold (e.g. 100 requests/minute) and rejects any excess requests by returning errors (like `429 Too Many Requests`). The client must handle the failure.
*   **Backpressure**: The consumer communicates its current capacity to the producer, instructing the producer to slow down or pause data generation before buffers overflow.

---

## Implementing Backpressure in Streams

In asynchronous streaming systems (like Reactive Streams or Akka/Pekko Streams), backpressure is managed through three primary strategies:

```text
               +--------------------------------------+
               |    Producer sends 1000 items/sec     |
               +--------------------------------------+
                                  |
                                  v
               +--------------------------------------+
               |     Consumer can process 100 items   |
               +--------------------------------------+
                /                 |                  \
           [Buffer]            [Drop]             [Control]
   (Save items in memory) (Discard latest items) (Signal producer to slow)
```

1.  **Buffering**: Store incoming items in a queue until the consumer is ready.
    *   *Limit:* If the mismatch persists, the queue runs out of memory, causing an Out Of Memory (OOM) error.
2.  **Dropping**: Discard incoming items that exceed the consumer's capacity.
    *   *Limit:* Data is lost, which is unacceptable for critical transactional systems.
3.  **Flow Control / Signaling**: The consumer sends credit/demand signals to the producer: "I can accept 5 items." The producer only sends 5 items and waits for the next demand signal.

---

## TCP-Level Backpressure

Backpressure exists at the network layer. In TCP connections, the receiver advertises its **Receive Window (RWND)** in header flags. If the receiver's OS buffer is full, it sets the RWND to 0. The sender immediately stops transmitting packets and waits until the receiver announces a non-zero window size.

---

## Best Practices & Pitfalls

| Best Practice | Common Pitfall |
|---------------|----------------|
| Set maximum bounds (size limits) on all asynchronous task queues to prevent infinite memory usage. | Relying on unbounded memory buffers, causing servers to crash under sudden traffic spikes. |

---

## Interview Points

> **📌 Interview Point 1: How does Backpressure solve the limitations of Buffering?**
> Buffering only delays failures: if the producer remains faster than the consumer, the memory buffer eventually overflows. Backpressure establishes a feedback loop, forcing the producer to match the speed of the consumer, preventing crashes.

---

## Exercises

### Exercise 1: Select the strategy ⭐
**Task:** Select the best flow control strategy for a system that streams live camera telemetry, where missing a frame is fine but latency must remain low.

<details>
<summary>✅ Solution (click to reveal)</summary>
**Dropping**. Since latency is critical and old frames are useless, dropping late frames prevents queue accumulation and keeps the stream real-time.
</details>

---

## Next Chapter

Continue to [Disaster Recovery (Active-Active, Active-Passive)](./ch26-disaster-recovery.md) to explore system recovery.
