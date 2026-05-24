---
title: ES6+ Features
description: Modern JavaScript syntax and features
order: 3
tags: [es6, modern]
---

# ES6+ Features

Essential modern JavaScript features you'll use every day.

## Modules

```javascript
// math.js
export const add = (a, b) => a + b;
export default class Calculator {}

// app.js
import Calculator, { add } from "./math.js";
```

## Classes

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
  speak() {
    return `${this.name} barks`;
  }
}
```

## Optional Chaining & Nullish Coalescing

```javascript
const city = user?.address?.city;       // safe nested access
const name = user?.name ?? "Anonymous"; // default for null/undefined
```

## Array Methods

```javascript
const nums = [1, 2, 3, 4, 5];

nums.map(n => n * 2);           // [2, 4, 6, 8, 10]
nums.filter(n => n > 2);         // [3, 4, 5]
nums.reduce((sum, n) => sum + n, 0); // 15
nums.find(n => n > 3);           // 4
nums.some(n => n > 4);           // true
nums.every(n => n > 0);          // true
```

## Template Literals

```javascript
const name = "Alice";
const msg = `Hello, ${name}!`;
const multiline = `
  Line 1
  Line 2
`;
```

## Map & Set

```javascript
const map = new Map([["key", "value"]]);
map.set("foo", "bar");
map.get("foo"); // "bar"

const set = new Set([1, 2, 2, 3]); // {1, 2, 3}
```
