---
title: Arrays and Objects in JavaScript
description: A complete guide to arrays, objects, destructuring, spread/rest, iteration, and real-world data patterns in JavaScript
order: 5
tags: [javascript, arrays, objects, destructuring, spread, rest, iteration, methods]
---

# Chapter 5: Arrays and Objects in JavaScript

> **"If functions are the muscles of JavaScript, arrays and objects are the skeleton — they hold everything together."**

---

## Table of Contents

1. [What is an Array?](#what-is-an-array)
2. [Creating Arrays](#creating-arrays)
3. [Accessing and Modifying Array Elements](#accessing-and-modifying-array-elements)
4. [Core Array Methods](#core-array-methods)
   - [Adding and Removing](#adding-and-removing)
   - [Searching](#searching)
   - [Transforming](#transforming)
   - [Iterating](#iterating)
   - [Sorting and Reversing](#sorting-and-reversing)
   - [Flattening](#flattening)
5. [What is an Object?](#what-is-an-object)
6. [Creating Objects](#creating-objects)
7. [Accessing and Modifying Object Properties](#accessing-and-modifying-object-properties)
8. [Object Methods](#object-methods)
9. [Computed Property Names](#computed-property-names)
10. [Destructuring](#destructuring)
    - [Array Destructuring](#array-destructuring)
    - [Object Destructuring](#object-destructuring)
11. [Spread Operator](#spread-operator)
12. [Rest in Arrays and Objects](#rest-in-arrays-and-objects)
13. [Nested Arrays and Objects](#nested-arrays-and-objects)
14. [Arrays of Objects (The Real-World Pattern)](#arrays-of-objects-the-real-world-pattern)
15. [Cloning vs Referencing](#cloning-vs-referencing)
16. [Common Mistakes](#common-mistakes)
17. [Best Practices](#best-practices)
18. [Interview Points](#interview-points)
19. [Debugging Tips](#debugging-tips)
20. [Exercises](#exercises)
21. [Chapter Summary](#chapter-summary)

---

## What is an Array?

### Definition

An **array** is an ordered, numbered list that can hold multiple values inside one variable.


### Explanation

Imagine you are building a shopping app. A user has 5 items in their cart.
Without arrays, you would need 5 separate variables:

```js
const item1 = "Apple";
const item2 = "Banana";
const item3 = "Milk";
const item4 = "Bread";
const item5 = "Eggs";
```

Now imagine a user adds 100 items. You cannot write 100 variables. That is
where arrays help. An array lets you store all values in **one place**, in
a specific **order**, and work with them using a single variable name.

Arrays are **ordered** (each item has a position), **zero-indexed** (positions
start from `0`, not `1`), and **dynamic** (you can add or remove items at any
time).

### Internal Working (Simple Terms)

Think of an array like a **row of numbered boxes**:

```
Index:   0        1        2        3        4
Value: "Apple" "Banana" "Milk"  "Bread"  "Eggs"
```

Each box has a number (called an **index**). You use the index to reach inside
and get the value. JavaScript starts counting from `0`, not `1` — this is one
of the most common beginner confusions, so remember it well.

### Why Arrays Exist

- Store **collections of related data** in one variable
- Loop over data without repeating yourself
- Use powerful built-in methods to search, transform, and sort data
- Represent real-world lists: users, products, messages, comments

---

## Creating Arrays

### Definition

You create an array by writing values separated by commas inside square brackets `[]`.


### Syntax

```js
// Empty array
const empty = [];

// Array of numbers
const scores = [95, 87, 72, 61, 88];

// Array of strings
const fruits = ["Apple", "Banana", "Cherry"];

// Array of mixed types (allowed but not recommended)
const mixed = [42, "hello", true, null, { name: "Alice" }];

// Array of arrays (nested)
const matrix = [[1, 2], [3, 4], [5, 6]];
```

### The `new Array()` Syntax (Less Common)

```js
// Creates an array with 3 empty slots — confusing and rarely used
const arr = new Array(3);
console.log(arr); // [ <3 empty items> ]

// PREFERRED: always use the literal syntax []
const arr = [1, 2, 3];
```

> ⚠️ **Warning:** Prefer `[]` over `new Array()`. It is shorter, clearer, and
> avoids a confusing edge case where `new Array(3)` creates 3 empty slots
> instead of an array with the number 3.

### Real-World Example

```js
// Shopping cart items
const cart = ["Laptop", "Mouse", "Keyboard", "Monitor"];

// User IDs in a system
const activeUserIds = [1042, 1088, 1101, 2003];

// To-do list items
const todos = [
  "Write unit tests",
  "Fix login bug",
  "Deploy to staging",
  "Review pull request"
];
```

### Interview Points

- Arrays in JavaScript are **objects** under the hood (`typeof [] === "object"`)
- Use `Array.isArray(value)` to properly check if something is an array
- JavaScript arrays are **dynamic** — no fixed size like in some other languages
- Arrays can hold **any data type**, including other arrays and objects

---

## Accessing and Modifying Array Elements

### Definition

You access an array item by writing the array name followed by its **index number** in square brackets: `array[index]`.


### Reading Values

```js
const colors = ["red", "green", "blue", "yellow"];

console.log(colors[0]); // "red"    — first item (index 0)
console.log(colors[1]); // "green"  — second item (index 1)
console.log(colors[2]); // "blue"   — third item (index 2)
console.log(colors[3]); // "yellow" — fourth item (index 3)
console.log(colors[4]); // undefined — no item at index 4!
```

### Getting the Last Element

```js
const colors = ["red", "green", "blue", "yellow"];

// Classic way
console.log(colors[colors.length - 1]); // "yellow"

// Modern way (ES2022)
console.log(colors.at(-1)); // "yellow" — negative index counts from the end
console.log(colors.at(-2)); // "blue"
```

### Modifying Values

Arrays declared with `const` can still have their **items changed**. `const`
only prevents you from reassigning the variable to a completely new array.

```js
const fruits = ["Apple", "Banana", "Cherry"];

// Change a value at a specific index
fruits[1] = "Mango";
console.log(fruits); // ["Apple", "Mango", "Cherry"]

// Add a new item at a specific index
fruits[3] = "Grape";
console.log(fruits); // ["Apple", "Mango", "Cherry", "Grape"]
```

### The `length` Property

```js
const animals = ["Cat", "Dog", "Bird"];

console.log(animals.length); // 3 — always one more than the last index

// Shortcut: get last item
console.log(animals[animals.length - 1]); // "Bird"
```

### Common Mistakes

```js
// ❌ WRONG: Off-by-one error — first item is index 0, not 1
const items = ["a", "b", "c"];
console.log(items[1]); // "b" — NOT "a"!

// ✅ CORRECT
console.log(items[0]); // "a" — first item is always index 0

// ❌ WRONG: Assuming length gives last index
const nums = [10, 20, 30];
console.log(nums[nums.length]); // undefined — length is 3, last index is 2

// ✅ CORRECT
console.log(nums[nums.length - 1]); // 30
```

---

## Core Array Methods

JavaScript arrays come with dozens of powerful built-in methods. Think of them
as tools that help you work with lists without writing everything manually.

---

### Adding and Removing

#### `.push()` — Add to End

```js
const fruits = ["Apple", "Banana"];

fruits.push("Cherry");         // add one item
fruits.push("Date", "Elderberry"); // add multiple items at once
console.log(fruits); // ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

// .push() returns the new length
const newLength = fruits.push("Fig");
console.log(newLength); // 6
```

#### `.pop()` — Remove from End

```js
const fruits = ["Apple", "Banana", "Cherry"];

const removed = fruits.pop(); // removes and returns the last item
console.log(removed); // "Cherry"
console.log(fruits);  // ["Apple", "Banana"]
```

#### `.unshift()` — Add to Beginning

```js
const fruits = ["Banana", "Cherry"];

fruits.unshift("Apple");         // add to the front
console.log(fruits); // ["Apple", "Banana", "Cherry"]
```

#### `.shift()` — Remove from Beginning

```js
const fruits = ["Apple", "Banana", "Cherry"];

const removed = fruits.shift(); // removes and returns the first item
console.log(removed); // "Apple"
console.log(fruits);  // ["Banana", "Cherry"]
```

#### `.splice()` — Add or Remove Anywhere

```js
// splice(startIndex, deleteCount, ...itemsToInsert)

const colors = ["red", "green", "blue", "yellow"];

// Remove 1 item at index 2
colors.splice(2, 1);
console.log(colors); // ["red", "green", "yellow"]

// Remove 0 items but INSERT "purple" at index 1
colors.splice(1, 0, "purple");
console.log(colors); // ["red", "purple", "green", "yellow"]

// Replace: remove 1 item at index 0, insert "orange"
colors.splice(0, 1, "orange");
console.log(colors); // ["orange", "purple", "green", "yellow"]
```

#### Quick Reference: Add / Remove Methods

| Method | Where | Returns | Mutates Original? |
|--------|-------|---------|------------------|
| `.push(...items)` | End | New length | ✅ Yes |
| `.pop()` | End | Removed item | ✅ Yes |
| `.unshift(...items)` | Beginning | New length | ✅ Yes |
| `.shift()` | Beginning | Removed item | ✅ Yes |
| `.splice(i, n, ...items)` | Anywhere | Array of removed items | ✅ Yes |

---

### Searching

#### `.indexOf()` — Find First Position

```js
const fruits = ["Apple", "Banana", "Cherry", "Banana"];

console.log(fruits.indexOf("Banana"));    // 1 — first occurrence
console.log(fruits.indexOf("Grape"));     // -1 — not found
console.log(fruits.lastIndexOf("Banana")); // 3 — last occurrence
```

#### `.includes()` — Check If Exists

```js
const roles = ["admin", "editor", "viewer"];

console.log(roles.includes("admin"));   // true
console.log(roles.includes("manager")); // false

// Practical use
if (roles.includes("admin")) {
  console.log("Access granted");
}
```

#### `.find()` — Get First Matching Item

```js
const users = [
  { id: 1, name: "Alice" },
  { id: 2, name: "Bob" },
  { id: 3, name: "Carol" }
];

// Find the first user whose id is 2
const user = users.find(u => u.id === 2);
console.log(user); // { id: 2, name: "Bob" }

// If nothing found, returns undefined
const notFound = users.find(u => u.id === 99);
console.log(notFound); // undefined
```

#### `.findIndex()` — Get Position of First Match

```js
const users = [
  { id: 1, name: "Alice" },
  { id: 2, name: "Bob" }
];

const index = users.findIndex(u => u.name === "Bob");
console.log(index); // 1

// Useful when you need to remove or update an item by condition
users.splice(index, 1); // remove Bob
console.log(users); // [{ id: 1, name: "Alice" }]
```

#### `.some()` — Does At Least One Match?

```js
const ages = [15, 22, 17, 30, 13];

const hasAdult = ages.some(age => age >= 18); // true if ANY age >= 18
console.log(hasAdult); // true
```

#### `.every()` — Do ALL Match?

```js
const ages = [22, 25, 30, 19];

const allAdults = ages.every(age => age >= 18); // true only if ALL >= 18
console.log(allAdults); // true

const ages2 = [22, 15, 30];
console.log(ages2.every(age => age >= 18)); // false — 15 fails
```

---

### Transforming

#### `.map()` — Transform Every Item

`.map()` creates a **brand new array** by applying a function to every element.
The original array is never changed.

```js
const prices = [10, 20, 30, 40];

// Apply 10% discount to every price
const discounted = prices.map(price => price * 0.9);
console.log(discounted); // [9, 18, 27, 36]
console.log(prices);     // [10, 20, 30, 40] — original unchanged ✅

// Real-world: transform API data for display
const users = [
  { firstName: "Alice", lastName: "Smith" },
  { firstName: "Bob", lastName: "Jones" }
];

const fullNames = users.map(u => `${u.firstName} ${u.lastName}`);
console.log(fullNames); // ["Alice Smith", "Bob Jones"]
```

#### `.filter()` — Keep Only Matching Items

`.filter()` creates a **new array** with only the items that pass the test
function (the function returns `true` to keep, `false` to remove).

```js
const scores = [45, 82, 60, 95, 38, 71];

// Keep only passing scores (60 or above)
const passing = scores.filter(score => score >= 60);
console.log(passing); // [82, 60, 95, 71]
console.log(scores);  // [45, 82, 60, 95, 38, 71] — unchanged ✅

// Real-world: filter active users
const users = [
  { name: "Alice", active: true },
  { name: "Bob", active: false },
  { name: "Carol", active: true }
];

const activeUsers = users.filter(u => u.active);
console.log(activeUsers); // [{ name: "Alice"... }, { name: "Carol"... }]
```

#### `.reduce()` — Combine All Items Into One Value

`.reduce()` is the most powerful but also the trickiest. It takes all items
and **accumulates** them into a single result (a number, string, object,
or even an array).

```js
// reduce(callback, initialValue)
// callback receives: (accumulator, currentItem, index, array)

const numbers = [1, 2, 3, 4, 5];

// Sum all numbers
const sum = numbers.reduce((total, num) => total + num, 0);
// Step by step: 0+1=1, 1+2=3, 3+3=6, 6+4=10, 10+5=15
console.log(sum); // 15

// Find the maximum value
const max = numbers.reduce((biggest, num) =>
  num > biggest ? num : biggest, numbers[0]
);
console.log(max); // 5

// Real-world: count occurrences of each item
const votes = ["Alice", "Bob", "Alice", "Carol", "Alice", "Bob"];

const tally = votes.reduce((counts, vote) => {
  counts[vote] = (counts[vote] || 0) + 1; // increment or start at 1
  return counts;
}, {}); // start with empty object

console.log(tally); // { Alice: 3, Bob: 2, Carol: 1 }
```

#### `.slice()` — Extract Part of an Array (Non-Destructive)

```js
const letters = ["a", "b", "c", "d", "e"];

// slice(startIndex, endIndex) — endIndex is NOT included
console.log(letters.slice(1, 3)); // ["b", "c"]
console.log(letters.slice(2));    // ["c", "d", "e"] — to the end
console.log(letters.slice(-2));   // ["d", "e"] — last 2 items
console.log(letters);             // ["a","b","c","d","e"] — unchanged ✅
```

#### `.concat()` — Merge Arrays

```js
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const arr3 = [7, 8, 9];

const merged = arr1.concat(arr2, arr3);
console.log(merged); // [1, 2, 3, 4, 5, 6, 7, 8, 9]
console.log(arr1);   // [1, 2, 3] — unchanged ✅

// Modern way using spread (covered later)
const merged2 = [...arr1, ...arr2, ...arr3];
```

#### `.join()` — Convert Array to String

```js
const words = ["Hello", "World", "from", "JavaScript"];

console.log(words.join(" "));  // "Hello World from JavaScript"
console.log(words.join("-"));  // "Hello-World-from-JavaScript"
console.log(words.join(""));   // "HelloWorldfromJavaScript"

// Practical: build CSV row
const row = ["Alice", "30", "Engineer"];
console.log(row.join(",")); // "Alice,30,Engineer"
```

---

### Iterating

#### `.forEach()` — Run Code for Each Item

`.forEach()` is like a `for` loop but cleaner. It runs a function on every
item. It does **not** return a new array — it is used purely for **side effects**
like logging, updating the DOM, or sending data.

```js
const tasks = ["Write code", "Test code", "Deploy code"];

tasks.forEach((task, index) => {
  console.log(`${index + 1}. ${task}`);
});
// 1. Write code
// 2. Test code
// 3. Deploy code
```

#### `for...of` — Loop Over Values

The cleanest way to loop over array items when you need to use `break` or
`continue` (which `forEach` does not support).

```js
const scores = [88, 55, 92, 45, 76];

for (const score of scores) {
  if (score < 60) {
    console.log(score + " — Failing");
    continue; // skip to next iteration
  }
  console.log(score + " — Passing");
}
```

#### `for...in` — Loop Over Keys (Use with Caution on Arrays)

> ⚠️ **Warning:** `for...in` is designed for **objects**, not arrays. It can
> behave unexpectedly with arrays — use `for...of` or `.forEach()` instead.

---

### Sorting and Reversing

#### `.sort()` — Sort Items

> ⚠️ **Warning:** By default, `.sort()` converts items to **strings** and
> sorts alphabetically. This gives wrong results for numbers!

```js
// ❌ Default sort — wrong for numbers!
const nums = [10, 1, 21, 2];
nums.sort();
console.log(nums); // [1, 10, 2, 21] — sorts as strings, not numbers!

// ✅ CORRECT: pass a comparison function for numbers
nums.sort((a, b) => a - b);   // ascending
console.log(nums); // [1, 2, 10, 21]

nums.sort((a, b) => b - a);   // descending
console.log(nums); // [21, 10, 2, 1]
```

**How the comparison function works:**

| Return Value | Behavior |
|-------------|----------|
| `a - b < 0` | `a` comes **before** `b` (a is smaller) |
| `a - b > 0` | `b` comes **before** `a` (b is smaller) |
| `a - b = 0` | Order unchanged |

```js
// Sort strings alphabetically
const fruits = ["Banana", "Apple", "Cherry", "Date"];
fruits.sort(); // default works fine for strings
console.log(fruits); // ["Apple", "Banana", "Cherry", "Date"]

// Sort objects by a property
const users = [
  { name: "Carol", age: 28 },
  { name: "Alice", age: 35 },
  { name: "Bob", age: 22 }
];

// Sort by age ascending
users.sort((a, b) => a.age - b.age);
console.log(users);
// [{name: "Bob", age: 22}, {name: "Carol", age: 28}, {name: "Alice", age: 35}]
```

#### `.reverse()` — Reverse the Array

```js
const letters = ["a", "b", "c", "d"];
letters.reverse();
console.log(letters); // ["d", "c", "b", "a"]

// Note: .reverse() mutates the original array!
// To reverse without mutating:
const original = [1, 2, 3, 4, 5];
const reversed = [...original].reverse(); // spread first to copy
console.log(original); // [1, 2, 3, 4, 5] — untouched
console.log(reversed); // [5, 4, 3, 2, 1]
```

---

### Flattening

#### `.flat()` — Flatten Nested Arrays

```js
const nested = [1, 2, [3, 4], [5, [6, 7]]];

console.log(nested.flat());    // [1, 2, 3, 4, 5, [6, 7]] — one level deep
console.log(nested.flat(2));   // [1, 2, 3, 4, 5, 6, 7]   — two levels deep
console.log(nested.flat(Infinity)); // fully flatten no matter how deep
```

#### `.flatMap()` — Map Then Flatten

```js
// Like doing .map() then .flat(1) in one step
const sentences = ["Hello World", "Foo Bar"];

const words = sentences.flatMap(sentence => sentence.split(" "));
console.log(words); // ["Hello", "World", "Foo", "Bar"]
```

---

## What is an Object?

### Definition

An **object** is a collection of **key-value pairs** where each key is a name (string) and each value can be any data type.


### Explanation

While arrays store ordered lists, objects store **named data**. Think about a
real-world user profile: they have a name, age, email, and job title. These
properties are different types and don't have a natural order — they have
**names**. Objects are perfect for this.

```
Key        Value
------     -------
name    → "Alice"
age     → 30
email   → "alice@example.com"
active  → true
```

### Why Objects Exist

- Model **real-world entities**: users, products, orders, settings
- Group **related data** that describes one thing
- Store **configuration**: API keys, options, defaults
- Represent **structured data** from APIs (JSON)

---

## Creating Objects

### Object Literal (Most Common)

```js
// Basic object
const user = {
  name: "Alice",          // key: "name", value: "Alice"
  age: 30,                // key: "age", value: 30
  email: "alice@ex.com",  // key: "email", value: "alice@ex.com"
  isActive: true          // key: "isActive", value: true
};
```

### Empty Object

```js
const config = {}; // empty, can add properties later
config.theme = "dark";
config.language = "en";
```

### Object with Method (Function as Value)

```js
const calculator = {
  brand: "MathPro",
  add: function(a, b) { return a + b; },   // method (old style)
  subtract(a, b) { return a - b; },        // method (shorthand — preferred)
  multiply: (a, b) => a * b                // arrow function method
};

console.log(calculator.add(5, 3));      // 8
console.log(calculator.subtract(9, 4)); // 5
```

---

## Accessing and Modifying Object Properties

### Dot Notation (Most Common)

```js
const person = { name: "Bob", age: 25, city: "NYC" };

// Read
console.log(person.name); // "Bob"
console.log(person.age);  // 25

// Write
person.age = 26;           // update existing property
person.email = "b@b.com";  // add new property
console.log(person); // { name: "Bob", age: 26, city: "NYC", email: "b@b.com" }

// Delete
delete person.city;
console.log(person); // { name: "Bob", age: 26, email: "b@b.com" }
```

### Bracket Notation

Use bracket notation when:
- The property name is stored in a **variable**
- The key has **spaces or special characters**
- The key is **dynamic** (computed at runtime)

```js
const person = { name: "Alice", "favorite color": "blue" };

// Access with a variable key
const key = "name";
console.log(person[key]);               // "Alice"

// Access key with spaces (dot notation won't work here)
console.log(person["favorite color"]);  // "blue"

// Dynamic property access
function getProperty(obj, propName) {
  return obj[propName]; // can't use dot notation here
}
console.log(getProperty(person, "name")); // "Alice"
```

### Optional Chaining `?.` (Modern — Very Important)

When you are not sure if a property exists, use `?.` to avoid errors:

```js
const user = { address: { city: "NYC" } };
const user2 = {};

// ❌ Without optional chaining — crashes if address is missing
console.log(user2.address.city); // TypeError: Cannot read property 'city' of undefined

// ✅ With optional chaining — returns undefined safely
console.log(user2?.address?.city); // undefined (no error)
console.log(user?.address?.city);  // "NYC"
```

### Checking If a Property Exists

```js
const config = { theme: "dark", fontSize: 16 };

// in operator — checks anywhere in the object (including prototype)
console.log("theme" in config);    // true
console.log("color" in config);    // false

// hasOwnProperty — checks only own properties (safer)
console.log(config.hasOwnProperty("theme")); // true

// Check if value is undefined
console.log(config.language === undefined);  // true — property doesn't exist
```

---

## Object Methods

JavaScript provides several powerful static methods on the `Object` class.

#### `Object.keys()` — Get All Keys

```js
const product = { id: 1, name: "Laptop", price: 999 };

const keys = Object.keys(product);
console.log(keys); // ["id", "name", "price"]
```

#### `Object.values()` — Get All Values

```js
const product = { id: 1, name: "Laptop", price: 999 };

const values = Object.values(product);
console.log(values); // [1, "Laptop", 999]
```

#### `Object.entries()` — Get Key-Value Pairs as Arrays

```js
const product = { id: 1, name: "Laptop", price: 999 };

const entries = Object.entries(product);
console.log(entries);
// [["id", 1], ["name", "Laptop"], ["price", 999]]

// Loop over an object cleanly using entries
for (const [key, value] of Object.entries(product)) {
  console.log(`${key}: ${value}`);
}
// id: 1
// name: Laptop
// price: 999
```

#### `Object.assign()` — Copy / Merge Objects

```js
const defaults = { theme: "light", fontSize: 14, language: "en" };
const userPrefs = { theme: "dark", fontSize: 18 };

// Merge userPrefs ON TOP of defaults
const finalConfig = Object.assign({}, defaults, userPrefs);
console.log(finalConfig);
// { theme: "dark", fontSize: 18, language: "en" }

// Note: {} as first arg prevents mutation of defaults
```

#### `Object.freeze()` — Make Object Immutable

```js
const config = Object.freeze({ MAX_RETRIES: 3, TIMEOUT: 5000 });

config.MAX_RETRIES = 10; // silently fails in normal mode
console.log(config.MAX_RETRIES); // still 3 — freeze worked

// Practical use: constants that must never change
```

#### `Object.fromEntries()` — Convert Array of Pairs to Object

```js
const entries = [["name", "Alice"], ["age", 30], ["city", "NYC"]];

const obj = Object.fromEntries(entries);
console.log(obj); // { name: "Alice", age: 30, city: "NYC" }

// Powerful with Map
const map = new Map([["a", 1], ["b", 2]]);
const fromMap = Object.fromEntries(map);
console.log(fromMap); // { a: 1, b: 2 }
```

---

## Computed Property Names

### Definition

You can use a **variable or expression** as a property name in an object literal by wrapping it in square brackets `[]`.


```js
const fieldName = "email";
const prefix = "user";

const person = {
  name: "Alice",
  [fieldName]: "alice@example.com",   // uses value of fieldName variable
  [`${prefix}Id`]: 42                 // "userId": 42
};

console.log(person.email);  // "alice@example.com"
console.log(person.userId); // 42
```

### Real-World Example

```js
// Dynamically update a form field in state
function updateField(state, fieldName, value) {
  return {
    ...state,                   // keep all existing fields
    [fieldName]: value          // update only the specified field
  };
}

const formState = { name: "", email: "", age: "" };
const updated = updateField(formState, "email", "alice@ex.com");
console.log(updated); // { name: "", email: "alice@ex.com", age: "" }
```

---

## Destructuring

### Array Destructuring

### Definition

Array destructuring lets you **unpack array values into separate variables** in one clean line, using position.


#### Why It Exists

Instead of writing `const a = arr[0]; const b = arr[1];` multiple times,
destructuring lets you do it all at once in a readable way.

```js
const rgb = [255, 128, 0];

// ❌ Without destructuring
const red = rgb[0];
const green = rgb[1];
const blue = rgb[2];

// ✅ With destructuring
const [red, green, blue] = rgb;
console.log(red, green, blue); // 255 128 0
```

#### Skip Items

```js
const [first, , third] = [10, 20, 30]; // skip the second item with a comma
console.log(first, third); // 10 30
```

#### Default Values in Destructuring

```js
const [a = 0, b = 0, c = 0] = [10, 20]; // c is missing, so it uses default 0
console.log(a, b, c); // 10 20 0
```

#### Swap Variables (Classic Trick)

```js
let x = 1;
let y = 2;

// ❌ Old way: needs a temp variable
const temp = x;
x = y;
y = temp;

// ✅ Modern: one-line swap
[x, y] = [y, x];
console.log(x, y); // 2 1
```

#### Real-World: Function Returning Multiple Values

```js
function getRange(numbers) {
  const sorted = [...numbers].sort((a, b) => a - b);
  return [sorted[0], sorted[sorted.length - 1]]; // return [min, max]
}

const [min, max] = getRange([3, 7, 1, 9, 4]);
console.log(min, max); // 1 9
```

---

### Object Destructuring

### Definition

Object destructuring lets you **unpack object properties into variables** using their key names, not position.


```js
const user = {
  name: "Alice",
  age: 30,
  email: "alice@example.com",
  city: "NYC"
};

// ❌ Without destructuring
const name = user.name;
const age = user.age;

// ✅ With destructuring
const { name, age, email } = user;
console.log(name, age, email); // "Alice" 30 "alice@example.com"
```

#### Rename While Destructuring

```js
const { name: fullName, age: yearsOld } = user;
console.log(fullName, yearsOld); // "Alice" 30
// 'name' and 'age' do NOT exist as variables — only 'fullName' and 'yearsOld' do
```

#### Default Values

```js
const { name, role = "guest", theme = "light" } = user;
console.log(role);  // "guest" — wasn't in user object, used default
console.log(theme); // "light" — wasn't in user object, used default
```

#### Nested Destructuring

```js
const profile = {
  user: {
    name: "Bob",
    address: {
      city: "LA",
      zip: "90001"
    }
  }
};

// Destructure nested properties
const { user: { name, address: { city } } } = profile;
console.log(name, city); // "Bob" "LA"
```

#### In Function Parameters (Extremely Common)

```js
// ❌ Without destructuring
function displayUser(user) {
  console.log(user.name + " (" + user.age + ")");
}

// ✅ With destructuring in parameters
function displayUser({ name, age, role = "member" }) {
  console.log(`${name} (${age}) — ${role}`);
}

displayUser({ name: "Alice", age: 30 }); // "Alice (30) — member"
displayUser({ name: "Bob", age: 25, role: "admin" }); // "Bob (25) — admin"
```

#### Real-World: Destructuring API Response

```js
// Typical API response
const apiResponse = {
  status: 200,
  message: "OK",
  data: {
    userId: 42,
    username: "alice_dev",
    stats: {
      posts: 87,
      followers: 1240
    }
  }
};

const {
  status,
  data: {
    username,
    stats: { posts, followers }
  }
} = apiResponse;

console.log(status);    // 200
console.log(username);  // "alice_dev"
console.log(posts);     // 87
console.log(followers); // 1240
```

---

## Spread Operator

### Definition

The **spread operator** `...` expands (spreads out) an array or object into individual elements or properties.


### Why It Exists

Before spread, copying arrays/objects or merging them required verbose methods.
Spread makes it clean, short, and readable in a single line.

### Spread with Arrays

```js
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];

// Copy an array (new reference — not the same array!)
const copy = [...arr1];
console.log(copy); // [1, 2, 3]

// Merge arrays
const merged = [...arr1, ...arr2];
console.log(merged); // [1, 2, 3, 4, 5, 6]

// Add items while merging
const extended = [0, ...arr1, 3.5, ...arr2, 7];
console.log(extended); // [0, 1, 2, 3, 3.5, 4, 5, 6, 7]

// Pass array as function arguments
function add(a, b, c) { return a + b + c; }
const nums = [1, 2, 3];
console.log(add(...nums)); // 6
```

### Spread with Objects

```js
const defaults = { theme: "light", lang: "en", fontSize: 14 };
const overrides = { theme: "dark", fontSize: 18 };

// Merge: later properties win
const config = { ...defaults, ...overrides };
console.log(config);
// { theme: "dark", lang: "en", fontSize: 18 }

// Copy an object
const original = { name: "Alice", age: 30 };
const copy = { ...original };
copy.age = 99;
console.log(original.age); // 30 — original untouched ✅
```

### Real-World: Immutable State Updates (React-style)

```js
// When updating state, never mutate — always create a new object
const state = {
  user: { name: "Alice", age: 30 },
  isLoading: false,
  count: 5
};

// Update only 'count', keep everything else
const newState = {
  ...state,         // spread all existing properties
  count: state.count + 1   // override just this one
};

console.log(newState.count);      // 6
console.log(state.count);         // 5 — original untouched ✅
```

> ⚠️ **Warning:** Spread does a **shallow copy** only. Nested objects are
> still referenced, not fully copied!

```js
const obj = { a: 1, nested: { b: 2 } };
const copy = { ...obj };

copy.nested.b = 99; // ← this changes the original too!
console.log(obj.nested.b); // 99 ← DANGER: shared reference!

// For deep copies, use: structuredClone(obj) (modern) or JSON parse/stringify
const deepCopy = structuredClone(obj);
```

---

## Rest in Arrays and Objects

### Definition

The **rest syntax** `...` collects the **remaining** items into a new array or object. It looks the same as spread but works in the opposite direction — gathering instead of spreading.


### Rest in Array Destructuring

```js
const [first, second, ...rest] = [10, 20, 30, 40, 50];

console.log(first);  // 10
console.log(second); // 20
console.log(rest);   // [30, 40, 50] — all remaining items
```

### Rest in Object Destructuring

```js
const user = { name: "Alice", age: 30, email: "a@a.com", city: "NYC" };

// Extract name, and collect everything else into 'profile'
const { name, ...profile } = user;

console.log(name);    // "Alice"
console.log(profile); // { age: 30, email: "a@a.com", city: "NYC" }
```

### Real-World: Remove a Property Immutably

```js
// Remove 'password' from user before sending to client
const userFromDB = { id: 1, name: "Alice", password: "hashed123", role: "admin" };

const { password, ...safeUser } = userFromDB; // destructure out the password
console.log(safeUser); // { id: 1, name: "Alice", role: "admin" }
// safeUser has no password — safe to send to the frontend
```

### Spread vs Rest — Side by Side

| | Spread `...` | Rest `...` |
|--|-------------|------------|
| **Used in** | Function calls, array/object literals | Function parameters, destructuring |
| **Direction** | Expands one into many | Collects many into one |
| **Example** | `Math.max(...arr)` | `const [first, ...rest] = arr` |

---

## Nested Arrays and Objects

Real-world data is almost always nested. Understanding how to navigate and
work with nested structures is essential.

```js
// A nested data structure representing a school
const school = {
  name: "Code Academy",
  location: "New York",
  courses: [
    {
      title: "JavaScript Basics",
      duration: 30,
      students: ["Alice", "Bob", "Carol"],
      instructor: { name: "Dave", experience: 5 }
    },
    {
      title: "React Fundamentals",
      duration: 45,
      students: ["Eve", "Frank"],
      instructor: { name: "Grace", experience: 8 }
    }
  ]
};

// Accessing deeply nested values
console.log(school.courses[0].title);               // "JavaScript Basics"
console.log(school.courses[0].instructor.name);     // "Dave"
console.log(school.courses[1].students[0]);         // "Eve"
console.log(school.courses[0].students.length);     // 3

// Modifying nested values
school.courses[0].duration = 35;
school.courses[1].students.push("Hannah");
```

### Practical Traversal with Modern Syntax

```js
// Get all instructor names from all courses
const instructorNames = school.courses.map(course => course.instructor.name);
console.log(instructorNames); // ["Dave", "Grace"]

// Count total students across all courses
const totalStudents = school.courses.reduce(
  (total, course) => total + course.students.length, 0
);
console.log(totalStudents); // 5
```

---

## Arrays of Objects (The Real-World Pattern)

In real applications — APIs, databases, user interfaces — data almost always
comes as an **array of objects**. Mastering this pattern is critical.

```js
const products = [
  { id: 1, name: "Laptop",   price: 999,  category: "Electronics", inStock: true  },
  { id: 2, name: "Desk",     price: 249,  category: "Furniture",   inStock: true  },
  { id: 3, name: "Monitor",  price: 349,  category: "Electronics", inStock: false },
  { id: 4, name: "Chair",    price: 179,  category: "Furniture",   inStock: true  },
  { id: 5, name: "Keyboard", price: 89,   category: "Electronics", inStock: true  }
];

// 1. Get all product names
const names = products.map(p => p.name);
console.log(names); // ["Laptop", "Desk", "Monitor", "Chair", "Keyboard"]

// 2. Filter only Electronics in stock
const availableElectronics = products.filter(
  p => p.category === "Electronics" && p.inStock
);
console.log(availableElectronics.map(p => p.name)); // ["Laptop", "Keyboard"]

// 3. Get total value of all in-stock products
const totalValue = products
  .filter(p => p.inStock)
  .reduce((sum, p) => sum + p.price, 0);
console.log(totalValue); // 999 + 249 + 179 + 89 = 1516

// 4. Find a product by ID
const product = products.find(p => p.id === 3);
console.log(product); // { id: 3, name: "Monitor", ... }

// 5. Sort by price low to high
const byPrice = [...products].sort((a, b) => a.price - b.price);
console.log(byPrice.map(p => `${p.name}: $${p.price}`));
// ["Keyboard: $89", "Chair: $179", "Desk: $249", "Monitor: $349", "Laptop: $999"]

// 6. Group by category (using reduce)
const grouped = products.reduce((groups, product) => {
  const cat = product.category;
  if (!groups[cat]) groups[cat] = []; // create array for new category
  groups[cat].push(product);
  return groups;
}, {});

console.log(Object.keys(grouped)); // ["Electronics", "Furniture"]
console.log(grouped.Furniture.length); // 2
```

---

## Cloning vs Referencing

This is one of the most misunderstood concepts in JavaScript and a huge
source of bugs.

### The Core Problem

In JavaScript, when you assign an object or array to a new variable, you do
**NOT** get a copy. You get a **reference** — both variables point to the
**same data in memory**.

```js
// 🔴 REFERENCE (both point to the same object)
const original = { name: "Alice", score: 100 };
const copy = original; // NOT a copy — it is an alias!

copy.score = 999;
console.log(original.score); // 999 — original changed! 😱
console.log(copy.score);     // 999

// This is called a REFERENCE — both variables point to the same object
```

### Shallow Clone

A shallow clone creates a new object but only copies the **top-level**
properties. Nested objects are still shared.

```js
const user = { name: "Alice", prefs: { theme: "dark" } };

// Shallow clone methods
const clone1 = { ...user };           // spread
const clone2 = Object.assign({}, user); // Object.assign

clone1.name = "Bob";            // ✅ original.name unchanged
clone1.prefs.theme = "light";   // ❌ original.prefs.theme ALSO changes!
console.log(user.prefs.theme);  // "light" — shared nested reference!
```

### Deep Clone

A deep clone copies **everything**, including all nested objects and arrays.

```js
const user = { name: "Alice", prefs: { theme: "dark" } };

// Modern deep clone (ES2022+, supported in most modern environments)
const deepClone = structuredClone(user);

deepClone.prefs.theme = "light";
console.log(user.prefs.theme); // "dark" — completely independent! ✅

// Older alternative (has limitations — cannot clone functions, undefined, etc.)
const jsonClone = JSON.parse(JSON.stringify(user));
```

### Visual Summary

```
Scenario          |  original.x  |  copy.x  | Same in memory?
---------------------------------------------------------------
Assignment =      |  Changes     | Changes  | YES (same ref)
Spread / assign   |  Unchanged   | Changes  | NO (shallow copy)
structuredClone   |  Unchanged   | Changes  | NO (deep copy)
```

---

## Common Mistakes

> ⚠️ **Mistake 1: Mutating arrays with methods that should be non-destructive**

```js
// ❌ .sort() mutates the original
const scores = [5, 3, 1, 4, 2];
const sorted = scores.sort(); // MUTATES scores!
console.log(scores); // [1, 2, 3, 4, 5] — original changed!

// ✅ Copy first, then sort
const sorted = [...scores].sort((a, b) => a - b);
console.log(scores); // [5, 3, 1, 4, 2] — original safe
```

> ⚠️ **Mistake 2: Using `==` to compare arrays/objects**

```js
// ❌ WRONG — this compares references, not content
const a = [1, 2, 3];
const b = [1, 2, 3];
console.log(a == b);  // false ← different references!
console.log(a === b); // false ← still different references!

// ✅ Compare content using JSON.stringify (for simple data)
console.log(JSON.stringify(a) === JSON.stringify(b)); // true
```

> ⚠️ **Mistake 3: Wrong default sort for numbers**

```js
// ❌ WRONG
[10, 2, 21].sort(); // [10, 2, 21] — sorts as strings!

// ✅ CORRECT
[10, 2, 21].sort((a, b) => a - b); // [2, 10, 21]
```

> ⚠️ **Mistake 4: Accessing a property that might not exist without optional chaining**

```js
// ❌ Crashes if user.address is undefined
const zip = user.address.zip; // TypeError

// ✅ Safe
const zip = user?.address?.zip; // undefined if missing
```

> ⚠️ **Mistake 5: Using `for...in` to loop over arrays**

```js
// ❌ for...in gives index as string, and may include prototype properties
for (const i in ["a", "b", "c"]) {
  console.log(i); // "0", "1", "2" — strings, not numbers!
}

// ✅ Use for...of or forEach for arrays
for (const item of ["a", "b", "c"]) {
  console.log(item); // "a", "b", "c"
}
```

> ⚠️ **Mistake 6: Thinking `const` makes objects immutable**

```js
// ❌ const does NOT prevent property changes
const user = { name: "Alice" };
user.name = "Bob"; // allowed!
console.log(user.name); // "Bob"

// ✅ Use Object.freeze() if you truly need immutability
const user = Object.freeze({ name: "Alice" });
user.name = "Bob"; // silently fails
console.log(user.name); // "Alice"
```

---

## Best Practices

- ✅ **Use `const` for all arrays and objects** — signals they won't be reassigned
- ✅ **Prefer non-mutating methods**: `map`, `filter`, `slice` over `splice`, `sort` on originals
- ✅ **Use optional chaining `?.`** when accessing deeply nested properties
- ✅ **Destructure for cleaner code** — especially in function parameters
- ✅ **Use `structuredClone()`** for reliable deep copies in modern environments
- ✅ **Use `Array.isArray()`** to check for arrays, not `typeof`
- ✅ **Prefer named keys over positional indexes** when data has semantics
- ✅ **Use `Object.freeze()`** for constants and config objects that must not change
- ✅ **Avoid mixing types in arrays** — arrays work best with a consistent type
- ✅ **Keep objects flat when possible** — deeply nested structures become hard to maintain

---

## Interview Points

### Beginner Level

**Q1. What is the difference between an array and an object in JavaScript?**

> Arrays are ordered lists accessed by numeric index. Objects are unordered
> collections of named properties (key-value pairs). Arrays are a special type
> of object — `typeof []` returns `"object"`.

**Q2. What does `.map()` return?**

> It always returns a **new array** of the same length where each element has
> been transformed by the callback. It never changes the original array.

**Q3. What is the difference between `.find()` and `.filter()`?**

> `.find()` returns the **first matching element** (or `undefined`).
> `.filter()` returns a **new array** of all matching elements.

---

### Intermediate Level

**Q4. What is the difference between a shallow copy and a deep copy?**

> A shallow copy creates a new object but nested objects are still shared
> references. A deep copy creates a completely independent copy of everything,
> including nested structures. Use `structuredClone()` for deep copies.

**Q5. How do you remove duplicates from an array?**

```js
const arr = [1, 2, 2, 3, 3, 3, 4];

// Using Set (most common — Set only stores unique values)
const unique = [...new Set(arr)];
console.log(unique); // [1, 2, 3, 4]
```

**Q6. How do you merge two objects where the second overrides the first?**

```js
const merged = { ...obj1, ...obj2 }; // obj2 properties win on conflict
// or
const merged = Object.assign({}, obj1, obj2);
```

---

### Advanced Level

**Q7. Explain how `.reduce()` works with an example.**

> `.reduce()` iterates over an array and accumulates a running result. It takes
> a callback `(accumulator, current)` and an initial value. Each return value
> becomes the next accumulator. Example: summing prices in a cart.

**Q8. How would you group an array of objects by a property?**

```js
const people = [
  { name: "Alice", dept: "Eng" },
  { name: "Bob", dept: "HR" },
  { name: "Carol", dept: "Eng" }
];

const byDept = people.reduce((groups, person) => {
  const key = person.dept;
  (groups[key] ??= []).push(person);
  return groups;
}, {});
```

**Q9. What is the difference between `null` and `undefined` as object values,
and how does optional chaining help?**

> `undefined` means the property does not exist. `null` means it exists but
> has no meaningful value. Optional chaining `?.` returns `undefined` when
> any part of the chain is `null` or `undefined`, preventing TypeErrors.

**Q10. How does `.sort()` work internally, and what is its most common mistake?**

> `.sort()` converts elements to strings by default and compares UTF-16 code
> units — which means numbers sort incorrectly. Always pass a comparison
> function `(a, b) => a - b` for numeric sorting. Also, `.sort()` mutates the
> original array in place.

---

## Debugging Tips

- 🔍 **Use `console.table(array)`** to display arrays of objects in a readable
  table format in the browser console — much easier than `console.log`
- 🔍 **Check `Array.isArray(value)`** if you are not sure whether something
  is actually an array
- 🔍 **Log before and after** any mutating method (`sort`, `splice`, `push`)
  to confirm what changed
- 🔍 **If an object property returns `undefined`**, check the exact spelling —
  property names are case-sensitive (`user.Name` ≠ `user.name`)
- 🔍 **Use optional chaining `?.`** when dealing with data from APIs where
  some fields may be missing
- 🔍 **If changes to a copy are affecting the original**, you have a reference
  issue — use spread `...` or `structuredClone()` to create a real copy
- 🔍 **Use `JSON.stringify(obj, null, 2)`** to pretty-print objects and see
  their full structure
- 🔍 **Breakpoints in DevTools** — set a breakpoint inside a `.map()` or
  `.filter()` callback to inspect each item step by step
- 🔍 **If `.sort()` produces wrong order**, add `(a, b) => a - b` — missing
  this is the #1 sort bug

---

## Exercises

### Exercise 1: Array Transformation Chain

You are given a list of raw student data. Using only `.map()`, `.filter()`,
and `.reduce()`, complete the tasks below.

```js
const students = [
  { name: "Alice", grade: 88, subject: "Math" },
  { name: "Bob", grade: 55, subject: "Science" },
  { name: "Carol", grade: 92, subject: "Math" },
  { name: "Dave", grade: 45, subject: "History" },
  { name: "Eve", grade: 76, subject: "Math" },
  { name: "Frank", grade: 61, subject: "Science" }
];

// Task 1: Get the names of all students who passed (grade >= 60)
// Task 2: Get the average grade of Math students only
// Task 3: Get an array of strings like "Alice: 88" for all students
// Task 4: Find the highest grade across ALL students
```

<details>
<summary>💡 Solution</summary>

```js
// Task 1: Names of passing students
const passing = students
  .filter(s => s.grade >= 60)
  .map(s => s.name);
console.log(passing); // ["Alice", "Carol", "Eve", "Frank"]

// Task 2: Average grade of Math students
const mathStudents = students.filter(s => s.subject === "Math");
const avgMath = mathStudents.reduce(
  (sum, s, _, arr) => sum + s.grade / arr.length, 0
);
console.log(avgMath.toFixed(1)); // "85.3"

// Task 3: Name: grade strings
const labels = students.map(s => `${s.name}: ${s.grade}`);
console.log(labels); // ["Alice: 88", "Bob: 55", ...]

// Task 4: Highest grade
const highest = students.reduce(
  (max, s) => s.grade > max ? s.grade : max, 0
);
console.log(highest); // 92
```

</details>

---

### Exercise 2: Object Destructuring + Renaming

Given the API response below, use **destructuring** to extract the values into
cleanly named variables. Use renaming and defaults where appropriate.

```js
const apiUser = {
  usr_id: 101,
  usr_name: "alice_dev",
  usr_email: "alice@example.com",
  usr_role: "admin",
  usr_meta: {
    joinedDate: "2022-03-15",
    totalPosts: 342
  }
};

// Task: Extract using destructuring:
// - usr_id → id
// - usr_name → username
// - usr_role → role (default: "viewer" if missing)
// - usr_meta.totalPosts → postCount
```

<details>
<summary>💡 Solution</summary>

```js
const {
  usr_id: id,
  usr_name: username,
  usr_role: role = "viewer",
  usr_meta: { totalPosts: postCount }
} = apiUser;

console.log(id);        // 101
console.log(username);  // "alice_dev"
console.log(role);      // "admin"
console.log(postCount); // 342
```

</details>

---

### Exercise 3: Immutable Object Updates

Without modifying the original `state` object, create a new state object with
the required changes using spread.

```js
const state = {
  user: { name: "Alice", loggedIn: false },
  theme: "light",
  notifications: ["msg1", "msg2"],
  count: 0
};

// Task 1: Create newState where count is incremented by 1
// Task 2: Create loggedInState where user.loggedIn is true (rest unchanged)
// Task 3: Create notifState where "msg3" is added to notifications
// In ALL cases: original state must remain unchanged
```

<details>
<summary>💡 Solution</summary>

```js
// Task 1: Increment count
const newState = { ...state, count: state.count + 1 };
console.log(newState.count); // 1
console.log(state.count);    // 0 ✅

// Task 2: Update nested user.loggedIn
const loggedInState = {
  ...state,
  user: { ...state.user, loggedIn: true } // spread nested too!
};
console.log(loggedInState.user.loggedIn); // true
console.log(state.user.loggedIn);         // false ✅

// Task 3: Add notification
const notifState = {
  ...state,
  notifications: [...state.notifications, "msg3"]
};
console.log(notifState.notifications); // ["msg1", "msg2", "msg3"]
console.log(state.notifications);      // ["msg1", "msg2"] ✅
```

</details>

---

### Exercise 4: Build a Mini Data Store

Build a simple in-memory "data store" for a list of users using only functions,
arrays, and objects. The store should support add, remove, find, and update.

```js
// Task: implement the store below
function createUserStore() {
  // TODO: implement using closures + array + objects

  return {
    add(user) {},        // add a new user object
    remove(id) {},       // remove user by id
    find(id) {},         // find and return user by id
    update(id, changes) {}, // merge changes into existing user
    getAll() {},         // return copy of all users
    count() {}           // return total number of users
  };
}

// Expected behavior:
const store = createUserStore();
store.add({ id: 1, name: "Alice", role: "admin" });
store.add({ id: 2, name: "Bob", role: "viewer" });
console.log(store.count()); // 2
console.log(store.find(1)); // { id: 1, name: "Alice", role: "admin" }
store.update(2, { role: "editor" });
console.log(store.find(2)); // { id: 2, name: "Bob", role: "editor" }
store.remove(1);
console.log(store.count()); // 1
console.log(store.getAll()); // [{ id: 2, name: "Bob", role: "editor" }]
```

<details>
<summary>💡 Solution</summary>

```js
function createUserStore() {
  let users = []; // private array via closure

  return {
    add(user) {
      users.push({ ...user }); // store a copy, not a reference
    },

    remove(id) {
      users = users.filter(u => u.id !== id); // create new array without the user
    },

    find(id) {
      const user = users.find(u => u.id === id);
      return user ? { ...user } : null; // return a copy or null
    },

    update(id, changes) {
      users = users.map(u =>
        u.id === id ? { ...u, ...changes } : u // spread changes onto matching user
      );
    },

    getAll() {
      return users.map(u => ({ ...u })); // return array of copies
    },

    count() {
      return users.length;
    }
  };
}
```

</details>

---

## Chapter Summary

| Concept | Key Takeaway |
|---------|-------------|
| **Array** | Ordered, zero-indexed list; use `[]` literal |
| **push/pop** | Add/remove at end; mutate original |
| **shift/unshift** | Add/remove at beginning; mutate original |
| **splice** | Add/remove anywhere; mutates original |
| **slice** | Extract portion; returns new array |
| **map** | Transform every item; returns new array |
| **filter** | Keep matching items; returns new array |
| **reduce** | Combine all items into one value |
| **find/findIndex** | First matching item / its position |
| **some/every** | Boolean check: any match / all match |
| **Object** | Named key-value pairs; use `{}` literal |
| **Dot/bracket notation** | Access properties; use `?.` for safe access |
| **Object.keys/values/entries** | Inspect object contents |
| **Destructuring** | Unpack arrays/objects into clean variables |
| **Spread `...`** | Expand array/object into copies or merges |
| **Rest `...`** | Collect remaining items into array/object |
| **Shallow vs Deep copy** | Spread = shallow; `structuredClone()` = deep |
| **Reference trap** | Assignment shares reference — always clone! |

---

> 🎉 **You have completed Chapter 5: Arrays and Objects in JavaScript.**
>
> These two data structures — arrays and objects — are the containers for
> almost everything in JavaScript. Whether you are building a UI, consuming
> an API, managing state, or transforming data, you will use these patterns
> every single day. Practice the exercises, experiment with `.reduce()` until
> it feels natural, and always remember the golden rule: **never mutate data
> you don't own — always return something new**.

---

### 📌 Key Rules to Remember

```
✅ Use const for arrays and objects
✅ Prefer map, filter, slice over mutating originals when you need a new result
✅ Use optional chaining (?.) for nested property access
✅ Destructure in function parameters and assignments for cleaner code
✅ Use structuredClone() for deep copies when nested data must be independent
✅ Use Array.isArray() — not typeof — to check for arrays
✅ Copy before sort/reverse when the original must stay unchanged
✅ Use (a, b) => a - b when sorting numbers
❌ Never compare arrays/objects with === expecting equal contents
❌ Never use for...in on arrays
❌ Never assume spread does a deep copy of nested objects
❌ Never mutate data you do not own — return new data instead
```

---

## Next Chapter

You have learned how to store and transform data with arrays and objects. Next, explore **ES6+ modern features** — modules, classes, template literals, `Map`, `Set`, and more.

---

**➡️ [Next Chapter: ES6+ Modern Features →](./ch06-es6-modern-features.md)**

---

*Last updated: 2024 | Chapter 5 of the Complete JavaScript Guide*

*Found an error or have a suggestion? [Open an issue on GitHub](https://github.com/zaid0091/CodeShelf/issues)*

*← [Previous Chapter: Functions](./ch04-functions.md)*

---

**Previous:** [Chapter 4: Functions](./ch04-functions.md) · **Next:** [Chapter 6: ES6+ Modern Features](./ch06-es6-modern-features.md)
