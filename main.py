#!/usr/bin/env python3
"""Six Words, One Story — v1.

Writes one complete story in exactly six words to /output/entry.txt.
"""

import os

STORY = "Obituary printed. She read it twice."


def main():
    words = STORY.split()
    assert len(words) == 6, "story must be exactly six words, got %d" % len(words)
    assert 1 <= len(STORY.encode("utf-8")) <= 60, "story must be 1-60 characters"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
