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

> **Definition:** This section explains **What Is OOP?** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **what is oop?** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: What Is OOP?
x = chapter_7_demo = True
print("What Is OOP?", x)
```

### Hands-on: What Is OOP?

1. State **What Is OOP?** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## When to Use Classes in Python

> **Definition:** This section explains **When to Use Classes in Python** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **when to use classes in python** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: When to Use Classes in Python
x = chapter_7_demo = True
print("When to Use Classes in Python", x)
```

### Hands-on: When to Use Classes in Python

1. State **When to Use Classes in Python** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Classes and Objects

> **Definition:** This section explains **Classes and Objects** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **classes and objects** in scripts, APIs, and data tasks.

### Example

```python
class Greeter:
    def __init__(self, prefix):
        self.prefix = prefix
    def greet(self, name):
        return f"{self.prefix}, {name}!"

g = Greeter("Hi")
print(g.greet("World"))
```

### Hands-on: Classes and Objects

1. State **Classes and Objects** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## The __init__ Constructor and self

> **Definition:** This section explains **The __init__ Constructor and self** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **the __init__ constructor and self** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: The __init__ Constructor and self
x = chapter_7_demo = True
print("The __init__ Constructor and self", x)
```

### Hands-on: The __init__ Constructor and self

1. State **The __init__ Constructor and self** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Instance vs Class Attributes

> **Definition:** This section explains **Instance vs Class Attributes** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **instance vs class attributes** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Instance vs Class Attributes
x = chapter_7_demo = True
print("Instance vs Class Attributes", x)
```

### Hands-on: Instance vs Class Attributes

1. State **Instance vs Class Attributes** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Instance Methods

> **Definition:** This section explains **Instance Methods** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **instance methods** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Instance Methods
x = chapter_7_demo = True
print("Instance Methods", x)
```

### Hands-on: Instance Methods

1. State **Instance Methods** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Inheritance

> **Definition:** This section explains **Inheritance** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **inheritance** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Inheritance
x = chapter_7_demo = True
print("Inheritance", x)
```

### Hands-on: Inheritance

1. State **Inheritance** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## super() and Method Overriding

> **Definition:** This section explains **super() and Method Overriding** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **super() and method overriding** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: super() and Method Overriding
x = chapter_7_demo = True
print("super() and Method Overriding", x)
```

### Hands-on: super() and Method Overriding

1. State **super() and Method Overriding** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Method Types: instance, class, static

> **Definition:** This section explains **Method Types: instance, class, static** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **method types: instance, class, static** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Method Types: instance, class, static
x = chapter_7_demo = True
print("Method Types: instance, class, static", x)
```

### Hands-on: Method Types: instance, class, static

1. State **Method Types: instance, class, static** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Encapsulation and Properties

> **Definition:** This section explains **Encapsulation and Properties** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **encapsulation and properties** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Encapsulation and Properties
x = chapter_7_demo = True
print("Encapsulation and Properties", x)
```

### Hands-on: Encapsulation and Properties

1. State **Encapsulation and Properties** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Dataclasses

> **Definition:** This section explains **Dataclasses** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **dataclasses** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Dataclasses
x = chapter_7_demo = True
print("Dataclasses", x)
```

### Hands-on: Dataclasses

1. State **Dataclasses** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Magic (Dunder) Methods

> **Definition:** This section explains **Magic (Dunder) Methods** — a core idea you will use throughout the chapter.

### Real-world analogy

Like a **recipe step** in a cookbook — order and clarity prevent mistakes.

You will use **magic (dunder) methods** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Magic (Dunder) Methods
x = chapter_7_demo = True
print("Magic (Dunder) Methods", x)
```

### Hands-on: Magic (Dunder) Methods

1. State **Magic (Dunder) Methods** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Abstract Base Classes

> **Definition:** This section explains **Abstract Base Classes** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **abstract base classes** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Abstract Base Classes
x = chapter_7_demo = True
print("Abstract Base Classes", x)
```

### Hands-on: Abstract Base Classes

1. State **Abstract Base Classes** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Composition vs Inheritance

> **Definition:** This section explains **Composition vs Inheritance** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **composition vs inheritance** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Composition vs Inheritance
x = chapter_7_demo = True
print("Composition vs Inheritance", x)
```

### Hands-on: Composition vs Inheritance

1. State **Composition vs Inheritance** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## Multiple Inheritance and MRO

> **Definition:** This section explains **Multiple Inheritance and MRO** — a core idea you will use throughout the chapter.

### Real-world analogy

Like LEGO **instruction booklets** — small standard pieces combine into big systems.

You will use **multiple inheritance and mro** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: Multiple Inheritance and MRO
x = chapter_7_demo = True
print("Multiple Inheritance and MRO", x)
```

### Hands-on: Multiple Inheritance and MRO

1. State **Multiple Inheritance and MRO** in your own words.
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
x = chapter_7_demo = True
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
x = chapter_7_demo = True
print("Common Mistakes", x)
```

### Hands-on: Common Mistakes

1. State **Common Mistakes** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



---

## OOP Design Checklist

> **Definition:** This section explains **OOP Design Checklist** — a core idea you will use throughout the chapter.

### Real-world analogy

Think of this like a **labeled drawer** in a desk — you know exactly where to look.

You will use **oop design checklist** in scripts, APIs, and data tasks.

### Example

```python
# Example related to: OOP Design Checklist
x = chapter_7_demo = True
print("OOP Design Checklist", x)
```

### Hands-on: OOP Design Checklist

1. State **OOP Design Checklist** in your own words.
2. Type the example; change one value and predict the output.
3. Note one real project where this concept appears.



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
