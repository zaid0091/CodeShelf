---
title: Data Types
description: Primitives, typeof, type coercion, and truthy/falsy values in JavaScript
order: 2
tags: [javascript, types, typeof, coercion, truthy, falsy]
---

# Chapter 2: Data Types in JavaScript

> **In this chapter, you will learn one of the most fundamental concepts in programming — data types.** Understanding data types means understanding *what kinds of information JavaScript can work with*, *how it stores that information*, and *what happens when you mix different types together.* Take your time here — this knowledge will make everything else in JavaScript much clearer.

---

## Table of Contents

1. [What Are Data Types?](#what-are-data-types)
2. [Two Categories: Primitive vs Reference](#two-categories-primitive-vs-reference)
3. [String](#string)
4. [Number](#number)
5. [Boolean](#boolean)
6. [Undefined](#undefined)
7. [Null](#null)
8. [BigInt](#bigint)
9. [Symbol](#symbol)
10. [The typeof Operator](#the-typeof-operator)
11. [Type Coercion](#type-coercion)
12. [Equality: == vs ===](#equality--vs-)
13. [Truthy and Falsy Values](#truthy-and-falsy-values)
14. [Objects vs Primitives: Value vs Reference](#objects-vs-primitives-value-vs-reference)
15. [Immutability of Primitives](#immutability-of-primitives)
16. [Best Practices](#best-practices)
17. [Common Mistakes](#common-mistakes)
18. [Interview Points](#interview-points)
19. [Exercises](#exercises)
20. [Chapter Summary](#chapter-summary)

---

## What Are Data Types?

### Definition

A **data type** tells JavaScript what *kind of information* a value is, so JavaScript knows what it can do with it.

Think about real life for a moment:
- The number `42` is different from the word `"forty-two"`
- You can do math with `42` (add it, subtract it, multiply it)
- You can read `"forty-two"` as text but you cannot do arithmetic with it directly

In the same way, JavaScript needs to know what *type* of data it is dealing with so it can handle it correctly.

### Why Do Data Types Exist?

Every piece of information stored in a computer is ultimately just a series of `0`s and `1`s (binary). The number `65` and the letter `"A"` might look different to you, but in memory, they can be stored the same way. The **data type** is the label that tells JavaScript:

- "This is a number — treat it as something you can calculate with"
- "This is text — treat it as something you can read and display"
- "This is true or false — treat it as a yes/no answer"

Without data types, a program would not know whether `"5" + "3"` should give `"53"` (joining text) or `8` (adding numbers). Data types give meaning to raw data.

### JavaScript is Dynamically Typed

In some languages (like Java or C++), you must **declare** what type a variable will hold before using it, and it can never change:

```java
// Java — you must specify the type upfront
int age = 25;        // this can ONLY ever hold integers
String name = "Bob"; // this can ONLY ever hold text
```

In JavaScript, you do **not** declare types. A variable can hold any type, and it can even change type later:

```javascript
// JavaScript — no type declaration needed
let value = 42;         // currently a number
console.log(value);     // 42

value = "Hello";        // now it's a string — perfectly valid!
console.log(value);     // Hello

value = true;           // now it's a boolean
console.log(value);     // true
```

This is called **dynamic typing** — the type is determined at runtime (when the code runs), not at the time you write the code. This makes JavaScript flexible and quick to write, but it also means you need to be more careful, because JavaScript will not stop you from accidentally mixing types in unexpected ways.

### JavaScript's Data Types at a Glance

JavaScript has **8 data types** in total:

| Type | Category | Example |
|---|---|---|
| `string` | Primitive | `"Hello"` |
| `number` | Primitive | `42`, `3.14` |
| `boolean` | Primitive | `true`, `false` |
| `undefined` | Primitive | `undefined` |
| `null` | Primitive | `null` |
| `bigint` | Primitive | `9007199254740991n` |
| `symbol` | Primitive | `Symbol("id")` |
| `object` | Reference | `{}`, `[]`, functions |

The first seven are called **primitives**. The last one — `object` — is the **reference type** and includes objects, arrays, and functions. Let's understand what this distinction means.

---

## Two Categories: Primitive vs Reference

This is one of the most important concepts in JavaScript. Understanding this will save you from many confusing bugs.

### Primitive Types

A **primitive** is a simple, single value. It is not an object and has no methods of its own (though JavaScript adds some temporarily — more on this later). Primitives are:

- **Stored directly** in the variable
- **Copied by value** — when you copy a primitive, you get a completely independent copy
- **Immutable** — the value itself cannot be changed (you can only replace the whole thing)

Think of a primitive like a number written on a piece of paper. If you copy that paper, you have two separate papers. Changing one does not affect the other.

```javascript
// Primitive: copied by value
let a = 10;
let b = a;  // b gets a COPY of the value 10

b = 20;     // we change b

console.log(a); // 10 ← a is UNCHANGED. a and b are independent.
console.log(b); // 20
```

### Reference Types (Objects)

A **reference type** (object) is a more complex structure that can hold multiple values. It is:

- **Stored in memory** (on the "heap") — the variable holds a *reference* (address) to where the object lives in memory
- **Copied by reference** — when you copy an object variable, both variables point to the **same** object in memory
- **Mutable** — the contents can be changed

Think of a reference like a house address written on a piece of paper. If you copy the address onto another paper, you now have two pieces of paper — but they both point to the **same house**. If someone paints the house red, both papers now point to a red house.

```javascript
// Reference type: copied by reference
let person1 = { name: "Alice", age: 25 };
let person2 = person1; // person2 gets the SAME reference (same address in memory)

person2.name = "Bob"; // we change a property through person2

console.log(person1.name); // "Bob" ← person1 is CHANGED too! Same object.
console.log(person2.name); // "Bob"

// Both variables point to the same object in memory.
```

### Visual Explanation

```
PRIMITIVE (stored by value):
┌──────────┐          ┌──────────┐
│  a = 10  │          │  b = 20  │
│  (own    │          │  (own    │
│   copy)  │          │   copy)  │
└──────────┘          └──────────┘
  changing b has NO effect on a

REFERENCE (stored by reference):
┌──────────────┐      ┌──────────────┐
│   person1    │      │   person2    │
│ (address: →) │      │ (address: →) │
└──────────────┘      └──────────────┘
         │                    │
         └────────┬───────────┘
                  ↓
         ┌─────────────────┐
         │  MEMORY (heap)  │
         │  { name: "Bob", │
         │    age: 25 }    │
         └─────────────────┘
  Both variables point to THE SAME object.
  Changing through one changes the other.
```

This distinction will matter enormously when you work with functions, arrays, and objects. We will explore this more in the [Objects vs Primitives](#objects-vs-primitives-value-vs-reference) section later in this chapter.

---

## String

### Definition

A **string** is a sequence of characters — letters, numbers, spaces, symbols, emojis — treated as text. It is used to represent and work with textual data.

The word "string" comes from the idea of characters strung together in a line, like beads on a necklace.

### Why Strings Exist

Almost every program needs to work with text — displaying messages to users, reading names, processing form inputs, showing error messages, handling URLs. Strings are how JavaScript represents and manipulates all text.

### Syntax

You create a string by wrapping text in quote marks. JavaScript supports three types of quotes:

```javascript
// 1. Single quotes
let firstName = 'Alice';

// 2. Double quotes
let lastName = "Smith";

// 3. Template literals (backticks) — introduced in ES6
let greeting = `Hello, World!`;
```

All three create strings. The choice between single and double quotes is mostly a matter of style — just be consistent. Template literals (backticks) are special because they allow **embedded expressions** and **multi-line strings**.

### Simple Example

```javascript
let name = "Alice";
let city = 'London';
let message = `Hello from ${city}!`; // Template literal with embedded variable

console.log(name);    // Alice
console.log(city);    // London
console.log(message); // Hello from London!
```

### Template Literals In Depth

Template literals use backticks `` ` `` and allow you to embed JavaScript expressions directly inside the string using `${}`:

```javascript
let product = "laptop";
let price = 999;
let quantity = 3;

// Old way — string concatenation (messy):
let total1 = "You ordered " + quantity + " " + product + "(s) for $" + (price * quantity);

// Modern way — template literals (clean and readable):
let total2 = `You ordered ${quantity} ${product}(s) for $${price * quantity}`;

console.log(total2); // You ordered 3 laptop(s) for $2997
```

Template literals also support **multi-line strings** without any special syntax:

```javascript
// Old way with \n (newline character):
let poem1 = "Roses are red,\nViolets are blue,\nJavaScript is great,\nAnd so are you.";

// Template literal way (natural line breaks):
let poem2 = `Roses are red,
Violets are blue,
JavaScript is great,
And so are you.`;

console.log(poem2);
// Roses are red,
// Violets are blue,
// JavaScript is great,
// And so are you.
```

### Special Characters (Escape Sequences)

Sometimes you need to include characters inside a string that would normally confuse JavaScript:

```javascript
// What if you need a quote mark INSIDE a string?

// Option 1: Use the other type of quote:
let sentence1 = "It's a beautiful day";   // single quote inside double quotes ✅
let sentence2 = 'She said "Hello!"';      // double quotes inside single quotes ✅

// Option 2: Use escape character \ (backslash) to "escape" the quote:
let sentence3 = 'It\'s a beautiful day';  // backslash tells JS: this is not the end of string
let sentence4 = "She said \"Hello!\"";    // ✅

// Common escape sequences:
let tab       = "Column1\tColumn2";  // \t = tab character
let newLine   = "Line1\nLine2";      // \n = new line
let backslash = "C:\\Users\\Alice";  // \\ = literal backslash
let unicode   = "\u2665";            // \u = Unicode character (♥)

console.log(tab);       // Column1    Column2
console.log(newLine);   // Line1
                        // Line2
console.log(backslash); // C:\Users\Alice
console.log(unicode);   // ♥
```

### String Properties and Methods

Strings come with built-in tools (called **methods**) you can use on them. We will cover these fully in a later chapter, but here is a quick preview:

```javascript
let text = "Hello, JavaScript!";

// .length — number of characters
console.log(text.length);          // 18

// .toUpperCase() / .toLowerCase()
console.log(text.toUpperCase());   // HELLO, JAVASCRIPT!
console.log(text.toLowerCase());   // hello, javascript!

// .includes() — check if a string contains something
console.log(text.includes("Java")); // true
console.log(text.includes("Python")); // false

// .slice(start, end) — extract part of a string
console.log(text.slice(0, 5));     // Hello

// .replace()
console.log(text.replace("JavaScript", "World")); // Hello, World!
```

### Real-World Example

```javascript
// Building a user profile display:
const firstName = "Maria";
const lastName = "Garcia";
const email = "maria@example.com";
const membershipLevel = "Gold";
const points = 1250;

const profileCard = `
  ===== User Profile =====
  Name:       ${firstName} ${lastName}
  Email:      ${email}
  Membership: ${membershipLevel}
  Points:     ${points.toLocaleString()} pts
  ========================
`;

console.log(profileCard);
/*
  ===== User Profile =====
  Name:       Maria Garcia
  Email:      maria@example.com
  Membership: Gold
  Points:     1,250 pts
  ========================
*/
```

### Internal Working

When JavaScript stores a string, it allocates a block of memory and stores each character in sequence. Each character is actually stored as a number internally (based on Unicode — a universal system where every character has a number). The letter `"A"` is stored as `65`, `"B"` as `66`, and so on.

When you compare strings or search within them, JavaScript compares these underlying numbers character by character.

### Common String Mistakes

```javascript
// ❌ Mistake 1: Mixing quote types without escaping
let bad = "She said 'wow" and left"; // ❌ SyntaxError — double quote breaks string
let good = "She said 'wow' and left"; // ✅

// ❌ Mistake 2: Forgetting that string + number = string concatenation
let result = "The answer is: " + 40 + 2;
console.log(result); // "The answer is: 402" — NOT "The answer is: 42"!
// Fix: do the math first
let fixed = "The answer is: " + (40 + 2);
console.log(fixed); // "The answer is: 42" ✅

// ❌ Mistake 3: Using == to compare strings (covered more in coercion section)
console.log("5" == 5);  // true ← dangerous!
console.log("5" === 5); // false ← correct ✅

// ❌ Mistake 4: Confusing string length with last index
let word = "hello";
console.log(word.length);     // 5 (5 characters)
console.log(word[word.length]); // undefined ← index 5 doesn't exist!
console.log(word[word.length - 1]); // "o" ✅ (last character is at index 4)
```

---
## Number

### Definition

The **number** type in JavaScript represents both integers (whole numbers) and floating-point numbers (decimals). Unlike many other languages, JavaScript has only ONE number type for all numeric values.

### Why the Number Type Exists

Programs need to perform calculations — prices, scores, distances, ages, coordinates, statistics. The number type makes all arithmetic possible.

### Syntax

```javascript
// Integer (whole number)
let age = 25;
let score = -10;
let zero = 0;

// Floating-point (decimal)
let price = 9.99;
let pi = 3.14159;
let negative = -273.15;

// Scientific notation (for very large or small numbers)
let billion = 1e9;      // 1 × 10^9 = 1,000,000,000
let tiny = 1.5e-3;      // 1.5 × 10^-3 = 0.0015

// Special number values:
let infinity = Infinity;          // positive infinity
let negInfinity = -Infinity;      // negative infinity
let notANumber = NaN;             // "Not a Number" — result of invalid math
```

### Simple Examples

```javascript
// Basic arithmetic
console.log(10 + 3);   // 13
console.log(10 - 3);   // 7
console.log(10 * 3);   // 30
console.log(10 / 3);   // 3.3333333333333335 (floating point result)
console.log(10 % 3);   // 1 (remainder — called "modulo")
console.log(10 ** 3);  // 1000 (10 to the power of 3)
```

### The Floating Point Precision Problem

JavaScript uses a standard called **IEEE 754** (double-precision floating point) to store decimal numbers. This is the same standard used by most programming languages. Because of how it works at the binary (hardware) level, some decimal numbers cannot be represented with perfect accuracy.

```javascript
// This is a famous JavaScript quirk:
console.log(0.1 + 0.2);       // 0.30000000000000004 ← NOT exactly 0.3!
console.log(0.1 + 0.2 === 0.3); // false ← ⚠️ Danger!

// Why? Because 0.1 and 0.2 cannot be stored perfectly in binary.
// It is like trying to write 1/3 in decimal — 0.333333... goes on forever.

// How to handle this:
// Option 1: Round to a fixed number of decimal places
let result = parseFloat((0.1 + 0.2).toFixed(2));
console.log(result);       // 0.3
console.log(result === 0.3); // true ✅

// Option 2: Work with integers (multiply by 100 for cents)
let price1 = 10; // represents $0.10 (10 cents)
let price2 = 20; // represents $0.20 (20 cents)
let total = (price1 + price2) / 100;
console.log(total); // 0.3 ✅ exactly
```

### Special Number Values

**NaN (Not a Number)**

`NaN` is the result of an invalid mathematical operation. Despite its name, `typeof NaN === "number"` — JavaScript still considers it a number type, just one that represents an invalid result.

```javascript
// NaN results from invalid math:
console.log("hello" * 2);    // NaN (can't multiply text)
console.log(0 / 0);          // NaN
console.log(Math.sqrt(-1));   // NaN (can't square root a negative number)
console.log(parseInt("abc")); // NaN (can't parse "abc" as a number)

// NaN has a strange property — it does not equal itself!
console.log(NaN === NaN); // false ← one of JavaScript's most bizarre quirks!

// How to check for NaN:
console.log(isNaN("hello" * 2));     // true ✅
console.log(Number.isNaN(NaN));      // true ✅ (safer version)
console.log(Number.isNaN("hello"));  // false ✅ (only true for actual NaN value)
```

**Infinity and -Infinity**

```javascript
console.log(1 / 0);       // Infinity (dividing by zero)
console.log(-1 / 0);      // -Infinity
console.log(Infinity + 1); // Infinity (still infinity)
console.log(Infinity - Infinity); // NaN (infinity minus itself is undefined)

// Check for finite numbers:
console.log(isFinite(42));        // true
console.log(isFinite(Infinity));  // false
console.log(isFinite(NaN));       // false
```

### Number Range and Safe Integers

JavaScript numbers have limits:

```javascript
// Maximum safe integer (beyond this, precision is lost):
console.log(Number.MAX_SAFE_INTEGER); // 9007199254740991 (about 9 quadrillion)
console.log(Number.MIN_SAFE_INTEGER); // -9007199254740991

// What happens beyond safe range:
console.log(9007199254740991 + 1);  // 9007199254740992 ✅
console.log(9007199254740991 + 2);  // 9007199254740992 ← Same as above! Precision lost!

// For numbers beyond this range, use BigInt (covered next)

// Maximum number value:
console.log(Number.MAX_VALUE); // 1.7976931348623157e+308
```

### Useful Math Methods

```javascript
// The Math object has many useful tools:
console.log(Math.round(4.6));  // 5   (round to nearest integer)
console.log(Math.floor(4.9));  // 4   (round DOWN)
console.log(Math.ceil(4.1));   // 5   (round UP)
console.log(Math.abs(-42));    // 42  (absolute value — removes negative sign)
console.log(Math.max(1, 5, 3, 9, 2)); // 9 (largest value)
console.log(Math.min(1, 5, 3, 9, 2)); // 1 (smallest value)
console.log(Math.pow(2, 10));  // 1024 (2 to the power of 10)
console.log(Math.sqrt(144));   // 12  (square root)
console.log(Math.random());    // random decimal between 0 (inclusive) and 1 (exclusive)

// Random integer between 1 and 10:
let randomInt = Math.floor(Math.random() * 10) + 1;
console.log(randomInt); // e.g., 7
```

### Real-World Example

```javascript
// Shopping cart calculation with proper rounding:
const ITEM_PRICE = 19.99;
const QUANTITY = 3;
const TAX_RATE = 0.08; // 8%
const DISCOUNT_PERCENT = 10; // 10% discount

let subtotal = ITEM_PRICE * QUANTITY;                        // 59.97
let discountAmount = subtotal * (DISCOUNT_PERCENT / 100);   // 5.997
let afterDiscount = subtotal - discountAmount;               // 53.973
let taxAmount = afterDiscount * TAX_RATE;                    // 4.31784
let finalTotal = afterDiscount + taxAmount;                  // 58.29084

// Round to 2 decimal places for currency:
console.log(`Subtotal:       $${subtotal.toFixed(2)}`);     // $59.97
console.log(`Discount (10%): -$${discountAmount.toFixed(2)}`); // -$6.00
console.log(`After discount: $${afterDiscount.toFixed(2)}`); // $53.97
console.log(`Tax (8%):       $${taxAmount.toFixed(2)}`);    // $4.32
console.log(`Total:          $${finalTotal.toFixed(2)}`);   // $58.29
```

### Common Number Mistakes

```javascript
// ❌ Mistake 1: Comparing floating point decimals directly
if (0.1 + 0.2 === 0.3) {
  // This block NEVER runs!
}

// ❌ Mistake 2: Forgetting that division of integers can give decimals
let result = 7 / 2;
console.log(result); // 3.5 (not 3 — JavaScript doesn't do "integer division")

// ❌ Mistake 3: Not checking for NaN before using a value
let userInput = "abc";
let numericValue = Number(userInput); // NaN
let calculation = numericValue * 2;  // NaN — silently broken!

// ✅ Always validate:
if (Number.isNaN(numericValue)) {
  console.error("Invalid number input!");
} else {
  let calculation = numericValue * 2;
}

// ❌ Mistake 4: Using + for both adding numbers AND concatenating strings
console.log(1 + 2 + "3");  // "33" ← not "123" or 6!
// JS evaluates left-to-right: (1 + 2) = 3, then 3 + "3" = "33"
console.log("3" + 1 + 2);  // "312" ← "3" + 1 = "31", then "31" + 2 = "312"
```

---

## Boolean

### Definition

A **boolean** is the simplest data type — it can only be one of two values: `true` or `false`. Think of it as a light switch — it is either ON or OFF. Nothing in between.

The name "boolean" comes from **George Boole**, a 19th-century mathematician who developed a system of logic based on true/false values.

### Why Booleans Exist

Every decision in programming is ultimately a yes/no question:
- Is the user logged in? (yes/no)
- Is the password correct? (yes/no)
- Is the shopping cart empty? (yes/no)
- Is the score greater than 100? (yes/no)

Booleans are the foundation of all decision-making, conditions, and control flow in code.

### Syntax

```javascript
let isLoggedIn = true;
let isGameOver = false;
let hasPermission = true;
let isDarkMode = false;
```

### Simple Example

```javascript
let isRaining = true;
let hasUmbrella = false;

// Use booleans in conditions:
if (isRaining && !hasUmbrella) {
  console.log("You'll get wet! Stay inside.");
} else if (isRaining && hasUmbrella) {
  console.log("Take your umbrella.");
} else {
  console.log("Nice weather! Enjoy your walk.");
}
// Output: You'll get wet! Stay inside.
```

### Creating Booleans Through Comparisons

Most booleans in real code are not written directly as `true` or `false`. They are created as the **result of a comparison**:

```javascript
let age = 20;
let minimumAge = 18;

let isAdult = age >= minimumAge;   // true (20 >= 18)
let isTeenager = age < 20;         // false (20 is not less than 20)
let isEighteen = age === 18;       // false (20 is not 18)

console.log(isAdult);     // true
console.log(isTeenager);  // false
console.log(isEighteen);  // false

// Comparison operators that return booleans:
console.log(5 > 3);    // true
console.log(5 < 3);    // false
console.log(5 >= 5);   // true
console.log(5 <= 4);   // false
console.log(5 === 5);  // true
console.log(5 !== 5);  // false
```

### Logical Operators with Booleans

```javascript
// AND (&&) — true only if BOTH sides are true:
console.log(true && true);   // true
console.log(true && false);  // false
console.log(false && true);  // false
console.log(false && false); // false

// OR (||) — true if AT LEAST ONE side is true:
console.log(true || true);   // true
console.log(true || false);  // true
console.log(false || true);  // true
console.log(false || false); // false

// NOT (!) — flips the boolean:
console.log(!true);  // false
console.log(!false); // true
```

### Real-World Example

```javascript
// Access control system:
const isLoggedIn = true;
const isEmailVerified = true;
const isBanned = false;
const subscriptionLevel = "premium";

const canAccessContent = isLoggedIn && isEmailVerified && !isBanned;
const hasPremiumAccess = canAccessContent && subscriptionLevel === "premium";

if (hasPremiumAccess) {
  console.log("Welcome! You have full access to all premium content.");
} else if (canAccessContent) {
  console.log("Welcome! Upgrade to premium for full access.");
} else {
  console.log("Please log in or verify your email to continue.");
}
// Output: Welcome! You have full access to all premium content.
```

### Common Boolean Mistakes

```javascript
// ❌ Mistake 1: Using = (assignment) instead of === (comparison)
let x = 5;
if (x = 10) { // This ASSIGNS 10 to x and evaluates the result (truthy)!
  console.log("This always runs!"); // Bug!
}

// ✅ Fix:
if (x === 10) { // Compare, don't assign
  console.log("x is 10");
}

// ❌ Mistake 2: Comparing boolean to true/false explicitly (unnecessary)
let isVisible = true;
if (isVisible === true) { /* redundant */ }

// ✅ Simpler and more readable:
if (isVisible) { /* equivalent and cleaner */ }
if (!isVisible) { /* when false */ }

// ❌ Mistake 3: Unexpected truthy/falsy coercion (covered fully later)
if ("false") {
  console.log("This runs!"); // "false" (non-empty string) is TRUTHY — surprising!
}
```

---
## Undefined

### Definition

`undefined` means a variable has been declared but has **not yet been given a value**. It is JavaScript's way of saying: "This thing exists, but I don't know what it is yet."

### Why Undefined Exists

When JavaScript creates a variable using `var` (or when a function parameter is not provided, or when you access a property that does not exist), it needs a way to represent "no value has been assigned yet." `undefined` is that placeholder.

```javascript
// How you encounter undefined:

// 1. Variable declared but not assigned:
let username;
console.log(username); // undefined

// 2. Function parameter not provided:
function greet(name) {
  console.log("Hello,", name); // Hello, undefined (if called without argument)
}
greet(); // undefined for 'name'

// 3. Accessing a property that doesn't exist:
let user = { name: "Alice" };
console.log(user.age); // undefined (no 'age' property)

// 4. Function with no return statement:
function doNothing() {
  // no return statement
}
console.log(doNothing()); // undefined
```

### Simple Example

```javascript
let favoriteColor;
console.log(favoriteColor); // undefined

console.log(typeof favoriteColor); // "undefined"

// You can explicitly check for undefined:
if (favoriteColor === undefined) {
  console.log("No favorite color set yet.");
}
// Output: No favorite color set yet.

// Assign a value later:
favoriteColor = "blue";
console.log(favoriteColor); // "blue"
```

### Real-World Example

```javascript
// Handling missing form data:
function createUserProfile(name, email, age) {
  // Check if required fields are provided
  if (name === undefined || email === undefined) {
    console.error("Name and email are required!");
    return;
  }

  // age is optional — handle undefined gracefully
  const displayAge = age !== undefined ? age : "Not provided";

  console.log(`Profile created:
    Name:  ${name}
    Email: ${email}
    Age:   ${displayAge}
  `);
}

createUserProfile("Alice", "alice@example.com", 25);
// Profile created: Name: Alice, Email: alice@example.com, Age: 25

createUserProfile("Bob", "bob@example.com");
// Profile created: Name: Bob, Email: bob@example.com, Age: Not provided

createUserProfile("Charlie");
// Error: Name and email are required!
```

> ⚠️ **Warning:** Never intentionally assign `undefined` to a variable. If you want to explicitly indicate "no value", use `null` instead. `undefined` should be left for JavaScript to use naturally — it signals something wasn't set up yet.

```javascript
// ❌ Bad practice:
let result = undefined; // Why set something to undefined manually?

// ✅ Better practice:
let result = null; // null = intentionally empty. Clearer meaning.
```

---

## Null

### Definition

`null` means the **intentional absence of a value**. It is explicitly set by a programmer to indicate "this variable exists but intentionally has no value."

Think of `undefined` vs `null` this way:
- `undefined` = "I forgot to fill this in" (accidental or not yet set)
- `null` = "I intentionally left this blank" (deliberate)

### Why Null Exists

Sometimes you need to explicitly signal that something is empty — a user with no profile picture, a form field that was cleared, a search that returned no results. `null` communicates this intent clearly.

### Syntax

```javascript
let profilePicture = null;    // No photo uploaded yet
let selectedItem = null;      // Nothing selected
let loggedInUser = null;      // Nobody is logged in
```

### Simple Example

```javascript
let currentUser = null; // Nobody logged in at the start

console.log(currentUser); // null
console.log(typeof currentUser); // "object" ← This is a famous JavaScript BUG!

// When user logs in:
currentUser = { name: "Alice", role: "admin" };
console.log(currentUser); // { name: "Alice", role: "admin" }

// When user logs out:
currentUser = null; // Reset — nobody logged in
console.log(currentUser); // null
```

### Real-World Example

```javascript
// API data handling — result could be null if not found:
function findUserById(id, database) {
  // Imagine searching a database...
  const found = database.find(user => user.id === id);
  return found || null; // Return the user OR null if not found
}

const database = [
  { id: 1, name: "Alice" },
  { id: 2, name: "Bob" }
];

const user1 = findUserById(1, database);
const user2 = findUserById(99, database); // ID 99 doesn't exist

// Always check for null before using the result:
if (user1 !== null) {
  console.log("Found:", user1.name); // Found: Alice
}

if (user2 === null) {
  console.log("User not found."); // User not found.
}
```

### The typeof null Bug

This is one of the most famous bugs in JavaScript:

```javascript
console.log(typeof null); // "object" ← This is WRONG but cannot be fixed!
```

**Why does this happen?**

In JavaScript's original implementation in 1995, values were stored with a type tag at the beginning of their memory representation. Objects had a type tag of `000`. The value `null` was represented as all zeros in memory (a null pointer). When `typeof` checked the type tag of `null`, it saw `000` and concluded it was an object.

This was a bug in the original implementation. When it was discovered, fixing it would have broken millions of websites that relied on this behavior. So the decision was made to keep the bug — permanently.

**How to correctly check for null:**

```javascript
let value = null;

// ❌ Wrong way (typeof doesn't work for null):
if (typeof value === "null") { } // "null" is never returned by typeof!

// ✅ Correct way — use strict equality:
if (value === null) {
  console.log("Value is null");
}

// ✅ Check for EITHER null OR undefined:
if (value == null) { // == (loose equality) matches both null and undefined
  console.log("Value is null or undefined");
}
```

### null vs undefined Quick Comparison

| | `undefined` | `null` |
|---|---|---|
| **Meaning** | Not yet assigned | Intentionally empty |
| **Set by** | JavaScript (automatically) | Programmer (intentionally) |
| **typeof** | `"undefined"` | `"object"` (bug!) |
| **== comparison** | `undefined == null` → `true` | `null == undefined` → `true` |
| **=== comparison** | `undefined === null` → `false` | `null === undefined` → `false` |
| **Use when** | You don't need to — JS handles it | You want to explicitly say "no value" |

---

## BigInt

### Definition

**BigInt** is a special numeric type that can represent integers of **arbitrarily large size** — far beyond what the regular `number` type can safely handle.

### Why BigInt Exists

As we saw, the regular `number` type has a maximum safe integer of `9007199254740991`. Beyond this, numbers start losing precision. But some applications genuinely need to work with much larger numbers:

- Financial systems (working with very large currency amounts)
- Cryptography (very large prime numbers)
- Scientific calculations (astronomical distances in millimeters)
- Database IDs (large systems with billions of records)

BigInt was added to JavaScript in ES2020 to solve this.

### Syntax

Create a BigInt by adding the letter `n` at the end of an integer, or using the `BigInt()` function:

```javascript
// Using the 'n' suffix:
let bigNumber = 9007199254740991n;  // This is a BigInt
let veryBig = 123456789012345678901234567890n;

// Using BigInt() function:
let fromFunction = BigInt(9007199254740991);

console.log(typeof bigNumber); // "bigint"
```

### Simple Example

```javascript
// Regular number loses precision:
let regularMax = 9007199254740991;
console.log(regularMax + 1); // 9007199254740992 ✅
console.log(regularMax + 2); // 9007199254740992 ← Same! Precision lost!

// BigInt handles it correctly:
let bigMax = 9007199254740991n;
console.log(bigMax + 1n); // 9007199254740992n ✅
console.log(bigMax + 2n); // 9007199254740993n ✅ Correct!
```

### BigInt Rules and Limitations

```javascript
// BigInt arithmetic uses the 'n' suffix on all numbers:
let a = 100n;
let b = 50n;

console.log(a + b); // 150n
console.log(a - b); // 50n
console.log(a * b); // 5000n
console.log(a / b); // 2n (BigInt division always gives integer result, no decimals)
console.log(a % b); // 0n

// ❌ Cannot mix BigInt and regular numbers directly:
let regular = 10;
let big = 20n;
console.log(regular + big); // ❌ TypeError: Cannot mix BigInt and other types

// ✅ Convert explicitly if needed:
console.log(BigInt(regular) + big); // 30n ✅
console.log(Number(big) + regular); // 30 ✅ (but loses BigInt precision for very large numbers)

// ❌ BigInt cannot use decimal points:
let bad = 1.5n; // ❌ SyntaxError

// ❌ BigInt cannot use Math methods:
Math.sqrt(9n); // ❌ TypeError

// ✅ Comparison between BigInt and regular number works:
console.log(10n === 10);  // false (different types)
console.log(10n == 10);   // true (loose equality, values are equal)
console.log(10n > 9);     // true (comparison works across types)
```

### Real-World Example

```javascript
// Cryptography: Working with large prime numbers
const largePrime1 = 17014118346046923173168730371588410572n;
const largePrime2 = 13164036458569648337239753460458804039n;

const product = largePrime1 * largePrime2;
console.log(product);
// 224018984777679584946842248748252564940...n (very large but exact!)

// Database ID generation with guaranteed uniqueness at scale:
function generateId(timestamp, serverId, sequence) {
  // Combine multiple numbers into one guaranteed-unique BigInt ID
  return (BigInt(timestamp) * 1000000n) + (BigInt(serverId) * 1000n) + BigInt(sequence);
}

const id = generateId(1704067200000, 42, 999);
console.log(id); // 1704067200042999n — unique and precise!
```

> **Note:** For most everyday programming, you will use regular `number`. BigInt is a specialized tool for specific use cases. You will rarely need it as a beginner, but knowing it exists is important.

---

## Symbol

### Definition

A **Symbol** is a **unique, immutable identifier**. Every time you create a Symbol, it is guaranteed to be completely unique — no two Symbols are ever equal, even if they were created with the same description.

### Why Symbols Exist

JavaScript objects can only have string keys by default. If two pieces of code (perhaps two different libraries you are using) both try to add a property called `"id"` to the same object, they will collide and one will overwrite the other.

Symbols solve this problem. They are used as **hidden, collision-proof property keys** for objects. This is especially important when building libraries or working with shared objects.

Symbols were added in ES6 (2015).

### Syntax

```javascript
// Create a Symbol using Symbol() function (NOT with 'new'):
let id = Symbol();
let id2 = Symbol();

// Every Symbol is unique — even with the same description:
let sym1 = Symbol("id");
let sym2 = Symbol("id");

console.log(sym1 === sym2); // false — they are DIFFERENT symbols!
console.log(sym1);          // Symbol(id)
console.log(typeof sym1);   // "symbol"
```

### Using Symbols as Object Keys

```javascript
// Problem without Symbols:
let user = {};
user.id = 1;      // Your code sets id
user.id = "abc";  // A library also sets id — now yours is overwritten! ❌

// Solution with Symbols:
const MY_ID = Symbol("id");         // Your unique symbol
const LIBRARY_ID = Symbol("id");    // Library's unique symbol (looks same, but isn't)

let user2 = {};
user2[MY_ID] = 1;        // Your id
user2[LIBRARY_ID] = "abc"; // Library's id

console.log(user2[MY_ID]);       // 1 ✅ — not affected by library
console.log(user2[LIBRARY_ID]);  // "abc" ✅ — separate, no collision!

// Symbol properties are "hidden" from most standard operations:
console.log(Object.keys(user2));    // [] — symbols don't show up here!
console.log(JSON.stringify(user2)); // {} — symbols are excluded from JSON
```

### Well-Known Symbols

JavaScript uses built-in Symbols internally to customize how objects behave. These are called "well-known Symbols":

```javascript
// Symbol.iterator — makes an object iterable (usable in for...of loops)
// Symbol.toString — customizes string conversion
// Symbol.toPrimitive — customizes type conversion

// Example: Custom iterator using Symbol.iterator
let range = {
  from: 1,
  to: 5,
  [Symbol.iterator]() {
    let current = this.from;
    const last = this.to;
    return {
      next() {
        if (current <= last) {
          return { value: current++, done: false };
        }
        return { value: undefined, done: true };
      }
    };
  }
};

for (let num of range) {
  console.log(num); // 1, 2, 3, 4, 5
}
```

> **Note for beginners:** Symbols are an advanced feature. You will not use them often at first. The most important thing to know is: (1) Symbols are unique identifiers, (2) they are used as object keys to avoid collisions, and (3) they exist in JavaScript. We will revisit them in the advanced chapters.

---
## The typeof Operator

### Definition

`typeof` is an operator that returns a **string** describing the type of a value or variable. Think of it as asking JavaScript: "Hey, what *kind* of thing is this?"

### Why typeof Exists

In a dynamically typed language like JavaScript, you often need to check what type of data you are working with before performing operations on it. For example, you might receive data from a user or an API, and you need to verify it is a number before doing math with it.

### Syntax

```javascript
// Two equivalent forms:
typeof value         // Without parentheses — standard
typeof(value)        // With parentheses — also works but unnecessary
```

### typeof Results Table

| Value | typeof result |
|---|---|
| `"hello"` | `"string"` |
| `42` | `"number"` |
| `3.14` | `"number"` |
| `NaN` | `"number"` ← (surprising!) |
| `true` | `"boolean"` |
| `false` | `"boolean"` |
| `undefined` | `"undefined"` |
| `null` | `"object"` ← (famous bug!) |
| `9007199254740991n` | `"bigint"` |
| `Symbol()` | `"symbol"` |
| `{}` | `"object"` |
| `[]` | `"object"` ← (arrays are objects!) |
| `function() {}` | `"function"` ← (functions are technically objects, but get special treatment) |

### Simple Examples

```javascript
console.log(typeof "hello");         // "string"
console.log(typeof 42);              // "number"
console.log(typeof 3.14);            // "number"
console.log(typeof true);            // "boolean"
console.log(typeof undefined);       // "undefined"
console.log(typeof null);            // "object" ← the famous bug
console.log(typeof 123n);            // "bigint"
console.log(typeof Symbol("id"));    // "symbol"
console.log(typeof {});              // "object"
console.log(typeof []);              // "object" (arrays are objects in JS)
console.log(typeof function(){});    // "function"
console.log(typeof NaN);             // "number" (NaN is technically a number type!)

// typeof with variables:
let name = "Alice";
let age = 25;
let isActive = true;
let nothing;

console.log(typeof name);     // "string"
console.log(typeof age);      // "number"
console.log(typeof isActive); // "boolean"
console.log(typeof nothing);  // "undefined"
```

### Deep Dive: typeof Quirks Explained

**Quirk 1: `typeof null === "object"` (the bug)**

```javascript
// As explained in the null section, this is a historical bug
// that cannot be fixed without breaking existing code.
console.log(typeof null); // "object" — wrong, but permanent

// Always use === null to check for null specifically:
let value = null;
if (value === null) {
  console.log("It's null!"); // ✅ Correct way to check
}
```

**Quirk 2: `typeof NaN === "number"`**

```javascript
// NaN stands for "Not a Number" but its type IS "number" — confusing!
// NaN is the result of invalid numeric operations.
// JavaScript still considers it to be in the number category.
console.log(typeof NaN);        // "number"
console.log(typeof (0 / 0));    // "number"
console.log(typeof parseInt("abc")); // "number"

// The correct way to detect NaN:
console.log(Number.isNaN(NaN)); // true ✅
```

**Quirk 3: `typeof [] === "object"` (arrays look like objects)**

```javascript
// Arrays in JavaScript are a special type of object.
// typeof cannot distinguish between arrays and plain objects:
console.log(typeof []);    // "object"
console.log(typeof {});    // "object" — same result!

// How to correctly check for an array:
console.log(Array.isArray([]));  // true ✅
console.log(Array.isArray({}));  // false ✅
```

**Quirk 4: typeof an undeclared variable does NOT throw an error**

```javascript
// Normally, using an undeclared variable causes ReferenceError:
console.log(xyz); // ❌ ReferenceError: xyz is not defined

// BUT typeof is special — it safely handles undeclared variables:
console.log(typeof xyz); // "undefined" ← no error! Just returns "undefined"

// This is useful for feature detection:
if (typeof window !== "undefined") {
  console.log("We are in a browser!");
}
if (typeof process !== "undefined") {
  console.log("We are in Node.js!");
}
```

### Real-World Example

```javascript
// A function that handles different input types gracefully:
function processInput(input) {
  const inputType = typeof input;

  switch (inputType) {
    case "string":
      console.log(`Text received: "${input.toUpperCase()}"`);
      break;

    case "number":
      if (Number.isNaN(input)) {
        console.error("Received NaN — invalid number!");
      } else {
        console.log(`Number received: ${input * 2} (doubled)`);
      }
      break;

    case "boolean":
      console.log(`Boolean received: ${input ? "YES" : "NO"}`);
      break;

    case "undefined":
      console.warn("No input provided!");
      break;

    case "object":
      if (input === null) {
        console.warn("Null value received.");
      } else if (Array.isArray(input)) {
        console.log(`Array received with ${input.length} items.`);
      } else {
        console.log(`Object received with keys: ${Object.keys(input).join(", ")}`);
      }
      break;

    default:
      console.log(`Unhandled type: ${inputType}`);
  }
}

processInput("hello");                  // Text received: "HELLO"
processInput(42);                       // Number received: 84 (doubled)
processInput(true);                     // Boolean received: YES
processInput(undefined);               // No input provided!
processInput(null);                    // Null value received.
processInput([1, 2, 3]);               // Array received with 3 items.
processInput({ name: "Alice" });        // Object received with keys: name
```

### Debugging Tips for typeof

```javascript
// Tip 1: Always log both the value AND its type when debugging:
let mystery = getUserData(); // Some unknown function
console.log("Value:", mystery, "| Type:", typeof mystery);

// Tip 2: Use typeof in defensive code to avoid errors:
function safeDouble(value) {
  if (typeof value !== "number" || Number.isNaN(value)) {
    console.error("Expected a number, got:", typeof value);
    return null;
  }
  return value * 2;
}

console.log(safeDouble(5));       // 10
console.log(safeDouble("hello")); // Error: Expected a number, got: string
console.log(safeDouble(NaN));     // Error: Expected a number, got: number
```

---

## Type Coercion

### Definition

**Type coercion** is the automatic (or manual) conversion of a value from one data type to another. When JavaScript needs to operate on two values of different types, it tries to convert one of them to make the operation possible.

Think of it like this: if you ask someone to add "five" and `3` together, they might mentally convert "five" to `5` and give you `8`. JavaScript does something similar — sometimes helpfully, sometimes in very surprising ways.

### Why Type Coercion Exists

JavaScript was designed to be flexible and forgiving. The goal was to make it easy for beginners to write code that *mostly works* without strict type rules. This is good for rapid development but can cause hard-to-find bugs.

There are two kinds of coercion:
1. **Implicit coercion** — JavaScript does it automatically
2. **Explicit coercion** — You do it manually in your code

### Implicit Coercion (Automatic)

JavaScript automatically converts types in certain situations. This is where surprises happen.

#### String Coercion (+ operator)

When you use `+` and one side is a string, JavaScript converts the other side to a string too:

```javascript
// Number + String = String (concatenation wins)
console.log(1 + "2");        // "12"  (1 is converted to "1", then joined)
console.log("3" + 4);        // "34"
console.log("Age: " + 25);   // "Age: 25"
console.log(true + " story"); // "true story" (boolean → string)
console.log(null + " value"); // "null value" (null → string)

// ⚠️ Order matters with multiple + operations:
console.log(1 + 2 + "3");    // "33"  (1+2=3, then 3+"3"="33")
console.log("1" + 2 + 3);    // "123" ("1"+2="12", then "12"+3="123")
```

#### Numeric Coercion (other arithmetic operators)

When you use `-`, `*`, `/`, `%`, or `**`, JavaScript tries to convert values to numbers:

```javascript
// String → Number coercion with arithmetic operators:
console.log("10" - 5);   // 5   ("10" → 10, then 10-5)
console.log("10" * 2);   // 20  ("10" → 10, then 10*2)
console.log("10" / 2);   // 5   ("10" → 10, then 10/2)
console.log("10" % 3);   // 1   ("10" → 10, then 10%3)

// Non-numeric strings become NaN:
console.log("hello" - 1); // NaN ("hello" can't become a number)
console.log("abc" * 2);   // NaN

// Booleans in arithmetic:
console.log(true + 1);    // 2   (true → 1)
console.log(false + 1);   // 1   (false → 0)
console.log(true + true); // 2   (1 + 1)

// null and undefined in arithmetic:
console.log(null + 1);       // 1   (null → 0)
console.log(undefined + 1);  // NaN (undefined → NaN)
```

#### Boolean Coercion (in conditions)

When you use a value in an `if` statement or logical operation, JavaScript converts it to `true` or `false`:

```javascript
// These all convert to boolean in a condition:
if ("hello") { console.log("truthy!"); }  // runs — non-empty string is truthy
if (0) { console.log("won't run"); }      // doesn't run — 0 is falsy
if ([]) { console.log("truthy!"); }       // runs — empty array is truthy (surprising!)
if ({}) { console.log("truthy!"); }       // runs — empty object is truthy
```

(We will cover truthy/falsy in full detail in its own section.)

### Implicit Coercion Examples Table

| Expression | Result | Why |
|---|---|---|
| `"5" + 3` | `"53"` | String + Number = String |
| `"5" - 3` | `2` | String converted to Number |
| `"5" * "2"` | `10` | Both strings converted to Numbers |
| `true + 1` | `2` | `true` → `1` |
| `false + 1` | `1` | `false` → `0` |
| `null + 1` | `1` | `null` → `0` |
| `undefined + 1` | `NaN` | `undefined` → `NaN` |
| `"5" - false` | `5` | `"5"` → `5`, `false` → `0` |
| `"" + 0` | `"0"` | Empty string + Number = String |
| `[] + []` | `""` | Both arrays convert to `""` |
| `[] + {}` | `"[object Object]"` | Array → `""`, Object → `"[object Object]"` |
| `{} + []` | `0` | Interpreted as empty block + `+[]` |

> ⚠️ **Warning:** The last few rows show how unpredictable implicit coercion can get. This is why many developers avoid relying on coercion and prefer explicit conversion.

### Explicit Coercion (Manual)

You control exactly when and how values are converted. This is always safer and more readable.

#### Converting to String

```javascript
// Method 1: String() function — safest, works on anything
console.log(String(42));        // "42"
console.log(String(true));      // "true"
console.log(String(false));     // "false"
console.log(String(null));      // "null"
console.log(String(undefined)); // "undefined"
console.log(String([1, 2, 3])); // "1,2,3"

// Method 2: .toString() method — works on most types (not null/undefined!)
console.log((42).toString());       // "42"
console.log((255).toString(16));    // "ff" (converts to hexadecimal)
console.log((8).toString(2));       // "1000" (converts to binary)
console.log(true.toString());       // "true"

// Method 3: Template literal — implicit but intentional
let num = 42;
let numAsString = `${num}`;
console.log(numAsString);           // "42"
console.log(typeof numAsString);    // "string"

// Method 4: Concatenating with empty string (less readable, not recommended)
console.log(42 + "");  // "42" (works but confusing to read)
```

#### Converting to Number

```javascript
// Method 1: Number() function — safest and most explicit
console.log(Number("42"));        // 42
console.log(Number("3.14"));      // 3.14
console.log(Number(""));          // 0 ← empty string → 0 (surprising!)
console.log(Number("  42  "));    // 42 ← trims whitespace
console.log(Number("42abc"));     // NaN ← not a pure number
console.log(Number(true));        // 1
console.log(Number(false));       // 0
console.log(Number(null));        // 0
console.log(Number(undefined));   // NaN
console.log(Number([]));          // 0
console.log(Number([5]));         // 5 ← single-element array!
console.log(Number([1, 2]));      // NaN ← multiple elements

// Method 2: parseInt() — parses an integer from the start of a string
console.log(parseInt("42"));       // 42
console.log(parseInt("42.9"));     // 42 (integer only, ignores decimal)
console.log(parseInt("42px"));     // 42 ← stops at non-numeric character!
console.log(parseInt("px42"));     // NaN ← string doesn't START with a digit
console.log(parseInt("0xFF", 16)); // 255 (parse hexadecimal)
console.log(parseInt("1010", 2));  // 10 (parse binary)

// Method 3: parseFloat() — parses a decimal number from a string
console.log(parseFloat("3.14"));      // 3.14
console.log(parseFloat("3.14abc"));   // 3.14 ← stops at non-numeric
console.log(parseFloat("$3.14"));     // NaN

// Method 4: Unary + operator (quick but less readable)
console.log(+"42");      // 42
console.log(+true);      // 1
console.log(+false);     // 0
console.log(+"");        // 0
console.log(+"hello");   // NaN
```

#### Converting to Boolean

```javascript
// Method 1: Boolean() function
console.log(Boolean(1));          // true
console.log(Boolean(0));          // false
console.log(Boolean("hello"));    // true
console.log(Boolean(""));         // false
console.log(Boolean(null));       // false
console.log(Boolean(undefined));  // false
console.log(Boolean(NaN));        // false
console.log(Boolean({}));         // true ← even empty objects are truthy!
console.log(Boolean([]));         // true ← even empty arrays are truthy!

// Method 2: Double NOT operator !! (quick conversion)
console.log(!!1);          // true
console.log(!!0);          // false
console.log(!!"hello");    // true
console.log(!!"");         // false
// First ! converts to opposite boolean, second ! flips it back
// Net result: value converted to boolean
```

### Real-World Example: Form Validation

```javascript
// Real scenario: Processing form input from a user
function processAgeInput(rawInput) {
  // rawInput is always a string (from HTML form)
  console.log("Raw input type:", typeof rawInput); // "string"
  console.log("Raw input value:", rawInput);        // e.g., "  25  "

  // Step 1: Convert to number explicitly (don't rely on coercion)
  const age = Number(rawInput.trim()); // trim() removes whitespace

  // Step 2: Validate the result
  if (Number.isNaN(age)) {
    return { success: false, error: "Please enter a valid number for age." };
  }

  if (!Number.isFinite(age)) {
    return { success: false, error: "Age must be a finite number." };
  }

  if (age < 0 || age > 150) {
    return { success: false, error: "Please enter a realistic age (0-150)." };
  }

  if (!Number.isInteger(age)) {
    return { success: false, error: "Age must be a whole number." };
  }

  return { success: true, age: age };
}

console.log(processAgeInput("  25  "));  // { success: true, age: 25 }
console.log(processAgeInput("abc"));     // { success: false, error: "Please enter a valid number..." }
console.log(processAgeInput("-5"));      // { success: false, error: "Please enter a realistic age..." }
console.log(processAgeInput("25.5"));    // { success: false, error: "Age must be a whole number." }
```

---
## Equality: == vs ===

### Definition

JavaScript has **two equality operators**:
- `==` — **Loose equality** (performs type coercion before comparing)
- `===` — **Strict equality** (no coercion — types must also match)

### Why Two Equality Operators?

`==` was in the original JavaScript and tried to be helpful by converting types before comparing. `===` was added later to give developers a way to compare values **without** any automatic conversion — making behavior predictable.

### How == Works

When you use `==`, JavaScript follows a set of rules to convert the values to the same type before comparing:

```javascript
// == (loose equality) — converts types first:
console.log(1 == "1");      // true  (string "1" converted to number 1)
console.log(0 == false);    // true  (false converted to 0)
console.log(1 == true);     // true  (true converted to 1)
console.log("" == false);   // true  (both convert to 0)
console.log(null == undefined); // true (special rule: these two are "equal" loosely)
console.log(null == 0);     // false (special rule: null only equals undefined with ==)
console.log(null == false); // false (special rule)
console.log([] == false);   // true  ([] → "" → 0, false → 0)
console.log("" == 0);       // true  ("" converts to 0)
```

The rules for `==` are complex and inconsistent. This leads to surprising results that are hard to predict.

### How === Works

`===` is simple: both the **value** AND the **type** must be exactly the same. No conversion, no surprises:

```javascript
// === (strict equality) — no type conversion:
console.log(1 === "1");      // false (number vs string — different types)
console.log(0 === false);    // false (number vs boolean — different types)
console.log(1 === true);     // false (number vs boolean — different types)
console.log(null === undefined); // false (null vs undefined — different types)
console.log(1 === 1);        // true ✅ (same type AND same value)
console.log("hello" === "hello"); // true ✅
console.log(null === null);  // true ✅
console.log(undefined === undefined); // true ✅
```

### Inequality Operators

```javascript
// != (loose inequality — same rules as ==, with coercion):
console.log(1 != "1");  // false (they are loosely equal, so not unequal)
console.log(1 != 2);    // true

// !== (strict inequality — no coercion):
console.log(1 !== "1"); // true (different types — strictly not equal)
console.log(1 !== 1);   // false (same type and value — they ARE strictly equal)
```

### Side-by-Side Comparison Table

| Expression | `==` | `===` |
|---|---|---|
| `1 == "1"` | `true` | — |
| `1 === "1"` | — | `false` |
| `0 == false` | `true` | — |
| `0 === false` | — | `false` |
| `null == undefined` | `true` | — |
| `null === undefined` | — | `false` |
| `"" == false` | `true` | — |
| `"" === false` | — | `false` |
| `NaN == NaN` | `false` | `false` (NaN never equals itself) |
| `NaN === NaN` | `false` | `false` (NaN never equals itself) |
| `[] == []` | `false` | `false` (different objects in memory) |
| `{} == {}` | `false` | `false` (different objects in memory) |

### Real-World Example

```javascript
// Login form validation:
function checkLogin(inputUsername, inputPassword, storedUsername, storedPassword) {

  // ❌ Using == is risky:
  if (inputUsername == storedUsername) {
    // A hacker could potentially exploit coercion behavior
    // with carefully crafted inputs
  }

  // ✅ Always use === for comparisons:
  if (inputUsername === storedUsername && inputPassword === storedPassword) {
    return { success: true, message: "Login successful!" };
  }

  return { success: false, message: "Invalid username or password." };
}

console.log(checkLogin("alice", "pass123", "alice", "pass123"));
// { success: true, message: "Login successful!" }

console.log(checkLogin("alice", "wrong", "alice", "pass123"));
// { success: false, message: "Invalid username or password." }

// Imagine a coercion-related trick:
console.log(0 == "0");   // true with == — potential vulnerability!
console.log(0 === "0");  // false with === — safe ✅
```

> ✅ **Best Practice:** **Always use `===` and `!==`** in your code. The only case where `==` is useful is checking for `null || undefined` simultaneously: `value == null` is true for both, which is sometimes convenient. But even then, it is clearer to write `value === null || value === undefined`.

---

## Truthy and Falsy Values

### Definition

In JavaScript, every value has an inherent boolean quality. When used in a boolean context (like an `if` statement), a value is either:
- **Truthy** — behaves like `true` (the `if` block runs)
- **Falsy** — behaves like `false` (the `if` block does NOT run)

You do not need to write `=== true` or `=== false` explicitly. JavaScript evaluates any value as true or false in a condition.

### Why Truthy/Falsy Exists

JavaScript's design allows any value to be used as a condition — not just actual booleans. This is intentional and enables a lot of useful shorthand patterns. Understanding it is essential for reading and writing real JavaScript code.

### The Falsy Values — Memorize These!

There are **exactly 8 falsy values** in JavaScript. Everything else is truthy:

| Falsy Value | Type | Notes |
|---|---|---|
| `false` | boolean | The obvious one |
| `0` | number | Zero |
| `-0` | number | Negative zero |
| `0n` | bigint | BigInt zero |
| `""` | string | Empty string (single or double quotes) |
| `''` | string | Empty string |
| ` `` ` | string | Empty template literal |
| `null` | null | Explicit no-value |
| `undefined` | undefined | Unassigned value |
| `NaN` | number | Not a Number |

```javascript
// All of these conditions will NOT run their block:
if (false)     { /* won't run */ }
if (0)         { /* won't run */ }
if (-0)        { /* won't run */ }
if (0n)        { /* won't run */ }
if ("")        { /* won't run */ }
if ('')        { /* won't run */ }
if (``)        { /* won't run */ }
if (null)      { /* won't run */ }
if (undefined) { /* won't run */ }
if (NaN)       { /* won't run */ }
```

### Truthy Values — Everything Else

Everything that is not falsy is truthy. Here are some surprising ones:

```javascript
// All of these conditions WILL run their block:
if (true)           { console.log("true is truthy"); }
if (1)              { console.log("1 is truthy"); }
if (-1)             { console.log("-1 is truthy (any non-zero number)"); }
if ("hello")        { console.log("non-empty string is truthy"); }
if ("0")            { console.log('"0" is truthy! (non-empty string)'); } // ← Surprising!
if ("false")        { console.log('"false" is truthy! (non-empty string)'); } // ← Surprising!
if ([])             { console.log("empty array is truthy!"); }             // ← Surprising!
if ({})             { console.log("empty object is truthy!"); }            // ← Surprising!
if (function(){})   { console.log("function is truthy"); }
if (Infinity)       { console.log("Infinity is truthy"); }
if (-Infinity)      { console.log("-Infinity is truthy"); }
```

> ⚠️ **Warning:** The most surprising truthy values:
> - `"0"` — The string `"0"` is truthy because it is a non-empty string (it has one character in it: the digit 0). The **number** `0` is falsy, but the **string** `"0"` is truthy.
> - `[]` — An empty array is truthy. In most other languages, an empty array would be falsy.
> - `{}` — An empty object is truthy.
> - `"false"` — The string containing the word "false" is truthy because it is non-empty!

### Truthy/Falsy in Real Code

Understanding truthy/falsy is key because JavaScript developers use it constantly for shorthand:

**Pattern 1: Checking if a value exists before using it**

```javascript
// Long version:
if (username !== null && username !== undefined && username !== "") {
  console.log("Username:", username);
}

// Short version using falsy check:
if (username) {
  console.log("Username:", username);
}
// This works because null, undefined, and "" are all falsy!
```

**Pattern 2: Default values with || (OR operator)**

```javascript
// If displayName is falsy (null, undefined, empty string), use "Guest":
let displayName = null;
let name = displayName || "Guest";
console.log(name); // "Guest"

// Another example:
let userInput = "";
let searchTerm = userInput || "all items";
console.log(searchTerm); // "all items" (empty string is falsy)

// This is called the "OR default" pattern:
function greetUser(name) {
  let displayName = name || "Guest"; // If name is falsy, use "Guest"
  console.log(`Hello, ${displayName}!`);
}

greetUser("Alice");  // Hello, Alice!
greetUser("");       // Hello, Guest! (empty string is falsy)
greetUser(null);     // Hello, Guest!
greetUser();         // Hello, Guest! (undefined is falsy)
```

**Pattern 3: Short-circuit evaluation with && (AND operator)**

```javascript
// Execute the right side ONLY IF the left side is truthy:
let user = { name: "Alice", isAdmin: true };

// Long version:
if (user && user.isAdmin) {
  console.log("Welcome, admin!");
}

// Using && for short-circuit:
user && user.isAdmin && console.log("Welcome, admin!"); // Same result!

// More common real-world usage:
let config = null;
let timeout = config && config.timeout; // If config is null, timeout = null (short-circuits)
// Instead of: let timeout = config ? config.timeout : null;

// This prevents the error "Cannot read property 'timeout' of null"
console.log(timeout); // null (safe — no error thrown)
```

**Pattern 4: The Nullish Coalescing Operator ?? (ES2020)**

The `||` default pattern has a problem: it treats `0` and `false` as falsy, even when those are valid values:

```javascript
// Problem with || default:
let userScore = 0;
let displayScore = userScore || "No score yet";
console.log(displayScore); // "No score yet" ← WRONG! 0 is a valid score!

// Solution: Use ?? (nullish coalescing) — only triggers for null or undefined:
let displayScore2 = userScore ?? "No score yet";
console.log(displayScore2); // 0 ← Correct! Only null/undefined triggers the default

let retries = 0;
let maxRetries = retries ?? 3; // retries is 0, not null/undefined
console.log(maxRetries); // 0 ← Correct! 0 is a valid retry count
```

**Pattern 5: Ternary operator for conditional values**

```javascript
let isLoggedIn = true;

// Ternary: condition ? valueIfTruthy : valueIfFalsy
let buttonText = isLoggedIn ? "Log Out" : "Log In";
console.log(buttonText); // "Log Out"

let cartCount = 0;
let cartMessage = cartCount ? `${cartCount} items` : "Cart is empty";
console.log(cartMessage); // "Cart is empty" (0 is falsy)

cartCount = 3;
cartMessage = cartCount ? `${cartCount} items` : "Cart is empty";
console.log(cartMessage); // "3 items"
```

### Real-World Example: Feature Flag System

```javascript
// A real feature flag system:
const features = {
  darkMode: true,
  betaFeatures: false,
  maxItems: 0,      // ← 0 is falsy! Handle carefully
  adminPanel: null, // ← not yet configured
  userLimit: 100
};

function isFeatureEnabled(featureName) {
  const value = features[featureName];

  // For boolean features, simple truthy check works:
  // But for numeric features like maxItems=0, use strict check
  if (value === undefined || value === null) {
    return false; // not configured = disabled
  }

  return Boolean(value); // convert to boolean
}

console.log(isFeatureEnabled("darkMode"));     // true
console.log(isFeatureEnabled("betaFeatures")); // false
console.log(isFeatureEnabled("maxItems"));     // false (0 is falsy — is this right?)
console.log(isFeatureEnabled("adminPanel"));   // false (null = not configured)
console.log(isFeatureEnabled("userLimit"));    // true (100 is truthy)
console.log(isFeatureEnabled("unknown"));      // false (undefined = not in config)
```

### Truthy/Falsy Summary Table

| Value | Truthy or Falsy? |
|---|---|
| `false` | 🔴 Falsy |
| `true` | 🟢 Truthy |
| `0` | 🔴 Falsy |
| `-0` | 🔴 Falsy |
| `1`, `-1`, `42` (any non-zero number) | 🟢 Truthy |
| `Infinity`, `-Infinity` | 🟢 Truthy |
| `NaN` | 🔴 Falsy |
| `""` (empty string) | 🔴 Falsy |
| `"0"`, `"false"`, `" "` (any non-empty string) | 🟢 Truthy |
| `null` | 🔴 Falsy |
| `undefined` | 🔴 Falsy |
| `[]` (empty array) | 🟢 Truthy |
| `{}` (empty object) | 🟢 Truthy |
| `function(){}` | 🟢 Truthy |
| `0n` | 🔴 Falsy |
| `1n` (any non-zero BigInt) | 🟢 Truthy |

---
## Objects vs Primitives: Value vs Reference

We introduced this concept at the beginning of the chapter. Now let's go deeper with examples and explain what happens internally.

### How JavaScript Stores Data in Memory

JavaScript uses two areas of memory:

1. **Stack** — fast, small memory where primitive values are stored directly
2. **Heap** — larger, slower memory where complex objects are stored

**Primitives live on the Stack:**

```javascript
let a = 10;  // The number 10 is stored directly in the variable 'a' on the stack
let b = a;   // A complete copy of 10 is stored in 'b'

// Stack:
// a → 10 (its own box)
// b → 10 (its own separate box)
```

**Objects live on the Heap:**

```javascript
let obj1 = { x: 1 };
// The object { x: 1 } is stored on the HEAP
// The variable 'obj1' on the stack stores only the MEMORY ADDRESS of where the object is

let obj2 = obj1;
// obj2 gets a COPY of the memory ADDRESS — not a copy of the object itself
// Both obj1 and obj2 now point to the SAME object on the heap

// Stack:           Heap:
// obj1 → 0x001 →  { x: 1 }
// obj2 → 0x001 ↗  (same address!)
```

### Demonstrations

**Primitive: Copy by value**

```javascript
let originalScore = 95;
let copiedScore = originalScore; // Copy the VALUE

copiedScore = 0; // Change the copy

console.log(originalScore); // 95 — unchanged! They are independent.
console.log(copiedScore);   // 0

// Modifying one does NOT affect the other.
```

**Object: Copy by reference**

```javascript
let originalUser = { name: "Alice", score: 95 };
let copiedUser = originalUser; // Copy the REFERENCE (the address)

copiedUser.score = 0; // Change through the copy

console.log(originalUser.score); // 0 ← Changed! Both point to same object.
console.log(copiedUser.score);   // 0

// Modifying through one DOES affect the other.
```

### How to Actually Copy an Object (Not Just the Reference)

If you want an independent copy of an object, you need to explicitly create one:

```javascript
let original = { name: "Alice", age: 25 };

// Method 1: Spread operator (shallow copy):
let copy1 = { ...original };
copy1.name = "Bob";
console.log(original.name); // "Alice" — unchanged ✅
console.log(copy1.name);    // "Bob"

// Method 2: Object.assign() (also shallow copy):
let copy2 = Object.assign({}, original);
copy2.name = "Carol";
console.log(original.name); // "Alice" — unchanged ✅
console.log(copy2.name);    // "Carol"

// Method 3: JSON.parse + JSON.stringify (deep copy — but has limitations):
let original2 = { name: "Alice", address: { city: "London" } };
let deepCopy = JSON.parse(JSON.stringify(original2));
deepCopy.address.city = "Paris";
console.log(original2.address.city); // "London" — unchanged ✅
console.log(deepCopy.address.city);  // "Paris"

// ⚠️ JSON method limitations: doesn't copy functions, dates, undefined, or symbols
```

**Shallow vs Deep Copy:**

```javascript
// SHALLOW COPY — only copies the top level:
let user = {
  name: "Alice",
  address: { city: "London" }  // nested object
};

let shallowCopy = { ...user };
shallowCopy.name = "Bob";        // ✅ doesn't affect original (primitive)
shallowCopy.address.city = "Paris"; // ❌ AFFECTS original! (nested object is still shared)

console.log(user.name);         // "Alice" — fine
console.log(user.address.city); // "Paris" — changed! Shallow copy doesn't deep-copy nested objects

// DEEP COPY — copies everything:
let deepCopy = JSON.parse(JSON.stringify(user));
deepCopy.address.city = "Tokyo";
console.log(user.address.city); // "Paris" — unchanged ✅ (deep copy is fully independent)
```

### Comparing Objects

```javascript
// Comparing primitives uses VALUE:
console.log(5 === 5);           // true ✅
console.log("hello" === "hello"); // true ✅

// Comparing objects uses REFERENCE (are they the SAME object in memory?):
let obj1 = { x: 1 };
let obj2 = { x: 1 };
let obj3 = obj1;

console.log(obj1 === obj2); // false! (same content, but DIFFERENT objects in memory)
console.log(obj1 === obj3); // true!  (same object — obj3 points to obj1)

// This means you CANNOT compare objects with === for content equality!
// You need a different approach for content comparison:
console.log(JSON.stringify(obj1) === JSON.stringify(obj2)); // true (but has limitations)
```

### Functions and Reference Types

Functions are objects in JavaScript, which means they are also reference types:

```javascript
// Passing primitives to functions:
function double(num) {
  num = num * 2; // Only changes the LOCAL copy inside the function
  return num;
}

let score = 10;
double(score);
console.log(score); // 10 — UNCHANGED (primitive was copied into the function)

// Passing objects to functions:
function birthday(person) {
  person.age = person.age + 1; // Changes the ACTUAL object (same reference!)
}

let alice = { name: "Alice", age: 25 };
birthday(alice);
console.log(alice.age); // 26 — CHANGED! (object reference was passed in)
```

---

## Immutability of Primitives

### Definition

**Immutability** means that a value **cannot be changed in place**. Primitive values in JavaScript are immutable — once created, the actual value cannot be modified.

When you "change" a primitive variable, you are not changing the original value. You are creating a **new value** and storing it in the variable.

### Why Primitives Are Immutable

This is a fundamental design principle. Primitive values are simple — they represent a single piece of data. Making them immutable means they are safe to share and copy without any unexpected side effects.

### Demonstration

```javascript
let str = "hello";
str.toUpperCase(); // This creates "HELLO" — but does NOT change 'str'!
console.log(str);  // "hello" — still lowercase! The original is untouched.

// To use the new value, you must STORE it:
let upperStr = str.toUpperCase(); // Create new string and save it
console.log(upperStr); // "HELLO" ✅

// You can reassign the variable to point to a new value:
str = "HELLO";         // 'str' now points to a NEW string "HELLO"
console.log(str);      // "HELLO" — the variable changed, not the original string!
```

### String Immutability in Detail

```javascript
let word = "cat";

// Can you change individual characters? No!
word[0] = "b"; // This silently FAILS! Strings are immutable.
console.log(word); // "cat" — unchanged

// Instead, create a new string:
let newWord = "b" + word.slice(1); // "b" + "at" = "bat"
console.log(newWord); // "bat" ✅
console.log(word);    // "cat" — original is untouched

// All string methods return NEW strings, never modify the original:
let original = "  hello world  ";
let trimmed = original.trim();        // New string, no leading/trailing spaces
let replaced = original.replace("hello", "goodbye"); // New string
let upper = original.toUpperCase();   // New string

console.log(original); // "  hello world  " — STILL unchanged after all those operations
console.log(trimmed);  // "hello world"
console.log(replaced); // "  goodbye world  "
console.log(upper);    // "  HELLO WORLD  "
```

### Numbers and Booleans Are Also Immutable

```javascript
let num = 42;
// There is no method that modifies 42 itself — all math operations create new numbers:
let doubled = num * 2; // Creates new number 84
console.log(num);      // 42 — still 42

let flag = true;
let flipped = !flag;   // Creates new boolean: false
console.log(flag);     // true — still true
```

### Why Immutability Matters

```javascript
// Because primitives are immutable and copied by value,
// you can safely share them without worrying about accidental changes:

function applyTax(price, taxRate) {
  // No matter what we do inside, the original 'price' is safe
  return price * (1 + taxRate);
}

let originalPrice = 100;
let taxedPrice = applyTax(originalPrice, 0.08);

console.log(originalPrice); // 100 — safe! The function couldn't have changed it.
console.log(taxedPrice);    // 108
```

---

## Best Practices

### Data Types

```javascript
// ✅ 1. Always use strict equality (===) instead of loose equality (==)
if (score === 0) { }      // ✅ predictable
if (score == false) { }   // ❌ unpredictable coercion

// ✅ 2. Use explicit type conversion, never rely on implicit coercion for important logic
let age = Number(inputField.value);  // ✅ Explicit — your intent is clear
let age2 = +inputField.value;        // ⚠️ Works but less readable
let age3 = inputField.value * 1;     // ❌ Confusing — implicit coercion

// ✅ 3. Always check for NaN after converting user input
let num = Number(userInput);
if (Number.isNaN(num)) {
  console.error("Invalid number");
}

// ✅ 4. Use null (not undefined) for intentional absence of a value
let currentUser = null;  // ✅ Intentionally empty
// let currentUser;       // ❌ Leaves it as undefined — less clear intent

// ✅ 5. Use const for values that won't change, let for those that will
const TAX_RATE = 0.08;   // ✅ Will never change
let cartTotal = 0;        // ✅ Will change as items are added

// ✅ 6. Use template literals for string building
const name = "Alice";
const age = 25;
const bio = `${name} is ${age} years old.`; // ✅ Clean and readable
const bio2 = name + " is " + age + " years old."; // ❌ Messy

// ✅ 7. Check for null/undefined before accessing properties
let user = null;
// ❌ Danger:
// let name = user.name; // TypeError: Cannot read property 'name' of null

// ✅ Safe (optional chaining — ES2020):
let name2 = user?.name;  // undefined (no error!)

// ✅ 8. Prefer ?? over || for default values when 0 and false are valid:
let retryCount = userConfig.retries ?? 3; // Only falls back if null/undefined
```

### Type Checking

```javascript
// ✅ Best ways to check each type:

// Check for string:
typeof value === "string"

// Check for number (and not NaN):
typeof value === "number" && !Number.isNaN(value)

// Check for boolean:
typeof value === "boolean"

// Check for null:
value === null

// Check for undefined:
value === undefined
// or: typeof value === "undefined" (safe for undeclared variables)

// Check for null OR undefined:
value == null   // (the one acceptable use of ==)

// Check for array:
Array.isArray(value)

// Check for plain object (not null, not array):
typeof value === "object" && value !== null && !Array.isArray(value)

// Check for function:
typeof value === "function"
```

---

## Common Mistakes

### Mistake 1: Using == Instead of ===

```javascript
// ❌ Bug-prone:
let input = "0";
if (input == false) {
  // This runs! "0" == false because "" == false → 0 == 0 → true
  // Very confusing!
}

// ✅ Safe:
if (input === false) {
  // This does NOT run — "0" is a string, false is a boolean
}
```

### Mistake 2: Checking for NaN Incorrectly

```javascript
// ❌ NaN is never equal to anything — even itself:
let value = NaN;
if (value === NaN) { /* NEVER runs! */ }
if (value == NaN)  { /* NEVER runs! */ }

// ✅ Correct:
if (Number.isNaN(value)) { console.log("It's NaN!"); } // ✅
if (isNaN(value)) { /* Also works but has coercion issues */ }
```

### Mistake 3: Mutating Objects Unintentionally

```javascript
// ❌ Accidental mutation:
function updateUser(user) {
  user.name = "Updated"; // ← Modifies the ORIGINAL object!
  return user;
}

let myUser = { name: "Alice" };
updateUser(myUser);
console.log(myUser.name); // "Updated" ← Original was changed!

// ✅ Return a new object instead:
function updateUserSafe(user) {
  return { ...user, name: "Updated" }; // Creates a new object
}

let myUser2 = { name: "Alice" };
let updated = updateUserSafe(myUser2);
console.log(myUser2.name); // "Alice" — unchanged ✅
console.log(updated.name); // "Updated" ✅
```

### Mistake 4: Treating typeof null as Reliable

```javascript
// ❌ Wrong:
function isObject(val) {
  return typeof val === "object"; // Returns true for null too! Bug!
}
console.log(isObject(null)); // true ← Wrong!

// ✅ Correct:
function isObject(val) {
  return typeof val === "object" && val !== null;
}
console.log(isObject(null));  // false ✅
console.log(isObject({}));    // true  ✅
```

### Mistake 5: Forgetting That Empty Array/Object Are Truthy

```javascript
// ❌ Common mistake — checking if array has items:
let items = [];

if (items) {
  console.log("Has items"); // This RUNS! [] is truthy, even when empty!
}

// ✅ Correct — check length:
if (items.length > 0) {
  console.log("Has items"); // Only runs when array actually has content ✅
}

// Or:
if (items.length) {
  console.log("Has items"); // 0 is falsy, any positive number is truthy ✅
}
```

### Mistake 6: Floating Point Comparisons

```javascript
// ❌ Direct comparison:
if (0.1 + 0.2 === 0.3) { /* Never runs! */ }

// ✅ Use a tolerance (epsilon):
const EPSILON = Number.EPSILON;
if (Math.abs((0.1 + 0.2) - 0.3) < EPSILON) {
  console.log("Equal enough!"); // ✅
}

// Or use toFixed() for currency:
let total = parseFloat((0.1 + 0.2).toFixed(2));
if (total === 0.30) { /* works */ }
```

### Mistake 7: The + Operator with Mixed Types

```javascript
// ❌ Confusing:
console.log([] + []);   // "" (both arrays become empty string)
console.log([] + {});   // "[object Object]"
console.log({} + []);   // "[object Object]" or 0 (depends on context!)

// ✅ Always be explicit about what you are doing:
// If you mean string concatenation, use template literals:
let result = `${someValue1} ${someValue2}`;

// If you mean addition, make sure both are numbers first:
let sum = Number(val1) + Number(val2);
```

---
## Interview Points

> **📌 Interview Point 1: What are the primitive data types in JavaScript?**

**Answer:** JavaScript has 7 primitive types: `string`, `number`, `boolean`, `undefined`, `null`, `bigint`, and `symbol`. The 8th type is `object`, which is the reference type (including arrays and functions).

---

> **📌 Interview Point 2: What is the difference between == and ===?**

**Answer:**
- `==` (loose equality) performs **type coercion** before comparing — it tries to convert values to the same type, which can lead to surprising results like `1 == "1"` being `true`.
- `===` (strict equality) compares both **value AND type** with no coercion — `1 === "1"` is `false`.
- Always use `===` in production code.

---

> **📌 Interview Point 3: Why does `typeof null === "object"`?**

**Answer:** This is a historical bug from JavaScript's original 1995 implementation. Values were stored with a type tag in memory. `null` was represented as all zeros (a null pointer), which had the same tag as objects (`000`). The `typeof` operator saw the tag and incorrectly returned `"object"`. By the time it was discovered, fixing it would have broken too many existing websites. The bug was kept permanently for backwards compatibility. Always use `=== null` to check for null specifically.

---

> **📌 Interview Point 4: What is type coercion and why can it be dangerous?**

**Answer:** Type coercion is JavaScript's automatic conversion of values from one type to another when mixing types in operations. It can be dangerous because it produces unexpected results silently — for example, `"" == false` is `true`, and `[] + {}` gives `"[object Object]"`. This can cause bugs that are hard to trace. Best practice is to use explicit type conversion (like `Number()`, `String()`, `Boolean()`) and always use `===`.

---

> **📌 Interview Point 5: What are falsy values in JavaScript?**

**Answer:** The falsy values are: `false`, `0`, `-0`, `0n`, `""` (empty string), `null`, `undefined`, and `NaN`. Everything else is truthy — including `"0"` (non-empty string), `[]` (empty array), and `{}` (empty object).

---

> **📌 Interview Point 6: What is the difference between null and undefined?**

**Answer:**
- `undefined` means a variable has been declared but not yet assigned a value. JavaScript sets this automatically.
- `null` is an intentional absence of value, set explicitly by the programmer to indicate "no value here."
- `typeof undefined` is `"undefined"`. `typeof null` is `"object"` (bug).
- `null == undefined` is `true` (loose). `null === undefined` is `false` (strict).

---

> **📌 Interview Point 7: What is the difference between value types and reference types?**

**Answer:** Primitive types (string, number, boolean, etc.) are **value types** — they store the actual value directly in the variable. Copying a primitive creates an independent copy. Reference types (objects, arrays, functions) store a **memory address** — the variable holds a reference to where the object lives in memory. Copying a reference type variable copies the address, so both variables point to the same object. Changes through one are visible through the other.

---

> **📌 Interview Point 8: What is the difference between `isNaN()` and `Number.isNaN()`?**

**Answer:**
- `isNaN(value)` converts the value to a number first, then checks. So `isNaN("hello")` is `true` because `"hello"` converts to `NaN`.
- `Number.isNaN(value)` does NOT convert — it only returns `true` if the value is literally `NaN`. `Number.isNaN("hello")` is `false`.
- `Number.isNaN()` is more precise and is the preferred method.

---

## Exercises

Practice is the only way to truly understand these concepts. Work through each exercise carefully, predict the output before running the code, then verify.

---

### Exercise 1: typeof Predictions ⭐

**Task:** Before running any code, predict what `typeof` will return for each value. Write your predictions, then check.

```javascript
// What will each of these print?
console.log(typeof 42);
console.log(typeof "42");
console.log(typeof true);
console.log(typeof undefined);
console.log(typeof null);
console.log(typeof {});
console.log(typeof []);
console.log(typeof function(){});
console.log(typeof NaN);
console.log(typeof 100n);
console.log(typeof Symbol("test"));
console.log(typeof typeof 42); // ← Tricky! What type does typeof return?
```

<details>
<summary>✅ Solution (click to reveal)</summary>

```javascript
console.log(typeof 42);            // "number"
console.log(typeof "42");          // "string"
console.log(typeof true);          // "boolean"
console.log(typeof undefined);     // "undefined"
console.log(typeof null);          // "object" ← famous bug!
console.log(typeof {});            // "object"
console.log(typeof []);            // "object" ← arrays are objects
console.log(typeof function(){}); // "function"
console.log(typeof NaN);           // "number" ← NaN is a number type!
console.log(typeof 100n);          // "bigint"
console.log(typeof Symbol("test")); // "symbol"
console.log(typeof typeof 42);     // "string" ← typeof always returns a STRING!
// typeof 42 returns "number" (a string), typeof "number" returns "string"
```

</details>

---

### Exercise 2: Coercion Output Prediction ⭐⭐

**Task:** Predict the output of each expression. Explain WHY it gives that result.

```javascript
console.log(1 + "2" + 3);
console.log(1 + 2 + "3");
console.log("5" - 3);
console.log("5" * "3");
console.log(true + true + false);
console.log(null + 1);
console.log(undefined + 1);
console.log("" + 0);
console.log(+"42");
console.log(+true);
console.log(!!"hello");
console.log(!!"");
console.log([] + []);
console.log("3" > 2);
console.log("10" > "9");
```

<details>
<summary>✅ Solution (click to reveal)</summary>

```javascript
console.log(1 + "2" + 3);     // "123"   — 1+"2"="12" (string), "12"+3="123"
console.log(1 + 2 + "3");     // "33"    — 1+2=3 (number), 3+"3"="33"
console.log("5" - 3);         // 2       — "-" coerces "5" to number → 5-3=2
console.log("5" * "3");       // 15      — both strings coerced to numbers → 5*3=15
console.log(true + true + false); // 2   — true=1, true=1, false=0 → 1+1+0=2
console.log(null + 1);        // 1       — null coerces to 0 → 0+1=1
console.log(undefined + 1);   // NaN     — undefined coerces to NaN → NaN+1=NaN
console.log("" + 0);          // "0"     — string + number = string → ""+0="0"
console.log(+"42");            // 42      — unary + converts string to number
console.log(+true);            // 1       — unary + converts true to 1
console.log(!!"hello");        // true    — "hello" is truthy, !truthy=false, !false=true
console.log(!!"");             // false   — "" is falsy, !falsy=true, !true=false
console.log([] + []);          // ""      — both arrays → "" , ""+"" = ""
console.log("3" > 2);         // true    — "3" coerced to 3 → 3 > 2 → true
console.log("10" > "9");      // false   — STRING comparison! "1" < "9" alphabetically
```

</details>

---

### Exercise 3: Truthy/Falsy Function ⭐⭐

**Task:** Write a function called `checkTruthiness` that takes any value and returns a descriptive string explaining whether it is truthy or falsy, and why.

```javascript
// Your function should work like this:
checkTruthiness(0);         // "0 is FALSY — it is the number zero"
checkTruthiness("hello");   // '"hello" is TRUTHY — it is a non-empty string'
checkTruthiness([]);        // "[] is TRUTHY — empty arrays are always truthy"
checkTruthiness(null);      // "null is FALSY — null represents no value"
// ... etc
```

<details>
<summary>💡 Hint</summary>

Use a combination of `typeof`, strict equality checks (`=== null`, `=== undefined`, etc.), `Array.isArray()`, and `Boolean()` to identify the specific type and determine truthiness.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```javascript
function checkTruthiness(value) {
  const isTruthy = Boolean(value);
  const truthLabel = isTruthy ? "TRUTHY" : "FALSY";
  let reason;

  // Identify specific falsy cases:
  if (value === false) {
    reason = "it is the boolean false";
  } else if (value === 0 || Object.is(value, -0)) {
    reason = "it is zero (or negative zero)";
  } else if (value === 0n) {
    reason = "it is BigInt zero";
  } else if (value === "") {
    reason = "it is an empty string";
  } else if (value === null) {
    reason = "null represents intentional absence of value";
  } else if (value === undefined) {
    reason = "undefined means no value was assigned";
  } else if (typeof value === "number" && Number.isNaN(value)) {
    reason = "NaN is always falsy (invalid number result)";
  }

  // Identify truthy cases:
  else if (typeof value === "string") {
    reason = `it is a non-empty string`;
  } else if (typeof value === "number") {
    reason = `it is a non-zero number`;
  } else if (typeof value === "boolean") {
    reason = "it is the boolean true";
  } else if (Array.isArray(value)) {
    reason = "arrays are ALWAYS truthy, even when empty";
  } else if (typeof value === "object") {
    reason = "objects are ALWAYS truthy, even when empty";
  } else if (typeof value === "function") {
    reason = "functions are always truthy";
  } else {
    reason = "it is a non-falsy value";
  }

  return `${JSON.stringify(value)} is ${truthLabel} — ${reason}`;
}

// Test it:
console.log(checkTruthiness(0));          // "0 is FALSY — it is zero (or negative zero)"
console.log(checkTruthiness("hello"));    // '"hello" is TRUTHY — it is a non-empty string'
console.log(checkTruthiness(""));         // '"" is FALSY — it is an empty string'
console.log(checkTruthiness([]));         // '[] is TRUTHY — arrays are ALWAYS truthy...'
console.log(checkTruthiness({}));         // '{} is TRUTHY — objects are ALWAYS truthy...'
console.log(checkTruthiness(null));       // 'null is FALSY — null represents...'
console.log(checkTruthiness(undefined));  // 'undefined is FALSY — undefined means...'
console.log(checkTruthiness(NaN));        // 'null is FALSY — NaN is always falsy...'
console.log(checkTruthiness(42));         // '42 is TRUTHY — it is a non-zero number'
console.log(checkTruthiness(false));      // 'false is FALSY — it is the boolean false'
```

</details>

---

### Exercise 4: Real-World Mini Application ⭐⭐⭐

**Task:** Build a safe user data processor function. It should receive raw input (as it might come from a web form — everything is a string), convert types properly, validate the data, and return either a clean user object or an array of error messages.

Requirements:
- `name`: must be a non-empty string
- `age`: must convert to a valid integer, must be between 1 and 120
- `email`: must be a non-empty string containing `@`
- `isAdmin`: convert `"true"` / `"false"` strings to actual booleans
- `score`: convert to number, default to `0` if not provided or invalid

```javascript
// Expected usage:
let rawInput1 = {
  name: "  Alice  ",
  age: "25",
  email: "alice@example.com",
  isAdmin: "false",
  score: "98.5"
};

let rawInput2 = {
  name: "",
  age: "not a number",
  email: "not-an-email",
  isAdmin: "yes",
  score: ""
};

processUserData(rawInput1);
// Should return: { name: "Alice", age: 25, email: "alice@example.com", isAdmin: false, score: 98.5 }

processUserData(rawInput2);
// Should return error messages for each invalid field
```

<details>
<summary>✅ Solution (click to reveal)</summary>

```javascript
function processUserData(rawInput) {
  const errors = [];
  const result = {};

  // --- Process name ---
  const name = typeof rawInput.name === "string" ? rawInput.name.trim() : "";
  if (!name) { // empty string is falsy
    errors.push("Name is required and cannot be empty.");
  } else {
    result.name = name;
  }

  // --- Process age ---
  const ageRaw = rawInput.age;
  const age = Number(ageRaw);
  if (Number.isNaN(age) || !Number.isInteger(age) || age < 1 || age > 120) {
    errors.push(`Age must be a whole number between 1 and 120. Got: "${ageRaw}"`);
  } else {
    result.age = age;
  }

  // --- Process email ---
  const email = typeof rawInput.email === "string" ? rawInput.email.trim() : "";
  if (!email) {
    errors.push("Email is required.");
  } else if (!email.includes("@")) {
    errors.push(`Email must contain "@". Got: "${email}"`);
  } else {
    result.email = email;
  }

  // --- Process isAdmin ---
  const isAdminRaw = rawInput.isAdmin;
  if (isAdminRaw === "true") {
    result.isAdmin = true;
  } else if (isAdminRaw === "false") {
    result.isAdmin = false;
  } else {
    errors.push(`isAdmin must be "true" or "false". Got: "${isAdminRaw}"`);
  }

  // --- Process score (optional — default to 0) ---
  const scoreRaw = rawInput.score;
  if (scoreRaw === "" || scoreRaw === undefined || scoreRaw === null) {
    result.score = 0; // default value
  } else {
    const score = Number(scoreRaw);
    if (Number.isNaN(score)) {
      errors.push(`Score must be a valid number. Got: "${scoreRaw}"`);
    } else {
      result.score = score;
    }
  }

  // --- Return result or errors ---
  if (errors.length > 0) {
    console.error("Validation failed:");
    errors.forEach((err, i) => console.error(`  ${i + 1}. ${err}`));
    return { success: false, errors };
  }

  console.log("User data processed successfully:", result);
  return { success: true, data: result };
}

// Test 1 — valid input:
processUserData({
  name: "  Alice  ",
  age: "25",
  email: "alice@example.com",
  isAdmin: "false",
  score: "98.5"
});
// User data processed successfully:
// { name: 'Alice', age: 25, email: 'alice@example.com', isAdmin: false, score: 98.5 }

// Test 2 — invalid input:
processUserData({
  name: "",
  age: "not a number",
  email: "not-an-email",
  isAdmin: "yes",
  score: ""
});
// Validation failed:
//   1. Name is required and cannot be empty.
//   2. Age must be a whole number between 1 and 120. Got: "not a number"
//   3. Email must contain "@". Got: "not-an-email"
//   4. isAdmin must be "true" or "false". Got: "yes"
// score defaults to 0 (no error — empty is treated as default)

// Test 3 — edge cases:
processUserData({
  name: "Bob",
  age: "0",          // invalid: 0 is not between 1 and 120
  email: "b@b.com",
  isAdmin: "true",
  score: undefined   // missing — defaults to 0
});
```

</details>

---

## Chapter Summary

Excellent work getting through Chapter 2! Here is a complete review of everything you learned:

### 🧱 Data Types Overview

JavaScript has **8 data types** — 7 primitives and 1 reference type:

| Type | Example | Notes |
|---|---|---|
| `string` | `"hello"` | Text — immutable |
| `number` | `42`, `3.14`, `NaN`, `Infinity` | IEEE 754 double precision |
| `boolean` | `true`, `false` | Yes/No values |
| `undefined` | `undefined` | Not yet assigned |
| `null` | `null` | Intentionally empty |
| `bigint` | `100n` | Integers beyond safe range |
| `symbol` | `Symbol("id")` | Unique identifiers |
| `object` | `{}`, `[]`, functions | Reference type |

### 📦 Primitive vs Reference

| Feature | Primitive | Reference (Object) |
|---|---|---|
| **Stored as** | Direct value | Memory address |
| **Copied as** | Independent copy | Same reference |
| **Mutability** | Immutable | Mutable |
| **Comparison** | By value | By reference (address) |

### 🔍 typeof

- Returns a string describing the type
- Famous bugs: `typeof null === "object"`, `typeof NaN === "number"`, `typeof [] === "object"`
- Use `=== null`, `Array.isArray()`, `Number.isNaN()` for accurate checks

### 🔄 Type Coercion

- **Implicit**: JavaScript converts automatically (e.g., `"5" - 3` = `2`)
- **Explicit**: You convert manually (`Number()`, `String()`, `Boolean()`)
- **Key rule**: `+` with a string does concatenation; other operators do numeric conversion
- **Always prefer explicit coercion** for clarity and safety

### ⚖️ Equality

- `==` does type coercion before comparing — unreliable
- `===` requires same type AND same value — always use this
- `NaN !== NaN` — use `Number.isNaN()` to check for NaN

### ✅❌ Truthy and Falsy

**8 Falsy values:**
`false`, `0`, `-0`, `0n`, `""`, `null`, `undefined`, `NaN`

**Everything else is truthy** — including `"0"`, `[]`, `{}`

Common patterns:
- `value || "default"` — use `||` for fallback values
- `value ?? "default"` — use `??` when `0` and `false` are valid values
- `obj?.property` — optional chaining to safely access properties

### 🔒 Immutability

- Primitive values cannot be changed in place
- All string methods return **new strings** — they never modify the original
- Reassigning a variable just makes it point to a new value

---

### 📌 Key Rules to Remember

```
✅ Always use === (strict equality) instead of ==
✅ Always use explicit type conversion for important logic
✅ Use Number.isNaN() to check for NaN — not NaN === NaN
✅ Use === null to check for null — not typeof
✅ Use Array.isArray() to check for arrays — not typeof
✅ Know your falsy values: false, 0, -0, 0n, "", null, undefined, NaN
✅ Be careful with truthy surprises: "0", [], {} are all TRUTHY
✅ Use ?? instead of || when 0 and false are valid values
✅ Copy objects intentionally with spread {...obj} or deep copy methods
❌ Never rely on implicit coercion in important business logic
❌ Never compare objects with === expecting content equality
❌ Never forget that empty array [] and empty object {} are TRUTHY
```

---

## Next Chapter

Now that you understand what kinds of data JavaScript can work with, we are ready to learn how to **operate on that data** — how to do calculations, compare values, combine conditions, and more.

---

**➡️ [Next Chapter: Operators in JavaScript →](./ch03-operators-and-control-flow.md)**

---

*Last updated: 2024 | Chapter 2 of the Complete JavaScript Guide*

*Found an error or have a suggestion? [Open an issue on GitHub](https://github.com/zaid0091/CodeShelf/issues)*

*← [Previous Chapter: JavaScript Basics](./ch01-javascript-basics.md)*
