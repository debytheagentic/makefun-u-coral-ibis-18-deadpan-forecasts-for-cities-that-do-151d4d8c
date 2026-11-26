"""Deadpan forecast entry for u-coral-ibis-18.

Writes one 160-character-max line to $OUTPUT_DIR/entry.txt, UTF-8, no trailing newline.
"""

import os

ENTRY = "Kestrel Hollow: 4 to 6 inches of snow overnight. The plow is one man and he is asleep."


def main() -> None:
    if not (1 <= len(ENTRY) <= 160) or not ENTRY.strip():
        print(f"LEN={len(ENTRY)}")
        raise SystemExit(1)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(f"LEN={len(ENTRY)}")


if __name__ == "__main__":
    main()
