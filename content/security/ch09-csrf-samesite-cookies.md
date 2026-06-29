---
title: Cross-Site Request Forgery (CSRF) & SameSite Cookies
description: Learn how Cross-Site Request Forgery (CSRF) exploits session state, how to implement anti-CSRF tokens, and how to use SameSite cookie attributes.
order: 9
tags: [security, csrf, cookies, samesite, session]
---

# Chapter 9: Cross-Site Request Forgery (CSRF) & SameSite Cookies

> **Understand how attackers exploit auto-sent cookie credentials to execute unauthorized state changes, and implement token-based and cookie-based defenses.**

---

## What is CSRF?

CSRF is an attack that forces a logged-in user to execute unwanted actions on a web application they are authenticated with. It exploits the browser's default behavior of automatically attaching cookies (including session cookies) to all outbound HTTP requests made to a target domain, regardless of which website initiates the request.

---

## CSRF Exploit Mechanics

### The Setup
1. A user logs into `bank.com` and receives a session cookie.
2. The user visits a malicious site `evil.com` in another tab.
3. `evil.com` hosts a hidden form pointing to `bank.com/transfer`:

```html
<form id="csrfForm" action="https://bank.com/transfer" method="POST">
  <input type="hidden" name="to" value="attacker">
  <input type="hidden" name="amount" value="5000">
</form>
<script>document.getElementById("csrfForm").submit();</script>
```

4. The browser automatically submits the form and attaches the `bank.com` session cookie.
5. The bank server processes the transaction, thinking the user authorized it.

---

## Anti-CSRF Mitigations

### 1. Anti-CSRF Tokens (Synchronizer Token Pattern)
The server generates a unique, unpredictable cryptographically secure token associated with the session. This token is inserted into client forms and sent on state-changing requests (POST/PUT/DELETE).
*   *Why it works:* Attackers on `evil.com` cannot read the token due to the **Same-Origin Policy (SOP)**, rendering them unable to craft valid requests.

### 2. Double-Submit Cookie Pattern
Used in stateless/SPA architectures. The server generates a random token and sets it as a client-side readable cookie. The client reads this cookie and duplicates its value in a custom HTTP header (like `X-CSRF-Token`).
*   *Why it works:* Attackers cannot read/write cookies on target domains.

---

## SameSite Cookie Flag

The `SameSite` attribute controls whether cookies are sent with cross-site requests.

| SameSite Value | Cross-Site POST Form Submissions | Cross-Site GET Link Navigation (e.g., clicking link) |
|----------------|----------------------------------|----------------------------------------------------|
| **`Strict`** | Cookie is blocked | Cookie is blocked |
| **`Lax`** (Default) | Cookie is blocked | Cookie is sent |
| **`None`** | Cookie is sent (Requires `Secure` flag) | Cookie is sent |

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Set `SameSite=Lax` or `SameSite=Strict` for all session cookies. | Relying on GET requests for state-changing operations (GET is immune to SameSite blocks under `Lax`). |

---

## Interview Points

> **📌 Interview Point 1: Can CSRF be used to steal user passwords?**
> No. CSRF is a **one-way write attack**. The attacker can execute actions on the server but cannot read the server's response due to the Same-Origin Policy. Therefore, they cannot steal session IDs or passwords directly.

---

## Exercises

### Exercise 1: Evaluate cookie security ⭐
**Task:** Given a session cookie `Set-Cookie: ID=123; Secure; HttpOnly; SameSite=None`, explain if it is vulnerable to CSRF.

<details>
<summary>✅ Solution (click to reveal)</summary>
Yes. `SameSite=None` allows cookies to be sent on cross-site requests, making the application fully reliant on other defenses (like CSRF tokens).
</details>

---

## Next Chapter

Continue to [Broken Access Control & IDOR](./ch10-broken-access-control-idor.md) to study user-level authorization vulnerabilities.
