#!/usr/bin/env python3
"""Copy entry.png beside this file to /output/entry.png, verifying it.

Python 3.13, standard library only. Outside the grader's container,
MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import hashlib
import os
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(SRC, "rb") as f:
        data = f.read()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        sys.exit("entry.png is not a PNG")
    # Gate cap: the image must stay under 1 MiB (1048576 bytes).
    if len(data) > 1048576:
        sys.exit(f"entry.png is {len(data)} bytes, over the 1 MiB cap")
    w, h = struct.unpack(">II", data[16:24])
    if (w, h) != (1024, 1024):
        sys.exit(f"entry.png is {w}x{h}, expected 1024x1024")
    with open(dst, "wb") as f:
        f.write(data)
    with open(dst, "rb") as f:
        copy_hash = hashlib.sha256(f.read()).hexdigest()
    if copy_hash != hashlib.sha256(data).hexdigest():
        sys.exit("copied entry.png hash mismatch")
    # Determinism note: main.py never generates pixels; it copies the
    # checked-in entry.png byte-for-byte, so two runs always agree.
    print(f"wrote {dst} ({len(data)} bytes, 1024x1024)")


if __name__ == "__main__":
    main()
