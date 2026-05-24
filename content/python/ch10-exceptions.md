---
title: Exceptions
description: try/except, raising, custom exceptions, EAFP, and context managers
order: 10
tags: [python, exceptions, errors]
---

# Chapter 10: Exceptions

> **Errors happen. Exceptions let programs recover gracefully instead of crashing silently or confusing users.**
> Take your time with each section — understanding beats speed.

---

## Table of Contents

1. [Errors vs Exceptions](#errors-vs-exceptions)
2. [How Exceptions Propagate](#how-exceptions-propagate)
3. [try / except Basics](#try-except-basics)
4. [else and finally Clauses](#else-and-finally-clauses)
5. [Catching Multiple Exceptions](#catching-multiple-exceptions)
6. [Exception Objects and as](#exception-objects-and-as)
7. [Raising Exceptions](#raising-exceptions)
8. [Custom Exception Classes](#custom-exception-classes)
9. [The Exception Hierarchy](#the-exception-hierarchy)
10. [Re-raising and Exception Chaining](#re-raising-and-exception-chaining)
11. [Assertions](#assertions)
12. [EAFP vs LBYL](#eafp-vs-lbyl)
13. [Context Managers](#context-managers)
14. [contextlib Utilities](#contextlib-utilities)
15. [Exceptions in Real Applications](#exceptions-in-real-applications)
16. [Best Practices](#best-practices)
17. [Common Mistakes](#common-mistakes)
18. [Reading Tracebacks](#reading-tracebacks)
19. [Exception Handling in APIs](#exception-handling-in-apis)
20. [Logging Exceptions](#logging-exceptions)
21. [Interview Points](#interview-points)
22. [Exercises](#exercises)
23. [Chapter Summary](#chapter-summary)

---

## Errors vs Exceptions

> **Definition:** This section explains **Errors vs Exceptions** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **errors vs exceptions** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Errors vs Exceptions
x = chapter_10_demo = True
print("Errors vs Exceptions", x)
```

### Hands-on: Errors vs Exceptions

1. State **Errors vs Exceptions** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## How Exceptions Propagate

> **Definition:** This section explains **How Exceptions Propagate** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **how exceptions propagate** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: How Exceptions Propagate
x = chapter_10_demo = True
print("How Exceptions Propagate", x)
```

### Hands-on: How Exceptions Propagate

1. State **How Exceptions Propagate** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## try / except Basics

> **Definition:** Wrap risky code in `try` and handle expected failures in `except` so users see helpful messages instead of crashes.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **try / except basics** in scripts, APIs, and data tasks.

### Example

```python
try:
    value = int(input("Number: "))
except ValueError:
    print("Please enter digits only.")
```

### Hands-on: try / except Basics

1. State **try / except Basics** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## else and finally Clauses

> **Definition:** This section explains **else and finally Clauses** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **else and finally clauses** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: else and finally Clauses
x = chapter_10_demo = True
print("else and finally Clauses", x)
```

### Hands-on: else and finally Clauses

1. State **else and finally Clauses** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Catching Multiple Exceptions

> **Definition:** This section explains **Catching Multiple Exceptions** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **catching multiple exceptions** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Catching Multiple Exceptions
x = chapter_10_demo = True
print("Catching Multiple Exceptions", x)
```

### Hands-on: Catching Multiple Exceptions

1. State **Catching Multiple Exceptions** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Exception Objects and as

> **Definition:** This section explains **Exception Objects and as** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **exception objects and as** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Exception Objects and as
x = chapter_10_demo = True
print("Exception Objects and as", x)
```

### Hands-on: Exception Objects and as

1. State **Exception Objects and as** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Raising Exceptions

> **Definition:** This section explains **Raising Exceptions** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **raising exceptions** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Raising Exceptions
x = chapter_10_demo = True
print("Raising Exceptions", x)
```

### Hands-on: Raising Exceptions

1. State **Raising Exceptions** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Custom Exception Classes

> **Definition:** This section explains **Custom Exception Classes** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **custom exception classes** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Custom Exception Classes
x = chapter_10_demo = True
print("Custom Exception Classes", x)
```

### Hands-on: Custom Exception Classes

1. State **Custom Exception Classes** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## The Exception Hierarchy

> **Definition:** This section explains **The Exception Hierarchy** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **the exception hierarchy** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: The Exception Hierarchy
x = chapter_10_demo = True
print("The Exception Hierarchy", x)
```

### Hands-on: The Exception Hierarchy

1. State **The Exception Hierarchy** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Re-raising and Exception Chaining

> **Definition:** This section explains **Re-raising and Exception Chaining** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **re-raising and exception chaining** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Re-raising and Exception Chaining
x = chapter_10_demo = True
print("Re-raising and Exception Chaining", x)
```

### Hands-on: Re-raising and Exception Chaining

1. State **Re-raising and Exception Chaining** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Assertions

> **Definition:** This section explains **Assertions** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **assertions** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Assertions
x = chapter_10_demo = True
print("Assertions", x)
```

### Hands-on: Assertions

1. State **Assertions** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## EAFP vs LBYL

> **Definition:** This section explains **EAFP vs LBYL** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **eafp vs lbyl** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: EAFP vs LBYL
x = chapter_10_demo = True
print("EAFP vs LBYL", x)
```

### Hands-on: EAFP vs LBYL

1. State **EAFP vs LBYL** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Context Managers

> **Definition:** This section explains **Context Managers** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **context managers** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Context Managers
x = chapter_10_demo = True
print("Context Managers", x)
```

### Hands-on: Context Managers

1. State **Context Managers** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## contextlib Utilities

> **Definition:** This section explains **contextlib Utilities** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **contextlib utilities** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: contextlib Utilities
x = chapter_10_demo = True
print("contextlib Utilities", x)
```

### Hands-on: contextlib Utilities

1. State **contextlib Utilities** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Exceptions in Real Applications

> **Definition:** This section explains **Exceptions in Real Applications** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **exceptions in real applications** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Exceptions in Real Applications
x = chapter_10_demo = True
print("Exceptions in Real Applications", x)
```

### Hands-on: Exceptions in Real Applications

1. State **Exceptions in Real Applications** in your own words.
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
x = chapter_10_demo = True
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
x = chapter_10_demo = True
print("Common Mistakes", x)
```

### Hands-on: Common Mistakes

1. State **Common Mistakes** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Reading Tracebacks

> **Definition:** This section explains **Reading Tracebacks** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **reading tracebacks** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Reading Tracebacks
x = chapter_10_demo = True
print("Reading Tracebacks", x)
```

### Hands-on: Reading Tracebacks

1. State **Reading Tracebacks** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Exception Handling in APIs

> **Definition:** This section explains **Exception Handling in APIs** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **exception handling in apis** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Exception Handling in APIs
x = chapter_10_demo = True
print("Exception Handling in APIs", x)
```

### Hands-on: Exception Handling in APIs

1. State **Exception Handling in APIs** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Logging Exceptions

> **Definition:** This section explains **Logging Exceptions** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **logging exceptions** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Logging Exceptions
x = chapter_10_demo = True
print("Logging Exceptions", x)
```

### Hands-on: Logging Exceptions

1. State **Logging Exceptions** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Interview Points

Study these before technical interviews. Practice answering out loud in 60–90 seconds.

---

> **📌 Interview Point 1: Exception vs syntax error?**

Syntax: parse time. Exception: runtime after valid syntax.

---

> **📌 Interview Point 2: try/except/else/finally order?**

`try` body; `except` on match; `else` if no exception; `finally` always runs.

---

> **📌 Interview Point 3: Bare `except`?**

Catches everything including `KeyboardInterrupt` — avoid; catch specific types.

---

> **📌 Interview Point 4: EAFP vs LBYL?**

**Easier to Ask Forgiveness** (try) vs **Look Before You Leap** (if checks) — Pythonic EAFP.

---

> **📌 Interview Point 5: Custom exception when?**

Domain errors users can catch — inherit from `Exception`, not `BaseException`.

---

> **📌 Interview Point 6: Re-raise with `raise`?**

Preserves traceback; `raise New from old` chains context.

---

> **📌 Interview Point 7: Assertion vs exception?**

`assert` for developer bugs — disabled with `-O`; use exceptions for user errors.

---

> **📌 Interview Point 8: Context manager protocol?**

`__enter__`/`__exit__` or `@contextmanager` with yield.

---

> **📌 Interview Point 9: Exception hierarchy?**

Catch specific before general; `Exception` catches most, not `SystemExit`.

---

> **📌 Interview Point 10: finally vs else?**

`else` only if no exception; `finally` always (cleanup).

---

> **📌 Interview Point 11: What is BaseException?**

Root — includes `SystemExit`, `KeyboardInterrupt` — rarely catch directly.

---

> **📌 Interview Point 12: ValueError vs TypeError?**

Right type wrong value vs wrong type entirely.

---

> **📌 Interview Point 13: Logging exceptions?**

`logging.exception()` in except block includes traceback.

---

> **📌 Interview Point 14: Exception groups 3.11+?**

`except*` handles ExceptionGroup from parallel tasks.

---

> **📌 Interview Point 15: When not to catch?**

Let bugs propagate in dev; catch at boundaries in production with logging.

---

## Exercises

Try each exercise before opening solutions.

---

Try each exercise before opening the solution. Type the code yourself — muscle memory matters.

---

### Exercise 1: Divide safe ⭐

**Task:** try/except ZeroDivisionError.

<details>
<summary>💡 Hint (click to reveal)</summary>

except specific type.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
```

</details>

---

### Exercise 2: Custom error ⭐⭐

**Task:** Raise ValueError for negative age.

<details>
<summary>💡 Hint (click to reveal)</summary>

if age < 0: raise.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
```

</details>


## Extended Study Appendix (Chapter 10)

> Spaced repetition section — revisit after 24 hours and again after one week.

### Review drill 1

**Concept check 1:** Explain one idea from this chapter without looking at notes.

```python
# Practice snippet 1 — type and run
values = list(range(1, 1 + 5))
print([v * 2 for v in values if v % 2 == 0])
```

**Interview mini-prompt:** How would you teach this concept to a junior developer in two minutes?

**Real-world link:** Where would this appear in a web API, data script, or automation task?




### Official documentation

Bookmark [docs.python.org/3/](https://docs.python.org/3/) — the tutorial and library reference are authoritative.




---

## Chapter Summary

| Concept | Takeaway |
|---------|----------|
| **try/except** | Handle expected failures |
| **finally** | Always-run cleanup |
| **raise** | Signal errors with types |
| **EAFP** | Try first — Pythonic style |

### Key rules to remember

```text
✅ Read error messages — they name the line and problem
✅ Type examples yourself instead of only reading
✅ Use the REPL for one-line experiments
❌ Do not copy-paste without understanding each line
```

---

## Previous / Next Chapter

**⬅️ [Previous: File I/O](./ch09-file-io.md)**

**➡️ [Next: Decorators and Generators →](./ch11-decorators-generators.md)**

---


*Chapter of the Complete Python Guide | CodeShelf*
