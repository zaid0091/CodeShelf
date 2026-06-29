---
title: System Design Blueprint & Mock Cases
description: Master the 4-step System Design interview blueprint. Walk through mock cases for TinyURL and Instagram Feed designs.
order: 29
tags: [architecture, system-design, interview-prep, tinyurl, feeds, blueprints]
---

# Chapter 29: System Design Blueprint & Mock Cases

> **Master the system design interview. Apply the 4-step design blueprint, and walk through TinyURL and Instagram scale mock architectures.**

---

## The System Design Interview Blueprint

When designing large-scale systems, follow a structured 4-step framework to ensure you cover all requirements:

```text
Step 1: Scope the Problem (Functional & Non-Functional, Back-of-the-envelope calculations)
  ↓
Step 2: High-Level Design (APIs, Data Models, Core Architecture Flow)
  ↓
Step 3: Deep Dive Design (Scaling individual components, database sharding, caching)
  ↓
Step 4: Resolve Bottlenecks (Failovers, rate limiting, logging, security)
```

---

## Mock Case 1: Design a URL Shortener (TinyURL)

### Step 1: Scope the Problem
*   **Functional**: User submits a long URL -> returns a short URL. User visits short URL -> redirects to long URL.
*   **Non-Functional**: High availability, minimal latency, non-guessable links.
*   **Scale**: 100M URLs generated per month. 10:1 read-to-write ratio.
*   **QPS Calculations**:
    *   Writes: $100\text{M} / (30\text{ days} \times 86400\text{s}) \approx 40\text{ writes/sec}$
    *   Reads (Redirects): $40 \times 10 = 400\text{ reads/sec}$

### Step 2: High-Level Design
*   **API**:
    *   `POST /api/v1/shorten` -> returns `{"short_url": "http://tiny.url/abc123xy"}`
    *   `GET /{short_key}` -> HTTP 302 redirect to Long URL.
*   **Database**: Key-value structure. No joins required. Select NoSQL (like MongoDB or DynamoDB) or relational DB with primary keys (`short_key`, `long_url`).

### Step 3: Deep Dive (Key Generation)
How do we generate unique 7-character keys?
*   **Hashing (MD5)**: Taking first 7 chars of `md5(long_url)`.
    *   *Issue:* Collision risk. Requires checking database before inserting.
*   **Key Generation Service (KGS)**: A separate service pre-generates random 7-character strings in a database and loads them into a fast in-memory queue. When a user requests a short URL, the app server simply pulls a key from the queue, guaranteeing uniqueness and eliminating runtime database checks.

---

## Mock Case 2: Design an Activity Feed (Instagram/Twitter)

### Step 1: Scope the Problem
*   **Functional**: Users can post images. Users can follow other users. Users can view a timeline feed of posts from people they follow.
*   **Scale**: 500M active users. 1M posts per day.
*   **Reads vs Writes**: Feed generation is read-heavy.

### Step 2: High-Level Design (Fan-Out)
When a user updates their feed, how do we distribute the post?

```text
Pull Model (Fan-out on Read):
  User opens feed -> query follows table -> fetch latest posts from all followed -> merge/sort.
  *Issue:* Slow load times for users who follow thousands of people.

Push Model (Fan-out on Write):
  User posts image -> fetch user's followers -> write post ID to every follower's pre-computed "Inbox" cache.
  *Issue:* If a celebrity posts, they have 100M followers, triggering 100M cache writes (celebrity bottleneck).

Hybrid Model (The Solution):
  For standard users: Use Push Model (writes to follower caches).
  For high-follower celebrities: Do not push. When followers load their feeds, pull celebrity posts and merge.
```

---

## Best Practices & Pitfalls

| Best Practice | Common Pitfall |
|---------------|----------------|
| Start with functional requirements and estimations before drawing any server components. | Diving straight into drawing database clusters and message queues without understanding scale constraints. |

---

## Interview Points

> **📌 Interview Point 1: What is the difference between HTTP 301 and HTTP 302 redirects in a URL shortener?**
> **301 Redirect**: Permanent redirect. Browsers cache the redirect destination. Subsequent clicks bypass the shortener server. Good for speed, bad for analytics.
> **302 Redirect**: Temporary redirect. Browsers query the shortener server on every click, allowing accurate tracking of click counts and user demographics.

---

## Exercises

### Exercise 1: Calculate Storage ⭐
**Task:** If a URL shortener saves 100 million records per month, and each record takes 500 bytes of database storage, how much disk space is required to store 5 years of data?

<details>
<summary>✅ Solution (click to reveal)</summary>
*   $100\text{M} \times 12\text{ months} \times 5\text{ years} = 6\text{ Billion records}$
*   $6\text{B} \times 500\text{ bytes} = 3,000,000,000,000\text{ bytes} = 3\text{ Terabytes (TB)}$
</details>

---

## Next Steps

**➡️ [Back to Course Overview](./ch00-course-overview.md)**

---

*Chapter 29 of the Design & Architecture Guide | CodeShelf*
