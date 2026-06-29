---
title: Event Sourcing & CQRS
description: Master Event Sourcing and Command Query Responsibility Segregation (CQRS). Learn how to replay state and design split read/write models.
order: 21
tags: [architecture, event-sourcing, cqrs, data-modeling, projections, reads-writes]
---

# Chapter 21: Event Sourcing & CQRS

> **Reconstruct application state. Implement Event Sourcing, structure Command Query Responsibility Segregation, and sync read projections.**

---

## Event Sourcing

In traditional databases, we store the *current state* of an object. If a user changes their name, the old name is overwritten and lost.

**Event Sourcing** stores the state of an application as a sequence of append-only, immutable events. The current state is reconstructed by replaying all historical events from the beginning of time.

### Traditional DB vs. Event Sourcing DB

| Action | Traditional DB (Current State) | Event Sourced DB (Event Log) |
|--------|--------------------------------|-----------------------------|
| Create Account | `id: 1, balance: $0` | `1. AccountCreated (id=1)` |
| Deposit $100 | `id: 1, balance: $100` | `2. MoneyDeposited (amount=$100)` |
| Withdraw $30 | `id: 1, balance: $70` | `3. MoneyWithdrawn (amount=$30)` |

*   *Benefits:* Complete audit log, time-travel debugging (restore state to any timestamp in history), easy analytics.
*   *Cons:* High CPU overhead to reconstruct state (mitigated using periodic **Snapshots**).

---

## CQRS (Command Query Responsibility Segregation)

In complex systems, the data structure optimized for writes (database transactions) is often inefficient for reads (complex dashboards and search queries).

**CQRS** splits the application into two separate paths:
1.  **Commands (Writes)**: Handle state-changing actions (create, update, delete). They validate business rules and write to the write database.
2.  **Queries (Reads)**: Handle read-only queries. They query a read-optimized database (projection store).

```text
               +-------------------+
               |      Client       |
               +-------------------+
                /                 \
       Command (Write)        Query (Read)
              /                     \
      +-------------+         +-------------+
      | Write Model |         | Read Model  |
      +-------------+         +-------------+
             |                       |
             v                       v
      [Write DB (SQL)] ---->  [Read DB (Elasticsearch)]
                     (Sync Projection)
```

---

## Syncing Read Stores: Projections

When a Command updates the Write DB, it emits an event. A background subscriber (projector) listens to this event and updates the Read DB (e.g., syncing relational SQL writes to Elasticsearch search indexes). This sync runs asynchronously, meaning reads are **Eventually Consistent**.

---

## Best Practices & Pitfalls

| Best Practice | Common Pitfall |
|---------------|----------------|
| Implement snapshots (saving the state at every 1,000th event) to prevent performance drops during event replays. | Using CQRS and Event Sourcing for simple CRUD applications, introducing excessive architectural complexity without benefit. |

---

## Interview Points

> **📌 Interview Point 1: Can you delete or update an event in Event Sourcing?**
> No. Events are strictly **immutable**. If a mistake is made, you must append a compensating event (e.g., if you mistakenly deposited $100, you append a "CorrectionWithdrawn" event of $100; you never edit the original deposit event).

---

## Exercises

### Exercise 1: Identify CQRS benefits ⭐
**Task:** Why is CQRS useful for search-heavy systems like e-commerce sites?

<details>
<summary>✅ Solution (click to reveal)</summary>
Because writes (orders, inventory updates) require transaction safety (SQL/ACID), whereas reads (searching, filtering products) require fast text-matching indexes (Elasticsearch). CQRS allows scaling and optimizing each layer independently.
</details>

---

## Next Chapter

Continue to [Saga Distributed Transactions](./ch22-saga-distributed-transactions.md) to explore multi-service transactions.
