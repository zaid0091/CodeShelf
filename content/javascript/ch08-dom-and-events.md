---
title: DOM and Events
description: Selecting elements, manipulating the DOM, events, and event delegation
order: 8
tags: [javascript, dom, events, delegation, browser]
---

# Chapter 8: DOM and Events

## 8.1 What is the DOM?

> **Definition:** The **Document Object Model (DOM)** is a tree-shaped API that represents an HTML (or XML) document. JavaScript can read and modify structure, content, and styles.

```text
document
 └── html
      ├── head
      └── body
           ├── header#site-header
           ├── main
           │    └── ul#todo-list
           │         ├── li.todo
           │         └── li.todo
           └── script
```

## 8.2 Selecting elements

| Method | Returns | Notes |
|--------|---------|-------|
| `getElementById(id)` | Element or null | Single ID |
| `querySelector(css)` | First match or null | Flexible CSS |
| `querySelectorAll(css)` | NodeList | Static collection |
| `getElementsByClassName(c)` | HTMLCollection | Live in older DOM |
| `getElementsByTagName(tag)` | HTMLCollection | Live |

```javascript
const title = document.getElementById("title");
const firstBtn = document.querySelector(".btn-primary");
const allItems = document.querySelectorAll(".todo-item");

console.log(allItems.length);
allItems.forEach((el) => console.log(el.textContent));
```

### Scoped queries

```javascript
const list = document.querySelector("#todo-list");
const items = list.querySelectorAll("li");
```

## 8.3 Reading and changing content

```javascript
const el = document.querySelector("#message");

// Text (escapes HTML — safe for user data)
el.textContent = "Hello, world!";

// HTML (use carefully — XSS risk)
el.innerHTML = "<strong>Hello</strong>";

// Attributes
el.setAttribute("data-id", "42");
el.getAttribute("data-id");
el.dataset.id; // "42" from data-id

// Classes
el.classList.add("active");
el.classList.remove("hidden");
el.classList.toggle("selected");
el.classList.contains("active");

// Styles
el.style.color = "crimson";
el.style.fontSize = "1.25rem";
```

## 8.4 Creating and removing nodes

```javascript
const li = document.createElement("li");
li.textContent = "New task";
li.className = "todo-item";

const list = document.querySelector("#todo-list");
list.appendChild(li);

// Modern: insertAdjacentHTML, replaceChildren
list.insertAdjacentHTML("beforeend", "<li>Quick add</li>");

li.remove(); // remove from DOM
```

| Method | Effect |
|--------|--------|
| `append(child)` | Add to end |
| `prepend(child)` | Add to start |
| `before(node)` | Sibling before element |
| `after(node)` | Sibling after element |
| `replaceChildren(...nodes)` | Replace all children |

## 8.5 Events — responding to user actions

```javascript
const button = document.querySelector("#save-btn");

button.addEventListener("click", (event) => {
  console.log("Clicked!", event.target);
});

// Remove listener (same function reference required)
function handleClick(e) {
  console.log(e.type);
}
button.addEventListener("click", handleClick);
button.removeEventListener("click", handleClick);
```

### Common events

| Event | When |
|-------|------|
| `click` | Mouse click / tap |
| `submit` | Form submitted |
| `input` | Input value changed |
| `change` | Value committed (select, blur) |
| `keydown` / `keyup` | Keyboard |
| `load` | Resource loaded |
| `DOMContentLoaded` | HTML parsed, before images |

```javascript
document.addEventListener("DOMContentLoaded", () => {
  console.log("DOM ready");
});
```

## 8.6 The event object

```javascript
input.addEventListener("keydown", (e) => {
  if (e.key === "Enter") submitForm();
  if (e.ctrlKey && e.key === "s") {
    e.preventDefault();
    save();
  }
});
```

| Property / method | Purpose |
|-------------------|---------|
| `e.target` | Element that triggered the event |
| `e.currentTarget` | Element with listener attached |
| `e.preventDefault()` | Cancel default (e.g. form submit) |
| `e.stopPropagation()` | Stop bubbling to parents |

## 8.7 Event propagation — bubbling and capturing

```text
click on <button>
  → capturing phase (window → ... → button)
  → target phase
  → bubbling phase (button → ... → window)
```

```javascript
parent.addEventListener("click", () => {
  console.log("parent");
});

child.addEventListener("click", (e) => {
  e.stopPropagation();
  console.log("child");
});
```

## 8.8 Event delegation

> **Definition:** **Event delegation** attaches one listener on a parent and uses `event.target` to handle events from dynamically added children.

```javascript
const list = document.querySelector("#todo-list");

list.addEventListener("click", (e) => {
  const item = e.target.closest("li.todo-item");
  if (!item) return;

  if (e.target.matches("button.delete")) {
    item.remove();
  } else if (e.target.matches("input[type=checkbox]")) {
    item.classList.toggle("completed", e.target.checked);
  }
});
```

Benefits:

- Fewer listeners (performance)
- Works for elements added later
- Simpler cleanup

## 8.9 Forms

```javascript
const form = document.querySelector("#signup-form");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const data = new FormData(form);
  const email = data.get("email");
  const password = data.get("password");

  console.log({ email, password });
});
```

## 8.10 Performance tips

```javascript
// Debounce — wait until typing stops
function debounce(fn, ms) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), ms);
  };
}

searchInput.addEventListener(
  "input",
  debounce((e) => fetchResults(e.target.value), 300)
);
```

## 8.11 Chapter summary

| Topic | Practice |
|-------|----------|
| Selection | Prefer `querySelector` / `querySelectorAll` |
| Text vs HTML | `textContent` for user strings |
| Events | `addEventListener`, avoid inline handlers |
| Delegation | Parent listener + `closest` / `matches` |
| Forms | `preventDefault` + `FormData` |

## Exercises

### Exercise 8.1 — Todo list UI

Build HTML with an input, Add button, and `<ul>`. Add items on click; each item has a delete button.

### Exercise 8.2 — Toggle theme

A button toggles `dark` class on `<body>` and saves preference to `localStorage` (see [ch11](./ch11-browser-apis.md)).

### Exercise 8.3 — Delegation

Rewrite Exercise 8.1 using one click listener on `<ul>` instead of per-item listeners.

### Exercise 8.4 — Keyboard shortcuts

On `document`, listen for `keydown` and log when user presses `?` for help.

---

**Previous:** [Chapter 7: Asynchronous JavaScript](./ch07-asynchronous-javascript.md) · **Next:** [Chapter 9: Error Handling](./ch09-error-handling.md)
