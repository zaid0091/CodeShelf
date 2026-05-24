"""Extract Chapter 4 markdown from parent transcript and split into 6 parts."""
import json
import os
import re

TRANSCRIPT = r"C:\Users\User\.cursor\projects\d-Mydocs-CodeShelf\agent-transcripts\f807f7a5-2787-40b5-87b0-c4c6c8e68d3f\f807f7a5-2787-40b5-87b0-c4c6c8e68d3f.jsonl"
OUT_DIR = r"d:\Mydocs\CodeShelf\scripts"

SPLITS = [
    ("_ch04_part1.md", "## What is a Function?", "## Parameters and Arguments"),
    ("_ch04_part2.md", "## Parameters and Arguments", "## Scope"),
    ("_ch04_part3.md", "## Scope", "## Higher-Order Functions"),
    ("_ch04_part4.md", "## Higher-Order Functions", "## Real-World Functional Patterns"),
    ("_ch04_part5.md", "## Real-World Functional Patterns", "## Best Practices"),
    ("_ch04_part6.md", "## Best Practices", None),
]

PART6_FOOTER = """---

**Previous:** [Chapter 3: Operators & Control Flow](./ch03-operators-and-control-flow.md) · **Next:** [Chapter 5: Arrays & Objects](./ch05-arrays-and-objects.md)

**➡️ [Next Chapter: Arrays & Objects →](./ch05-arrays-and-objects.md)"""


def extract_md():
    with open(TRANSCRIPT, "r", encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            if obj.get("role") != "user":
                continue
            text = obj["message"]["content"][0]["text"]
            if "use this content" not in text or "Chapter 4: Functions" not in text:
                continue
            m = re.search(r'```md\n(.*?)```"', text, re.DOTALL)
            if not m:
                m = re.search(r'```md\n(.*)', text, re.DOTALL)
            if not m:
                raise SystemExit("Could not find ```md block")
            md = m.group(1)
            if md.endswith('```'):
                md = md[:-3].rstrip()
            return md
    raise SystemExit("Chapter 4 message not found")


def slice_content(full: str, start: str, end: str | None) -> str:
    i = full.index(start)
    if end is None:
        chunk = full[i:]
    else:
        j = full.index(end, i + 1)
        chunk = full[i:j].rstrip() + "\n"
    chunk = re.sub(r"<!--\s*CH04_PART\d+\s*-->\s*\n?", "", chunk)
    chunk = re.sub(
        r">\s*➡️\s*\*\*Next Chapter: Objects and Prototypes.*?\*\*",
        "",
        chunk,
        flags=re.DOTALL,
    )
    return chunk.rstrip() + "\n"


def main():
    full = extract_md()
    # Body only: from first ## What is a Function? (skip frontmatter/TOC in full doc)
    start_body = full.index("## What is a Function?")
    body = full[start_body:]

    counts = {}
    for filename, start, end in SPLITS:
        chunk = slice_content(body, start, end)
        if filename == "_ch04_part6.md":
            chunk = chunk.rstrip() + "\n\n" + PART6_FOOTER + "\n"
        path = os.path.join(OUT_DIR, filename)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(chunk)
        counts[filename] = chunk.count("\n") + (0 if chunk.endswith("\n") else 1)

    print("Line counts:")
    for name, n in counts.items():
        print(f"  {name}: {n}")
    print(f"  TOTAL: {sum(counts.values())}")


if __name__ == "__main__":
    main()
