# Auto-built topic bodies ch2–ch14. Import: from python_body_data import CH2, CH3, ...
from textwrap import dedent
from make_python_bodies import b, bp, cm


def _c(code: str) -> str:
    return f"```python\n{dedent(code).strip()}\n```"


CH2 = {
  "Why Data Types Matter": b("Every value has a **type** that determines what operations are valid.", "Adding a string to an integer raises `TypeError`.", "Check types with `type()` and convert explicitly.", _c("print(type(42), type('42'))")),
  "Overview of Built-in Types": b("Core types include numbers, strings, booleans, sequences, and mappings.", "Choosing the right type models your data correctly.", _c("sample = [1, 'a', True, {'k': 1}]\nprint([type(x).__name__ for x in sample]")),
  "type() and isinstance()": b("`type(x)` returns the exact class. `isinstance(x, int)` respects inheritance.", "Prefer `isinstance` for type checks in application code.", _c("print(isinstance(3, int))\nprint(isinstance(True, int))  # bool subclasses int")),
  "Integers": b("**int** is arbitrary-precision whole numbers.", "No overflow like fixed-width integers in C.", _c("big = 10 ** 30\nprint(big)")),
  "Floating-Point Numbers": b("**float** represents decimals in binary — some values are approximate.", "Use `decimal.Decimal` for money.", _c("print(0.1 + 0.2)\nprint(round(0.1 + 0.2, 2)")),
  "Complex Numbers": b("**complex** uses `j` for imaginary unit: `3+4j`.", "Used in science/engineering libraries.", _c("z = 3 + 4j\nprint(z.real, z.imag, abs(z))")),
  "Strings": b("**str** is immutable Unicode text in quotes.", "Most user-facing data is strings.", _c('msg = "Hello"\nprint(msg.upper(), len(msg))')),
  "String Methods Reference": b("Strings have dozens of methods: `strip`, `split`, `join`, `replace`, etc.", "Methods return new strings — originals never change.", _c('line = "  a,b,c  "\nparts = line.strip().split(",")\nprint("|".join(parts))')),
  "String Formatting Deep Dive": b("Format with **f-strings**, `.format()`, or `%` (legacy).", "f-strings are fastest to read and write.", _c('name, score = "Ada", 98\nprint(f"{name} scored {score}%")')),
  "Booleans": b("**bool** is `True` or `False`, subclass of `int`.", "Drive conditional logic.", _c("print(bool(0), bool(1), bool(''))")),
  "Truthiness and Falsiness": b("Empty containers and zero are **falsy**; most other values are **truthy**.", "Use `if items:` instead of `if len(items) > 0`.", _c("values = [[], [0], '0', None]\nprint([bool(v) for v in values])")),
  "Type Conversion": b("Convert with `int()`, `float()`, `str()`, `list()`, etc.", "Explicit conversion beats implicit surprises.", _c("n = int('42')\nprint(n + 8)")),
  "Immutability Explained": b("Immutable objects cannot change in place; operations create new objects.", "Explains why strings/tuples behave differently from lists.", _c("s = 'hi'\ns2 = s + '!'\nprint(s, s2)")),
  "Identity vs Equality": b("`==` compares values; `is` compares object identity.", "Use `is` for `None` only in most code.", _c("a = [1,2]\nb = [1,2]\nprint(a == b, a is b)")),
  "The None Type": b("`None` has type `NoneType` — single global instance.", "Represents missing or optional values.", _c("x = None\nprint(x is None)")),
  "Bytes and Bytearray": b("`bytes` is immutable binary; `bytearray` is mutable.", "Use at file/network boundaries.", _c("data = b'hello'\nprint(data.decode('utf-8'))")),
  "Numeric Special Values": b("Floats include `inf`, `-inf`, and `nan` from the math module.", "Comparisons with `nan` are always False.", _c("import math\nprint(math.isnan(float('nan')))")),
}
CH2_BP = bp(["Prefer `isinstance` over `type() ==`", "Use f-strings", "Never compare floats with `==` for money"])
CH2_CM = cm([("`is` for values", "Wrong equality semantics", "Use `==` except for `None`")])

CH3 = {
  "What Is Control Flow?": b("**Control flow** decides which lines run, how often, and in what order.", "Without branches and loops, programs cannot respond to input or process collections.", _c("score = 85\nprint('pass' if score >= 60 else 'fail')")),
  "Boolean Conditions Recap": b("Conditions use `and`, `or`, `not` and evaluate to `True` or `False`.", "Short-circuiting skips the right side when the result is already known.", _c("name = ''\nif name and name[0] == 'A':\n    print('starts with A')")),
  "The if Statement": b("`if condition:` runs a block when the condition is truthy.", "The building block of decision-making.", _c("age = 20\nif age >= 18:\n    print('adult')")),
  "elif and else": b("`elif` checks another condition; `else` runs when all prior conditions were false.", "Order from most specific to most general.", _c("x = 15\nif x < 10:\n    print('small')\nelif x < 20:\n    print('medium')\nelse:\n    print('large')")),
  "Ternary Conditional Expressions": b("`value_if_true if condition else value_if_false` chooses between two expressions.", "Use for simple assignments, not multi-line logic.", _c("status = 'ok' if errors == 0 else 'fail'")),
  "Chained Comparisons": b("`a < b < c` is equivalent to `a < b and b < c`.", "Readable range and bound checks.", _c("n = 15\nprint(10 < n < 20)")),
  "Truthiness in Conditions": b("Objects convert to `bool` in `if` — empty collections and zero are falsy.", "Write `if items:` instead of `if len(items) > 0`.", _c("if []:\n    print('never')\nif [0]:\n    print('runs')")),
  "The for Loop": b("`for item in iterable:` visits each element.", "Preferred when iterating sequences.", _c("for ch in 'abc':\n    print(ch)")),
  "The range() Function": b("`range(n)` or `range(start, stop, step)` yields integers lazily.", "Avoid building huge lists with `list(range(...))` unless needed.", _c("print(list(range(2, 10, 2)))")),
  "enumerate() and zip()": b("`enumerate` adds indexes; `zip` pairs parallel iterables.", "Cleaner than manual index arithmetic.", _c("for i, w in enumerate(['a','b']):\n    print(i, w)\nfor a, b in zip([1,2], ['x','y']):\n    print(a, b)")),
  "The while Loop": b("Repeats while the condition stays true.", "Update loop variables inside the body to avoid infinite loops.", _c("n = 3\nwhile n:\n    print(n)\n    n -= 1")),
  "break, continue, and pass": b("`break` exits the loop; `continue` skips to the next item; `pass` is a no-op placeholder.", "Search loops often `break` when a match is found.", _c("for n in range(10):\n    if n == 5:\n        break\n    print(n)")),
  "else on Loops": b("A loop `else` runs only if the loop did not `break`.", "Useful for 'not found' patterns.", _c("for x in [1,2,3]:\n    if x == 9:\n        break\nelse:\n    print('not found')")),
  "Nested Control Flow": b("Loops and `if` statements can nest inside each other.", "Extract functions when nesting exceeds two levels.", _c("for row in matrix:\n    for val in row:\n        if val < 0:\n            print('negative', val)")),
  "Structural Pattern Matching": b("`match subject:` / `case pattern:` (Python 3.10+) matches shapes and values.", "Replaces some long `if/elif` chains.", _c("def label(x):\n    match x:\n        case 0: return 'zero'\n        case str(s): return s.upper()\n        case _: return 'other'")),
  "Common Loop Patterns": b("Accumulate totals, search, filter, and transform data in loops.", "Know these before reaching for heavy libraries.", _c("total = sum(x for x in [1,2,3])\nprint(total)")),
  "Infinite Loops and Safety": b("A `while True` loop needs a clear `break` or exit condition.", "Add timeouts or counters in production systems.", _c("attempts = 0\nwhile attempts < 3:\n    attempts += 1\n    print('try', attempts)")),
}
CH3_BP = bp(["Prefer `for` over `while` when iterating collections", "Avoid deep nesting — extract functions"])
CH3_CM = cm([("Infinite while", "Forgot to update loop variable", "Check exit condition")])

CH4 = {
  "Why Functions Exist": b("Functions group reusable logic under a name — **Don't Repeat Yourself**.", "Change behavior in one place instead of many copy-pasted blocks.", _c("def area(w, h):\n    return w * h\nprint(area(3, 4), area(5, 2))")),
  "Defining and Calling Functions": b("Define with `def name(params):` and call with `name(args)`.", "Definition creates the function; call executes it.", _c("def greet(name):\n    return f'Hi, {name}'\nprint(greet('Sam'))")),
  "Parameters vs Arguments": b("**Parameters** appear in the `def` line; **arguments** are values you pass at the call.", "Positional arguments match parameters in order.", _c("def power(base, exp):\n    return base ** exp\nprint(power(2, 8))")),
  "Return Values": b("`return` sends a value back; omitting it returns `None`.", "Return early to simplify logic.", _c("def abs_val(n):\n    if n < 0:\n        return -n\n    return n")),
  "Default Parameters": b("Defaults apply when an argument is omitted.", "Defaults evaluate once at definition — avoid mutable defaults.", _c("def greet(name, greeting='Hello'):\n    return f'{greeting}, {name}'")),
  "Keyword Arguments": b("Pass `name=value` to skip order.", "Improves readability for many parameters.", _c("greet(name='Ada', greeting='Hi')")),
  "Positional-Only and Keyword-Only Parameters": b("`/` marks positional-only parameters; `*` starts keyword-only parameters (PEP 570).", "Library APIs use this to prevent breaking changes.", _c("def f(a, b, /, c, *, d):\n    return a+b+c+d")),
  "*args and **kwargs": b("`*args` collects extra positional tuple; `**kwargs` extra keyword dict.", "Used in wrappers and decorators.", _c("def log(*args, **kwargs):\n    print(args, kwargs)")),
  "Scope and the LEGB Rule": b("Python looks up names: **L**ocal, **E**nclosing, **G**lobal, **B**uilt-in.", "Assignments create or update bindings in the innermost relevant scope.", _c("x = 'global'\ndef outer():\n    x = 'enclosing'\n    def inner():\n        print(x)\n    inner()\nouter()")),
  "global and nonlocal": b("`global` updates a module-level name; `nonlocal` updates a variable in an enclosing function.", "Prefer passing values explicitly when possible.", _c("def counter():\n    n = 0\n    def inc():\n        nonlocal n\n        n += 1\n        return n\n    return inc")),
  "Closures": b("Inner functions remember variables from enclosing scope.", "Power decorators and factories.", _c("def make_multiplier(k):\n    def mul(x):\n        return x * k\n    return mul\ndouble = make_multiplier(2)")),
  "Lambda Functions": b("`lambda args: expression` creates a small anonymous function.", "Use for short callbacks; use `def` for anything complex.", _c("nums = [1,2,3]\nprint(list(map(lambda x: x*x, nums)))")),
  "Docstrings and help()": b("A string literal right after `def` is the **docstring** — documentation for `help()` and IDEs.", "Describe parameters, return value, and raised errors.", _c("def add(a, b):\n    '''Return the sum of a and b.'''\n    return a + b\nhelp(add)")),
  "Type Hints": b("Annotations like `def f(x: int) -> str:` help static checkers.", "Not enforced at runtime in standard Python.", _c("def slugify(text: str) -> str:\n    return text.lower().replace(' ', '-')")),
  "Recursion": b("A function calls itself with a smaller problem until a base case.", "Use when problem is naturally recursive (trees).", _c("def fact(n):\n    return 1 if n <= 1 else n * fact(n-1)")),
  "First-Class Functions": b("Functions are objects — assign, store in lists, pass as arguments.", "Enables functional patterns.", _c("def apply(fn, x):\n    return fn(x)\nprint(apply(lambda v: v+1, 10))")),
  "Unpacking at the Call Site": b("`*sequence` and `**mapping` spread into positional and keyword arguments.", "Useful when arguments live in collections.", _c("def f(a, b):\n    return a+b\nprint(f(**{'a':1,'b':2}))")),
  "Mutable Default Arguments": b("Default values like `[]` are created **once** at function definition time.", "Shared mutable defaults cause bugs across calls.", _c("def bad(x, items=[]):\n    items.append(x)\n    return items\nprint(bad(1), bad(2))  # surprise!\ndef good(x, items=None):\n    if items is None: items = []\n    items.append(x)\n    return items")),
}
CH4_BP = bp(["Never use mutable default arguments", "Keep functions small and named clearly"])
CH4_CM = cm([("Mutable default `def f(x=[])`", "Shared list across calls", "Use `None` and create inside")])

CH5 = {
  "What Is a Data Structure?": b("A **data structure** is how you organize multiple values in memory (list, dict, set, tuple).", "The right structure makes code simpler and faster.", _c("users = [{'id':1,'name':'Ada'}]\nprint(users[0]['name'])")),
  "Choosing the Right Structure": b("Use **list** for ordered sequences, **dict** for lookups by key, **set** for uniqueness, **tuple** for fixed records.", "Pick based on operations you need most.", _c("tags = {'python', 'web'}\norder = ['first', 'second']\nlookup = {'ada': 98}")),
  "Lists": b("Ordered, mutable sequences in `[...]`.", "Workhorse collection type.", _c("nums = [1,2,3]\nnums.append(4)\nprint(nums[0], nums[-1])")),
  "List Methods Reference": b("Common methods: `.append`, `.extend`, `.insert`, `.pop`, `.sort`, `.reverse`.", "Most list methods mutate in place.", _c("items = [3,1,2]\nitems.sort()\nprint(items)")),
  "Slicing Sequences": b("`seq[start:stop:step]` extracts sub-sequences; stop is exclusive.", "Works on lists, tuples, and strings.", _c("a = [0,1,2,3,4]\nprint(a[1:4], a[::-1])")),
  "Tuples": b("Ordered, **immutable** sequences in `(...)`.", "Records, dict keys, return multiple values.", _c("point = (10, 20)\nx, y = point")),
  "Dictionaries": b("Hash map: unique keys → values.", "Fast lookup by key.", _c("user = {'name':'Sam','role':'admin'}\nprint(user.get('phone', 'n/a'))")),
  "Dictionary Methods and Patterns": b("Use `.get`, `.items`, `.setdefault`, and `.update` for safe, clear dict code.", "Iterate with `.items()` when you need both key and value.", _c("counts = {}\nfor word in ['a','b','a']:\n    counts[word] = counts.get(word, 0) + 1")),
  "Sets": b("Unordered collection of **unique** hashable items.", "Membership and deduplication.", _c("tags = {'py','web','py'}\nprint(tags, len(tags))")),
  "Set Operations": b("Union `|`, intersection `&`, difference `-`.", "Compare categories without nested loops.", _c("a, b = {1,2}, {2,3}\nprint(a & b, a | b)")),
  "Nested Structures": b("Lists of dicts, dicts of lists — model real JSON-like data.", "Access with chained `[][]` carefully.", _c("data = {'users':[{'id':1}]}\nprint(data['users'][0]['id'])")),
  "Copying: Shallow vs Deep": b("Assignment copies reference. `copy.copy` shallow; `copy.deepcopy` recursive.", "Nested mutations need deep copy.", _c("import copy\na = [[1]]\nb = copy.deepcopy(a)\na[0][0] = 9\nprint(b)")),
  "Sorting Data": b("`sorted(iterable)` returns new list; `.sort()` mutates list in place.", "Pass `key=` for custom order.", _c("print(sorted(['banana','apple'], key=len))")),
  "The collections Module": b("Specialized containers: `Counter`, `defaultdict`, `deque`.", "Stdlib batteries for common patterns.", _c("from collections import Counter\nprint(Counter('abracadabra').most_common(2))")),
}
CH5_BP = bp(["Use `.get()` on dicts for optional keys", "Choose tuple for fixed records"])
CH5_CM = cm([("Shallow copy nested list", "Shared inner objects", "Use `deepcopy`")])

CH6 = {
  "What Are Comprehensions?": b("Comprehensions build collections from iterables in one expression.", "More readable than manual append loops for transforms.", _c("squares = [n*n for n in range(5)]\nprint(squares)")),
  "Why Comprehensions Exist": b("They express map/filter logic declaratively.", "Idiomatic Python — reviewers expect them.", _c("evens = [n for n in range(10) if n % 2 == 0]")),
  "List Comprehensions": b("`[expr for item in iterable if cond]`.", "Filter with trailing `if`; ternary before `for`.", _c("names = ['ada','bob']\nupper = [n.upper() for n in names]")),
  "Filtering with if": b("Trailing `if` keeps items matching a condition.", "Equivalent to filter + list.", _c("nums = [1,2,3,4,5]\nprint([n for n in nums if n % 2])")),
  "Conditional Expressions in Comprehensions": b("`[a if cond else b for x in xs]` chooses per item.", "Do not confuse with filter `if`.", _c("labels = ['even' if n%2==0 else 'odd' for n in range(4)]")),
  "Dict Comprehensions": b("`{k: v for ...}` builds dicts.", "Invert or transform mappings.", _c("nums = [1,2,3]\nprint({n: n*n for n in nums})")),
  "Set Comprehensions": b("`{expr for ...}` — unique results.", "Deduplicate while transforming.", _c("print({len(w) for w in ['hi','hey','yo']})")),
  "Generator Expressions": b("`(expr for ...)` is lazy — one item at a time.", "Save memory on large data.", _c("total = sum(n*n for n in range(1000000))\nprint(total)")),
  "Nested Comprehensions": b("Loops read left-to-right like nested fors.", "Keep depth ≤ 2 for readability.", _c("matrix = [[1,2],[3,4]]\nflat = [x for row in matrix for x in row]")),
  "Comprehensions vs Loops": b("Use comprehension for simple transform/filter; loop for side effects.", "If you need `break`, use a loop.", _c("# side effect -> loop\nfor u in users:\n    send_email(u)")),
  "Comprehensions vs map and filter": b("`map`/`filter` return iterators; comprehensions are more Pythonic.", "Still useful with existing functions.", _c("print(list(map(str, [1,2,3])))")),
  "Walrus Operator in Comprehensions": b("`:=` assigns inside an expression (3.8+).", "Avoid repeating expensive calls.", _c("import random\nnums = [random.random() for _ in range(5)]\nfiltered = [y for x in nums if (y := round(x,2)) > 0.5]")),
  "Real-World Examples": b("Parse logs, normalize CSV rows, build lookup tables.", "Comprehensions shine in ETL scripts.", _c("rows = ['1,Ada','2,Bob']\nusers = {int(r.split(',')[0]): r.split(',')[1] for r in rows}")),
  "Performance and Memory": b("List comps build full list; generators stream.", "Profile before micro-optimizing.", _c("import sys\nprint(sys.getsizeof([n for n in range(1000)]))")),
  "Debugging Comprehensions": b("Expand to a loop temporarily to print intermediate values.", "Read inside-out: result, condition, source.", _c("# debug version\nout = []\nfor n in range(5):\n    if n % 2: out.append(n)\nprint(out)")),
  "Reading Comprehensions Aloud": b("Say: 'a list of EXPR for ITEM in ITER if COND'.", "Practice decoding others' code.", _c("result = [c.upper() for c in 'abc' if c != 'b']")),
}
CH6_BP = bp(["Prefer generator expressions for large streams", "Do not nest more than two levels"])
CH6_CM = cm([("Confusing filter if vs ternary", "Wrong output", "Filter after `for`; ternary before `for`")])

CH7 = {
  "What Is OOP?": b("**Object-oriented programming** bundles data and behavior in **objects**.", "Models real entities (User, Order, Cart).", _c("class Dog:\n    def speak(self):\n        return 'woof'")),
  "When to Use Classes in Python": b("Use classes when you have state + behavior together; otherwise functions may suffice.", "Dataclasses help data-only objects.", _c("# simple data -> dataclass later in chapter")),
  "Classes and Objects": b("A **class** is a blueprint; an **object** is an instance.", "Call `ClassName()` to construct.", _c("class Point:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\np = Point(1,2)")),
  "The __init__ Constructor and self": b("`__init__` initializes instance attributes; `self` is the instance.", "Every method receives `self` first.", _c("class User:\n    def __init__(self, name):\n        self.name = name")),
  "Instance vs Class Attributes": b("Instance attrs on `self`; class attrs shared by all instances.", "Mutable class attrs are shared — beware.", _c("class Config:\n    debug = False")),
  "Instance Methods": b("Functions on the class taking `self`.", "Define behavior that uses instance state.", _c("class Counter:\n    def __init__(self):\n        self.n = 0\n    def inc(self):\n        self.n += 1")),
  "Inheritance": b("Subclass extends superclass with `class Child(Parent):`.", "Reuse and specialize behavior.", _c("class Animal:\n    def speak(self):\n        return '...'\nclass Dog(Animal):\n    def speak(self):\n        return 'bark'")),
  "super() and Method Overriding": b("`super()` calls parent implementation.", "Override methods to customize; call `super()` to extend.", _c("class B(A):\n    def greet(self):\n        return super().greet() + '!'")),
  "Method Types: instance, class, static": b("`@classmethod` gets `cls`; `@staticmethod` no implicit first arg.", "Class methods for factories; static for utilities.", _c("class Math:\n    @staticmethod\n    def add(a,b):\n        return a+b")),
  "Encapsulation and Properties": b("Use `@property` for computed or validated attributes.", "Public API without exposing raw fields.", _c("class Circle:\n    def __init__(self, r):\n        self._r = r\n    @property\n    def area(self):\n        return 3.14 * self._r ** 2")),
  "Dataclasses": b("`@dataclass` auto-generates `__init__`, `__repr__`, etc.", "Less boilerplate for data containers.", _c("from dataclasses import dataclass\n@dataclass\nclass User:\n    name: str\n    active: bool = True")),
  "Magic (Dunder) Methods": b("Double-underscore methods customize operators and builtins.", "`__str__`, `__len__`, `__eq__` are common.", _c("class Vec:\n    def __init__(self, x,y):\n        self.x, self.y = x,y\n    def __repr__(self):\n        return f'Vec({self.x},{self.y})'")),
  "Abstract Base Classes": b("`abc.ABC` enforces subclasses implement methods.", "Define interfaces in larger systems.", _c("from abc import ABC, abstractmethod\nclass Repo(ABC):\n    @abstractmethod\n    def get(self, id): ...")),
  "Composition vs Inheritance": b("**Composition** builds objects from other objects; **inheritance** is-is-a.", "Favor composition when reuse is has-a.", _c("class Engine: ...\nclass Car:\n    def __init__(self):\n        self.engine = Engine()")),
  "Multiple Inheritance and MRO": b("Python supports multiple bases; **MRO** orders lookup.", "Keep hierarchies shallow; use mixins carefully.", _c("class A: pass\nclass B(A): pass\nprint(B.__mro__)")),
  "OOP Design Checklist": b("Ask: one responsibility? clear names? minimal public surface?", "Refactor when classes grow past ~200 lines.", _c("# sketch classes on paper before coding")),
}
CH7_BP = bp(["Prefer composition over deep inheritance", "Use dataclasses for plain data"])
CH7_CM = cm([("God object class", "Hard to test", "Split responsibilities")])

CH8 = {
  "Why Modules Matter": b("A **module** is a `.py` file; splitting code keeps projects maintainable.", "Large single files are hard to test and review.", _c("import math\nprint(math.sqrt(16))")),
  "What Is a Module?": b("Any `.py` file is importable by its module name.", "Reuse code across scripts and packages.", _c("# helpers.py\ndef slug(s):\n    return s.lower().replace(' ', '-')")),
  "Your First Import": b("`import module` loads code once and binds the name.", "Access attributes with dot notation.", _c("import datetime\nprint(datetime.date.today())")),
  "Import Styles Compared": b("Whole module, selective names, aliases, and wildcards.", "Explicit imports aid readability.", _c("import os\nfrom pathlib import Path\nimport json as js")),
  "The import Statement Deep Dive": b("Python searches `sys.path` and caches in `sys.modules`.", "First import runs top-level code once.", _c("import sys\nprint(sys.path[:3])")),
  "Aliasing and Selective Imports": b("`import numpy as np` and `from x import y`.", "Alias long package names.", _c("from collections import Counter as C\nprint(C('aab')))")),
  "When to Avoid import *": b("Wildcard dumps all public names into your namespace.", "Hides origins and breaks linters.", _c("from math import sqrt  # explicit\nprint(sqrt(9))")),
  "__name__ and the Script Entry Point": b("`__name__ == '__main__'` when file run directly.", "Guard script-only code.", _c("def main():\n    print('run')\nif __name__ == '__main__':\n    main()")),
  "How Python Finds Modules": b("Directories on `sys.path`, plus stdlib and site-packages.", "Wrong layout causes ModuleNotFoundError.", _c("import sys\nsys.path.insert(0, 'src')")),
  "What Is a Package?": b("A folder of modules with `__init__.py` (regular package).", "Hierarchical imports like `pkg.submod`.", _c("# mypkg/__init__.py\n# mypkg/utils.py")),
  "Package Layout and __init__.py": b("`__init__.py` marks package and can re-export API.", "Keep package imports stable.", _c("# mypkg/__init__.py\nfrom .utils import helper")),
  "Relative vs Absolute Imports": b("Absolute from project root; relative uses dots inside package.", "Use relative inside package internals.", _c("# from . import models\n# from ..common import util")),
  "Namespace Packages": b("PEP 420 packages without `__init__.py` spanning dirs.", "Plugin systems use namespace packages.", _c("# advanced — see docs.python.org")),
  "The __all__ Public API": b("List of names exported by `from mod import *`.", "Document public surface.", _c("__all__ = ['public_fn']\ndef public_fn(): ...")),
  "Circular Imports": b("A imports B while B imports A.", "Fix by extracting shared code or lazy imports.", _c("def get_a():\n    import a\n    return a")),
  "Standard Library Tour": b("Batteries included: os, pathlib, json, datetime, collections, etc.", "Read docs before pip installing.", _c("from pathlib import Path\nprint(Path('.').resolve())")),
  "Third-Party Packages and pip": b("Install with `pip install package` into active environment.", "Pin versions in requirements.txt.", _c("# pip install requests\n# import requests")),
  "Organizing a Real Project": b("Use `src/` layout, tests/, README, pyproject.toml.", "Predictable structure helps teams.", _c("# src/myproject/__init__.py\n# tests/test_app.py")),
}
CH8_BP = bp(["Prefer explicit imports", "Use `python -m package` to run modules"])
CH8_CM = cm([("Naming file random.py", "Shadows stdlib random", "Rename module")])

CH9 = {
  "Why File I/O Matters": b("Programs read config, logs, and user uploads from disk.", "Persistence survives process restarts.", _c("from pathlib import Path\np = Path('notes.txt')\nprint(p.exists())")),
  "Files vs File Objects": b("Open files return **file objects** with `.read()`, `.write()`, `.close()`.", "Always close files — use `with`.", _c("with open('out.txt','w') as f:\n    f.write('hi')")),
  "Opening Files with open()": b("`open(path, mode='r', encoding='utf-8')`.", "Text modes need encoding on Windows.", _c("with open('data.txt', encoding='utf-8') as f:\n    text = f.read()")),
  "File Modes Explained": b("`r` read, `w` write (truncate), `a` append, `x` exclusive create, `b` binary.", "Wrong mode corrupts or truncates data.", _c("with open('log.txt','a') as f:\n    f.write('line\\n')")),
  "The with Statement": b("Context manager closes file even on exceptions.", "Preferred over manual `close()`.", _c("with open('f.txt') as f:\n    data = f.read()")),
  "Reading Text Files": b("`.read()`, `.readline()`, `.readlines()` or iterate lines.", "Iterate large files line by line.", _c("with open('f.txt') as f:\n    for line in f:\n        print(line.strip())")),
  "Writing and Appending Text": b("`.write()` and `.writelines()`.", "Append mode preserves existing content.", _c("lines = ['a\\n','b\\n']\nwith open('f.txt','w') as f:\n    f.writelines(lines)")),
  "Encoding and Unicode": b("Specify `encoding='utf-8'` for text files.", "Avoid mojibake on international text.", _c("text = 'café'\nopen('u.txt','w',encoding='utf-8').write(text)")),
  "Line Endings and newline": b("`newline=''` lets Python normalize `\\r\\n` vs `\\n`.", "Important for cross-platform CSV.", _c("import csv\nwith open('r.csv',newline='') as f:\n    rows = list(csv.reader(f))")),
  "Binary Files": b("Mode `rb`/`wb` for images, pickles, compressed data.", "Do not decode binary as text.", _c("data = b'\\x00\\x01'\nwith open('b.bin','wb') as f:\n    f.write(data)")),
  "Path Handling with pathlib": b("`Path` objects replace `os.path` string juggling.", "Use `/` operator to join paths.", _c("from pathlib import Path\nroot = Path('project')\nprint(root / 'src' / 'app.py')")),
  "Working with JSON": b("`json.load`/`dump` for files; `loads`/`dumps` for strings.", "JSON keys are always strings.", _c("import json\nobj = {'ok': True}\nprint(json.dumps(obj))")),
  "Working with CSV": b("`csv` module reads/writes tabular text.", "Use `DictReader` for header rows.", _c("import csv\nwith open('t.csv',newline='') as f:\n    print(list(csv.reader(f)))")),
  "Reading Large Files Efficiently": b("Stream line-by-line or in chunks.", "Never `read()` multi-GB files into RAM.", _c("with open('big.log') as f:\n    for i, line in enumerate(f):\n        if i > 2: break\n        print(line[:80])")),
  "Copying, Moving, and Deleting": b("`shutil.copy`, `Path.rename`, `Path.unlink`.", "Automate file housekeeping.", _c("import shutil\nshutil.copy('a.txt', 'backup/a.txt')")),
  "Temporary Files and Directories": b("`tempfile` for safe scratch space.", "Cleaned up automatically.", _c("import tempfile\nwith tempfile.TemporaryDirectory() as d:\n    print(d)")),
  "Error Handling for I/O": b("Catch `FileNotFoundError`, `PermissionError`.", "Tell users what path failed.", _c("try:\n    open('missing.txt')\nexcept FileNotFoundError:\n    print('not found')")),
  "Context Managers Recap": b("Objects with `__enter__`/`__exit__` work with `with`.", "Files are the classic example.", _c("class Ctx:\n    def __enter__(self): return self\n    def __exit__(self, *a): pass")),
}
CH9_BP = bp(["Always specify UTF-8 for text", "Use pathlib for paths"])
CH9_CM = cm([("Forgetting encoding on Windows", "UnicodeDecodeError", "encoding='utf-8'")])

CH10 = {
  "Errors vs Exceptions": b("**Syntax errors** fail before run; **exceptions** occur at runtime.", "Exceptions can be caught and handled.", _c("try:\n    1/0\nexcept ZeroDivisionError:\n    print('handled')")),
  "How Exceptions Propagate": b("Uncaught exceptions bubble up the call stack.", "Tracebacks show the chain.", _c("def inner():\n    raise ValueError('bad')\ndef outer():\n    inner()")),
  "try / except Basics": b("Wrap risky code in `try`; handle in `except`.", "Recover or show friendly errors.", _c("try:\n    n = int('x')\nexcept ValueError:\n    n = 0")),
  "else and finally Clauses": b("`else` runs if no exception; `finally` always runs.", "Use `finally` for cleanup.", _c("try:\n    f = open('t.txt')\nexcept FileNotFoundError:\n    pass\nfinally:\n    print('done')")),
  "Catching Multiple Exceptions": b("Tuple of types or multiple `except` blocks.", "Catch specific types first.", _c("try:\n    risky()\nexcept (ValueError, TypeError) as e:\n    print(e)")),
  "Exception Objects and as": b("`except E as e` binds the instance.", "Log `e` or its args.", _c("try:\n    {}\nexcept KeyError as e:\n    print(repr(e))")),
  "Raising Exceptions": b("`raise ValueError('msg')` signals errors.", "Validate inputs early.", _c("def withdraw(amount):\n    if amount < 0:\n        raise ValueError('negative')")),
  "Custom Exception Classes": b("Subclass `Exception` for domain errors.", "Callers catch your type specifically.", _c("class PaymentError(Exception):\n    pass\nraise PaymentError('declined')")),
  "The Exception Hierarchy": b("Catch `Exception` broadly; subclass for precision.", "Do not catch `BaseException` unless you know why.", _c("print(issubclass(ValueError, Exception))")),
  "Re-raising and Exception Chaining": b("`raise` from `e` preserves context.", "Debugging across layers.", _c("try:\n    int('x')\nexcept ValueError as e:\n    raise RuntimeError('bad input') from e")),
  "Assertions": b("`assert cond, msg` for developer checks (can be disabled with -O).", "Not for user input validation.", _c("assert 2 + 2 == 4")),
  "EAFP vs LBYL": b("**Easier to ask forgiveness** — try/except; **look before you leap** — check first.", "Python culture prefers EAFP.", _c("try:\n    return d[key]\nexcept KeyError:\n    return default")),
  "Context Managers": b("`with` ensures setup/teardown.", "Files, locks, DB connections.", _c("with open('f.txt') as f:\n    use(f)")),
  "contextlib Utilities": b("`contextlib.contextmanager` builds managers from generators.", "Reuse cleanup patterns.", _c("from contextlib import contextmanager\n@contextmanager\ndef tag(name):\n    print(f'<{name}>')\n    yield\n    print(f'</{name}>')")),
  "Exceptions in Real Applications": b("Map errors to HTTP status or user messages.", "Log stack traces server-side only.", _c("def api_handler():\n    try:\n        return process()\n    except ValidationError as e:\n        return {'error': str(e)}, 400")),
  "Reading Tracebacks": b("Read **bottom** line first (where it started), then up.", "Search the message and line number.", _c("# practice reading Traceback in REPL")),
  "Exception Handling in APIs": b("Return structured errors; never bare 500 without logging.", "Consistent JSON error shape.", _c("{'error': {'code': 'NOT_FOUND', 'message': '...'}}")),
  "Logging Exceptions": b("Use `logging.exception` inside `except` to include traceback.", "Better than `print` in production.", _c("import logging\nlog = logging.getLogger(__name__)\ntry:\n    1/0\nexcept ZeroDivisionError:\n    log.exception('failed')")),
}
CH10_BP = bp(["Catch specific exceptions", "Use finally for cleanup"])
CH10_CM = cm([("Bare except:", "Hides bugs", "except Exception as e:")])

CH11 = {
  "Functions as First-Class Objects": b("Functions can be assigned and passed like any value.", "Foundation for decorators.", _c("def shout(s): return s.upper()\nfn = shout\nprint(fn('hi'))")),
  "Iterables vs Iterators": b("**Iterable** can produce iterator; **iterator** has `__next__`.", "for-loops use iterators under the hood.", _c("it = iter([1,2])\nprint(next(it), next(it))")),
  "The Iterator Protocol": b("Implement `__iter__` returning self and `__next__` raising StopIteration.", "Custom sequences and streams.", _c("class Count:\n    def __init__(self, n): self.n, self.i = n, 0\n    def __iter__(self): return self\n    def __next__(self):\n        if self.i >= self.n: raise StopIteration\n        self.i += 1; return self.i")),
  "Generator Functions and yield": b("`yield` pauses function preserving state.", "Lazy sequences without storing all values.", _c("def gen():\n    yield 1\n    yield 2\nprint(list(gen()))")),
  "Generator Expressions": b("`(x for x in it)` like list comp but lazy.", "Pass to `sum`, `max`, etc.", _c("print(sum(x*x for x in range(1000)))")),
  "yield from Delegation": b("`yield from subgen` delegates to another generator.", "Flatten nested iteration.", _c("def chain(a, b):\n    yield from a\n    yield from b")),
  "Sending Values to Generators": b("`.send(value)` injects into `yield` expression.", "Coroutine-style generators (advanced).", _c("def acc():\n    total = 0\n    while True:\n        x = yield total\n        if x is not None:\n            total += x\ng = acc(); next(g); print(g.send(10))")),
  "When to Use Generators": b("Large datasets, pipelines, infinite streams.", "Memory bounded processing.", _c("def read_chunks(path, size=1024):\n    with open(path,'rb') as f:\n        while chunk := f.read(size):\n            yield chunk")),
  "What Are Decorators?": b("Decorators wrap functions to add behavior without changing their code.", "Logging, auth, timing, caching.", _c("def deco(fn):\n    def wrapper(*a, **k):\n        return fn(*a, **k)\n    return wrapper")),
  "Writing Your First Decorator": b("Outer function returns wrapper that calls original.", "Apply with `@deco` above `def`.", _c("def log(fn):\n    def wrapper(*a, **k):\n        print('call', fn.__name__)\n        return fn(*a, **k)\n    return wrapper\n@log\ndef add(a,b): return a+b")),
  "Decorators with Arguments": b("Extra outer function returns the decorator.", "Configure decorator behavior.", _c("def repeat(n):\n    def deco(fn):\n        def wrapper(*a, **k):\n            for _ in range(n): fn(*a, **k)\n        return wrapper\n    return deco")),
  "functools.wraps": b("Copies metadata from wrapped function to wrapper.", "Preserves `__name__` and docstrings.", _c("from functools import wraps\ndef deco(fn):\n    @wraps(fn)\n    def wrapper(*a, **k):\n        return fn(*a, **k)\n    return wrapper")),
  "Stacking Decorators": b("Applied bottom-up: `@a @b def f` → `a(b(f))`.", "Order matters.", _c("@dec_a\n@dec_b\ndef f(): pass")),
  "Built-in Decorators": b("`@property`, `@classmethod`, `@staticmethod`.", "Language-supported patterns.", _c("class C:\n    @classmethod\n    def create(cls):\n        return cls()")),
  "Class Decorators": b("Classes can decorate functions or other classes.", "Rare but powerful.", _c("class Tag:\n    def __init__(self, t): self.t = t\n    def __call__(self, fn):\n        return fn")),
  "contextlib.contextmanager": b("Decorator turning generator into context manager.", "Simpler than class-based managers.", _c("from contextlib import contextmanager\n@contextmanager\ndef opened(path):\n    f = open(path)\n    try:\n        yield f\n    finally:\n        f.close()")),
  "The itertools Module": b("Iterator algebra: `chain`, `islice`, `groupby`, etc.", "Express combinatorics without nested loops.", _c("from itertools import islice\nprint(list(islice(range(10), 3)))")),
  "functools Beyond Decorators": b("`partial`, `lru_cache`, `reduce`.", "Reuse and memoization.", _c("from functools import lru_cache\n@lru_cache\ndef fib(n):\n    return n if n < 2 else fib(n-1)+fib(n-2)")),
  "More itertools Recipes": b("See `itertools` docs recipes section.", "Professional one-liners for streams.", _c("from itertools import accumulate\nprint(list(accumulate([1,2,3,4])))")),
}
CH11_BP = bp(["Always use functools.wraps", "Generators for large data"])
CH11_CM = cm([("Decorator forgetting return wrapper", "Replaces function with None", "return wrapper")])

CH12 = {
  "Why Virtual Environments Exist": b("Isolate dependencies per project.", "Avoid version conflicts globally.", _c("# python -m venv .venv")),
  "System Python vs Project Python": b("OS Python is shared; venv has own `site-packages`.", "Never pip install globally for apps.", _c("import sys\nprint(sys.prefix)")),
  "Creating a venv with venv": b("`python -m venv .venv` creates a folder.", "Commit `.venv` to gitignore, not repo.", _c("# python -m venv .venv")),
  "Activating and Deactivating": b("Activate sets PATH to venv python; `deactivate` restores.", "Must activate each new shell.", _c("# Windows: .venv\\Scripts\\activate\n# Unix: source .venv/bin/activate")),
  "What Changes Inside a venv": b("`python`, `pip`, and `site-packages` point inside `.venv`.", "Imports resolve to installed packages there.", _c("import site\nprint(site.getsitepackages())")),
  "Introduction to pip": b("**pip** installs packages from PyPI.", "Comes with Python — upgrade occasionally.", _c("python -m pip --version")),
  "Installing and Uninstalling Packages": b("`pip install pkg` and `pip uninstall pkg`.", "Install into active environment only.", _c("python -m pip install requests")),
  "Version Specifiers": b("`==`, `>=`, `~=` in requirements pin compatibility.", "Reproducible builds need pins.", _c("# requests>=2.28,<3")),
  "requirements.txt": b("List of packages for `pip install -r requirements.txt`.", "Share with team and CI.", _c("# requirements.txt\nrequests==2.31.0")),
  "Lock Files and Reproducibility": b("Exact pins or tools like `pip-tools`/`uv` lock transitive deps.", "Production deploys need determinism.", _c("pip freeze > requirements.lock")),
  "pyproject.toml and Modern Packaging": b("PEP 518 project metadata and build backend.", "Standard for new libraries.", _c("# [project]\n# name = 'myapp'\n# version = '0.1.0'")),
  "Editable Installs": b("`pip install -e .` links source for development.", "Edit code without reinstalling.", _c("pip install -e .")),
  "pip list, show, and freeze": b("Inspect installed packages.", "Debug wrong versions.", _c("pip list\npip show requests")),
  "Upgrading pip and Packages": b("`python -m pip install -U pip`.", "Stay current for security fixes.", _c("python -m pip install -U pip")),
  "Security: pip audit": b("Scan dependencies for known CVEs.", "Run in CI pipelines.", _c("pip install pip-audit\npip-audit")),
  ".gitignore for Python Projects": b("Ignore `.venv/`, `__pycache__/`, `*.pyc`, `.env`.", "Keep secrets out of git.", _c("# .gitignore\n.venv/\n__pycache__/")),
  "Multiple Python Versions": b("Use `py -3.12` on Windows or `python3.11` on Linux.", "pyenv/asdf manage many versions.", _c("py -0p  # list installed")),
  "pip vs conda vs uv": b("pip is default; conda for scientific stacks; uv is fast modern installer.", "Pick one workflow per project.", _c("# team standard: venv + pip")),
  "End-to-End Project Workflow": b("venv → activate → pip install -r requirements → run tests.", "Document steps in README.", _c("# README quickstart commands")),
}
CH12_BP = bp(["One venv per project", "Pin dependencies for production"])
CH12_CM = cm([("Installing globally", "Breaks other projects", "Always activate venv first")])

CH13 = {
  "The Zen of Python": b("Run `import this` for design principles.", "Readability counts.", _c("import this")),
  "Readability and Maintainability": b("Code is read more than written.", "Clear beats clever.", _c("# prefer explicit names over cryptic abbreviations")),
  "PEP 8 Style Guide": b("Official conventions for layout and naming.", "Use black/ruff to automate.", _c("# 4 spaces, two blank lines between top-level defs")),
  "Naming Conventions": b("snake_case functions, CapWords classes, UPPER constants.", "Consistency across modules.", _c("MAX_RETRIES = 3\ndef fetch_data(): ...")),
  "Imports and Module Structure": b("stdlib, third-party, local — blank line between groups.", "Absolute imports preferred.", _c("import os\nfrom pathlib import Path\nfrom myapp import utils")),
  "Formatting Tools: black and ruff": b("Auto-format and lint.", "Run in CI and pre-commit.", _c("# ruff check .\n# black .")),
  "Type Hints Fundamentals": b("Annotate parameters and returns.", "mypy catches bugs early.", _c("def greet(name: str) -> str:\n    return f'Hi {name}'")),
  "Static Analysis with mypy": b("Type checker without running code.", "Add gradually to legacy projects.", _c("# mypy src/")),
  "Project Layout Patterns": b("src layout, tests beside or under tests/.", "Document in README.", _c("src/myapp/__init__.py")),
  "Documentation and Docstrings": b("Google or NumPy docstring styles.", "Generate docs with Sphinx/MkDocs.", _c('def fn():\n    """One-line summary.\n\n    Args:\n        x: description\n    """')),
  "Testing with pytest": b("Functions named `test_*` discovered automatically.", "Assertions use plain `assert`.", _c("def test_add():\n    assert add(1,2) == 3")),
  "Fixtures and Test Organization": b("`@pytest.fixture` shares setup.", "Keep tests fast and isolated.", _c("import pytest\n@pytest.fixture\ndef user():\n    return {'id':1}")),
  "Logging vs print": b("`logging` levels and handlers for production.", "print is for quick debugging only.", _c("import logging\nlogging.basicConfig(level=logging.INFO)\nlogging.info('started')")),
  "Configuration and Secrets": b("Environment variables via `os.environ` or `.env` files.", "Never commit API keys.", _c("import os\napi_key = os.environ['API_KEY']")),
  "Error Handling Discipline": b("Catch specific exceptions; log context.", "Fail fast on programmer errors.", _c("except ValueError as e:\n    logger.warning('bad input %s', e)")),
  "Performance: Measure First": b("Profile with `cProfile` before optimizing.", "Big-O beats micro-opts.", _c("import cProfile\ncProfile.run('sum(range(100000))')")),
  "Security Basics": b("No `eval` on user input; validate paths; use HTTPS.", "Dependabot/pip-audit for deps.", _c("path = user_input  # validate before open")),
  "Code Review Checklist": b("Tests pass, types check, docs updated, no secrets.", "Review for design not just style.", _c("# PR template checklist")),
  "Best Practices Summary Table": b("See chapter summary table.", "Revisit when starting new repos.", _c("# team wiki link")),
  "Pre-commit Hooks": b("Run ruff/black/tests before each commit.", "Catches issues early.", _c("# .pre-commit-config.yaml hooks")),
}
CH13_BP = bp(["Automate format and lint", "Write tests for new features"])
CH13_CM = cm([("Skipping tests", "Regressions ship", "pytest on every PR")])

CH14 = {
  "How to Prepare": b("Spaced repetition, timed practice, mock interviews.", "Consistency beats cramming.", _c("# 4-week plan: fundamentals → patterns → mocks")),
  "Study Plan by Week": b("Week1 syntax, week2 collections/OOP, week3 I/O/exceptions, week4 patterns.", "Track weak topics.", _c("topics = ['dict','closure','async']\nprint(topics)")),
  "Language Fundamentals Review": b("Types, control flow, functions, comprehensions.", "Flashcards for truthiness and mutability.", _c("assert [] is not None")),
  "Data Structures Deep Dive": b("Know list/dict/set ops and complexity.", "Two-sum uses hash map.", _c("def two_sum(nums, target):\n    seen = {}\n    for i, n in enumerate(nums):\n        if target-n in seen: return [seen[target-n], i]\n        seen[n] = i")),
  "Time and Space Complexity": b("Big-O for loops, dict lookup O(1) average.", "Mention tradeoffs aloud.", _c("# nested loop O(n^2)\n# dict lookup O(1) avg")),
  "Functions, Closures, and Scope": b("LEGB, closures, decorators basics.", "Explain mutable default trap.", _c("def make():\n    xs = []\n    def add(x):\n        xs.append(x)\n        return xs\n    return add")),
  "OOP Interview Topics": b("Inheritance vs composition, dunder methods, dataclasses.", "When not to use classes.", _c("@dataclass\nclass Point:\n    x: int; y: int")),
  "Modules, I/O, and Exceptions": b("import styles, with open, try/except.", "Design error responses.", _c("if __name__ == '__main__': main()")),
  "Decorators and Generators Q&A": b("Explain yield and @wraps.", "Iterator vs iterable.", _c("@lru_cache\ndef fib(n): ...")),
  "Environment and Tooling Questions": b("venv, pip, pytest, mypy.", "How you ship safely.", _c("python -m venv .venv")),
  "Coding Patterns": b("Two-pointer, sliding window, BFS/DFS basics.", "Practice on LeetCode easy/medium.", _c("def bfs(start, neighbors):\n    seen = {start}; q = [start]")),
  "Standard Library in Interviews": b("collections.Counter, heapq, bisect, itertools.", "Do not reinvent poorly.", _c("from collections import deque\nq = deque([1])")),
  "Python Gotchas": b("Mutable defaults, late binding closures, is vs ==.", "Shows experience.", _c("def f(x, items=None):\n    if items is None: items = []")),
  "System Design for Python Backends": b("WSGI/ASGI, workers, caching, DB pooling.", "High-level boxes and data flow.", _c("# Django/FastAPI + Postgres + Redis sketch")),
  "Behavioral and Communication Tips": b("Think aloud, clarify inputs, test examples.", "Interviewers grade process.", _c("# STAR stories prepared")),
  "Mock Interview Questions": b("Practice 20 common questions out loud.", "Record yourself.", _c("Q: GIL? A: allows one thread bytecode at a time...")),
  "Practice Problems with Solutions": b("Implement FizzBuzz, anagram check, flatten list.", "Time-box 25 minutes.", _c("def flatten(nested):\n    for x in nested:\n        if isinstance(x, list): yield from flatten(x)\n        else: yield x")),
  "Resources": b("docs.python.org, Real Python, official tutorials.", "Avoid outdated Python 2 material.", _c("print('https://docs.python.org/3/')")),
  "Course Review Checklist": b("Re-read summaries ch1-13.", "Redo exercises you skipped.", _c("checklist = ['types','oop','exceptions']\nprint(len(checklist))")),
  "Day-Before Checklist": b("Sleep, light review, no new topics.", "Prepare questions for interviewer.", _c("print('rest + confidence')")),
  "Additional Verbal Q&A": b("Explain list vs tuple, GIL at high level, pickle risks.", "Short crisp answers.", _c("# practice 60-second answers")),
}
CH14_BP = bp(["Explain thought process", "Write clean code before optimizing"])
CH14_CM = cm([("Silence during interview", "Interviewer cannot help", "Think aloud")])
