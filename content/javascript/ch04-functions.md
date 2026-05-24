---
title: Functions
description: Function declarations, expressions, arrow functions, scope, hoisting, and closures
order: 4
tags: [javascript, functions, arrow, scope, closure, hoisting]
---

# Chapter 4: Functions in JavaScript

> **"Functions are the building blocks of readable, maintainable, and reusable code."**

---

## Table of Contents

1. [What is a Function?](#what-is-a-function)
2. [Function Declarations](#function-declarations)
3. [Function Expressions](#function-expressions)
4. [Arrow Functions](#arrow-functions)
5. [Parameters and Arguments](#parameters-and-arguments)
   - [Default Parameters](#default-parameters)
   - [Rest Parameters](#rest-parameters)
   - [Destructuring Parameters](#destructuring-parameters)
6. [Return Values](#return-values)
7. [Scope](#scope)
8. [Hoisting](#hoisting)
9. [Closures](#closures)
10. [Higher-Order Functions](#higher-order-functions)
11. [IIFE](#iife-immediately-invoked-function-expression)
12. [Pure vs Impure Functions](#pure-vs-impure-functions)
13. [Real-World Functional Patterns](#real-world-functional-patterns)
14. [Common Mistakes](#common-mistakes-developers-make)
15. [Best Practices](#best-practices)
16. [Interview Questions](#interview-questions)
17. [Debugging Tips](#debugging-tips)
18. [Exercises](#exercises)

---

## What is a Function?

### Definition

A **function** is a named, reusable block of code that performs a specific task.
Think of it like a recipe. You write the recipe once (define the function), and
you can cook the dish as many times as you want (call the function) without
rewriting the recipe from scratch every time.

### Why Functions Exist

Imagine you are building a website, and on every page you need to show a
greeting message to the user. Without functions, you would write the same
greeting code on every single page — maybe 50 times. If the greeting changes,
you must update all 50 places. That is error-prone and exhausting.

With a function, you write the greeting logic **once**, give it a name, and
**call it** wherever you need it. This is called the **DRY principle** —
*Don't Repeat Yourself*.

Functions also help you:

- **Break complex problems into smaller pieces** (divide and conquer)
- **Test one piece at a time** instead of the whole program
- **Name logic clearly** so code reads like English
- **Share and reuse logic** across files and teams

### How JavaScript Runs a Function (Internally — Simple Explanation)

When JavaScript sees a function **call**, it:

1. Pauses the current code
2. Creates a new **execution context** (a private workspace) for that function
3. Runs the code inside the function
4. Returns the result (if any) back to where it was called
5. Destroys the workspace and resumes the original code

> 💡 **Execution Context** is simply JavaScript's way of saying:
> *"I am now working inside this function. It has its own variables, its own
> scope, and its own rules."* Every function call creates one.

---

## Function Declarations

### Definition

A **function declaration** is the classic, traditional way to define a function
in JavaScript. You use the `function` keyword, give the function a name, and
write the body (the logic) inside curly braces `{}`.

### Why It Exists

Function declarations are the foundation of JavaScript. They give a function a
permanent name in the current scope and are available throughout the entire
file, even before they are written, thanks to **hoisting** (covered later).

### Syntax

```js
function functionName(parameter1, parameter2) {
  // code to run
  return result;
}
```

### Simple Example

```js
// Define the function once
function greet(name) {
  return "Hello, " + name + "!"; // combine greeting with name
}

// Call (use) the function many times
console.log(greet("Alice")); // "Hello, Alice!"
console.log(greet("Bob"));   // "Hello, Bob!"
console.log(greet("Carol")); // "Hello, Carol!"
```

### Real-World Example

```js
// A function to calculate the total price with tax
function calculateTotal(price, taxRate) {
  const tax = price * taxRate;       // calculate the tax amount
  const total = price + tax;         // add tax to the original price
  return total;                      // send the result back
}

const finalPrice = calculateTotal(100, 0.08); // 100 dollars, 8% tax
console.log("Total: $" + finalPrice);         // "Total: $108"
```

### Step-by-Step Breakdown

| Step | What Happens |
|------|-------------|
| 1 | JavaScript reads `function calculateTotal(...)` and stores it in memory |
| 2 | You call `calculateTotal(100, 0.08)` |
| 3 | JavaScript creates a private workspace with `price = 100` and `taxRate = 0.08` |
| 4 | The code inside runs line by line |
| 5 | `return total` sends the value `108` back |
| 6 | The workspace is destroyed; `finalPrice` holds `108` |

### Common Mistakes

```js
// ❌ WRONG: Forgetting to return a value
function add(a, b) {
  a + b; // This calculates but throws it away!
}
console.log(add(2, 3)); // undefined

// ✅ CORRECT
function add(a, b) {
  return a + b; // This sends the value back
}
console.log(add(2, 3)); // 5
```

### Interview Points

- Function declarations are **hoisted** (can be called before they are written)
- They always have a **name**, which makes stack traces easier to debug
- They create their own **function scope**

---

## Function Expressions

### Definition

A **function expression** is when you create a function and assign it to a
**variable**, just like assigning a number or string to a variable. The function
itself has no permanent name — it lives inside the variable.

### Why It Exists

Sometimes you only need a function in one specific place. Or you want to decide
*later* which function a variable should hold. Function expressions let you
treat functions as **values** — just like numbers or strings. This opens the
door to passing functions around your code, which is a powerful idea.

### Syntax

```js
const functionName = function(parameter1, parameter2) {
  // code to run
  return result;
};
```

> ⚠️ **Note:** Notice the semicolon `;` at the end. Because this is a variable
> assignment statement, it ends with a semicolon, just like `const x = 5;`.

### Simple Example

```js
// Assign a function to a variable called "multiply"
const multiply = function(a, b) {
  return a * b; // return the product
};

console.log(multiply(3, 4)); // 12
console.log(multiply(7, 2)); // 14
```

### Named Function Expression

You can optionally give the function inside a name. This is useful for
recursion and better error messages in the browser.

```js
const factorial = function calculateFactorial(n) {
  if (n <= 1) return 1;                        // base case: stop at 1
  return n * calculateFactorial(n - 1);        // call itself by its inner name
};

console.log(factorial(5)); // 120
// calculateFactorial(5) would throw ReferenceError — inner name not accessible outside
```

### Real-World Example

```js
// Choose a different formatter based on user preference
let formatCurrency;

if (userLocale === "en-US") {
  formatCurrency = function(amount) {
    return "$" + amount.toFixed(2); // format as US dollars
  };
} else {
  formatCurrency = function(amount) {
    return "€" + amount.toFixed(2); // format as Euros
  };
}

console.log(formatCurrency(19.9)); // "$19.90" or "€19.90"
```

### Function Declaration vs Function Expression

| Feature | Function Declaration | Function Expression |
|---------|---------------------|---------------------|
| Syntax | `function name() {}` | `const name = function() {}` |
| Hoisted? | ✅ Yes (fully) | ❌ No |
| Has a name? | Always | Optional |
| Use case | General reusable functions | Conditional, callbacks, closures |
| Semicolon at end? | No | Yes (it's a statement) |

### Common Mistakes

```js
// ❌ WRONG: Calling a function expression before it is defined
console.log(double(5)); // ReferenceError: Cannot access 'double' before initialization

const double = function(n) {
  return n * 2;
};

// ✅ CORRECT: Call it after
const triple = function(n) {
  return n * 3;
};
console.log(triple(5)); // 15
```

### Interview Points

- Function expressions are **not hoisted** — the variable is hoisted but
  stays `undefined` until the assignment line
- They are perfect for **callbacks** and **conditional definitions**
- They make it obvious that functions are **first-class values** in JavaScript

---

## Arrow Functions

### Definition

An **arrow function** is a shorter, modern way to write a function, introduced
in **ES6 (2015)**. Instead of the `function` keyword, you use a fat arrow `=>`.

### Why It Exists

Arrow functions solve two problems:

1. **Shorter syntax** — less code to write for small functions
2. **`this` keyword behavior** — arrow functions do **not** have their own
   `this`. They inherit `this` from the surrounding code, which fixes a very
   common bug in object methods and callbacks (explained below).

### Syntax

```js
// Full arrow function
const functionName = (parameter1, parameter2) => {
  // code
  return result;
};

// Short form: one parameter, no parentheses needed
const double = n => n * 2;

// Short form: no parameters, use empty parentheses
const sayHello = () => "Hello!";

// Short form: one expression (implicit return — no return keyword needed)
const add = (a, b) => a + b;
```

### Simple Example

```js
// Classic function
const squareClassic = function(n) {
  return n * n;
};

// Same function as an arrow function
const squareArrow = n => n * n;

console.log(squareClassic(5)); // 25
console.log(squareArrow(5));   // 25
```

### Implicit Return

If the function body is a **single expression**, you can skip the curly braces
`{}` and the `return` keyword. JavaScript automatically returns the expression.

```js
// With curly braces: need explicit return
const add = (a, b) => {
  return a + b;
};

// Without curly braces: implicit return
const add = (a, b) => a + b;

// Return an object — wrap it in parentheses to avoid confusion with {}
const makeUser = (name, age) => ({ name: name, age: age });
console.log(makeUser("Alice", 25)); // { name: "Alice", age: 25 }
```

### The `this` Keyword Difference (Very Important)

This is the most important concept about arrow functions.

In regular functions, `this` refers to **who called the function**.
In arrow functions, `this` refers to **where the function was written** (the
surrounding scope). Arrow functions don't have their own `this` at all.

```js
// ❌ PROBLEM with regular function in a method
const timer = {
  seconds: 0,
  start: function() {
    setInterval(function() {
      this.seconds++;             // 'this' here is NOT timer — it's window/undefined
      console.log(this.seconds);  // NaN or error
    }, 1000);
  }
};

// ✅ SOLUTION with arrow function
const timer = {
  seconds: 0,
  start: function() {
    setInterval(() => {
      this.seconds++;             // 'this' here IS timer — arrow inherits it
      console.log(this.seconds);  // 1, 2, 3, 4...
    }, 1000);
  }
};
```

### Real-World Example

```js
const prices = [10, 25, 8, 42, 15];

// Filter prices over $20 and double them, using arrow functions
const result = prices
  .filter(price => price > 20)    // keep only prices above 20
  .map(price => price * 2);       // double each remaining price

console.log(result); // [50, 84, 30]
```

### Arrow Function Quick Reference Table

| Scenario | Syntax Example |
|----------|---------------|
| No parameters | `() => expression` |
| One parameter | `n => expression` |
| Multiple parameters | `(a, b) => expression` |
| Multiple statements | `(a, b) => { ...; return x; }` |
| Return an object | `(a) => ({ key: a })` |

### When NOT to Use Arrow Functions

> ⚠️ **Warning:** Do not use arrow functions for:
>
> - **Object methods** — `this` will not refer to the object
> - **Constructor functions** — arrow functions cannot be used with `new`
> - **`arguments` object** — arrow functions don't have their own `arguments`

```js
// ❌ WRONG: Arrow function as object method
const person = {
  name: "Alice",
  greet: () => {
    console.log("Hello, " + this.name); // 'this' is NOT person here
  }
};
person.greet(); // "Hello, undefined"

// ✅ CORRECT: Regular function as object method
const person = {
  name: "Alice",
  greet: function() {
    console.log("Hello, " + this.name); // 'this' IS person
  }
};
person.greet(); // "Hello, Alice"
```

### Interview Points

- Arrow functions are **syntactic sugar** but have a meaningful difference: `this`
- They **cannot** be used as constructors (`new arrowFn()` throws a `TypeError`)
- They do **not** have their own `arguments` object
- They are ideal for **callbacks, array methods, and functional patterns**

---
## Parameters and Arguments

### Definition

- **Parameters** are the named variables listed in the function definition
  (placeholders)
- **Arguments** are the actual values you pass when calling the function

```js
function greet(name) {  // 'name' is the PARAMETER (a placeholder)
  return "Hi, " + name;
}

greet("Alice"); // "Alice" is the ARGUMENT (the actual value)
```

### Default Parameters

#### Definition

Default parameters let you define a **fallback value** for a parameter if the
caller does not provide one (or passes `undefined`).

#### Why It Exists

Without defaults, unset parameters are `undefined`, which causes bugs. Instead
of writing `if` checks inside every function, you can set smart defaults right
in the parameter list.

#### Syntax & Example

```js
// ❌ OLD WAY: manual default check
function greet(name) {
  name = name || "Guest"; // if name is falsy, use "Guest"
  return "Hello, " + name;
}

// ✅ MODERN WAY: default parameter
function greet(name = "Guest") {    // if name is not passed, use "Guest"
  return "Hello, " + name;
}

console.log(greet("Alice")); // "Hello, Alice"
console.log(greet());        // "Hello, Guest"
```

#### Real-World Example

```js
// Create a styled button with sensible defaults
function createButton(label = "Click Me", color = "blue", size = "medium") {
  return `<button style="color:${color}; font-size:${size}">${label}</button>`;
}

console.log(createButton());                      // default button
console.log(createButton("Submit", "green"));     // custom label and color
console.log(createButton("Delete", "red", "large")); // fully custom
```

---

### Rest Parameters

#### Definition

The **rest parameter** (`...`) collects all remaining arguments into a real
JavaScript **array**. It must always be the **last parameter**.

#### Why It Exists

Sometimes you don't know in advance how many arguments a function will receive.
Rest parameters let you handle any number of arguments cleanly.

#### Syntax & Example

```js
function sum(...numbers) {          // 'numbers' collects ALL arguments into an array
  let total = 0;
  for (const n of numbers) {
    total += n;                     // add each number to the total
  }
  return total;
}

console.log(sum(1, 2));          // 3
console.log(sum(1, 2, 3, 4, 5)); // 15
console.log(sum(10, 20, 30));    // 60
```

#### Real-World Example

```js
// Log messages with a severity prefix
function log(severity, ...messages) {       // first arg is severity, rest are messages
  const prefix = `[${severity.toUpperCase()}]`;
  messages.forEach(msg => console.log(prefix, msg)); // log each message
}

log("info", "Server started", "Port: 3000");
// [INFO] Server started
// [INFO] Port: 3000

log("error", "Database connection failed");
// [ERROR] Database connection failed
```

---

### Destructuring Parameters

#### Definition

**Destructuring parameters** let you unpack object properties or array elements
directly in the function signature instead of accessing them inside the body.

#### Why It Exists

When functions receive large objects (like user data or API responses), it is
cleaner and more readable to name only what you need right at the top.

#### Syntax & Example

```js
// ❌ WITHOUT destructuring
function displayUser(user) {
  console.log(user.name + " is " + user.age); // have to write user.name, user.age
}

// ✅ WITH destructuring
function displayUser({ name, age }) {           // unpack directly from object
  console.log(name + " is " + age);            // use directly
}

displayUser({ name: "Alice", age: 30, city: "NY" }); // "Alice is 30"
```

#### Real-World Example

```js
// API response object
const apiResponse = {
  status: 200,
  data: {
    id: 42,
    username: "alice_dev",
    email: "alice@example.com"
  }
};

// Destructure nested object and use defaults
function handleResponse({ status, data: { username, email } = {} }) {
  if (status === 200) {
    console.log(`Welcome back, ${username}! (${email})`);
  }
}

handleResponse(apiResponse); // "Welcome back, alice_dev! (alice@example.com)"
```

---

## Return Values

### Definition

The `return` statement ends the function and **sends a value back** to where
the function was called. Without `return`, a function gives back `undefined`.

### Why It Exists

Functions would be useless if they could not communicate results. `return` is
how a function shares the outcome of its work with the rest of the program.

### Key Rules

- A function **stops immediately** when it hits `return`
- A function can only return **one value** (but that value can be an array or object)
- If there is no `return`, the function returns `undefined` automatically

```js
// Returning a single value
function square(n) {
  return n * n;  // sends n*n back to the caller
  console.log("This never runs"); // code after return is unreachable
}

// Returning multiple values via an object
function getMinMax(numbers) {
  const min = Math.min(...numbers); // find smallest
  const max = Math.max(...numbers); // find largest
  return { min, max };              // return both in one object
}

const { min, max } = getMinMax([3, 1, 7, 2, 9]);
console.log(min, max); // 1 9
```

### Common Mistakes

```js
// ❌ WRONG: Accidental line break after return
function getValue() {
  return       // JavaScript inserts a semicolon here automatically!
    { value: 42 };  // This never executes
}
console.log(getValue()); // undefined ← Bug!

// ✅ CORRECT: Opening brace on same line as return
function getValue() {
  return {     // Opening brace on same line
    value: 42
  };
}
console.log(getValue()); // { value: 42 }
```

---
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
## Real-World Functional Patterns

### 1. Function Composition

Build complex operations by combining (composing) small, pure functions:

```js
// Small, single-purpose functions
const trim = str => str.trim();                    // remove whitespace
const lowercase = str => str.toLowerCase();        // make lowercase
const capitalize = str => str[0].toUpperCase() + str.slice(1); // capitalize first

// Compose them: right to left
const compose = (...fns) => value =>
  fns.reduceRight((acc, fn) => fn(acc), value);

const formatName = compose(capitalize, lowercase, trim);

console.log(formatName("  aLiCe  ")); // "Alice"
```

### 2. Currying

Transform a function that takes multiple arguments into a chain of functions,
each taking one argument:

```js
// Regular function
const add = (a, b) => a + b;

// Curried version
const curriedAdd = a => b => a + b;  // returns a new function that waits for b

const add5 = curriedAdd(5); // 'a' is fixed at 5
console.log(add5(3));  // 8
console.log(add5(10)); // 15
console.log(add5(20)); // 25

// Real use: create specialized validators
const isGreaterThan = min => value => value > min;
const isAdult = isGreaterThan(18);
const isHighScore = isGreaterThan(90);

console.log(isAdult(25));     // true
console.log(isAdult(16));     // false
console.log(isHighScore(95)); // true
```

### 3. Memoization (Caching Results)

Cache the result of expensive function calls so they are not recalculated:

```js
function memoize(fn) {
  const cache = {};              // private cache object via closure

  return function(...args) {
    const key = JSON.stringify(args); // convert args to a string key

    if (cache[key] !== undefined) {
      console.log("From cache:", key);
      return cache[key];             // return cached result immediately
    }

    const result = fn(...args);      // calculate for the first time
    cache[key] = result;             // store in cache
    return result;
  };
}

// Expensive calculation: fibonacci
function slowFib(n) {
  if (n <= 1) return n;
  return slowFib(n - 1) + slowFib(n - 2);
}

const fastFib = memoize(slowFib);

console.log(fastFib(40)); // calculated (slow first time)
console.log(fastFib(40)); // "From cache: [40]" — instant!
```

### 4. Partial Application

Pre-fill some arguments of a function to create a specialized version:

```js
function partial(fn, ...presetArgs) {
  return function(...laterArgs) {
    return fn(...presetArgs, ...laterArgs); // combine preset + later args
  };
}

function sendEmail(from, to, subject, body) {
  console.log(`From: ${from} | To: ${to} | Subject: ${subject}`);
}

// Pre-fill the 'from' address for all emails from this system
const sendFromSystem = partial(sendEmail, "system@myapp.com");

sendFromSystem("user@example.com", "Welcome!", "Welcome to MyApp!");
sendFromSystem("user@example.com", "Alert", "Your password was changed");
```

---

## Common Mistakes Developers Make

> ⚠️ **Mistake 1: Forgetting `return`**

```js
// Bug: function returns undefined silently
function double(n) { n * 2; }      // ❌ no return
function double(n) { return n * 2; } // ✅
```

> ⚠️ **Mistake 2: Calling function expression before declaration**

```js
greet(); // ❌ TypeError
const greet = () => "hello";
```

> ⚠️ **Mistake 3: Using arrow functions as object methods**

```js
const obj = { name: "X", getName: () => this.name }; // ❌ this is wrong
const obj = { name: "X", getName() { return this.name; } }; // ✅
```

> ⚠️ **Mistake 4: Mutating function parameters (objects/arrays)**

```js
function addItem(arr, item) {
  arr.push(item); // ❌ mutates the original array!
  return arr;
}

function addItem(arr, item) {
  return [...arr, item]; // ✅ returns a new array
}
```

> ⚠️ **Mistake 5: Ignoring the `var` + loop closure problem**

```js
for (var i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100); // ❌ prints 5 five times
}
// Fix: use let
for (let i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100); // ✅ prints 0,1,2,3,4
}
```

> ⚠️ **Mistake 6: Accidental `return` line break**

```js
return  // ❌ JS inserts semicolon here
{ value: 1 };
// Fix: brace on same line
return { // ✅
  value: 1
};
```

---
## Best Practices

- ✅ **Name functions clearly** — `getUserAge()` is better than `getData()`
- ✅ **Keep functions small** — one function, one job (Single Responsibility)
- ✅ **Prefer `const` for function expressions and arrow functions**
- ✅ **Use pure functions wherever possible** — easier to test and debug
- ✅ **Avoid modifying parameters** — return new values instead
- ✅ **Use default parameters** instead of `if/else` guards inside the body
- ✅ **Use arrow functions for callbacks** — shorter and avoids `this` bugs
- ✅ **Always `return` from functions that produce a value**
- ✅ **Keep nesting shallow** — deeply nested closures are hard to read
- ✅ **Use `let` instead of `var` in loops** to avoid closure bugs

---

## Interview Questions

### Beginner Level

**Q1. What is the difference between a function declaration and a function
expression?**

> Function declarations are hoisted completely and can be called before they
> are written. Function expressions are assigned to variables and are not
> available until the assignment line is reached.

**Q2. What does `return` do?**

> It ends function execution and sends a value back to the caller. Without it,
> the function returns `undefined`.

**Q3. What is a parameter vs an argument?**

> Parameters are the named placeholders in the function definition. Arguments
> are the actual values passed when calling the function.

---

### Intermediate Level

**Q4. What is a closure? Give an example.**

> A closure is a function that remembers variables from its outer scope even
> after the outer function has finished. Example: a counter function that keeps
> its `count` variable alive via an inner function.

**Q5. What is the difference between `var`, `let`, and `const` in the context
of scope?**

> `var` is function-scoped and ignores block boundaries. `let` and `const` are
> block-scoped and respect `{}` blocks. `var` is hoisted with `undefined`,
> while `let`/`const` are in the Temporal Dead Zone until declared.

**Q6. What is the output of this code, and why?**

```js
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}
```

> Output: `3, 3, 3`. Because `var` creates a single `i` shared by all
> iterations. By the time the callbacks run, the loop has finished and `i`
> is `3`. Fix by using `let`.

---

### Advanced Level

**Q7. What is a higher-order function? Name three built-in examples.**

> A function that takes a function as an argument or returns one. Examples:
> `.map()`, `.filter()`, `.reduce()`.

**Q8. What is currying and why is it useful?**

> Currying transforms a function with multiple arguments into a chain of
> single-argument functions. It enables partial application and creating
> specialized functions from general ones.

**Q9. What is an IIFE and when would you use it?**

> An Immediately Invoked Function Expression runs as soon as it is defined.
> It creates a private scope to avoid polluting the global namespace — useful
> for initialization code and the module pattern.

**Q10. What is the difference between `this` in a regular function and an
arrow function?**

> Regular functions have their own `this` which is determined by how they are
> called. Arrow functions inherit `this` from their surrounding scope and never
> have their own `this`.

---

## Debugging Tips

- 🔍 **Use `console.log` at the start and end** of a function to trace inputs
  and outputs
- 🔍 **Check for missing `return`** if a function gives back `undefined`
  unexpectedly
- 🔍 **Use browser DevTools Debugger** — set breakpoints inside functions to
  step through line by line
- 🔍 **Inspect the call stack** in DevTools to see which function called which
- 🔍 **Use named function expressions** instead of anonymous ones — they show
  better names in stack traces
- 🔍 **If `this` is `undefined`**, you probably need to use an arrow function
  or `.bind()`
- 🔍 **If a closure variable doesn't update**, make sure you are not copying
  a primitive value — closures capture the **reference**, not a snapshot,
  unless the variable is reassigned
- 🔍 **Use `typeof fn === 'function'`** before calling a variable as a function
  to avoid `TypeError: fn is not a function`

---

## Exercises

### Exercise 1: Arrow Function Conversion

Convert the following function declarations to arrow functions. Try all three
short forms where appropriate.

```js
// Convert each of these:

// 1.
function double(n) {
  return n * 2;
}

// 2.
function greet(name) {
  return "Hello, " + name + "!";
}

// 3.
function add(a, b) {
  return a + b;
}

// 4.
function getUser(id) {
  return { id: id, active: true };
}
```

<details>
<summary>💡 Solution</summary>

```js
// 1. Single parameter — no parentheses, implicit return
const double = n => n * 2;

// 2. Single parameter — no parentheses, implicit return
const greet = name => "Hello, " + name + "!";

// 3. Multiple parameters — parentheses, implicit return
const add = (a, b) => a + b;

// 4. Returns object — wrap in parentheses for implicit return
const getUser = id => ({ id: id, active: true });
```

</details>

---

### Exercise 2: Closure-Based Counter

Build a counter using closures that supports `increment`, `decrement`, `reset`,
and `getCount`. The count should start at a value passed in.

```js
// Your task:
function createCounter(startValue) {
  // TODO: implement using closure
}

// Expected behavior:
const counter = createCounter(10);
counter.increment(); // 11
counter.increment(); // 12
counter.decrement(); // 11
counter.reset();
counter.getCount();  // 10
```

<details>
<summary>💡 Solution</summary>

```js
function createCounter(startValue = 0) {
  let count = startValue; // private variable captured by closure

  return {
    increment() {
      count++;
      return count;
    },
    decrement() {
      count--;
      return count;
    },
    reset() {
      count = startValue; // reset to the original start value
      return count;
    },
    getCount() {
      return count;
    }
  };
}

const counter = createCounter(10);
console.log(counter.increment()); // 11
console.log(counter.increment()); // 12
console.log(counter.decrement()); // 11
counter.reset();
console.log(counter.getCount()); // 10
```

</details>

---

### Exercise 3: The `once` Function

Implement a `once` higher-order function that wraps any function and ensures
it can only be called **one time**. After the first call, it returns the same
result without running the function again.

```js
// Your task:
function once(fn) {
  // TODO: implement using closure
}

// Expected behavior:
const initApp = once(() => {
  console.log("App initialized!");
  return true;
});

initApp(); // "App initialized!" → true
initApp(); // nothing logs → still returns true (same result, no re-run)
initApp(); // nothing logs → still returns true
```

<details>
<summary>💡 Solution</summary>

```js
function once(fn) {
  let called = false;    // has the function been called yet?
  let result;            // store the result from the first call

  return function(...args) {
    if (!called) {
      called = true;           // mark as called
      result = fn(...args);    // run the original function once
    }
    return result;             // always return the first call's result
  };
}

const initApp = once(() => {
  console.log("App initialized!");
  return true;
});

console.log(initApp()); // "App initialized!" → true
console.log(initApp()); //                    → true (no log, not re-run)
console.log(initApp()); //                    → true
```

</details>

---

### Exercise 4: Function Composition Pipeline

Implement a `pipe` function that takes multiple functions and returns a single
function. When called, it passes its argument through each function from left
to right (the output of each becomes the input of the next).

```js
// Your task:
function pipe(...fns) {
  // TODO: implement using reduce
}

// Test functions
const trim = str => str.trim();
const lowercase = str => str.toLowerCase();
const removeSpaces = str => str.replace(/\s+/g, "-");
const addPrefix = str => "user-" + str;

// Expected behavior:
const formatUsername = pipe(trim, lowercase, removeSpaces, addPrefix);
console.log(formatUsername("  John Doe  ")); // "user-john-doe"
```

<details>
<summary>💡 Solution</summary>

```js
function pipe(...fns) {
  return function(value) {
    return fns.reduce((acc, fn) => fn(acc), value);
    // Start with 'value', pass it through each function left to right
  };
}

const trim = str => str.trim();
const lowercase = str => str.toLowerCase();
const removeSpaces = str => str.replace(/\s+/g, "-");
const addPrefix = str => "user-" + str;

const formatUsername = pipe(trim, lowercase, removeSpaces, addPrefix);

console.log(formatUsername("  John Doe  "));   // "user-john-doe"
console.log(formatUsername("  JANE SMITH  ")); // "user-jane-smith"
```

</details>

---

## Chapter Summary

| Concept | One-Line Summary |
|---------|-----------------|
| **Function Declaration** | Named, hoisted, classic way to define functions |
| **Function Expression** | Function stored in a variable; not hoisted |
| **Arrow Function** | Short syntax; inherits `this` from parent scope |
| **Default Parameters** | Fallback values when arguments are not provided |
| **Rest Parameters** | Collects extra arguments into an array |
| **Destructuring Parameters** | Unpack objects/arrays directly in function signature |
| **Return** | Ends function and sends a value back |
| **Scope** | Rules determining where variables are accessible |
| **Hoisting** | Declarations moved to top of scope before execution |
| **Closure** | Inner function remembers outer function's variables |
| **Higher-Order Functions** | Functions that take or return other functions |
| **IIFE** | Function that runs immediately on definition |
| **Pure Function** | Same input → same output, no side effects |
| **Currying** | Transform multi-arg function into chain of single-arg functions |
| **Memoization** | Cache expensive results using closures |

---

> 🎉 **You have completed Chapter 4: Functions in JavaScript.**
>
> Functions are truly the heart of JavaScript. Every concept you have learned
> here — scope, closures, higher-order functions — builds directly on the
> previous one. Take time to practice the exercises, re-read the closure
> section multiple times, and experiment in the browser console. Understanding
> functions deeply will make every other topic in JavaScript easier.

---

**Previous:** [Chapter 3: Operators & Control Flow](./ch03-operators-and-control-flow.md) · **Next:** [Chapter 5: Arrays & Objects](./ch05-arrays-and-objects.md)

**➡️ [Next Chapter: Arrays & Objects →](./ch05-arrays-and-objects.md)
