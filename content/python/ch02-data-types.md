---
title: Data Types
description: Numbers, strings, booleans, type conversion, immutability, and truthiness
order: 2
tags: [python, types, strings]
---

# Chapter 2: Data Types

## 2.1 Overview of built-in types

> **Definition:** A **data type** describes the kind of value an object holds and what operations are valid on it.

| Category | Types | Mutable? |
|----------|-------|----------|
| Numeric | `int`, `float`, `complex` | N/A (immutable) |
| Text | `str` | No |
| Boolean | `bool` | No |
| Sequence | `list`, `tuple`, `range` | list yes; tuple/range no |
| Mapping | `dict` | Yes |
| Set | `set`, `frozenset` | set yes; frozenset no |
| None | `NoneType` | No |

See [Data Structures](./ch05-data-structures.md) for collections in depth.

## 2.2 Numbers

```python
# Integers — arbitrary precision
count = 42
big = 10 ** 100

# Floats — IEEE 754 double precision
pi = 3.14159
scientific = 1.5e-4  # 0.00015

# Complex (rare in everyday code)
z = 3 + 4j
```

| Type | Example | Notes |
|------|---------|-------|
| `int` | `42`, `-7`, `0b1010` | Binary `0b`, octal `0o`, hex `0x` |
| `float` | `3.14`, `2.0`, `1e6` | Avoid `==` for exact equality |
| `complex` | `2+3j` | `.real`, `.imag` attributes |

```python
# Float precision caveat
0.1 + 0.2 == 0.3  # False
round(0.1 + 0.2, 1) == 0.3  # True
```

```python
from decimal import Decimal
Decimal("0.1") + Decimal("0.2") == Decimal("0.3")  # True
```

## 2.3 Strings

> **Definition:** A **string** (`str`) is an immutable sequence of Unicode characters.

```python
single = 'hello'
double = "world"
multi = """Line one
Line two"""

# Indexing and slicing
word = "Python"
word[0]      # 'P'
word[-1]     # 'n'
word[0:3]    # 'Pyt'
word[::-1]   # 'nohtyP' (reverse)
```

### Common string methods

```python
"  hello  ".strip()       # 'hello'
"hello".upper()           # 'HELLO'
"HELLO".lower()           # 'hello'
"a,b,c".split(",")        # ['a', 'b', 'c']
"-".join(["a", "b"])      # 'a-b'
"hello".replace("l", "L") # 'heLLo'
"123".isdigit()           # True
"hello".startswith("he")  # True
```

### String formatting

```python
name, score = "Alice", 95
f"{name} scored {score}%"
"{name} scored {score}%".format(name=name, score=score)
"%s scored %d%%" % (name, score)
```

## 2.4 Booleans

```python
True
False
bool(0)       # False
bool("")      # False
bool("hi")    # True
bool([])      # False
bool([1])     # True
```

> **Definition:** **Truthiness** — in boolean contexts, empty or zero values are falsy; most other values are truthy.

| Falsy values | Truthy examples |
|--------------|-----------------|
| `False`, `None`, `0`, `0.0` | Non-zero numbers |
| `""`, `[]`, `{}`, `set()` | Non-empty collections |
| | Non-empty strings |

## 2.5 Type conversion

```python
int("42")        # 42
float("3.14")    # 3.14
str(42)          # "42"
bool(1)          # True
bool(0)          # False
list("abc")      # ['a', 'b', 'c']
tuple([1, 2])    # (1, 2)
```

Invalid conversions raise `ValueError`:

```python
int("hello")  # ValueError
```

See [Exceptions](./ch10-exceptions.md) for handling errors.

## 2.6 Checking types

```python
type(42)           # <class 'int'>
isinstance(42, int)  # True — preferred over type() ==
isinstance(True, int)  # True — bool is subclass of int
```

Use `isinstance()` for polymorphic checks; avoid comparing `type(x) == int`.

## 2.7 Immutability

```python
s = "hello"
# s[0] = "H"  # TypeError — strings cannot change in place

n = 10
# n += 1 creates a new int object; old 10 may be garbage-collected
```

Immutable types: `int`, `float`, `str`, `tuple`, `frozenset`, `bytes`.

## 2.8 Identity vs equality

```python
a = [1, 2]
b = [1, 2]
a == b   # True  (same values)
a is b   # False (different objects)

x = None
x is None  # preferred check
```

| Operator | Meaning |
|----------|---------|
| `==` | Equal value |
| `is` | Same object in memory |
| `!=`, `is not` | Negations |

## 2.9 `bytes` and `bytearray`

```python
data = b"hello"           # immutable bytes
mutable = bytearray(b"hi")  # mutable
mutable[0] = 72           # b'Hi'
```

Used for binary files, network protocols, and encoding:

```python
" café".encode("utf-8")
b'\xc3\xa9'.decode("utf-8")  # 'é'
```

## Exercises

1. Given `text = "  Python Programming  "`, strip whitespace and convert to title case.
2. Split `"apple,banana,cherry"` into a list; join with `" | "`.
3. Explain why `0.1 + 0.2 != 0.3` and fix with `round()`.
4. Write expressions that demonstrate three falsy and three truthy values.

## Summary

Python's dynamic typing lets variables refer to any type. Master strings, numbers, booleans, conversion, and the difference between `==` and `is`.

## Next chapter

Continue to [Control Flow](./ch03-control-flow.md) for conditionals and loops.
