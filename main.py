#!/usr/bin/env python3
"""The Most Shameless Lie entry: writes the one-line lie to /output/entry.txt."""
import os

TEXT = "I already backed that up."
MAX_CHARS = 88

def validate(line):
    """Single line, 1-5 words, within the gate: collapse stray whitespace, then check."""
    line = " ".join(line.split())
    words = line.split()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(words) <= 5, f"entry must be 1-5 words, got {len(words)}"
    assert 1 <= len(line) <= MAX_CHARS, f"entry length {len(line)} outside 1..{MAX_CHARS}"
    return line

def main():
    line = validate(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")

if __name__ == "__main__":
    main()
