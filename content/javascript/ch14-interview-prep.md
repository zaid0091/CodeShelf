---
title: JavaScript Interview Preparation
description: Common JavaScript interview questions with clear answers and code examples
order: 14
tags: [javascript, interview, questions, preparation]
---

# Chapter 14: Interview Preparation

> **"Interviews test whether you can think in JavaScript — not whether you memorized syntax."**
> Use this chapter after [Chapters 1–13](./ch00-course-overview.md). Answer aloud, then code.

---

## Table of Contents

1. [How to Use This Chapter](#how-to-use-this-chapter)
2. [Study Plan](#study-plan)
3. [Fundamentals Review](#fundamentals-review)
4. [Functions and Scope](#functions-and-scope)
5. [Async and Event Loop](#async-and-event-loop)
6. [Arrays and Objects](#arrays-and-objects)
7. [Prototypes and Classes](#prototypes-and-classes)
8. [DOM and Browser](#dom-and-browser)
9. [Modules and Tooling](#modules-and-tooling)
10. [Coding Challenges](#coding-challenges)
11. [System Design Topics](#system-design-topics)
12. [Behavioral Tips](#behavioral-tips)
13. [Mock Interview](#mock-interview)
14. [Revision Checklist](#revision-checklist)
15. [Common Mistakes](#common-mistakes)
16. [Best Practices](#best-practices)
17. [Interview Points](#interview-points)
18. [Exercises](#exercises)
19. [Chapter Summary](#chapter-summary)

---

## How to Use This Chapter

### Definition

Structured Q&A and coding drills mirroring real JavaScript interviews.

### Why It Matters

Knowing syntax from earlier chapters is not enough — you must **explain** and **implement** under time pressure.

### How It Works

For each question: (1) answer without code, (2) write minimal example, (3) link to course chapter for depth.

---

## Study Plan

| Week | Focus | Chapters |
|------|-------|----------|
| 1 | Types, variables, operators | 1–3 |
| 2 | Functions, arrays, objects | 4–5 |
| 3 | ES6, async, DOM | 6–8 |
| 4 | Errors, modules, APIs, OOP | 9–12 |
| 5 | Best practices + this chapter | 13–14 |

---

## Fundamentals Review


### Q1: var vs let vs const?

Block scope for let/const; TDZ; never var. [ch01](./ch01-javascript-basics.md)


```js
const x=1; let y=2;
```


### Q2: Falsy values?

false, 0, -0, 0n, '', null, undefined, NaN. [ch02](./ch02-data-types.md)



### Q3: == vs ===?

=== no coercion; prefer ===.


```js
0===false // false
```


### Q4: typeof null?

'object' bug; use === null.



### Q5: Closure?

Function + outer lexical env. [ch04](./ch04-functions.md)


```js
function counter(){let n=0;return()=>++n;}
```


### Q6: Arrow vs function?

Lexical this; no arguments; not constructable.




---

## Functions and Scope


### Q7: Hoisting?

Declarations processed first; let/const TDZ.



### Q8: Event loop order?

Sync, microtasks, macrotasks. [ch07](./ch07-asynchronous-javascript.md)


```js
console.log(1);Promise.resolve().then(()=>2);setTimeout(()=>3,0);
```


### Q9: Promise.all vs race?

all waits all; race first settled.



### Q10: map vs forEach?

map returns array; forEach for side effects. [ch05](./ch05-arrays-and-objects.md)



### Q11: Shallow vs deep copy?

spread shallow; structuredClone deep.



### Q12: this in method?

obj.method() binds this to obj; extracted loses. [ch12](./ch12-oop-prototypes.md)




---

## Async and Event Loop


### Q13: Prototype chain?

Lookup until null.



### Q14: Delegation?

Parent listener + target. [ch08](./ch08-dom-and-events.md)



### Q15: localStorage vs session?

persistent vs tab session. [ch11](./ch11-browser-apis.md)



### Q16: Debouncing?

Wait until pause before fn. [ch08](./ch08-dom-and-events.md)


```js
function debounce(fn,ms){let t;return(...a)=>{clearTimeout(t);t=setTimeout(()=>fn(...a),ms);};}
```


### Q17: Throttle?

Run at most once per interval.



### Q18: Implement Promise.all?

Track results array and count.


```js
function promiseAll(ps){return new Promise((res,rej)=>{const r=[];let n=ps.length;if(!n)return res([]);ps.forEach((p,i)=>Promise.resolve(p).then(v=>{r[i]=v;if(!--n)res(r);},rej));});}
```



---

## Arrays and Objects


### Q19: Curry?

Partial application until arity met.



### Q20: Event bubbling?

Target to ancestors.



### Q21: async await vs then?

Same Promises; await syntactic sugar.



### Q22: ES modules vs script?

Module scope, strict, defer. [ch10](./ch10-modules-and-npm.md)




---

## Prototypes and Classes


### Q23: Optional chaining?

?. short-circuit undefined. [ch06](./ch06-es6-modern-features.md)



### Q24: Nullish coalescing?

?? only null/undefined.



### Q25: What is TDZ?

let/const inaccessible before declaration line.



### Q26: IIFE?

Run function immediately for private scope. [ch04](./ch04-functions.md)




---

## DOM and Browser


### Q27: Rest vs spread?

Same ... syntax; rest collects, spread expands. [ch06](./ch06-es6-modern-features.md)



### Q28: Generator use case?

Lazy sequences, async iterators.



### Q29: WeakMap use?

Metadata on objects without leak.



### Q30: CORS?

Browser security; server headers allow origins.




---

## Modules and Tooling



---

## Coding Challenges

### Challenge A: Debounce


```js
function debounce(fn, delay) {
  let timer;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}
```


### Challenge B: Flatten Array


```js
function flatten(arr) {
  return arr.reduce(
    (acc, item) => acc.concat(Array.isArray(item) ? flatten(item) : item),
    []
  );
}
```


### Challenge C: Deep Equal (sketch)

Compare primitives, arrays, objects recursively; watch cycles in advanced versions.

### Challenge D: once


```js
function once(fn) {
  let called = false;
  let result;
  return function (...args) {
    if (!called) {
      called = true;
      result = fn.apply(this, args);
    }
    return result;
  };
}
```


### Challenge E: memoize


```js
function memoize(fn) {
  const cache = new Map();
  return function (...args) {
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key);
    const result = fn.apply(this, args);
    cache.set(key, result);
    return result;
  };
}
```


---

## System Design Topics

Be ready to whiteboard:

- Component hierarchy and state (local vs global)
- API client layer with [fetch](./ch11-browser-apis.md) and [error handling](./ch09-error-handling.md)
- Caching (memory, HTTP cache headers, localStorage limits)
- Auth: tokens, XSS, CSRF basics
- Performance: lazy routes, code splitting, virtual lists

---

## Behavioral Tips

| Do | Don't |
|----|-------|
| Think aloud | Stay silent |
| Clarify requirements | Assume edge cases |
| Start simple | One-liner tricks first |
| Admit gaps honestly | Bluff APIs |

---

## Mock Interview — 30 Minutes

1. **5 min:** Explain event loop with setTimeout + Promise.
2. **10 min:** Implement debounce.
3. **10 min:** fetch wrapper with error handling.
4. **5 min:** class vs factory for creating objects.

---

## Revision Checklist

- [ ] Variables, types, coercion, falsy — [ch01](./ch01-javascript-basics.md), [ch02](./ch02-data-types.md)
- [ ] Closures, this, prototypes — [ch04](./ch04-functions.md), [ch12](./ch12-oop-prototypes.md)
- [ ] map / filter / reduce — [ch05](./ch05-arrays-and-objects.md)
- [ ] Promises, async/await, event loop — [ch07](./ch07-asynchronous-javascript.md)
- [ ] DOM events and delegation — [ch08](./ch08-dom-and-events.md)
- [ ] fetch, JSON, storage — [ch11](./ch11-browser-apis.md)
- [ ] Error handling — [ch09](./ch09-error-handling.md)
- [ ] ES modules and npm — [ch10](./ch10-modules-and-npm.md)


### Drill 1: Explain in 60 seconds

Pick a random topic from chapters 1–13. Record yourself explaining it without reading notes.
Topic rotation: closures, event loop, prototype chain, destructuring, Promise.all, event delegation.

```js
// Micro-practice 1: predict output before running
const a = () => console.log("a");
const b = () => Promise.resolve().then(() => console.log("b"));
const c = () => setTimeout(() => console.log("c"), 0);
a(); b(); c(); console.log("d");
// a, d, b, c
```

### Drill 2: Explain in 60 seconds

Pick a random topic from chapters 1–13. Record yourself explaining it without reading notes.
Topic rotation: closures, event loop, prototype chain, destructuring, Promise.all, event delegation.

```js
// Micro-practice 2: predict output before running
const a = () => console.log("a");
const b = () => Promise.resolve().then(() => console.log("b"));
const c = () => setTimeout(() => console.log("c"), 0);
a(); b(); c(); console.log("d");
// a, d, b, c
```

### Drill 3: Explain in 60 seconds

Pick a random topic from chapters 1–13. Record yourself explaining it without reading notes.
Topic rotation: closures, event loop, prototype chain, destructuring, Promise.all, event delegation.

```js
// Micro-practice 3: predict output before running
const a = () => console.log("a");
const b = () => Promise.resolve().then(() => console.log("b"));
const c = () => setTimeout(() => console.log("c"), 0);
a(); b(); c(); console.log("d");
// a, d, b, c
```

### Drill 4: Explain in 60 seconds

Pick a random topic from chapters 1–13. Record yourself explaining it without reading notes.
Topic rotation: closures, event loop, prototype chain, destructuring, Promise.all, event delegation.

```js
// Micro-practice 4: predict output before running
const a = () => console.log("a");
const b = () => Promise.resolve().then(() => console.log("b"));
const c = () => setTimeout(() => console.log("c"), 0);
a(); b(); c(); console.log("d");
// a, d, b, c
```

### Drill 5: Explain in 60 seconds

Pick a random topic from chapters 1–13. Record yourself explaining it without reading notes.
Topic rotation: closures, event loop, prototype chain, destructuring, Promise.all, event delegation.

```js
// Micro-practice 5: predict output before running
const a = () => console.log("a");
const b = () => Promise.resolve().then(() => console.log("b"));
const c = () => setTimeout(() => console.log("c"), 0);
a(); b(); c(); console.log("d");
// a, d, b, c
```

### Drill 6: Explain in 60 seconds

Pick a random topic from chapters 1–13. Record yourself explaining it without reading notes.
Topic rotation: closures, event loop, prototype chain, destructuring, Promise.all, event delegation.

```js
// Micro-practice 6: predict output before running
const a = () => console.log("a");
const b = () => Promise.resolve().then(() => console.log("b"));
const c = () => setTimeout(() => console.log("c"), 0);
a(); b(); c(); console.log("d");
// a, d, b, c
```

### Drill 7: Explain in 60 seconds

Pick a random topic from chapters 1–13. Record yourself explaining it without reading notes.
Topic rotation: closures, event loop, prototype chain, destructuring, Promise.all, event delegation.

```js
// Micro-practice 7: predict output before running
const a = () => console.log("a");
const b = () => Promise.resolve().then(() => console.log("b"));
const c = () => setTimeout(() => console.log("c"), 0);
a(); b(); c(); console.log("d");
// a, d, b, c
```

### Drill 8: Explain in 60 seconds

Pick a random topic from chapters 1–13. Record yourself explaining it without reading notes.
Topic rotation: closures, event loop, prototype chain, destructuring, Promise.all, event delegation.

```js
// Micro-practice 8: predict output before running
const a = () => console.log("a");
const b = () => Promise.resolve().then(() => console.log("b"));
const c = () => setTimeout(() => console.log("c"), 0);
a(); b(); c(); console.log("d");
// a, d, b, c
```

### Drill 9: Explain in 60 seconds

Pick a random topic from chapters 1–13. Record yourself explaining it without reading notes.
Topic rotation: closures, event loop, prototype chain, destructuring, Promise.all, event delegation.

```js
// Micro-practice 9: predict output before running
const a = () => console.log("a");
const b = () => Promise.resolve().then(() => console.log("b"));
const c = () => setTimeout(() => console.log("c"), 0);
a(); b(); c(); console.log("d");
// a, d, b, c
```

### Drill 10: Explain in 60 seconds

Pick a random topic from chapters 1–13. Record yourself explaining it without reading notes.
Topic rotation: closures, event loop, prototype chain, destructuring, Promise.all, event delegation.

```js
// Micro-practice 10: predict output before running
const a = () => console.log("a");
const b = () => Promise.resolve().then(() => console.log("b"));
const c = () => setTimeout(() => console.log("c"), 0);
a(); b(); c(); console.log("d");
// a, d, b, c
```

### Drill 11: Explain in 60 seconds

Pick a random topic from chapters 1–13. Record yourself explaining it without reading notes.
Topic rotation: closures, event loop, prototype chain, destructuring, Promise.all, event delegation.

```js
// Micro-practice 11: predict output before running
const a = () => console.log("a");
const b = () => Promise.resolve().then(() => console.log("b"));
const c = () => setTimeout(() => console.log("c"), 0);
a(); b(); c(); console.log("d");
// a, d, b, c
```

### Drill 12: Explain in 60 seconds

Pick a random topic from chapters 1–13. Record yourself explaining it without reading notes.
Topic rotation: closures, event loop, prototype chain, destructuring, Promise.all, event delegation.

```js
// Micro-practice 12: predict output before running
const a = () => console.log("a");
const b = () => Promise.resolve().then(() => console.log("b"));
const c = () => setTimeout(() => console.log("c"), 0);
a(); b(); c(); console.log("d");
// a, d, b, c
```

### Drill 13: Explain in 60 seconds

Pick a random topic from chapters 1–13. Record yourself explaining it without reading notes.
Topic rotation: closures, event loop, prototype chain, destructuring, Promise.all, event delegation.

```js
// Micro-practice 13: predict output before running
const a = () => console.log("a");
const b = () => Promise.resolve().then(() => console.log("b"));
const c = () => setTimeout(() => console.log("c"), 0);
a(); b(); c(); console.log("d");
// a, d, b, c
```

### Drill 14: Explain in 60 seconds

Pick a random topic from chapters 1–13. Record yourself explaining it without reading notes.
Topic rotation: closures, event loop, prototype chain, destructuring, Promise.all, event delegation.

```js
// Micro-practice 14: predict output before running
const a = () => console.log("a");
const b = () => Promise.resolve().then(() => console.log("b"));
const c = () => setTimeout(() => console.log("c"), 0);
a(); b(); c(); console.log("d");
// a, d, b, c
```

### Drill 15: Explain in 60 seconds

Pick a random topic from chapters 1–13. Record yourself explaining it without reading notes.
Topic rotation: closures, event loop, prototype chain, destructuring, Promise.all, event delegation.

```js
// Micro-practice 15: predict output before running
const a = () => console.log("a");
const b = () => Promise.resolve().then(() => console.log("b"));
const c = () => setTimeout(() => console.log("c"), 0);
a(); b(); c(); console.log("d");
// a, d, b, c
```

### Drill 16: Explain in 60 seconds

Pick a random topic from chapters 1–13. Record yourself explaining it without reading notes.
Topic rotation: closures, event loop, prototype chain, destructuring, Promise.all, event delegation.

```js
// Micro-practice 16: predict output before running
const a = () => console.log("a");
const b = () => Promise.resolve().then(() => console.log("b"));
const c = () => setTimeout(() => console.log("c"), 0);
a(); b(); c(); console.log("d");
// a, d, b, c
```

### Drill 17: Explain in 60 seconds

Pick a random topic from chapters 1–13. Record yourself explaining it without reading notes.
Topic rotation: closures, event loop, prototype chain, destructuring, Promise.all, event delegation.

```js
// Micro-practice 17: predict output before running
const a = () => console.log("a");
const b = () => Promise.resolve().then(() => console.log("b"));
const c = () => setTimeout(() => console.log("c"), 0);
a(); b(); c(); console.log("d");
// a, d, b, c
```

### Drill 18: Explain in 60 seconds

Pick a random topic from chapters 1–13. Record yourself explaining it without reading notes.
Topic rotation: closures, event loop, prototype chain, destructuring, Promise.all, event delegation.

```js
// Micro-practice 18: predict output before running
const a = () => console.log("a");
const b = () => Promise.resolve().then(() => console.log("b"));
const c = () => setTimeout(() => console.log("c"), 0);
a(); b(); c(); console.log("d");
// a, d, b, c
```

### Drill 19: Explain in 60 seconds

Pick a random topic from chapters 1–13. Record yourself explaining it without reading notes.
Topic rotation: closures, event loop, prototype chain, destructuring, Promise.all, event delegation.

```js
// Micro-practice 19: predict output before running
const a = () => console.log("a");
const b = () => Promise.resolve().then(() => console.log("b"));
const c = () => setTimeout(() => console.log("c"), 0);
a(); b(); c(); console.log("d");
// a, d, b, c
```

### Drill 20: Explain in 60 seconds

Pick a random topic from chapters 1–13. Record yourself explaining it without reading notes.
Topic rotation: closures, event loop, prototype chain, destructuring, Promise.all, event delegation.

```js
// Micro-practice 20: predict output before running
const a = () => console.log("a");
const b = () => Promise.resolve().then(() => console.log("b"));
const c = () => setTimeout(() => console.log("c"), 0);
a(); b(); c(); console.log("d");
// a, d, b, c
```

### Drill 21: Explain in 60 seconds

Pick a random topic from chapters 1–13. Record yourself explaining it without reading notes.
Topic rotation: closures, event loop, prototype chain, destructuring, Promise.all, event delegation.

```js
// Micro-practice 21: predict output before running
const a = () => console.log("a");
const b = () => Promise.resolve().then(() => console.log("b"));
const c = () => setTimeout(() => console.log("c"), 0);
a(); b(); c(); console.log("d");
// a, d, b, c
```

### Drill 22: Explain in 60 seconds

Pick a random topic from chapters 1–13. Record yourself explaining it without reading notes.
Topic rotation: closures, event loop, prototype chain, destructuring, Promise.all, event delegation.

```js
// Micro-practice 22: predict output before running
const a = () => console.log("a");
const b = () => Promise.resolve().then(() => console.log("b"));
const c = () => setTimeout(() => console.log("c"), 0);
a(); b(); c(); console.log("d");
// a, d, b, c
```

### Drill 23: Explain in 60 seconds

Pick a random topic from chapters 1–13. Record yourself explaining it without reading notes.
Topic rotation: closures, event loop, prototype chain, destructuring, Promise.all, event delegation.

```js
// Micro-practice 23: predict output before running
const a = () => console.log("a");
const b = () => Promise.resolve().then(() => console.log("b"));
const c = () => setTimeout(() => console.log("c"), 0);
a(); b(); c(); console.log("d");
// a, d, b, c
```

### Drill 24: Explain in 60 seconds

Pick a random topic from chapters 1–13. Record yourself explaining it without reading notes.
Topic rotation: closures, event loop, prototype chain, destructuring, Promise.all, event delegation.

```js
// Micro-practice 24: predict output before running
const a = () => console.log("a");
const b = () => Promise.resolve().then(() => console.log("b"));
const c = () => setTimeout(() => console.log("c"), 0);
a(); b(); c(); console.log("d");
// a, d, b, c
```

## Common Mistakes

### Skipping fundamentals

Review ch01–05 even for senior roles.

### Only reading solutions

Type code yourself.


## Best Practices

- Practice on whiteboard or paper.
- Time-box 20 minutes per coding question.
- Review wrong answers same day.

## Interview Points

### How to approach unknown question?

Clarify, brute force, optimize, test edge cases.


## Exercises

### Exercise 14.1 — Flash cards

Write 20 Q&A cards from this chapter.

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
// Your cards here
```


</details>

### Exercise 14.2 — once memoize deepEqual

Implement without libraries.

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
function once(fn){let v,d;return(...a)=>d? v:(d=1,v=fn(...a));}
```


</details>

### Exercise 14.3 — Explain closures

Record 2-minute explanation.

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
// practice speaking
```


</details>

### Exercise 14.4 — Weak areas

List 3 topics and re-read chapters.

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
// ch07, ch12, etc.
```


</details>

### Exercise 14.5 — Mock interview

Do 30-minute mock with friend.

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
// timer
```


</details>

### Exercise 14.6 — Leetcode easy JS

Solve 5 array/string problems.

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
// use map/filter
```


</details>

## Chapter Summary

You are ready to interview when you can explain the event loop, implement debounce, and trace prototype lookup without hesitation.

---

## Next Chapter

Return to the [course overview](./ch00-course-overview.md) or revisit any chapter.

---

**⬅️ [Previous: Best Practices](./ch13-best-practices.md)** · **➡️ [Next Chapter: Course Overview →](./ch00-course-overview.md)**

---

*Last updated: 2026 | Chapter 14 of the Complete JavaScript Guide*

*Found an error or have a suggestion? [Open an issue on GitHub](https://github.com/zaid0091/CodeShelf/issues)*
