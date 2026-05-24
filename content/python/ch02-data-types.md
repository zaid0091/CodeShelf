---
title: Data Types
description: Numbers, strings, booleans, type conversion, immutability, truthiness, bytes, and identity
order: 2
tags: [python, types, strings]
---

# Chapter 2: Data Types

> **Every value in Python has a type. This chapter explains built-in types, how to convert between them, and why immutability and truthiness matter every day.**
> Take your time with each section — understanding beats speed.

---

## Table of Contents

1. [Why Data Types Matter](#why-data-types-matter)
2. [Overview of Built-in Types](#overview-of-built-in-types)
3. [type() and isinstance()](#type-and-isinstance)
4. [Integers](#integers)
5. [Floating-Point Numbers](#floating-point-numbers)
6. [Complex Numbers](#complex-numbers)
7. [Strings](#strings)
8. [String Methods Reference](#string-methods-reference)
9. [String Formatting Deep Dive](#string-formatting-deep-dive)
10. [Booleans](#booleans)
11. [Truthiness and Falsiness](#truthiness-and-falsiness)
12. [Type Conversion](#type-conversion)
13. [Immutability Explained](#immutability-explained)
14. [Identity vs Equality](#identity-vs-equality)
15. [The None Type](#the-none-type)
16. [Bytes and Bytearray](#bytes-and-bytearray)
17. [Numeric Special Values](#numeric-special-values)
18. [Best Practices](#best-practices)
19. [Common Mistakes](#common-mistakes)
20. [Interview Points](#interview-points)
21. [Exercises](#exercises)
22. [Chapter Summary](#chapter-summary)

---

## Why Data Types Matter

> **Definition:** Every value has a **type** that determines what operations are valid.

### Why it matters

Adding a string to an integer raises `TypeError`.

### How it works

Check types with `type()` and convert explicitly.

```python
print(type(42), type('42'))
```


---

## Overview of Built-in Types

> **Definition:** Core types include numbers, strings, booleans, sequences, and mappings.

### Why it matters

Choosing the right type models your data correctly.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
sample = [1, 'a', True, {'k': 1}]
print([type(x).__name__ for x in sample]
```


---

## type() and isinstance()

> **Definition:** `type(x)` returns the exact class. `isinstance(x, int)` respects inheritance.

### Why it matters

Prefer `isinstance` for type checks in application code.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
print(isinstance(3, int))
print(isinstance(True, int))  # bool subclasses int
```


---

## Integers

> **Definition:** **int** is arbitrary-precision whole numbers.

### Why it matters

No overflow like fixed-width integers in C.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
big = 10 ** 30
print(big)
```


---

## Floating-Point Numbers

> **Definition:** **float** represents decimals in binary — some values are approximate.

### Why it matters

Use `decimal.Decimal` for money.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
print(0.1 + 0.2)
print(round(0.1 + 0.2, 2)
```


---

## Complex Numbers

> **Definition:** **complex** uses `j` for imaginary unit: `3+4j`.

### Why it matters

Used in science/engineering libraries.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
z = 3 + 4j
print(z.real, z.imag, abs(z))
```


---

## Strings

> **Definition:** **str** is immutable Unicode text in quotes.

### Why it matters

Most user-facing data is strings.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
msg = "Hello"
print(msg.upper(), len(msg))
```


---

## String Methods Reference

> **Definition:** Strings have dozens of methods: `strip`, `split`, `join`, `replace`, etc.

### Why it matters

Methods return new strings — originals never change.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
line = "  a,b,c  "
parts = line.strip().split(",")
print("|".join(parts))
```


---

## String Formatting Deep Dive

> **Definition:** Format with **f-strings**, `.format()`, or `%` (legacy).

### Why it matters

f-strings are fastest to read and write.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
name, score = "Ada", 98
print(f"{name} scored {score}%")
```


---

## Booleans

> **Definition:** **bool** is `True` or `False`, subclass of `int`.

### Why it matters

Drive conditional logic.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
print(bool(0), bool(1), bool(''))
```


---

## Truthiness and Falsiness

> **Definition:** Empty containers and zero are **falsy**; most other values are **truthy**.

### Why it matters

Use `if items:` instead of `if len(items) > 0`.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
values = [[], [0], '0', None]
print([bool(v) for v in values])
```


---

## Type Conversion

> **Definition:** Convert with `int()`, `float()`, `str()`, `list()`, etc.

### Why it matters

Explicit conversion beats implicit surprises.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
n = int('42')
print(n + 8)
```


---

## Immutability Explained

> **Definition:** Immutable objects cannot change in place; operations create new objects.

### Why it matters

Explains why strings/tuples behave differently from lists.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
s = 'hi'
s2 = s + '!'
print(s, s2)
```


---

## Identity vs Equality

> **Definition:** `==` compares values; `is` compares object identity.

### Why it matters

Use `is` for `None` only in most code.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
a = [1,2]
b = [1,2]
print(a == b, a is b)
```


---

## The None Type

> **Definition:** `None` has type `NoneType` — single global instance.

### Why it matters

Represents missing or optional values.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
x = None
print(x is None)
```


---

## Bytes and Bytearray

> **Definition:** `bytes` is immutable binary; `bytearray` is mutable.

### Why it matters

Use at file/network boundaries.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
data = b'hello'
print(data.decode('utf-8'))
```


---

## Numeric Special Values

> **Definition:** Floats include `inf`, `-inf`, and `nan` from the math module.

### Why it matters

Comparisons with `nan` are always False.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
import math
print(math.isnan(float('nan')))
```


---

## Best Practices

### Guidelines

- Prefer `isinstance` over `type() ==`
- Use f-strings
- Never compare floats with `==` for money


---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| `is` for values | Wrong equality semantics | Use `==` except for `None` |


---

## Interview Points

Study these before technical interviews. Practice answering out loud in 60–90 seconds.

---

> **📌 Interview Point 1: Mutable vs immutable types?**

**Immutable:** `int`, `float`, `str`, `tuple`, `frozenset`, `bytes` — cannot change in place. **Mutable:** `list`, `dict`, `set`, `bytearray`.

---

> **📌 Interview Point 2: Why can strings not be changed?**

Immutability enables hashing, interning, and safe sharing. `s += "x"` creates a **new** string object.

---

> **📌 Interview Point 3: What is truthiness?**

`bool(x)` — empty collections, `0`, `None`, `False` are falsy; `[0]` and `"0"` are truthy.

---

> **📌 Interview Point 4: `is` vs `==` for integers?**

Small ints may be **interned** (cached); large ints may be separate objects with equal value. Always use `==` for value comparison.

---

> **📌 Interview Point 5: What is `isinstance` vs `type`?**

`isinstance(x, int)` respects inheritance; `type(x) is int` does not. Prefer `isinstance`.

---

> **📌 Interview Point 6: How do you format strings?**

Prefer **f-strings**; also `.format()` and `%` for legacy code.

---

> **📌 Interview Point 7: What is `None` type?**

Singleton `NoneType` — absence of value. Only one `None` object exists.

---

> **📌 Interview Point 8: str vs bytes?**

`str` is Unicode text; `bytes` is raw binary. Encode/decode at I/O boundaries.

---

> **📌 Interview Point 9: Float precision issues?**

Binary floats cannot represent all decimals exactly — use `decimal.Decimal` for money.

---

> **📌 Interview Point 10: What is slicing?**

`seq[start:stop:step]` — half-open interval; negative indices from end.

---

> **📌 Interview Point 11: What is immutability benefit for dict keys?**

Keys must be **hashable** (immutable types like str, int, tuple of hashables).

---

> **📌 Interview Point 12: What does `int('101', 2)` do?**

Parses base-2 string to integer — `int` accepts optional `base`.

---

> **📌 Interview Point 13: Complex numbers in Python?**

`3+4j` type `complex`; `.real`, `.imag`, `abs()` gives magnitude.

---

> **📌 Interview Point 14: What is `Ellipsis`?**

`...` singleton used in NumPy slicing and type hints — rare in beginner code.

---

> **📌 Interview Point 15: Why use underscore in numeric literals?**

`1_000_000` improves readability; ignored by parser.

---

## Exercises

Try each exercise before opening solutions.

---

Try each exercise before opening the solution. Type the code yourself — muscle memory matters.

---

### Exercise 1: Type inspection ⭐

**Task:** Print `type()` and `isinstance(42, int)` for several values.

<details>
<summary>💡 Hint (click to reveal)</summary>

Use int, str, list, None.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
for v in [42, "hi", [1], None]:
    print(v, type(v), isinstance(v, (int, str)))
```

</details>

---

### Exercise 2: Reverse a string ⭐

**Task:** Reverse `'Python'` using slicing.

<details>
<summary>💡 Hint (click to reveal)</summary>

Slice with step -1: `[::-1]`.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
s = "Python"
print(s[::-1])  # nohtyP
```

</details>

---

### Exercise 3: Truthy report ⭐⭐

**Task:** Print `bool(v)` for six values (three falsy, three truthy).

<details>
<summary>💡 Hint (click to reveal)</summary>

0, '', [], 1, '0', [0].

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
for v in [0, '', [], 1, '0', [0]]:
    print(repr(v), bool(v))
```

</details>

---

### Exercise 4: Safe int conversion ⭐⭐

**Task:** Convert user input; handle invalid with try/except.

<details>
<summary>💡 Hint (click to reveal)</summary>

try/except ValueError.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
raw = input("number: ")
try:
    n = int(raw)
    print(n ** 2)
except ValueError:
    print("not a valid integer")
```

</details>

---

### Exercise 5: Format a receipt ⭐⭐

**Task:** Use f-string with width and thousands separator.

<details>
<summary>💡 Hint (click to reveal)</summary>

`{price:,.2f}`.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
price = 1234.5
print(f"Total: ${price:,.2f}")
```

</details>

---

### Exercise 6: Immutable demo ⭐⭐⭐

**Task:** Show str 'mutation' creates new object.

<details>
<summary>💡 Hint (click to reveal)</summary>

Use `id()` before/after +=.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
s = "hello"
a = id(s)
s += " world"
print(id(s) != a)
```

</details>

---

### Exercise 7: Parse CSV-like line ⭐⭐⭐

**Task:** Split `'a,b,c'` and strip spaces from each part.

<details>
<summary>💡 Hint (click to reveal)</summary>

split + comprehension.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
line = "a, b , c"
parts = [p.strip() for p in line.split(",")]
print(parts)
```

</details>


## Chapter Summary

| Concept | Takeaway |
|---------|----------|
| **Types** | int, float, str, bool, list, dict, set, None |
| **str** | Immutable Unicode text; rich methods |
| **Truthiness** | bool(x) for conditions |
| **Conversion** | int(), float(), str() at boundaries |
| **is vs ==** | Identity vs value equality |
| **Immutability** | Cannot change str/int/tuple in place |

### Key rules to remember

```text
✅ Read error messages — they name the line and problem
✅ Type examples yourself instead of only reading
✅ Use the REPL for one-line experiments
❌ Do not copy-paste without understanding each line
```

---

## Previous / Next Chapter

**⬅️ [Previous: Python Basics](./ch01-python-basics.md)**

**➡️ [Next: Control Flow →](./ch03-control-flow.md)**

---


*Chapter of the Complete Python Guide | CodeShelf*
