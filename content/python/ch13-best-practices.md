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

> **Definition:** This section explains **The Zen of Python** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **the zen of python** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: The Zen of Python
x = chapter_13_demo = True
print("The Zen of Python", x)
```

### Hands-on: The Zen of Python

1. State **The Zen of Python** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Readability and Maintainability

> **Definition:** This section explains **Readability and Maintainability** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **readability and maintainability** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Readability and Maintainability
x = chapter_13_demo = True
print("Readability and Maintainability", x)
```

### Hands-on: Readability and Maintainability

1. State **Readability and Maintainability** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## PEP 8 Style Guide

> **Definition:** This section explains **PEP 8 Style Guide** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **pep 8 style guide** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: PEP 8 Style Guide
x = chapter_13_demo = True
print("PEP 8 Style Guide", x)
```

### Hands-on: PEP 8 Style Guide

1. State **PEP 8 Style Guide** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Naming Conventions

> **Definition:** This section explains **Naming Conventions** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **naming conventions** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Naming Conventions
x = chapter_13_demo = True
print("Naming Conventions", x)
```

### Hands-on: Naming Conventions

1. State **Naming Conventions** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Imports and Module Structure

> **Definition:** This section explains **Imports and Module Structure** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **imports and module structure** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Imports and Module Structure
x = chapter_13_demo = True
print("Imports and Module Structure", x)
```

### Hands-on: Imports and Module Structure

1. State **Imports and Module Structure** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Formatting Tools: black and ruff

> **Definition:** This section explains **Formatting Tools: black and ruff** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **formatting tools: black and ruff** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Formatting Tools: black and ruff
x = chapter_13_demo = True
print("Formatting Tools: black and ruff", x)
```

### Hands-on: Formatting Tools: black and ruff

1. State **Formatting Tools: black and ruff** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Type Hints Fundamentals

> **Definition:** This section explains **Type Hints Fundamentals** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **type hints fundamentals** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Type Hints Fundamentals
x = chapter_13_demo = True
print("Type Hints Fundamentals", x)
```

### Hands-on: Type Hints Fundamentals

1. State **Type Hints Fundamentals** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Static Analysis with mypy

> **Definition:** This section explains **Static Analysis with mypy** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **static analysis with mypy** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Static Analysis with mypy
x = chapter_13_demo = True
print("Static Analysis with mypy", x)
```

### Hands-on: Static Analysis with mypy

1. State **Static Analysis with mypy** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Project Layout Patterns

> **Definition:** This section explains **Project Layout Patterns** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **project layout patterns** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Project Layout Patterns
x = chapter_13_demo = True
print("Project Layout Patterns", x)
```

### Hands-on: Project Layout Patterns

1. State **Project Layout Patterns** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Documentation and Docstrings

> **Definition:** This section explains **Documentation and Docstrings** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **documentation and docstrings** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Documentation and Docstrings
x = chapter_13_demo = True
print("Documentation and Docstrings", x)
```

### Hands-on: Documentation and Docstrings

1. State **Documentation and Docstrings** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Testing with pytest

> **Definition:** This section explains **Testing with pytest** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **testing with pytest** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Testing with pytest
x = chapter_13_demo = True
print("Testing with pytest", x)
```

### Hands-on: Testing with pytest

1. State **Testing with pytest** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Fixtures and Test Organization

> **Definition:** This section explains **Fixtures and Test Organization** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **fixtures and test organization** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Fixtures and Test Organization
x = chapter_13_demo = True
print("Fixtures and Test Organization", x)
```

### Hands-on: Fixtures and Test Organization

1. State **Fixtures and Test Organization** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Logging vs print

> **Definition:** This section explains **Logging vs print** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **logging vs print** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Logging vs print
x = chapter_13_demo = True
print("Logging vs print", x)
```

### Hands-on: Logging vs print

1. State **Logging vs print** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Configuration and Secrets

> **Definition:** This section explains **Configuration and Secrets** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **configuration and secrets** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Configuration and Secrets
x = chapter_13_demo = True
print("Configuration and Secrets", x)
```

### Hands-on: Configuration and Secrets

1. State **Configuration and Secrets** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Error Handling Discipline

> **Definition:** This section explains **Error Handling Discipline** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **error handling discipline** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Error Handling Discipline
x = chapter_13_demo = True
print("Error Handling Discipline", x)
```

### Hands-on: Error Handling Discipline

1. State **Error Handling Discipline** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Performance: Measure First

> **Definition:** This section explains **Performance: Measure First** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **performance: measure first** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Performance: Measure First
x = chapter_13_demo = True
print("Performance: Measure First", x)
```

### Hands-on: Performance: Measure First

1. State **Performance: Measure First** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Security Basics

> **Definition:** This section explains **Security Basics** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **security basics** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Security Basics
x = chapter_13_demo = True
print("Security Basics", x)
```

### Hands-on: Security Basics

1. State **Security Basics** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Code Review Checklist

> **Definition:** This section explains **Code Review Checklist** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **code review checklist** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Code Review Checklist
x = chapter_13_demo = True
print("Code Review Checklist", x)
```

### Hands-on: Code Review Checklist

1. State **Code Review Checklist** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Best Practices Summary Table

> **Definition:** This section explains **Best Practices Summary Table** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **best practices summary table** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Best Practices Summary Table
x = chapter_13_demo = True
print("Best Practices Summary Table", x)
```

### Hands-on: Best Practices Summary Table

1. State **Best Practices Summary Table** in your own words.
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
x = chapter_13_demo = True
print("Common Mistakes", x)
```

### Hands-on: Common Mistakes

1. State **Common Mistakes** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Pre-commit Hooks

> **Definition:** This section explains **Pre-commit Hooks** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **pre-commit hooks** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Pre-commit Hooks
x = chapter_13_demo = True
print("Pre-commit Hooks", x)
```

### Hands-on: Pre-commit Hooks

1. State **Pre-commit Hooks** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



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
