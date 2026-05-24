## Parameters and Arguments

### Definition

- **Parameters** are the named variables listed in the function definition
  (placeholders)
- **Arguments** are the actual values you pass when calling the function

```js
function greet(name) {  // 'name' is the PARAMETER (a placeholder)
  return "Hi, " + name;
}

greet("Alice"); // "Alice" is the ARGUMENT (the actual value)
```

### Default Parameters

#### Definition

Default parameters let you define a **fallback value** for a parameter if the
caller does not provide one (or passes `undefined`).

#### Why It Exists

Without defaults, unset parameters are `undefined`, which causes bugs. Instead
of writing `if` checks inside every function, you can set smart defaults right
in the parameter list.

#### Syntax & Example

```js
// ❌ OLD WAY: manual default check
function greet(name) {
  name = name || "Guest"; // if name is falsy, use "Guest"
  return "Hello, " + name;
}

// ✅ MODERN WAY: default parameter
function greet(name = "Guest") {    // if name is not passed, use "Guest"
  return "Hello, " + name;
}

console.log(greet("Alice")); // "Hello, Alice"
console.log(greet());        // "Hello, Guest"
```

#### Real-World Example

```js
// Create a styled button with sensible defaults
function createButton(label = "Click Me", color = "blue", size = "medium") {
  return `<button style="color:${color}; font-size:${size}">${label}</button>`;
}

console.log(createButton());                      // default button
console.log(createButton("Submit", "green"));     // custom label and color
console.log(createButton("Delete", "red", "large")); // fully custom
```

---

### Rest Parameters

#### Definition

The **rest parameter** (`...`) collects all remaining arguments into a real
JavaScript **array**. It must always be the **last parameter**.

#### Why It Exists

Sometimes you don't know in advance how many arguments a function will receive.
Rest parameters let you handle any number of arguments cleanly.

#### Syntax & Example

```js
function sum(...numbers) {          // 'numbers' collects ALL arguments into an array
  let total = 0;
  for (const n of numbers) {
    total += n;                     // add each number to the total
  }
  return total;
}

console.log(sum(1, 2));          // 3
console.log(sum(1, 2, 3, 4, 5)); // 15
console.log(sum(10, 20, 30));    // 60
```

#### Real-World Example

```js
// Log messages with a severity prefix
function log(severity, ...messages) {       // first arg is severity, rest are messages
  const prefix = `[${severity.toUpperCase()}]`;
  messages.forEach(msg => console.log(prefix, msg)); // log each message
}

log("info", "Server started", "Port: 3000");
// [INFO] Server started
// [INFO] Port: 3000

log("error", "Database connection failed");
// [ERROR] Database connection failed
```

---

### Destructuring Parameters

#### Definition

**Destructuring parameters** let you unpack object properties or array elements
directly in the function signature instead of accessing them inside the body.

#### Why It Exists

When functions receive large objects (like user data or API responses), it is
cleaner and more readable to name only what you need right at the top.

#### Syntax & Example

```js
// ❌ WITHOUT destructuring
function displayUser(user) {
  console.log(user.name + " is " + user.age); // have to write user.name, user.age
}

// ✅ WITH destructuring
function displayUser({ name, age }) {           // unpack directly from object
  console.log(name + " is " + age);            // use directly
}

displayUser({ name: "Alice", age: 30, city: "NY" }); // "Alice is 30"
```

#### Real-World Example

```js
// API response object
const apiResponse = {
  status: 200,
  data: {
    id: 42,
    username: "alice_dev",
    email: "alice@example.com"
  }
};

// Destructure nested object and use defaults
function handleResponse({ status, data: { username, email } = {} }) {
  if (status === 200) {
    console.log(`Welcome back, ${username}! (${email})`);
  }
}

handleResponse(apiResponse); // "Welcome back, alice_dev! (alice@example.com)"
```

---

## Return Values

### Definition

The `return` statement ends the function and **sends a value back** to where
the function was called. Without `return`, a function gives back `undefined`.

### Why It Exists

Functions would be useless if they could not communicate results. `return` is
how a function shares the outcome of its work with the rest of the program.

### Key Rules

- A function **stops immediately** when it hits `return`
- A function can only return **one value** (but that value can be an array or object)
- If there is no `return`, the function returns `undefined` automatically

```js
// Returning a single value
function square(n) {
  return n * n;  // sends n*n back to the caller
  console.log("This never runs"); // code after return is unreachable
}

// Returning multiple values via an object
function getMinMax(numbers) {
  const min = Math.min(...numbers); // find smallest
  const max = Math.max(...numbers); // find largest
  return { min, max };              // return both in one object
}

const { min, max } = getMinMax([3, 1, 7, 2, 9]);
console.log(min, max); // 1 9
```

### Common Mistakes

```js
// ❌ WRONG: Accidental line break after return
function getValue() {
  return       // JavaScript inserts a semicolon here automatically!
    { value: 42 };  // This never executes
}
console.log(getValue()); // undefined ← Bug!

// ✅ CORRECT: Opening brace on same line as return
function getValue() {
  return {     // Opening brace on same line
    value: 42
  };
}
console.log(getValue()); // { value: 42 }
```

---
