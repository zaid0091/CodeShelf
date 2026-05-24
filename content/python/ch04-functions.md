---
title: Functions
description: Defining functions, parameters, return values, scope, lambdas, recursion, and type hints
order: 4
tags: [python, functions, scope]
---

# Chapter 4: Functions

> **Functions are the primary way to organize logic. Learn parameters, scope, and patterns that scale from scripts to large applications.**
> Take your time with each section — understanding beats speed.

---

## Table of Contents

1. [Why Functions Exist](#why-functions-exist)
2. [Defining and Calling Functions](#defining-and-calling-functions)
3. [Parameters vs Arguments](#parameters-vs-arguments)
4. [Return Values](#return-values)
5. [Default Parameters](#default-parameters)
6. [Keyword Arguments](#keyword-arguments)
7. [Positional-Only and Keyword-Only Parameters](#positional-only-and-keyword-only-parameters)
8. [*args and **kwargs](#args-and-kwargs)
9. [Unpacking at the Call Site](#unpacking-at-the-call-site)
10. [Scope and the LEGB Rule](#scope-and-the-legb-rule)
11. [global and nonlocal](#global-and-nonlocal)
12. [Lambda Functions](#lambda-functions)
13. [Type Hints](#type-hints)
14. [Docstrings and help()](#docstrings-and-help)
15. [First-Class Functions](#first-class-functions)
16. [Recursion](#recursion)
17. [Mutable Default Arguments](#mutable-default-arguments)
18. [Best Practices](#best-practices)
19. [Common Mistakes](#common-mistakes)
20. [Interview Points](#interview-points)
21. [Exercises](#exercises)
22. [Chapter Summary](#chapter-summary)

---

## Why Functions Exist

> **Definition:** This section explains **Why Functions Exist** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **why functions exist** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Why Functions Exist
x = chapter_4_demo = True
print("Why Functions Exist", x)
```

### Hands-on: Why Functions Exist

1. State **Why Functions Exist** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Defining and Calling Functions

> **Definition:** This section explains **Defining and Calling Functions** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **defining and calling functions** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Defining and Calling Functions
x = chapter_4_demo = True
print("Defining and Calling Functions", x)
```

### Hands-on: Defining and Calling Functions

1. State **Defining and Calling Functions** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Parameters vs Arguments

> **Definition:** This section explains **Parameters vs Arguments** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **parameters vs arguments** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Parameters vs Arguments
x = chapter_4_demo = True
print("Parameters vs Arguments", x)
```

### Hands-on: Parameters vs Arguments

1. State **Parameters vs Arguments** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Return Values

> **Definition:** This section explains **Return Values** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **return values** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Return Values
x = chapter_4_demo = True
print("Return Values", x)
```

### Hands-on: Return Values

1. State **Return Values** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Default Parameters

> **Definition:** This section explains **Default Parameters** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **default parameters** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Default Parameters
x = chapter_4_demo = True
print("Default Parameters", x)
```

### Hands-on: Default Parameters

1. State **Default Parameters** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Keyword Arguments

> **Definition:** This section explains **Keyword Arguments** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **keyword arguments** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Keyword Arguments
x = chapter_4_demo = True
print("Keyword Arguments", x)
```

### Hands-on: Keyword Arguments

1. State **Keyword Arguments** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Positional-Only and Keyword-Only Parameters

> **Definition:** This section explains **Positional-Only and Keyword-Only Parameters** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **positional-only and keyword-only parameters** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Positional-Only and Keyword-Only Parameters
x = chapter_4_demo = True
print("Positional-Only and Keyword-Only Parameters", x)
```

### Hands-on: Positional-Only and Keyword-Only Parameters

1. State **Positional-Only and Keyword-Only Parameters** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## *args and **kwargs

> **Definition:** This section explains ***args and **kwargs** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use ***args and **kwargs** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: *args and **kwargs
x = chapter_4_demo = True
print("*args and **kwargs", x)
```

### Hands-on: *args and **kwargs

1. State ***args and **kwargs** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Unpacking at the Call Site

> **Definition:** This section explains **Unpacking at the Call Site** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **unpacking at the call site** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Unpacking at the Call Site
x = chapter_4_demo = True
print("Unpacking at the Call Site", x)
```

### Hands-on: Unpacking at the Call Site

1. State **Unpacking at the Call Site** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Scope and the LEGB Rule

> **Definition:** This section explains **Scope and the LEGB Rule** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **scope and the legb rule** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Scope and the LEGB Rule
x = chapter_4_demo = True
print("Scope and the LEGB Rule", x)
```

### Hands-on: Scope and the LEGB Rule

1. State **Scope and the LEGB Rule** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## global and nonlocal

> **Definition:** This section explains **global and nonlocal** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **global and nonlocal** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: global and nonlocal
x = chapter_4_demo = True
print("global and nonlocal", x)
```

### Hands-on: global and nonlocal

1. State **global and nonlocal** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Lambda Functions

> **Definition:** This section explains **Lambda Functions** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **lambda functions** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Lambda Functions
x = chapter_4_demo = True
print("Lambda Functions", x)
```

### Hands-on: Lambda Functions

1. State **Lambda Functions** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Type Hints

> **Definition:** This section explains **Type Hints** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **type hints** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Type Hints
x = chapter_4_demo = True
print("Type Hints", x)
```

### Hands-on: Type Hints

1. State **Type Hints** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Docstrings and help()

> **Definition:** This section explains **Docstrings and help()** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **docstrings and help()** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Docstrings and help()
x = chapter_4_demo = True
print("Docstrings and help()", x)
```

### Hands-on: Docstrings and help()

1. State **Docstrings and help()** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## First-Class Functions

> **Definition:** This section explains **First-Class Functions** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **first-class functions** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: First-Class Functions
x = chapter_4_demo = True
print("First-Class Functions", x)
```

### Hands-on: First-Class Functions

1. State **First-Class Functions** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Recursion

> **Definition:** This section explains **Recursion** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **recursion** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Recursion
x = chapter_4_demo = True
print("Recursion", x)
```

### Hands-on: Recursion

1. State **Recursion** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Mutable Default Arguments

> **Definition:** This section explains **Mutable Default Arguments** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **mutable default arguments** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Mutable Default Arguments
x = chapter_4_demo = True
print("Mutable Default Arguments", x)
```

### Hands-on: Mutable Default Arguments

1. State **Mutable Default Arguments** in your own words.
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
x = chapter_4_demo = True
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
x = chapter_4_demo = True
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

> **📌 Interview Point 1: What is a function?**

Reusable named block — parameters in, return value out. Defined with `def`.

---

> **📌 Interview Point 2: Parameters vs arguments?**

**Parameters** in definition; **arguments** passed at call site.

---

> **📌 Interview Point 3: What is `*args` and `**kwargs`?**

Collect extra positional (`tuple`) and keyword (`dict`) arguments.

---

> **📌 Interview Point 4: What is LEGB?**

Scope lookup order: **L**ocal, **E**nclosing, **G**lobal, **B**uilt-in.

---

> **📌 Interview Point 5: What is a closure?**

Inner function remembering variables from enclosing scope — used in decorators.

---

> **📌 Interview Point 6: Mutable default argument trap?**

Default `[]` created once — shared across calls. Use `None` and create inside.

---

> **📌 Interview Point 7: What is recursion?**

Function calling itself — needs base case to stop.

---

> **📌 Interview Point 8: Lambda limitations?**

Single expression only — no statements; use `def` for complex logic.

---

> **📌 Interview Point 9: Positional-only vs keyword-only?**

PEP 570 `/` and `*` in signature control how callers may pass args.

---

> **📌 Interview Point 10: What are type hints?**

Optional annotations for static checkers (mypy) — not enforced at runtime.

---

> **📌 Interview Point 11: First-class functions?**

Functions are objects — assign, pass, return like any value.

---

> **📌 Interview Point 12: What does `return` without value?**

Returns `None` — same as falling off end of function.

---

> **📌 Interview Point 13: Docstring convention?**

Triple-quoted string right after `def` — documents purpose, params, returns.

---

> **📌 Interview Point 14: When use `global` / `nonlocal`?**

Rare — prefer return values and parameters. `nonlocal` updates enclosing (non-global) binding.

---

> **📌 Interview Point 15: What is unpacking?**

`a, b = (1, 2)` or `*rest` — at definition and call sites.

---

## Exercises

Try each exercise before opening solutions.

---

Try each exercise before opening the solution. Type the code yourself — muscle memory matters.

---

### Exercise 1: Greet function ⭐

**Task:** Define `greet(name)` returning hello message.

<details>
<summary>💡 Hint (click to reveal)</summary>

def + return f-string.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
def greet(name):
    return f"Hello, {name}!"
```

</details>

---

### Exercise 2: Power function ⭐⭐

**Task:** `power(base, exp=2)` with default exponent.

<details>
<summary>💡 Hint (click to reveal)</summary>

Use default parameter.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
def power(base, exp=2):
    return base ** exp
```

</details>

---

### Exercise 3: Variable args sum ⭐⭐

**Task:** `*args` sum all numbers.

<details>
<summary>💡 Hint (click to reveal)</summary>

Loop or built-in sum.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
def add_all(*args):
    return sum(args)
```

</details>

---

### Exercise 4: LEGB closure ⭐⭐

**Task:** Inner function increments counter in enclosing scope.

<details>
<summary>💡 Hint (click to reveal)</summary>

nonlocal.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc
```

</details>

---

### Exercise 5: Recursive factorial ⭐⭐⭐

**Task:** factorial(n) recursive with base case.

<details>
<summary>💡 Hint (click to reveal)</summary>

n<=1 return 1.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
def factorial(n):
    if n <= 1: return 1
    return n * factorial(n - 1)
```

</details>

---

### Exercise 6: Keyword-only API ⭐⭐⭐

**Task:** Function with `*, name, age`.

<details>
<summary>💡 Hint (click to reveal)</summary>

Call must use keywords after *.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
def create_user(*, name, age):
    return {"name": name, "age": age}
print(create_user(name="A", age=30))
```

</details>


## Chapter Summary

| Concept | Takeaway |
|---------|----------|
| **def** | Reusable named blocks with return |
| **Parameters** | Positional, keyword, defaults, * and ** |
| **Scope** | LEGB lookup order |
| **Closures** | Inner functions capture enclosing names |
| **Type hints** | Optional static checking with mypy |

### Key rules to remember

```text
✅ Read error messages — they name the line and problem
✅ Type examples yourself instead of only reading
✅ Use the REPL for one-line experiments
❌ Do not copy-paste without understanding each line
```

---

## Previous / Next Chapter

**⬅️ [Previous: Control Flow](./ch03-control-flow.md)**

**➡️ [Next: Data Structures →](./ch05-data-structures.md)**

---


*Chapter of the Complete Python Guide | CodeShelf*
