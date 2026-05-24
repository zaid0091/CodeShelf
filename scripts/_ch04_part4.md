## Higher-Order Functions

### Definition

A **higher-order function** is a function that either:

1. **Takes another function as an argument**, OR
2. **Returns a function as its result**

(or both)

### Why It Exists

Higher-order functions are the backbone of **functional programming** in
JavaScript. They allow you to abstract behavior — not just data — and write
code that is shorter, more expressive, and more reusable.

Instead of writing the same loop structure over and over, you tell a
higher-order function **what to do** (pass a function), and it handles the
**how** (the loop, the iteration).

### Example 1: Function Takes a Function (Callback Pattern)

```js
// 'operate' is a higher-order function — it takes a function as argument
function operate(a, b, operation) {
  return operation(a, b);  // call whatever function was passed in
}

const add = (x, y) => x + y;
const multiply = (x, y) => x * y;
const power = (x, y) => x ** y;

console.log(operate(5, 3, add));      // 8
console.log(operate(5, 3, multiply)); // 15
console.log(operate(5, 3, power));    // 125
```

### Example 2: Function Returns a Function

```js
// 'withLogging' wraps any function to add logging behavior
function withLogging(fn) {
  return function(...args) {           // return a new function
    console.log("Calling with:", args); // log the inputs
    const result = fn(...args);          // call the original function
    console.log("Result:", result);      // log the output
    return result;
  };
}

const add = (a, b) => a + b;
const loggedAdd = withLogging(add);    // create a logged version of add

loggedAdd(3, 4);
// Calling with: [3, 4]
// Result: 7
```

### Built-in Higher-Order Functions

JavaScript arrays have powerful built-in higher-order functions:

#### `.map()` — Transform Every Element

```js
const names = ["alice", "bob", "carol"];

// Regular loop approach
const upperNames = [];
for (const name of names) {
  upperNames.push(name.toUpperCase());
}

// HOF approach — shorter, cleaner, no mutation
const upperNames = names.map(name => name.toUpperCase());
console.log(upperNames); // ["ALICE", "BOB", "CAROL"]
```

#### `.filter()` — Keep Matching Elements

```js
const scores = [45, 82, 60, 95, 38, 71];

const passing = scores.filter(score => score >= 60);
console.log(passing); // [82, 60, 95, 71]
```

#### `.reduce()` — Combine All Elements Into One Value

```js
const cart = [
  { item: "Book", price: 15 },
  { item: "Pen", price: 3 },
  { item: "Bag", price: 45 }
];

// accumulator starts at 0, adds each item's price
const total = cart.reduce((accumulator, current) => {
  return accumulator + current.price;
}, 0); // 0 is the starting value

console.log(total); // 63
```

#### `.forEach()` — Run Something for Each Element

```js
const tasks = ["Write tests", "Fix bug", "Deploy app"];
tasks.forEach((task, index) => {
  console.log(`${index + 1}. ${task}`);
});
// 1. Write tests
// 2. Fix bug
// 3. Deploy app
```

### Real-World Example: Data Pipeline

```js
const employees = [
  { name: "Alice", department: "Engineering", salary: 90000 },
  { name: "Bob", department: "Marketing", salary: 65000 },
  { name: "Carol", department: "Engineering", salary: 95000 },
  { name: "Dave", department: "Marketing", salary: 70000 },
  { name: "Eve", department: "Engineering", salary: 85000 }
];

// Find the average salary of Engineering department employees
const avgEngineerSalary = employees
  .filter(emp => emp.department === "Engineering")  // keep engineers only
  .map(emp => emp.salary)                           // extract salaries
  .reduce((sum, salary, _, arr) =>
    sum + salary / arr.length, 0);                  // compute average

console.log(avgEngineerSalary); // 90000
```

### Interview Points

- `.map()`, `.filter()`, `.reduce()` are the most important built-in HOFs
- HOFs enable **function composition** (chaining transforms)
- They make code **declarative** (describe what you want) vs **imperative**
  (describe how to do it step by step)
- HOFs are key to **React** (event handlers, array rendering) and **Node.js**

---

## IIFE (Immediately Invoked Function Expression)

### Definition

An **IIFE** is a function that is **defined and called at the exact same time**,
in one expression. It runs once and immediately.

### Why It Exists

IIFEs were invented to create a **private scope** to prevent variable pollution
of the global scope — especially before ES6 modules existed. They are still
used for initialization code, plugin patterns, and avoiding naming conflicts.

### Syntax

```js
(function() {
  // code here
})();

// Arrow function IIFE
(() => {
  // code here
})();
```

> The outer `()` around the function turns it into an **expression** (not a
> declaration). The final `()` **calls** it immediately.

### Simple Example

```js
(function() {
  const message = "I run immediately!"; // this variable stays private
  console.log(message);                  // "I run immediately!"
})();

console.log(message); // ❌ ReferenceError — message doesn't leak out
```

### Real-World Example: App Initialization

```js
const app = (function() {
  // Private setup — these variables are not accessible from outside
  const VERSION = "1.0.0";
  let isInitialized = false;

  function init() {
    isInitialized = true;
    console.log(`App v${VERSION} initialized`);
  }

  // Only expose what is needed
  return {
    start: init,
    version: VERSION
  };
})(); // runs immediately and returns the object

app.start();           // "App v1.0.0 initialized"
console.log(app.version); // "1.0.0"
console.log(isInitialized); // ❌ ReferenceError — private!
```

### Interview Points

- IIFEs create a **private scope** that does not pollute the global scope
- They were the foundation of the **module pattern** before ES6 modules
- They are still used in some **library bundles** and **configuration scripts**
- The `(function(){})()` pattern is a classic JavaScript interview question

---

## Pure vs Impure Functions

### Definition

- A **pure function** always returns the **same output for the same input**
  and has **no side effects** (it doesn't touch anything outside itself)
- An **impure function** either depends on external state OR changes something
  outside itself

### Why It Exists

Pure functions are the gold standard of functional programming because they
are **predictable, testable, and safe**. Given the same input, they always
do the same thing — no surprises, no hidden consequences.

### Pure Function

```js
// ✅ Pure: same input ALWAYS gives same output, nothing outside is changed
function add(a, b) {
  return a + b; // depends only on its own parameters
}

console.log(add(2, 3)); // always 5
console.log(add(2, 3)); // always 5 — no matter what
```

### Impure Function — External Dependency

```js
// ❌ Impure: depends on external variable 'tax'
let tax = 0.1;

function calculatePrice(price) {
  return price + price * tax; // depends on external 'tax'
}

console.log(calculatePrice(100)); // 110 (when tax = 0.1)
tax = 0.2;
console.log(calculatePrice(100)); // 120 — same input, different output!
```

### Impure Function — Side Effect

```js
// ❌ Impure: modifies an external array (side effect)
const log = [];

function recordEvent(event) {
  log.push(event); // changes something outside the function!
}

// ✅ Pure alternative: return a new array instead
function recordEvent(log, event) {
  return [...log, event]; // creates a NEW array, doesn't change the original
}
```

### Comparison Table

| Aspect | Pure Function | Impure Function |
|--------|--------------|----------------|
| Same input → same output? | ✅ Always | ❌ Not guaranteed |
| Changes external state? | ❌ Never | ✅ May change things |
| Easy to test? | ✅ Very easy | ❌ Requires mocking |
| Predictable? | ✅ Completely | ❌ Depends on context |
| Examples | `Math.max`, `add`, `filter` | `console.log`, `Math.random` |

---
