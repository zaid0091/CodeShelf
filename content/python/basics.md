---
title: Python Basics
description: Core Python syntax and concepts
order: 1
tags: [basics, fundamentals]
---

# Python Basics

Python is a high-level, interpreted language known for readability and versatility.

## Variables & Types

```python
name = "Alice"          # str
age = 30                # int
price = 19.99           # float
active = True           # bool
items = [1, 2, 3]       # list
coords = (1, 2)         # tuple
user = {"name": "Alice"} # dict
```

## Control Flow

```python
# if/elif/else
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")

# for loop
for item in items:
    print(item)

# while loop
while count > 0:
    count -= 1

# list comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

## Functions

```python
def greet(name: str, greeting: str = "Hello") -> str:
  """Return a greeting message."""
  return f"{greeting}, {name}!"

# *args and **kwargs
def log(*args, **kwargs):
    print(args)    # tuple of positional args
    print(kwargs)  # dict of keyword args
```

## Common Built-ins

```python
len([1, 2, 3])           # 3
range(5)                   # 0, 1, 2, 3, 4
enumerate(["a", "b"])      # (0, "a"), (1, "b")
zip([1, 2], ["a", "b"])   # (1, "a"), (2, "b")
sorted([3, 1, 2])          # [1, 2, 3]
any([False, True])         # True
all([True, True])         # True
```

## File I/O

```python
with open("file.txt", "r") as f:
    content = f.read()

with open("output.txt", "w") as f:
    f.write("Hello, World!")
```
