---
title: DOM and Events
description: Selecting elements, manipulating the DOM, events, and event delegation
order: 8
tags: [javascript, dom, events, delegation, browser]
---

# Chapter 8: DOM and Events

> "The DOM is your canvas — events are the brush strokes that make pages feel alive."

---

## Table of Contents

1. [What is the DOM?](#what-is-the-dom?)
2. [Nodes vs Elements](#nodes-vs-elements)
3. [Selecting Elements](#selecting-elements)
4. [Scoped DOM Queries](#scoped-dom-queries)
5. [Reading and Changing Content](#reading-and-changing-content)
6. [Creating and Removing Nodes](#creating-and-removing-nodes)
7. [DOM Traversal](#dom-traversal)
8. [Attributes and Data Attributes](#attributes-and-data-attributes)
9. [ClassList and CSS](#classlist-and-css)
10. [Events — Responding to Users](#events--responding-to-users)
11. [Common Event Types](#common-event-types)
12. [The Event Object](#the-event-object)
13. [Event Propagation](#event-propagation)
14. [Event Delegation](#event-delegation)
15. [Forms and FormData](#forms-and-formdata)
16. [Debouncing and Throttling](#debouncing-and-throttling)
17. [Custom Events](#custom-events)
18. [DOM Performance](#dom-performance)
19. [Accessibility Basics](#accessibility-basics)
20. [Shadow DOM Overview](#shadow-dom-overview)
21. [Common Mistakes](#common-mistakes)
22. [Best Practices](#best-practices)
23. [Interview Points](#interview-points)
24. [Exercises](#exercises)
25. [Chapter Summary](#chapter-summary)

---

## What is the DOM?

### Definition

The **Document Object Model (DOM)** is a tree-shaped API representing an HTML/XML document. Each tag is a **node**; JavaScript can read and mutate structure, attributes, and content.

### Why It Matters

Every interactive website uses the DOM — buttons, forms, dynamic lists.

### How It Works

The browser parses HTML into a tree; `document` is the entry point.


```js
// document → html → head, body → descendants
const title = document.querySelector("h1");
console.log(title.textContent);
```

```text
document
 └── html
      ├── head
      └── body
           └── main
                └── ul#list
                     └── li.item
```
---

## Nodes vs Elements

### Definition

**Nodes** include elements, text, comments. **Elements** are node type 1 with tag names and attributes.

### Why It Matters

Selecting and traversing requires knowing node types.

### How It Works

`nodeType`, `nodeName`, `childNodes` vs `children` (elements only).


```js
const el = document.createElement("div");
el.nodeType; // 1 (ELEMENT_NODE)
const text = document.createTextNode("hi");
text.nodeType; // 3 (TEXT_NODE)
```


---

## Selecting Elements

### Definition

Query the DOM with `getElementById`, `querySelector`, `querySelectorAll`, and legacy collections.

### Why It Matters

Modern code prefers CSS selectors for flexibility.

### How It Works

`querySelector` returns first match or `null`; always null-check.


```js
const title = document.getElementById("title");
const btn = document.querySelector(".btn-primary");
const items = document.querySelectorAll(".todo-item");
items.forEach((el) => console.log(el.textContent));
```

| Method | Returns |
|--------|----------|
| `getElementById` | Element or null |
| `querySelector` | First match |
| `querySelectorAll` | NodeList |
---

## Scoped DOM Queries

### Definition

Search within a subtree by calling `querySelector` on an element, not only `document`.

### Why It Matters

Faster and safer in components — avoids matching wrong section of page.

### How It Works

Store parent reference once.


```js
const list = document.querySelector("#todo-list");
const items = list.querySelectorAll("li");
```


---

## Reading and Changing Content

### Definition

`textContent` sets plain text (safe). `innerHTML` parses HTML (XSS risk with user data).

### Why It Matters

Display user names safely; render trusted templates carefully.

### How It Works

Attributes via `setAttribute`, `dataset`, `classList`, `style`.


```js
const el = document.querySelector("#message");
el.textContent = "Hello"; // escapes HTML
el.classList.add("active");
el.dataset.id = "42"; // data-id attribute
```


---

## Creating and Removing Nodes

### Definition

Build elements with `createElement`, attach with `append`, `prepend`, `insertAdjacentHTML`.

### Why It Matters

Dynamic todo lists, modals, notifications.

### How It Works

`remove()` detaches node; `replaceChildren` clears container.


```js
const li = document.createElement("li");
li.textContent = "New task";
document.querySelector("#list").append(li);
li.remove();
```


---

## DOM Traversal

### Definition

Walk the tree with `parentElement`, `children`, `nextElementSibling`, `closest`.

### Why It Matters

Event delegation uses `closest` to find matching ancestor.

### How It Works

Prefer element properties over full `childNodes` when you want elements only.


```js
const btn = event.target.closest("button.delete");
if (!btn) return;
const item = btn.closest("li");
```


---

## Attributes and Data Attributes

### Definition

HTML attributes map to DOM properties; `data-*` attributes expose `element.dataset`.

### Why It Matters

Store IDs and config on elements for JS behavior.

### How It Works

Dataset keys are camelCase: `data-user-id` → `dataset.userId`.


```js
const card = document.querySelector(".card");
card.dataset.userId = "99";
console.log(card.dataset.userId);
```


---

## ClassList and CSS

### Definition

`classList` adds/removes/toggles classes; prefer classes over inline styles for themes.

### Why It Matters

Works with stylesheets — separation of concerns.

### How It Works

Use `toggle('active', condition)` to set class based on boolean.


```js
el.classList.add("open");
el.classList.toggle("selected", isSelected);
el.classList.contains("hidden");
```


---

## Events — Responding to Users

### Definition

**Events** are signals that something happened (click, input, submit). Register with `addEventListener`.

### Why It Matters

Decouple HTML from JS — no inline `onclick` in professional code.

### How It Works

Same function reference needed to remove listener.


```js
const button = document.querySelector("#save");
button.addEventListener("click", (e) => {
  console.log("clicked", e.target);
});
```


---

## Common Event Types

### Definition

Clicks, keyboard, forms, loading, and custom events cover most UIs.

### Why It Matters

Match event to user intent — `input` vs `change`.

### How It Works

`DOMContentLoaded` fires when HTML is parsed.


```js
document.addEventListener("DOMContentLoaded", initApp);
form.addEventListener("submit", onSubmit);
input.addEventListener("input", onType);
```

| Event | When |
|-------|------|
| click | pointer activation |
| submit | form submit |
| input | value changing |
| keydown | key pressed |
---

## The Event Object

### Definition

The **event object** carries `target`, `currentTarget`, keys, and methods `preventDefault`, `stopPropagation`.

### Why It Matters

Keyboard shortcuts, form validation, custom modifiers.

### How It Works

`target` is what was clicked; `currentTarget` is element with listener.


```js
input.addEventListener("keydown", (e) => {
  if (e.key === "Enter") submit();
  if (e.ctrlKey && e.key === "s") {
    e.preventDefault();
    save();
  }
});
```


---

## Event Propagation

### Definition

Events flow **capture** (window → target) then **bubble** (target → window).

### Why It Matters

Parent can listen for child events during bubble phase.

### How It Works

Third argument `true` listens in capture phase.


```js
parent.addEventListener("click", () => console.log("parent"));
child.addEventListener("click", (e) => {
  e.stopPropagation();
  console.log("child");
});
```


---

## Event Delegation

### Definition

Attach one listener on a parent; handle children via `event.target` and `closest`.

### Why It Matters

Dynamic lists — new items work without new listeners.

### How It Works

Fewer listeners, better memory on large lists.


```js
list.addEventListener("click", (e) => {
  const item = e.target.closest("li.todo-item");
  if (!item) return;
  if (e.target.matches("button.delete")) item.remove();
});
```


---

## Forms and FormData

### Definition

Forms fire `submit`; use `preventDefault` and `FormData` to read fields.

### Why It Matters

Login, signup, search — standard web pattern.

### How It Works

Validate before sending to server — [Chapter 9](./ch09-error-handling.md).


```js
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const data = new FormData(form);
  console.log(data.get("email"));
});
```


---

## Debouncing and Throttling

### Definition

**Debounce** waits until activity stops; **throttle** limits execution rate.

### Why It Matters

Search-as-you-type, resize handlers.

### How It Works

Implement with `setTimeout` — see [Chapter 7](./ch07-asynchronous-javascript.md).


```js
function debounce(fn, ms) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), ms);
  };
}
searchInput.addEventListener("input", debounce(onSearch, 300));
```


---

## Custom Events

### Definition

`CustomEvent` lets components communicate without tight coupling.

### Why It Matters

Widget notifies parent when done.

### How It Works

`dispatchEvent` on element.


```js
const done = new CustomEvent("save-complete", { detail: { id: 1 } });
form.dispatchEvent(done);
```


---

## DOM Performance

### Definition

Minimize reflows — batch DOM updates, use `DocumentFragment`, avoid layout thrashing.

### Why It Matters

Smooth UIs on large lists.

### How It Works

Read then write; don't interleave layout reads/writes in loops.


```js
const frag = document.createDocumentFragment();
items.forEach((t) => {
  const li = document.createElement("li");
  li.textContent = t;
  frag.appendChild(li);
});
list.appendChild(frag);
```


---

## Accessibility Basics

### Definition

Use semantic HTML, labels, `aria-*` when needed, keyboard focus.

### Why It Matters

Inclusive apps reach more users and reduce legal risk.

### How It Works

Don't rely on color alone; ensure buttons are real `<button>` elements.


```js
<button type="button" aria-expanded="false" id="menu-btn">
  Menu
</button>
```


---

## Shadow DOM Overview

### Definition

**Shadow DOM** encapsulates styles and markup inside Web Components.

### Why It Matters

Design systems and reusable widgets.

### How It Works

Brief exposure — advanced topic beyond this chapter.


```js
// const shadow = element.attachShadow({ mode: "open" });
// shadow.innerHTML = `<style>p { color: red; }</style><p>Hi</p>`;
```


---

### Selecting Elements — Example 1

```js
// Example 1: practical pattern for selecting elements
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


### Selecting Elements — Example 2

```js
// Example 2: practical pattern for selecting elements
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


### Selecting Elements — Example 3

```js
// Example 3: practical pattern for selecting elements
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


### Selecting Elements — Example 4

```js
// Example 4: practical pattern for selecting elements
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


### Selecting Elements — Example 5

```js
// Example 5: practical pattern for selecting elements
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

### Event Delegation — Example 1

```js
// Example 1: practical pattern for event delegation
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


### Event Delegation — Example 2

```js
// Example 2: practical pattern for event delegation
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


### Event Delegation — Example 3

```js
// Example 3: practical pattern for event delegation
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


### Event Delegation — Example 4

```js
// Example 4: practical pattern for event delegation
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


### Event Delegation — Example 5

```js
// Example 5: practical pattern for event delegation
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

### Forms and FormData — Example 1

```js
// Example 1: practical pattern for forms and formdata
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


### Forms and FormData — Example 2

```js
// Example 2: practical pattern for forms and formdata
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


### Forms and FormData — Example 3

```js
// Example 3: practical pattern for forms and formdata
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


### Forms and FormData — Example 4

```js
// Example 4: practical pattern for forms and formdata
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


### Forms and FormData — Example 5

```js
// Example 5: practical pattern for forms and formdata
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

### Events — Responding to Users — Example 1

```js
// Example 1: practical pattern for events — responding to users
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


### Events — Responding to Users — Example 2

```js
// Example 2: practical pattern for events — responding to users
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


### Events — Responding to Users — Example 3

```js
// Example 3: practical pattern for events — responding to users
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


### Events — Responding to Users — Example 4

```js
// Example 4: practical pattern for events — responding to users
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


### Events — Responding to Users — Example 5

```js
// Example 5: practical pattern for events — responding to users
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

### Using innerHTML with user input

XSS risk — use `textContent` or sanitize.

### Forgetting preventDefault on forms

Page reloads unexpectedly.

### Inline handlers

Hard to maintain — use `addEventListener`.


## Best Practices

- Prefer `querySelector` / `querySelectorAll`.
- Use event delegation for dynamic lists.
- Use `classList` instead of long `className` strings.
- Debounce expensive handlers.

## Interview Points

### What is event bubbling?

Events propagate from target up through ancestors unless stopped.

### Delegation benefits?

One listener, works for future children, less memory.

### Difference textContent vs innerHTML?

textContent is text only; innerHTML parses HTML.


## Exercises

### Exercise 8.1 — Todo list UI

Build list with add/delete using createElement.

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
// See delegation pattern in Event Delegation section
```


</details>

### Exercise 8.2 — Theme toggle

Toggle `dark` on body; save to localStorage — [ch11](./ch11-browser-apis.md).

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
document.body.classList.toggle("dark");
localStorage.setItem("theme", document.body.classList.contains("dark") ? "dark" : "light");
```


</details>

### Exercise 8.3 — Delegation rewrite

One click on ul handles all delete buttons.

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
list.addEventListener('click', handler);
```


</details>

### Exercise 8.4 — Keyboard shortcut

Log when user presses `?`.

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
document.addEventListener('keydown', e => { if (e.key === '?') console.log('help'); });
```


</details>

### Exercise 8.5 — Form validation

Prevent submit if email missing @.

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
if (!email.includes('@')) { e.preventDefault(); alert('Invalid'); }
```


</details>

### Exercise 8.6 — DocumentFragment

Add 100 items efficiently with fragment.

<details>
<summary>💡 Hint (click to reveal)</summary>

See the solution structure below if you are stuck.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>


```js
const f = document.createDocumentFragment(); /* append children */ list.append(f);
```


</details>

## Chapter Summary

| Topic | Practice |
|-------|----------|
| Selection | querySelector |
| Content | textContent for users |
| Events | addEventListener + delegation |
| Forms | preventDefault + FormData |


---

## Next Chapter

Next: handle failures gracefully with **error handling**.

---

**⬅️ [Previous: Asynchronous JavaScript](./ch07-asynchronous-javascript.md)** · **➡️ [Next Chapter: Error Handling →](./ch09-error-handling.md)**

---

*Last updated: 2026 | Chapter 8 of the Complete JavaScript Guide*

*Found an error or have a suggestion? [Open an issue on GitHub](https://github.com/zaid0091/CodeShelf/issues)*

---

## Worked Example 1: DOM and Events

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
// Worked example 1 for Chapter 8
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

## Worked Example 2: DOM and Events

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
// Worked example 2 for Chapter 8
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

## Worked Example 3: DOM and Events

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
// Worked example 3 for Chapter 8
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

## Worked Example 4: DOM and Events

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
// Worked example 4 for Chapter 8
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

## Worked Example 5: DOM and Events

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
// Worked example 5 for Chapter 8
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

## Worked Example 6: DOM and Events

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
// Worked example 6 for Chapter 8
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

## Worked Example 7: DOM and Events

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
// Worked example 7 for Chapter 8
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

