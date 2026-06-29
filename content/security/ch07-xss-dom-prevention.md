---
title: Cross-Site Scripting (XSS) - DOM-Based & Prevention
description: Examine DOM-based Cross-Site Scripting (XSS) flows, framework-specific protections in React, and sanitization using DOMPurify.
order: 7
tags: [security, xss, dom-xss, react, sanitization, dompurify]
---

# Chapter 7: Cross-Site Scripting (XSS) - DOM-Based & Prevention

> **Understand DOM-based data flows from sources to sinks, explore how modern frontend frameworks handle XSS, and learn how to sanitize dynamic HTML.**

---

## DOM-Based XSS

DOM-based XSS occurs entirely in the client-side JavaScript. It happens when JS reads data from an untrusted **Source** (like the URL hash, query string, or referrer) and passes it to a dangerous **Sink** that executes code.

```text
Source (e.g., location.hash) -> client JS processing -> Sink (e.g., element.innerHTML)
```

### Common Sources & Sinks

| Sources (Inputs) | Sinks (Execution Points) |
|------------------|--------------------------|
| `location.search` | `element.innerHTML` |
| `location.hash` | `document.write()` |
| `document.referrer` | `eval()` |
| `window.name` | `setTimeout()` (with string arguments) |

### Vulnerable DOM Code
```javascript
// URL: page.html#<img src=x onerror=alert(1)>
// Source: location.hash
// Sink: innerHTML
const payload = decodeURIComponent(window.location.hash.substring(1));
document.getElementById("output").innerHTML = payload; // Script executes!
```

---

## Framework Protections (React & Vue)

Modern frameworks protect against XSS by auto-escaping values rendered in templates:

```jsx
// React automatically encodes characters like <, >, & to prevent HTML injection
const input = "<script>alert(1)</script>";
return <div>{input}</div>; // Safely rendered as text
```

### Bypassing Protections (Framework Sinks)
Both React and Vue provide escape hatches to render raw HTML. Using these improperly introduces XSS vulnerabilities:

```jsx
// REACT VULNERABILITY:
// If API output is unsanitized, this is vulnerable to XSS
return <div dangerouslySetInnerHTML={{ __html: apiResponse }} />;
```

```html
<!-- VUE VULNERABILITY: -->
<div v-html="apiResponse"></div>
```

---

## Client-Side Sanitization: DOMPurify

If you *must* render raw HTML on the client, clean the string beforehand using a dedicated sanitizer library like **DOMPurify**:

```javascript
import DOMPurify from 'dompurify';

const dirtyHTML = "<img src=x onerror=alert(1)> Safe Content";
const cleanHTML = DOMPurify.sanitize(dirtyHTML); // Removes the img element or its event handler
```

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Use `element.textContent` or `element.innerText` instead of `element.innerHTML` whenever inserting text. | Using client-side template engines or frameworks to print raw database responses without running sanitizers. |

---

## Interview Points

> **📌 Interview Point 1: What is the difference between HTML encoding and HTML sanitization?**
> **HTML encoding** converts characters into HTML entities (e.g. `<` becomes `&lt;`), converting scripts into safe text strings. **HTML sanitization** parses the HTML and removes dangerous tags/attributes (like `<script>` or `onerror`), preserving valid styling tags (like `<b>` or `<i>`).

---

## Exercises

### Exercise 1: Identify the source and sink ⭐
**Task:** Identify the source and sink in the following code:
`document.getElementById("greeting").innerHTML = new URLSearchParams(window.location.search).get("name");`

<details>
<summary>✅ Solution (click to reveal)</summary>
*   **Source**: `window.location.search` (specifically the `"name"` query parameter).
*   **Sink**: `innerHTML` property of the element.
</details>

---

## Next Chapter

Continue to [HTML Sanitization & Safe Output Encoding](./ch08-html-sanitization-encoding.md) to learn backend and templating encoding.
