#!/usr/bin/env python3
"""Append and verify immutable judgement events under ai-evaluation/<year>/.

The Markdown scorecards remain the readable report.  This JSONL is the audit
trail: importing the same scorecard twice is a no-op, while a changed judgement
appends a new event linked to the previous event for that candidate.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


SCHEMA = "webseclist-judgement-history/v1"
HEADING = re.compile(r"^## (?P<score>\d+(?:\.\d+)?) — (?P<body>.+)$", re.MULTILINE)
STATUS = re.compile(
    r"^\*\*(?P<decision>KEPT|REMOVED)\*\* · (?P<verdict>.+?) · confidence (?P<confidence>.+?)$",
    re.MULTILINE,
)
LINK = re.compile(r"\[(?P<label>[^\]]+)\]\((?P<url><[^>]+>|https?://[^\s)]+)\)")
DECISIONS = {"kept", "removed"}
EVENT_TYPES = {"baseline-import", "judgement", "rejudgement"}


class HistoryError(ValueError):
    pass


def repo_root() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "ai-evaluation").is_dir() and (parent / ".claude").is_dir():
            return parent
    raise HistoryError("could not find the repository root above the history script")


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def normalise_url(url: str) -> str:
    url = url.strip().strip("<>")
    parsed = urlsplit(url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        raise HistoryError("candidate URL must be an absolute HTTP(S) URL: %s" % url)
    path = parsed.path or "/"
    if path != "/":
        path = path.rstrip("/")
    return urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), path,
                       parsed.query, ""))


def candidate_id(url: str) -> str:
    return "url-sha256:" + sha256_text(normalise_url(url))


def relative_source(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def parse_markdown(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    headings = list(HEADING.finditer(text))
    parsed = []
    for position, match in enumerate(headings):
        end = headings[position + 1].start() if position + 1 < len(headings) else len(text)
        block = text[match.start():end].strip() + "\n"
        status = STATUS.search(block)
        links = list(LINK.finditer(match.group("body")))
        if not status:
            raise HistoryError("judgement at line %d has no KEPT/REMOVED status" %
                               (text.count("\n", 0, match.start()) + 1))
        if not links:
            raise HistoryError("judgement at line %d has no candidate link" %
                               (text.count("\n", 0, match.start()) + 1))
        primary = links[0]
        urls = [item.group("url").strip("<>") for item in links]
        parsed.append({
            "title": primary.group("label"),
            "primary_url": primary.group("url").strip("<>"),
            "related_urls": urls[1:],
            "score": float(match.group("score")),
            "verdict": status.group("verdict").strip(),
            "decision": status.group("decision").lower(),
            "confidence": status.group("confidence").strip(),
            "source_line": text.count("\n", 0, match.start()) + 1,
            "snapshot_sha256": sha256_text(block),
        })
    if not parsed:
        raise HistoryError("no judgement headings found in %s" % path)
    return parsed


def read_history(path: Path) -> list[dict]:
    if not path.exists():
        return []
    events = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as error:
            raise HistoryError("%s:%d is invalid JSON: %s" % (path, number, error))
        validate_event(event, "%s:%d" % (path, number))
        events.append(event)
    return events


def validate_event(event: dict, where: str = "event") -> None:
    required = {
        "schema", "event_id", "recorded_at", "event_type", "year",
        "candidate_id", "title", "primary_url", "related_urls", "score",
        "verdict", "decision", "confidence", "snapshot_sha256", "source",
        "supersedes",
    }
    missing = sorted(required - set(event))
    if missing:
        raise HistoryError("%s is missing %s" % (where, ", ".join(missing)))
    if event["schema"] != SCHEMA:
        raise HistoryError("%s has unsupported schema %r" % (where, event["schema"]))
    if event["decision"] not in DECISIONS:
        raise HistoryError("%s has invalid decision %r" % (where, event["decision"]))
    if event["event_type"] not in EVENT_TYPES:
        raise HistoryError("%s has invalid event_type %r" % (where, event["event_type"]))
    if not isinstance(event["score"], (int, float)) or not 0 <= event["score"] <= 100:
        raise HistoryError("%s score must be between 0 and 100" % where)
    if not isinstance(event["related_urls"], list):
        raise HistoryError("%s related_urls must be a list" % where)
    normalise_url(event["primary_url"])
    for url in event["related_urls"]:
        normalise_url(url)
    try:
        dt.datetime.fromisoformat(event["recorded_at"].replace("Z", "+00:00"))
    except (TypeError, ValueError):
        raise HistoryError("%s has invalid recorded_at" % where)
    identity = json.dumps({key: value for key, value in event.items() if key != "event_id"},
                          sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    expected = "sha256:" + sha256_text(identity)
    if event["event_id"] != expected:
        raise HistoryError("%s event_id does not match its content" % where)


def history_path(year: int, supplied: str | None, root: Path) -> Path:
    return Path(supplied).resolve() if supplied else root / "ai-evaluation" / str(year) / "history.jsonl"


def latest_by_candidate(events: list[dict]) -> dict[str, dict]:
    latest = {}
    for event in events:
        latest[event["candidate_id"]] = event
    return latest


def make_event(*, year: int, title: str, primary_url: str, related_urls: list[str],
               score: float, verdict: str, decision: str, confidence: str,
               snapshot_sha256: str, source_file: str, source_line: int,
               event_type: str, recorded_at: str, supersedes: str = "") -> dict:
    decision = decision.lower()
    event = {
        "schema": SCHEMA,
        "recorded_at": recorded_at,
        "event_type": event_type,
        "year": int(year),
        "candidate_id": candidate_id(primary_url),
        "title": title.strip(),
        "primary_url": primary_url.strip().strip("<>"),
        "related_urls": [url.strip().strip("<>") for url in related_urls],
        "score": float(score),
        "verdict": verdict.strip(),
        "decision": decision,
        "confidence": confidence.strip(),
        "snapshot_sha256": snapshot_sha256,
        "source": {"file": source_file, "line": int(source_line)},
        "supersedes": supersedes,
    }
    identity = json.dumps(event, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    event["event_id"] = "sha256:" + sha256_text(identity)
    validate_event(event)
    return event


def append_events(path: Path, additions: list[dict]) -> None:
    if not additions:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        for event in additions:
            handle.write(json.dumps(event, sort_keys=True, ensure_ascii=False,
                                    separators=(",", ":")) + "\n")


def command_import(args) -> int:
    root = repo_root()
    source = Path(args.file).resolve()
    destination = history_path(args.year, args.history, root)
    events = read_history(destination)
    latest = latest_by_candidate(events)
    additions = []
    recorded_at = args.recorded_at or utc_now()
    source_file = relative_source(source, root)
    judgements = parse_markdown(source)
    for judgement in judgements:
        identifier = candidate_id(judgement["primary_url"])
        previous = latest.get(identifier)
        if previous and previous["snapshot_sha256"] == judgement["snapshot_sha256"]:
            continue
        event = make_event(
            year=args.year,
            title=judgement["title"],
            primary_url=judgement["primary_url"],
            related_urls=judgement["related_urls"],
            score=judgement["score"],
            verdict=judgement["verdict"],
            decision=judgement["decision"],
            confidence=judgement["confidence"],
            snapshot_sha256=judgement["snapshot_sha256"],
            source_file=source_file,
            source_line=judgement["source_line"],
            event_type=args.event_type,
            recorded_at=recorded_at,
            supersedes=previous["event_id"] if previous else "",
        )
        additions.append(event)
        latest[identifier] = event
    append_events(destination, additions)
    print("%d judgement event(s) appended, %d unchanged; %s" %
          (len(additions), len(judgements) - len(additions),
           relative_source(destination, root)))
    return 0


def command_record(args) -> int:
    root = repo_root()
    destination = history_path(args.year, args.history, root)
    events = read_history(destination)
    identifier = args.candidate_id or candidate_id(args.url)
    latest = latest_by_candidate(events)
    previous = latest.get(identifier)
    snapshot = sha256_text(json.dumps({
        "title": args.title, "url": normalise_url(args.url), "related": args.related_url,
        "score": float(args.score), "verdict": args.verdict,
        "decision": args.decision.lower(), "confidence": args.confidence,
        "note": args.note or "",
    }, sort_keys=True, ensure_ascii=False))
    if previous and previous["snapshot_sha256"] == snapshot:
        print("0 judgement event(s) appended, 1 unchanged; %s" %
              relative_source(destination, root))
        return 0
    event = make_event(
        year=args.year, title=args.title, primary_url=args.url,
        related_urls=args.related_url, score=args.score, verdict=args.verdict,
        decision=args.decision, confidence=args.confidence,
        snapshot_sha256=snapshot, source_file=args.source, source_line=args.line,
        event_type="judgement", recorded_at=args.recorded_at or utc_now(),
        supersedes=previous["event_id"] if previous else "",
    )
    if args.candidate_id:
        event["candidate_id"] = identifier
        identity = json.dumps({key: value for key, value in event.items() if key != "event_id"},
                              sort_keys=True, ensure_ascii=False, separators=(",", ":"))
        event["event_id"] = "sha256:" + sha256_text(identity)
    append_events(destination, [event])
    print("1 judgement event appended; %s" % relative_source(destination, root))
    return 0


def command_verify(args) -> int:
    root = repo_root()
    paths = [Path(args.history).resolve()] if args.history else sorted(
        (root / "ai-evaluation").glob("*/history.jsonl"))
    if not paths:
        raise HistoryError("no judgement history files found")
    failures = []
    total = 0
    for path in paths:
        events = read_history(path)
        known = set()
        latest = {}
        for number, event in enumerate(events, start=1):
            if event["event_id"] in known:
                failures.append("%s:%d duplicates event_id %s" %
                                (path, number, event["event_id"]))
            if event["supersedes"]:
                if event["supersedes"] not in known:
                    failures.append("%s:%d supersedes an unknown or later event" %
                                    (path, number))
                previous = latest.get(event["candidate_id"])
                if not previous or previous["event_id"] != event["supersedes"]:
                    failures.append("%s:%d does not supersede that candidate's latest event" %
                                    (path, number))
            elif event["candidate_id"] in latest:
                failures.append("%s:%d repeats a candidate without supersedes" % (path, number))
            known.add(event["event_id"])
            latest[event["candidate_id"]] = event
        total += len(events)
        print("ok  %s  %d event(s), %d candidate(s)" %
              (relative_source(path, root), len(events), len(latest)))
    if failures:
        for failure in failures:
            print("FAIL  " + failure, file=sys.stderr)
        return 1
    print("history valid: %d event(s)" % total)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    importer = sub.add_parser("import-markdown", help="append changed scorecards from judgements.md")
    importer.add_argument("--year", type=int, required=True)
    importer.add_argument("--file", required=True)
    importer.add_argument("--history")
    importer.add_argument("--recorded-at")
    importer.add_argument("--event-type", default="baseline-import",
                          choices=sorted(EVENT_TYPES))
    importer.set_defaults(handler=command_import)

    record = sub.add_parser("record", help="append one structured judgement")
    record.add_argument("--year", type=int, required=True)
    record.add_argument("--title", required=True)
    record.add_argument("--url", required=True)
    record.add_argument("--related-url", action="append", default=[])
    record.add_argument("--score", type=float, required=True)
    record.add_argument("--verdict", required=True)
    record.add_argument("--decision", choices=sorted(DECISIONS), required=True)
    record.add_argument("--confidence", required=True)
    record.add_argument("--source", required=True)
    record.add_argument("--line", type=int, default=1)
    record.add_argument("--note")
    record.add_argument("--candidate-id")
    record.add_argument("--history")
    record.add_argument("--recorded-at")
    record.set_defaults(handler=command_record)

    verify = sub.add_parser("verify", help="validate all yearly history chains")
    verify.add_argument("--history")
    verify.set_defaults(handler=command_verify)
    return parser


def main(argv=None) -> int:
    try:
        args = build_parser().parse_args(argv)
        return args.handler(args)
    except HistoryError as error:
        print("error: %s" % error, file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
