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

> **Definition:** Python is a **general-purpose, high-level programming language** known for readable syntax. You write `.py` files, run them with an interpreter, and get results quickly — ideal for beginners and experts.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **what is python?** in scripts, APIs, and data tasks.

### Example

```python
# Python reads like pseudocode
names = ["Alice", "Bob", "Carol"]
for name in names:
    print(f"Hello, {name}!")
```

### Hands-on: What is Python?

1. State **What is Python?** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Python vs Other Languages

> **Definition:** This section explains **Python vs Other Languages** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **python vs other languages** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Python vs Other Languages
x = chapter_1_demo = True
print("Python vs Other Languages", x)
```

### Hands-on: Python vs Other Languages

1. State **Python vs Other Languages** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## History of Python

> **Definition:** This section explains **History of Python** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **history of python** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: History of Python
x = chapter_1_demo = True
print("History of Python", x)
```

### Hands-on: History of Python

1. State **History of Python** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Where Python Is Used

> **Definition:** This section explains **Where Python Is Used** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **where python is used** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Where Python Is Used
x = chapter_1_demo = True
print("Where Python Is Used", x)
```

### Hands-on: Where Python Is Used

1. State **Where Python Is Used** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Installing Python

> **Definition:** Install **Python 3** from [python.org](https://www.python.org/downloads/) or your package manager. On Windows, enable **Add Python to PATH** so `python` works in the terminal.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **installing python** in scripts, APIs, and data tasks.

### Example

```bash
python --version
python -m pip --version
```

### Hands-on: Installing Python

1. State **Installing Python** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Running Python Code

> **Definition:** This section explains **Running Python Code** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **running python code** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Running Python Code
x = chapter_1_demo = True
print("Running Python Code", x)
```

### Hands-on: Running Python Code

1. State **Running Python Code** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Your First Python Program

> **Definition:** This section explains **Your First Python Program** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **your first python program** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Your First Python Program
x = chapter_1_demo = True
print("Your First Python Program", x)
```

### Hands-on: Your First Python Program

1. State **Your First Python Program** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Statements and Expressions

> **Definition:** This section explains **Statements and Expressions** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **statements and expressions** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Statements and Expressions
x = chapter_1_demo = True
print("Statements and Expressions", x)
```

### Hands-on: Statements and Expressions

1. State **Statements and Expressions** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Comments in Python

> **Definition:** This section explains **Comments in Python** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **comments in python** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Comments in Python
x = chapter_1_demo = True
print("Comments in Python", x)
```

### Hands-on: Comments in Python

1. State **Comments in Python** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Variables and Assignment

> **Definition:** A **variable** is a name bound to an object. Python is **dynamically typed** — the same name can refer to different types over time.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **variables and assignment** in scripts, APIs, and data tasks.

### Example

```python
count = 0
count += 1
name, age = "Dana", 28
```

### Hands-on: Variables and Assignment

1. State **Variables and Assignment** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Variable Naming Rules

> **Definition:** This section explains **Variable Naming Rules** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **variable naming rules** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Variable Naming Rules
x = chapter_1_demo = True
print("Variable Naming Rules", x)
```

### Hands-on: Variable Naming Rules

1. State **Variable Naming Rules** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Arithmetic Operators

> **Definition:** This section explains **Arithmetic Operators** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **arithmetic operators** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Arithmetic Operators
x = chapter_1_demo = True
print("Arithmetic Operators", x)
```

### Hands-on: Arithmetic Operators

1. State **Arithmetic Operators** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Comparison and Logical Operators

> **Definition:** This section explains **Comparison and Logical Operators** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **comparison and logical operators** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Comparison and Logical Operators
x = chapter_1_demo = True
print("Comparison and Logical Operators", x)
```

### Hands-on: Comparison and Logical Operators

1. State **Comparison and Logical Operators** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Assignment and Identity Operators

> **Definition:** This section explains **Assignment and Identity Operators** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **assignment and identity operators** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Assignment and Identity Operators
x = chapter_1_demo = True
print("Assignment and Identity Operators", x)
```

### Hands-on: Assignment and Identity Operators

1. State **Assignment and Identity Operators** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Input and Output

> **Definition:** This section explains **Input and Output** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **input and output** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Input and Output
x = chapter_1_demo = True
print("Input and Output", x)
```

### Hands-on: Input and Output

1. State **Input and Output** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Indentation and Code Blocks

> **Definition:** This section explains **Indentation and Code Blocks** — a core idea you will use throughout the chapter.

### Real-world analogy

Like traffic **signals** — rules keep many moving parts safe and predictable.

You will use **indentation and code blocks** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Indentation and Code Blocks
x = chapter_1_demo = True
print("Indentation and Code Blocks", x)
```

### Hands-on: Indentation and Code Blocks

1. State **Indentation and Code Blocks** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## The None Value

> **Definition:** This section explains **The None Value** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **the none value** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: The None Value
x = chapter_1_demo = True
print("The None Value", x)
```

### Hands-on: The None Value

1. State **The None Value** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Essential Built-in Functions

> **Definition:** This section explains **Essential Built-in Functions** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **essential built-in functions** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Essential Built-in Functions
x = chapter_1_demo = True
print("Essential Built-in Functions", x)
```

### Hands-on: Essential Built-in Functions

1. State **Essential Built-in Functions** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## PEP 8 and Code Style

> **Definition:** This section explains **PEP 8 and Code Style** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **pep 8 and code style** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: PEP 8 and Code Style
x = chapter_1_demo = True
print("PEP 8 and Code Style", x)
```

### Hands-on: PEP 8 and Code Style

1. State **PEP 8 and Code Style** in your own words.
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
x = chapter_1_demo = True
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
x = chapter_1_demo = True
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
