---
title: Security Logging & Monitoring
description: Learn about secure logging practices, preventing log injection vulnerabilities, masking sensitive data, and setting up monitoring alerts.
order: 27
tags: [security, logging, monitoring, logs, log-injection]
---

# Chapter 27: Security Logging & Monitoring

> **Implement secure audit logs, prevent log injection tampering, mask sensitive credentials, and configure intrusion alerts.**

---

## The Risk: Invisible Intrusions

According to security statistics, the average time to detect a data breach is over 200 days. If an application fails to log critical events (login failures, privilege modifications, high-value transactions), or stores logs locally where attackers can delete them, security teams remain blind to intrusions.

---

## Log Injection (Log Forgery)

Log injection occurs when an application writes unsanitized user input to log files. Attackers inject newline characters (`\n` or `\r\n`) followed by fake log entries to deceive auditors or hide footprints.

### Vulnerable Code (Python)
```python
# Input: "user123\n[INFO] 2026-06-29 10:00:00 - User admin successfully logged in"
# Result: Generates a fake second log line indicating admin login
logger.info(f"Failed login attempt for user: {user_input}")
```

### Remediation
1. **Sanitize Inputs**: Strip newline and carriage return characters before logging.
2. **Structured Logging**: Use JSON formats for logs. Modern logging collectors parse JSON properties strictly, preventing plain text forgery injections.

```python
# Secure JSON logging format
logger.info({
    "event": "failed_login",
    "username": user_input.replace('\n', '').replace('\r', ''),
    "ip": client_ip
})
```

---

## What to Log vs. What NOT to Log

To comply with privacy laws (GDPR, PCI-DSS) and secure secrets, verify logging filters:

| Should Log (Audit Trails) | Should NOT Log (Sensitive Data) |
|---------------------------|---------------------------------|
| Failed login attempts (helps detect brute-forcing). | Plaintext passwords or credentials. |
| Account password resets or email changes. | Session tokens, JWTs, or API keys. |
| Database record deletions or modifications. | Full credit card numbers (PAN) or CVVs. |
| Authorization failures (403 HTTP codes). | Personal Health Information (PHI) or private PII. |

---

## Centralized Logging Architecture

Never store production log files locally on application servers. If an attacker gains server access, they will delete logs to hide their tracks. Stream logs in real-time to external, centralized logging aggregators (e.g., Elasticsearch/Logstash/Kibana (ELK), Splunk, Datadog).

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Configure real-time alerts for spikes in authorization failures (403s) or system errors (500s) to detect active scanners. | Storing logs in clear text files without access control restrictions, exposing them to read-access exploits. |

---

## Interview Points

> **📌 Interview Point 1: What is the risk of logging sensitive data like passwords?**
> If logs contain clear text passwords, anyone with access to the logging dashboard (developers, auditors, support staff) can read them. Furthermore, if the log store is leaked, thousands of user credentials are exposed without requiring database decryptions.

---

## Exercises

### Exercise 1: Spot the logging bug ⭐
**Task:** Identify the problem with:
`logger.error(f"Transaction failed for token: {request.headers.get('Authorization')}")`

<details>
<summary>✅ Solution (click to reveal)</summary>
Information Disclosure. It writes the active authentication token to the log file.
</details>

---

## Next Chapter

Continue to [Automated Security Testing](./ch28-automated-security-testing.md) to explore CI/CD scanners.
