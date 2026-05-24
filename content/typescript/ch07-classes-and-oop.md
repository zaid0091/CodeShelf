---
title: Chapter 7 — Classes and OOP
description: Classes, access modifiers, readonly, static, abstract classes, and implements.
order: 7
tags: [typescript, classes, oop, abstract, implements]
---


# Chapter 7: Classes and OOP

> **TypeScript adds types to JavaScript classes — modifiers, abstract members, and interfaces implemented by classes.**
> Take your time with each section. TypeScript rewards patience — read compiler errors carefully and experiment in a small project as you go.

---


## Table of Contents

1. [Class Basics](#class-basics)
2. [Parameter Properties](#parameter-properties)
3. [Access Modifiers](#access-modifiers)
4. [readonly](#readonly)
5. [static Members](#static-members)
6. [Inheritance](#inheritance)
7. [override](#override)
8. [Abstract Classes](#abstract-classes)
9. [implements](#implements)
10. [Getters and Setters](#getters-and-setters)
11. [Best Practices](#best-practices)
12. [Interview Points](#interview-points)
13. [Exercises](#exercises)
14. [Chapter Summary](#chapter-summary)

---

## 7.1 Classes in TypeScript

TypeScript classes are JavaScript classes with type annotations and visibility modifiers. They compile to JS constructor/prototype patterns (or native class syntax).

```typescript
class User {
  id: string;
  name: string;

  constructor(id: string, name: string) {
    this.id = id;
    this.name = name;
  }

  greet(): string {
    return `Hello, ${this.name}`;
  }
}

const u = new User("1", "Ada");
console.log(u.greet());
```

> **Definition:** A **class** encapsulates state (fields) and behavior (methods), with a constructor for initialization and optional inheritance.

## 7.2 Parameter properties

Shorthand — declare and assign in constructor:

```typescript
class Product {
  constructor(
    public readonly id: string,
    public name: string,
    private price: number
  ) {}

  getPrice(taxRate: number): number {
    return this.price * (1 + taxRate);
  }
}
```

Equivalent to manual assignment but concise.

## 7.3 Access modifiers

| Modifier | Accessible from |
|----------|-----------------|
| `public` | Everywhere (default) |
| `protected` | Class + subclasses |
| `private` | Declaring class only |
| `#field` | True private (JS private fields, ES2022) |

```typescript
class BankAccount {
  private balance = 0;

  deposit(amount: number): void {
    if (amount > 0) this.balance += amount;
  }

  getBalance(): number {
    return this.balance;
  }
}

// account.balance; // ❌ private
```

### private vs #private

```typescript
class Example {
  private legacyPrivate = 1;
  #modernPrivate = 2;
}
```

`#` fields are enforced at runtime; `private` is compile-time only.

## 7.4 readonly fields

```typescript
class Session {
  readonly token: string;
  readonly createdAt: Date;

  constructor(token: string) {
    this.token = token;
    this.createdAt = new Date();
  }
}
```

Must be assigned in constructor or at declaration.

## 7.5 Static members

Belong to the class, not instances:

```typescript
class MathUtils {
  static PI = 3.14159;

  static clamp(value: number, min: number, max: number): number {
    return Math.min(max, Math.max(min, value));
  }
}

MathUtils.clamp(15, 0, 10);
```

Use for factories, constants, and utility namespaces.

## 7.6 Inheritance

```typescript
class Animal {
  constructor(public name: string) {}

  move(distance: number): void {
    console.log(`${this.name} moved ${distance}m`);
  }
}

class Dog extends Animal {
  constructor(name: string, public breed: string) {
    super(name);
  }

  bark(): void {
    console.log("Woof!");
  }
}

const dog = new Dog("Rex", "Lab");
dog.move(5);
dog.bark();
```

`super()` must be called before using `this` in subclass constructor.

## 7.7 Method overriding

```typescript
class Shape {
  area(): number {
    return 0;
  }
}

class Circle extends Shape {
  constructor(public radius: number) {
    super();
  }

  override area(): number {
    return Math.PI * this.radius ** 2;
  }
}
```

`override` keyword (TS 4.3+) catches typos when parent has no matching method.

## 7.8 Abstract classes

> **Definition:** An **abstract class** cannot be instantiated directly. It may include abstract members (no implementation) that subclasses must implement.

```typescript
abstract class Repository<T> {
  abstract findById(id: string): Promise<T | null>;
  abstract save(entity: T): Promise<void>;

  async exists(id: string): Promise<boolean> {
    const item = await this.findById(id);
    return item !== null;
  }
}

class UserRepository extends Repository<User> {
  async findById(id: string): Promise<User | null> {
    return null; // DB logic
  }

  async save(entity: User): Promise<void> {
    // persist
  }
}
```

Use abstract classes when sharing implementation + enforcing a contract.

## 7.9 implements — interface compliance

Classes can implement one or more interfaces:

```typescript
interface Serializable {
  serialize(): string;
}

interface Timestamped {
  updatedAt: Date;
}

class Document implements Serializable, Timestamped {
  updatedAt = new Date();

  constructor(public title: string, public body: string) {}

  serialize(): string {
    return JSON.stringify({ title: this.title, body: this.body });
  }
}
```

`implements` checks shape at compile time — no runtime effect.

## 7.10 Classes vs interfaces for objects

| Use class when | Use interface when |
|----------------|-------------------|
| Need instances + methods | Describing data shape only |
| Encapsulation with private state | API contracts, DTOs |
| Inheritance with shared code | Structural typing across libs |

Many TS codebases prefer **functions + interfaces** over classes except for domain models and frameworks (Angular, NestJS).

## 7.11 Generic classes

```typescript
class Queue<T> {
  private items: T[] = [];

  enqueue(item: T): void {
    this.items.push(item);
  }

  dequeue(): T | undefined {
    return this.items.shift();
  }
}

const q = new Queue<number>();
q.enqueue(1);
```

See [Chapter 5](./ch05-generics.md).

## 7.12 Getters and setters

```typescript
class CelsiusTemperature {
  private _celsius = 0;

  get celsius(): number {
    return this._celsius;
  }

  set celsius(value: number) {
    if (value < -273.15) throw new Error("Below absolute zero");
    this._celsius = value;
  }

  get fahrenheit(): number {
    return this._celsius * 1.8 + 32;
  }
}
```

## 7.13 this types and arrow methods

```typescript
class ClickCounter {
  count = 0;

  // Arrow preserves lexical this for callbacks
  handleClick = (): void => {
    this.count += 1;
  };
}
```

Regular methods passed as callbacks may lose `this` — bind in constructor or use arrows.

## 7.14 Common pitfalls

| Pitfall | Fix |
|---------|-----|
| Forgetting `super()` | Call before accessing `this` in subclass |
| Public by default exposing internals | Mark fields `private` or `#` |
| God classes | Split responsibilities; favor composition |
| Class for every DTO | Use `type`/`interface` for plain data |
| Deep inheritance trees | Prefer interfaces + functions |

> **Key takeaway:** TypeScript classes add visibility, abstract members, and interface implementation to JavaScript classes. Use them when encapsulation and shared behavior matter; use interfaces for shape-only contracts.
<!-- codeshelf:generated-appendix -->

---

## Class design — when to use classes

Use classes when you have **state + behavior** that belong together:

```typescript
class ShoppingCart {
  private items: { sku: string; qty: number }[] = [];

  add(sku: string, qty: number) {
    this.items.push({ sku, qty });
  }

  totalItems(): number {
    return this.items.reduce((sum, i) => sum + i.qty, 0);
  }
}
```

For plain data shapes, prefer `interface` + functions.

---

## implements vs extends

- **`extends`** — inherit implementation from a parent class.
- **`implements`** — promise your class matches an interface shape.

```typescript
interface Serializable { toJSON(): object }

class User implements Serializable {
  constructor(public name: string) {}
  toJSON() { return { name: this.name }; }
}
```

---

## Access modifiers — visibility


| Modifier | Class | Subclass | External |
|----------|-------|----------|----------|
| public | yes | yes | yes |
| protected | yes | yes | no |
| private | yes | no | no |
| # private field | yes | no | no |


---

## Abstract class pattern


```typescript
abstract class Repository<T extends { id: string }> {
  abstract findById(id: string): Promise<T | null>;
  abstract save(entity: T): Promise<void>;
}
```


---

## Parameter properties


```typescript
class Point {
  constructor(
    public readonly x: number,
    public readonly y: number,
  ) {}
}
```


---

## implements vs extends


```typescript
interface Serializable {
  toJSON(): object;
}

class User implements Serializable {
  constructor(public name: string) {}
  toJSON() { return { name: this.name }; }
}
```


---

## override keyword


```typescript
class Animal {
  speak(): string { return "..."; }
}
class Dog extends Animal {
  override speak(): string { return "woof"; }
}
```


---

## Static factory methods


```typescript
class User {
  private constructor(public id: string, public name: string) {}
  static create(name: string): User {
    return new User(crypto.randomUUID(), name);
  }
}
```


---

## Protected members


Use `protected` when subclasses need access but external code should not.


---

## Class vs interface


| Use | Choice |
|-----|--------|
| Data only | `interface` |
| Behavior + state | `class` |
| Contract for class | `implements` |


---

## Definition — Encapsulation

> **Definition:** **Encapsulation** — Hiding internal state so outside code cannot put the object in an invalid state.


---

## Class diagram — simple hierarchy


```text
        Animal
           │
           ├── Dog
           └── Cat
```

```typescript
abstract class Animal {
  abstract speak(): string;
}
class Dog extends Animal {
  override speak() { return "woof"; }
}
```


---

## When not to use classes


Prefer functions + interfaces when you only transform data. Use classes when you manage lifecycle and invariants (connections, caches, game entities).


---

## Interface for test doubles


```typescript
interface Clock { now(): Date }
class SystemClock implements Clock { now() { return new Date(); } }
class FakeClock implements Clock { constructor(private t: Date) {} now() { return this.t; } }
```


---

## Review Q1

**Q:** `private` vs `#private`? **A:** `private` is compile-time only; `#` is true runtime privacy.

---

## Review Q2

**Q:** When use `abstract`? **A:** When subclasses must implement specific methods but you share base logic.

---

## Scenario — domain model


```typescript
abstract class Entity {
  constructor(public readonly id: string) {}
  abstract validate(): string[];
}

class Order extends Entity {
  constructor(
    id: string,
    public readonly totalCents: number,
    public readonly lines: { sku: string; qty: number }[],
  ) {
    super(id);
  }

  validate() {
    const errors: string[] = [];
    if (this.totalCents < 0) errors.push("Negative total");
    if (this.lines.length === 0) errors.push("Empty order");
    return errors;
  }
}
```


---

## Best Practices

- ✅ Prefer composition over deep inheritance trees.
- ✅ Use `implements` to document contracts; classes for behavior with state.

---

## Common Mistakes

Watch for these patterns — they cost hours in real projects.

### Mistake 1: public everything

All fields public by default habit

Mark internal state `private`.

---

### Mistake 2: Arrow vs method in React

Wrong `this` in class components

Use arrow fields or bind in constructor.

---

## Interview Points

> **📌 Interview Point 1: abstract vs interface?**

abstract can have implementation; interface is shape only.

---

> **📌 Interview Point 2: private vs #?**

private is compile-time; # is runtime private field.

---

## Exercises

Practice with `npx tsc --noEmit` after each exercise.

### Exercise 7.1: User class ⭐

**Task:** Class with constructor and method.

<details><summary>💡 Hint</summary>

Basics.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
class User {
  constructor(public name: string) {}
  greet() { return `Hi, ${this.name}`; }
}
```

</details>

---

### Exercise 7.2: Abstract repo ⭐⭐

**Task:** Abstract Repository<T> with save/find.

<details><summary>💡 Hint</summary>

Abstract pattern.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
abstract class Repository<T extends { id: string }> {
  abstract findById(id: string): Promise<T | null>;
  abstract save(entity: T): Promise<void>;
}
```

</details>

---

### Exercise 7.3: implements ⭐⭐⭐

**Task:** Logger implements interface.

<details><summary>💡 Hint</summary>

Contract.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
interface Logger { log(msg: string): void }
class ConsoleLogger implements Logger {
  log(msg: string) { console.log(msg); }
}
```

</details>

---

### Exercise 7.4: override ⭐⭐

**Task:** Subclass override with keyword.

<details><summary>💡 Hint</summary>

TS 4.3+.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
class Animal { speak() { return "..."; } }
class Dog extends Animal {
  override speak() { return "woof"; }
}
```

</details>

---

### Exercise 7.5: static util ⭐⭐⭐

**Task:** MathUtils static methods.

<details><summary>💡 Hint</summary>

static keyword.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
class MathUtils {
  static clamp(n: number, min: number, max: number) {
    return Math.min(max, Math.max(min, n));
  }
}
```

</details>

---

### Exercise 7.6: Generic Queue ⭐⭐

**Task:** Queue<T> class.

<details><summary>💡 Hint</summary>

Generic class.

</details>

<details><summary>✅ Solution (click to reveal)</summary>

```typescript
class Queue<T> {
  private items: T[] = [];
  enqueue(item: T) { this.items.push(item); }
  dequeue(): T | undefined { return this.items.shift(); }
}
```

</details>

---

## Chapter Summary

You covered a lot in this chapter. Here is a concise recap:

- Classes type OOP in TS; modifiers control visibility.
- Abstract classes template shared behavior.

---

---

## Navigation

**⬅️ [Previous: Utility Types](./ch06-utility-types.md)**  
**➡️ [Next: Type Narrowing](./ch08-type-narrowing.md)**

---
## Quick glossary (review)

- **TypeScript** — Typed superset of JavaScript that compiles to JS.
- **Inference** — Compiler deduces types without explicit annotations.
- **Union** — Value may be one of several types: `A | B`.
- **Narrowing** — Refining a union to a specific type in a branch.
- **Generic** — Type parameter for reusable APIs.
- **Interface** — Named object shape contract.
- **Utility type** — Built-in type transformer like `Partial`.
- **Strict mode** — Bundle of safer compiler flags in tsconfig.
- **Type erasure** — Types removed in emitted JavaScript.
- **Declaration file** — `.d.ts` describing types for JS modules.
- **TypeScript** — Typed superset of JavaScript that compiles to JS.
- **Inference** — Compiler deduces types without explicit annotations.
- **Union** — Value may be one of several types: `A | B`.
- **Narrowing** — Refining a union to a specific type in a branch.
- **Generic** — Type parameter for reusable APIs.
- **Interface** — Named object shape contract.
- **Utility type** — Built-in type transformer like `Partial`.
- **Strict mode** — Bundle of safer compiler flags in tsconfig.
- **Type erasure** — Types removed in emitted JavaScript.
- **Declaration file** — `.d.ts` describing types for JS modules.
- **TypeScript** — Typed superset of JavaScript that compiles to JS.
- **Inference** — Compiler deduces types without explicit annotations.
- **Union** — Value may be one of several types: `A | B`.

*Last updated: 2025 | TypeScript course — CodeShelf*

*Found an error or have a suggestion? [Open an issue on GitHub](https://github.com/zaid0091/CodeShelf/issues)*
