---
title: JavaScript Basics
description: Core JavaScript concepts for quick revision
order: 1
tags: [basics, fundamentals]
---

# JavaScript Basics

JavaScript is a dynamic, interpreted language that runs in browsers and on servers (Node.js).

## Variables

```javascript
// let — block-scoped, reassignable
let count = 0;
count = 1;

// const — block-scoped, not reassignable
const PI = 3.14159;

// Avoid var in modern JS (function-scoped, hoisted)
```

## Data Types

```javascript
typeof "hello"    // "string"
typeof 42         // "number"
typeof true       // "boolean"
typeof undefined  // "undefined"
typeof null       // "object" (historical quirk!)
typeof {}         // "object"
typeof []         // "object"
typeof function(){} // "function"
```

## Functions

```javascript
// Function declaration
function add(a, b) {
  return a + b;
}

// Arrow function
const multiply = (a, b) => a * b;

// Default parameters
const greet = (name = "World") => `Hello, ${name}!`;
```

## Destructuring

```javascript
const { name, age } = { name: "Alice", age: 30 };
const [first, second] = [1, 2, 3];

// Spread operator
const merged = { ...obj1, ...obj2 };
const combined = [...arr1, ...arr2];
```

## Truthy & Falsy

Falsy values: `false`, `0`, `""`, `null`, `undefined`, `NaN`

```javascript
const value = input || "default";      // fallback
const value = input ?? "default";      // nullish coalescing (only null/undefined)
const result = condition ? "yes" : "no"; // ternary
```
