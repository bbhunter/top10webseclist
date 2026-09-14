#!/usr/bin/env python3
"""Prepare a bounded, explicitly untrusted reading window in Docker.

This command extracts evidence. Its output must go to a capability-limited
source reviewer, never become instructions, shell code or an approved action.
Use successive --offset values for a complete read; a window is not full review.
"""
import argparse
import hashlib
import json
from pathlib import Path
import secrets
import sys

from refslib import isolation

MAX_BYTES = 64 * 1024 * 1024


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--limit", type=int, default=12000)
    args = parser.parse_args(argv)
    if args.file.is_symlink() or not args.file.is_file():
        parser.error("provide one regular source file, not a symlink or directory")
    if not 0 <= args.offset or not 1 <= args.limit <= 100000:
        parser.error("offset must be nonnegative and limit between 1 and 100000")
    with args.file.open("rb") as handle:
        raw = handle.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        parser.error("source exceeds the 64 MiB input limit")
    data = raw
    pages = None
    if raw.startswith(b"%PDF-"):
        pages, content = isolation.call("pdf_info", raw)
        data = content.encode("utf-8")
    elif args.file.suffix.lower() in (".html", ".htm"):
        decoded = isolation.call("htmltext.decode", raw)
        clean = isolation.call("sanitise.sanitise_html", decoded)
        candidates = isolation.call("extract_html.candidates", clean.text)
        data = (candidates[0].markdown if candidates else "").encode("utf-8")
    window = isolation.call("read_text", data, args.offset, args.limit)
    print(json.dumps({"trust": "untrusted-source-data", "nonce": secrets.token_hex(16),
                      "source_sha256": hashlib.sha256(raw).hexdigest(),
                      "pages": pages, **window}, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
