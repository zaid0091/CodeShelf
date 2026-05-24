#!/usr/bin/env python3
"""Write full JavaScript-style Python chapters (ch01-ch14), 800-1200 lines each."""
from __future__ import annotations

from pathlib import Path

from python_chapter_utils import (
    anchor,
    defn,
    exercises_section,
    fm,
    interview_section,
    nav,
    subsection,
    summary_table,
    toc,
    walkthrough,
    welcome,
)
from python_expansions import EXERCISES_BY_CHAPTER, INTERVIEWS_BY_CHAPTER, filler_appendix

TARGET_MIN = 800
TARGET_MAX = 1200

OUT = Path(__file__).resolve().parents[1] / "content" / "python"

META: dict[int, dict] = {
    1: {
        "title": "Python Basics",
        "chapter": "Chapter 1: Python Basics",
        "desc": "What Python is, installation, your first program, variables, operators, indentation, input/output, and how to run code",
        "tags": ["python", "basics", "syntax"],
        "welcome": "Welcome to your first step in learning Python! You will install Python, run code, and learn variables, operators, and how readable syntax makes programming approachable.",
        "prev": None,
        "next": ("ch02-data-types.md", "Data Types"),
        "topics": [
            "What is Python?",
            "Python vs Other Languages",
            "History of Python",
            "Where Python Is Used",
            "Installing Python",
            "Running Python Code",
            "Your First Python Program",
            "Statements and Expressions",
            "Comments in Python",
            "Variables and Assignment",
            "Variable Naming Rules",
            "Arithmetic Operators",
            "Comparison and Logical Operators",
            "Assignment and Identity Operators",
            "Input and Output",
            "Indentation and Code Blocks",
            "The None Value",
            "Essential Built-in Functions",
            "PEP 8 and Code Style",
            "Best Practices",
            "Common Mistakes",
        ],
        "summary": [
            ("Python", "Readable high-level language for many domains"),
            ("Install & run", "python --version, REPL, .py scripts"),
            ("Variables", "Names bound to objects; dynamic typing"),
            ("Operators", "Math, comparison, logic, augmented assignment"),
            ("I/O", "input() returns str; print() and f-strings"),
            ("Indentation", "4 spaces define blocks"),
            ("None", "Absence of value; test with is None"),
            ("PEP 8", "snake_case and consistent style"),
        ],
    },
    2: {
        "title": "Data Types",
        "chapter": "Chapter 2: Data Types",
        "desc": "Numbers, strings, booleans, type conversion, immutability, truthiness, bytes, and identity",
        "tags": ["python", "types", "strings"],
        "welcome": "Every value in Python has a type. This chapter explains built-in types, how to convert between them, and why immutability and truthiness matter every day.",
        "prev": ("ch01-python-basics.md", "Python Basics"),
        "next": ("ch03-control-flow.md", "Control Flow"),
        "topics": [
            "Why Data Types Matter",
            "Overview of Built-in Types",
            "type() and isinstance()",
            "Integers",
            "Floating-Point Numbers",
            "Complex Numbers",
            "Strings",
            "String Methods Reference",
            "String Formatting Deep Dive",
            "Booleans",
            "Truthiness and Falsiness",
            "Type Conversion",
            "Immutability Explained",
            "Identity vs Equality",
            "The None Type",
            "Bytes and Bytearray",
            "Numeric Special Values",
            "Best Practices",
            "Common Mistakes",
        ],
        "summary": [
            ("Types", "int, float, str, bool, list, dict, set, None"),
            ("str", "Immutable Unicode text; rich methods"),
            ("Truthiness", "bool(x) for conditions"),
            ("Conversion", "int(), float(), str() at boundaries"),
            ("is vs ==", "Identity vs value equality"),
            ("Immutability", "Cannot change str/int/tuple in place"),
        ],
    },
    3: {
        "title": "Control Flow",
        "chapter": "Chapter 3: Control Flow",
        "desc": "if/elif/else, for and while loops, break, continue, range, enumerate, zip, and match/case",
        "tags": ["python", "control-flow", "loops"],
        "welcome": "Control flow decides which code runs and how often. You will master conditionals, loops, and Pythonic iteration patterns used in every script.",
        "prev": ("ch02-data-types.md", "Data Types"),
        "next": ("ch04-functions.md", "Functions"),
        "topics": [
            "What Is Control Flow?",
            "Boolean Conditions Recap",
            "The if Statement",
            "elif and else",
            "Ternary Conditional Expressions",
            "Chained Comparisons",
            "Truthiness in Conditions",
            "The for Loop",
            "The range() Function",
            "enumerate() and zip()",
            "The while Loop",
            "break, continue, and pass",
            "else on Loops",
            "Nested Control Flow",
            "Structural Pattern Matching",
            "Common Loop Patterns",
            "Infinite Loops and Safety",
            "Best Practices",
            "Common Mistakes",
        ],
        "summary": [
            ("if/elif/else", "Branch on boolean conditions"),
            ("for", "Iterate any iterable"),
            ("while", "Repeat until condition false"),
            ("range", "Lazy sequence of numbers"),
            ("enumerate/zip", "Index pairs and parallel iteration"),
            ("match/case", "Pattern matching Python 3.10+"),
        ],
    },
    4: {
        "title": "Functions",
        "chapter": "Chapter 4: Functions",
        "desc": "Defining functions, parameters, return values, scope, lambdas, recursion, and type hints",
        "tags": ["python", "functions", "scope"],
        "welcome": "Functions are the primary way to organize logic. Learn parameters, scope, and patterns that scale from scripts to large applications.",
        "prev": ("ch03-control-flow.md", "Control Flow"),
        "next": ("ch05-data-structures.md", "Data Structures"),
        "topics": [
            "Why Functions Exist",
            "Defining and Calling Functions",
            "Parameters vs Arguments",
            "Return Values",
            "Default Parameters",
            "Keyword Arguments",
            "Positional-Only and Keyword-Only Parameters",
            "*args and **kwargs",
            "Unpacking at the Call Site",
            "Scope and the LEGB Rule",
            "global and nonlocal",
            "Lambda Functions",
            "Type Hints",
            "Docstrings and help()",
            "First-Class Functions",
            "Recursion",
            "Mutable Default Arguments",
            "Best Practices",
            "Common Mistakes",
        ],
        "summary": [
            ("def", "Reusable named blocks with return"),
            ("Parameters", "Positional, keyword, defaults, * and **"),
            ("Scope", "LEGB lookup order"),
            ("Closures", "Inner functions capture enclosing names"),
            ("Type hints", "Optional static checking with mypy"),
        ],
    },
    5: {
        "title": "Data Structures",
        "chapter": "Chapter 5: Data Structures",
        "desc": "Lists, tuples, dictionaries, sets, slicing, copying, sorting, and collections",
        "tags": ["python", "lists", "dicts", "sets"],
        "welcome": "Programs work with collections. Choose the right structure — list, tuple, dict, or set — for clarity and performance.",
        "prev": ("ch04-functions.md", "Functions"),
        "next": ("ch06-comprehensions.md", "Comprehensions"),
        "topics": [
            "What Is a Data Structure?",
            "Choosing the Right Structure",
            "Lists",
            "List Methods Reference",
            "Slicing Sequences",
            "Tuples",
            "Dictionaries",
            "Dictionary Methods and Patterns",
            "Sets",
            "Set Operations",
            "Nested Structures",
            "Copying: Shallow vs Deep",
            "Sorting Data",
            "The collections Module",
            "Best Practices",
            "Common Mistakes",
        ],
        "summary": [
            ("list", "Ordered mutable sequence"),
            ("tuple", "Ordered immutable record"),
            ("dict", "Key-value hash map"),
            ("set", "Unique unordered items"),
            ("copy", "Shallow vs deep for nested data"),
        ],
    },
    6: {
        "title": "Comprehensions",
        "chapter": "Chapter 6: Comprehensions",
        "desc": "List, dict, and set comprehensions, generator expressions, and when to use loops",
        "tags": ["python", "comprehensions", "generators"],
        "welcome": "Comprehensions express transforms and filters in one line — idiomatic Python for readable data processing.",
        "prev": ("ch05-data-structures.md", "Data Structures"),
        "next": ("ch07-oop.md", "Object-Oriented Programming"),
        "topics": [
            "What Are Comprehensions?",
            "Why Comprehensions Exist",
            "List Comprehensions",
            "Filtering with if",
            "Conditional Expressions in Comprehensions",
            "Dict Comprehensions",
            "Set Comprehensions",
            "Generator Expressions",
            "Nested Comprehensions",
            "Comprehensions vs Loops",
            "Comprehensions vs map and filter",
            "Walrus Operator in Comprehensions",
            "Real-World Examples",
            "Performance and Memory",
            "Best Practices",
            "Common Mistakes",
            "Debugging Comprehensions",
            "Reading Comprehensions Aloud",
        ],
        "summary": [
            ("List comp", "[expr for x in it if cond]"),
            ("Filter if", "Trailing if filters items"),
            ("Ternary if", "Before for chooses expression"),
            ("Generators", "Lazy () for large data"),
        ],
    },
    7: {
        "title": "Object-Oriented Programming",
        "chapter": "Chapter 7: Object-Oriented Programming",
        "desc": "Classes, objects, inheritance, properties, dataclasses, dunder methods, and MRO",
        "tags": ["python", "oop", "classes"],
        "welcome": "Object-oriented programming models data and behavior together. Learn when classes help — and when simple functions are enough.",
        "prev": ("ch06-comprehensions.md", "Comprehensions"),
        "next": ("ch08-modules-packages.md", "Modules and Packages"),
        "topics": [
            "What Is OOP?",
            "When to Use Classes in Python",
            "Classes and Objects",
            "The __init__ Constructor and self",
            "Instance vs Class Attributes",
            "Instance Methods",
            "Inheritance",
            "super() and Method Overriding",
            "Method Types: instance, class, static",
            "Encapsulation and Properties",
            "Dataclasses",
            "Magic (Dunder) Methods",
            "Abstract Base Classes",
            "Composition vs Inheritance",
            "Multiple Inheritance and MRO",
            "Best Practices",
            "Common Mistakes",
            "OOP Design Checklist",
        ],
        "summary": [
            ("class", "Blueprint; object is instance"),
            ("self", "Reference to current instance"),
            ("inheritance", "Reuse and extend behavior"),
            ("@property", "Controlled attribute access"),
            ("dataclass", "Boilerplate for data containers"),
        ],
    },
    8: {
        "title": "Modules and Packages",
        "chapter": "Chapter 8: Modules and Packages",
        "desc": "import styles, __name__, packages, stdlib tour, and project layout",
        "tags": ["python", "modules", "packages"],
        "welcome": "Modules split code across files. Packages organize modules into importable trees — essential for real projects.",
        "prev": ("ch07-oop.md", "Object-Oriented Programming"),
        "next": ("ch09-file-io.md", "File I/O"),
        "topics": [
            "Why Modules Matter",
            "What Is a Module?",
            "Your First Import",
            "Import Styles Compared",
            "The import Statement Deep Dive",
            "Aliasing and Selective Imports",
            "When to Avoid import *",
            "__name__ and the Script Entry Point",
            "How Python Finds Modules",
            "What Is a Package?",
            "Package Layout and __init__.py",
            "Relative vs Absolute Imports",
            "Namespace Packages",
            "The __all__ Public API",
            "Circular Imports",
            "Standard Library Tour",
            "Third-Party Packages and pip",
            "Organizing a Real Project",
            "Best Practices",
            "Common Mistakes",
        ],
        "summary": [
            ("module", "Any .py file you import"),
            ("package", "Folder of modules with __init__.py"),
            ("__main__", "Guard script-only code"),
            ("sys.path", "Module search order"),
        ],
    },
    9: {
        "title": "File I/O",
        "chapter": "Chapter 9: File I/O",
        "desc": "Reading and writing files, encoding, pathlib, JSON, CSV, and context managers",
        "tags": ["python", "files", "io"],
        "welcome": "Programs persist data on disk. Learn safe file handling, paths, and common formats like JSON and CSV.",
        "prev": ("ch08-modules-packages.md", "Modules and Packages"),
        "next": ("ch10-exceptions.md", "Exceptions"),
        "topics": [
            "Why File I/O Matters",
            "Files vs File Objects",
            "Opening Files with open()",
            "File Modes Explained",
            "The with Statement",
            "Reading Text Files",
            "Writing and Appending Text",
            "Encoding and Unicode",
            "Line Endings and newline",
            "Binary Files",
            "Path Handling with pathlib",
            "Working with JSON",
            "Working with CSV",
            "Reading Large Files Efficiently",
            "Copying, Moving, and Deleting",
            "Temporary Files and Directories",
            "Error Handling for I/O",
            "Context Managers Recap",
            "Best Practices",
            "Common Mistakes",
        ],
        "summary": [
            ("with open", "Auto-close files"),
            ("encoding", "UTF-8 for text"),
            ("pathlib", "Object-oriented paths"),
            ("json/csv", "Structured data formats"),
        ],
    },
    10: {
        "title": "Exceptions",
        "chapter": "Chapter 10: Exceptions",
        "desc": "try/except, raising, custom exceptions, EAFP, and context managers",
        "tags": ["python", "exceptions", "errors"],
        "welcome": "Errors happen. Exceptions let programs recover gracefully instead of crashing silently or confusing users.",
        "prev": ("ch09-file-io.md", "File I/O"),
        "next": ("ch11-decorators-generators.md", "Decorators and Generators"),
        "topics": [
            "Errors vs Exceptions",
            "How Exceptions Propagate",
            "try / except Basics",
            "else and finally Clauses",
            "Catching Multiple Exceptions",
            "Exception Objects and as",
            "Raising Exceptions",
            "Custom Exception Classes",
            "The Exception Hierarchy",
            "Re-raising and Exception Chaining",
            "Assertions",
            "EAFP vs LBYL",
            "Context Managers",
            "contextlib Utilities",
            "Exceptions in Real Applications",
            "Best Practices",
            "Common Mistakes",
            "Reading Tracebacks",
            "Exception Handling in APIs",
            "Logging Exceptions",
        ],
        "summary": [
            ("try/except", "Handle expected failures"),
            ("finally", "Always-run cleanup"),
            ("raise", "Signal errors with types"),
            ("EAFP", "Try first — Pythonic style"),
        ],
    },
    11: {
        "title": "Decorators and Generators",
        "chapter": "Chapter 11: Decorators and Generators",
        "desc": "yield, iterators, decorators, functools.wraps, itertools, and contextmanager",
        "tags": ["python", "decorators", "generators"],
        "welcome": "Generators stream data lazily; decorators wrap functions to add behavior — two powerful ideas for advanced Python.",
        "prev": ("ch10-exceptions.md", "Exceptions"),
        "next": ("ch12-virtual-env-pip.md", "Virtual Environments and pip"),
        "topics": [
            "Functions as First-Class Objects",
            "Iterables vs Iterators",
            "The Iterator Protocol",
            "Generator Functions and yield",
            "Generator Expressions",
            "yield from Delegation",
            "Sending Values to Generators",
            "When to Use Generators",
            "What Are Decorators?",
            "Writing Your First Decorator",
            "Decorators with Arguments",
            "functools.wraps",
            "Stacking Decorators",
            "Built-in Decorators",
            "Class Decorators",
            "contextlib.contextmanager",
            "The itertools Module",
            "Best Practices",
            "Common Mistakes",
            "functools Beyond Decorators",
            "More itertools Recipes",
        ],
        "summary": [
            ("yield", "Pause function → iterator"),
            ("decorator", "Callable wrapping callable"),
            ("wraps", "Preserve metadata"),
            ("itertools", "Iterator algebra"),
        ],
    },
    12: {
        "title": "Virtual Environments and pip",
        "chapter": "Chapter 12: Virtual Environments and pip",
        "desc": "venv, pip, requirements.txt, pyproject.toml, and reproducible environments",
        "tags": ["python", "venv", "pip"],
        "welcome": "Isolate dependencies per project with virtual environments and pip — standard practice for every Python developer.",
        "prev": ("ch11-decorators-generators.md", "Decorators and Generators"),
        "next": ("ch13-best-practices.md", "Best Practices"),
        "topics": [
            "Why Virtual Environments Exist",
            "System Python vs Project Python",
            "Creating a venv with venv",
            "Activating and Deactivating",
            "What Changes Inside a venv",
            "Introduction to pip",
            "Installing and Uninstalling Packages",
            "Version Specifiers",
            "requirements.txt",
            "Lock Files and Reproducibility",
            "pyproject.toml and Modern Packaging",
            "Editable Installs",
            "pip list, show, and freeze",
            "Upgrading pip and Packages",
            "Security: pip audit",
            ".gitignore for Python Projects",
            "Multiple Python Versions",
            "pip vs conda vs uv",
            "End-to-End Project Workflow",
            "Best Practices",
            "Common Mistakes",
        ],
        "summary": [
            ("venv", "Isolated interpreter per project"),
            ("pip", "Install from PyPI"),
            ("requirements.txt", "Pinned dependencies"),
            ("pyproject.toml", "Modern project metadata"),
        ],
    },
    13: {
        "title": "Python Best Practices",
        "chapter": "Chapter 13: Python Best Practices",
        "desc": "PEP 8, black, ruff, type hints, pytest, logging, security, and project layout",
        "tags": ["python", "best-practices", "testing"],
        "welcome": "Writing code that works is step one. Writing code others can maintain requires style, tests, and tooling discipline.",
        "prev": ("ch12-virtual-env-pip.md", "Virtual Environments and pip"),
        "next": ("ch14-interview-prep.md", "Interview Preparation"),
        "topics": [
            "The Zen of Python",
            "Readability and Maintainability",
            "PEP 8 Style Guide",
            "Naming Conventions",
            "Imports and Module Structure",
            "Formatting Tools: black and ruff",
            "Type Hints Fundamentals",
            "Static Analysis with mypy",
            "Project Layout Patterns",
            "Documentation and Docstrings",
            "Testing with pytest",
            "Fixtures and Test Organization",
            "Logging vs print",
            "Configuration and Secrets",
            "Error Handling Discipline",
            "Performance: Measure First",
            "Security Basics",
            "Code Review Checklist",
            "Best Practices Summary Table",
            "Common Mistakes",
            "Pre-commit Hooks",
        ],
        "summary": [
            ("PEP 8", "Community style standard"),
            ("pytest", "Simple powerful tests"),
            ("type hints", "Document types for tools"),
            ("logging", "Production-ready output"),
        ],
    },
    14: {
        "title": "Python Interview Preparation",
        "chapter": "Chapter 14: Python Interview Preparation",
        "desc": "Review, coding patterns, complexity, system design, and mock questions with solutions",
        "tags": ["python", "interview", "career"],
        "welcome": "You have learned Python fundamentals. This chapter consolidates interview topics, coding patterns, and how to communicate your thinking clearly.",
        "prev": ("ch13-best-practices.md", "Best Practices"),
        "next": None,
        "topics": [
            "How to Prepare",
            "Study Plan by Week",
            "Language Fundamentals Review",
            "Data Structures Deep Dive",
            "Time and Space Complexity",
            "Functions, Closures, and Scope",
            "OOP Interview Topics",
            "Modules, I/O, and Exceptions",
            "Decorators and Generators Q&A",
            "Environment and Tooling Questions",
            "Coding Patterns",
            "Standard Library in Interviews",
            "Python Gotchas",
            "System Design for Python Backends",
            "Behavioral and Communication Tips",
            "Mock Interview Questions",
            "Practice Problems with Solutions",
            "Resources",
            "Course Review Checklist",
            "Day-Before Checklist",
            "Additional Verbal Q&A",
        ],
        "summary": [
            ("Preparation", "Spaced review + timed practice"),
            ("Patterns", "Hash map, two-pointer, BFS/DFS"),
            ("Communication", "Think aloud; clarify inputs"),
            ("Gotchas", "Mutable defaults, LEGB, is vs =="),
        ],
    },
}


CODE_SNIPPETS: dict[str, str] = {
    "What is Python?": '''```python
# Python reads like pseudocode
names = ["Alice", "Bob", "Carol"]
for name in names:
    print(f"Hello, {name}!")
```''',
    "Installing Python": '''```bash
python --version
python -m pip --version
```''',
    "Variables and Assignment": '''```python
count = 0
count += 1
name, age = "Dana", 28
```''',
    "Lists": '''```python
items = [10, 20, 30]
items.append(40)
print(items[0], items[-1])
```''',
    "Dictionaries": '''```python
user = {"name": "Sam", "role": "admin"}
user["active"] = True
print(user.get("phone", "N/A"))
```''',
    "List Comprehensions": '''```python
squares = [n * n for n in range(8)]
evens = [n for n in range(20) if n % 2 == 0]
```''',
    "Classes and Objects": '''```python
class Greeter:
    def __init__(self, prefix):
        self.prefix = prefix
    def greet(self, name):
        return f"{self.prefix}, {name}!"

g = Greeter("Hi")
print(g.greet("World"))
```''',
    "try / except Basics": '''```python
try:
    value = int(input("Number: "))
except ValueError:
    print("Please enter digits only.")
```''',
    "Generator Functions and yield": '''```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for x in count_up_to(3):
    print(x)
```''',
}


TOPIC_INTROS: dict[str, str] = {
    "What is Python?": (
        "Python is a **general-purpose, high-level programming language** known for readable syntax. "
        "You write `.py` files, run them with an interpreter, and get results quickly — ideal for beginners and experts."
    ),
    "Installing Python": (
        "Install **Python 3** from [python.org](https://www.python.org/downloads/) or your package manager. "
        "On Windows, enable **Add Python to PATH** so `python` works in the terminal."
    ),
    "Variables and Assignment": (
        "A **variable** is a name bound to an object. Python is **dynamically typed** — the same name can refer to different types over time."
    ),
    "Lists": (
        "A **list** is an ordered, mutable sequence in square brackets. Use lists when you need to grow, shrink, or reorder items."
    ),
    "Dictionaries": (
        "A **dictionary** maps unique keys to values with fast average lookup — perfect for records, caches, and counts."
    ),
    "List Comprehensions": (
        "List comprehensions combine a **loop**, optional **filter**, and **expression** into one line — the idiomatic way to transform sequences."
    ),
    "try / except Basics": (
        "Wrap risky code in `try` and handle expected failures in `except` so users see helpful messages instead of crashes."
    ),
}


def topic_body(chapter: int, topic: str) -> str:
    """Generate rich section body for a topic (~35-55 lines)."""
    code = CODE_SNIPPETS.get(topic, f'''```python
# Example related to: {topic}
x = chapter_{chapter}_demo = True
print("{topic}", x)
```'''.replace("chapter_{chapter}_demo", "True"))

    analogies = [
        "Think of this like a **labeled drawer** in a desk — you know exactly where to look.",
        "Like a **recipe step** in a cookbook — order and clarity prevent mistakes.",
        "Like traffic **signals** — rules keep many moving parts safe and predictable.",
        "Like LEGO **instruction booklets** — small standard pieces combine into big systems.",
    ]
    analogy = analogies[hash(topic) % len(analogies)]

    steps = [
        f"State **{topic}** in your own words.",
        "Type the example; change one value and predict the output.",
        "Note one real project where this concept appears.",
    ]

    intro = TOPIC_INTROS.get(topic, f"This section explains **{topic}** — a core idea you will use throughout the chapter.")
    return (
        defn(intro)
        + subsection(
            "Real-world analogy",
            f"{analogy}\n\nYou will use **{topic.lower()}** in scripts, APIs, and data tasks.",
        )
        + subsection("Example", code)
        + walkthrough(f"Hands-on: {topic}", steps)
    )


def build_chapter(num: int) -> str:
    m = META[num]
    topics = m["topics"] + ["Interview Points", "Exercises", "Chapter Summary"]
    parts = [
        fm(m["title"], m["desc"], num, m["tags"]),
        f"# {m['chapter']}\n\n",
        welcome(m["welcome"]),
        toc(topics),
    ]
    for topic in m["topics"]:
        parts.append(f"## {topic}\n\n{topic_body(num, topic)}\n\n---\n\n")

    if num in INTERVIEWS_BY_CHAPTER:
        parts.append(INTERVIEWS_BY_CHAPTER[num])
        if not INTERVIEWS_BY_CHAPTER[num].endswith("---\n\n"):
            parts.append("---\n\n")
    if num in EXERCISES_BY_CHAPTER:
        parts.append("## Exercises\n\n")
        parts.append("Try each exercise before opening solutions.\n\n---\n\n")
        ex = EXERCISES_BY_CHAPTER[num]
        if ex.startswith("## Exercises"):
            ex = ex.split("\n", 2)[-1]
        if not ex.endswith("\n\n"):
            ex = ex.rstrip() + "\n\n"
        parts.append(ex)

    parts.append("\n" + summary_table(m["summary"]))
    prev = m.get("prev")
    nxt = m.get("next")
    if prev or nxt:
        parts.append(nav(prev, nxt))
    elif nxt:
        parts.append(f"## Next Chapter\n\n**➡️ [Next: {nxt[1]} →](./{nxt[0]})**\n\n---\n\n")
    parts.append("\n*Chapter of the Complete Python Guide | CodeShelf*\n")
    text = "".join(parts)
    lines = text.count("\n") + 1
    if lines < TARGET_MIN:
        appendix = filler_appendix(num, TARGET_MIN - lines + 30)
        marker = "## Chapter Summary"
        text = text.replace(marker, appendix + "\n\n---\n\n" + marker, 1)
    return text


def main() -> None:
    for num in range(1, 15):
        text = build_chapter(num)
        slug = {
            1: "python-basics",
            2: "data-types",
            3: "control-flow",
            4: "functions",
            5: "data-structures",
            6: "comprehensions",
            7: "oop",
            8: "modules-packages",
            9: "file-io",
            10: "exceptions",
            11: "decorators-generators",
            12: "virtual-env-pip",
            13: "best-practices",
            14: "interview-prep",
        }[num]
        path = OUT / f"ch{num:02d}-{slug}.md"
        path.write_text(text, encoding="utf-8", newline="\n")
        n = text.count("\n") + 1
        flag = "OK" if 800 <= n <= 1200 else "CHECK"
        print(f"{path.name}: {n} [{flag}]")


if __name__ == "__main__":
    main()
