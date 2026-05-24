## Real-World Functional Patterns

### 1. Function Composition

Build complex operations by combining (composing) small, pure functions:

```js
// Small, single-purpose functions
const trim = str => str.trim();                    // remove whitespace
const lowercase = str => str.toLowerCase();        // make lowercase
const capitalize = str => str[0].toUpperCase() + str.slice(1); // capitalize first

// Compose them: right to left
const compose = (...fns) => value =>
  fns.reduceRight((acc, fn) => fn(acc), value);

const formatName = compose(capitalize, lowercase, trim);

console.log(formatName("  aLiCe  ")); // "Alice"
```

### 2. Currying

Transform a function that takes multiple arguments into a chain of functions,
each taking one argument:

```js
// Regular function
const add = (a, b) => a + b;

// Curried version
const curriedAdd = a => b => a + b;  // returns a new function that waits for b

const add5 = curriedAdd(5); // 'a' is fixed at 5
console.log(add5(3));  // 8
console.log(add5(10)); // 15
console.log(add5(20)); // 25

// Real use: create specialized validators
const isGreaterThan = min => value => value > min;
const isAdult = isGreaterThan(18);
const isHighScore = isGreaterThan(90);

console.log(isAdult(25));     // true
console.log(isAdult(16));     // false
console.log(isHighScore(95)); // true
```

### 3. Memoization (Caching Results)

Cache the result of expensive function calls so they are not recalculated:

```js
function memoize(fn) {
  const cache = {};              // private cache object via closure

  return function(...args) {
    const key = JSON.stringify(args); // convert args to a string key

    if (cache[key] !== undefined) {
      console.log("From cache:", key);
      return cache[key];             // return cached result immediately
    }

    const result = fn(...args);      // calculate for the first time
    cache[key] = result;             // store in cache
    return result;
  };
}

// Expensive calculation: fibonacci
function slowFib(n) {
  if (n <= 1) return n;
  return slowFib(n - 1) + slowFib(n - 2);
}

const fastFib = memoize(slowFib);

console.log(fastFib(40)); // calculated (slow first time)
console.log(fastFib(40)); // "From cache: [40]" — instant!
```

### 4. Partial Application

Pre-fill some arguments of a function to create a specialized version:

```js
function partial(fn, ...presetArgs) {
  return function(...laterArgs) {
    return fn(...presetArgs, ...laterArgs); // combine preset + later args
  };
}

function sendEmail(from, to, subject, body) {
  console.log(`From: ${from} | To: ${to} | Subject: ${subject}`);
}

// Pre-fill the 'from' address for all emails from this system
const sendFromSystem = partial(sendEmail, "system@myapp.com");

sendFromSystem("user@example.com", "Welcome!", "Welcome to MyApp!");
sendFromSystem("user@example.com", "Alert", "Your password was changed");
```

---

## Common Mistakes Developers Make

> ⚠️ **Mistake 1: Forgetting `return`**

```js
// Bug: function returns undefined silently
function double(n) { n * 2; }      // ❌ no return
function double(n) { return n * 2; } // ✅
```

> ⚠️ **Mistake 2: Calling function expression before declaration**

```js
greet(); // ❌ TypeError
const greet = () => "hello";
```

> ⚠️ **Mistake 3: Using arrow functions as object methods**

```js
const obj = { name: "X", getName: () => this.name }; // ❌ this is wrong
const obj = { name: "X", getName() { return this.name; } }; // ✅
```

> ⚠️ **Mistake 4: Mutating function parameters (objects/arrays)**

```js
function addItem(arr, item) {
  arr.push(item); // ❌ mutates the original array!
  return arr;
}

function addItem(arr, item) {
  return [...arr, item]; // ✅ returns a new array
}
```

> ⚠️ **Mistake 5: Ignoring the `var` + loop closure problem**

```js
for (var i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100); // ❌ prints 5 five times
}
// Fix: use let
for (let i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100); // ✅ prints 0,1,2,3,4
}
```

> ⚠️ **Mistake 6: Accidental `return` line break**

```js
return  // ❌ JS inserts semicolon here
{ value: 1 };
// Fix: brace on same line
return { // ✅
  value: 1
};
```

---
