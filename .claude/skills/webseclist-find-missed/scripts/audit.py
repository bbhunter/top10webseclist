#!/usr/bin/env python3
"""Audit historical missed-technique ledgers and their curated-list projections."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
YEARS = range(2006, 2026)
WEIGHTS = {
    "Original contribution": 25,
    "Transferability": 20,
    "Lasting value": 20,
    "Technical soundness": 15,
    "Practical usability": 10,
    "Clarity and reproducibility": 10,
}
HEADING_RE = re.compile(
    r"^## (?P<score>\d+(?:\.\d+)?) — \[(?P<title>[^]]+)\]\((?P<url><[^>]+>|[^)]+)\)",
    re.MULTILINE,
)
FINAL_RE = re.compile(r"\*\*Final score:\s*(\d+(?:\.\d+)?)/100(?:\.)?\*\*")
ROW_RE = re.compile(
    r"^\|\s*(?P<label>[^|]+?)\s*\|\s*(?P<score>\d+(?:\.\d+)?)(?:/100)?\s*\|",
    re.MULTILINE,
)
SCORED_LIST_RE = re.compile(
    r"(?:judge|Score:)\s*\*{0,2}(\d+(?:\.\d+)?)/100", re.IGNORECASE
)


def year_file(year: int) -> Path:
    return ROOT / ("2016-17.md" if year in (2016, 2017) else f"{year}.md")


def blocks(markdown: str) -> list[tuple[re.Match[str], str]]:
    found = list(HEADING_RE.finditer(markdown))
    return [
        (match, markdown[match.start() : found[index + 1].start() if index + 1 < len(found) else None])
        for index, match in enumerate(found)
    ]


def latest_history(path: Path) -> dict[str, dict]:
    latest: dict[str, dict] = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_number}: invalid JSON: {exc}") from exc
        latest[event["candidate_id"]] = event
    return latest


def audit_year(year: int) -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    directory = ROOT / "ai-evaluation" / str(year)
    required = [directory / name for name in ("README.md", "judgements.md", "history.jsonl")]
    for path in required:
        if not path.is_file():
            errors.append(f"{year}: missing {path.relative_to(ROOT)}")
    if errors:
        return errors, {"cards": 0, "kept": 0, "low_band": 0}

    judgement_path = required[1]
    parsed_blocks = blocks(judgement_path.read_text(encoding="utf-8"))
    if not parsed_blocks:
        errors.append(f"{year}: no judgement scorecards")

    cards: dict[str, dict[str, object]] = {}
    for heading, block in parsed_blocks:
        url = heading.group("url").strip("<>")
        title = heading.group("title")
        displayed = float(heading.group("score"))
        if url in cards:
            errors.append(f"{year}: duplicate judgement URL {url}")
            continue

        rows = {match.group("label").strip(): float(match.group("score")) for match in ROW_RE.finditer(block)}
        missing = [label for label in WEIGHTS if label not in rows]
        if missing:
            errors.append(f"{year}: {title}: missing score rows: {', '.join(missing)}")
            continue
        # Match score.py's operation order exactly; mathematically equivalent
        # decimal-weight multiplication can round a binary midpoint differently.
        raw_final = 0.0
        for label, weight in WEIGHTS.items():
            raw_final += rows[label] / 100 * weight
        calculated = float(f"{raw_final:.1f}")
        finals = FINAL_RE.findall(block)
        if len(finals) != 1:
            errors.append(f"{year}: {title}: expected one final score, found {len(finals)}")
            continue
        final = float(finals[0])
        if displayed != calculated or final != calculated:
            errors.append(
                f"{year}: {title}: displayed/final/calculated "
                f"{displayed:.1f}/{final:.1f}/{calculated:.1f}"
            )
        status_match = re.search(r"\*\*(KEPT|REMOVED)\*\*", block)
        if not status_match:
            errors.append(f"{year}: {title}: missing KEPT/REMOVED status")
            continue
        decision = "kept" if status_match.group(1) == "KEPT" else "removed"
        cards[url] = {"score": calculated, "decision": decision, "title": title}

    history = latest_history(required[2])
    history_by_url = {event["primary_url"]: event for event in history.values()}
    if set(cards) != set(history_by_url):
        for url in sorted(set(cards) - set(history_by_url)):
            errors.append(f"{year}: judgement missing from latest history: {url}")
        for url in sorted(set(history_by_url) - set(cards)):
            errors.append(f"{year}: latest history missing from judgements: {url}")
    for url in sorted(set(cards) & set(history_by_url)):
        card = cards[url]
        event = history_by_url[url]
        if event["decision"] != card["decision"]:
            errors.append(
                f"{year}: {card['title']}: card/history decision "
                f"{card['decision']}/{event['decision']}"
            )
        if float(event["score"]) != float(card["score"]):
            errors.append(
                f"{year}: {card['title']}: card/history score "
                f"{card['score']}/{event['score']}"
            )

    list_text = year_file(year).read_text(encoding="utf-8")
    sections = list_text.split("## Missed from the original list")
    if len(sections) != 2:
        errors.append(f"{year}: expected exactly one missed section in {year_file(year).name}")
        missed = ""
    else:
        missed = sections[1]
        if "60 or above" not in missed.split("\n\n", 1)[0] + missed[:700]:
            errors.append(f"{year}: missed-section policy does not state 60 or above")

    for score_text in SCORED_LIST_RE.findall(missed):
        if float(score_text) < 60:
            errors.append(f"{year}: curated missed entry below 60: {score_text}")
    for url, card in cards.items():
        present = url in missed
        should_be_present = card["decision"] == "kept" and float(card["score"]) >= 60
        if should_be_present and not present:
            errors.append(f"{year}: kept judgement absent from missed section: {url}")
        if not should_be_present and present:
            errors.append(f"{year}: removed/below-gate judgement appears in missed section: {url}")

    kept = sum(card["decision"] == "kept" for card in cards.values())
    low_band = sum(
        card["decision"] == "kept" and 60 <= float(card["score"]) < 70
        for card in cards.values()
    )
    return errors, {"cards": len(cards), "kept": kept, "low_band": low_band}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("years", nargs="*", type=int, help="years to audit; defaults to 2006..2025")
    args = parser.parse_args()
    years = args.years or list(YEARS)
    invalid = [year for year in years if year not in YEARS]
    if invalid:
        parser.error(f"years outside 2006..2025: {', '.join(map(str, invalid))}")

    all_errors: list[str] = []
    totals = {"cards": 0, "kept": 0, "low_band": 0}
    for year in years:
        errors, counts = audit_year(year)
        all_errors.extend(errors)
        for key in totals:
            totals[key] += counts[key]
        state = "FAIL" if errors else "ok"
        print(
            f"{state:4} {year}: {counts['cards']} cards, {counts['kept']} kept, "
            f"{counts['low_band']} in 60-69.9"
        )

    if all_errors:
        print("\nAudit failures:", file=sys.stderr)
        for error in all_errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(
        f"audit valid: {len(years)} years, {totals['cards']} cards, "
        f"{totals['kept']} kept, {totals['low_band']} in 60-69.9"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
