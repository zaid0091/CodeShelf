---
title: Object-Oriented Programming
description: Classes, objects, inheritance, properties, dataclasses, dunder methods, and MRO
order: 7
tags: [python, oop, classes]
---

# Chapter 7: Object-Oriented Programming

> **Object-oriented programming models data and behavior together. Learn when classes help — and when simple functions are enough.**
> Take your time with each section — understanding beats speed.

---

## Table of Contents

1. [What Is OOP?](#what-is-oop)
2. [When to Use Classes in Python](#when-to-use-classes-in-python)
3. [Classes and Objects](#classes-and-objects)
4. [The __init__ Constructor and self](#the-init-constructor-and-self)
5. [Instance vs Class Attributes](#instance-vs-class-attributes)
6. [Instance Methods](#instance-methods)
7. [Inheritance](#inheritance)
8. [super() and Method Overriding](#super-and-method-overriding)
9. [Method Types: instance, class, static](#method-types-instance-class-static)
10. [Encapsulation and Properties](#encapsulation-and-properties)
11. [Dataclasses](#dataclasses)
12. [Magic (Dunder) Methods](#magic-dunder-methods)
13. [Abstract Base Classes](#abstract-base-classes)
14. [Composition vs Inheritance](#composition-vs-inheritance)
15. [Multiple Inheritance and MRO](#multiple-inheritance-and-mro)
16. [Best Practices](#best-practices)
17. [Common Mistakes](#common-mistakes)
18. [OOP Design Checklist](#oop-design-checklist)
19. [Interview Points](#interview-points)
20. [Exercises](#exercises)
21. [Chapter Summary](#chapter-summary)

---

## What Is OOP?

> **Definition:** **Object-oriented programming** bundles data and behavior in **objects**.

### Why it matters

Models real entities (User, Order, Cart).

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
class Dog:
    def speak(self):
        return 'woof'
```


---

## When to Use Classes in Python

> **Definition:** Use classes when you have state + behavior together; otherwise functions may suffice.

### Why it matters

Dataclasses help data-only objects.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
# simple data -> dataclass later in chapter
```


---

## Classes and Objects

> **Definition:** A **class** is a blueprint; an **object** is an instance.

### Why it matters

Call `ClassName()` to construct.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
p = Point(1,2)
```


---

## The __init__ Constructor and self

> **Definition:** `__init__` initializes instance attributes; `self` is the instance.

### Why it matters

Every method receives `self` first.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
class User:
    def __init__(self, name):
        self.name = name
```


---

## Instance vs Class Attributes

> **Definition:** Instance attrs on `self`; class attrs shared by all instances.

### Why it matters

Mutable class attrs are shared — beware.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
class Config:
    debug = False
```


---

## Instance Methods

> **Definition:** Functions on the class taking `self`.

### Why it matters

Define behavior that uses instance state.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
class Counter:
    def __init__(self):
        self.n = 0
    def inc(self):
        self.n += 1
```


---

## Inheritance

> **Definition:** Subclass extends superclass with `class Child(Parent):`.

### Why it matters

Reuse and specialize behavior.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
class Animal:
    def speak(self):
        return '...'
class Dog(Animal):
    def speak(self):
        return 'bark'
```


---

## super() and Method Overriding

> **Definition:** `super()` calls parent implementation.

### Why it matters

Override methods to customize; call `super()` to extend.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
class B(A):
    def greet(self):
        return super().greet() + '!'
```


---

## Method Types: instance, class, static

> **Definition:** `@classmethod` gets `cls`; `@staticmethod` no implicit first arg.

### Why it matters

Class methods for factories; static for utilities.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
class Math:
    @staticmethod
    def add(a,b):
        return a+b
```


---

## Encapsulation and Properties

> **Definition:** Use `@property` for computed or validated attributes.

### Why it matters

Public API without exposing raw fields.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
class Circle:
    def __init__(self, r):
        self._r = r
    @property
    def area(self):
        return 3.14 * self._r ** 2
```


---

## Dataclasses

> **Definition:** `@dataclass` auto-generates `__init__`, `__repr__`, etc.

### Why it matters

Less boilerplate for data containers.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
from dataclasses import dataclass
@dataclass
class User:
    name: str
    active: bool = True
```


---

## Magic (Dunder) Methods

> **Definition:** Double-underscore methods customize operators and builtins.

### Why it matters

`__str__`, `__len__`, `__eq__` are common.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
class Vec:
    def __init__(self, x,y):
        self.x, self.y = x,y
    def __repr__(self):
        return f'Vec({self.x},{self.y})'
```


---

## Abstract Base Classes

> **Definition:** `abc.ABC` enforces subclasses implement methods.

### Why it matters

Define interfaces in larger systems.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
from abc import ABC, abstractmethod
class Repo(ABC):
    @abstractmethod
    def get(self, id): ...
```


---

## Composition vs Inheritance

> **Definition:** **Composition** builds objects from other objects; **inheritance** is-is-a.

### Why it matters

Favor composition when reuse is has-a.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
class Engine: ...
class Car:
    def __init__(self):
        self.engine = Engine()
```


---

## Multiple Inheritance and MRO

> **Definition:** Python supports multiple bases; **MRO** orders lookup.

### Why it matters

Keep hierarchies shallow; use mixins carefully.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
class A: pass
class B(A): pass
print(B.__mro__)
```


---

## Best Practices

### Guidelines

- Prefer composition over deep inheritance
- Use dataclasses for plain data


---

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| God object class | Hard to test | Split responsibilities |


---

## OOP Design Checklist

> **Definition:** Ask: one responsibility? clear names? minimal public surface?

### Why it matters

Refactor when classes grow past ~200 lines.

### How it works

Read the example, run it in a REPL or script, then change one value and predict the output before you execute.

```python
# sketch classes on paper before coding
```


---

## Interview Points

Study these before technical interviews. Practice answering out loud in 60–90 seconds.

---

> **📌 Interview Point 1: What is OOP?**

Modeling with **classes** (blueprints) and **objects** (instances) — data + behavior.

---

> **📌 Interview Point 2: `__init__` vs `__new__`?**

`__new__` creates instance; `__init__` initializes it. Rarely override `__new__`.

---

> **📌 Interview Point 3: Instance vs class attributes?**

Instance on `self`; class on class object — shared unless shadowed.

---

> **📌 Interview Point 4: Inheritance vs composition?**

**has-a** (compose objects) often beats **is-a** (deep trees) for flexibility.

---

> **📌 Interview Point 5: What is MRO?**

Method Resolution Order — C3 linearization for multiple inheritance.

---

> **📌 Interview Point 6: `@property` purpose?**

Computed attributes with getter/setter validation — Pythonic encapsulation.

---

> **📌 Interview Point 7: Dataclass when?**

Boilerplate data containers — auto `__init__`, `__repr__`, optional ordering.

---

> **📌 Interview Point 8: Dunder methods?**

`__str__`, `__repr__`, `__eq__`, `__len__` — hook into built-ins.

---

> **📌 Interview Point 9: Abstract base class?**

`abc.ABC` forces subclasses to implement interface methods.

---

> **📌 Interview Point 10: `staticmethod` vs `classmethod`?**

staticmethod: no `self`; classmethod: receives class, used for factories.

---

> **📌 Interview Point 11: What is encapsulation in Python?**

Convention `_protected`, `__mangled` — not true private like Java.

---

> **📌 Interview Point 12: Multiple inheritance pitfalls?**

Diamond problem — know MRO; favor mixins with single responsibility.

---

> **📌 Interview Point 13: `super()` behavior?**

Calls next class in MRO — cooperative multiple inheritance.

---

> **📌 Interview Point 14: Magic method for context manager?**

`__enter__` / `__exit__` — or `@contextmanager` generator.

---

> **📌 Interview Point 15: When not to use classes?**

Simple scripts, pure functions suffice — avoid over-OOP.

---

## Exercises

Try each exercise before opening solutions.

---

Try each exercise before opening the solution. Type the code yourself — muscle memory matters.

---

### Exercise 1: Dog class ⭐

**Task:** Class Dog with name and speak method.

<details>
<summary>💡 Hint (click to reveal)</summary>

__init__ and method.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} says woof"
```

</details>

---

### Exercise 2: Rectangle area ⭐⭐

**Task:** Rectangle with width, height, area property.

<details>
<summary>💡 Hint (click to reveal)</summary>

@property for area.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
class Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h
    @property
    def area(self):
        return self.w * self.h
```

</details>

---

### Exercise 3: Inheritance ⭐⭐

**Task:** Employee and Manager with bonus pay.

<details>
<summary>💡 Hint (click to reveal)</summary>

super().__init__.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
class Employee:
    def __init__(self, name, salary):
        self.name, self.salary = name, salary
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
```

</details>

---

### Exercise 4: Dataclass Point ⭐⭐⭐

**Task:** Use @dataclass for Point x,y.

<details>
<summary>💡 Hint (click to reveal)</summary>

from dataclasses import dataclass.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
from dataclasses import dataclass
@dataclass
class Point:
    x: float
    y: float
```

</details>

---

### Exercise 5: __repr__ ⭐⭐⭐

**Task:** Class with readable __repr__.

<details>
<summary>💡 Hint (click to reveal)</summary>

f-string in dunder.

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

```python
class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"User(name={self.name!r})"
```

</details>


## Chapter Summary

| Concept | Takeaway |
|---------|----------|
| **class** | Blueprint; object is instance |
| **self** | Reference to current instance |
| **inheritance** | Reuse and extend behavior |
| **@property** | Controlled attribute access |
| **dataclass** | Boilerplate for data containers |

### Key rules to remember

```text
✅ Read error messages — they name the line and problem
✅ Type examples yourself instead of only reading
✅ Use the REPL for one-line experiments
❌ Do not copy-paste without understanding each line
```

---

## Previous / Next Chapter

**⬅️ [Previous: Comprehensions](./ch06-comprehensions.md)**

**➡️ [Next: Modules and Packages →](./ch08-modules-packages.md)**

---


*Chapter of the Complete Python Guide | CodeShelf*
