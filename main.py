"""Deadpan forecast entry for u-coral-ibis-18.

Writes one line, at most 160 characters, to $OUTPUT_DIR/entry.txt, UTF-8,
with no trailing newline. Exits non-zero when the line breaks the length gate.
"""

import os
import sys

# Write 2 of 2: the revised line — behavioural deadpan, punch last.
ENTRY = "Ostmere: 12 degrees, winds 30 km/h off the water, and a 60% chance the ferry runs anyway."


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    length = len(ENTRY)
    if not (1 <= length <= 160) or not ENTRY.strip():
        print(f"LEN={length}")
        return 1
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(f"LEN={length}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
