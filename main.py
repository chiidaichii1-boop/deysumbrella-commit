#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes a single commit message (at most 100 characters) for a bug fix
that made everything worse, to /output/entry.txt.

The joke: the logout crash was "fixed" by making logout impossible,
so now nobody can ever leave. A real commit-subject voice, a fresh
angle on a repair that broke more than it mended.
"""

import os

ENTRY = "fix: crash on logout fixed, now nobody can leave"

# The gate requires 1 to 100 characters of non-whitespace text.
assert 1 <= len(ENTRY.strip()) <= 100, "entry must be 1-100 characters"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
