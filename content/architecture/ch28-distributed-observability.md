---
title: "Distributed Observability: Tracing, Logs, Metrics"
description: Master distributed systems observability. Learn about Trace IDs, Span IDs, context propagation, OpenTelemetry, metrics types, and Prometheus.
order: 28
tags: [architecture, observability, distributed-tracing, opentelemetry, metrics, logs]
---

# Chapter 28: Distributed Observability: Tracing, Logs, Metrics

> **Monitor complex distributed networks. Implement distributed tracing, propagate trace contexts, and monitor application metrics.**

---

## Observability vs. Monitoring

*   **Monitoring**: Tells you *when* a system is failing (e.g. "Alert: API error rate is > 5%").
*   **Observability**: Allows you to understand *why* a system is failing by inspecting its internal states and dependencies in real-time.

---

## The Three Pillars of Observability

```text
               +--------------------------------------+
               |      Pillars of Observability        |
               +--------------------------------------+
                /                 |                  \
           [Metrics]            [Logs]            [Traces]
       (How is it now?)   (What happened when?) (Where did it flow?)
```

### 1. Metrics (Aggregated Numeric Data)
Time-series data points indicating resource usage and system health.
*   **Counter**: A cumulative metric that only increases (e.g., total requests received).
*   **Gauge**: A single numerical value that can go up and down (e.g., current memory usage, thread pool size).
*   **Histogram**: Measures the distribution of values (e.g., request latency percentiles: p95, p99).

### 2. Logs (Discrete Event Text)
Detailed text records of events. In distributed systems, logs must be **Structured** (JSON format) to allow automated indexing and search queries.

### 3. Traces (Request Journeys)
Tracks the lifecycle of a request as it flows across multiple backend microservices.

---

## Distributed Tracing: Trace IDs & Span IDs

When a client initiates a request:
1.  **Trace ID**: The entry service generates a unique Trace ID for the request.
2.  **Span ID**: Each individual operation within a service is represented by a Span ID.
3.  **Context Propagation**: When Service A calls Service B, it passes the Trace ID in the HTTP headers (e.g., using `traceparent` standard). All downstream logs use the same Trace ID.

```text
Trace ID: 00-4bf92f3577b34da6a3ce929d0e0e4736 (Shared across all logs)
  ├── Span 1 (API Gateway) -> Span ID: 00f067aa0ba902b7
  └── Span 2 (User Service) -> Span ID: 5fb397be34d23b0f
```
*If a payment fails, searching the Trace ID in your log collector brings up logs from the Gateway, Payment service, and database queries in a single timeline.*

---

## Standards: OpenTelemetry

**OpenTelemetry (OTel)** is an open-source observability framework. It provides a standardized set of APIs, SDKs, and tooling to generate, collect, and export traces, metrics, and logs, preventing vendor lock-in.

---

## Best Practices & Pitfalls

| Best Practice | Common Pitfall |
|---------------|----------------|
| Set up trace sampling (e.g., only log 5% of successful traces, but 100% of error traces) to save storage costs. | Writing un-structured plain-text logs in microservices, making it impossible to run aggregation searches. |

---

## Interview Points

> **📌 Interview Point 1: What is Context Propagation in Distributed Tracing?**
> The process of transferring trace metadata (like Trace ID and baggage headers) across network boundaries (e.g., injected into HTTP headers or metadata fields in gRPC/Kafka messages) so downstream services can join the trace.

---

## Exercises

### Exercise 1: Identify Metric types ⭐
**Task:** Classify the following metrics:
1. Active websocket connections.
2. Total bytes sent.

<details>
<summary>✅ Solution (click to reveal)</summary>
1. **Gauge** (can increase and decrease).
2. **Counter** (only increases over time).
</details>

---

## Next Chapter

Continue to [System Design Blueprint & Mock Cases](./ch29-system-design-blueprint.md) to practice mock system interview cases.
