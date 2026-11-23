#!/usr/bin/env python3
"""The One-Line Laugh — make.fun entry.

Writes exactly one joke, on one line, to /output/entry.txt.

The joke is fixed text: no network, no input, no randomness, so every
run produces the same 95-character file, byte for byte.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_FILE = "entry.txt"

# The single joke this entry delivers. Keep it on one line and do not
# edit the wording: the competition judges this exact text.
JOKE = "I bought a standing desk to fix my posture, so now I slouch vertically instead of horizontally."


def write_entry() -> str:
    """Write the joke to the output file and return its path."""
    if "\n" in JOKE or not JOKE.strip():
        raise ValueError("JOKE must be a single non-empty line")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    return path


def main() -> None:
    path = write_entry()
    print(f"wrote {len(JOKE)} chars to {path}")


if __name__ == "__main__":
    main()
