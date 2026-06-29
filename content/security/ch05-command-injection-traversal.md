---
title: Command Injection & Path Traversal
description: Understand how OS Command Injection and Directory Path Traversal attacks function, and learn how to secure shell executions and file paths.
order: 5
tags: [security, command-injection, path-traversal, file-security, backend]
---

# Chapter 5: Command Injection & Path Traversal

> **Learn how unsanitized input triggers shell executions on the host system and how directory traversal compromises file systems.**

---

## OS Command Injection

Command injection occurs when user input is passed directly to system shell commands (e.g. `system()`, `exec()`, `subprocess.Popen`).

### Vulnerable Code (Python)
```python
import os

# Input: "8.8.8.8; rm -rf /"
# The shell interprets the semicolon and executes the deletion command
def ping_host(ip):
    os.system(f"ping -c 1 {ip}")
```

### Remediation
1. **Avoid shell commands**: Utilize native libraries (e.g. Python's `socket` library for network tests).
2. **Avoid `shell=True`**: In Python, pass arguments as a list to disable shell syntax parsing.

```python
import subprocess

# Secure approach
def ping_host_secure(ip):
    # Arguments are not parsed by a shell interpreter
    subprocess.run(["ping", "-c", "1", ip], check=True)
```

---

## Directory / Path Traversal

Path traversal allows attackers to read or write files outside the intended web root directory by using `../` segments.

### Vulnerable Code (Node.js)
```javascript
const fs = require('fs');

// Input: "../../../../etc/passwd"
app.get('/view', (req, res) => {
    const filename = req.query.file;
    fs.readFile('/var/www/uploads/' + filename, (err, data) => {
        res.send(data);
    });
});
```

### Remediation
1. **Use `basename`**: Isolate the file name, removing path directories.
2. **Resolve absolute paths**: Verify that the resolved absolute path starts with the intended directory.

```javascript
const path = require('path');

app.get('/view', (req, res) => {
    const baseDir = '/var/www/uploads/';
    const filename = path.basename(req.query.file); // Removes relative paths
    const safePath = path.join(baseDir, filename);
    
    // Additional check: verify directory starts with baseDir
    if (safePath.startsWith(baseDir)) {
        fs.readFile(safePath, ...);
    }
});
```

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Treat user inputs as strict index keys and fetch the corresponding file path from a predefined dictionary database. | Escaping path delimiters manually using regex search/replace, which can be bypassed (e.g., using URL-encoding `%2e%2e%2f`). |

---

## Interview Points

> **📌 Interview Point 1: What is the risk of using `shell=True` in Python `subprocess`?**
> When `shell=True` is set, the subprocess executes commands inside a system shell (`/bin/sh` or `cmd.exe`). This enables shell features like piping, redirects (`&&`, `;`), and variable expansions, opening paths for command injection.

---

## Exercises

### Exercise 1: Identify Command Injection ⭐
**Task:** Identify the vulnerability in:
`subprocess.Popen("cat " + user_file, shell=True)`

<details>
<summary>✅ Solution (click to reveal)</summary>
Using `shell=True` with string concatenation allows executing secondary commands if the input contains semicolons or pipe symbols.
</details>

---

## Next Chapter

Continue to [Cross-Site Scripting (XSS) - Reflected & Stored](./ch06-xss-reflected-stored.md) to explore client-side script injection.
