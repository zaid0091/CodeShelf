---
title: Chapter 7 — Classes and OOP
description: TypeScript classes, access modifiers, readonly, static members, abstract classes, and implements.
order: 7
tags: [typescript, classes, oop, abstract, implements]
---

# Chapter 7: Classes and OOP

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

## Practice Exercise — Chapter 7

```text
Exercise 7.1: Payment model
  a) Abstract class PaymentMethod with abstract charge(amount: number): Promise<boolean>.
  b) Implement CreditCard and PayPal subclasses.
  c) Shared method formatAmount on base class.

Exercise 7.2: Access control
  a) Class Vault with private secret, public getHint(): string.
  b) Attempt external access — confirm compile error.

Exercise 7.3: implements
  a) Interface Validatable { validate(): string[] } (error messages).
  b) Class SignupForm implements Validatable with email/password fields.

Exercise 7.4: Generic repository
  a) Abstract CRUDRepository<T extends { id: string }>.
  b) Concrete MemoryRepository<T> with Map storage.
```

Next: [Chapter 8 — Type Narrowing](./ch08-type-narrowing.md).
