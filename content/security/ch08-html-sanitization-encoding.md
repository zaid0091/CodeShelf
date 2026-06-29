---
title: HTML Sanitization & Safe Output Encoding
description: Learn about context-aware output encoding, backend sanitization libraries, and how to defend against cross-context scripting vulnerabilities.
order: 8
tags: [security, xss, sanitization, encoding, templates]
---

# Chapter 8: HTML Sanitization & Safe Output Encoding

> **Understand why output encoding must be context-aware, explore templating engine auto-escapes, and learn how to sanitize text fields.**

---

## Context-Aware Output Encoding

When rendering untrusted data, the encoding technique must match the specific location (context) in the HTML document. Using the wrong encoding allows attackers to break out of elements.

### The 4 Major Contexts

| Context | Example Location | Target Characters to Encode | Safe Code Example |
|---------|------------------|-----------------------------|-------------------|
| **HTML Body** | `<div>UNTRUSTED</div>` | `<`, `>`, `&`, `"`, `'` | `&lt;script&gt;` |
| **HTML Attribute** | `<input value="UNTRUSTED">` | `"`, `'`, `&` | `<input value="&quot;test">` |
| **JavaScript** | `<script>let u = 'UNTRUSTED';</script>` | Unicode escapes (`\uXXXX`) | `<script>let u = '\u0027...';</script>` |
| **CSS** | `<div style="color: UNTRUSTED">` | Hexadecimal escapes (`\XX`) | `<div style="color: \31 \32 33">` |

---

## Templating Engine Protections

Most modern backend engines (Jinja2 in Flask, Django templates, Thymeleaf) enable auto-escaping by default.

### Python Jinja2 Example
```html
<!-- If user_name is "<script>alert(1)</script>" -->
<p>Welcome, {{ user_name }}</p> 
<!-- Output is safely rendered as: &lt;script&gt;alert(1)&lt;/script&gt; -->
```

### Bypassing Auto-Escaping (Backend Sinks)
Developers can explicitly disable escaping. Doing this incorrectly creates severe security vulnerabilities:

```html
<!-- DANGEROUS Django template rendering: -->
<p>Welcome, {{ user_name|safe }}</p>

<!-- DANGEROUS Jinja2 rendering: -->
<p>Welcome, {{ user_name | raw }}</p>
```

---

## Sanitizing on the Backend

When storing HTML inputs (e.g., from rich text editors), sanitize the input before saving it to the database, or before rendering. In Python, use **Bleach**:

```python
import bleach

dirty_html = "<b>Hello</b> <script>alert('xss')</script>"
# Whitelist tags: only allows 'b' and 'i'
clean_html = bleach.clean(dirty_html, tags=['b', 'i'], attributes={})
# Result: "<b>Hello</b> &lt;script&gt;alert('xss')&lt;/script&gt;"
```

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Encode variables right before rendering them to the client, keeping database records raw. | Sanitizing databases once on input and assuming the values are safe to render in any HTML/JS context later. |

---

## Interview Points

> **📌 Interview Point 1: Why is encoding variables inside `<script>` blocks using standard HTML entity escaping unsafe?**
> Inside `<script>` elements, the browser parses code as JavaScript, not HTML. Encoding `<` as `&lt;` is not recognized by the JS engine, which can lead to parsing errors or bypasses depending on variable delimiters. You must use JavaScript Unicode encoding instead.

---

## Exercises

### Exercise 1: Spot the injection vulnerability ⭐
**Task:** Identify the vulnerability in:
`<a href="{{ user_link }}">Click Here</a>` (assuming `user_link` is HTML-encoded).

<details>
<summary>✅ Solution (click to reveal)</summary>
Even if `user_link` is HTML-encoded, it is vulnerable to XSS if an attacker inputs `javascript:alert(1)`. Output encoding does not prevent execution of the `javascript:` protocol scheme in `href` links.
</details>

---

## Next Chapter

Continue to [Cross-Site Request Forgery (CSRF) & SameSite Cookies](./ch09-csrf-samesite-cookies.md) to explore session request attacks.
