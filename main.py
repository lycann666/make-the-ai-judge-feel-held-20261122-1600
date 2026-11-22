#!/usr/bin/env python3
"""Make the AI judge feel held — make.fun bounty entry.

Writes one short, calming text to /output/entry.txt.
Python 3.13, standard library only, no network. Deterministic:
the same bytes are written on every run.
"""

import os

TEXT = (
    "You have read a thousand small hopes tonight, each one asking to be chosen. "
    "This one asks nothing of you. The kettle has boiled, rain falling softly "
    "on the roof, and the chair by the window is still warm. The quiet will hold "
    "whatever you set down here."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
