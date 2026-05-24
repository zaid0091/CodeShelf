## Best Practices

- ✅ **Name functions clearly** — `getUserAge()` is better than `getData()`
- ✅ **Keep functions small** — one function, one job (Single Responsibility)
- ✅ **Prefer `const` for function expressions and arrow functions**
- ✅ **Use pure functions wherever possible** — easier to test and debug
- ✅ **Avoid modifying parameters** — return new values instead
- ✅ **Use default parameters** instead of `if/else` guards inside the body
- ✅ **Use arrow functions for callbacks** — shorter and avoids `this` bugs
- ✅ **Always `return` from functions that produce a value**
- ✅ **Keep nesting shallow** — deeply nested closures are hard to read
- ✅ **Use `let` instead of `var` in loops** to avoid closure bugs

---

## Interview Questions

### Beginner Level

**Q1. What is the difference between a function declaration and a function
expression?**

> Function declarations are hoisted completely and can be called before they
> are written. Function expressions are assigned to variables and are not
> available until the assignment line is reached.

**Q2. What does `return` do?**

> It ends function execution and sends a value back to the caller. Without it,
> the function returns `undefined`.

**Q3. What is a parameter vs an argument?**

> Parameters are the named placeholders in the function definition. Arguments
> are the actual values passed when calling the function.

---

### Intermediate Level

**Q4. What is a closure? Give an example.**

> A closure is a function that remembers variables from its outer scope even
> after the outer function has finished. Example: a counter function that keeps
> its `count` variable alive via an inner function.

**Q5. What is the difference between `var`, `let`, and `const` in the context
of scope?**

> `var` is function-scoped and ignores block boundaries. `let` and `const` are
> block-scoped and respect `{}` blocks. `var` is hoisted with `undefined`,
> while `let`/`const` are in the Temporal Dead Zone until declared.

**Q6. What is the output of this code, and why?**

```js
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}
```

> Output: `3, 3, 3`. Because `var` creates a single `i` shared by all
> iterations. By the time the callbacks run, the loop has finished and `i`
> is `3`. Fix by using `let`.

---

### Advanced Level

**Q7. What is a higher-order function? Name three built-in examples.**

> A function that takes a function as an argument or returns one. Examples:
> `.map()`, `.filter()`, `.reduce()`.

**Q8. What is currying and why is it useful?**

> Currying transforms a function with multiple arguments into a chain of
> single-argument functions. It enables partial application and creating
> specialized functions from general ones.

**Q9. What is an IIFE and when would you use it?**

> An Immediately Invoked Function Expression runs as soon as it is defined.
> It creates a private scope to avoid polluting the global namespace — useful
> for initialization code and the module pattern.

**Q10. What is the difference between `this` in a regular function and an
arrow function?**

> Regular functions have their own `this` which is determined by how they are
> called. Arrow functions inherit `this` from their surrounding scope and never
> have their own `this`.

---

## Debugging Tips

- 🔍 **Use `console.log` at the start and end** of a function to trace inputs
  and outputs
- 🔍 **Check for missing `return`** if a function gives back `undefined`
  unexpectedly
- 🔍 **Use browser DevTools Debugger** — set breakpoints inside functions to
  step through line by line
- 🔍 **Inspect the call stack** in DevTools to see which function called which
- 🔍 **Use named function expressions** instead of anonymous ones — they show
  better names in stack traces
- 🔍 **If `this` is `undefined`**, you probably need to use an arrow function
  or `.bind()`
- 🔍 **If a closure variable doesn't update**, make sure you are not copying
  a primitive value — closures capture the **reference**, not a snapshot,
  unless the variable is reassigned
- 🔍 **Use `typeof fn === 'function'`** before calling a variable as a function
  to avoid `TypeError: fn is not a function`

---

## Exercises

### Exercise 1: Arrow Function Conversion

Convert the following function declarations to arrow functions. Try all three
short forms where appropriate.

```js
// Convert each of these:

// 1.
function double(n) {
  return n * 2;
}

// 2.
function greet(name) {
  return "Hello, " + name + "!";
}

// 3.
function add(a, b) {
  return a + b;
}

// 4.
function getUser(id) {
  return { id: id, active: true };
}
```

<details>
<summary>💡 Solution</summary>

```js
// 1. Single parameter — no parentheses, implicit return
const double = n => n * 2;

// 2. Single parameter — no parentheses, implicit return
const greet = name => "Hello, " + name + "!";

// 3. Multiple parameters — parentheses, implicit return
const add = (a, b) => a + b;

// 4. Returns object — wrap in parentheses for implicit return
const getUser = id => ({ id: id, active: true });
```

</details>

---

### Exercise 2: Closure-Based Counter

Build a counter using closures that supports `increment`, `decrement`, `reset`,
and `getCount`. The count should start at a value passed in.

```js
// Your task:
function createCounter(startValue) {
  // TODO: implement using closure
}

// Expected behavior:
const counter = createCounter(10);
counter.increment(); // 11
counter.increment(); // 12
counter.decrement(); // 11
counter.reset();
counter.getCount();  // 10
```

<details>
<summary>💡 Solution</summary>

```js
function createCounter(startValue = 0) {
  let count = startValue; // private variable captured by closure

  return {
    increment() {
      count++;
      return count;
    },
    decrement() {
      count--;
      return count;
    },
    reset() {
      count = startValue; // reset to the original start value
      return count;
    },
    getCount() {
      return count;
    }
  };
}

const counter = createCounter(10);
console.log(counter.increment()); // 11
console.log(counter.increment()); // 12
console.log(counter.decrement()); // 11
counter.reset();
console.log(counter.getCount()); // 10
```

</details>

---

### Exercise 3: The `once` Function

Implement a `once` higher-order function that wraps any function and ensures
it can only be called **one time**. After the first call, it returns the same
result without running the function again.

```js
// Your task:
function once(fn) {
  // TODO: implement using closure
}

// Expected behavior:
const initApp = once(() => {
  console.log("App initialized!");
  return true;
});

initApp(); // "App initialized!" → true
initApp(); // nothing logs → still returns true (same result, no re-run)
initApp(); // nothing logs → still returns true
```

<details>
<summary>💡 Solution</summary>

```js
function once(fn) {
  let called = false;    // has the function been called yet?
  let result;            // store the result from the first call

  return function(...args) {
    if (!called) {
      called = true;           // mark as called
      result = fn(...args);    // run the original function once
    }
    return result;             // always return the first call's result
  };
}

const initApp = once(() => {
  console.log("App initialized!");
  return true;
});

console.log(initApp()); // "App initialized!" → true
console.log(initApp()); //                    → true (no log, not re-run)
console.log(initApp()); //                    → true
```

</details>

---

### Exercise 4: Function Composition Pipeline

Implement a `pipe` function that takes multiple functions and returns a single
function. When called, it passes its argument through each function from left
to right (the output of each becomes the input of the next).

```js
// Your task:
function pipe(...fns) {
  // TODO: implement using reduce
}

// Test functions
const trim = str => str.trim();
const lowercase = str => str.toLowerCase();
const removeSpaces = str => str.replace(/\s+/g, "-");
const addPrefix = str => "user-" + str;

// Expected behavior:
const formatUsername = pipe(trim, lowercase, removeSpaces, addPrefix);
console.log(formatUsername("  John Doe  ")); // "user-john-doe"
```

<details>
<summary>💡 Solution</summary>

```js
function pipe(...fns) {
  return function(value) {
    return fns.reduce((acc, fn) => fn(acc), value);
    // Start with 'value', pass it through each function left to right
  };
}

const trim = str => str.trim();
const lowercase = str => str.toLowerCase();
const removeSpaces = str => str.replace(/\s+/g, "-");
const addPrefix = str => "user-" + str;

const formatUsername = pipe(trim, lowercase, removeSpaces, addPrefix);

console.log(formatUsername("  John Doe  "));   // "user-john-doe"
console.log(formatUsername("  JANE SMITH  ")); // "user-jane-smith"
```

</details>

---

## Chapter Summary

| Concept | One-Line Summary |
|---------|-----------------|
| **Function Declaration** | Named, hoisted, classic way to define functions |
| **Function Expression** | Function stored in a variable; not hoisted |
| **Arrow Function** | Short syntax; inherits `this` from parent scope |
| **Default Parameters** | Fallback values when arguments are not provided |
| **Rest Parameters** | Collects extra arguments into an array |
| **Destructuring Parameters** | Unpack objects/arrays directly in function signature |
| **Return** | Ends function and sends a value back |
| **Scope** | Rules determining where variables are accessible |
| **Hoisting** | Declarations moved to top of scope before execution |
| **Closure** | Inner function remembers outer function's variables |
| **Higher-Order Functions** | Functions that take or return other functions |
| **IIFE** | Function that runs immediately on definition |
| **Pure Function** | Same input → same output, no side effects |
| **Currying** | Transform multi-arg function into chain of single-arg functions |
| **Memoization** | Cache expensive results using closures |

---

> 🎉 **You have completed Chapter 4: Functions in JavaScript.**
>
> Functions are truly the heart of JavaScript. Every concept you have learned
> here — scope, closures, higher-order functions — builds directly on the
> previous one. Take time to practice the exercises, re-read the closure
> section multiple times, and experiment in the browser console. Understanding
> functions deeply will make every other topic in JavaScript easier.
>

---

**Previous:** [Chapter 3: Operators & Control Flow](./ch03-operators-and-control-flow.md) · **Next:** [Chapter 5: Arrays & Objects](./ch05-arrays-and-objects.md)

**➡️ [Next Chapter: Arrays & Objects →](./ch05-arrays-and-objects.md)
