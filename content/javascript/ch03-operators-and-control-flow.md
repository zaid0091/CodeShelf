---
title: Operators and Control Flow
description: Arithmetic, comparison, logical operators, if/else, switch, and loops in JavaScript
order: 3
tags: [javascript, operators, if, switch, loops, control-flow]
---

# Chapter 3: Operators and Control Flow

## 3.1 Arithmetic operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `5 / 2` | `2.5` |
| `%` | Remainder | `5 % 2` | `1` |
| `**` | Exponent | `2 ** 3` | `8` |
| `++` | Increment | `let n=1; n++` | post-increment |
| `--` | Decrement | `let n=1; --n` | pre-decrement |

```javascript
let x = 10;
x += 5;   // 15 — same as x = x + 5
x *= 2;   // 30
x %= 7;   // 2
```

### String concatenation with `+`

```javascript
"Hello" + " " + "World"; // "Hello World"
"Count: " + 42;          // "Count: 42"
```

## 3.2 Comparison operators

| Operator | Meaning | Notes |
|----------|---------|-------|
| `===` | Strict equal | Preferred |
| `!==` | Strict not equal | Preferred |
| `==` | Loose equal | Coerces types |
| `!=` | Loose not equal | Avoid |
| `>`, `<`, `>=`, `<=` | Ordering | Coerces when using `==` rules |

```javascript
"a" < "b";           // true (lexicographic)
10 < "2";            // false — "2" coerced to number 2
"10" < "2";          // true — string comparison
```

## 3.3 Logical operators

| Operator | Description | Short-circuit |
|----------|-------------|---------------|
| `&&` | AND — returns first falsy or last value | Yes |
| `\|\|` | OR — returns first truthy or last value | Yes |
| `!` | NOT — boolean negation | No |

```javascript
const user = { name: "Alice", role: "admin" };

const canEdit = user && user.role === "admin";
const displayName = user.name || "Guest";

// Nullish coalescing — only null/undefined
const port = config.port ?? 3000;
```

### Optional chaining

```javascript
const zip = user?.address?.zip ?? "N/A";
```

## 3.4 Conditional statements — `if` / `else`

```javascript
const score = 85;

if (score >= 90) {
  console.log("A");
} else if (score >= 80) {
  console.log("B");
} else if (score >= 70) {
  console.log("C");
} else {
  console.log("F");
}
```

### Ternary operator

```javascript
const status = isOnline ? "online" : "offline";
const max = a > b ? a : b;
```

### Nested conditions (keep shallow)

```javascript
function getTicketPrice(age, isStudent) {
  if (age < 5) return 0;
  if (isStudent) return 10;
  if (age >= 65) return 12;
  return 20;
}
```

## 3.5 `switch` statement

> **Definition:** `switch` compares an expression to multiple `case` values using strict equality (`===`).

```javascript
const day = 3;
let dayName;

switch (day) {
  case 1:
    dayName = "Monday";
    break;
  case 2:
    dayName = "Tuesday";
    break;
  case 3:
    dayName = "Wednesday";
    break;
  default:
    dayName = "Unknown";
}

console.log(dayName); // "Wednesday"
```

### Fall-through (intentional grouping)

```javascript
const grade = "B";

switch (grade) {
  case "A":
  case "B":
    console.log("Good job");
    break;
  case "C":
  case "D":
    console.log("Needs improvement");
    break;
  default:
    console.log("Invalid grade");
}
```

| When to use `switch` | When to use `if/else` |
|----------------------|------------------------|
| Many discrete values on one variable | Complex boolean conditions |
| Readable day/status enums | Ranges (`score > 80`) |

## 3.6 Loops — `for`

```javascript
for (let i = 0; i < 5; i++) {
  console.log(i); // 0, 1, 2, 3, 4
}
```

### `for...of` (iterables: arrays, strings)

```javascript
const colors = ["red", "green", "blue"];

for (const color of colors) {
  console.log(color);
}

for (const char of "hi") {
  console.log(char); // "h", "i"
}
```

### `for...in` (enumerable keys — usually objects)

```javascript
const person = { name: "Alice", age: 30 };

for (const key in person) {
  if (Object.hasOwn(person, key)) {
    console.log(key, person[key]);
  }
}
```

> Prefer `for...of` for arrays; `for...in` on arrays can include unexpected keys.

## 3.7 `while` and `do...while`

```javascript
let count = 0;

while (count < 3) {
  console.log(count);
  count++;
}

// do...while runs at least once
let input;
do {
  input = getInput(); // pseudo
} while (!input);
```

## 3.8 Loop control — `break` and `continue`

```javascript
for (let i = 0; i < 10; i++) {
  if (i === 3) continue; // skip 3
  if (i === 7) break;    // stop at 7
  console.log(i);        // 0,1,2,4,5,6
}
```

### Labeled break (rare)

```javascript
outer: for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if (i === 1 && j === 1) break outer;
  }
}
```

## 3.9 Modern array iteration (preview)

```javascript
const nums = [1, 2, 3, 4, 5];

nums.forEach((n) => console.log(n));

const doubled = nums.map((n) => n * 2);
const evens = nums.filter((n) => n % 2 === 0);
const sum = nums.reduce((acc, n) => acc + n, 0);
```

See [Chapter 5: Arrays & Objects](./ch05-arrays-and-objects.md) for full coverage.

## 3.10 Common patterns

### FizzBuzz structure

```javascript
function fizzBuzz(n) {
  const result = [];
  for (let i = 1; i <= n; i++) {
    if (i % 15 === 0) result.push("FizzBuzz");
    else if (i % 3 === 0) result.push("Fizz");
    else if (i % 5 === 0) result.push("Buzz");
    else result.push(i);
  }
  return result;
}
```

### Guard clauses (early return)

```javascript
function processOrder(order) {
  if (!order) return;
  if (!order.items?.length) return;
  if (order.total < 0) throw new Error("Invalid total");
  // main logic here
}
```

## 3.11 Chapter summary

| Topic | Best practice |
|-------|---------------|
| Comparisons | Use `===` |
| Logic | Know short-circuit `&&` and `\|\|` |
| `switch` | Always `break` unless fall-through is intentional |
| Arrays | `for...of` or array methods |
| Objects | `for...in` with `Object.hasOwn` |

## Exercises

### Exercise 3.1 — Grade calculator

Write `getLetterGrade(score)` using `if/else` for A (90+), B (80+), C (70+), D (60+), F otherwise.

### Exercise 3.2 — Day of week

Rewrite the day lookup using `switch` for numbers 1–7.

### Exercise 3.3 — Sum loop

Use a `for` loop to compute the sum of integers from 1 to `n`.

### Exercise 3.4 — Multiplication table

Print a 5×5 multiplication table using nested `for` loops and `console.log` with padded spacing.

### Exercise 3.5 — Find first match

Given `const ids = [4, 7, 2, 9, 7]`, use a loop with `break` to find the first id greater than 5.

---

**Previous:** [Chapter 2: Data Types](./ch02-data-types.md) · **Next:** [Chapter 4: Functions](./ch04-functions.md)
