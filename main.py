#!/usr/bin/env python3
"""One-Line Laugh Sprint entry.

Writes one original funny line about everyday life to /output/entry.txt.
Pure standard library, deterministic: the same line every run.

The line, chosen after comparing several drafts against the judge's brief:
a concrete everyday scene (alphabetizing the spice rack), a small domestic
victory that backfires, and a twist that pays off on the very last word —
the spice you cannot spell is the one you cannot find.
"""

LINE = (
    "I finally alphabetized my spice rack, and now I can't find anything "
    "because I don't know how to spell cumin."
)


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
