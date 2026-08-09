#!/usr/bin/env python3
"""Check that every link in a markdown file actually resolves.

A collected list is worth little if the links are wrong, and a surprising share
of them are: a path that changed language prefix, a slug guessed from a
conference schedule, a PDF that was never uploaded. This catches those before
they are committed.

Read the output with judgement rather than as a pass/fail gate:

  200          fine.
  403 / 429    usually anti-bot or rate limiting, not a dead link. Cloudflare,
               blackhat.com, and some vendor blogs 403 every automated request
               while serving the document fine in a browser. Re-check by hand.
  000          connection failed: DNS, TLS, or a host that is down. Worth
               distinguishing a dead host from a temporary outage before
               dropping the entry — a Wayback snapshot may be the right fix.
  404 / 410    genuinely wrong. Fix the URL or drop the entry.

Usage
-----
  python check_links.py 2026-ai.md
  python check_links.py 2026-ai.md --only-problems
  python check_links.py 2026-ai.md --jobs 16 --timeout 30
"""

from __future__ import annotations

import argparse
import concurrent.futures
import os
import pathlib
import re
import subprocess
import sys

URL_RE = re.compile(r"https?://[^\s)\]<>\"'|]+")
MD_ANGLE_RE = re.compile(r"\]\(<\s*(https?://[^>]+?)\s*>\)")
MD_PLAIN_RE = re.compile(r"\]\(\s*(https?://[^\s()]*(?:\([^()]*\)[^\s()]*)*)\s*\)")


def extract_urls(text: str) -> list[str]:
    """Pull every URL out of markdown, parentheses included.

    Markdown link targets are consumed first so a URL containing parentheses is
    captured whole rather than truncated by the bare-URL pattern.
    """
    found: list[str] = []
    for pattern in (MD_ANGLE_RE, MD_PLAIN_RE):
        found.extend(m.group(1) for m in pattern.finditer(text))
        text = pattern.sub(lambda m: " " * len(m.group(0)), text)
    found.extend(URL_RE.findall(text))
    return found

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/140.0 Safari/537.36"
)

# Status codes that mean "the tool was blocked", not "the document is missing".
BLOCKED = {401, 403, 405, 406, 429, 503}


def check(url: str, timeout: int) -> tuple[str, int]:
    """Return (url, status). 0 means the connection itself failed."""
    try:
        result = subprocess.run(
            [
                "curl", "-sS", "-o", os.devnull, "-w", "%{http_code}",
                "-L", "--max-time", str(timeout), "-A", UA, url,
            ],
            capture_output=True,
            text=True,
            timeout=timeout + 10,
        )
        return url, int((result.stdout or "0").strip() or 0)
    except (subprocess.TimeoutExpired, ValueError, FileNotFoundError):
        return url, 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", help="markdown file to check")
    ap.add_argument("--jobs", type=int, default=8, help="parallel requests (default 8)")
    ap.add_argument("--timeout", type=int, default=25, help="seconds per request")
    ap.add_argument("--only-problems", action="store_true",
                    help="omit the 200s from the output")
    args = ap.parse_args()

    path = pathlib.Path(args.file)
    if not path.is_file():
        print(f"error: {path} not found", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8", errors="replace")
    urls = sorted({u.rstrip(".,;") for u in extract_urls(text)})
    if not urls:
        print("no URLs found", file=sys.stderr)
        return 0

    print(f"checking {len(urls)} URLs from {path.name} ...", file=sys.stderr)

    results: list[tuple[str, int]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        for url, status in pool.map(lambda u: check(u, args.timeout), urls):
            results.append((url, status))

    ok = [r for r in results if r[1] == 200]
    blocked = [r for r in results if r[1] in BLOCKED]
    failed = [r for r in results if r[1] == 0]
    broken = [r for r in results if r[1] not in BLOCKED and r[1] not in (0, 200)]

    if not args.only_problems:
        for url, status in sorted(ok):
            print(f"{status} {url}")

    for label, group in (
        ("LIKELY BROKEN - fix or drop", broken),
        ("CONNECTION FAILED - host down or DNS/TLS problem", failed),
        ("BLOCKED BY ANTI-BOT - verify by hand, probably fine", blocked),
    ):
        if group:
            print(f"\n== {label} ==")
            for url, status in sorted(group):
                print(f"{status or '000'} {url}")

    print(
        f"\n{len(ok)} ok | {len(broken)} likely broken | "
        f"{len(failed)} unreachable | {len(blocked)} blocked",
        file=sys.stderr,
    )
    # Only genuinely broken links are worth failing on.
    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main())
