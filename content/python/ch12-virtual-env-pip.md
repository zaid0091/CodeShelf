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

> **Definition:** Isolate dependencies per project.

### Why it matters

Avoid version conflicts globally.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
# python -m venv .venv
```


---

## System Python vs Project Python

> **Definition:** OS Python is shared; venv has own `site-packages`.

### Why it matters

Never pip install globally for apps.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
import sys
print(sys.prefix)
```


---

## Creating a venv with venv

> **Definition:** `python -m venv .venv` creates a folder.

### Why it matters

Commit `.venv` to gitignore, not repo.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
# python -m venv .venv
```


---

## Activating and Deactivating

> **Definition:** Activate sets PATH to venv python; `deactivate` restores.

### Why it matters

Must activate each new shell.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
# Windows: .venv\Scripts\activate
# Unix: source .venv/bin/activate
```


---

## What Changes Inside a venv

> **Definition:** `python`, `pip`, and `site-packages` point inside `.venv`.

### Why it matters

Imports resolve to installed packages there.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
import site
print(site.getsitepackages())
```


---

## Introduction to pip

> **Definition:** **pip** installs packages from PyPI.

### Why it matters

Comes with Python — upgrade occasionally.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
python -m pip --version
```


---

## Installing and Uninstalling Packages

> **Definition:** `pip install pkg` and `pip uninstall pkg`.

### Why it matters

Install into active environment only.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
python -m pip install requests
```


---

## Version Specifiers

> **Definition:** `==`, `>=`, `~=` in requirements pin compatibility.

### Why it matters

Reproducible builds need pins.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
# requests>=2.28,<3
```


---

## requirements.txt

> **Definition:** List of packages for `pip install -r requirements.txt`.

### Why it matters

Share with team and CI.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
# requirements.txt
requests==2.31.0
```


---

## Lock Files and Reproducibility

> **Definition:** Exact pins or tools like `pip-tools`/`uv` lock transitive deps.

### Why it matters

Production deploys need determinism.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
pip freeze > requirements.lock
```


---

## pyproject.toml and Modern Packaging

> **Definition:** PEP 518 project metadata and build backend.

### Why it matters

Standard for new libraries.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
# [project]
# name = 'myapp'
# version = '0.1.0'
```


---

## Editable Installs

> **Definition:** `pip install -e .` links source for development.

### Why it matters

Edit code without reinstalling.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
pip install -e .
```


---

## pip list, show, and freeze

> **Definition:** Inspect installed packages.

### Why it matters

Debug wrong versions.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
pip list
pip show requests
```


---

## Upgrading pip and Packages

> **Definition:** `python -m pip install -U pip`.

### Why it matters

Stay current for security fixes.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
python -m pip install -U pip
```


---

## Security: pip audit

> **Definition:** Scan dependencies for known CVEs.

### Why it matters

Run in CI pipelines.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
pip install pip-audit
pip-audit
```


---

## .gitignore for Python Projects

> **Definition:** Ignore `.venv/`, `__pycache__/`, `*.pyc`, `.env`.

### Why it matters

Keep secrets out of git.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
# .gitignore
.venv/
__pycache__/
```


---

## Multiple Python Versions

> **Definition:** Use `py -3.12` on Windows or `python3.11` on Linux.

### Why it matters

pyenv/asdf manage many versions.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
py -0p  # list installed
```


---

## pip vs conda vs uv

> **Definition:** pip is default; conda for scientific stacks; uv is fast modern installer.

### Why it matters

Pick one workflow per project.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
# team standard: venv + pip
```


---

## End-to-End Project Workflow

> **Definition:** venv → activate → pip install -r requirements → run tests.

### Why it matters

Document steps in README.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
# README quickstart commands
```


---

## Best Practices

### Guidelines

- One venv per project
- Pin dependencies for production


---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Installing globally | Breaks other projects | Always activate venv first |


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
