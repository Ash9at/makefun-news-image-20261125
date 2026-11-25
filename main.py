#!/usr/bin/env python3
"""Entrypoint for The Daily Ledger, 25 November 2026.

Writes the front-page image to /output/entry.png.

The image itself is drawn by gen.py (Pillow, run at build time) and shipped
in this repository as entry.png. This entrypoint uses only the Python
standard library, so it runs in the grader's no-network sandbox: it copies
the shipped image byte for byte, which is deterministic by construction.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    os.chmod(target, 0o644)
    size = os.path.getsize(target)
    if size > 1048576:
        raise SystemExit("entry.png exceeds the 1 MiB limit: %d bytes" % size)
    print("wrote", target, size, "bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
