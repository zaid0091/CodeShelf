## Scope

### Definition

**Scope** determines **where** a variable is accessible in your code. Think of
scope as a security rule: each variable has a region where it lives and can be
read or changed. Outside that region, it simply does not exist.

### Why It Exists

Without scope, every variable in every function would be accessible everywhere.
Variables would accidentally overwrite each other, making large programs
impossible to manage safely.

### The Three Types of Scope

#### 1. Global Scope

Variables declared **outside** all functions and blocks are in the global scope.
They are accessible everywhere in your program.

```js
const appName = "MyApp"; // global variable — accessible everywhere

function showName() {
  console.log(appName); // ✅ can access global variable
}

showName(); // "MyApp"
```

#### 2. Function Scope

Variables declared **inside a function** (with `var`, `let`, or `const`) are
only accessible inside that function. They are destroyed when the function ends.

```js
function makeSecret() {
  const secret = "password123"; // only lives inside makeSecret
  console.log(secret);          // ✅ accessible here
}

makeSecret();
console.log(secret); // ❌ ReferenceError: secret is not defined
```

#### 3. Block Scope

Variables declared with `let` or `const` inside a block `{}` (if statement,
loop, etc.) are only accessible within that block.

```js
if (true) {
  let blockVar = "I am block scoped";  // only exists inside this if block
  const blockConst = "Me too";
  var functionVar = "I escape blocks!"; // var ignores blocks
}

console.log(functionVar); // ✅ "I escape blocks!" (var leaks out)
console.log(blockVar);    // ❌ ReferenceError
console.log(blockConst);  // ❌ ReferenceError
```

### Scope Comparison Table

| Scope Type | Declared With | Where Accessible | Destroyed When |
|------------|--------------|-----------------|---------------|
| Global | `var` / `let` / `const` outside any block | Everywhere | Program ends |
| Function | `var` / `let` / `const` inside function | Inside function only | Function returns |
| Block | `let` / `const` inside `{}` | Inside `{}` only | Block exits |

### The Scope Chain (How JavaScript Looks Up Variables)

When JavaScript looks for a variable, it searches:

1. Current scope first
2. Then the parent scope
3. Then the parent's parent
4. All the way up to global scope
5. If not found anywhere → `ReferenceError`

```js
const globalMsg = "I am global";

function outer() {
  const outerMsg = "I am outer";

  function inner() {
    const innerMsg = "I am inner";
    console.log(innerMsg);  // ✅ found in own scope
    console.log(outerMsg);  // ✅ found in parent scope
    console.log(globalMsg); // ✅ found in global scope
  }

  inner();
  console.log(innerMsg);   // ❌ ReferenceError — inner's scope not visible to outer
}
```

---

## Hoisting

### Definition

**Hoisting** is JavaScript's behavior of moving **declarations** (not
assignments) to the top of their scope before code runs. It's as if JavaScript
pre-scans the file and registers all declarations first.

### Why It Exists

JavaScript was designed so that function declarations could be used before
they appear in the file. This made early programs easier to organize, with
"setup code" at the bottom and "use code" at the top.

### How It Works — Internally (Simple Terms)

Before your code runs, JavaScript goes through two phases:

1. **Creation Phase** — scans all declarations, registers them in memory
2. **Execution Phase** — runs code line by line

During phase 1, `function` declarations are fully stored. `var` variables are
registered with value `undefined`. `let` and `const` are registered but put
in a "temporal dead zone" — they exist but cannot be accessed yet.

### Hoisting Behavior Table

| Type | Hoisted? | Initial Value | Notes |
|------|----------|--------------|-------|
| `function` declaration | ✅ Yes | Full function | Can call before definition |
| `var` variable | ✅ Yes | `undefined` | Exists but has no value yet |
| `let` variable | ✅ Yes | Temporal Dead Zone | Cannot access before declaration |
| `const` variable | ✅ Yes | Temporal Dead Zone | Cannot access before declaration |
| Function expression (`var`) | Partially | `undefined` | Variable hoisted, not the function |

### Code Examples

```js
// ✅ Function declaration hoisting — works fine
console.log(greet("Alice")); // "Hello, Alice!" — works before definition!

function greet(name) {
  return "Hello, " + name;
}

// ---

// ❌ var hoisting — variable exists but has no value yet
console.log(score); // undefined (not an error, but not 100 either)
var score = 100;
console.log(score); // 100

// ---

// ❌ let/const in Temporal Dead Zone
console.log(points); // ReferenceError: Cannot access 'points' before initialization
let points = 50;

// ---

// ❌ Function expression hoisting — only the variable is hoisted
console.log(double(5)); // TypeError: double is not a function
var double = function(n) {
  return n * 2;
};
```

### Temporal Dead Zone (TDZ) — Simple Explanation

The TDZ is the period between when `let`/`const` is hoisted (JavaScript knows
it exists) and when it is actually assigned. During this time, touching the
variable throws an error — JavaScript is protecting you from using something
before it's ready.

```js
// TDZ starts here for 'color'
// ...any code here that uses 'color' will throw ReferenceError
const color = "blue"; // TDZ ends here — 'color' is now safe to use
console.log(color);   // "blue"
```

### Interview Points

- Only **declarations** are hoisted, not **initializations**
- `let` and `const` are hoisted but in the **Temporal Dead Zone**
- Function declarations are hoisted **completely** (definition + body)
- Function expressions are **not** fully hoisted — treat them like variables
- Always **declare variables at the top** of their scope to avoid confusion

---

## Closures

### Definition

A **closure** is a function that **remembers the variables from its parent
scope** even after the parent function has finished executing.

### Simple Explanation

Imagine you write a letter (inner function) while sitting in a room (outer
function). The room has certain things in it — a desk, a lamp. You take the
letter with you when you leave the room (outer function ends). Even though the
room is gone, the letter still **remembers** the desk and lamp because it was
written there. That memory is a closure.

### Why It Exists

JavaScript normally destroys a function's variables when it finishes. But if
an inner function is returned or passed somewhere, JavaScript is smart enough
to keep the outer variables **alive in memory** as long as the inner function
needs them. This enables powerful patterns like private state, factories, and
data encapsulation.

### Simple Example — Step by Step

```js
function makeCounter() {
  let count = 0;               // 'count' lives in makeCounter's scope

  function increment() {
    count++;                   // inner function accesses parent's 'count'
    console.log(count);
  }

  return increment;            // return the inner function
}

const counter = makeCounter();  // makeCounter runs and FINISHES
                                // but 'count' is kept alive by the closure!

counter(); // 1
counter(); // 2
counter(); // 3
```

**Step-by-step breakdown:**

| Step | What Happens |
|------|-------------|
| 1 | `makeCounter()` runs, creates `count = 0` in its scope |
| 2 | `increment` function is created, it forms a closure over `count` |
| 3 | `makeCounter()` returns `increment` and finishes |
| 4 | Normally `count` would be destroyed — but `increment` still references it |
| 5 | JavaScript keeps `count` alive in a "closure environment" |
| 6 | Every call to `counter()` reads and updates **the same** `count` |

### Memory Concept in Simple Terms

When JavaScript sees that an inner function uses a variable from an outer
function, it says: *"I cannot destroy this variable. Someone still needs it."*
It stores the variable in a special hidden object called the **closure
environment** or **lexical environment**. This environment stays in memory as
long as the inner function exists.

### Real-World Example 1: Counter with Reset

```js
function createCounter(startValue = 0) {
  let count = startValue;  // private variable

  return {
    increment: () => ++count,           // add 1
    decrement: () => --count,           // subtract 1
    reset: () => { count = startValue; return count; }, // reset to start
    getCount: () => count               // read current value
  };
}

const pageViews = createCounter(0);
pageViews.increment(); // 1
pageViews.increment(); // 2
pageViews.increment(); // 3
console.log(pageViews.getCount()); // 3
pageViews.reset();
console.log(pageViews.getCount()); // 0
```

### Real-World Example 2: Private Variables

Closures are the classic way to create **private variables** in JavaScript
(before ES2022 class private fields):

```js
function createBankAccount(initialBalance) {
  let balance = initialBalance; // 'balance' is PRIVATE — not accessible directly

  return {
    deposit(amount) {
      if (amount > 0) balance += amount;
      return balance;
    },
    withdraw(amount) {
      if (amount > balance) {
        console.log("Insufficient funds");
        return balance;
      }
      balance -= amount;
      return balance;
    },
    getBalance() {
      return balance; // only way to read balance from outside
    }
  };
}

const account = createBankAccount(1000);
console.log(account.balance);      // undefined — can't access directly!
console.log(account.getBalance()); // 1000
account.deposit(500);
console.log(account.getBalance()); // 1500
account.withdraw(200);
console.log(account.getBalance()); // 1300
```

### Real-World Example 3: Factory Functions

A **factory function** uses closures to create customized functions on the fly:

```js
function makeMultiplier(factor) {
  // 'factor' is captured by the returned function
  return function(number) {
    return number * factor; // uses 'factor' from outer scope
  };
}

const double = makeMultiplier(2);  // factor = 2 is remembered
const triple = makeMultiplier(3);  // factor = 3 is remembered
const times10 = makeMultiplier(10);

console.log(double(5));   // 10
console.log(triple(5));   // 15
console.log(times10(5));  // 50
```

### The Loop + Closure Problem: `var` vs `let`

This is one of the most famous JavaScript interview problems. It demonstrates
how closures interact with `var`.

```js
// ❌ WRONG — using var in a loop with setTimeout
for (var i = 0; i < 3; i++) {
  setTimeout(function() {
    console.log(i); // What prints?
  }, 1000);
}
// Prints: 3, 3, 3 — NOT 0, 1, 2!

// WHY? 'var' is function-scoped, not block-scoped.
// There is only ONE 'i' variable shared across ALL iterations.
// By the time the callbacks run (after 1 second), the loop is done,
// and 'i' is already 3. All three closures reference the SAME 'i'.
```

```js
// ✅ SOLUTION 1 — Use let (block-scoped, creates new 'i' each iteration)
for (let i = 0; i < 3; i++) {
  setTimeout(function() {
    console.log(i); // 0, 1, 2 ✅ each closure captures its own 'i'
  }, 1000);
}

// ✅ SOLUTION 2 — Use an IIFE to capture the value
for (var i = 0; i < 3; i++) {
  (function(capturedI) {   // immediately creates a new scope with its own copy
    setTimeout(function() {
      console.log(capturedI); // 0, 1, 2 ✅
    }, 1000);
  })(i); // pass current 'i' as argument immediately
}
```

### Why Closures Are Powerful

| Power | Explanation |
|-------|-------------|
| **Private state** | Variables hidden from outside — only accessible through controlled functions |
| **Factory functions** | Create families of related functions with shared config |
| **Memoization** | Cache expensive results in closed-over variables |
| **Event handlers** | Remember context when events fire later |
| **Module pattern** | Organize code into self-contained units (before ES6 modules) |
| **Currying** | Transform a multi-argument function into a chain of single-argument functions |

### Interview Points

- A closure is the combination of a **function + its lexical environment**
- Closures keep outer variables alive **as long as** the inner function exists
- Every function in JavaScript forms a closure (it always has access to its
  outer scope)
- Closures are the foundation of **the module pattern, currying, memoization**
- The `var` + loop problem is a classic closure gotcha — answer with `let`

---
