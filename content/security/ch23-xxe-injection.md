---
title: XML External Entity (XXE) Injection
description: Understand XML External Entity (XXE) vulnerabilities, how DTD parsers are exploited to leak files, and how to safely parse XML payloads.
order: 23
tags: [security, xxe, xml, dtd, external-entities]
---

# Chapter 23: XML External Entity (XXE) Injection

> **Deconstruct XML parsers, analyze how External Entities read local files, and disable DTD processing.**

---

## What is XXE Injection?

XXE Injection occurs when an XML parser is configured to process custom **Document Type Definitions (DTDs)** containing external entities. If the parser resolves these entities, an attacker can submit a malicious XML payload to read local files, scan internal ports, or trigger SSRF attacks.

---

## XML Entities & Exploitation

XML allows declaring shortcuts called entities. A standard entity is like a constant variable:
```xml
<!ENTITY author "Alice">
<title>&author;</title> <!-- resolves to <title>Alice</title> -->
```

An **External Entity** instructs the parser to fetch data from an external resource or system URI (like the local file system):
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "file:///etc/passwd" >
]>
<foo>&xxe;</foo>
```
*If the parser processes this DTD, it replaces `&xxe;` with the contents of the `/etc/passwd` file, returning it in the HTTP response.*

---

## Remediation: Secure XML Parsing

The primary mitigation is to disable **External Entity Resolution** and **DTD Processing** in your XML parser settings.

### 1. Python (defusedxml)
Standard Python libraries like `xml.etree` or `lxml` are vulnerable by default. Use `defusedxml` to parse XML securely:

```python
# VULNERABLE parsing
from lxml import etree
parser = etree.XMLParser(resolve_entities=True) # DANGEROUS

# SECURE parsing
import defusedxml.ElementTree as ET
# Auto-blocks DTD and external entities
root = ET.fromstring(xml_data)
```

### 2. Java (DOM Parser)
Disable external entity features before parsing:
```java
DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
dbf.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
```

---

## Best Practices & Common Mistakes

| Best Practice | Common Mistake |
|---------------|----------------|
| Use JSON instead of XML for web APIs wherever possible. | Assuming that using newer versions of programming languages automatically secures default XML parsing configurations. |

---

## Interview Points

> **📌 Interview Point 1: What is Blind XXE (Out-of-Band XXE)?**
> When the application does not return the resolved entity value in the response. Attackers exploit this by writing DTDs that force the XML parser to send the extracted file contents to an attacker-controlled server via HTTP or DNS queries.

---

## Exercises

### Exercise 1: Spot the vulnerability ⭐
**Task:** Identify the risk of parsing raw, unvalidated SVG image uploads.

<details>
<summary>✅ Solution (click to reveal)</summary>
SVG is an XML-based image format. If the backend processes uploaded SVGs using a vulnerable XML engine, it can trigger an XXE vulnerability.
</details>

---

## Next Chapter

Continue to [Secure Defaults & Hardening Web Servers](./ch24-hardening-web-servers.md) to explore host server security.
