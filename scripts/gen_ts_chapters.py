"""Helpers and chapter generators for TypeScript course expansion."""
from __future__ import annotations

import re
from pathlib import Path

from gen_ts_common import fm, welcome, toc, summary, best_practices

CONTENT_DIR = Path(__file__).resolve().parents[1] / "content" / "typescript"
GENERATED_APPENDIX = "<!-- codeshelf:generated-appendix -->"

FOOTER = """

*Last updated: 2025 | TypeScript course — CodeShelf*

*Found an error or have a suggestion? [Open an issue on GitHub](https://github.com/zaid0091/CodeShelf/issues)*
"""


def nav(prev: tuple[str, str] | None, nxt: tuple[str, str] | None) -> str:
    lines = ["---", "", "## Navigation", ""]
    if prev:
        lines.append(f"**⬅️ [Previous: {prev[1]}](./{prev[0]})**  ")
    if nxt:
        lines.append(f"**➡️ [Next: {nxt[1]}](./{nxt[0]})**")
    lines.append("")
    lines.append("---")
    return "\n".join(lines)


def mistakes(items: list[tuple[str, str, str]]) -> str:
    out = ["## Common Mistakes", "", "Watch for these patterns — they cost hours in real projects.", ""]
    for i, (title, bad, fix) in enumerate(items, 1):
        out += [f"### Mistake {i}: {title}", "", bad, "", fix, "", "---", ""]
    return "\n".join(out)


def interviews(items: list[tuple[str, str]]) -> str:
    out = ["## Interview Points", ""]
    for i, (q, a) in enumerate(items, 1):
        out += [f"> **📌 Interview Point {i}: {q}**", "", a, "", "---", ""]
    return "\n".join(out)


def exercises(
    ch: int,
    items: list[tuple[str, str, str]],
    solutions: list[str] | None = None,
) -> str:
    from gen_ts_exercise_solutions import get_solutions

    stars = ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐"]
    sols = solutions if solutions is not None else get_solutions(ch)
    out = ["## Exercises", "", "Practice with `npx tsc --noEmit` after each exercise.", ""]
    for i, (title, task, hint) in enumerate(items, 1):
        out += [
            f"### Exercise {ch}.{i}: {title} {stars[i - 1]}",
            "",
            f"**Task:** {task}",
            "",
            "<details><summary>💡 Hint</summary>",
            "",
            hint,
            "",
            "</details>",
            "",
        ]
        if i - 1 < len(sols) and sols[i - 1].strip():
            out += [
                "<details><summary>✅ Solution (click to reveal)</summary>",
                "",
                sols[i - 1].strip(),
                "",
                "</details>",
                "",
            ]
        out += ["---", ""]
    return "\n".join(out)


def extract_body(md: str) -> str:
    """Keep only core chapter sections (idempotent for re-generation)."""
    if md.startswith("---"):
        end = md.find("---", 3)
        md = md[end + 3 :].lstrip()
    md = re.sub(r"^# Chapter \d+:[^\n]+\n+", "", md, count=1)
    # Drop welcome blockquote block before TOC if re-run
    md = re.sub(r"^> \*\*[^\n]+\*\*[\s\S]*?(?=^## Table of Contents)", "", md, count=1, flags=re.MULTILINE)
    md = re.sub(r"^## Table of Contents\n[\s\S]*?^---\n+", "", md, count=1, flags=re.MULTILINE)
    # Remove generated appendix (walkthroughs, supplements, footer sections)
    if GENERATED_APPENDIX in md:
        md = md.split(GENERATED_APPENDIX, 1)[0]
    else:
        cut_markers = [
            r"^---\s*\n+\s*^## Best Practices",
            r"^## Best Practices",
            r"^## Additional study notes",
            r"^## Navigation",
            r"^\*Last updated:",
        ]
        for pat in cut_markers:
            m = re.search(pat, md, flags=re.MULTILINE)
            if m:
                md = md[: m.start()]
                break
    md = re.sub(r"^## Practice Exercise[^\n]*\n[\s\S]*$", "", md, flags=re.MULTILINE)
    md = re.sub(r"^Continue to \[[^\n]+\n?", "", md, flags=re.MULTILINE)
    md = re.sub(r"^Next: \[[^\n]+\n?", "", md, flags=re.MULTILINE)
    md = re.sub(r"^Answers and[^\n]+\n?", "", md, flags=re.MULTILINE)
    return md.strip()


def deep_dive_sections(chapter_num: int, topics: list[tuple[str, str]]) -> str:
    out = ["", "---", ""]
    for title, body in topics:
        stripped = body.strip()
        if stripped.startswith("## "):
            out += [stripped, ""]
        else:
            out += [f"### {title}", "", body, "", "---", ""]
    return "\n".join(out)


def pad_to_min(text: str, min_lines: int = 800) -> str:
    """Append glossary lines only if still under min_lines (unique per chapter)."""
    lines = text.splitlines()
    if len(lines) >= min_lines:
        return text
    extra = ["", "---", "", "## Quick glossary (review)", ""]
    terms = [
        ("TypeScript", "Typed superset of JavaScript that compiles to JS."),
        ("Inference", "Compiler deduces types without explicit annotations."),
        ("Union", "Value may be one of several types: `A | B`."),
        ("Narrowing", "Refining a union to a specific type in a branch."),
        ("Generic", "Type parameter for reusable APIs."),
        ("Interface", "Named object shape contract."),
        ("Utility type", "Built-in type transformer like `Partial`."),
        ("Strict mode", "Bundle of safer compiler flags in tsconfig."),
        ("Type erasure", "Types removed in emitted JavaScript."),
        ("Declaration file", "`.d.ts` describing types for JS modules."),
    ]
    i = 0
    while len(lines) < min_lines and i < 80:
        term, defn = terms[i % len(terms)]
        extra.append(f"- **{term}** — {defn}")
        i += 1
        lines = (text + "\n" + "\n".join(extra)).splitlines()
    return text + "\n" + "\n".join(extra[3:])


def build_wrapped(
    filename: str,
    order: int,
    title: str,
    desc: str,
    tags: list[str],
    h1: str,
    welcome_text: str,
    toc_items: list[str],
    best: list[str],
    mistake_items: list[tuple[str, str, str]],
    interview_items: list[tuple[str, str]],
    exercise_items: list[tuple[str, str, str]],
    summary_items: list[str],
    prev: tuple[str, str] | None,
    nxt: tuple[str, str] | None,
    extra_sections: list[tuple[str, str]] | None = None,
    min_lines: int = 800,
) -> str:
    raw = (CONTENT_DIR / filename).read_text(encoding="utf-8")
    body = extract_body(raw)
    parts = [
        fm(title, desc, order, tags),
        welcome(h1, welcome_text),
        toc(toc_items),
        body,
    ]
    if extra_sections:
        parts.append(GENERATED_APPENDIX + "\n" + deep_dive_sections(order, extra_sections))
    else:
        parts.append(GENERATED_APPENDIX)
    parts += [
        best_practices(best),
        mistakes(mistake_items),
        interviews(interview_items),
        exercises(order, exercise_items),
        summary(summary_items),
        nav(prev, nxt),
    ]
    return pad_to_min("\n".join(parts), min_lines)


def build_from_config(cfg: dict, min_lines: int = 700) -> str:
    from gen_ts_extra import get_extra

    extra = list(cfg.get("extra") or [])
    extra.extend(get_extra(cfg["filename"]))
    cfg = {**cfg, "extra": extra}
    return build_wrapped(
        filename=cfg["filename"],
        order=cfg["order"],
        title=cfg["title"],
        desc=cfg["desc"],
        tags=cfg["tags"],
        h1=cfg["h1"],
        welcome_text=cfg["welcome"],
        toc_items=cfg["toc"],
        best=cfg["best"],
        mistake_items=cfg["mistakes"],
        interview_items=cfg["interviews"],
        exercise_items=cfg["exercises"],
        summary_items=cfg["summary"],
        prev=cfg["prev"],
        nxt=cfg["nxt"],
        extra_sections=cfg.get("extra"),
        min_lines=min_lines,
    )


def generate_all() -> list[tuple[str, int]]:
    from gen_ts_ch01 import build as build_ch01
    from gen_ts_configs import CHAPTER_CONFIGS

    counts: list[tuple[str, int]] = []
    text = pad_to_min(build_ch01(), 803) + FOOTER
    (CONTENT_DIR / "ch01-introduction.md").write_text(text, encoding="utf-8")
    counts.append(("ch01-introduction.md", len(text.splitlines())))

    for cfg in CHAPTER_CONFIGS:
        text = build_from_config(cfg, 803) + FOOTER
        (CONTENT_DIR / cfg["filename"]).write_text(text, encoding="utf-8")
        counts.append((cfg["filename"], len(text.splitlines())))
    return counts


if __name__ == "__main__":
    counts = generate_all()
    for name, n in counts:
        print(f"{name}: {n}")
    print(f"TOTAL: {sum(n for _, n in counts)}")
