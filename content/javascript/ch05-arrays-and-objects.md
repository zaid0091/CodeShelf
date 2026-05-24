---
title: Arrays and Objects
description: Array methods, object literals, destructuring, spread, and rest in JavaScript
order: 5
tags: [javascript, arrays, objects, destructuring, spread, map, filter]
---

# Chapter 5: Arrays and Objects

## 5.1 Arrays — ordered lists

```javascript
const fruits = ["apple", "banana", "cherry"];

console.log(fruits[0]);       // "apple"
console.log(fruits.length);   // 3
fruits.push("date");          // add to end
fruits.unshift("apricot");    // add to start
const last = fruits.pop();    // remove from end
```

| Method | Mutates? | Returns |
|--------|----------|---------|
| `push(el)` | Yes | New length |
| `pop()` | Yes | Removed element |
| `shift()` | Yes | Removed first |
| `unshift(el)` | Yes | New length |
| `splice(i, n, ...items)` | Yes | Removed items |
| `slice(start, end)` | No | New array |
| `concat(...arrs)` | No | New array |

## 5.2 Iteration methods (essential)

```javascript
const nums = [1, 2, 3, 4, 5];

// forEach — side effects, no return
nums.forEach((n, i) => console.log(i, n));

// map — transform → new array
const doubled = nums.map((n) => n * 2);

// filter — keep matching items
const evens = nums.filter((n) => n % 2 === 0);

// reduce — single accumulated value
const sum = nums.reduce((acc, n) => acc + n, 0);

// find / findIndex — first match
const firstBig = nums.find((n) => n > 3);       // 4
const idx = nums.findIndex((n) => n > 3);       // 3

// some / every — boolean tests
nums.some((n) => n > 4);   // true
nums.every((n) => n > 0);  // true

// includes
nums.includes(3);          // true
```

### Chaining

```javascript
const result = users
  .filter((u) => u.active)
  .map((u) => u.name)
  .sort();
```

## 5.3 Sorting and reversing

```javascript
const words = ["banana", "apple", "cherry"];
words.sort(); // lexicographic: ["apple", "banana", "cherry"]

const numbers = [10, 2, 30];
numbers.sort(); // [10, 2, 30] — converts to strings!

numbers.sort((a, b) => a - b); // [2, 10, 30] numeric sort
```

## 5.4 Objects — key-value collections

```javascript
const user = {
  id: 1,
  name: "Alice",
  email: "alice@example.com",
  isAdmin: false,
};

// Access
user.name;
user["email"];

// Add / update
user.lastLogin = new Date();
user["isAdmin"] = true;

// Delete
delete user.email;

// Check key
"name" in user;                    // true
Object.hasOwn(user, "name");       // true (preferred)
```

## 5.5 Object methods and `this`

```javascript
const calculator = {
  value: 0,
  add(n) {
    this.value += n;
    return this;
  },
  reset() {
    this.value = 0;
    return this;
  },
};

calculator.add(5).add(3).value; // 8
```

## 5.6 Destructuring

### Array destructuring

```javascript
const [first, second, ...rest] = [1, 2, 3, 4];
// first: 1, second: 2, rest: [3, 4]

const [, , third] = [1, 2, 3]; // skip elements

let a = 1, b = 2;
[a, b] = [b, a]; // swap
```

### Object destructuring

```javascript
const { name, age, country = "US" } = user;

// Rename
const { name: userName } = user;

// Nested
const { address: { city } } = { address: { city: "NYC" } };
```

### In function parameters

```javascript
function display({ name, age }) {
  console.log(`${name} (${age})`);
}
```

## 5.7 Spread operator (`...`)

```javascript
// Arrays
const arr1 = [1, 2];
const arr2 = [...arr1, 3, 4]; // [1, 2, 3, 4]

// Objects — shallow copy + merge
const defaults = { theme: "light", lang: "en" };
const prefs = { ...defaults, theme: "dark" };

// Clone (shallow)
const copy = { ...user };
```

## 5.8 Rest in destructuring and parameters

```javascript
const { id, ...profile } = user; // profile = all except id

function logAll(first, ...others) {
  console.log(first, others);
}
```

## 5.9 `Object` static methods

```javascript
Object.keys(user);     // ["id", "name", ...]
Object.values(user);   // [1, "Alice", ...]
Object.entries(user);  // [["id", 1], ["name", "Alice"], ...]

const fromEntries = Object.fromEntries([
  ["a", 1],
  ["b", 2],
]);

Object.assign({}, user, { role: "admin" }); // merge (mutates target)
```

## 5.10 JSON — data interchange

```javascript
const json = JSON.stringify(user);
const parsed = JSON.parse(json);

// Dates become strings in JSON
JSON.stringify({ date: new Date() });
```

See [Chapter 11: Browser APIs](./ch11-browser-apis.md) for `fetch` + JSON patterns.

## 5.11 Array extras (ES6+)

```javascript
Array.from("abc");           // ["a", "b", "c"]
Array.from({ length: 3 }, (_, i) => i); // [0, 1, 2]

const flat = [1, [2, [3]]].flat(2);      // [1, 2, 3]

const set = new Set([1, 2, 2, 3]);
[...set];                                 // [1, 2, 3]
```

## 5.12 Immutability patterns

```javascript
// Add to array without mutating
const updated = [...todos, newTodo];

// Update one item
const toggled = todos.map((t) =>
  t.id === id ? { ...t, done: !t.done } : t
);

// Remove item
const filtered = todos.filter((t) => t.id !== id);
```

## 5.13 Chapter summary

| Tool | Use when |
|------|----------|
| `map` | Transform each element |
| `filter` | Select subset |
| `reduce` | Aggregate to one value |
| Spread | Copy/merge arrays and objects |
| Destructuring | Extract fields cleanly |

## Exercises

### Exercise 5.1 — Stats

Given `const scores = [88, 92, 75, 100, 63]`, use array methods to compute average, highest, and passing count (≥ 70).

### Exercise 5.2 — User list

Map `users` to an array of `"Name <email>"` strings for active users only.

### Exercise 5.3 — Group by

Write `groupBy(arr, keyFn)` returning an object keyed by `keyFn(item)`.

### Exercise 5.4 — Immutable update

Given `const state = { items: [{ id: 1, qty: 2 }] }`, return a new state with item 1 qty incremented by 1 without mutating `state`.

---

**Previous:** [Chapter 4: Functions](./ch04-functions.md) · **Next:** [Chapter 6: ES6+ Modern Features](./ch06-es6-modern-features.md)
