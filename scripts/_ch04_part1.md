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
