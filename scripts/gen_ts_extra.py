"""Large supplemental sections per chapter to reach depth targets."""

from gen_ts_supplement_ch14 import CH14_QA

EXTRA_BY_FILE: dict[str, list[tuple[str, str]]] = {
    "ch14-interview-prep.md": [("Extended interview bank", CH14_QA)],
}


def get_extra(filename: str) -> list[tuple[str, str]]:
    from gen_ts_supplements_all import SUPPLEMENTS
    from gen_ts_walkthroughs import get_walkthrough

    out: list[tuple[str, str]] = []
    walk = get_walkthrough(filename)
    if walk.strip():
        out.append(("In-depth walkthroughs", walk))
    if filename in EXTRA_BY_FILE:
        out.extend(EXTRA_BY_FILE[filename])
    if filename in SUPPLEMENTS:
        out.append((f"Extended reference", SUPPLEMENTS[filename]))
    from gen_ts_more_supplements import MORE_BY_FILE

    if filename in MORE_BY_FILE:
        out.append(("More examples and patterns", MORE_BY_FILE[filename]))
    from gen_ts_depth import get_depth

    depth = get_depth(filename)
    if depth.strip():
        out.append(("Deep dive — worked examples", depth))
    from gen_ts_review import get_review

    review = get_review(filename)
    if review.strip():
        out.append(("Chapter review Q&A", review))
    return out
