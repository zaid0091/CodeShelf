---
title: OOP and Prototypes
description: Prototype chain, this binding, constructor functions, and ES6 classes
order: 12
tags: [javascript, oop, prototypes, this, classes, inheritance]
---

# Chapter 12: OOP and Prototypes

> "JavaScript is not class-based — it is prototype-based with optional class syntax on top."

---

## Table of Contents

1. [Objects and Prototypes](#objects-and-prototypes)
2. [The Prototype Chain](#the-prototype-chain)
3. [__proto__ vs prototype](#__proto__-vs-prototype)
4. [Constructor Functions](#constructor-functions)
5. [Classes vs Constructors](#classes-vs-constructors)
6. [Understanding this](#understanding-this)
7. [call apply bind](#call-apply-bind)
8. [Inheritance with extends](#inheritance-with-extends)
9. [Object.create](#objectcreate)
10. [hasOwnProperty and in](#hasownproperty-and-in)
11. [Factory Functions](#factory-functions)
12. [Mixins](#mixins)
13. [Common Mistakes](#common-mistakes)
14. [Best Practices](#best-practices)
15. [Interview Points](#interview-points)
16. [Exercises](#exercises)
17. [Chapter Summary](#chapter-summary)

---

## Objects and Prototypes

### Definition

JavaScript uses **prototypal inheritance** — objects delegate to other objects via `[[Prototype]]`.

### Why It Matters

Unlike classical OOP-only languages.

### How It Works


```js
const animal = { speak() { return "sound"; } };
const dog = Object.create(animal);
dog.speak();
```




---

## The Prototype Chain

### Definition

Lookup walks `obj → proto → ... → null`.

### Why It Matters

Property resolution algorithm core to JS.

### How It Works

```text
dog → animal → Object.prototype → null
```



---

## __proto__ vs prototype

### Definition

`obj.__proto__` is instance link; `Fn.prototype` is object used for `new Fn()` instances.

### Why It Matters

Interview classic.

### How It Works

Prefer `Object.getPrototypeOf(obj)`.



---

## Constructor Functions

### Definition

`function Person(name) { this.name = name; }` with `new` creates instance linked to `Person.prototype`.

### Why It Matters

Pre-ES6 pattern still in legacy code.

### How It Works


```js
function Person(name) { this.name = name; }
Person.prototype.greet = function() { return "Hi " + this.name; };
const a = new Person("Alice");
```




---

## Classes vs Constructors

### Definition

`class` is syntactic sugar — methods still on prototype.

### Why It Matters

Modern syntax — [Chapter 6](./ch06-es6-modern-features.md).

### How It Works


```js
class Car {
  constructor(brand) { this.brand = brand; }
  drive() { return this.brand + " moves"; }
}
```




---

## Understanding this

### Definition

`this` depends on **call site**: method call, plain call, `new`, `call`/`apply`/`bind`.

### Why It Matters

Most confusing JS topic.

### How It Works


```js
const obj = { name: "A", getName() { return this.name; } };
const fn = obj.getName;
fn(); // undefined in strict — lost binding
```




---

## call apply bind

### Definition

Explicitly set `this` for a function.

### Why It Matters

Borrow methods, fix callbacks.

### How It Works


```js
function greet() { return "Hi " + this.name; }
greet.call({ name: "Bob" });
const bound = greet.bind({ name: "Carol" });
```




---

## Inheritance with extends

### Definition

`extends` sets up prototype chain; `super` calls parent.

### Why It Matters

Reuse behavior in class hierarchies.

### How It Works


```js
class Dog extends Animal {
  constructor(name) { super(name); }
}
```




---

## Object.create

### Definition

Creates object with specified prototype.

### Why It Matters

Pure prototypal pattern.

### How It Works


```js
const proto = { type: "animal" };
const o = Object.create(proto);
```




---

## hasOwnProperty and in

### Definition

`in` checks chain; `hasOwnProperty` / `Object.hasOwn` checks own keys only.

### Why It Matters

Iterate own keys safely.

### How It Works


```js
Object.hasOwn(obj, "key");
```




---

## Factory Functions

### Definition

Return new object without `new` — alternative to classes.

### Why It Matters

Functional style, no `this` confusion.

### How It Works


```js
function createUser(name) {
  return { name, greet() { return "Hi " + name; } };
}
```




---

## Mixins

### Definition

Copy methods onto prototype or object.

### Why It Matters

Share behavior without single inheritance tree.

### How It Works


```js
const canEat = { eat() { return "eating"; } };
Object.assign(Dog.prototype, canEat);
```




---

### Understanding this — Example 1

```js
// Example 1: practical pattern for understanding this
// (Study how inputs become outputs step by step)

function example1Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example1Demo("  hello  ")); // "hello"
```


### Understanding this — Example 2

```js
// Example 2: practical pattern for understanding this
// (Study how inputs become outputs step by step)

function example2Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example2Demo("  hello  ")); // "hello"
```


### Understanding this — Example 3

```js
// Example 3: practical pattern for understanding this
// (Study how inputs become outputs step by step)

function example3Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example3Demo("  hello  ")); // "hello"
```


### Understanding this — Example 4

```js
// Example 4: practical pattern for understanding this
// (Study how inputs become outputs step by step)

function example4Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example4Demo("  hello  ")); // "hello"
```


### Understanding this — Example 5

```js
// Example 5: practical pattern for understanding this
// (Study how inputs become outputs step by step)

function example5Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example5Demo("  hello  ")); // "hello"
```

### The Prototype Chain — Example 1

```js
// Example 1: practical pattern for the prototype chain
// (Study how inputs become outputs step by step)

function example1Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example1Demo("  hello  ")); // "hello"
```


### The Prototype Chain — Example 2

```js
// Example 2: practical pattern for the prototype chain
// (Study how inputs become outputs step by step)

function example2Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example2Demo("  hello  ")); // "hello"
```


### The Prototype Chain — Example 3

```js
// Example 3: practical pattern for the prototype chain
// (Study how inputs become outputs step by step)

function example3Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example3Demo("  hello  ")); // "hello"
```


### The Prototype Chain — Example 4

```js
// Example 4: practical pattern for the prototype chain
// (Study how inputs become outputs step by step)

function example4Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example4Demo("  hello  ")); // "hello"
```


### The Prototype Chain — Example 5

```js
// Example 5: practical pattern for the prototype chain
// (Study how inputs become outputs step by step)

function example5Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example5Demo("  hello  ")); // "hello"
```

### Classes vs Constructors — Example 1

```js
// Example 1: practical pattern for classes vs constructors
// (Study how inputs become outputs step by step)

function example1Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example1Demo("  hello  ")); // "hello"
```


### Classes vs Constructors — Example 2

```js
// Example 2: practical pattern for classes vs constructors
// (Study how inputs become outputs step by step)

function example2Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example2Demo("  hello  ")); // "hello"
```


### Classes vs Constructors — Example 3

```js
// Example 3: practical pattern for classes vs constructors
// (Study how inputs become outputs step by step)

function example3Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example3Demo("  hello  ")); // "hello"
```


### Classes vs Constructors — Example 4

```js
// Example 4: practical pattern for classes vs constructors
// (Study how inputs become outputs step by step)

function example4Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example4Demo("  hello  ")); // "hello"
```


### Classes vs Constructors — Example 5

```js
// Example 5: practical pattern for classes vs constructors
// (Study how inputs become outputs step by step)

function example5Demo(input) {
  // Step 1: validate
  if (input == null) return null;
  // Step 2: transform
  const result = typeof input === "string" ? input.trim() : input;
  // Step 3: return
  return result;
}

console.log(example5Demo("  hello  ")); // "hello"
```

## Common Mistakes

### Losing this in callbacks

Use arrow or bind.

### Modifying built-in prototypes

Don't.


## Best Practices

- Prefer classes or factories consistently.
- Use Object.hasOwn in loops.
- Learn prototype chain for interviews.

## Interview Points

### Prototype chain?

Delegation lookup until null.

### class vs constructor?

Mostly sugar; still prototypes.


## Exercises

### Exercise 12.1 — createUser factory

Return user object with methods

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
function createUser(n){return{name:n,greet(){return n}}}
```


</details>

### Exercise 12.2 — bind fix

Fix lost this

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
button.addEventListener('click', obj.method.bind(obj));
```


</details>

### Exercise 12.3 — extends

Animal/Dog classes

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
class Dog extends Animal { speak(){ return 'bark'; } }
```


</details>

### Exercise 12.4 — Object.create

Proto chain

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
const o = Object.create({a:1});
```


</details>

### Exercise 12.5 — call/apply

Borrow array slice

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
Array.prototype.slice.call(arrayLike);
```


</details>

### Exercise 12.6 — instanceof

Check prototype chain

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
dog instanceof Dog
```


</details>

## Chapter Summary

| Topic | Remember |
|-------|----------|
| this | call site |
| class | sugar |
| chain | delegation |


---

## Next Chapter

Next: **best practices** for production code.

---

**⬅️ [Previous: Browser APIs](./ch11-browser-apis.md)** · **➡️ [Next Chapter: Best Practices →](./ch13-best-practices.md)**

---

*Last updated: 2026 | Chapter 12 of the Complete JavaScript Guide*

*Found an error or have a suggestion? [Open an issue on GitHub](https://github.com/zaid0091/CodeShelf/issues)*

---

## Worked Example 1: OOP and Prototypes

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 1 for Chapter 12
function demo1(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo1({ a: 1, b: 2 }));
console.log(demo1([1, 2, 3]));
console.log(demo1("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 2: OOP and Prototypes

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 2 for Chapter 12
function demo2(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo2({ a: 1, b: 2 }));
console.log(demo2([1, 2, 3]));
console.log(demo2("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 3: OOP and Prototypes

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 3 for Chapter 12
function demo3(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo3({ a: 1, b: 2 }));
console.log(demo3([1, 2, 3]));
console.log(demo3("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 4: OOP and Prototypes

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 4 for Chapter 12
function demo4(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo4({ a: 1, b: 2 }));
console.log(demo4([1, 2, 3]));
console.log(demo4("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 5: OOP and Prototypes

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 5 for Chapter 12
function demo5(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo5({ a: 1, b: 2 }));
console.log(demo5([1, 2, 3]));
console.log(demo5("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 6: OOP and Prototypes

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 6 for Chapter 12
function demo6(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo6({ a: 1, b: 2 }));
console.log(demo6([1, 2, 3]));
console.log(demo6("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 7: OOP and Prototypes

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 7 for Chapter 12
function demo7(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo7({ a: 1, b: 2 }));
console.log(demo7([1, 2, 3]));
console.log(demo7("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 8: OOP and Prototypes

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 8 for Chapter 12
function demo8(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo8({ a: 1, b: 2 }));
console.log(demo8([1, 2, 3]));
console.log(demo8("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 9: OOP and Prototypes

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 9 for Chapter 12
function demo9(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo9({ a: 1, b: 2 }));
console.log(demo9([1, 2, 3]));
console.log(demo9("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 10: OOP and Prototypes

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 10 for Chapter 12
function demo10(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo10({ a: 1, b: 2 }));
console.log(demo10([1, 2, 3]));
console.log(demo10("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 11: OOP and Prototypes

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 11 for Chapter 12
function demo11(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo11({ a: 1, b: 2 }));
console.log(demo11([1, 2, 3]));
console.log(demo11("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 12: OOP and Prototypes

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 12 for Chapter 12
function demo12(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo12({ a: 1, b: 2 }));
console.log(demo12([1, 2, 3]));
console.log(demo12("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 13: OOP and Prototypes

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 13 for Chapter 12
function demo13(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo13({ a: 1, b: 2 }));
console.log(demo13([1, 2, 3]));
console.log(demo13("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.


---

## Worked Example 14: OOP and Prototypes

### Definition

Hands-on reinforcement of concepts from this chapter.

### Why Practice Matters

Reading alone is not enough — typing examples builds muscle memory for interviews and real projects.

### How to Study This Example

1. Predict the output before running.
2. Change one line and observe what breaks.
3. Link the pattern to earlier chapters in the course.

### Example Code

```js
// Worked example 14 for Chapter 12
function demo14(input) {
  const steps = [];
  steps.push("start:" + input);
  if (input == null) return steps;
  if (typeof input === "object") {
    steps.push("keys:" + Object.keys(input).join(","));
  }
  if (Array.isArray(input)) {
    steps.push("length:" + input.length);
  }
  steps.push("done");
  return steps;
}

console.log(demo14({ a: 1, b: 2 }));
console.log(demo14([1, 2, 3]));
console.log(demo14("test"));
```

### Step-by-Step Table

| Step | Action |
|------|--------|
| 1 | Validate input type |
| 2 | Branch for object vs array vs primitive |
| 3 | Collect debug steps in array |
| 4 | Return trace for learning |

> 💡 **Tip:** Re-run in DevTools and set breakpoints on the `if` branches.

