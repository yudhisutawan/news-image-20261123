#!/usr/bin/env python3
"""The World Today — front page for Monday 23 November 2026.

The picture is pre-rendered and stored in this repository as entry.png
(1024x1024, 48 stories: 2 leads, 1 banner, 15 tiles, 30 briefs).
This script only copies it to the output path, using nothing but the
Python standard library: no network, no clock, no randomness, so a
second run writes byte-identical output.
"""

import os
import shutil

SRC_NAME = "entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, SRC_NAME)
    if not os.path.isfile(src):
        raise SystemExit(f"missing pre-rendered picture: {src}")
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    dst = os.path.join(outdir, SRC_NAME)
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    print(f"wrote {dst} ({size} bytes)")


if __name__ == "__main__":
    main()
