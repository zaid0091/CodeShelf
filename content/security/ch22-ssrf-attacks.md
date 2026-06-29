---
title: Server-Side Request Forgery (SSRF)
description: Examine Server-Side Request Forgery (SSRF) vulnerabilities, cloud metadata attacks (like AWS IMDSv1), and how to secure backend requests.
order: 22
tags: [security, ssrf, cloud-metadata, aws, backend-requests]
---

# Chapter 22: Server-Side Request Forgery (SSRF)

> **Understand how attackers trick backend servers into querying internal networks, analyze cloud metadata compromises, and implement secure outbound request filters.**

---

## What is SSRF?

SSRF is a vulnerability where the backend server is manipulated into executing arbitrary HTTP requests to a destination specified by the attacker. This allows attackers to bypass firewalls and access internal systems (like databases, Redis caches, or metadata services) that are not exposed to the public internet.

---

## SSRF Exploit Mechanics

### 1. Basic SSRF (Port Scanning / Internal Queries)
If a site has a PDF generator or image fetcher endpoint:
```text
Vulnerable URL: https://example.com/fetch?url=http://google.com/logo.png
Attacker URL: https://example.com/fetch?url=http://127.0.0.1:6379 (scans internal Redis port)
```

### 2. Cloud Metadata Attacks
Cloud instances (AWS, GCP, Azure) run a metadata service accessible locally at `169.254.169.254`. This endpoint returns configuration details, including IAM credentials.

```text
Attacker payload: https://example.com/fetch?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/role-name
```
*If IMDSv1 is enabled on AWS, this query returns temporary AWS keys, giving the attacker control over your cloud environment.*

---

## Vulnerable vs Secure Code

### Vulnerable Code (Python)
```python
import requests

@app.get("/proxy")
def proxy_request(url: str):
    # Vulnerable: fetches any URL without restriction
    response = requests.get(url)
    return response.text
```

### Remediation
1. **Domain Whitelisting**: Resolve and check domains against an explicit allowed host list.
2. **Block Private IPs**: Resolve DNS and verify that target IPs are not private or loopback ranges (`127.0.0.0/8`, `10.0.0.0/8`, `192.168.0.0/16`, `169.254.169.254`).
3. **Upgrade Cloud Services**: Upgrade AWS EC2 nodes to **IMDSv2** (which enforces session tokens, neutralizing standard SSRF requests).

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Perform DNS resolution of the input URL *before* validation to prevent DNS Rebinding attacks. | Relying on regular expressions to block substrings like `127.0.0.1` (which can be bypassed using decimal IP conversions like `2130706433` or localhost aliases). |

---

## Interview Points

> **📌 Interview Point 1: What is a DNS Rebinding Attack?**
> A technique used to bypass SSRF IP blacklists. The attacker registers a domain that initially resolves to a public IP (passes validation), but during the actual fetch connection steps resolves to a private IP (e.g. `127.0.0.1`), tricking the server.

---

## Exercises

### Exercise 1: Evaluate IP bypasses ⭐
**Task:** Identify which IP address `http://0x7f000001` represents.

<details>
<summary>✅ Solution (click to reveal)</summary>
It represents `127.0.0.1` (hexadecimal format). Many basic string filters miss this conversion, allowing SSRF bypasses.
</details>

---

## Next Chapter

Continue to [XML External Entity (XXE) Injection](./ch23-xxe-injection.md) to explore XML parsing vulnerabilities.
