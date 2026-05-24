---
title: Python Best Practices
description: PEP 8, black, ruff, type hints, pytest, logging, security, and project layout
order: 13
tags: [python, best-practices, testing]
---

# Chapter 13: Python Best Practices

> **Writing code that works is step one. Writing code others can maintain requires style, tests, and tooling discipline.**
> Take your time with each section — understanding beats speed.

---

## Table of Contents

1. [The Zen of Python](#the-zen-of-python)
2. [Readability and Maintainability](#readability-and-maintainability)
3. [PEP 8 Style Guide](#pep-8-style-guide)
4. [Naming Conventions](#naming-conventions)
5. [Imports and Module Structure](#imports-and-module-structure)
6. [Formatting Tools: black and ruff](#formatting-tools-black-and-ruff)
7. [Type Hints Fundamentals](#type-hints-fundamentals)
8. [Static Analysis with mypy](#static-analysis-with-mypy)
9. [Project Layout Patterns](#project-layout-patterns)
10. [Documentation and Docstrings](#documentation-and-docstrings)
11. [Testing with pytest](#testing-with-pytest)
12. [Fixtures and Test Organization](#fixtures-and-test-organization)
13. [Logging vs print](#logging-vs-print)
14. [Configuration and Secrets](#configuration-and-secrets)
15. [Error Handling Discipline](#error-handling-discipline)
16. [Performance: Measure First](#performance-measure-first)
17. [Security Basics](#security-basics)
18. [Code Review Checklist](#code-review-checklist)
19. [Best Practices Summary Table](#best-practices-summary-table)
20. [Common Mistakes](#common-mistakes)
21. [Pre-commit Hooks](#pre-commit-hooks)
22. [Interview Points](#interview-points)
23. [Exercises](#exercises)
24. [Chapter Summary](#chapter-summary)

---

## The Zen of Python

> **Definition:** Run `import this` for design principles.

### Why it matters

Readability counts.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
import this
```


---

## Readability and Maintainability

> **Definition:** Code is read more than written.

### Why it matters

Clear beats clever.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
# prefer explicit names over cryptic abbreviations
```


---

## PEP 8 Style Guide

> **Definition:** Official conventions for layout and naming.

### Why it matters

Use black/ruff to automate.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
# 4 spaces, two blank lines between top-level defs
```


---

## Naming Conventions

> **Definition:** snake_case functions, CapWords classes, UPPER constants.

### Why it matters

Consistency across modules.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
MAX_RETRIES = 3
def fetch_data(): ...
```


---

## Imports and Module Structure

> **Definition:** stdlib, third-party, local — blank line between groups.

### Why it matters

Absolute imports preferred.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
import os
from pathlib import Path
from myapp import utils
```


---

## Formatting Tools: black and ruff

> **Definition:** Auto-format and lint.

### Why it matters

Run in CI and pre-commit.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
# ruff check .
# black .
```


---

## Type Hints Fundamentals

> **Definition:** Annotate parameters and returns.

### Why it matters

mypy catches bugs early.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def greet(name: str) -> str:
    return f'Hi {name}'
```


---

## Static Analysis with mypy

> **Definition:** Type checker without running code.

### Why it matters

Add gradually to legacy projects.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
# mypy src/
```


---

## Project Layout Patterns

> **Definition:** src layout, tests beside or under tests/.

### Why it matters

Document in README.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
src/myapp/__init__.py
```


---

## Documentation and Docstrings

> **Definition:** Google or NumPy docstring styles.

### Why it matters

Generate docs with Sphinx/MkDocs.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def fn():
    """One-line summary.

    Args:
        x: description
    """
```


---

## Testing with pytest

> **Definition:** Functions named `test_*` discovered automatically.

### Why it matters

Assertions use plain `assert`.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
def test_add():
    assert add(1,2) == 3
```


---

## Fixtures and Test Organization

> **Definition:** `@pytest.fixture` shares setup.

### Why it matters

Keep tests fast and isolated.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
import pytest
@pytest.fixture
def user():
    return {'id':1}
```


---

## Logging vs print

> **Definition:** `logging` levels and handlers for production.

### Why it matters

print is for quick debugging only.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info('started')
```


---

## Configuration and Secrets

> **Definition:** Environment variables via `os.environ` or `.env` files.

### Why it matters

Never commit API keys.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
import os
api_key = os.environ['API_KEY']
```


---

## Error Handling Discipline

> **Definition:** Catch specific exceptions; log context.

### Why it matters

Fail fast on programmer errors.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
except ValueError as e:
    logger.warning('bad input %s', e)
```


---

## Performance: Measure First

> **Definition:** Profile with `cProfile` before optimizing.

### Why it matters

Big-O beats micro-opts.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
import cProfile
cProfile.run('sum(range(100000))')
```


---

## Security Basics

> **Definition:** No `eval` on user input; validate paths; use HTTPS.

### Why it matters

Dependabot/pip-audit for deps.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
path = user_input  # validate before open
```


---

## Code Review Checklist

> **Definition:** Tests pass, types check, docs updated, no secrets.

### Why it matters

Review for design not just style.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
# PR template checklist
```


---

## Best Practices Summary Table

> **Definition:** See chapter summary table.

### Why it matters

Revisit when starting new repos.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
# team wiki link
```


---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Skipping tests | Regressions ship | pytest on every PR |


---

## Pre-commit Hooks

> **Definition:** Run ruff/black/tests before each commit.

### Why it matters

Catches issues early.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
# .pre-commit-config.yaml hooks
```


---

## Interview Points

Study these before technical interviews. Practice answering out loud in 60–90 seconds.

---

> **📌 Interview Point 1: Zen of Python?**

`import this` — readability counts, explicit > implicit, etc.

---

> **📌 Interview Point 2: PEP 8 highlights?**

snake_case, 4 spaces, imports order, line length ~88 with black.

---

> **📌 Interview Point 3: Type hints benefit?**

Documentation + mypy catch bugs before runtime — gradual typing.

---

> **📌 Interview Point 4: pytest vs unittest?**

pytest: simpler asserts, fixtures; unittest: stdlib xUnit style.

---

> **📌 Interview Point 5: logging vs print?**

Levels, handlers, production filtering — never debug print in prod.

---

> **📌 Interview Point 6: black vs manual format?**

black: opinionated, zero debate — CI enforce.

---

> **📌 Interview Point 7: Secrets management?**

Environment variables, `.env` not committed, secret managers in prod.

---

> **📌 Interview Point 8: Measure before optimize?**

Profile (`cProfile`) — guess wrong often.

---

> **📌 Interview Point 9: Docstring styles?**

Google, NumPy, Sphinx — pick one per project.

---

> **📌 Interview Point 10: Pre-commit hooks?**

Run format/lint/tests before commit — team quality gate.

---

> **📌 Interview Point 11: Dataclass vs dict?**

Typed fields, defaults, immutability option — clearer APIs.

---

> **📌 Interview Point 12: Security: eval/exec?**

Never on untrusted strings — code injection.

---

> **📌 Interview Point 13: Project layout src vs flat?**

`src/package` prevents accidental imports from cwd.

---

> **📌 Interview Point 14: CI for Python?**

matrix Python versions, pip cache, pytest, ruff, mypy.

---

> **📌 Interview Point 15: Code review focus?**

Correctness, tests, readability, security — not bike-shedding style if automated.

---

## Exercises

Try each exercise before opening solutions.

---

Try each exercise before opening the solution. Type the code yourself — muscle memory matters.

---

### Exercise 1: Add type hints ⭐⭐

**Task:** Annotate function sum_two(a: int, b: int) -> int.

<details>
<summary>💡 Hint (click to reveal)</summary>

PEP 484.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
def sum_two(a: int, b: int) -> int:
    return a + b
```

</details>

---

### Exercise 2: pytest sample ⭐⭐

**Task:** Write test asserting 2+2==4.

<details>
<summary>💡 Hint (click to reveal)</summary>

def test_add.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
def add(a, b): return a + b
def test_add():
    assert add(2, 2) == 4
```

</details>


## Chapter Summary

| Concept | Takeaway |
|---------|----------|
| **PEP 8** | Community style standard |
| **pytest** | Simple powerful tests |
| **type hints** | Document types for tools |
| **logging** | Production-ready output |

### Key rules to remember

```text
✅ Read error messages — they name the line and problem
✅ Type examples yourself instead of only reading
✅ Use the REPL for one-line experiments
❌ Do not copy-paste without understanding each line
```

---

## Previous / Next Chapter

**⬅️ [Previous: Virtual Environments and pip](./ch12-virtual-env-pip.md)**

**➡️ [Next: Interview Preparation →](./ch14-interview-prep.md)**

---


*Chapter of the Complete Python Guide | CodeShelf*
