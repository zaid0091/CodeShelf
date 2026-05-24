"""Shared helpers for Python course chapter generation."""
from __future__ import annotations

import re


def fm(title: str, desc: str, order: int, tags: list[str]) -> str:
    t = ", ".join(tags)
    return f"""---
title: {title}
description: {desc}
order: {order}
tags: [{t}]
---

"""


def anchor(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def toc(items: list[str]) -> str:
    lines = ["## Table of Contents\n", "\n"]
    for i, title in enumerate(items, 1):
        lines.append(f"{i}. [{title}](#{anchor(title)})\n")
    lines.append("\n---\n\n")
    return "".join(lines)


def welcome(text: str) -> str:
    return (
        f"> **{text}**\n"
        "> Take your time with each section — understanding beats speed.\n\n---\n\n"
    )


def section(title: str, body: str) -> str:
    return f"## {title}\n\n{body}\n\n---\n\n"


def subsection(title: str, body: str) -> str:
    return f"### {title}\n\n{body}\n\n"


def defn(text: str) -> str:
    return f"> **Definition:** {text}\n\n"


def interview_block(n: int, q: str, answer: str) -> str:
    return f"""> **📌 Interview Point {n}: {q}**

{answer}

---

"""


def interview_section(points: list[tuple[str, str]]) -> str:
    lines = [
        "## Interview Points\n\n",
        "Study these before technical interviews. Practice answering out loud in 60–90 seconds.\n\n---\n\n",
    ]
    for i, (q, a) in enumerate(points, 1):
        lines.append(interview_block(i, q, a))
    return "".join(lines)


def exercise_block(
    n: int,
    stars: str,
    title: str,
    task: str,
    hint: str,
    solution: str,
) -> str:
    return f"""### Exercise {n}: {title} {stars}

**Task:** {task}

<details>
<summary>💡 Hint (click to reveal)</summary>

{hint}

</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

{solution}

</details>

---

"""


def exercises_section(exs: list[tuple]) -> str:
    lines = [
        "## Exercises\n\n",
        "Try each exercise before opening the solution. Type the code yourself — muscle memory matters.\n\n---\n\n",
    ]
    for ex in exs:
        e = list(ex)
        while len(e) < 6:
            e.append("Build the solution in a `.py` file and run it with `python script.py`.")
        lines.append(exercise_block(*e[:6]))
    return "".join(lines)


def walkthrough(title: str, steps: list[str]) -> str:
    body = "\n".join(f"{i}. {s}" for i, s in enumerate(steps, 1))
    return subsection(title, body)


def mistakes_section(items: list[tuple[str, str, str]]) -> str:
    lines = [
        "## Common Mistakes\n\n",
        "| Mistake | Why it breaks | Fix |\n",
        "|---------|---------------|-----|\n",
    ]
    for m, why, fix in items:
        lines.append(f"| {m} | {why} | {fix} |\n")
    lines.append("\n---\n\n")
    return "".join(lines)


def summary_table(rows: list[tuple[str, str]]) -> str:
    lines = ["## Chapter Summary\n\n", "| Concept | Takeaway |\n", "|---------|----------|\n"]
    for k, v in rows:
        lines.append(f"| **{k}** | {v} |\n")
    lines.extend(
        [
            "\n### Key rules to remember\n\n",
            "```text\n",
            "✅ Read error messages — they name the line and problem\n",
            "✅ Type examples yourself instead of only reading\n",
            "✅ Use the REPL for one-line experiments\n",
            "❌ Do not copy-paste without understanding each line\n",
            "```\n\n---\n\n",
        ]
    )
    return "".join(lines)


def nav(
    prev: tuple[str, str] | None,
    nxt: tuple[str, str] | None,
) -> str:
    parts = ["## Previous / Next Chapter\n\n"]
    if prev:
        parts.append(f"**⬅️ [Previous: {prev[1]}](./{prev[0]})**\n\n")
    if nxt:
        parts.append(f"**➡️ [Next: {nxt[1]} →](./{nxt[0]})**\n\n")
    parts.append("---\n\n")
    return "".join(parts)
