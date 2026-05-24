#!/usr/bin/env python3
"""Python course topic content — CH1 here, ch2–ch14 in python_body_data.py."""
from __future__ import annotations

from pathlib import Path
from textwrap import dedent

def b(
    defn: str,
    why: str,
    how_or_code: str,
    code: str | None = None,
    tip: str = "",
) -> str:
    if code is None:
        code = how_or_code
        how = (
            "Read the example, run it in a REPL or script, then change one value "
            "and predict the output before you execute."
        )
    else:
        how = how_or_code
    block = f"""> **Definition:** {defn}

### Why it matters

{why}

### How it works

{how}

{code.strip()}
"""
    if tip:
        block += f"\n### Tip\n\n{tip}\n"
    return block


def bp(items: list[str]) -> str:
    lines = "\n".join(f"- {x}" for x in items)
    return f"### Guidelines\n\n{lines}\n"


def cm(rows: list[tuple[str, str, str]]) -> str:
  lines = [
    "| Mistake | Why it hurts | Fix |",
    "|---------|--------------|-----|",
  ]
  for m, why, fix in rows:
    lines.append(f"| {m} | {why} | {fix} |")
  return "\n".join(lines) + "\n"


# ─── Chapter 1 ─────────────────────────────────────────────────────────────

CH1: dict[str, str] = {
  "What is Python?": b(
    "Python is a **high-level, interpreted programming language** focused on readability and productivity.",
    "You can build web apps, automation, data tools, and scripts without fighting verbose syntax.",
    "You write `.py` files, run them with the Python interpreter, and get results quickly.",
    dedent("""\
```python
names = ["Alice", "Bob", "Carol"]
for name in names:
    print(f"Hello, {name}!")
```"""),
  ),
  "Python vs Other Languages": b(
    "Python trades some raw speed for **developer speed** — less boilerplate than Java or C++, more structure than shell scripts.",
    "Choosing a language depends on the problem: Python excels at glue code, APIs, and data work.",
    "Compare syntax, typing model, and ecosystem when learning a second language.",
    dedent("""\
```python
# Python: no braces, indentation defines blocks
def greet(name):
    return f"Hi, {name}"

print(greet("Sam"))
```"""),
  ),
  "History of Python": b(
    "Python was created by **Guido van Rossum**, first released in 1991, and is now maintained by the Python Software Foundation.",
    "Knowing the timeline explains Python 2 vs 3 and why modern tutorials target Python 3 only.",
    "Major versions add features (f-strings, type hints, pattern matching) while keeping readability.",
    dedent("""\
```python
import sys
print(sys.version)  # shows your interpreter version
```"""),
  ),
  "Where Python Is Used": b(
    "Python appears in **web backends**, data science, DevOps automation, education, and scripting.",
    "One language can support many career paths — fundamentals transfer across domains.",
    "Libraries extend the core: Django for web, pandas for data, pytest for testing.",
    dedent("""\
```python
# Tiny automation example
from pathlib import Path
count = sum(1 for _ in Path(".").glob("*.py"))
print(f"Python files here: {count}")
```"""),
  ),
  "Installing Python": b(
    "Install **Python 3.10+** from [python.org](https://www.python.org/downloads/) or your OS package manager.",
    "Without a working interpreter you cannot run examples from this course.",
    "Verify install with `python --version` and `python -m pip --version`.",
    dedent("""\
```bash
python --version
python -m pip --version
```"""),
  ),
  "Running Python Code": b(
    "Run code in the **REPL** (interactive shell), as a **script** (`.py` file), or from an **IDE**.",
    "Different modes suit experiments vs repeatable programs.",
    "Use the REPL for quick tests; use `.py` files for anything you want to keep or share.",
    dedent("""\
```bash
python                    # REPL
python hello.py           # script
python -c "print(2 + 2)"  # one-liner
```"""),
  ),
  "Your First Python Program": b(
    "A minimal program uses `print()` to show output.",
    "Success here proves your environment works.",
    "Save code in `hello.py` and run `python hello.py` from the terminal.",
    dedent("""\
```python
print("Hello, Python!")
```"""),
  ),
  "Statements and Expressions": b(
    "An **expression** produces a value (`2 + 2`). A **statement** performs an action (`x = 5`, `if`, `for`).",
    "Every useful program mixes both.",
    dedent("""\
```python
x = 10          # statement (assignment)
y = x * 2       # expression on right side
print(y)        # statement calling print
```"""),
  ),
  "Comments in Python": b(
    "Comments start with `#` and are ignored by the interpreter. **Docstrings** document modules and functions.",
    "Comments explain *why*, not *what* obvious code already shows.",
    dedent("""\
```python
# tax rate for the current year
RATE = 0.08

def total(price):
    '''Return price with tax.'''
    return price * (1 + RATE)
```"""),
  ),
  "Variables and Assignment": b(
    "A **variable** is a name bound to an object. Python is **dynamically typed**.",
    "Names make code readable and let you reuse values.",
    dedent("""\
```python
count = 0
count += 1
name, age = "Dana", 28
```"""),
  ),
  "Variable Naming Rules": b(
    "Names use letters, digits, and underscores; cannot start with a digit. Follow **snake_case** (PEP 8).",
    "Good names reduce bugs and help teammates understand code.",
    dedent("""\
```python
user_count = 3      # good
# 2fast = True      # SyntaxError
class = "A"         # SyntaxError — reserved word
```"""),
    "Avoid single-letter names except loop counters (`i`, `j`).",
  ),
  "Arithmetic Operators": b(
    "Python supports `+`, `-`, `*`, `/`, `//`, `%`, and `**` (power).",
    "Math operators underpin calculations in every program.",
    dedent("""\
```python
print(10 / 3)   # 3.333... true division
print(10 // 3)  # 3 floor division
print(10 % 3)   # 1 remainder
print(2 ** 10)  # 1024
```"""),
  ),
  "Comparison and Logical Operators": b(
    "Comparisons (`==`, `!=`, `<`, `>`) return `bool`. Combine with `and`, `or`, `not`.",
    "Conditions drive `if` statements and loops.",
    dedent("""\
```python
age = 20
can_vote = age >= 18
has_id = True
if can_vote and has_id:
    print("Eligible")
```"""),
  ),
  "Assignment and Identity Operators": b(
    "**Augmented assignment** (`+=`, `-=`) updates in place. **`is`** tests object identity; **`==`** tests value equality.",
    "Use `is` only for `None` and small singleton cases; otherwise prefer `==`.",
    dedent("""\
```python
score = 10
score += 5
x = None
if x is None:
    print("no value yet")
```"""),
  ),
  "Input and Output": b(
    "`input()` reads a line of text from the user. `print()` writes to the console.",
    "Interactive programs need both.",
    dedent("""\
```python
name = input("Your name: ").strip()
print(f"Welcome, {name}!")
```"""),
    "Always `.strip()` user input unless whitespace matters.",
  ),
  "Indentation and Code Blocks": b(
    "Python uses **indentation** (4 spaces) instead of braces to define blocks.",
    "Consistent indentation is required — mixing tabs and spaces causes errors.",
    dedent("""\
```python
if True:
    print("inside block")
    print("still inside")
print("outside")
```"""),
  ),
  "The None Value": b(
    "`None` is a singleton meaning **no value** or **not set yet**.",
    "Functions without `return` give `None`. APIs use `None` for missing data.",
    dedent("""\
```python
result = None

def find_user(id):
  return None  # not found

if result is None:
    print("empty")
```"""),
  ),
  "Essential Built-in Functions": b(
    "Built-ins like `len`, `type`, `int`, `str`, `sum`, and `max` are always available.",
    "They cover common tasks without imports.",
    dedent("""\
```python
print(len("hello"))
print(type(42))
print(sum([1, 2, 3]))
print(max(3, 9, 2))
```"""),
  ),
  "PEP 8 and Code Style": b(
    "**PEP 8** is the official Python style guide: naming, spacing, imports, and line length.",
    "Consistent style makes team code reviews faster.",
    dedent("""\
```python
# PEP 8: spaces around operators, blank lines between functions

def add(a, b):
    return a + b
```"""),
  ),
}

CH1_BP = bp([
    "Use `snake_case` for variables and functions.",
    "Prefer f-strings for formatting.",
    "Run `python -m pip install` only inside a virtual environment for projects.",
    "Read tracebacks from the bottom line upward.",
])
CH1_CM = cm([
    ("Using `=` instead of `==` in conditions", "Assigns instead of comparing", "Use `==` for equality"),
    ("Forgetting `input()` returns str", "Math on strings fails or behaves oddly", "Cast with `int()` / `float()`"),
    ("Tabs vs spaces", "IndentationError", "Configure editor to insert 4 spaces"),
])


def get_topic_content() -> tuple[dict[str, str], dict[int, str], dict[int, str]]:
    """Merge chapter topic dicts from source modules (no generated file needed)."""
    from python_body_data import (
        CH10,
        CH10_BP,
        CH10_CM,
        CH11,
        CH11_BP,
        CH11_CM,
        CH12,
        CH12_BP,
        CH12_CM,
        CH13,
        CH13_BP,
        CH13_CM,
        CH14,
        CH14_BP,
        CH14_CM,
        CH2,
        CH2_BP,
        CH2_CM,
        CH3,
        CH3_BP,
        CH3_CM,
        CH4,
        CH4_BP,
        CH4_CM,
        CH5,
        CH5_BP,
        CH5_CM,
        CH6,
        CH6_BP,
        CH6_CM,
        CH7,
        CH7_BP,
        CH7_CM,
        CH8,
        CH8_BP,
        CH8_CM,
        CH9,
        CH9_BP,
        CH9_CM,
    )

    topic_bodies: dict[str, str] = {}
    for block in (CH1, CH2, CH3, CH4, CH5, CH6, CH7, CH8, CH9, CH10, CH11, CH12, CH13, CH14):
        topic_bodies.update(block)

    return topic_bodies, {
        1: CH1_BP,
        2: CH2_BP,
        3: CH3_BP,
        4: CH4_BP,
        5: CH5_BP,
        6: CH6_BP,
        7: CH7_BP,
        8: CH8_BP,
        9: CH9_BP,
        10: CH10_BP,
        11: CH11_BP,
        12: CH12_BP,
        13: CH13_BP,
        14: CH14_BP,
    }, {
        1: CH1_CM,
        2: CH2_CM,
        3: CH3_CM,
        4: CH4_CM,
        5: CH5_CM,
        6: CH6_CM,
        7: CH7_CM,
        8: CH8_CM,
        9: CH9_CM,
        10: CH10_CM,
        11: CH11_CM,
        12: CH12_CM,
        13: CH13_CM,
        14: CH14_CM,
    }


def main() -> None:
    topic_bodies, _, _ = get_topic_content()
    print(f"Loaded {len(topic_bodies)} topic bodies from python_body_data.py + CH1")


if __name__ == "__main__":
    main()
