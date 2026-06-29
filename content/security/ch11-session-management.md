---
title: "Session Management: Hijacking, Fixation, and Timeouts"
description: Explore typical session management threats like session hijacking and session fixation, and learn how to implement secure cookie settings and session lifecycles.
order: 11
tags: [security, session, hijacking, fixation, session-timeout]
---

# Chapter 11: Session Management: Hijacking, Fixation, and Timeouts

> **Learn how session states are compromised and implement robust session protection mechanisms including token rotation and timeouts.**

---

## The Session Lifecycle

HTTP is stateless. Web applications maintain a logical connection to users by associating them with a unique, server-side matched **Session ID** stored in the browser (usually as a cookie). The security of your application depends on how safely this ID is generated, stored, and retired.

---

## Session Hijacking

Session Hijacking occurs when an attacker obtains a user's active Session ID and uses it to impersonate them.

### Common Vectors
1. **Network Sniffing**: Intercepting cookies on unencrypted HTTP connections.
2. **Cross-Site Scripting (XSS)**: Using JavaScript `document.cookie` to steal credentials.
3. **Session ID Prediction**: Guessing sequential or weakly-hashed keys.

---

## Session Fixation

In a Session Fixation attack, the attacker forces a known session ID onto a victim's browser. When the victim logs in, the server elevates the authorization level of that *same* session ID, granting the attacker access.

```text
Attacker visits site -> Gets session ID (123) -> Attacker sends link to victim with ID=123 
-> Victim logs in using ID=123 -> Attacker accesses site using ID=123 (now logged in as victim)
```

### Mitigation
Always regenerate (re-create) the session identifier immediately upon authentication changes (login, logout, privilege changes).

```python
# Session regeneration flow (pseudocode)
def login_user(request):
    user = authenticate(request.username, request.password)
    if user:
        # 1. Store old session variables
        data = request.session.data
        # 2. Destroy old session ID
        request.session.destroy()
        # 3. Create fresh session ID and restore data
        request.session.create()
        request.session.data = data
```

---

## Secure Session Configuration

Implement strict parameters when setting session cookies:
*   **HttpOnly**: Blocks JavaScript access (XSS defense).
*   **Secure**: Restricts cookie transmission to HTTPS connections only.
*   **SameSite=Lax/Strict**: Prevents CSRF.
*   **Timeouts**:
    *   **Idle Timeout**: Auto-expires sessions if inactive (e.g. 15 minutes).
    *   **Absolute Timeout**: Expiates sessions regardless of activity (e.g. 24 hours).

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Invalidate session keys on both the client (delete cookie) and server (clear database/redis store) during logouts. | Only deleting the client-side cookie, leaving the session ID active in the database. |

---

## Interview Points

> **📌 Interview Point 1: Why should you regenerate session IDs upon login?**
> To prevent Session Fixation. By generating a new ID on login, any pre-auth session ID obtained by an attacker is orphaned and rendered useless.

---

## Exercises

### Exercise 1: Evaluate the risk ⭐
**Task:** If a user logs out and you run `document.cookie = "session_id=; expires=Thu, 01 Jan 1970 00:00:00 UTC;"` without deleting the record in Redis, what vulnerability exists?

<details>
<summary>✅ Solution (click to reveal)</summary>
An attacker who intercepted the session ID *before* logout can still access the application, as the ID is still valid in the server-side Redis store.
</details>

---

## Next Chapter

Continue to [Securing JSON Web Tokens (JWT) in Development & Prod](./ch12-securing-jwts.md) to explore stateless token architectures.
