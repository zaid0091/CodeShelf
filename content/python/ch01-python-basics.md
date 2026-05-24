---
title: Python Basics
description: What Python is, installation, your first program, variables, operators, indentation, input/output, and how to run code
order: 1
tags: [python, basics, syntax]
---

# Chapter 1: Python Basics

> **Welcome to your first step in learning Python! You will install Python, run code, and learn variables, operators, and how readable syntax makes programming approachable.**
> Take your time with each section — understanding beats speed.

---

## Table of Contents

1. [What is Python?](#what-is-python)
2. [Python vs Other Languages](#python-vs-other-languages)
3. [History of Python](#history-of-python)
4. [Where Python Is Used](#where-python-is-used)
5. [Installing Python](#installing-python)
6. [Running Python Code](#running-python-code)
7. [Your First Python Program](#your-first-python-program)
8. [Statements and Expressions](#statements-and-expressions)
9. [Comments in Python](#comments-in-python)
10. [Variables and Assignment](#variables-and-assignment)
11. [Variable Naming Rules](#variable-naming-rules)
12. [Arithmetic Operators](#arithmetic-operators)
13. [Comparison and Logical Operators](#comparison-and-logical-operators)
14. [Assignment and Identity Operators](#assignment-and-identity-operators)
15. [Input and Output](#input-and-output)
16. [Indentation and Code Blocks](#indentation-and-code-blocks)
17. [The None Value](#the-none-value)
18. [Essential Built-in Functions](#essential-built-in-functions)
19. [PEP 8 and Code Style](#pep-8-and-code-style)
20. [Best Practices](#best-practices)
21. [Common Mistakes](#common-mistakes)
22. [Interview Points](#interview-points)
23. [Exercises](#exercises)
24. [Chapter Summary](#chapter-summary)

---

## What is Python?

> **Definition:** Python is a **high-level, interpreted programming language** focused on readability and productivity.

### Why it matters

You can build web apps, automation, data tools, and scripts without fighting verbose syntax.

### How it works

You write `.py` files, run them with the Python interpreter, and get results quickly.

```python
names = ["Alice", "Bob", "Carol"]
for name in names:
    print(f"Hello, {name}!")
```


---

## Python vs Other Languages

> **Definition:** Python trades some raw speed for **developer speed** — less boilerplate than Java or C++, more structure than shell scripts.

### Why it matters

Choosing a language depends on the problem: Python excels at glue code, APIs, and data work.

### How it works

Compare syntax, typing model, and ecosystem when learning a second language.

```python
# Python: no braces, indentation defines blocks
def greet(name):
    return f"Hi, {name}"

print(greet("Sam"))
```


---

## History of Python

> **Definition:** Python was created by **Guido van Rossum**, first released in 1991, and is now maintained by the Python Software Foundation.

### Why it matters

Knowing the timeline explains Python 2 vs 3 and why modern tutorials target Python 3 only.

### How it works

Major versions add features (f-strings, type hints, pattern matching) while keeping readability.

```python
import sys
print(sys.version)  # shows your interpreter version
```


---

## Where Python Is Used

> **Definition:** Python appears in **web backends**, data science, DevOps automation, education, and scripting.

### Why it matters

One language can support many career paths — fundamentals transfer across domains.

### How it works

Libraries extend the core: Django for web, pandas for data, pytest for testing.

```python
# Tiny automation example
from pathlib import Path
count = sum(1 for _ in Path(".").glob("*.py"))
print(f"Python files here: {count}")
```


---

## Installing Python

> **Definition:** Install **Python 3.10+** from [python.org](https://www.python.org/downloads/) or your OS package manager.

### Why it matters

Without a working interpreter you cannot run examples from this course.

### How it works

Verify install with `python --version` and `python -m pip --version`.

```bash
python --version
python -m pip --version
```


---

## Running Python Code

> **Definition:** Run code in the **REPL** (interactive shell), as a **script** (`.py` file), or from an **IDE**.

### Why it matters

Different modes suit experiments vs repeatable programs.

### How it works

Use the REPL for quick tests; use `.py` files for anything you want to keep or share.

```bash
python                    # REPL
python hello.py           # script
python -c "print(2 + 2)"  # one-liner
```


---

## Your First Python Program

> **Definition:** A minimal program uses `print()` to show output.

### Why it matters

Success here proves your environment works.

### How it works

Save code in `hello.py` and run `python hello.py` from the terminal.

```python
print("Hello, Python!")
```


---

## Statements and Expressions

> **Definition:** An **expression** produces a value (`2 + 2`). A **statement** performs an action (`x = 5`, `if`, `for`).

### Why it matters

Every useful program mixes both.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
x = 10          # statement (assignment)
y = x * 2       # expression on right side
print(y)        # statement calling print
```


---

## Comments in Python

> **Definition:** Comments start with `#` and are ignored by the interpreter. **Docstrings** document modules and functions.

### Why it matters

Comments explain *why*, not *what* obvious code already shows.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
# tax rate for the current year
RATE = 0.08

def total(price):
    '''Return price with tax.'''
    return price * (1 + RATE)
```


---

## Variables and Assignment

> **Definition:** A **variable** is a name bound to an object. Python is **dynamically typed**.

### Why it matters

Names make code readable and let you reuse values.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
count = 0
count += 1
name, age = "Dana", 28
```


---

## Variable Naming Rules

> **Definition:** Names use letters, digits, and underscores; cannot start with a digit. Follow **snake_case** (PEP 8).

### Why it matters

Good names reduce bugs and help teammates understand code.

### How it works

```python
user_count = 3      # good
# 2fast = True      # SyntaxError
class = "A"         # SyntaxError — reserved word
```

Avoid single-letter names except loop counters (`i`, `j`).


---

## Arithmetic Operators

> **Definition:** Python supports `+`, `-`, `*`, `/`, `//`, `%`, and `**` (power).

### Why it matters

Math operators underpin calculations in every program.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
print(10 / 3)   # 3.333... true division
print(10 // 3)  # 3 floor division
print(10 % 3)   # 1 remainder
print(2 ** 10)  # 1024
```


---

## Comparison and Logical Operators

> **Definition:** Comparisons (`==`, `!=`, `<`, `>`) return `bool`. Combine with `and`, `or`, `not`.

### Why it matters

Conditions drive `if` statements and loops.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
age = 20
can_vote = age >= 18
has_id = True
if can_vote and has_id:
    print("Eligible")
```


---

## Assignment and Identity Operators

> **Definition:** **Augmented assignment** (`+=`, `-=`) updates in place. **`is`** tests object identity; **`==`** tests value equality.

### Why it matters

Use `is` only for `None` and small singleton cases; otherwise prefer `==`.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
score = 10
score += 5
x = None
if x is None:
    print("no value yet")
```


---

## Input and Output

> **Definition:** `input()` reads a line of text from the user. `print()` writes to the console.

### Why it matters

Interactive programs need both.

### How it works

```python
name = input("Your name: ").strip()
print(f"Welcome, {name}!")
```

Always `.strip()` user input unless whitespace matters.


---

## Indentation and Code Blocks

> **Definition:** Python uses **indentation** (4 spaces) instead of braces to define blocks.

### Why it matters

Consistent indentation is required — mixing tabs and spaces causes errors.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
if True:
    print("inside block")
    print("still inside")
print("outside")
```


---

## The None Value

> **Definition:** `None` is a singleton meaning **no value** or **not set yet**.

### Why it matters

Functions without `return` give `None`. APIs use `None` for missing data.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
result = None

def find_user(id):
  return None  # not found

if result is None:
    print("empty")
```


---

## Essential Built-in Functions

> **Definition:** Built-ins like `len`, `type`, `int`, `str`, `sum`, and `max` are always available.

### Why it matters

They cover common tasks without imports.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
print(len("hello"))
print(type(42))
print(sum([1, 2, 3]))
print(max(3, 9, 2))
```


---

## PEP 8 and Code Style

> **Definition:** **PEP 8** is the official Python style guide: naming, spacing, imports, and line length.

### Why it matters

Consistent style makes team code reviews faster.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
# PEP 8: spaces around operators, blank lines between functions

def add(a, b):
    return a + b
```


---

## Best Practices

### Guidelines

- Use `snake_case` for variables and functions.
- Prefer f-strings for formatting.
- Run `python -m pip install` only inside a virtual environment for projects.
- Read tracebacks from the bottom line upward.


---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Using `=` instead of `==` in conditions | Assigns instead of comparing | Use `==` for equality |
| Forgetting `input()` returns str | Math on strings fails or behaves oddly | Cast with `int()` / `float()` |
| Tabs vs spaces | IndentationError | Configure editor to insert 4 spaces |


---

## Interview Points

Study these before technical interviews. Practice answering out loud in 60–90 seconds.

---

> **📌 Interview Point 1: Is Python compiled or interpreted?**

**Answer framework:** CPython compiles source to **bytecode**, then interprets it. Colloquially *interpreted*; PyPy adds JIT.

---

> **📌 Interview Point 2: What is dynamic typing?**

Names bind to objects with types on objects. Rebinding `x` from `int` to `str` is legal.

---

> **📌 Interview Point 3: Difference between `/` and `//`?**

`/` true division (float). `//` floor division.

---

> **📌 Interview Point 4: What does `None` mean?**

Singleton *no value*. Prefer `if x is None`.

---

> **📌 Interview Point 5: Why indentation for blocks?**

Forces readable structure — PEP 8: 4 spaces per level.

---

> **📌 Interview Point 6: What is PEP 8?**

Official style guide; tools like black/ruff enforce it.

---

> **📌 Interview Point 7: What is an f-string?**

`f"{expr}"` — preferred string formatting.

---

> **📌 Interview Point 8: Statement vs expression?**

Expressions have values; statements perform actions (`if`, `for`).

---

> **📌 Interview Point 9: Python 2 vs 3?**

Use Python 3 only — Python 2 is EOL.

---

> **📌 Interview Point 10: What is `is` vs `==`?**

`==` value equality; `is` identity — use `is` for `None`.

---

> **📌 Interview Point 11: Why convert `input()`?**

`input()` returns str — use `int()`/`float()` for math.

---

> **📌 Interview Point 12: Mutable default assignment risk?**

`a = b = []` shares one list — use separate literals.

---

## Exercises

Try each exercise before opening solutions.

---

Try each exercise before opening the solution. Type the code yourself — muscle memory matters.

---

### Exercise 1: Greeting program ⭐

**Task:** Ask for name and age; print `Hello, {name}! You are {age} years old.`

<details>
<summary>💡 Hint (click to reveal)</summary>

Use `input()` twice, `int()` for age, f-string for output.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello, {name}! You are {age} years old.")
```

</details>

---

### Exercise 2: Circle area ⭐

**Task:** Compute area for `r = 5` with `PI = 3.14159`, print two decimals.

<details>
<summary>💡 Hint (click to reveal)</summary>

Use `area = PI * r ** 2` and `f"{area:.2f}"`.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
PI = 3.14159
r = 5
area = PI * r ** 2
print(f"Area: {area:.2f}")
```

</details>

---

### Exercise 3: Quotient and remainder ⭐

**Task:** Split 17 by 5 using `//` and `%`.

<details>
<summary>💡 Hint (click to reveal)</summary>

`17 // 5` is 3, `17 % 5` is 2.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
n, d = 17, 5
print(f"quotient={n//d}, remainder={n%d}")
```

</details>

---

### Exercise 4: Temperature converter ⭐⭐

**Task:** Read Celsius, print Fahrenheit `F = C * 9/5 + 32`.

<details>
<summary>💡 Hint (click to reveal)</summary>

Use `float(input(...))` for decimals.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
c = float(input("Celsius: "))
f = c * 9 / 5 + 32
print(f"{c}°C = {f:.1f}°F")
```

</details>

---

### Exercise 5: Swap variables ⭐⭐

**Task:** Swap `a=10`, `b=20` without temp variable.

<details>
<summary>💡 Hint (click to reveal)</summary>

Tuple unpacking: `a, b = b, a`.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
a, b = 10, 20
a, b = b, a
print(a, b)  # 20 10
```

</details>

---

### Exercise 6: Truthiness lab ⭐⭐

**Task:** Print `bool()` for three falsy and three truthy values.

<details>
<summary>💡 Hint (click to reveal)</summary>

Falsy: `0`, `""`, `[]`. Truthy: `1`, `"hi"`, `[0]`.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
for v in [0, "", [], 1, "hi", [0]]:
    print(repr(v), "->", bool(v))
```

</details>

---

### Exercise 7: Mini calculator ⭐⭐⭐

**Task:** Two numbers + operator `+ - * /`; print result.

<details>
<summary>💡 Hint (click to reveal)</summary>

Use `if/elif` on operator string; `float` inputs.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
a = float(input("a: "))
b = float(input("b: "))
op = input("op (+,-,*,/): ")
if op == "+": print(a + b)
elif op == "-": print(a - b)
elif op == "*": print(a * b)
elif op == "/": print(a / b if b else "cannot divide by zero")
else: print("unknown op")
```

</details>


## Chapter Summary

| Concept | Takeaway |
|---------|----------|
| **Python** | Readable high-level language for many domains |
| **Install & run** | python --version, REPL, .py scripts |
| **Variables** | Names bound to objects; dynamic typing |
| **Operators** | Math, comparison, logic, augmented assignment |
| **I/O** | input() returns str; print() and f-strings |
| **Indentation** | 4 spaces define blocks |
| **None** | Absence of value; test with is None |
| **PEP 8** | snake_case and consistent style |

### Key rules to remember

```text
✅ Read error messages — they name the line and problem
✅ Type examples yourself instead of only reading
✅ Use the REPL for one-line experiments
❌ Do not copy-paste without understanding each line
```

---

## Previous / Next Chapter

**➡️ [Next: Data Types →](./ch02-data-types.md)**

---


*Chapter of the Complete Python Guide | CodeShelf*
