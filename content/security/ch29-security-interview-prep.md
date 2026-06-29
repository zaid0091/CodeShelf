---
title: "Interview Preparation: Web Security & OWASP Top 10"
description: 20 high-yield interview questions and answers covering OWASP Top 10 vulnerabilities, secure coding, web protocols, browser security controls, and cryptography.
order: 29
tags: [security, interview-prep, owasp, architecture, web-security]
---

# Chapter 29: Interview Preparation: Web Security & OWASP Top 10

> **Prepare for technical assessments with 20 critical interview questions and answers covering application security.**

---

## 1. What is the Same-Origin Policy (SOP)?
SOP is a fundamental browser security control. It restricts scripts running on one origin (protocol, domain, port combination) from reading data from another origin. It does not prevent sending data (which allows POST request CSRFs), but prevents reading responses (which blocks cross-origin token reading).

---

## 2. How does CORS relate to the Same-Origin Policy?
CORS (Cross-Origin Resource Sharing) is a mechanism that allows servers to declare relaxation policies for the SOP. By sending headers like `Access-Control-Allow-Origin`, the backend server explicitly permits specified external websites to read its responses.

---

## 3. What is the difference between Reflected, Stored, and DOM-based XSS?
*   **Reflected XSS**: The malicious script is sent inside a URL query or parameter and immediately echoed back in the server's HTML response.
*   **Stored XSS**: The payload is saved persistently (in a database/file) and executed whenever other users load the page rendering that data.
*   **DOM-based XSS**: The vulnerability exists entirely in the client-side JavaScript. The script reads data from a client source (like `location.hash`) and passes it to a client sink (like `element.innerHTML`) without server involvement.

---

## 4. How do you defend against Cross-Site Scripting (XSS)?
1. **Context-aware output encoding**: Encode characters like `<`, `>`, `&`, `"`, and `'` to safe HTML entities before rendering.
2. **HTML Sanitization**: Use libraries like DOMPurify (client) or Bleach (backend) when rendering rich text inputs.
3. **HTTP Cookie Flags**: Set session cookies with `HttpOnly` to block script access to `document.cookie`.
4. **Content Security Policy (CSP)**: Set strict script headers to block unauthorized script source execution.

---

## 5. What is CSRF and how is it exploited?
CSRF (Cross-Site Request Forgery) is an attack where a malicious site forces a victim's browser to execute state-changing actions on a target web application they are logged into. It exploits the browser's default behavior of automatically attaching session cookies to outbound requests made to target domains.

---

## 6. How do you prevent CSRF?
1. **SameSite Cookies**: Enforce `SameSite=Lax` or `SameSite=Strict` on session cookies to block transmission on cross-site requests.
2. **Anti-CSRF Tokens**: Generate cryptographically secure tokens associated with the session. Require forms to submit this token and validate it on the server.
3. **Custom Headers**: In SPAs, write request handlers that include custom headers (e.g., `X-Requested-With`). Browsers restrict cross-site origins from attaching custom headers unless pre-flight checks pass.

---

## 7. What is an IDOR vulnerability?
IDOR (Insecure Direct Object Reference) is a Broken Access Control vulnerability. It occurs when an application exposes a database record identifier directly in a URL (e.g., `/user/123/invoice`) and returns data without checking if the authenticated user owns or is authorized to view that specific record.

---

## 8. How do you mitigate IDOR?
1. **Object-Level Checks**: Implement authorization code logic to verify record ownership before querying or updating the database.
2. **UUIDs**: Use random version-4 UUIDs instead of sequential integers in URLs to prevent attackers from brute-forcing IDs.

---

## 9. What is Server-Side Request Forgery (SSRF)?
SSRF occurs when a backend server is tricked into making outbound HTTP requests to a destination specified by the attacker (e.g., scan internal ports, query private databases, or read cloud metadata keys from `169.254.169.254`).

---

## 10. How do you defend against SSRF?
1. **Outbound IP Blacklisting**: Resolve DNS and reject queries to private, loopback, or cloud-local metadata IP address ranges.
2. **Outbound Whitelisting**: Restrict API proxies to explicitly approved host domains.
3. **Enforce IMDSv2**: On AWS instances, enforce token-based metadata queries to prevent classic SSRF lookups.

---

## 11. What is the difference between Hashing and Encryption?
*   **Hashing**: A mathematical one-way function that is irreversible. It is used to verify integrity (e.g. passwords, files).
*   **Encryption**: A two-way function that is reversible using keys. It is used to maintain confidentiality (e.g. data in transit or database fields).

---

## 12. Why should you salt user passwords?
A salt is a random string added to the password before hashing. It prevents lookup and rainbow table attacks. Even if two users choose the same password, they will yield unique hash strings in the database because of their unique salts.

---

## 13. What is the difference between a Salt and a Pepper?
*   **Salt**: Unique per user, stored alongside the hashed password in the database.
*   **Pepper**: A secret key shared across all passwords, stored outside the database (e.g. in environment configuration files).

---

## 14. What are the current recommended password hashing algorithms?
**Argon2id** is the current industry champion recommended by OWASP because it is memory-hard and CPU-hard, limiting GPU-based cracking efficiency. **Bcrypt** is also a highly secure, time-tested standard.

---

## 15. What is the difference between SAST and DAST?
*   **SAST (Static Application Security Testing)**: Scans source code files without running the application (white-box). Excellent for finding syntax bugs, hardcoded secrets, or SQL injection vectors early.
*   **DAST (Dynamic Application Security Testing)**: Tests the running application externally (black-box). Excellent for finding server misconfigurations, SSL vulnerabilities, or missing security headers.

---

## 16. What does HSTS do?
HSTS (HTTP Strict Transport Security) is a response header that instructs browsers to convert all future HTTP requests for that domain to HTTPS automatically, preventing downgrade MITM attacks.

---

## 17. How does a SQL Injection work and how do prepared statements prevent it?
SQLi occurs when user input is concatenated directly into a query string, altering the SQL syntax structure. Prepared statements (parameterized queries) prevent this by pre-compiling the SQL template. The user input is handled strictly as a parameter value, never as executable SQL commands.

---

## 18. What is the risk of the `none` algorithm in JWT tokens?
If a JWT library respects `"alg": "none"`, an attacker can modify the token payload (e.g., elevating privileges) and sign it with the `"none"` algorithm. The server accepts it without signature validation. Mitigation: Always enforce a whitelist of algorithms during decodes.

---

## 19. What are the `__Host-` and `__Secure-` cookie prefixes?
They are browser-enforced security prefixes in cookie names. 
*   `__Secure-` enforces the `Secure` flag.
*   `__Host-` enforces `Secure`, binds the cookie to a specific host (no subdomains can access or overwrite it), and locks the path scope to `/`.

---

## 20. What is an XML External Entity (XXE) Injection and how is it prevented?
XXE occurs when an XML parser processes custom DTDs containing external entity references, allowing attackers to read files on the server or execute SSRF queries. Prevention: Disable DTD processing and external entity resolution in your XML parser configurations.

---

## Next Steps

**⬅️ [Previous: Automated Security Testing](./ch28-automated-security-testing.md)**

**➡️ [Back to Course Overview](./ch00-course-overview.md)**

---

*Chapter 29 of the Web Security Guide | CodeShelf*
