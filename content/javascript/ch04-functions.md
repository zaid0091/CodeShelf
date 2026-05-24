---
title: Functions
description: Function declarations, expressions, arrow functions, scope, hoisting, and closures
order: 4
tags: [javascript, functions, arrow, scope, closure, hoisting]
---

# Chapter 4: Functions

## 4.1 What is a function?

> **Definition:** A **function** is a reusable block of code that performs a task. Functions can accept **parameters** (inputs) and **return** a value (output).

```javascript
function greet(name) {
  return `Hello, ${name}!`;
}

console.log(greet("Alice")); // "Hello, Alice!"
```

## 4.2 Function declarations

```javascript
function add(a, b) {
  return a + b;
}

console.log(add(2, 3)); // 5
```

### Hoisting

Function declarations are hoisted — you can call them before the line they appear on:

```javascript
sayHi(); // works

function sayHi() {
  console.log("Hi!");
}
```

## 4.3 Function expressions

```javascript
const multiply = function (a, b) {
  return a * b;
};

// multiply is not hoisted like declarations
// multiply(2, 3); // OK after assignment
```

### Named function expressions

```javascript
const factorial = function fact(n) {
  if (n <= 1) return 1;
  return n * fact(n - 1); // recursive via internal name
};
```

## 4.4 Arrow functions (ES6)

```javascript
const square = (x) => x * x;

const sum = (a, b) => {
  const total = a + b;
  return total;
};

const greet = () => "Hello!";

const makePerson = (name) => ({ name }); // returns object — parens required
```

| Feature | Regular function | Arrow function |
|---------|------------------|----------------|
| `this` binding | Own `this` | Lexical `this` from enclosing scope |
| `arguments` object | Yes | No |
| Constructor (`new`) | Yes | No |
| Hoisting | Declarations yes | No |

```javascript
const obj = {
  name: "Timer",
  start() {
    setTimeout(() => {
      console.log(this.name); // "Timer" — arrow inherits `this`
    }, 100);
  },
};
```

## 4.5 Parameters and arguments

### Default parameters

```javascript
function createUser(name, role = "user", active = true) {
  return { name, role, active };
}

createUser("Bob"); // role: "user", active: true
```

### Rest parameters

```javascript
function sum(...numbers) {
  return numbers.reduce((a, b) => a + b, 0);
}

sum(1, 2, 3, 4); // 10
```

### Destructuring parameters

```javascript
function printUser({ name, age }) {
  console.log(`${name} is ${age}`);
}

printUser({ name: "Alice", age: 30 });
```

## 4.6 Return values

```javascript
function divide(a, b) {
  if (b === 0) return null; // early return
  return a / b;
}

// Functions without return yield undefined
function noop() {}
console.log(noop()); // undefined
```

## 4.7 Scope

| Scope type | Created by | Accessible |
|------------|------------|------------|
| Global | Top-level `var`/`let`/`const` | Everywhere |
| Function | `function` body, `var` | Inside that function |
| Block | `let`/`const` in `{}` | Inside that block |

```javascript
const globalVar = "global";

function outer() {
  const outerVar = "outer";

  function inner() {
    const innerVar = "inner";
    console.log(globalVar, outerVar, innerVar); // all accessible
  }

  inner();
  // console.log(innerVar); // ReferenceError
}

outer();
```

## 4.8 Closures

> **Definition:** A **closure** is a function that remembers variables from its outer (enclosing) scope even after that outer function has finished executing.

```javascript
function createCounter() {
  let count = 0;

  return function () {
    count++;
    return count;
  };
}

const counter = createCounter();
console.log(counter()); // 1
console.log(counter()); // 2
console.log(counter()); // 3
```

### Practical uses

```javascript
// Private data
function createWallet(initial) {
  let balance = initial;
  return {
    deposit(amount) { balance += amount; },
    getBalance() { return balance; },
  };
}

// Factory functions
function multiplier(factor) {
  return (n) => n * factor;
}

const double = multiplier(2);
double(5); // 10
```

### Classic loop + closure fix

```javascript
// Problem: var in loop
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100); // 3, 3, 3
}

// Fix: let creates block scope per iteration
for (let j = 0; j < 3; j++) {
  setTimeout(() => console.log(j), 100); // 0, 1, 2
}
```

## 4.9 Higher-order functions

Functions that take or return other functions:

```javascript
function applyOperation(a, b, op) {
  return op(a, b);
}

applyOperation(5, 3, (x, y) => x + y); // 8

function withLogging(fn) {
  return function (...args) {
    console.log("Calling with", args);
    return fn(...args);
  };
}
```

## 4.10 Immediately Invoked Function Expression (IIFE)

```javascript
(function () {
  const secret = 42;
  console.log("IIFE runs once");
})();

// Modern alternative: modules (see ch06, ch10)
```

## 4.11 Pure functions and side effects

| Pure function | Impure function |
|---------------|-----------------|
| Same input → same output | Depends on external state |
| No side effects | Mutates globals, I/O, DOM |

```javascript
// Pure
function addTax(price, rate) {
  return price * (1 + rate);
}

// Impure
let total = 0;
function addToTotal(n) {
  total += n; // mutates outer state
}
```

## 4.12 Chapter summary

| Topic | Takeaway |
|-------|----------|
| Declaration vs expression | Hoisting differs |
| Arrows | Short syntax; lexical `this` |
| Closures | Enable private state and factories |
| Defaults / rest | Cleaner APIs |
| Scope | `let`/`const` block scope |

## Exercises

### Exercise 4.1 — Temperature converter

Write `celsiusToFahrenheit(c)` and `fahrenheitToCelsius(f)` as arrow functions.

### Exercise 4.2 — Closure counter

Create `createCounter(start)` that returns `{ increment, decrement, value }` without exposing `start` directly.

### Exercise 4.3 — Once

Implement `once(fn)` so `fn` runs only on the first call; later calls return the first result.

### Exercise 4.4 — Compose

Write `compose(f, g)` returning `(x) => f(g(x))`. Test with `compose(x => x + 1, x => x * 2)(3)` → 7.

---

**Previous:** [Chapter 3: Operators & Control Flow](./ch03-operators-and-control-flow.md) · **Next:** [Chapter 5: Arrays & Objects](./ch05-arrays-and-objects.md)
