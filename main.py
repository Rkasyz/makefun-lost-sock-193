"""Funniest Lost Sock Status Update — make.fun entry.

Writes one status update of at most 120 characters, in the voice of a
lost sock, to ``entry.txt`` in the output directory.

The program is deterministic: it writes the same bytes on every run,
with no time, no randomness and no network access.
"""

import os

ENTRY = (
    "Day 47 behind the dryer. The lint is friendly, the dark is total, "
    "and I have accepted I am a single sock now. Send help."
)

# The gate requires 1 to 120 characters of UTF-8 text, not only
# whitespace. This line is exactly 120 characters, counted twice by
# hand, and is a single line with no trailing newline in the file.
assert 1 <= len(ENTRY) <= 120
assert ENTRY.strip() == ENTRY
assert "\n" not in ENTRY and "\r" not in ENTRY


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
