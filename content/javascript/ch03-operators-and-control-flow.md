---
title: Operators and Control Flow
description: Arithmetic, comparison, logical operators, if/else, switch, and loops in JavaScript
order: 3
tags: [javascript, operators, if, switch, loops, control-flow]
---

# Chapter 3: Operators and Control Flow

> **This chapter is the engine room of programming.** Every useful program needs to make decisions, repeat actions, and perform calculations. In this chapter, you will learn exactly how JavaScript evaluates expressions, makes choices, and repeats tasks. By the end, you will be able to write programs that *think* and *act* based on data — which is the heart of all programming.

---

## Table of Contents

1. [What Are Operators?](#what-are-operators)
2. [Arithmetic Operators](#arithmetic-operators)
3. [Assignment Operators](#assignment-operators)
4. [Comparison Operators](#comparison-operators)
5. [Logical Operators](#logical-operators)
6. [Nullish Coalescing (??)](#nullish-coalescing-)
7. [Optional Chaining (?.)](#optional-chaining-)
8. [What is Control Flow?](#what-is-control-flow)
9. [if / else Statements](#if--else-statements)
10. [The Ternary Operator](#the-ternary-operator)
11. [The switch Statement](#the-switch-statement)
12. [Loops](#loops)
13. [The for Loop](#the-for-loop)
14. [The while Loop](#the-while-loop)
15. [The do...while Loop](#the-dowhile-loop)
16. [The for...of Loop](#the-forof-loop)
17. [The for...in Loop](#the-forin-loop)
18. [break and continue](#break-and-continue)
19. [Labeled Loops](#labeled-loops)
20. [Modern Array Iteration](#modern-array-iteration)
21. [Common Patterns](#common-patterns)
22. [Best Practices](#best-practices)
23. [Common Mistakes](#common-mistakes)
24. [Interview Points](#interview-points)
25. [Exercises](#exercises)
26. [Chapter Summary](#chapter-summary)

---

## What Are Operators?

### Definition

An **operator** is a symbol or keyword that tells JavaScript to perform a specific operation on one or more values. The values that an operator works on are called **operands**.

Think of operators like verbs in a sentence — they describe the *action* being performed on the *subjects* (operands).

```
10  +  5   =   15
│   │  │
│   │  └── right operand
│   └───── operator (addition)
└───────── left operand
```

### Why Operators Exist

Without operators, a program could only store data — it could never *do* anything with that data. Operators are what allow you to:
- Calculate (`price * quantity`)
- Compare (`age >= 18`)
- Make decisions (`isLoggedIn && hasPermission`)
- Assign values (`score = score + 10`)

### Operator Precedence (Order of Operations)

Just like in mathematics, JavaScript evaluates operators in a specific order. Multiplication happens before addition, for example. This is called **operator precedence**.

```javascript
// Without understanding precedence, this is confusing:
let result = 2 + 3 * 4; // Is it (2+3)*4=20 or 2+(3*4)=14?

console.log(result); // 14 — multiplication (*) has higher precedence than addition (+)

// Use parentheses to force a specific order:
let result2 = (2 + 3) * 4;
console.log(result2); // 20 ✅ parentheses always have the highest precedence
```

**Precedence order (high to low, simplified):**

| Priority | Operators | Example |
|---|---|---|
| 1 (highest) | `()` Grouping | `(2 + 3)` |
| 2 | `**` Exponentiation | `2 ** 3` |
| 3 | `!`, `+`, `-` (unary) | `!true`, `+5` |
| 4 | `*`, `/`, `%` | `10 * 2` |
| 5 | `+`, `-` (binary) | `5 + 3` |
| 6 | `<`, `>`, `<=`, `>=` | `5 > 3` |
| 7 | `===`, `!==`, `==`, `!=` | `x === y` |
| 8 | `&&` | `a && b` |
| 9 | `\|\|`, `??` | `a \|\| b` |
| 10 (lowest) | `=`, `+=`, `-=`, etc. | `x = 5` |

> **Practical tip:** When in doubt, use parentheses `()` to make your intent explicit. It makes code easier to read and prevents precedence-related bugs.

---

## Arithmetic Operators

### Definition

**Arithmetic operators** perform mathematical calculations on numeric values, just like the operations you learned in school.

### Why They Exist

Every program that deals with quantities — prices, scores, distances, time, percentages — needs arithmetic. These operators are the mathematical foundation of JavaScript.

### All Arithmetic Operators

| Operator | Name | Example | Result |
|---|---|---|---|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | Division | `10 / 3` | `3.333...` |
| `%` | Modulo (remainder) | `10 % 3` | `1` |
| `**` | Exponentiation | `2 ** 8` | `256` |
| `++` | Increment | `x++` | `x + 1` |
| `--` | Decrement | `x--` | `x - 1` |

### Simple Examples

```javascript
let a = 10;
let b = 3;

console.log(a + b);  // 13 — addition
console.log(a - b);  // 7  — subtraction
console.log(a * b);  // 30 — multiplication
console.log(a / b);  // 3.3333333333333335 — division (with floating point)
console.log(a % b);  // 1  — remainder: 10 divided by 3 is 3 remainder 1
console.log(a ** b); // 1000 — 10 to the power of 3 (10³)
```

### The Modulo Operator (%) in Depth

Modulo is the one most beginners find confusing. It gives you the **remainder** after division — the "leftover" when one number doesn't divide evenly into another.

```javascript
// Think of it as: "What's left over after dividing as many whole times as possible?"
console.log(10 % 3);  // 1   — 3 goes into 10 three times (3×3=9), leftover is 1
console.log(15 % 4);  // 3   — 4 goes into 15 three times (3×4=12), leftover is 3
console.log(8 % 2);   // 0   — 2 goes into 8 four times exactly, no remainder
console.log(5 % 10);  // 5   — 10 goes into 5 zero times, leftover is 5

// Real-world uses of modulo:

// 1. Check if a number is even or odd:
let number = 7;
if (number % 2 === 0) {
  console.log("Even");
} else {
  console.log("Odd"); // "Odd" — 7 divided by 2 has remainder 1
}

// 2. Wrap around within a range (circular counting):
// For example, 12-hour clock: after 12, go back to 1
let hour = 14; // 14:00 in 24-hour format
let clockHour = hour % 12 || 12; // % 12 gives 2, which is 2 PM
console.log(clockHour); // 2

// 3. FizzBuzz (the famous interview problem — shown later):
for (let i = 1; i <= 15; i++) {
  if (i % 15 === 0) console.log("FizzBuzz");
  else if (i % 3 === 0) console.log("Fizz");
  else if (i % 5 === 0) console.log("Buzz");
  else console.log(i);
}
```

### Increment and Decrement Operators

These add 1 or subtract 1 from a variable. They have two forms: **prefix** and **postfix**.

```javascript
let x = 5;

// POSTFIX: x++ → uses the CURRENT value first, THEN increments
let a = x++; // a gets 5 (current value), THEN x becomes 6
console.log(a); // 5 (the value BEFORE incrementing)
console.log(x); // 6 (now incremented)

// RESET for clarity:
x = 5;

// PREFIX: ++x → increments FIRST, THEN uses the new value
let b = ++x; // x becomes 6 FIRST, then b gets 6
console.log(b); // 6 (the value AFTER incrementing)
console.log(x); // 6

// Similarly for decrement:
let y = 10;
let c = y--; // c gets 10 (old value), y becomes 9
let d = --y; // y becomes 8 first, d gets 8
console.log(c); // 10
console.log(d); // 8
```

```
POSTFIX (x++):
  Step 1: Read current value of x (5)
  Step 2: Return that value (5) → assigned to 'a'
  Step 3: Increment x (x becomes 6)

PREFIX (++x):
  Step 1: Increment x (x becomes 6)
  Step 2: Return the new value (6) → assigned to 'b'
```

> ⚠️ **Warning:** The difference between `x++` and `++x` only matters when you use the result in an expression. In a standalone statement like `x++;` or `++x;` by itself, both do the same thing — increment `x` by 1.

### The + Operator with Strings (Context Matters!)

The `+` operator has dual behavior — it is both an **arithmetic addition** and a **string concatenation** operator, depending on the types of its operands.

```javascript
// Number + Number = Addition:
console.log(5 + 3);         // 8

// String + Anything = Concatenation (joining strings):
console.log("Hello" + " World"); // "Hello World"
console.log("Age: " + 25);       // "Age: 25" (25 coerced to "25")
console.log("" + true);          // "true" (boolean coerced to string)

// ⚠️ The order matters:
console.log(1 + 2 + "3");  // "33" — (1+2)=3, then 3+"3"="33"
console.log("1" + 2 + 3);  // "123" — "1"+2="12", then "12"+3="123"

// Always use template literals for string building — much cleaner:
let name = "Alice";
let age = 25;
console.log(`${name} is ${age} years old.`); // "Alice is 25 years old."
```

### Real-World Example: Shopping Cart Calculator

```javascript
// E-commerce order calculation:
const ITEM_PRICE = 24.99;
const QUANTITY = 4;
const SHIPPING_FEE = 5.99;
const DISCOUNT_PERCENT = 15;
const TAX_RATE = 0.08;

// Step 1: Calculate subtotal
let subtotal = ITEM_PRICE * QUANTITY;
console.log(`Subtotal: $${subtotal.toFixed(2)}`); // $99.96

// Step 2: Apply percentage discount
let discountAmount = subtotal * (DISCOUNT_PERCENT / 100);
let afterDiscount = subtotal - discountAmount;
console.log(`Discount (${DISCOUNT_PERCENT}%): -$${discountAmount.toFixed(2)}`); // -$14.99
console.log(`After discount: $${afterDiscount.toFixed(2)}`); // $84.97

// Step 3: Apply tax
let taxAmount = afterDiscount * TAX_RATE;
console.log(`Tax (${TAX_RATE * 100}%): $${taxAmount.toFixed(2)}`); // $6.80

// Step 4: Add shipping
let finalTotal = afterDiscount + taxAmount + SHIPPING_FEE;
console.log(`Shipping: $${SHIPPING_FEE.toFixed(2)}`);
console.log(`TOTAL: $${finalTotal.toFixed(2)}`); // $97.76

// Exponentiation real-world: compound interest
// Formula: A = P(1 + r)^n
const PRINCIPAL = 1000;   // initial investment
const RATE = 0.05;        // 5% annual interest
const YEARS = 10;

let compoundTotal = PRINCIPAL * ((1 + RATE) ** YEARS);
console.log(`$${PRINCIPAL} at ${RATE*100}% for ${YEARS} years = $${compoundTotal.toFixed(2)}`);
// $1000 at 5% for 10 years = $1628.89
```

### Common Arithmetic Mistakes

```javascript
// ❌ Mistake 1: Forgetting floating point imprecision:
console.log(0.1 + 0.2 === 0.3); // false! — always use toFixed() for money

// ❌ Mistake 2: Dividing integers and expecting no decimal:
let half = 5 / 2;
console.log(half); // 2.5 — JS has no integer division by default
// ✅ Use Math.floor() if you want whole number:
console.log(Math.floor(5 / 2)); // 2

// ❌ Mistake 3: Confusing postfix vs prefix:
let score = 10;
let display = score++; // Thinking this gives 11
console.log(display);  // 10 — postfix returns the OLD value first!

// ❌ Mistake 4: Division by zero:
console.log(10 / 0);  // Infinity — not an error in JS!
console.log(-5 / 0);  // -Infinity
console.log(0 / 0);   // NaN
```

---

## Assignment Operators

### Definition

**Assignment operators** store a value into a variable. The basic one is `=`. The compound versions combine an arithmetic operation with assignment.

### Why They Exist

Updating a variable based on its current value is extremely common — incrementing a counter, adding to a total, reducing a health bar. Compound assignment operators make this shorter and more readable.

### All Assignment Operators

| Operator | Meaning | Example | Equivalent To |
|---|---|---|---|
| `=` | Assign | `x = 5` | `x = 5` |
| `+=` | Add and assign | `x += 3` | `x = x + 3` |
| `-=` | Subtract and assign | `x -= 3` | `x = x - 3` |
| `*=` | Multiply and assign | `x *= 3` | `x = x * 3` |
| `/=` | Divide and assign | `x /= 3` | `x = x / 3` |
| `%=` | Modulo and assign | `x %= 3` | `x = x % 3` |
| `**=` | Exponentiate and assign | `x **= 3` | `x = x ** 3` |
| `??=` | Assign if nullish | `x ??= 5` | `x = x ?? 5` |
| `\|\|=` | Assign if falsy | `x \|\|= 5` | `x = x \|\| 5` |
| `&&=` | Assign if truthy | `x &&= 5` | `x = x && 5` |

### Examples

```javascript
let score = 100;

score += 50;   // score = 100 + 50 = 150
console.log(score); // 150

score -= 30;   // score = 150 - 30 = 120
console.log(score); // 120

score *= 2;    // score = 120 * 2 = 240
console.log(score); // 240

score /= 4;    // score = 240 / 4 = 60
console.log(score); // 60

score %= 7;    // score = 60 % 7 = 4 (remainder when 60 is divided by 7)
console.log(score); // 4

score **= 3;   // score = 4 ** 3 = 64 (4 cubed)
console.log(score); // 64

// Logical assignment (ES2021):
let user = null;
user ??= "Guest"; // Assign "Guest" only if user is null or undefined
console.log(user); // "Guest"

let name = "Alice";
name ??= "Guest"; // name is NOT null/undefined, so nothing changes
console.log(name); // "Alice"
```

---

## Comparison Operators

### Definition

**Comparison operators** compare two values and always return a **boolean** — either `true` or `false`. They are used to make decisions in your code.

### Why They Exist

Every condition in programming is a question with a yes/no answer. Is the user old enough? Is the score high enough? Is the cart empty? Comparison operators answer these questions.

### All Comparison Operators

| Operator | Name | Example | Result |
|---|---|---|---|
| `===` | Strict equal | `5 === 5` | `true` |
| `!==` | Strict not equal | `5 !== 6` | `true` |
| `==` | Loose equal (with coercion) | `5 == "5"` | `true` |
| `!=` | Loose not equal | `5 != "6"` | `true` |
| `>` | Greater than | `10 > 5` | `true` |
| `<` | Less than | `5 < 10` | `true` |
| `>=` | Greater than or equal | `5 >= 5` | `true` |
| `<=` | Less than or equal | `4 <= 5` | `true` |

### How JavaScript Evaluates Comparisons Internally

When JavaScript sees a comparison like `10 > 5`, it:
1. Evaluates the left operand: `10`
2. Evaluates the right operand: `5`
3. Applies the operator: is `10` greater than `5`? Yes.
4. Returns the boolean result: `true`

That result can then be stored in a variable or used directly in a condition.

```javascript
let age = 20;

// Each of these creates a boolean value:
let isAdult = age >= 18;          // true
let isChild = age < 13;           // false
let isPerfectAge = age === 21;    // false
let isNotRetired = age !== 65;    // true

console.log(isAdult);      // true
console.log(isChild);      // false
console.log(isPerfectAge); // false
console.log(isNotRetired); // true
```

### String Comparisons

When comparing strings, JavaScript compares character by character using **Unicode values** (the numeric code of each character). This means strings are compared **alphabetically** — but with some surprising rules for uppercase letters.

```javascript
// Alphabetical comparison:
console.log("apple" < "banana");  // true ("a" comes before "b")
console.log("cat" > "bat");       // true ("c" > "b")
console.log("abc" === "abc");     // true (identical strings)

// ⚠️ Uppercase letters come BEFORE lowercase in Unicode!
console.log("A" < "a");          // true  (A=65, a=97 in Unicode)
console.log("Banana" < "apple"); // true  ("B"=66 < "a"=97 — uppercase B comes first!)
console.log("Zoo" < "ant");      // true  ("Z"=90 < "a"=97)

// ⚠️ Numbers as strings compare character by character — not numerically!
console.log("10" > "9");   // false! "1" (49) < "9" (57) in Unicode — string comparison!
console.log(10 > 9);       // true — numeric comparison works correctly

// Always convert to numbers before numeric comparison:
console.log(Number("10") > Number("9")); // true ✅
```

### Deep Dive: Why Type Coercion Happens in == Comparisons

When you use `==`, JavaScript follows a specific algorithm to convert types:

```
If types are the same → compare directly (like ===)
If one is null and other is undefined → return true (special rule)
If one is a number and other is a string → convert string to number, then compare
If one is a boolean → convert boolean to number (true→1, false→0), then compare again
If one is an object → convert object to primitive, then compare again
```

```javascript
// Why == produces surprising results:
console.log(false == 0);   // true — false converts to 0
console.log(true == 1);    // true — true converts to 1
console.log("" == 0);      // true — "" converts to 0
console.log("1" == true);  // true — true→1, "1"→1
console.log(null == undefined); // true — special rule: these two are "equal" with ==
console.log(null == 0);    // false — special rule: null only equals undefined (not 0!)
console.log([] == false);  // true — []→""→0, false→0

// All of the above return false with ===:
console.log(false === 0);   // false ✅
console.log("" === 0);      // false ✅
console.log(null === undefined); // false ✅

// RULE: Always use === unless you have a very specific reason for ==
```

### Real-World Example: User Access Control

```javascript
// Checking multiple conditions for system access:
function checkAccess(user) {
  const currentYear = 2024;
  const minimumAge = 18;

  // Strict comparisons for reliability:
  const isOldEnough = user.birthYear <= (currentYear - minimumAge);
  const hasActiveAccount = user.status === "active";
  const hasNotExpired = user.expiryYear >= currentYear;
  const isPremium = user.tier === "premium" || user.tier === "enterprise";

  console.log(`
    Access check for ${user.name}:
    Old enough:      ${isOldEnough}
    Account active:  ${hasActiveAccount}
    Not expired:     ${hasNotExpired}
    Premium tier:    ${isPremium}
  `);

  return isOldEnough && hasActiveAccount && hasNotExpired;
}

let user = {
  name: "Alice",
  birthYear: 1990,
  status: "active",
  expiryYear: 2025,
  tier: "premium"
};

let canAccess = checkAccess(user);
console.log("Access granted:", canAccess); // true
```

---
## Logical Operators

### Definition

**Logical operators** combine or modify boolean values (or any values that can be evaluated as boolean). They are the foundation of all multi-condition decision making.

### Why They Exist

Real decisions are rarely simple yes/no questions with a single condition. "Can this user check out?" requires: is the user logged in? AND is the cart not empty? AND is the payment method valid? Logical operators let you combine multiple conditions into one.

### The Three Core Logical Operators

#### AND (&&) — "All must be true"

`&&` returns `true` only if **both** operands are truthy. The moment it finds a falsy value, it stops.

```javascript
// Truth table for &&:
console.log(true  && true);  // true  — both truthy ✅
console.log(true  && false); // false — right side is falsy
console.log(false && true);  // false — left side is falsy (stops here!)
console.log(false && false); // false — both falsy

// Real example:
let isLoggedIn = true;
let hasPermission = true;
let isNotBanned = true;

if (isLoggedIn && hasPermission && isNotBanned) {
  console.log("Access granted!");
}
```

#### OR (||) — "At least one must be true"

`||` returns `true` if **at least one** operand is truthy. The moment it finds a truthy value, it stops.

```javascript
// Truth table for ||:
console.log(true  || true);  // true  — left is truthy (stops here!)
console.log(true  || false); // true  — left is truthy
console.log(false || true);  // true  — right is truthy
console.log(false || false); // false — both falsy

// Real example:
let isAdmin = false;
let isModerator = true;
let isOwner = false;

if (isAdmin || isModerator || isOwner) {
  console.log("Can manage content!"); // runs because isModerator is true
}
```

#### NOT (!) — "Flip the boolean"

`!` inverts a boolean value — `true` becomes `false`, `false` becomes `true`.

```javascript
console.log(!true);  // false
console.log(!false); // true

// NOT also converts any value to its opposite boolean:
console.log(!0);       // true  (0 is falsy, !falsy = true)
console.log(!"hello"); // false (non-empty string is truthy, !truthy = false)
console.log(!null);    // true  (null is falsy)
console.log(!undefined); // true (undefined is falsy)
console.log(![]);      // false (empty array is TRUTHY, !truthy = false)

// Double NOT (!!) converts any value to a boolean without flipping it:
console.log(!!0);      // false (convert 0 to boolean: false)
console.log(!!1);      // true  (convert 1 to boolean: true)
console.log(!!"");     // false
console.log(!!"hi");   // true
```

### Short-Circuit Evaluation — How Logical Operators Really Work

This is one of the most important and powerful concepts in JavaScript. Logical operators do NOT just return `true` or `false`. They return one of their **actual operand values**, and they **stop evaluating** as soon as the result is determined.

This is called **short-circuit evaluation**.

#### How && Short-Circuits

`&&` evaluates left to right. It returns the **first falsy value** it encounters. If all values are truthy, it returns the **last value**.

```javascript
// && returns the FIRST FALSY value, or the LAST value if all are truthy:
console.log(1 && 2);         // 2       — 1 is truthy, so evaluate next; 2 is last → return 2
console.log(1 && 2 && 3);    // 3       — all truthy, returns last value
console.log(0 && "hello");   // 0       — 0 is falsy, stop here, return 0
console.log("" && 42);       // ""      — "" is falsy, stop here, return ""
console.log(null && 42);     // null    — null is falsy, stop here
console.log(false && alert("won't run")); // false — stops at false, alert never called!

// Real-world pattern: execute something ONLY if a condition is true
let user = { name: "Alice", isAdmin: true };

// Instead of a full if statement:
user.isAdmin && console.log("Showing admin panel"); // Only logs if isAdmin is truthy

// Access a property only if the object exists:
let config = null;
let timeout = config && config.timeout; // If config is null, timeout = null (safe!)
console.log(timeout); // null — no error thrown
```

#### How || Short-Circuits

`||` evaluates left to right. It returns the **first truthy value** it encounters. If all values are falsy, it returns the **last value**.

```javascript
// || returns the FIRST TRUTHY value, or the LAST value if all are falsy:
console.log(1 || 2);         // 1       — 1 is truthy, stop here, return 1
console.log(0 || 2);         // 2       — 0 is falsy, check next; 2 is truthy → return 2
console.log(0 || "" || 3);   // 3       — first two are falsy, 3 is truthy
console.log(0 || "" || null); // null   — all falsy, return last value (null)
console.log(false || undefined || 0); // 0 — all falsy, returns last (0)

// Real-world pattern: FALLBACK / DEFAULT VALUES
function greet(name) {
  let displayName = name || "Guest"; // If name is falsy, use "Guest"
  console.log(`Hello, ${displayName}!`);
}

greet("Alice");  // Hello, Alice!
greet("");       // Hello, Guest!   (empty string is falsy)
greet(null);     // Hello, Guest!   (null is falsy)
greet();         // Hello, Guest!   (undefined is falsy)

// Config defaults:
function connectToDatabase(options) {
  let host = options.host || "localhost";
  let port = options.port || 5432;
  let dbName = options.database || "myapp";
  console.log(`Connecting to ${host}:${port}/${dbName}`);
}
```

### Logical Operators with Non-Boolean Values — Practical Patterns

```javascript
// Pattern 1: Conditional execution with &&
// "If user exists, log their name"
let user = { name: "Alice" };
user && console.log(user.name); // "Alice"

let noUser = null;
noUser && console.log(noUser.name); // Nothing logged — short-circuits at null ✅

// Pattern 2: Default values with ||
let userTheme = ""; // User hasn't set a theme (empty string = falsy)
let activeTheme = userTheme || "light"; // Default to "light"
console.log(activeTheme); // "light"

// Pattern 3: Guard execution with &&
let permissions = ["read", "write"];
permissions.length > 0 && console.log("User has permissions:", permissions);

// Pattern 4: Complex conditions
let age = 22;
let hasId = true;
let isMember = false;

let canEnterVIP = age >= 21 && hasId && (isMember || age >= 30);
console.log(canEnterVIP); // false (isMember is false AND age < 30)

isMember = true;
canEnterVIP = age >= 21 && hasId && (isMember || age >= 30);
console.log(canEnterVIP); // true ✅
```

---

## Nullish Coalescing (??)

### Definition

The **nullish coalescing operator** `??` returns the right-hand side value if the left-hand side is `null` or `undefined`. It is like `||` but more specific — it only triggers for `null` and `undefined`, not for other falsy values like `0`, `false`, or `""`.

### Why It Exists

The `||` default pattern has a flaw: it treats `0`, `false`, and `""` as "missing" values because they are falsy. But sometimes `0` is a perfectly valid value (a score of zero, a retry count of zero, etc.). `??` was introduced in ES2020 to solve this specific problem.

```javascript
// THE PROBLEM with ||:
let userScore = 0; // A real score of zero
let displayScore = userScore || "No score yet";
console.log(displayScore); // "No score yet" ← WRONG! 0 is a valid score!

// THE SOLUTION with ??:
let displayScore2 = userScore ?? "No score yet";
console.log(displayScore2); // 0 ← Correct! 0 is not null/undefined

// More examples:
console.log(null ?? "default");        // "default" (null triggers ??)
console.log(undefined ?? "default");   // "default" (undefined triggers ??)
console.log(0 ?? "default");           // 0 (0 does NOT trigger ?? — it's not null/undefined)
console.log("" ?? "default");          // "" (empty string does NOT trigger ??)
console.log(false ?? "default");       // false (false does NOT trigger ??)
console.log(NaN ?? "default");         // NaN (NaN does NOT trigger ??)
```

### ?? vs || Comparison

| Value | `value ?? "default"` | `value \|\| "default"` |
|---|---|---|
| `null` | `"default"` | `"default"` |
| `undefined` | `"default"` | `"default"` |
| `0` | `0` ✅ | `"default"` ❌ |
| `""` | `""` ✅ | `"default"` ❌ |
| `false` | `false` ✅ | `"default"` ❌ |
| `NaN` | `NaN` ✅ | `"default"` ❌ |
| `"hello"` | `"hello"` | `"hello"` |
| `42` | `42` | `42` |

### Real-World Example

```javascript
// User settings where 0 and false are VALID values:
function applyUserSettings(settings) {
  // Use ?? — don't treat 0, false, or "" as "missing"
  const volume = settings.volume ?? 50;         // 0 is valid (muted)
  const brightness = settings.brightness ?? 100; // 0 is valid (dark)
  const notifications = settings.notifications ?? true; // false is valid (off)
  const username = settings.username ?? "Anonymous"; // "" is... debatable

  console.log({ volume, brightness, notifications, username });
}

// User explicitly set volume to 0 (muted):
applyUserSettings({ volume: 0, brightness: 80, notifications: false, username: "Alice" });
// { volume: 0, brightness: 80, notifications: false, username: "Alice" } ✅

// Missing settings use defaults:
applyUserSettings({});
// { volume: 50, brightness: 100, notifications: true, username: "Anonymous" } ✅
```

### Nullish Assignment (??=)

```javascript
// Assign a value only if the variable is currently null or undefined:
let config = null;
config ??= { theme: "dark", lang: "en" }; // config is null, so assign
console.log(config); // { theme: "dark", lang: "en" }

let existing = { theme: "light" };
existing ??= { theme: "dark" }; // existing is NOT null/undefined, so no change
console.log(existing); // { theme: "light" } — unchanged ✅
```

---

## Optional Chaining (?.)

### Definition

The **optional chaining operator** `?.` lets you safely access nested properties of an object without getting an error if an intermediate property is `null` or `undefined`. Instead of throwing a `TypeError`, it short-circuits and returns `undefined`.

### Why It Exists

In real applications, data often comes from APIs, databases, or user input — and it might be incomplete or missing. Accessing a property on `null` or `undefined` crashes your program. Before optional chaining, you had to write lengthy defensive checks.

```javascript
// THE PROBLEM — accessing nested properties safely (old way):
let user = null;

// Without optional chaining — crashes!
// console.log(user.address.city); // ❌ TypeError: Cannot read property 'address' of null

// Old defensive code — ugly and verbose:
let city1 = user && user.address && user.address.city;
console.log(city1); // null (short-circuits safely, but messy)

// WITH optional chaining — clean and safe:
let city2 = user?.address?.city;
console.log(city2); // undefined (no error! ✅)
```

### Syntax Forms

```javascript
// Property access:
obj?.property

// Computed property access (with variable key):
obj?.[expression]

// Method call:
obj?.method()

// Combined:
obj?.nested?.property?.method?.()
```

### Examples

```javascript
let user = {
  name: "Alice",
  address: {
    city: "London",
    zip: "SW1A 1AA"
  },
  getGreeting() {
    return `Hello, I'm ${this.name}!`;
  }
};

// Safe property access:
console.log(user?.name);             // "Alice"
console.log(user?.address?.city);    // "London"
console.log(user?.phone?.number);    // undefined (phone doesn't exist — no crash!)
console.log(user?.address?.country); // undefined (country doesn't exist)

// Safe method calls:
console.log(user?.getGreeting());    // "Hello, I'm Alice!"
console.log(user?.nonExistent?.());  // undefined (no crash)

// With null user:
let noUser = null;
console.log(noUser?.name);           // undefined ✅ (no crash)
console.log(noUser?.getGreeting?.()); // undefined ✅

// With arrays:
let data = { items: [1, 2, 3] };
console.log(data?.items?.[0]);        // 1
console.log(data?.missing?.[0]);      // undefined ✅

// Combined with ?? for defaults:
let config = null;
let theme = config?.settings?.theme ?? "light";
console.log(theme); // "light" (config is null, optional chain returns undefined, ?? gives "light")
```

### Real-World Example: API Response Handling

```javascript
// Handling potentially incomplete API response data:
function displayUserProfile(apiResponse) {
  // The API might return incomplete data — handle it safely:
  const name = apiResponse?.user?.profile?.fullName ?? "Unknown User";
  const email = apiResponse?.user?.contact?.email ?? "No email provided";
  const city = apiResponse?.user?.address?.city ?? "Location not set";
  const premiumBadge = apiResponse?.user?.subscription?.isPremium
    ? "⭐ Premium Member"
    : "Free Member";
  const lastLogin = apiResponse?.user?.activity?.lastLogin?.toLocaleDateString?.()
    ?? "Never logged in";

  console.log(`
    Name:    ${name}
    Email:   ${email}
    City:    ${city}
    Status:  ${premiumBadge}
    Last:    ${lastLogin}
  `);
}

// Complete response:
displayUserProfile({
  user: {
    profile: { fullName: "Alice Smith" },
    contact: { email: "alice@example.com" },
    address: { city: "London" },
    subscription: { isPremium: true },
    activity: { lastLogin: new Date("2024-01-15") }
  }
});

// Incomplete response (real-world scenario):
displayUserProfile({ user: null });
displayUserProfile(null);
displayUserProfile({});
// All produce: Unknown User, No email provided, Location not set, Free Member, Never logged in
```

---
## What is Control Flow?

### Definition

**Control flow** is the order in which JavaScript executes statements in your code. By default, JavaScript runs code from top to bottom, one line at a time. **Control flow structures** let you change that — jumping over some code, repeating other code, or making decisions about what to run.

### Why Control Flow Exists

A program without control flow can only do one fixed thing. Every useful program needs to:
- **Branch**: do *this* if condition A is true, do *that* if condition B is true
- **Loop**: repeat an action until something changes
- **Skip**: jump past code that shouldn't run in this situation

Without control flow, programming would be impossible for any real-world task.

```
Default (no control flow):
Line 1 → Line 2 → Line 3 → Line 4 → Done

With branching (if/else):
Line 1 → Check condition →
           YES → Line 2A → Line 3 → Done
           NO  → Line 2B → Line 3 → Done

With looping (for):
Line 1 → Line 2 (repeat 5 times) → Line 3 → Done
```

---

## if / else Statements

### Definition

An `if` statement checks a condition and runs a block of code **only if** that condition is truthy. `else` provides an alternative block to run when the condition is falsy. `else if` lets you chain multiple conditions.

### Why It Exists

Making decisions is the most fundamental thing a program does. Every interactive feature — login validation, age verification, price calculation, game logic — relies on `if/else` to choose between different paths.

### Syntax

```javascript
// Basic if:
if (condition) {
  // code to run when condition is truthy
}

// if / else:
if (condition) {
  // runs when condition is truthy
} else {
  // runs when condition is falsy
}

// if / else if / else:
if (condition1) {
  // runs when condition1 is truthy
} else if (condition2) {
  // runs when condition1 is false AND condition2 is truthy
} else if (condition3) {
  // runs when condition1 and condition2 are false AND condition3 is truthy
} else {
  // runs when ALL conditions above are false
}
```

### Simple Example

```javascript
let temperature = 35; // degrees Celsius

if (temperature > 30) {
  console.log("It's hot! Stay hydrated.");
} else if (temperature > 20) {
  console.log("Nice weather. Enjoy it!");
} else if (temperature > 10) {
  console.log("A bit chilly. Bring a jacket.");
} else {
  console.log("It's cold! Bundle up.");
}
// Output: "It's hot! Stay hydrated."
```

### How JavaScript Evaluates if/else Internally

```
1. JavaScript evaluates the condition in parentheses: (temperature > 30)
2. The result is: true (35 > 30 is true)
3. Since the result is truthy, the first block runs
4. All other else if / else blocks are SKIPPED — they are never even checked
5. Execution continues after the entire if/else chain
```

This means in a chain of `if / else if / else`, **only ONE block ever runs** — the first one whose condition is truthy.

```javascript
// Demonstration — only the FIRST truthy condition runs:
let score = 85;

if (score >= 50) {
  console.log("Pass"); // This runs
} else if (score >= 70) {
  console.log("Good"); // This is SKIPPED — even though 85 >= 70, the first matched already!
} else if (score >= 90) {
  console.log("Excellent"); // SKIPPED
}
// Output: "Pass" — the grades are in the wrong order!

// ✅ Correct order — check most specific condition first:
if (score >= 90) {
  console.log("Excellent");
} else if (score >= 70) {
  console.log("Good");      // This now runs for score 85 ✅
} else if (score >= 50) {
  console.log("Pass");
} else {
  console.log("Fail");
}
// Output: "Good"
```

### Real-World Example: E-Commerce Discount System

```javascript
// A tiered discount system:
function calculateDiscount(customer) {
  let discountPercent;
  let reason;

  if (customer.isPremium && customer.totalSpent >= 1000) {
    // Premium customers who have spent $1000+ get 30% off
    discountPercent = 30;
    reason = "Premium VIP discount";
  } else if (customer.isPremium) {
    // All other premium customers get 20% off
    discountPercent = 20;
    reason = "Premium member discount";
  } else if (customer.totalSpent >= 500) {
    // High-spending regular customers get 10% off
    discountPercent = 10;
    reason = "Loyalty discount";
  } else if (customer.isFirstOrder) {
    // First-time customers get 5% off
    discountPercent = 5;
    reason = "Welcome discount";
  } else {
    // Everyone else gets no discount
    discountPercent = 0;
    reason = "No discount applicable";
  }

  return { discountPercent, reason };
}

let customer1 = { isPremium: true, totalSpent: 1500, isFirstOrder: false };
let customer2 = { isPremium: false, totalSpent: 0, isFirstOrder: true };
let customer3 = { isPremium: false, totalSpent: 750, isFirstOrder: false };

console.log(calculateDiscount(customer1));
// { discountPercent: 30, reason: "Premium VIP discount" }

console.log(calculateDiscount(customer2));
// { discountPercent: 5, reason: "Welcome discount" }

console.log(calculateDiscount(customer3));
// { discountPercent: 10, reason: "Loyalty discount" }
```

### Guard Clauses — A Better Way to Write Conditionals

A **guard clause** is a technique where you check for invalid or edge-case conditions at the **beginning** of a function and return early, instead of nesting your main logic deep inside `if` statements.

```javascript
// ❌ DEEPLY NESTED approach (hard to read):
function processOrder(user, cart, paymentMethod) {
  if (user) {
    if (user.isActive) {
      if (cart && cart.items.length > 0) {
        if (paymentMethod && paymentMethod.isValid) {
          // The actual logic is buried 4 levels deep!
          let total = cart.items.reduce((sum, item) => sum + item.price, 0);
          console.log(`Processing order for ${user.name}: $${total}`);
          return { success: true, total };
        } else {
          console.error("Invalid payment method");
          return { success: false };
        }
      } else {
        console.error("Cart is empty");
        return { success: false };
      }
    } else {
      console.error("User account is not active");
      return { success: false };
    }
  } else {
    console.error("No user provided");
    return { success: false };
  }
}

// ✅ GUARD CLAUSE approach (clean and readable):
function processOrder(user, cart, paymentMethod) {
  // Guard clause 1: Check each invalid condition upfront and return EARLY
  if (!user) {
    console.error("No user provided");
    return { success: false };
  }

  if (!user.isActive) {
    console.error("User account is not active");
    return { success: false };
  }

  if (!cart || cart.items.length === 0) {
    console.error("Cart is empty");
    return { success: false };
  }

  if (!paymentMethod || !paymentMethod.isValid) {
    console.error("Invalid payment method");
    return { success: false };
  }

  // Main logic is now at the TOP LEVEL — easy to read:
  let total = cart.items.reduce((sum, item) => sum + item.price, 0);
  console.log(`Processing order for ${user.name}: $${total}`);
  return { success: true, total };
}
```

Guard clauses make your code:
- Flatter (less nesting)
- Easier to read
- Easier to debug
- More focused on the "happy path" (the normal case)

---

## The Ternary Operator

### Definition

The **ternary operator** is a compact way to write an `if/else` expression on a single line. It is the only operator in JavaScript that takes **three** operands (hence "ternary" — meaning "three-part").

### Why It Exists

Often you just need to choose between two values based on a condition. Writing a full `if/else` block for this feels overly verbose. The ternary operator is the concise, inline alternative.

### Syntax

```javascript
condition ? valueIfTrue : valueIfFalse
```

Read it as: "If condition is true, give me valueIfTrue; otherwise give me valueIfFalse."

### Simple Example

```javascript
let age = 20;

// Full if/else (5 lines):
let status;
if (age >= 18) {
  status = "Adult";
} else {
  status = "Minor";
}

// Ternary (1 line, same result):
let status2 = age >= 18 ? "Adult" : "Minor";

console.log(status);  // "Adult"
console.log(status2); // "Adult"
```

### Intermediate Examples

```javascript
let score = 75;
let grade = score >= 90 ? "A"
          : score >= 80 ? "B"   // ← Chained ternaries
          : score >= 70 ? "C"
          : score >= 60 ? "D"
          : "F";
console.log(grade); // "C"

// Using ternary for dynamic strings:
let itemCount = 3;
let cartMessage = `You have ${itemCount} ${itemCount === 1 ? "item" : "items"} in your cart.`;
console.log(cartMessage); // "You have 3 items in your cart."

itemCount = 1;
cartMessage = `You have ${itemCount} ${itemCount === 1 ? "item" : "items"} in your cart.`;
console.log(cartMessage); // "You have 1 item in your cart."

// Conditional class names (common in React/UI code):
let isDarkMode = true;
let themeClass = isDarkMode ? "theme-dark" : "theme-light";
console.log(themeClass); // "theme-dark"
```

### Real-World Example

```javascript
// Dynamic button text and behavior:
function renderButton(user) {
  const buttonText = user.isLoggedIn ? "Log Out" : "Log In";
  const buttonColor = user.isLoggedIn ? "red" : "blue";
  const welcomeMsg = user.isLoggedIn
    ? `Welcome back, ${user.name}!`
    : "Please sign in to continue.";

  console.log(`Button: [${buttonText}] (${buttonColor})`);
  console.log(welcomeMsg);
}

renderButton({ isLoggedIn: true, name: "Alice" });
// Button: [Log Out] (red)
// Welcome back, Alice!

renderButton({ isLoggedIn: false, name: "" });
// Button: [Log In] (blue)
// Please sign in to continue.
```

> ⚠️ **Warning:** Avoid deeply chaining ternary operators — they become unreadable quickly. If you have more than two levels of nesting, use a regular `if/else` instead.

```javascript
// ❌ Too nested — confusing:
let result = a > b ? a > c ? "a is biggest" : "c is biggest" : b > c ? "b is biggest" : "c is biggest";

// ✅ Much clearer as if/else:
let biggest;
if (a > b && a > c) biggest = "a is biggest";
else if (b > c) biggest = "b is biggest";
else biggest = "c is biggest";
```

---

## The switch Statement

### Definition

The `switch` statement compares one value against multiple possible cases and runs the matching case's code. It is an alternative to a long chain of `if/else if` when you are comparing **one variable against multiple specific values**.

### Why It Exists

When you have many possible specific values to check (day of the week, HTTP status codes, user roles, keyboard key codes), a series of `if/else if` statements all testing the same variable becomes repetitive. `switch` makes this cleaner.

### Syntax

```javascript
switch (expression) {
  case value1:
    // code for value1
    break;    // ← IMPORTANT: stops execution from falling through

  case value2:
    // code for value2
    break;

  case value3:
  case value4:
    // code for BOTH value3 AND value4 (intentional fall-through)
    break;

  default:
    // code if no case matches (like the final 'else')
    // 'break' here is optional (it's the last case)
}
```

### How Switch Works Internally

```
1. JavaScript evaluates the expression in parentheses once
2. It compares the result using STRICT EQUALITY (===) against each case value
3. When a match is found, execution starts at that case
4. Without 'break', execution FALLS THROUGH to the next case automatically!
5. 'break' exits the switch block entirely
6. 'default' runs if no case matches
```

### Simple Example

```javascript
let dayNumber = 3;
let dayName;

switch (dayNumber) {
  case 1:
    dayName = "Monday";
    break;
  case 2:
    dayName = "Tuesday";
    break;
  case 3:
    dayName = "Wednesday"; // This matches!
    break;
  case 4:
    dayName = "Thursday";
    break;
  case 5:
    dayName = "Friday";
    break;
  case 6:
    dayName = "Saturday";
    break;
  case 7:
    dayName = "Sunday";
    break;
  default:
    dayName = "Invalid day";
}

console.log(dayName); // "Wednesday"
```

### Why switch Uses Strict Equality (===)

This catches many developers off-guard:

```javascript
let input = "1"; // a STRING

switch (input) {
  case 1:           // number 1
    console.log("It's the number 1");
    break;
  case "1":         // string "1"
    console.log("It's the string '1'"); // This matches!
    break;
}
// Output: "It's the string '1'"

// switch uses === — it checks BOTH value AND type!
// "1" === 1 is false (different types)
// "1" === "1" is true ✅
```

### Fall-Through — The Most Important switch Concept

Without a `break`, execution **falls through** to the next case. This is usually a bug, but it can occasionally be used intentionally.

```javascript
// ❌ ACCIDENTAL fall-through (common bug):
let fruit = "apple";

switch (fruit) {
  case "apple":
    console.log("Apples are red");
    // ← FORGOT break!
  case "banana":
    console.log("Bananas are yellow"); // This ALSO runs!
    break;
  case "grape":
    console.log("Grapes are purple");
    break;
}
// Output:
// "Apples are red"
// "Bananas are yellow"  ← Not what we intended!

// ✅ INTENTIONAL fall-through (multiple cases, same code):
let dayOfWeek = "Saturday";

switch (dayOfWeek) {
  case "Saturday":
  case "Sunday":
    // Both Saturday and Sunday fall through to the same code
    console.log("It's the weekend! 🎉");
    break;
  case "Monday":
  case "Tuesday":
  case "Wednesday":
  case "Thursday":
  case "Friday":
    console.log("It's a weekday. 💼");
    break;
  default:
    console.log("Invalid day.");
}
// Output: "It's the weekend! 🎉"
```

### Real-World Example: HTTP Status Code Handler

```javascript
// Handling different API response codes:
function handleHttpResponse(statusCode, data) {
  switch (statusCode) {
    case 200:
    case 201:
      // Both 200 (OK) and 201 (Created) are success responses
      console.log("✅ Success:", data);
      return { success: true, data };

    case 400:
      console.error("❌ Bad Request: The request was invalid.");
      return { success: false, error: "bad_request" };

    case 401:
      console.error("🔒 Unauthorized: Please log in.");
      return { success: false, error: "unauthorized" };

    case 403:
      console.error("🚫 Forbidden: You don't have permission.");
      return { success: false, error: "forbidden" };

    case 404:
      console.error("🔍 Not Found: The resource doesn't exist.");
      return { success: false, error: "not_found" };

    case 429:
      console.error("⏱️ Too Many Requests: Please slow down.");
      return { success: false, error: "rate_limited" };

    case 500:
    case 502:
    case 503:
      // Server errors
      console.error("💥 Server Error: Something went wrong on our end.");
      return { success: false, error: "server_error" };

    default:
      console.warn(`⚠️ Unexpected status code: ${statusCode}`);
      return { success: false, error: "unknown" };
  }
}

console.log(handleHttpResponse(201, { id: 1, name: "New Item" }));
// ✅ Success: { id: 1, name: 'New Item' }
// { success: true, data: { id: 1, name: 'New Item' } }

console.log(handleHttpResponse(404, null));
// 🔍 Not Found: The resource doesn't exist.
// { success: false, error: 'not_found' }
```

### switch vs if/else — When to Use Which

| Use `switch` when | Use `if/else` when |
|---|---|
| Comparing ONE variable against MANY specific values | Testing complex conditions or ranges |
| Cases are specific, discrete values | Conditions involve `>`, `<`, `>=`, `<=` |
| Multiple cases share the same code (fall-through) | Conditions test different variables |
| Code readability is improved (e.g., 10+ cases) | You have 1–3 conditions only |

```javascript
// switch is great here (one variable, many discrete values):
switch (errorCode) { /* ... many specific codes ... */ }

// if/else is better here (different variables, ranges):
if (age >= 18 && hasId) { /* ... */ }
else if (balance > 1000) { /* ... */ }
```

---
## Loops

### What Are Loops?

A **loop** is a control flow structure that repeats a block of code multiple times. Instead of writing the same code over and over, you write it once and tell JavaScript how many times (or under what conditions) to repeat it.

### Why Loops Exist

Almost everything in programming involves repetition:
- Process each item in a shopping cart
- Check each character in a password
- Count down from 10 to 0
- Retry a network request up to 5 times
- Display each user in a list

Without loops, you would have to manually write each repetition, which would be impossible for dynamic data.

---

## The for Loop

### Definition

The `for` loop is the most common and controlled loop. It repeats a block of code a **specific number of times**, with precise control over the start, end, and step.

### Why It Exists

When you know exactly how many times you need to repeat something — or you need access to the current index/count — the `for` loop is the perfect tool.

### Syntax

```javascript
for (initialization; condition; update) {
  // code to repeat
}
```

The three parts:
- **Initialization**: runs **once** at the very start — sets up the counter variable
- **Condition**: checked **before each iteration** — if false, the loop stops
- **Update**: runs **after each iteration** — changes the counter for next time

### How the for Loop Executes Step by Step

```javascript
for (let i = 0; i < 3; i++) {
  console.log("Iteration:", i);
}

/*
Step 1: Initialization — let i = 0  (runs ONCE)
Step 2: Check condition — 0 < 3 → true → run the block
        Block runs: "Iteration: 0"
Step 3: Update — i++ → i becomes 1
Step 4: Check condition — 1 < 3 → true → run the block
        Block runs: "Iteration: 1"
Step 5: Update — i++ → i becomes 2
Step 6: Check condition — 2 < 3 → true → run the block
        Block runs: "Iteration: 2"
Step 7: Update — i++ → i becomes 3
Step 8: Check condition — 3 < 3 → false → STOP, exit loop
*/
```

### Simple Example

```javascript
// Count from 1 to 5:
for (let i = 1; i <= 5; i++) {
  console.log(i);
}
// 1
// 2
// 3
// 4
// 5

// Count DOWN from 5 to 1:
for (let i = 5; i >= 1; i--) {
  console.log(i);
}
// 5, 4, 3, 2, 1

// Count by 2s:
for (let i = 0; i <= 10; i += 2) {
  console.log(i);
}
// 0, 2, 4, 6, 8, 10
```

### Looping Through Arrays

```javascript
let fruits = ["apple", "banana", "cherry", "date"];

// Using index to access each item:
for (let i = 0; i < fruits.length; i++) {
  console.log(`Item ${i}: ${fruits[i]}`);
}
// Item 0: apple
// Item 1: banana
// Item 2: cherry
// Item 3: date
```

### Real-World Example: Grade Calculator

```javascript
// Calculate class statistics:
let grades = [72, 88, 95, 64, 91, 78, 85, 69, 94, 88];

let total = 0;
let highest = grades[0]; // Start with first grade as initial highest
let lowest = grades[0];  // Start with first grade as initial lowest
let passingCount = 0;

for (let i = 0; i < grades.length; i++) {
  let grade = grades[i];

  total += grade; // Add to running total

  // Track highest and lowest:
  if (grade > highest) highest = grade;
  if (grade < lowest) lowest = grade;

  // Count passing grades (60 and above):
  if (grade >= 60) passingCount++;
}

let average = total / grades.length;
let passingRate = (passingCount / grades.length) * 100;

console.log(`Students:     ${grades.length}`);
console.log(`Average:      ${average.toFixed(1)}`);      // 82.4
console.log(`Highest:      ${highest}`);                  // 95
console.log(`Lowest:       ${lowest}`);                   // 64
console.log(`Passing rate: ${passingRate.toFixed(1)}%`);  // 100.0%
```

### Nested for Loops

You can put a loop inside another loop. The inner loop runs completely for each iteration of the outer loop.

```javascript
// Multiplication table (3x3):
for (let row = 1; row <= 3; row++) {
  let rowOutput = "";
  for (let col = 1; col <= 3; col++) {
    rowOutput += `${row * col}\t`; // \t is a tab character
  }
  console.log(rowOutput);
}
// 1    2    3
// 2    4    6
// 3    6    9

// Pattern printing:
for (let i = 1; i <= 5; i++) {
  let stars = "";
  for (let j = 1; j <= i; j++) {
    stars += "★";
  }
  console.log(stars);
}
// ★
// ★★
// ★★★
// ★★★★
// ★★★★★
```

---

## The while Loop

### Definition

The `while` loop repeats a block of code **as long as a condition is truthy**. Unlike `for`, it doesn't have a built-in counter — it just keeps going while the condition is true.

### Why It Exists

Sometimes you don't know in advance how many times you need to loop. "Keep retrying until the server responds." "Keep reading user input until they type 'quit'." "Keep shuffling until the array is randomized." These situations need a `while` loop.

### Syntax

```javascript
while (condition) {
  // code to repeat
  // IMPORTANT: something inside must eventually make the condition false!
}
```

### How while Executes Internally

```
1. Check the condition
2. If truthy → run the block → go back to step 1
3. If falsy → exit the loop
```

### Simple Example

```javascript
let count = 1;

while (count <= 5) {
  console.log(count);
  count++; // ← CRITICAL: without this, count never changes and loop runs forever!
}
// 1, 2, 3, 4, 5

// Count down:
let countdown = 5;
while (countdown > 0) {
  console.log(countdown);
  countdown--;
}
console.log("Blast off! 🚀");
// 5, 4, 3, 2, 1, Blast off!
```

### The Infinite Loop Danger

```javascript
// ❌ INFINITE LOOP — NEVER DO THIS (your browser/program will freeze!):
let x = 1;
while (x > 0) {
  console.log(x);
  // x is never changed! Condition is always true — loop never ends!
  // x++; ← MUST add this or a similar update
}

// ✅ Safe: always ensure the condition will eventually become false:
let x = 1;
while (x <= 1000000) {
  // ... some work ...
  x++;  // x keeps growing, eventually x > 1000000 and loop stops
}
```

### Real-World Example: User Input Validation Loop

```javascript
// Simulating repeated prompts until valid input:
// (In a real browser, prompt() would be used; here we simulate with a function)
function simulateUserInput(attempts) {
  // Simulated responses: first two are invalid, third is valid
  let responses = ["", "   ", "Alice"];
  return responses[Math.min(attempts, 2)];
}

let userName = "";
let attemptCount = 0;
const MAX_ATTEMPTS = 5;

while (!userName.trim() && attemptCount < MAX_ATTEMPTS) {
  userName = simulateUserInput(attemptCount);
  attemptCount++;

  if (!userName.trim()) {
    console.log(`Attempt ${attemptCount}: Name cannot be empty. Please try again.`);
  }
}

if (userName.trim()) {
  console.log(`Welcome, ${userName.trim()}!`); // Welcome, Alice!
} else {
  console.log("Too many failed attempts. Please refresh and try again.");
}
```

### Retry Pattern with while

```javascript
// Retry a network request up to 3 times:
async function fetchWithRetry(url, maxRetries = 3) {
  let attempt = 0;
  let lastError;

  while (attempt < maxRetries) {
    try {
      let response = await fetch(url);
      if (response.ok) {
        return await response.json(); // Success! Exit loop.
      }
      throw new Error(`HTTP ${response.status}`);
    } catch (error) {
      lastError = error;
      attempt++;
      console.warn(`Attempt ${attempt} failed: ${error.message}. Retrying...`);
      // Wait 1 second between retries:
      await new Promise(resolve => setTimeout(resolve, 1000));
    }
  }

  throw new Error(`All ${maxRetries} attempts failed. Last error: ${lastError.message}`);
}
```

---

## The do...while Loop

### Definition

The `do...while` loop is similar to `while`, but it **always runs the block at least once** before checking the condition. The condition is checked *after* each iteration, not before.

### Why It Exists

Sometimes you need to execute the code at least once, and then continue based on a condition. A common example: show a menu, get user input, then decide whether to show it again.

### Syntax

```javascript
do {
  // code runs at LEAST ONCE
} while (condition);
// Note the semicolon at the end — it's required
```

### How do...while Executes

```
1. Run the block (always, unconditionally)
2. Check the condition
3. If truthy → go back to step 1
4. If falsy → exit the loop
```

### Simple Example

```javascript
// while: might not run at all
let x = 10;
while (x < 5) {
  console.log("while: This never runs — condition is false from start");
  x++;
}

// do...while: always runs at least once
let y = 10;
do {
  console.log("do...while: This RUNS ONCE even though condition is false from start!");
  y++;
} while (y < 5);

// Output: "do...while: This RUNS ONCE even though condition is false from start!"
```

### Real-World Example: Interactive Menu

```javascript
// A menu that always shows at least once and repeats until user quits:
function showMenu() {
  // Simulate user choices: first visit "Add Item", second "View Cart", third "Quit"
  let choices = ["add", "view", "quit"];
  let choiceIndex = 0;

  let choice;

  do {
    // Simulate getting user input:
    choice = choices[choiceIndex++];
    console.log(`User chose: ${choice}`);

    switch (choice) {
      case "add":
        console.log("  → Item added to cart!");
        break;
      case "view":
        console.log("  → Showing cart contents...");
        break;
      case "remove":
        console.log("  → Item removed from cart.");
        break;
      case "quit":
        console.log("  → Goodbye!");
        break;
      default:
        console.log("  → Invalid choice. Please try again.");
    }

  } while (choice !== "quit"); // Repeat until user chooses to quit
}

showMenu();
// User chose: add
//   → Item added to cart!
// User chose: view
//   → Showing cart contents...
// User chose: quit
//   → Goodbye!
```

---
## The for...of Loop

### Definition

The `for...of` loop iterates over the **values** of any iterable — arrays, strings, Maps, Sets, and more. It is the cleanest way to loop through collections when you only need the values (not the index).

### Why It Exists

The traditional `for` loop with an index is powerful but verbose. When you just want to look at each item in a list without caring about the index number, `for...of` is far cleaner and less error-prone.

### Syntax

```javascript
for (const item of iterable) {
  // item = current element's VALUE
  // use 'const' because item doesn't need to be reassigned
}
```

### Simple Examples

```javascript
// Arrays:
let colors = ["red", "green", "blue"];

for (const color of colors) {
  console.log(color);
}
// red
// green
// blue

// Strings (iterates character by character):
let word = "hello";
for (const char of word) {
  console.log(char);
}
// h, e, l, l, o

// Numbers: Sum all elements
let numbers = [10, 20, 30, 40, 50];
let sum = 0;
for (const num of numbers) {
  sum += num;
}
console.log(sum); // 150

// Getting both index AND value with entries():
let fruits = ["apple", "banana", "cherry"];
for (const [index, fruit] of fruits.entries()) {
  console.log(`${index}: ${fruit}`);
}
// 0: apple
// 1: banana
// 2: cherry
```

### for...of with Other Iterables

```javascript
// Set (collection of unique values):
let uniqueColors = new Set(["red", "blue", "red", "green", "blue"]);
console.log(uniqueColors); // Set { 'red', 'blue', 'green' } (duplicates removed)

for (const color of uniqueColors) {
  console.log(color);
}
// red, blue, green

// Map (key-value pairs):
let prices = new Map([
  ["apple", 0.99],
  ["banana", 0.49],
  ["cherry", 2.99]
]);

for (const [fruit, price] of prices) {
  console.log(`${fruit}: $${price}`);
}
// apple: $0.99
// banana: $0.49
// cherry: $2.99
```

### Real-World Example: Cart Processor

```javascript
// Processing shopping cart items:
const cart = [
  { name: "Laptop",  price: 999, quantity: 1 },
  { name: "Mouse",   price: 29,  quantity: 2 },
  { name: "Keyboard",price: 79,  quantity: 1 },
  { name: "Monitor", price: 349, quantity: 1 }
];

let cartTotal = 0;
let itemSummaries = [];

for (const item of cart) {
  let itemTotal = item.price * item.quantity;
  cartTotal += itemTotal;

  itemSummaries.push(
    `${item.name} x${item.quantity} = $${itemTotal.toFixed(2)}`
  );
}

console.log("=== Order Summary ===");
for (const summary of itemSummaries) {
  console.log(`  ${summary}`);
}
console.log(`Total: $${cartTotal.toFixed(2)}`);

// === Order Summary ===
//   Laptop x1 = $999.00
//   Mouse x2 = $58.00
//   Keyboard x1 = $79.00
//   Monitor x1 = $349.00
// Total: $1485.00
```

---

## The for...in Loop

### Definition

The `for...in` loop iterates over the **enumerable property keys** (not values) of an object. It gives you the property names, one by one.

### Why It Exists

Sometimes you need to work with an object when you don't know in advance what properties it has — for example, when processing dynamic API responses, cloning objects, or debugging by printing all properties.

### Syntax

```javascript
for (const key in object) {
  // key = current property NAME (as a string)
  // object[key] = the value of that property
}
```

### Simple Example

```javascript
let person = {
  name: "Alice",
  age: 25,
  city: "London",
  role: "Developer"
};

for (const key in person) {
  console.log(`${key}: ${person[key]}`);
}
// name: Alice
// age: 25
// city: London
// role: Developer
```

### ⚠️ Why for...in is Dangerous on Arrays

`for...in` on arrays gives you the **index as a string**, not the actual values. Worse, it also iterates over any custom properties added to the Array prototype — which can cause mysterious bugs.

```javascript
// ❌ Using for...in on an array — AVOID THIS:
let colors = ["red", "green", "blue"];

// Someone adds a custom property to Array prototype (happens in old libraries):
Array.prototype.customProp = "oops";

for (const i in colors) {
  console.log(i, colors[i]);
}
// "0" "red"
// "1" "green"
// "2" "blue"
// "customProp" "oops"  ← This was added to Array.prototype! for...in finds it!

delete Array.prototype.customProp; // cleanup for this demo

// ✅ Use for...of for arrays:
for (const color of colors) {
  console.log(color);
}
// red, green, blue  (no surprises!)

// ✅ Or the classic for loop:
for (let i = 0; i < colors.length; i++) {
  console.log(i, colors[i]);
}
```

### When for...in IS Appropriate

```javascript
// ✅ for...in is appropriate for plain objects:
let settings = {
  theme: "dark",
  language: "en",
  fontSize: 16,
  notifications: true
};

// Print all settings:
for (const key in settings) {
  console.log(`${key} = ${settings[key]}`);
}

// Check if object has a specific property:
for (const key in settings) {
  if (key === "theme") {
    console.log("Theme setting found:", settings[key]);
  }
}

// Clone an object's own properties (hasOwnProperty check for safety):
let clone = {};
for (const key in settings) {
  if (settings.hasOwnProperty(key)) { // Only own properties, not inherited ones
    clone[key] = settings[key];
  }
}
console.log(clone);
```

### for...in vs for...of Quick Comparison

| Feature | `for...in` | `for...of` |
|---|---|---|
| **Iterates over** | Object property KEYS (strings) | Iterable VALUES |
| **Works on objects?** | ✅ Yes | ❌ No (plain objects are not iterable) |
| **Works on arrays?** | ⚠️ Yes, but dangerous | ✅ Yes, preferred |
| **Works on strings?** | ⚠️ Yes, gives index | ✅ Yes, gives characters |
| **Includes inherited props?** | ⚠️ Yes (can cause bugs) | N/A |
| **Recommended for arrays?** | ❌ No | ✅ Yes |
| **Recommended for objects?** | ✅ Yes (with caution) | ❌ No |

---

## break and continue

### break — Exit the Loop Immediately

`break` immediately terminates the entire loop and continues with the code after it. It is like an emergency exit.

### Why break Exists

Sometimes you find what you're looking for before reaching the end of a loop. There's no reason to keep iterating — breaking out saves time and makes intent clear.

```javascript
// Find the first even number:
let numbers = [3, 7, 11, 4, 9, 16, 2];
let firstEven = null;

for (const num of numbers) {
  if (num % 2 === 0) {
    firstEven = num;
    break; // Found it! Stop the loop — no need to check the rest.
  }
}
console.log("First even number:", firstEven); // 4

// Without break, it would continue checking 9, 16, 2 unnecessarily
```

### continue — Skip to Next Iteration

`continue` skips the **rest of the current iteration** and jumps to the next one. It does not exit the loop — it just skips one round.

### Why continue Exists

Sometimes you want to skip certain items in a loop without stopping the entire loop. "Process all products except the ones that are out of stock."

```javascript
// Print only odd numbers (skip even ones):
for (let i = 1; i <= 10; i++) {
  if (i % 2 === 0) {
    continue; // Skip this iteration — go to next i
  }
  console.log(i); // Only reaches here for odd numbers
}
// 1, 3, 5, 7, 9

// Skip invalid data entries:
let data = [42, null, 17, undefined, 8, null, 99];

let validNumbers = [];
for (const item of data) {
  if (item === null || item === undefined) {
    console.warn("Skipping invalid entry:", item);
    continue; // Skip to next item
  }
  validNumbers.push(item); // Only valid numbers reach here
}
console.log(validNumbers); // [42, 17, 8, 99]
```

### break in switch (reminder)

```javascript
// break is also required in switch statements to prevent fall-through:
switch (value) {
  case 1:
    console.log("One");
    break; // Without this, execution falls through to case 2!
  case 2:
    console.log("Two");
    break;
}
```

### Real-World Example: Search with break, Filter with continue

```javascript
// Product search system:
let products = [
  { id: 1, name: "Laptop",   price: 999, inStock: true  },
  { id: 2, name: "Phone",    price: 699, inStock: false },
  { id: 3, name: "Tablet",   price: 449, inStock: true  },
  { id: 4, name: "Watch",    price: 299, inStock: false },
  { id: 5, name: "Earbuds",  price: 149, inStock: true  },
];

// Find first product in stock under $500 (break when found):
let affordable = null;
for (const product of products) {
  if (!product.inStock) {
    continue; // Skip out-of-stock products
  }
  if (product.price < 500) {
    affordable = product;
    break; // Found the first one — stop searching
  }
}
console.log("Found:", affordable?.name ?? "None"); // "Tablet"

// Collect all in-stock products (continue to skip out-of-stock):
let inStockProducts = [];
for (const product of products) {
  if (!product.inStock) {
    continue; // Skip this product
  }
  inStockProducts.push(product.name);
}
console.log("In stock:", inStockProducts); // ["Laptop", "Tablet", "Earbuds"]
```

---
## Labeled Loops

### Definition

A **label** is a name you give to a loop, allowing `break` or `continue` to target a specific outer loop instead of the innermost one.

### Why They Exist

In **nested loops**, a plain `break` only exits the **innermost** loop. If you need to break out of an outer loop from inside a nested one, labels make that possible.

### Syntax

```javascript
outerLabel: for (...) {
  innerLabel: for (...) {
    break outerLabel;    // exits the OUTER loop
    continue outerLabel; // skips to next iteration of the OUTER loop
  }
}
```

### Example

```javascript
// Without label: break only exits the inner loop
outer: for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if (i === 1 && j === 1) {
      break outer; // Exits BOTH loops immediately!
    }
    console.log(`i=${i}, j=${j}`);
  }
}
// i=0, j=0
// i=0, j=1
// i=0, j=2
// i=1, j=0
// (stops here when i=1, j=1 — breaks out of OUTER loop)
```

> **Note:** Labeled loops are rarely needed. If you find yourself reaching for a label, consider restructuring your code using functions instead. Labels can make code harder to understand.

---

## Modern Array Iteration

For arrays specifically, JavaScript provides powerful built-in methods that replace explicit loops for common tasks. These are **higher-order functions** — they take a function as an argument and apply it to each element.

### Array.forEach() — Loop Through Each Element

```javascript
let fruits = ["apple", "banana", "cherry"];

fruits.forEach((fruit, index) => {
  console.log(`${index}: ${fruit}`);
});
// 0: apple
// 1: banana
// 2: cherry

// Note: forEach has no return value and you cannot break out of it
```

### Array.map() — Transform Each Element into a New Array

`map()` creates a **new array** by applying a function to every element. The original array is not modified.

```javascript
let numbers = [1, 2, 3, 4, 5];

// Square each number:
let squared = numbers.map(num => num ** 2);
console.log(squared);  // [1, 4, 9, 16, 25]
console.log(numbers);  // [1, 2, 3, 4, 5] — original unchanged!

// Real-world: Format product data for display
let products = [
  { name: "Laptop", price: 999 },
  { name: "Mouse",  price: 29  },
  { name: "Pad",    price: 15  }
];

let displayItems = products.map(product => ({
  label: product.name.toUpperCase(),
  formattedPrice: `$${product.price.toFixed(2)}`
}));

console.log(displayItems);
// [
//   { label: "LAPTOP", formattedPrice: "$999.00" },
//   { label: "MOUSE",  formattedPrice: "$29.00"  },
//   { label: "PAD",    formattedPrice: "$15.00"  }
// ]
```

### Array.filter() — Select Elements That Pass a Test

`filter()` creates a **new array** containing only the elements where the function returns `true`.

```javascript
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Keep only even numbers:
let evens = numbers.filter(num => num % 2 === 0);
console.log(evens); // [2, 4, 6, 8, 10]

// Real-world: Filter available products
let products = [
  { name: "Laptop",  price: 999, inStock: true  },
  { name: "Phone",   price: 699, inStock: false },
  { name: "Tablet",  price: 449, inStock: true  },
  { name: "Watch",   price: 299, inStock: false }
];

let affordable = products.filter(p => p.inStock && p.price < 500);
console.log(affordable.map(p => p.name)); // ["Tablet"]
```

### Array.reduce() — Reduce Array to a Single Value

`reduce()` processes every element and accumulates them into a **single result value**.

```javascript
// Sum all numbers:
let numbers = [10, 20, 30, 40, 50];
let sum = numbers.reduce((accumulator, current) => accumulator + current, 0);
//                        ↑                  ↑                             ↑
//                   running total    current element              starting value

console.log(sum); // 150

// Find the maximum:
let max = numbers.reduce((acc, curr) => curr > acc ? curr : acc, numbers[0]);
console.log(max); // 50

// Real-world: Calculate cart total
let cart = [
  { name: "Laptop", price: 999, qty: 1 },
  { name: "Mouse",  price: 29,  qty: 2 },
  { name: "Pad",    price: 15,  qty: 3 }
];

let cartTotal = cart.reduce((total, item) => total + (item.price * item.qty), 0);
console.log(`Cart total: $${cartTotal.toFixed(2)}`); // $1102.00
```

### Chaining Array Methods

The real power comes from chaining these methods:

```javascript
let orders = [
  { product: "Laptop",  price: 999, status: "shipped",   qty: 1 },
  { product: "Mouse",   price: 29,  status: "pending",   qty: 3 },
  { product: "Tablet",  price: 449, status: "shipped",   qty: 2 },
  { product: "Monitor", price: 349, status: "cancelled", qty: 1 },
  { product: "Keyboard",price: 89,  status: "shipped",   qty: 1 }
];

// Total revenue from shipped orders only:
let shippedRevenue = orders
  .filter(order => order.status === "shipped")  // Keep only shipped
  .map(order => order.price * order.qty)        // Calculate each order's value
  .reduce((total, value) => total + value, 0);  // Sum them all

console.log(`Shipped revenue: $${shippedRevenue}`);
// Shipped: Laptop(999) + Tablet(898) + Keyboard(89) = $1986

// Get names of shipped products sorted alphabetically:
let shippedProducts = orders
  .filter(order => order.status === "shipped")
  .map(order => order.product)
  .sort();

console.log("Shipped products:", shippedProducts);
// ["Keyboard", "Laptop", "Tablet"]
```

---

## Common Patterns

### The FizzBuzz Pattern

FizzBuzz is the most famous coding interview problem. It tests your ability to use loops, conditions, and the modulo operator together.

**Problem:** Print numbers 1 to 100. But for multiples of 3, print "Fizz". For multiples of 5, print "Buzz". For multiples of both 3 and 5, print "FizzBuzz".

```javascript
// The key insight: check for BOTH first (15 = 3×5), then each individually:
for (let i = 1; i <= 100; i++) {
  if (i % 15 === 0) {
    // Must be first! 15 is a multiple of both 3 AND 5
    console.log("FizzBuzz");
  } else if (i % 3 === 0) {
    console.log("Fizz");
  } else if (i % 5 === 0) {
    console.log("Buzz");
  } else {
    console.log(i);
  }
}

// Modern string-building approach (often used in interviews):
for (let i = 1; i <= 100; i++) {
  let output = "";
  if (i % 3 === 0) output += "Fizz";
  if (i % 5 === 0) output += "Buzz";
  console.log(output || i); // If output is empty string (falsy), print i
}

// Output for 1-20:
// 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz,
// 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz
```

### The Guard Clause Pattern (revisited)

```javascript
// Pattern: Return early to reduce nesting
function sendEmail(to, subject, body) {
  // Guards — check bad conditions first:
  if (!to)      return { success: false, error: "Recipient required" };
  if (!subject) return { success: false, error: "Subject required" };
  if (!body)    return { success: false, error: "Body required" };
  if (!to.includes("@")) return { success: false, error: "Invalid email address" };

  // Happy path — the main logic:
  console.log(`Sending email to ${to}: "${subject}"`);
  return { success: true };
}

console.log(sendEmail("", "Hello", "Hi!")); // { success: false, error: "Recipient required" }
console.log(sendEmail("alice@test.com", "Hello", "Hi!")); // { success: true }
```

### The Accumulator Pattern

```javascript
// Build up a result by looping and accumulating:
function groupByCategory(products) {
  let grouped = {}; // accumulator — starts empty

  for (const product of products) {
    const category = product.category;

    // If this category hasn't been seen yet, create an empty array for it:
    if (!grouped[category]) {
      grouped[category] = [];
    }

    // Add this product to its category group:
    grouped[category].push(product.name);
  }

  return grouped;
}

let products = [
  { name: "Laptop",     category: "Electronics" },
  { name: "Phone",      category: "Electronics" },
  { name: "Apple",      category: "Food"        },
  { name: "Headphones", category: "Electronics" },
  { name: "Bread",      category: "Food"        },
  { name: "Desk",       category: "Furniture"   }
];

console.log(groupByCategory(products));
// {
//   Electronics: ["Laptop", "Phone", "Headphones"],
//   Food: ["Apple", "Bread"],
//   Furniture: ["Desk"]
// }
```

---

## Best Practices

```javascript
// ✅ 1. Always use === instead of == in comparisons
if (age === 18) { }   // ✅ Strict — predictable
if (age == 18) { }    // ❌ Loose — may coerce types unexpectedly

// ✅ 2. Use const in for...of unless you need to reassign:
for (const item of list) { }   // ✅ item doesn't change each iteration
for (let item of list) { }     // ❌ let is unnecessary here

// ✅ 3. Prefer for...of over for...in on arrays:
for (const item of array) { }   // ✅ Safe, clear
for (const i in array) { }      // ❌ Dangerous, gives string keys

// ✅ 4. Always include break in switch cases (unless intentional fall-through):
switch (x) {
  case 1:
    doSomething();
    break; // ✅ Always add this
}

// ✅ 5. Always update the loop variable to prevent infinite loops:
let i = 0;
while (i < 10) {
  i++; // ✅ Loop will eventually end
}

// ✅ 6. Use guard clauses to reduce nesting:
function process(data) {
  if (!data) return; // ✅ Exit early — avoid nesting
  // ... main logic at top level
}

// ✅ 7. Use ?? instead of || for default values when 0 and false are valid:
let volume = userVolume ?? 50; // ✅ 0 is a valid volume
let name = userName || "Guest"; // ✅ OK here — empty string should use default

// ✅ 8. Use map/filter/reduce for array transformations:
let doubled = numbers.map(n => n * 2);     // ✅ Clear intent
let filtered = items.filter(i => i.active); // ✅ Clean and readable

// ✅ 9. Use optional chaining for nested access:
let city = user?.address?.city ?? "Unknown"; // ✅ Safe and concise

// ✅ 10. Always have a 'default' case in switch statements:
switch (status) {
  case "active":   /* ... */ break;
  case "inactive": /* ... */ break;
  default:
    console.warn("Unexpected status:", status); // ✅ Handle unexpected values
}
```

---

## Common Mistakes

### Mistake 1: Wrong Order in if/else if Chains

```javascript
// ❌ Wrong — conditions overlap, first one catches everything:
let score = 95;
if (score >= 50) {
  console.log("Pass"); // This runs for 95 — but it should be "Excellent"!
} else if (score >= 90) {
  console.log("Excellent"); // Never reached for high scores!
}

// ✅ Correct — most specific condition first:
if (score >= 90) {
  console.log("Excellent"); // Runs for 95 ✅
} else if (score >= 50) {
  console.log("Pass");
}
```

### Mistake 2: Missing break in switch

```javascript
// ❌ Missing break causes unintended fall-through:
switch (day) {
  case "Monday":
    console.log("Start of week");
    // Forgot break!
  case "Tuesday":
    console.log("Second day"); // This ALSO runs when day is "Monday"!
    break;
}

// ✅ Always add break (unless fall-through is intentional and documented):
switch (day) {
  case "Monday":
    console.log("Start of week");
    break; // ✅
  case "Tuesday":
    console.log("Second day");
    break;
}
```

### Mistake 3: Infinite Loops

```javascript
// ❌ Loop variable never changes:
let count = 0;
while (count < 5) {
  console.log(count);
  // Forgot count++! Infinite loop!
}

// ❌ Condition is always true:
while (true) {
  // No break statement inside! Infinite loop!
}

// ✅ Always ensure the loop will terminate:
let count = 0;
while (count < 5) {
  console.log(count);
  count++; // ✅ Loop variable is updated
}
```

### Mistake 4: Using for...in on Arrays

```javascript
// ❌ for...in on arrays:
let arr = [10, 20, 30];
for (const i in arr) {
  console.log(typeof i); // "string" — index is a string, not a number!
  console.log(arr[i]);
}

// ✅ Use for...of instead:
for (const value of arr) {
  console.log(value); // 10, 20, 30
}
```

### Mistake 5: Modifying an Array While Iterating It

```javascript
// ❌ Dangerous: removing items while looping can skip elements:
let numbers = [1, 2, 3, 4, 5];
for (let i = 0; i < numbers.length; i++) {
  if (numbers[i] % 2 === 0) {
    numbers.splice(i, 1); // Removing element shifts indices!
    // i++ still runs, so you skip the next element!
  }
}
console.log(numbers); // [1, 3, 5] — looks right by accident here, but is fragile

// ✅ Better: use filter to create a new array:
let odds = numbers.filter(n => n % 2 !== 0);
console.log(odds); // [1, 3, 5] ✅ Reliable
```

### Mistake 6: Not Understanding Short-Circuit with Side Effects

```javascript
// ❌ Unexpected: second function might not run
function riskyCheck() {
  console.log("riskyCheck ran!");
  return false;
}

function importantSetup() {
  console.log("Setup ran!"); // ← This WON'T run if riskyCheck() returns false
  return true;
}

let result = riskyCheck() && importantSetup();
// "riskyCheck ran!" — printed
// "Setup ran!" — NOT printed (short-circuited by false)

// ✅ If importantSetup must always run, call it separately:
let check = riskyCheck();
let setup = importantSetup(); // Always runs
let result2 = check && setup;
```

---
## Interview Points

> **📌 Interview Point 1: What is the difference between == and === in JavaScript?**

**Answer:** `==` (loose equality) performs type coercion before comparing — it converts operands to the same type, which can lead to surprising results like `1 == "1"` being `true`. `===` (strict equality) compares both the value and the type with no coercion — `1 === "1"` is `false`. Always use `===` because it is predictable and prevents coercion-related bugs.

---

> **📌 Interview Point 2: How does short-circuit evaluation work with && and ||?**

**Answer:**
- `&&` returns the **first falsy value**, or the last value if all are truthy. It stops evaluating as soon as it finds a falsy value.
- `||` returns the **first truthy value**, or the last value if all are falsy. It stops evaluating as soon as it finds a truthy value.
- This is used for patterns like `config && config.timeout` (safe access) and `value || "default"` (fallback values).

---

> **📌 Interview Point 3: What is the difference between ?? and ||?**

**Answer:**
- `||` returns the right side if the left side is any **falsy** value (`false`, `0`, `""`, `null`, `undefined`, `NaN`)
- `??` returns the right side **only** if the left side is `null` or `undefined`
- `??` is better when `0`, `false`, or `""` are valid values that shouldn't trigger a default.

---

> **📌 Interview Point 4: Why does switch use strict equality (===)?**

**Answer:** JavaScript's `switch` statement uses strict equality (`===`) when comparing the expression to each case value. This means both the value AND the type must match. So `switch (1)` will NOT match `case "1"` because `1 === "1"` is `false`. This is actually safer than `==`, but it catches developers off guard when working with user input (which is always a string from form elements).

---

> **📌 Interview Point 5: What is the difference between break and continue?**

**Answer:**
- `break` exits the **entire loop** immediately. Execution continues with the code after the loop.
- `continue` skips the **rest of the current iteration** and jumps to the next one. The loop itself continues running.

---

> **📌 Interview Point 6: Why is for...in dangerous on arrays?**

**Answer:** `for...in` iterates over all **enumerable properties** of an object, including inherited properties from the prototype chain. On arrays, it gives you the index as a **string** (not a number), and if any library has added properties to `Array.prototype`, those will also be iterated — causing unexpected bugs. Use `for...of` for arrays, which only iterates over the actual values.

---

> **📌 Interview Point 7: What is a guard clause and why is it used?**

**Answer:** A guard clause is an early `return` statement at the beginning of a function that checks for invalid or edge-case inputs. Instead of wrapping the main logic in deeply nested `if` statements, you return early for the "bad" cases and keep the main logic flat and readable at the top level. It improves readability, reduces nesting, and makes debugging easier.

---

> **📌 Interview Point 8: What is the difference between for...of and for...in?**

**Answer:**
- `for...in` iterates over the **enumerable property keys** (names) of an object. Good for plain objects. Dangerous for arrays.
- `for...of` iterates over the **iterable values** of a collection (arrays, strings, Maps, Sets). Preferred for arrays and other iterables.
- Plain objects are NOT iterable, so `for...of` cannot be used on them directly.

---

> **📌 Interview Point 9: What does the optional chaining operator (?.) do?**

**Answer:** `?.` allows you to safely access nested properties of an object without throwing a `TypeError` if an intermediate value is `null` or `undefined`. Instead of crashing, it short-circuits and returns `undefined`. Example: `user?.address?.city` returns `undefined` if `user` or `address` is null/undefined, instead of throwing an error.

---

> **📌 Interview Point 10: Explain the difference between while and do...while.**

**Answer:**
- `while` checks the condition **before** running the block. If the condition is initially false, the block **never runs**.
- `do...while` checks the condition **after** running the block. The block **always runs at least once**, then repeats while the condition is true. Used when you need to guarantee at least one execution, like showing a menu or making an initial request.

---

## Exercises

---

### Exercise 1: Operator Output Prediction ⭐

**Task:** Predict the output of each expression before running the code. Write your predictions, then verify.

```javascript
// Part A — Arithmetic:
console.log(15 % 4);
console.log(2 ** 10);
console.log(10 / 3);
let a = 5;
console.log(a++);
console.log(a);
console.log(++a);
console.log(a);

// Part B — Comparison:
console.log("10" > "9");
console.log(10 > 9);
console.log("5" === 5);
console.log(null == undefined);
console.log(null === undefined);

// Part C — Logical (short-circuit):
console.log(0 && "hello");
console.log(1 && "hello");
console.log("" || "default");
console.log("value" || "default");
console.log(null ?? "fallback");
console.log(0 ?? "fallback");
console.log(0 || "fallback");
```

<details>
<summary>✅ Solution (click to reveal)</summary>

```javascript
// Part A:
console.log(15 % 4);    // 3 (15 = 3×4 + 3, remainder is 3)
console.log(2 ** 10);   // 1024 (2 to the power of 10)
console.log(10 / 3);    // 3.3333333333333335

let a = 5;
console.log(a++); // 5 — postfix: returns THEN increments. Returns current value (5)
console.log(a);   // 6 — a was incremented after the previous log
console.log(++a); // 7 — prefix: increments THEN returns. Increments to 7, returns 7
console.log(a);   // 7 — a is still 7

// Part B:
console.log("10" > "9");       // false — STRING comparison: "1" < "9" (Unicode values)
console.log(10 > 9);           // true — numeric comparison
console.log("5" === 5);        // false — string vs number, strict equality, different types
console.log(null == undefined); // true — special rule: they are loosely equal
console.log(null === undefined);// false — different types, strict equality

// Part C:
console.log(0 && "hello");     // 0 — 0 is falsy, && returns first falsy value
console.log(1 && "hello");     // "hello" — 1 is truthy, continue; "hello" is last, return it
console.log("" || "default");  // "default" — "" is falsy, || returns first truthy ("default")
console.log("value" || "default"); // "value" — "value" is truthy, || returns it immediately
console.log(null ?? "fallback");// "fallback" — null triggers ??
console.log(0 ?? "fallback");  // 0 — 0 is NOT null/undefined, ?? does not trigger
console.log(0 || "fallback");  // "fallback" — 0 IS falsy, || triggers and returns "fallback"
```

</details>

---

### Exercise 2: if/else Logic — Grade Classifier ⭐⭐

**Task:** Write a function `classifyGrade(score)` that takes a numerical score (0–100) and returns a letter grade with a message, using proper `if/else if/else` logic.

```
90-100  → "A" — "Excellent work!"
80-89   → "B" — "Great job!"
70-79   → "C" — "Good effort!"
60-69   → "D" — "Needs improvement."
0-59    → "F" — "Please see your instructor."
Invalid → Error message for scores below 0 or above 100
```

Test with: `55`, `72`, `88`, `95`, `100`, `-5`, `110`

<details>
<summary>✅ Solution (click to reveal)</summary>

```javascript
function classifyGrade(score) {
  // Guard clauses for invalid input:
  if (typeof score !== "number" || Number.isNaN(score)) {
    return "❌ Invalid input: score must be a number.";
  }
  if (score < 0 || score > 100) {
    return `❌ Invalid score: ${score}. Score must be between 0 and 100.`;
  }

  // Grade classification (most specific range first):
  let grade, message;

  if (score >= 90) {
    grade = "A";
    message = "Excellent work!";
  } else if (score >= 80) {
    grade = "B";
    message = "Great job!";
  } else if (score >= 70) {
    grade = "C";
    message = "Good effort!";
  } else if (score >= 60) {
    grade = "D";
    message = "Needs improvement.";
  } else {
    grade = "F";
    message = "Please see your instructor.";
  }

  return `Score: ${score} → Grade: ${grade} — ${message}`;
}

// Tests:
console.log(classifyGrade(55));   // Score: 55 → Grade: F — Please see your instructor.
console.log(classifyGrade(72));   // Score: 72 → Grade: C — Good effort!
console.log(classifyGrade(88));   // Score: 88 → Grade: B — Great job!
console.log(classifyGrade(95));   // Score: 95 → Grade: A — Excellent work!
console.log(classifyGrade(100));  // Score: 100 → Grade: A — Excellent work!
console.log(classifyGrade(-5));   // ❌ Invalid score: -5. Score must be between 0 and 100.
console.log(classifyGrade(110));  // ❌ Invalid score: 110. Score must be between 0 and 100.
```

</details>

---

### Exercise 3: switch Statement — Season Finder ⭐⭐

**Task:** Write a function `getSeason(month)` that takes a month number (1–12) and returns the season using a `switch` statement. Use fall-through intentionally for months in the same season.

```
December, January, February   → "Winter ❄️"
March, April, May             → "Spring 🌸"
June, July, August            → "Summer ☀️"
September, October, November  → "Autumn 🍂"
Anything else                 → Error message
```

<details>
<summary>✅ Solution (click to reveal)</summary>

```javascript
function getSeason(month) {
  // Guard clause:
  if (typeof month !== "number" || month < 1 || month > 12 || !Number.isInteger(month)) {
    return `❌ Invalid month: ${month}. Please provide a number from 1 to 12.`;
  }

  let season;

  switch (month) {
    case 12:
    case 1:
    case 2:
      // Intentional fall-through: all three months are Winter
      season = "Winter ❄️";
      break;

    case 3:
    case 4:
    case 5:
      season = "Spring 🌸";
      break;

    case 6:
    case 7:
    case 8:
      season = "Summer ☀️";
      break;

    case 9:
    case 10:
    case 11:
      season = "Autumn 🍂";
      break;

    default:
      season = "Unknown"; // Should never reach here due to guard clause
  }

  return `Month ${month} is in ${season}`;
}

// Tests:
console.log(getSeason(1));   // Month 1 is in Winter ❄️
console.log(getSeason(4));   // Month 4 is in Spring 🌸
console.log(getSeason(7));   // Month 7 is in Summer ☀️
console.log(getSeason(10));  // Month 10 is in Autumn 🍂
console.log(getSeason(12));  // Month 12 is in Winter ❄️
console.log(getSeason(0));   // ❌ Invalid month: 0. Please provide a number from 1 to 12.
console.log(getSeason(13));  // ❌ Invalid month: 13. Please provide a number from 1 to 12.
```

</details>

---

### Exercise 4: Loop Sum Calculator ⭐⭐

**Task:** Write a function `analyzeNumbers(numbers)` that takes an array of numbers and uses a `for` loop to calculate and return:
- `sum`: total of all numbers
- `average`: sum divided by count
- `max`: highest number
- `min`: lowest number
- `evenCount`: how many numbers are even
- `oddCount`: how many numbers are odd

Test with: `[4, 7, 2, 9, 1, 8, 3, 6, 5, 10]`

<details>
<summary>✅ Solution (click to reveal)</summary>

```javascript
function analyzeNumbers(numbers) {
  // Guard clause:
  if (!Array.isArray(numbers) || numbers.length === 0) {
    return "❌ Please provide a non-empty array of numbers.";
  }

  // Initialize accumulators:
  let sum = 0;
  let max = numbers[0]; // Start with first element
  let min = numbers[0];
  let evenCount = 0;
  let oddCount = 0;

  // Single loop to gather all statistics:
  for (let i = 0; i < numbers.length; i++) {
    const num = numbers[i];

    sum += num;

    if (num > max) max = num;
    if (num < min) min = num;

    if (num % 2 === 0) {
      evenCount++;
    } else {
      oddCount++;
    }
  }

  const average = sum / numbers.length;

  return {
    count:     numbers.length,
    sum:       sum,
    average:   parseFloat(average.toFixed(2)),
    max:       max,
    min:       min,
    evenCount: evenCount,
    oddCount:  oddCount
  };
}

// Test:
let result = analyzeNumbers([4, 7, 2, 9, 1, 8, 3, 6, 5, 10]);
console.log(result);
// {
//   count:     10,
//   sum:       55,
//   average:   5.5,
//   max:       10,
//   min:       1,
//   evenCount: 5,   (2, 4, 6, 8, 10)
//   oddCount:  5    (1, 3, 5, 7, 9)
// }

// Additional formatting:
console.log(`
  Analyzed ${result.count} numbers:
  Sum:      ${result.sum}
  Average:  ${result.average}
  Max:      ${result.max}
  Min:      ${result.min}
  Even:     ${result.evenCount} numbers
  Odd:      ${result.oddCount} numbers
`);
```

</details>

---

### Exercise 5: Nested Loops + break/continue — Seat Booking ⭐⭐⭐

**Task:** Build a cinema seat finder. You have a 5-row × 8-column seating grid. Some seats are already taken. Write a function `findConsecutiveSeats(bookedSeats, needed)` that finds the first row with `needed` consecutive empty seats and returns the row number and seat numbers. Use nested loops, `break`, and `continue`.

```javascript
// Pre-booked seats (represented as "row-seat" strings):
const booked = ["1-1","1-2","1-3","2-5","2-6","3-1","3-2","3-5","3-6","3-7","4-3","4-4","4-5"];

// Find seats for a group of 3:
findConsecutiveSeats(booked, 3);
// Expected: Row 1, seats 4-5-6 (first available block of 3 consecutive empty seats in row 1)
// Or whichever row has the first consecutive block
```

<details>
<summary>✅ Solution (click to reveal)</summary>

```javascript
function findConsecutiveSeats(bookedSeats, needed) {
  const ROWS = 5;
  const COLS = 8;

  // Convert bookedSeats to a Set for O(1) lookup:
  const bookedSet = new Set(bookedSeats);

  for (let row = 1; row <= ROWS; row++) {
    let consecutiveCount = 0;
    let startSeat = 1;

    for (let seat = 1; seat <= COLS; seat++) {
      const seatKey = `${row}-${seat}`;

      if (bookedSet.has(seatKey)) {
        // This seat is taken — reset consecutive count:
        consecutiveCount = 0;
        startSeat = seat + 1; // Next potential start
        continue; // Skip to next seat
      }

      // Seat is available:
      consecutiveCount++;

      if (consecutiveCount === needed) {
        // Found enough consecutive seats!
        let foundSeats = [];
        for (let s = startSeat; s < startSeat + needed; s++) {
          foundSeats.push(s);
        }

        return {
          success: true,
          row: row,
          seats: foundSeats,
          message: `✅ Row ${row}, seats ${foundSeats.join(", ")} are available!`
        };
      }
    }
    // Could not find consecutive block in this row — try next row (loop continues)
  }

  return {
    success: false,
    message: `❌ No block of ${needed} consecutive seats available.`
  };
}

const booked = [
  "1-1","1-2","1-3",
  "2-5","2-6",
  "3-1","3-2","3-5","3-6","3-7",
  "4-3","4-4","4-5"
];

// Find 3 consecutive seats:
let result3 = findConsecutiveSeats(booked, 3);
console.log(result3.message); // ✅ Row 1, seats 4, 5, 6 are available!

// Find 4 consecutive seats:
let result4 = findConsecutiveSeats(booked, 4);
console.log(result4.message); // ✅ Row 1, seats 4, 5, 6, 7 are available!

// Find 8 consecutive seats (entire row):
let result8 = findConsecutiveSeats(booked, 8);
console.log(result8.message); // ✅ Row 5, seats 1-8 (no bookings in row 5)

// Find 9 seats (impossible):
let result9 = findConsecutiveSeats(booked, 9);
console.log(result9.message); // ❌ No block of 9 consecutive seats available.
```

</details>

---

## Chapter Summary

Outstanding work completing Chapter 3! Here is a complete review of everything you learned:

### ➕ Operators

**Arithmetic:** `+`, `-`, `*`, `/`, `%`, `**`, `++`, `--`
- `%` (modulo) gives the remainder — useful for even/odd checks and wrap-around logic
- `++x` (prefix) increments first, returns new value; `x++` (postfix) returns current value, then increments
- `+` with a string causes concatenation — use template literals to avoid confusion

**Assignment:** `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `??=`

**Comparison:** Always use `===` and `!==`; avoid `==` and `!=` due to coercion surprises

**Logical:**
- `&&` — returns first falsy OR last value; short-circuits on first falsy
- `||` — returns first truthy OR last value; short-circuits on first truthy
- `!` — flips boolean; `!!` converts any value to boolean
- `??` — returns right side only if left is `null`/`undefined` (not all falsy values)

### 🔀 Control Flow

**if / else if / else**
- Check most specific condition first (or conditions can be masked by broader ones)
- Use **guard clauses** to avoid deep nesting — check bad conditions first, return early

**Ternary operator** `condition ? a : b`
- Great for simple inline conditional values
- Avoid deep nesting of ternaries — use `if/else` instead

**switch**
- Uses `===` (strict) for case comparison
- Always add `break` unless fall-through is intentional and documented
- Use `default` to handle unexpected values

### 🔁 Loops

| Loop | Best For | Runs At Least Once? |
|---|---|---|
| `for` | Known number of iterations, index access | Depends on condition |
| `while` | Unknown iterations, condition-based | No |
| `do...while` | Must run at least once (menus, initial fetch) | Yes |
| `for...of` | Array/iterable VALUES | Depends on array size |
| `for...in` | Object KEYS (not arrays!) | Depends on properties |

**break** — exits the entire loop  
**continue** — skips current iteration, continues loop  
**Labels** — allow break/continue to target outer loops (use sparingly)

### 🛠️ Modern Patterns

- `?.` (optional chaining) — safe nested property access
- `??` (nullish coalescing) — default values for null/undefined only
- `arr.map()` — transform each element into a new array
- `arr.filter()` — keep only elements passing a test
- `arr.reduce()` — reduce array to a single value
- Chain `.filter().map().reduce()` for powerful data processing

---

### 📌 Golden Rules

```
✅ Always use === not ==
✅ Always break in switch (unless intentional fall-through)
✅ Always update loop variables to prevent infinite loops
✅ Prefer for...of over for...in on arrays
✅ Use guard clauses to flatten nested if/else
✅ Use ?? for defaults when 0 and false are valid values
✅ Use optional chaining (?.) for safe nested property access
✅ Prefer map/filter/reduce over manual loops for array operations
❌ Never modify an array while iterating over it with a for loop
❌ Never use for...in on arrays
❌ Never forget break in switch cases
❌ Never create infinite loops (always ensure condition will become false)
```

---

## Next Chapter

You now have the tools to make decisions and repeat actions. The next step is learning how to organize and reuse your code — the cornerstone of scalable programming.

---

**➡️ [Next Chapter: Functions in JavaScript →](./ch04-functions.md)**

---

*Last updated: 2024 | Chapter 3 of the Complete JavaScript Guide*

*Found an error or have a suggestion? [Open an issue on GitHub](https://github.com/zaid0091/CodeShelf/issues)*

*← [Previous Chapter: Data Types](./ch02-data-types.md)*
