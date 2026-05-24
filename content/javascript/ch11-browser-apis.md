---
title: Browser APIs
description: fetch, localStorage, sessionStorage, JSON, and common Web APIs
order: 11
tags: [javascript, fetch, localStorage, json, browser, web-api]
---

# Chapter 11: Browser APIs

## 11.1 Browser vs JavaScript

JavaScript (ECMAScript) defines the language. **Web APIs** are provided by the browser (or Node with polyfills): DOM, `fetch`, `localStorage`, timers, etc.

```javascript
// Language
const x = [1, 2, 3].map((n) => n * 2);

// Web API
fetch("/api/users");
localStorage.setItem("theme", "dark");
```

## 11.2 `fetch` — HTTP requests

```javascript
async function getPosts() {
  const response = await fetch("https://jsonplaceholder.typicode.com/posts");

  if (!response.ok) {
    throw new Error(`HTTP error: ${response.status}`);
  }

  const posts = await response.json();
  return posts;
}
```

### POST with JSON

```javascript
async function createPost(title, body) {
  const response = await fetch("https://jsonplaceholder.typicode.com/posts", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ title, body, userId: 1 }),
  });

  return response.json();
}
```

| `fetch` option | Purpose |
|----------------|---------|
| `method` | GET, POST, PUT, PATCH, DELETE |
| `headers` | Content-Type, Authorization, etc. |
| `body` | String, FormData, Blob |
| `credentials` | `"include"` for cookies cross-origin |
| `signal` | `AbortController` for cancellation |

### Aborting requests

```javascript
const controller = new AbortController();

fetch("/api/slow", { signal: controller.signal })
  .then((r) => r.json())
  .catch((err) => {
    if (err.name === "AbortError") console.log("Cancelled");
  });

setTimeout(() => controller.abort(), 5000);
```

## 11.3 JSON — JavaScript Object Notation

```javascript
const user = { id: 1, name: "Alice", tags: ["admin"] };

const json = JSON.stringify(user, null, 2);
const copy = JSON.parse(json);

// JSON limitations
JSON.stringify({ date: new Date() }); // date becomes ISO string
JSON.stringify({ fn: () => {} });     // function omitted
```

| Method | Direction |
|--------|-----------|
| `JSON.stringify(obj)` | Object → string |
| `JSON.parse(str)` | String → object |

## 11.4 Web Storage — `localStorage` and `sessionStorage`

| API | Persistence | Scope |
|-----|-------------|-------|
| `localStorage` | Until cleared | Per origin, survives tab close |
| `sessionStorage` | Tab session | Per tab |

```javascript
// Store (values must be strings)
localStorage.setItem("user", JSON.stringify({ name: "Alice" }));

// Read
const raw = localStorage.getItem("user");
const user = raw ? JSON.parse(raw) : null;

// Remove
localStorage.removeItem("user");
localStorage.clear();

// Keys
for (let i = 0; i < localStorage.length; i++) {
  const key = localStorage.key(i);
  console.log(key, localStorage.getItem(key));
}
```

### Storage helper pattern

```javascript
const storage = {
  get(key, fallback = null) {
    try {
      const item = localStorage.getItem(key);
      return item ? JSON.parse(item) : fallback;
    } catch {
      return fallback;
    }
  },
  set(key, value) {
    localStorage.setItem(key, JSON.stringify(value));
  },
};
```

> **Security:** Never store passwords or JWTs in `localStorage` if XSS is possible. Prefer `httpOnly` cookies for sensitive tokens.

## 11.5 `URL` and query strings

```javascript
const url = new URL("https://example.com/search?q=js&page=2");

console.log(url.hostname);  // "example.com"
console.log(url.searchParams.get("q"));     // "js"
console.log(url.searchParams.get("page"));  // "2"

url.searchParams.set("sort", "date");
```

## 11.6 Timers

```javascript
const id = setTimeout(() => console.log("once"), 1000);
clearTimeout(id);

const intervalId = setInterval(() => console.log("tick"), 1000);
clearInterval(intervalId);

// requestAnimationFrame — smooth animations
function animate() {
  // update frame
  requestAnimationFrame(animate);
}
```

## 11.7 `navigator` and `location`

```javascript
console.log(navigator.userAgent);
console.log(navigator.language);

console.log(location.href);
location.hash = "#section-2";
```

## 11.8 Clipboard API

```javascript
async function copyText(text) {
  try {
    await navigator.clipboard.writeText(text);
  } catch (err) {
    console.error("Copy failed", err);
  }
}
```

Requires secure context (HTTPS or localhost).

## 11.9 Geolocation (optional)

```javascript
navigator.geolocation.getCurrentPosition(
  (pos) => {
    console.log(pos.coords.latitude, pos.coords.longitude);
  },
  (err) => console.error(err.message)
);
```

## 11.10 Putting it together — weather widget

```javascript
const API = "https://api.open-meteo.com/v1/forecast";

async function loadWeather(lat, lon) {
  const url = `${API}?latitude=${lat}&longitude=${lon}&current=temperature_2m`;
  const res = await fetch(url);
  if (!res.ok) throw new Error("Weather fetch failed");
  const data = await res.json();
  return data.current.temperature_2m;
}

async function init() {
  const cached = storage.get("lastTemp");
  if (cached != null) showTemp(cached);

  try {
    const temp = await loadWeather(40.71, -74.01);
    storage.set("lastTemp", temp);
    showTemp(temp);
  } catch (err) {
    showError(err.message);
  }
}
```

## 11.11 Chapter summary

| API | Use |
|-----|-----|
| `fetch` | HTTP GET/POST with async/await |
| `JSON` | Serialize for storage and APIs |
| `localStorage` | Persist non-sensitive UI state |
| `URL` | Parse and build query strings |
| `AbortController` | Cancel in-flight requests |

## Exercises

### Exercise 11.1 — User list

Fetch users from `jsonplaceholder.typicode.com/users` and render names in the DOM.

### Exercise 11.2 — Theme persistence

Save and restore dark/light theme with `localStorage` (pair with [ch08](./ch08-dom-and-events.md)).

### Exercise 11.3 — Search API

Build a search box that fetches posts where title contains the query (debounce input).

### Exercise 11.4 — Storage quota

Write a function that estimates bytes used in `localStorage` by summing key + value lengths.

---

**Previous:** [Chapter 10: Modules & npm](./ch10-modules-and-npm.md) · **Next:** [Chapter 12: OOP & Prototypes](./ch12-oop-prototypes.md)
