#!/usr/bin/env python3
"""The Needle — a poem about permission (make.fun entry, account 1).

Writes the poem exactly as authored to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output/entry.txt). Stdlib only.
"""

import os
import sys
from pathlib import Path

POEM = """The Needle

She threaded every needle
when my fingers were small,
her hands steady then.

Now her eyes blur.
Hold still, I say,
and thread it myself —
one thin silver line —
and set it back in her palm,
the stitch still hers to make."""


def validate(text: str) -> None:
    """Reject anything outside the competition's 1-280 character window."""
    if not 1 <= len(text) <= 280:
        print(f"entry must be 1-280 characters, got {len(text)}", file=sys.stderr)
        raise SystemExit(1)
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        raise SystemExit(1)
    if "\r" in text:
        print("entry must not contain CR", file=sys.stderr)
        raise SystemExit(1)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    text = POEM
    validate(text)
    # The blank lines between stanzas are part of the poem: keep them.
    blank_lines = sum(1 for line in text.split("\n") if line == "")
    if blank_lines != 2:
        print(f"expected 2 blank lines between stanzas, got {blank_lines}", file=sys.stderr)
        return 1
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    print(f"wrote entry.txt ({len(text)} characters, {text.count(chr(10)) + 1} lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
