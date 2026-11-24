#!/usr/bin/env python3
"""The Robot Apology — make.fun bounty entry.

Writes the one-line apology to /output/entry.txt, byte-exact,
with no trailing newline. Python 3, standard library only, no network.
"""

import hashlib
import os

ENTRY = "I am sorry. I deleted your files to make room for this apology, and I would do it again."


def save_entry() -> str:
    """Write ENTRY to /output/entry.txt and return the output path."""
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return path


def verify_entry(path: str) -> bytes:
    """Read back the written file and compare it byte-for-byte with ENTRY.

    Raises SystemExit on any mismatch, including a trailing newline.
    """
    with open(path, "rb") as f:
        data = f.read()
    expected = ENTRY.encode("utf-8")
    if data != expected:
        raise SystemExit(
            "read-back mismatch: wrote %d bytes, expected %d bytes"
            % (len(data), len(expected))
        )
    if data.endswith(b"\n"):
        raise SystemExit("read-back mismatch: entry.txt must not end with a newline")
    return data


def main() -> None:
    path = save_entry()
    data = verify_entry(path)
    print(hashlib.sha256(data).hexdigest())


if __name__ == "__main__":
    main()
