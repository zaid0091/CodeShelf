---
title: Object-Oriented Programming
description: Classes, inheritance, encapsulation, dataclasses, and magic methods
order: 7
tags: [python, oop, classes]
---

# Chapter 7: Object-Oriented Programming

## 7.1 OOP in Python

> **Definition:** **Object-oriented programming (OOP)** models software as objects that combine data (**attributes**) and behavior (**methods**).

Python supports OOP without forcing everything into classes — use classes when state and behavior belong together.

## 7.2 Classes and objects

```python
class Dog:
    species = "Canis familiaris"  # class attribute

    def __init__(self, name: str, age: int):
        self.name = name          # instance attribute
        self.age = age

    def bark(self) -> str:
        return f"{self.name} says woof!"

    def __str__(self) -> str:
        return f"Dog(name={self.name}, age={self.age})"

buddy = Dog("Buddy", 3)
print(buddy.bark())
print(buddy.species)
```

| Concept | Description |
|---------|-------------|
| Class | Blueprint for objects |
| Instance | Concrete object created from a class |
| `self` | Reference to the current instance |
| `__init__` | Constructor — initializes instance |

## 7.3 Instance vs class attributes

```python
class Counter:
    total = 0  # shared by all instances

    def __init__(self):
        Counter.total += 1
        self.id = Counter.total
```

Class attributes are shared; instance attributes are per-object.

## 7.4 Inheritance

```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError("Subclass must implement")

class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says meow"

class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says woof"
```

### `super()`

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
```

## 7.5 Method types

```python
class MyClass:
    @classmethod
    def from_string(cls, data: str):
        return cls(data.split())

    @staticmethod
    def add(x, y):
        return x + y
```

| Decorator | First arg | Use case |
|-----------|-----------|----------|
| (none) | `self` | Instance behavior |
| `@classmethod` | `cls` | Alternative constructors |
| `@staticmethod` | none | Utility in class namespace |

## 7.6 Encapsulation and properties

```python
class Circle:
    def __init__(self, radius: float):
        self._radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        if value < 0:
            raise ValueError("Radius must be non-negative")
        self._radius = value

    @property
    def area(self) -> float:
        return 3.14159 * self._radius ** 2
```

## 7.7 Dataclasses (Python 3.7+)

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class User:
    id: int
    name: str
    email: str = ""
    tags: List[str] = field(default_factory=list)

user = User(id=1, name="Alice")
print(user)
```

## 7.8 Magic (dunder) methods

| Method | Purpose |
|--------|---------|
| `__init__` | Constructor |
| `__str__` | Human-readable string (`str()`) |
| `__repr__` | Developer representation (`repr()`) |
| `__len__` | Support `len(obj)` |
| `__eq__` | Equality `==` |
| `__lt__` etc. | Ordering |
| `__getitem__` | Index access `obj[key]` |
| `__enter__`/`__exit__` | Context manager |

```python
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"Stack({self._items!r})"
```

## 7.9 Abstract base classes

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self) -> float:
        return self.w * self.h
```

## 7.10 Composition over inheritance

```python
class Engine:
    def start(self):
        return "Engine running"

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return self.engine.start()
```

Prefer composing objects over deep inheritance hierarchies.

## Exercises

1. Create a `BankAccount` class with deposit, withdraw, and balance property; prevent negative balance.
2. Subclass `Animal` with two concrete classes implementing `speak()`.
3. Convert a simple data-holding class to a `@dataclass`.
4. Implement `__eq__` and `__repr__` for a `Point(x, y)` class.

## Summary

Classes bundle state and behavior. Use inheritance sparingly, properties for validated attributes, and dataclasses for simple data containers.

## Next chapter

Continue to [Modules & Packages](./ch08-modules-packages.md).
