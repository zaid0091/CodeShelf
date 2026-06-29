---
title: Secure Defaults & Hardening Web Servers
description: Hardening configurations for web servers (Nginx, Apache). Learn about server banner disabling, limiting request sizes, disabling HTTP methods, and mitigating DoS vectors.
order: 24
tags: [security, server-hardening, nginx, secure-defaults, infrastructure]
---

# Chapter 24: Secure Defaults & Hardening Web Servers

> **Expose fewer details to attackers. Harden Nginx and Apache configurations, disable banner disclosures, and restrict HTTP methods.**

---

## The Principle of Secure Defaults

Applications and servers must be secure-by-default. This means default setups must run under the most restrictive rules possible, requiring administrators to explicitly enable features as needed.

---

## 1. Disabling Banner Disclosures

By default, Nginx and Apache display their specific version numbers in HTTP response headers and error pages. Attackers scan headers to match version numbers against lists of public CVE vulnerabilities.

### Nginx Hiding version
Modify `/etc/nginx/nginx.conf`:
```nginx
http {
    # Hides Nginx version (e.g., outputs "Server: nginx" instead of "nginx/1.22.1")
    server_tokens off;
}
```

### Apache Hiding version
Modify `httpd.conf`:
```apache
ServerTokens Prod
ServerSignature Off
```

---

## 2. Restricting HTTP Methods

Disable HTTP methods that are not required for your web application. Methods like `TRACE` (can leak session cookies via XSS) or `PUT`/`DELETE` (if public access is not intended) must be restricted.

```nginx
# Nginx configuration to restrict methods
if ($request_method !~ ^(GET|POST|HEAD)$ ) {
    return 405;
}
```

---

## 3. Mitigating Denial of Service (DoS)

Configure resource limits to prevent memory exhaustion and slowloris attacks (where attackers open connections and send data very slowly to exhaust the server's thread pool).

### Nginx Buffer Limits
```nginx
# Restrict body payload size (e.g., max 10MB file uploads)
client_max_body_size 10M;

# Set short timeouts to drop idle connections
client_body_timeout 10s;
client_header_timeout 10s;
keepalive_timeout 65s;
send_timeout 10s;
```

---

## 4. Run Services as Non-Root

Never run web servers or application processes (like Gunicorn, Node.js) as the root user. If an attacker achieves Remote Code Execution (RCE), they inherit the privileges of the running process. Run under designated accounts (e.g. `www-data`, `nginx`, or a custom non-root system user).

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Set up automatic security updates for host operating systems and web server binaries. | Leaving default welcome landing pages (like index.html of Nginx/Apache) active on production domains. |

---

## Interview Points

> **📌 Interview Point 1: What is a Slowloris Attack?**
> A type of Denial of Service attack where the client opens multiple connections to the web server and sends partial HTTP headers very slowly. This keeps thread pools occupied, preventing legitimate users from establishing connections. Mitigation: Set short header read timeouts (`client_header_timeout` in Nginx).

---

## Exercises

### Exercise 1: Evaluate Server Headers ⭐
**Task:** Given an HTTP header: `Server: Apache/2.4.41 (Ubuntu)`, what is the vulnerability?

<details>
<summary>✅ Solution (click to reveal)</summary>
Information Disclosure. It reveals the exact server version and host OS. Attackers can look up known vulnerabilities for Apache 2.4.41.
</details>

---

## Next Chapter

Continue to [Vulnerable and Outdated Components (SCA)](./ch25-dependency-vulnerabilities.md) to study dependency auditing.
