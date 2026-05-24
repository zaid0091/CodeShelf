---
title: OOP and Prototypes
description: Prototype chain, this binding, constructor functions, and ES6 classes
order: 12
tags: [javascript, oop, prototypes, this, classes, inheritance]
---

# Chapter 12: OOP and Prototypes

## 12.1 Objects and prototypes

> **Definition:** In JavaScript, objects inherit from other objects via the **prototype chain**. Every object has an internal link `[[Prototype]]` (exposed as `Object.getPrototypeOf(obj)`).

```javascript
const animal = {
  speak() {
    return "Some sound";
  },
};

const dog = Object.create(animal);
dog.name = "Rex";
dog.speak = function () {
  return `${this.name} barks`;
};

dog.speak(); // "Rex barks"
```

```text
dog → animal → Object.prototype → null
```

## 12.2 `__proto__` vs `prototype`

| | Meaning |
|---|---------|
| `obj.__proto__` | Object's prototype (prefer `Object.getPrototypeOf`) |
| `Fn.prototype` | Object used as `[[Prototype]]` for `new Fn()` instances |

```javascript
function Person(name) {
  this.name = name;
}

Person.prototype.greet = function () {
  return `Hi, I'm ${this.name}`;
};

const alice = new Person("Alice");
alice.greet(); // "Hi, I'm Alice"
```

## 12.3 Constructor functions vs classes

```javascript
// ES5 style
function Car(brand) {
  this.brand = brand;
}
Car.prototype.drive = function () {
  return `${this.brand} is moving`;
};

// ES6 class — same underlying prototype machinery
class Car {
  constructor(brand) {
    this.brand = brand;
  }
  drive() {
    return `${this.brand} is moving`;
  }
}
```

See also [Chapter 6: ES6+ Modern Features](./ch06-es6-modern-features.md).

## 12.4 Understanding `this`

> **Definition:** **`this`** is determined by how a function is **called**, not where it is defined (except arrows, which use lexical `this`).

| Call style | `this` value |
|------------|--------------|
| `obj.method()` | `obj` |
| `func()` | `undefined` (strict) or global |
| `new Func()` | new object |
| `func.call(ctx, ...)` | `ctx` |
| Arrow function | Enclosing scope's `this` |

```javascript
const user = {
  name: "Alice",
  greet() {
    console.log(this.name);
  },
};

user.greet(); // "Alice"

const fn = user.greet;
fn(); // undefined (strict) — lost context

fn.call(user); // "Alice"
```

### Binding methods

```javascript
const bound = user.greet.bind(user);
bound(); // "Alice"
```

## 12.5 Inheritance with prototypes

```javascript
function Animal(name) {
  this.name = name;
}

Animal.prototype.speak = function () {
  return `${this.name} makes a sound`;
};

function Dog(name, breed) {
  Animal.call(this, name);
  this.breed = breed;
}

Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

Dog.prototype.speak = function () {
  return `${this.name} barks`;
};
```

### Class syntax inheritance

```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }
  speak() {
    return `${this.name} makes a sound`;
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name);
    this.breed = breed;
  }
  speak() {
    return `${this.name} barks`;
  }
}
```

## 12.6 Property descriptors

```javascript
const obj = {};

Object.defineProperty(obj, "id", {
  value: 1,
  writable: false,
  enumerable: true,
  configurable: false,
});

Object.getOwnPropertyDescriptor(obj, "id");
```

| Descriptor | Effect |
|------------|--------|
| `writable` | Can change value |
| `enumerable` | Shows in `for...in` |
| `configurable` | Can delete or redefine |

## 12.7 Static vs instance members

```javascript
class MathHelper {
  static add(a, b) {
    return a + b;
  }
  instanceDouble(n) {
    return n * 2;
  }
}

MathHelper.add(2, 3); // 5
```

## 12.8 Composition vs inheritance

```javascript
// Composition — often preferred
function canFly(state) {
  return {
    fly() {
      return `${state.name} flies`;
    },
  };
}

function createBird(name) {
  const state = { name };
  return {
    name,
    ...canFly(state),
  };
}
```

| Inheritance | Composition |
|-------------|-------------|
| "is-a" relationship | "has-a" / mix behaviors |
| Deep hierarchies get fragile | Flexible, explicit |

## 12.9 `instanceof` and type checks

```javascript
const d = new Dog("Rex", "Lab");
d instanceof Dog;    // true
d instanceof Animal; // true

Array.isArray([]);
typeof d === "object";
```

## 12.10 Chapter summary

| Concept | Remember |
|---------|----------|
| Prototype chain | Lookup walks up until `null` |
| `this` | Depends on call site; bind when passing callbacks |
| Classes | Syntax sugar over prototypes |
| `super` | Call parent constructor/methods |
| Prefer composition | When inheritance depth grows |

## Exercises

### Exercise 12.1 — Prototype chain

Create `shape` with `area()` returning 0. Create `circle` inheriting from `shape` with `radius` and overridden `area()`.

### Exercise 12.2 — `this` quiz

Predict output:

```javascript
const o = {
  x: 10,
  getX() { return this.x; },
  getXArrow: () => this?.x,
};
console.log(o.getX());
const g = o.getX;
console.log(g());
```

### Exercise 12.3 — Class hierarchy

Implement `Employee` and `Manager extends Employee` with `bonus` percent added to `getSalary()`.

### Exercise 12.4 — Mixin

Create `withTimestamp(obj)` that adds `createdAt` and `touch()` method without class inheritance.

---

**Previous:** [Chapter 11: Browser APIs](./ch11-browser-apis.md) · **Next:** [Chapter 13: Best Practices](./ch13-best-practices.md)
