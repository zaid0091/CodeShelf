---
title: Python Basics
description: Installation, syntax, variables, operators, comments, and basic input/output
order: 1
tags: [python, basics, syntax]
---

# Chapter 1: Python Basics

## 1.1 What is Python?

> **Definition:** Python is a high-level, interpreted language whose design emphasizes code readability through significant whitespace (indentation) and a concise syntax.

Python is used for web backends (Django, Flask), data science, automation, scripting, and more. This chapter covers the building blocks every Python program uses.

## 1.2 Installing Python

| Platform | Steps |
|----------|--------|
| Windows | Download from [python.org](https://python.org); check "Add Python to PATH" |
| macOS | `brew install python` or use the official installer |
| Linux | `sudo apt install python3 python3-pip` (Debian/Ubuntu) |

Verify installation:

```bash
python --version
# Python 3.12.0
```

## 1.3 Your first program

```python
print("Hello, World!")
```

`print()` sends output to the console. Parentheses are required in Python 3.

## 1.4 Comments

```python
# This is a single-line comment

"""
This is a multi-line string, often used as a docstring
or block comment at the top of a file.
"""

def greet(name):
    """Return a greeting for name."""  # docstring
    return f"Hello, {name}!"
```

| Style | Use |
|-------|-----|
| `# comment` | Inline or end-of-line notes |
| `"""..."""` | Module/class/function documentation |

## 1.5 Variables and assignment

> **Definition:** A **variable** is a name bound to an object in memory. Python uses dynamic typing — the type is determined at runtime.

```python
name = "Alice"
age = 30
price = 19.99
active = True

# Multiple assignment
x, y, z = 1, 2, 3
a = b = 0  # both bind to same object (use carefully with mutable types)
```

Variable names must start with a letter or underscore; use `snake_case` by convention.

## 1.6 Basic operators

### Arithmetic

```python
10 + 3   # 13
10 - 3   # 7
10 * 3   # 30
10 / 3   # 3.333... (float division)
10 // 3  # 3 (floor division)
10 % 3   # 1 (modulo)
2 ** 10  # 1024 (exponent)
```

### Comparison and logical

```python
5 == 5    # True
5 != 3    # True
5 > 3     # True
5 >= 5    # True

True and False  # False
True or False   # True
not True        # False
```

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not equal |
| `>`, `<`, `>=`, `<=` | Ordering |
| `and`, `or`, `not` | Boolean logic |

## 1.7 Input and output

```python
name = input("Enter your name: ")
print(f"Welcome, {name}!")

# Formatted strings (f-strings)
score = 95
print(f"Score: {score}%")
print("Score: {}%".format(score))
```

> **Definition:** An **f-string** (formatted string literal) embeds expressions inside `{}` and is prefixed with `f` — the preferred formatting style in modern Python.

## 1.8 Indentation and blocks

Python uses indentation (4 spaces standard) instead of braces:

```python
if True:
    print("Indented block")
    print("Same level")
print("Back to outer level")
```

Mixing tabs and spaces causes errors — configure your editor to insert spaces.

## 1.9 The `None` value

```python
result = None  # represents absence of a value

if result is None:
    print("No result yet")
```

Use `is None` / `is not None` for identity checks with `None`.

## 1.10 Common built-in functions

```python
len("hello")        # 5
type(42)            # <class 'int'>
int("42")           # 42
str(42)             # "42"
abs(-5)             # 5
round(3.14159, 2)   # 3.14
min(1, 2, 3)        # 1
max([1, 2, 3])      # 3
sum([1, 2, 3])      # 6
```

## 1.11 Running scripts vs REPL

| Mode | When to use |
|------|-------------|
| REPL (`python`) | Quick experiments, one-liners |
| Script (`.py` file) | Reusable programs, projects |
| IDE debugger | Stepping through complex logic |

```bash
python my_script.py
```

## Exercises

1. Write a program that asks for your name and age, then prints: `Hello, {name}! You are {age} years old.`
2. Calculate the area of a circle with radius `r = 5` using `3.14159 * r ** 2`.
3. Use `//` and `%` to split 17 into quotient and remainder when divided by 5.
4. Experiment with f-strings: include a float formatted to two decimal places.

## Summary

| Concept | Takeaway |
|---------|----------|
| Variables | Names bound to objects; no type declaration |
| Operators | Arithmetic, comparison, logical |
| Indentation | Defines code blocks — 4 spaces |
| I/O | `input()` and `print()` with f-strings |

## Next chapter

Continue to [Data Types](./ch02-data-types.md) for a deep dive into Python's built-in types.
