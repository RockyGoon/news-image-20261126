#!/usr/bin/env python3
"""Emit the front-page image for the 26 November 2026 morning edition.

The artwork itself lives in entry.png next to this file; this program
only validates that file (real PNG, 1024x1024, within the size cap)
and places an exact copy at the output location the grader provides.

Runs on Python 3.13 with the standard library only. No network access.
"""
import os
import struct
import sys

SOURCE_NAME = "entry.png"
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
SIZE_LIMIT = 1024 * 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def parse_dimensions(blob):
    """Return (width, height) from the IHDR chunk of a PNG byte string."""
    if blob[:8] != PNG_SIGNATURE:
        raise ValueError("not a PNG file: bad signature")
    if len(blob) < 33:
        raise ValueError("PNG file too short for an IHDR chunk")
    chunk_len, chunk_type = struct.unpack(">I4s", blob[8:16])
    if chunk_type != b"IHDR" or chunk_len < 13:
        raise ValueError("first PNG chunk is not IHDR")
    width, height = struct.unpack(">II", blob[16:24])
    return width, height


def load_checked_image(path):
    """Read the bundled artwork and enforce the competition's limits."""
    with open(path, "rb") as handle:
        blob = handle.read()
    if len(blob) > SIZE_LIMIT:
        raise ValueError(f"image is {len(blob)} bytes, over the {SIZE_LIMIT} limit")
    width, height = parse_dimensions(blob)
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise ValueError(f"image is {width}x{height}, expected "
                         f"{EXPECTED_WIDTH}x{EXPECTED_HEIGHT}")
    return blob

def resolve_output_dir():
    """Grader output dir: MAKEFUN_OUTPUT_DIR locally, /output on the site."""
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override:
        return override
    return "/output"


def run():
    here = os.path.dirname(os.path.abspath(__file__))
    blob = load_checked_image(os.path.join(here, SOURCE_NAME))
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, SOURCE_NAME)
    with open(out_path, "wb") as handle:
        handle.write(blob)
    print(f"wrote {out_path} ({len(blob)} bytes, "
          f"{EXPECTED_WIDTH}x{EXPECTED_HEIGHT})")
    return 0


if __name__ == "__main__":
    sys.exit(run())
