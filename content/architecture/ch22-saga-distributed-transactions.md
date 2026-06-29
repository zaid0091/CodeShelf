---
title: Saga Distributed Transactions
description: Learn how to manage distributed transactions across microservices using the Saga pattern. Compare Choreography vs. Orchestration.
order: 22
tags: [architecture, saga-pattern, distributed-transactions, orchestration, choreography, compensating-transaction]
---

# Chapter 22: Saga Distributed Transactions

> **Coordinate multi-service workflows. Implement the Saga pattern, compare Choreography vs. Orchestration, and write compensating transactions.**

---

## The Distributed Transaction Problem

In a monolithic application, maintaining transaction integrity is easy: we open a database transaction, modify multiple tables, and commit. If any step fails, the database rolls everything back.

In a microservices architecture, a single business transaction (e.g. buying a book) spans multiple independent services and databases:
1.  **Order Service**: Creates order.
2.  **Payment Service**: Charges credit card.
3.  **Inventory Service**: Reserves book.

Traditional solutions like **Two-Phase Commit (2PC)** require holding locks across all databases until the transaction completes. This blocks resources, limits scaling, and introduces single-point-of-failure risks.

---

## The Saga Pattern

A Saga is a sequence of local transactions. Each local transaction updates the database inside a single service and emits an event. If a local transaction fails, the Saga runs a series of **Compensating Transactions** that go backward, undoing the changes made by previous steps.

---

## Saga Implementation Patterns

### 1. Choreography (Decentralized)
There is no central coordinator. Services listen to events and execute their local logic independently:

```text
Order Service (creates order) -> emits OrderCreated 
  -> Payment Service (charges card) -> emits PaymentSuccessful 
    -> Inventory Service (reserves book) -> emits OrderComplete
```
*   *Pros:* Simple, no single coordinator bottleneck.
*   *Cons:* Hard to track workflow state; risk of circular dependency loops.

### 2. Orchestration (Centralized)
A central service (the Orchestrator) coordinates the workflow. It directs individual services on which actions to perform:

```text
Order Service (Orchestrator) 
  -- 1. Charge Card --> Payment Service
  <-- 2. Success ------
  -- 3. Reserve Book -> Inventory Service
```
*   *Pros:* Centralized state tracking; easy to design complex workflows.
*   *Cons:* Single point of failure; orchestrator can become bloated with business logic.

---

## Compensating Transactions

A compensating transaction is an action that explicitly reverses a previous action (e.g., if a payment was charged but inventory allocation fails, the compensating transaction executes a credit refund).

| Action | Compensating Transaction (Undo) |
|--------|---------------------------------|
| Charge Credit Card | Issue Refund |
| Reserve Inventory Item | Release Inventory Item |
| Create Pending Order | Cancel Order |

---

## Best Practices & Pitfalls

| Best Practice | Common Pitfall |
|---------------|----------------|
| Make all compensating transactions **Idempotent** (safe to run multiple times during retries without duplicating refunds or releases). | Assuming a Saga guarantees ACID isolation. Sagas are eventually consistent, meaning other users can see intermediate, half-finished transaction states. |

---

## Interview Points

> **📌 Interview Point 1: What is the difference between rolling back a SQL transaction and running a compensating transaction?**
> A SQL rollback deletes database changes from the transaction log before they are committed (it is a physical restore). A compensating transaction is a *new, separate transaction* that writes new data to reverse the semantic state of the previous commit (e.g., writing a "+100 refund" row to undo a "-100 payment" row).

---

## Exercises

### Exercise 1: Map the failure ⭐
**Task:** If a Saga fails during Step 3 (Inventory Allocation), in what order are the compensating transactions executed?

<details>
<summary>✅ Solution (click to reveal)</summary>
They are executed in **reverse chronological order** (Step 2 Compensating Transaction, then Step 1 Compensating Transaction) to undo actions step-by-step.
</details>

---

## Next Chapter

Continue to [Outbox Pattern & Idempotency](./ch23-outbox-pattern-idempotency.md) to explore event reliability.
