---
title: JavaScript Interview Preparation
description: Common JavaScript interview questions with clear answers and code examples
order: 14
tags: [javascript, interview, questions, preparation]
---

# Chapter 14: Interview Preparation

## 14.1 How to use this chapter

Review after completing [Chapters 1–13](./ch00-course-overview.md). For each question:

1. Try answering aloud without code.
2. Write a minimal example.
3. Connect to course chapters via links.

## 14.2 Fundamentals

### Q1: Difference between `var`, `let`, and `const`?

| | `var` | `let` | `const` |
|---|-------|-------|---------|
| Scope | Function | Block | Block |
| Hoisting | Yes (undefined) | TDZ | TDZ |
| Reassign | Yes | Yes | No (binding) |

**Chapter:** [ch01](./ch01-javascript-basics.md)

### Q2: What are falsy values?

`false`, `0`, `-0`, `0n`, `""`, `null`, `undefined`, `NaN`.

**Chapter:** [ch02](./ch02-data-types.md)

### Q3: `==` vs `===`?

`===` checks value and type without coercion. Prefer `===`.

```javascript
0 == false;   // true
0 === false;  // false
```

### Q4: `typeof null`?

Returns `"object"` — historical bug. Use `value === null`.

## 14.3 Functions and scope

### Q5: What is a closure?

A function that retains access to variables from its outer scope after the outer function returns.

```javascript
function counter() {
  let n = 0;
  return () => ++n;
}
const inc = counter();
inc(); // 1
inc(); // 2
```

**Chapter:** [ch04](./ch04-functions.md)

### Q6: Arrow vs regular function?

Arrows: lexical `this`, no `arguments`, not constructable. Regular: dynamic `this`, usable with `new`.

### Q7: Explain hoisting.

Declarations are processed before execution. `var` → `undefined` until assignment. `let`/`const` in temporal dead zone until line runs. Function declarations fully hoisted.

## 14.4 Async and event loop

### Q8: Promise vs callback?

Promises provide chaining, unified error handling, and composability (`all`, `race`).

### Q9: Output order?

```javascript
console.log("1");
setTimeout(() => console.log("2"), 0);
Promise.resolve().then(() => console.log("3"));
console.log("4");
// 1, 4, 3, 2
```

Microtasks (promises) run before macrotasks (`setTimeout`).

**Chapter:** [ch07](./ch07-asynchronous-javascript.md)

### Q10: `async/await` vs `.then()`?

Same underlying Promises. `async/await` reads like sync code; use `try/catch` for errors.

## 14.5 Arrays and objects

### Q11: `map` vs `forEach`?

`map` returns new array; `forEach` returns `undefined` — use for side effects only.

### Q12: Shallow vs deep copy?

```javascript
const copy = { ...obj };           // shallow
const deep = structuredClone(obj); // deep (modern)
```

### Q13: How does `this` work in `obj.method()`?

`this` is `obj` when called as `obj.method()`. Lost if extracted: `const m = obj.method; m()`.

**Chapter:** [ch12](./ch12-oop-prototypes.md)

## 14.6 Prototypes and classes

### Q14: What is the prototype chain?

Property lookup walks `obj → obj.__proto__ → ... → null`.

### Q15: `class` vs constructor function?

`class` is mostly syntactic sugar; still prototype-based. Use `extends` and `super` for inheritance.

## 14.7 DOM and browser

### Q16: Event bubbling vs capturing?

Events travel down (capture), hit target, bubble up. `stopPropagation()` stops further propagation.

**Chapter:** [ch08](./ch08-dom-and-events.md)

### Q17: Event delegation?

One listener on parent; identify child via `event.target` and `closest()`.

### Q18: `localStorage` vs `sessionStorage`?

`localStorage` persists across sessions; `sessionStorage` per tab/window session.

**Chapter:** [ch11](./ch11-browser-apis.md)

## 14.8 Coding challenges (common)

### Challenge A: Debounce

```javascript
function debounce(fn, delay) {
  let timer;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}
```

### Challenge B: Flatten array

```javascript
function flatten(arr) {
  return arr.reduce(
    (acc, item) =>
      acc.concat(Array.isArray(item) ? flatten(item) : item),
    []
  );
}
// Or: arr.flat(Infinity)
```

### Challenge C: Implement `Promise.all`

```javascript
function promiseAll(promises) {
  return new Promise((resolve, reject) => {
    const results = [];
    let remaining = promises.length;
    if (remaining === 0) return resolve([]);

    promises.forEach((p, i) => {
      Promise.resolve(p).then(
        (value) => {
          results[i] = value;
          if (--remaining === 0) resolve(results);
        },
        reject
      );
    });
  });
}
```

### Challenge D: Curry

```javascript
function curry(fn) {
  return function curried(...args) {
    if (args.length >= fn.length) {
      return fn.apply(this, args);
    }
    return (...next) => curried(...args, ...next);
  };
}

const add = (a, b, c) => a + b + c;
const curriedAdd = curry(add);
curriedAdd(1)(2)(3); // 6
```

## 14.9 System design (front-end)

Be ready to discuss:

- Component structure and state management
- API layer (`fetch`, error handling, caching)
- Performance (lazy loading, code splitting)
- Auth (tokens, cookies, XSS/CSRF awareness)

## 14.10 Behavioral tips

| Do | Don't |
|----|-------|
| Think aloud | Stay silent too long |
| Clarify requirements | Assume edge cases |
| Start simple, then optimize | Jump to clever one-liners |
| Admit unknowns | Bluff APIs you've never used |

## 14.11 Quick revision checklist

- [ ] Variables, types, coercion, falsy
- [ ] Closures, `this`, prototypes
- [ ] `map` / `filter` / `reduce`
- [ ] Promises, `async/await`, event loop
- [ ] DOM events and delegation
- [ ] `fetch`, JSON, storage
- [ ] Error handling patterns
- [ ] ES modules and npm basics

## 14.12 Mock interview — 30 minutes

1. **5 min:** Explain event loop with `setTimeout` + `Promise`.
2. **10 min:** Implement debounce or throttle.
3. **10 min:** Build `fetch` wrapper with error handling.
4. **5 min:** Difference between class and factory for creating objects.

## Exercises

### Exercise 14.1 — Flash cards

Write 20 flash cards (question on front, 2-sentence answer on back) from this chapter.

### Exercise 14.2 — Live code

Implement `once`, `memoize`, and `deepEqual(a, b)` without libraries.

### Exercise 14.3 — Explain to a beginner

Record yourself explaining closures in under 2 minutes.

### Exercise 14.4 — Weak areas

List three topics you missed and re-read those chapters.

---

**Previous:** [Chapter 13: Best Practices](./ch13-best-practices.md) · **Course start:** [Overview](./ch00-course-overview.md)
