---
title: Virtual Environments and pip
description: venv, pip, requirements.txt, pyproject.toml, and reproducible environments
order: 12
tags: [python, venv, pip]
---

# Chapter 12: Virtual Environments and pip

> **Isolate dependencies per project with virtual environments and pip — standard practice for every Python developer.**
> Take your time with each section — understanding beats speed.

---

## Table of Contents

1. [Why Virtual Environments Exist](#why-virtual-environments-exist)
2. [System Python vs Project Python](#system-python-vs-project-python)
3. [Creating a venv with venv](#creating-a-venv-with-venv)
4. [Activating and Deactivating](#activating-and-deactivating)
5. [What Changes Inside a venv](#what-changes-inside-a-venv)
6. [Introduction to pip](#introduction-to-pip)
7. [Installing and Uninstalling Packages](#installing-and-uninstalling-packages)
8. [Version Specifiers](#version-specifiers)
9. [requirements.txt](#requirements-txt)
10. [Lock Files and Reproducibility](#lock-files-and-reproducibility)
11. [pyproject.toml and Modern Packaging](#pyproject-toml-and-modern-packaging)
12. [Editable Installs](#editable-installs)
13. [pip list, show, and freeze](#pip-list-show-and-freeze)
14. [Upgrading pip and Packages](#upgrading-pip-and-packages)
15. [Security: pip audit](#security-pip-audit)
16. [.gitignore for Python Projects](#gitignore-for-python-projects)
17. [Multiple Python Versions](#multiple-python-versions)
18. [pip vs conda vs uv](#pip-vs-conda-vs-uv)
19. [End-to-End Project Workflow](#end-to-end-project-workflow)
20. [Best Practices](#best-practices)
21. [Common Mistakes](#common-mistakes)
22. [Interview Points](#interview-points)
23. [Exercises](#exercises)
24. [Chapter Summary](#chapter-summary)

---

## Why Virtual Environments Exist

> **Definition:** This section explains **Why Virtual Environments Exist** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **why virtual environments exist** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Why Virtual Environments Exist
x = chapter_12_demo = True
print("Why Virtual Environments Exist", x)
```

### Hands-on: Why Virtual Environments Exist

1. State **Why Virtual Environments Exist** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## System Python vs Project Python

> **Definition:** This section explains **System Python vs Project Python** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **system python vs project python** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: System Python vs Project Python
x = chapter_12_demo = True
print("System Python vs Project Python", x)
```

### Hands-on: System Python vs Project Python

1. State **System Python vs Project Python** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Creating a venv with venv

> **Definition:** This section explains **Creating a venv with venv** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **creating a venv with venv** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Creating a venv with venv
x = chapter_12_demo = True
print("Creating a venv with venv", x)
```

### Hands-on: Creating a venv with venv

1. State **Creating a venv with venv** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Activating and Deactivating

> **Definition:** This section explains **Activating and Deactivating** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **activating and deactivating** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Activating and Deactivating
x = chapter_12_demo = True
print("Activating and Deactivating", x)
```

### Hands-on: Activating and Deactivating

1. State **Activating and Deactivating** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## What Changes Inside a venv

> **Definition:** This section explains **What Changes Inside a venv** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **what changes inside a venv** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: What Changes Inside a venv
x = chapter_12_demo = True
print("What Changes Inside a venv", x)
```

### Hands-on: What Changes Inside a venv

1. State **What Changes Inside a venv** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Introduction to pip

> **Definition:** This section explains **Introduction to pip** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **introduction to pip** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Introduction to pip
x = chapter_12_demo = True
print("Introduction to pip", x)
```

### Hands-on: Introduction to pip

1. State **Introduction to pip** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Installing and Uninstalling Packages

> **Definition:** This section explains **Installing and Uninstalling Packages** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **installing and uninstalling packages** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Installing and Uninstalling Packages
x = chapter_12_demo = True
print("Installing and Uninstalling Packages", x)
```

### Hands-on: Installing and Uninstalling Packages

1. State **Installing and Uninstalling Packages** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Version Specifiers

> **Definition:** This section explains **Version Specifiers** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **version specifiers** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Version Specifiers
x = chapter_12_demo = True
print("Version Specifiers", x)
```

### Hands-on: Version Specifiers

1. State **Version Specifiers** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## requirements.txt

> **Definition:** This section explains **requirements.txt** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **requirements.txt** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: requirements.txt
x = chapter_12_demo = True
print("requirements.txt", x)
```

### Hands-on: requirements.txt

1. State **requirements.txt** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Lock Files and Reproducibility

> **Definition:** This section explains **Lock Files and Reproducibility** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **lock files and reproducibility** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Lock Files and Reproducibility
x = chapter_12_demo = True
print("Lock Files and Reproducibility", x)
```

### Hands-on: Lock Files and Reproducibility

1. State **Lock Files and Reproducibility** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## pyproject.toml and Modern Packaging

> **Definition:** This section explains **pyproject.toml and Modern Packaging** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **pyproject.toml and modern packaging** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: pyproject.toml and Modern Packaging
x = chapter_12_demo = True
print("pyproject.toml and Modern Packaging", x)
```

### Hands-on: pyproject.toml and Modern Packaging

1. State **pyproject.toml and Modern Packaging** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Editable Installs

> **Definition:** This section explains **Editable Installs** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **editable installs** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Editable Installs
x = chapter_12_demo = True
print("Editable Installs", x)
```

### Hands-on: Editable Installs

1. State **Editable Installs** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## pip list, show, and freeze

> **Definition:** This section explains **pip list, show, and freeze** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **pip list, show, and freeze** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: pip list, show, and freeze
x = chapter_12_demo = True
print("pip list, show, and freeze", x)
```

### Hands-on: pip list, show, and freeze

1. State **pip list, show, and freeze** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Upgrading pip and Packages

> **Definition:** This section explains **Upgrading pip and Packages** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **upgrading pip and packages** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Upgrading pip and Packages
x = chapter_12_demo = True
print("Upgrading pip and Packages", x)
```

### Hands-on: Upgrading pip and Packages

1. State **Upgrading pip and Packages** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Security: pip audit

> **Definition:** This section explains **Security: pip audit** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **security: pip audit** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Security: pip audit
x = chapter_12_demo = True
print("Security: pip audit", x)
```

### Hands-on: Security: pip audit

1. State **Security: pip audit** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## .gitignore for Python Projects

> **Definition:** This section explains **.gitignore for Python Projects** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **.gitignore for python projects** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: .gitignore for Python Projects
x = chapter_12_demo = True
print(".gitignore for Python Projects", x)
```

### Hands-on: .gitignore for Python Projects

1. State **.gitignore for Python Projects** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Multiple Python Versions

> **Definition:** This section explains **Multiple Python Versions** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **multiple python versions** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Multiple Python Versions
x = chapter_12_demo = True
print("Multiple Python Versions", x)
```

### Hands-on: Multiple Python Versions

1. State **Multiple Python Versions** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## pip vs conda vs uv

> **Definition:** This section explains **pip vs conda vs uv** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **pip vs conda vs uv** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: pip vs conda vs uv
x = chapter_12_demo = True
print("pip vs conda vs uv", x)
```

### Hands-on: pip vs conda vs uv

1. State **pip vs conda vs uv** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## End-to-End Project Workflow

> **Definition:** This section explains **End-to-End Project Workflow** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **end-to-end project workflow** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: End-to-End Project Workflow
x = chapter_12_demo = True
print("End-to-End Project Workflow", x)
```

### Hands-on: End-to-End Project Workflow

1. State **End-to-End Project Workflow** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Best Practices

> **Definition:** This section explains **Best Practices** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **best practices** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Best Practices
x = chapter_12_demo = True
print("Best Practices", x)
```

### Hands-on: Best Practices

1. State **Best Practices** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Common Mistakes

> **Definition:** This section explains **Common Mistakes** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **common mistakes** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Common Mistakes
x = chapter_12_demo = True
print("Common Mistakes", x)
```

### Hands-on: Common Mistakes

1. State **Common Mistakes** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Interview Points

Study these before technical interviews. Practice answering out loud in 60–90 seconds.

---

> **📌 Interview Point 1: Why virtual environments?**

Isolate dependencies per project — avoid version conflicts globally.

---

> **📌 Interview Point 2: venv vs virtualenv?**

`venv` stdlib since 3.3; `virtualenv` third-party faster/older features.

---

> **📌 Interview Point 3: What does activate do?**

Prepends venv `bin`/`Scripts` to PATH — `python` and `pip` point to venv.

---

> **📌 Interview Point 4: requirements.txt purpose?**

Pinned dependencies for reproducible `pip install -r`.

---

> **📌 Interview Point 5: pip freeze vs pip list?**

`freeze` install format; `list` human readable all packages.

---

> **📌 Interview Point 6: pyproject.toml role?**

Modern packaging metadata — PEP 517/518 build system.

---

> **📌 Interview Point 7: Editable install?**

`pip install -e .` — src changes reflect without reinstall.

---

> **📌 Interview Point 8: Why not pip install globally?**

Breaks other projects; may need admin; wrong Python version.

---

> **📌 Interview Point 9: pip vs conda?**

pip: PyPI packages. conda: binary stacks, non-Python deps — different ecosystems.

---

> **📌 Interview Point 10: What is uv?**

Fast modern installer/resolver — drop-in pip alternative gaining adoption.

---

> **📌 Interview Point 11: SECURITY: pip audit?**

Scan known CVEs in dependencies — run in CI.

---

> **📌 Interview Point 12: PYTHONPATH?**

Extra module search paths — prefer proper package install.

---

> **📌 Interview Point 13: Multiple Python versions?**

pyenv, official installers — match project `.python-version`.

---

> **📌 Interview Point 14: Docker + venv?**

Often install into system/site in container (disposable env).

---

> **📌 Interview Point 15: Lock files?**

`pip-tools`, Poetry, uv lock — exact reproducible builds.

---

## Exercises

Try each exercise before opening solutions.

---

Try each exercise before opening the solution. Type the code yourself — muscle memory matters.

---

### Exercise 1: Create venv ⭐

**Task:** Document commands to create and activate venv.

<details>
<summary>💡 Hint (click to reveal)</summary>

python -m venv .venv.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
```

</details>

---

### Exercise 2: freeze requirements ⭐⭐

**Task:** Explain pip freeze > requirements.txt.

<details>
<summary>💡 Hint (click to reveal)</summary>

reproducible installs.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```bash
pip install requests
pip freeze > requirements.txt
```

</details>


## Chapter Summary

| Concept | Takeaway |
|---------|----------|
| **venv** | Isolated interpreter per project |
| **pip** | Install from PyPI |
| **requirements.txt** | Pinned dependencies |
| **pyproject.toml** | Modern project metadata |

### Key rules to remember

```text
✅ Read error messages — they name the line and problem
✅ Type examples yourself instead of only reading
✅ Use the REPL for one-line experiments
❌ Do not copy-paste without understanding each line
```

---

## Previous / Next Chapter

**⬅️ [Previous: Decorators and Generators](./ch11-decorators-generators.md)**

**➡️ [Next: Best Practices →](./ch13-best-practices.md)**

---


*Chapter of the Complete Python Guide | CodeShelf*
