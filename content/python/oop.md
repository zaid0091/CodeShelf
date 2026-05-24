---
title: Python OOP
description: Classes, inheritance, and object-oriented patterns
order: 2
tags: [oop, classes]
---

# Python OOP

Object-oriented programming in Python — classes, inheritance, and magic methods.

## Classes & Objects

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

dog = Dog("Buddy", 3)
print(dog.bark())
```

## Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof"
```

## Properties & Encapsulation

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * self._radius ** 2
```

## Dataclasses (Python 3.7+)

```python
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    email: str = ""

user = User(1, "Alice")
print(user)  # User(id=1, name='Alice', email='')
```

## Magic Methods

| Method | Purpose |
|--------|---------|
| `__init__` | Constructor |
| `__str__` | Human-readable string |
| `__repr__` | Developer representation |
| `__len__` | Length support |
| `__eq__` | Equality comparison |
| `__getitem__` | Index access |
