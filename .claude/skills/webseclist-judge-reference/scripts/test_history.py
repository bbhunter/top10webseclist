"""Tests for the append-only judgement history."""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("history.py")
SPEC = importlib.util.spec_from_file_location("judgement_history", MODULE_PATH)
history = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(history)


SAMPLE = """# Per-entry judgements

## 67.5 — [A finding](https://example.test/finding/) [Paper](<https://example.test/paper(v1).pdf>) — A. Researcher

**KEPT** · Meaningful extension · confidence Medium-High

**What is new.** A useful contribution.

---

## 42.0 — [Known work](https://example.test/known) — B. Researcher

**REMOVED** · Duplicate / already known · confidence High

**What was already known.** Everything.
"""


class HistoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.source = self.root / "judgements.md"
        self.output = self.root / "history.jsonl"
        self.source.write_text(SAMPLE, encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def import_once(self, event_type="baseline-import"):
        args = type("Args", (), {
            "year": 2026,
            "file": str(self.source),
            "history": str(self.output),
            "recorded_at": "2026-08-08T12:00:00+00:00",
            "event_type": event_type,
        })()
        return history.command_import(args)

    def events(self):
        return [json.loads(line) for line in self.output.read_text(encoding="utf-8").splitlines()]

    def test_parser_keeps_primary_and_related_links(self):
        parsed = history.parse_markdown(self.source)
        self.assertEqual(len(parsed), 2)
        self.assertEqual(parsed[0]["primary_url"], "https://example.test/finding/")
        self.assertEqual(parsed[0]["related_urls"], ["https://example.test/paper(v1).pdf"])
        self.assertEqual(parsed[0]["confidence"], "Medium-High")

    def test_import_is_idempotent(self):
        self.import_once()
        self.import_once()
        self.assertEqual(len(self.events()), 2)

    def test_changed_judgement_appends_and_supersedes(self):
        self.import_once()
        self.source.write_text(SAMPLE.replace("67.5", "68.0", 1), encoding="utf-8")
        self.import_once("rejudgement")
        events = self.events()
        self.assertEqual(len(events), 3)
        self.assertEqual(events[-1]["score"], 68.0)
        self.assertEqual(events[-1]["supersedes"], events[0]["event_id"])

    def test_verify_accepts_a_valid_chain(self):
        self.import_once()
        args = type("Args", (), {"history": str(self.output)})()
        self.assertEqual(history.command_verify(args), 0)

    def test_invalid_json_is_rejected(self):
        self.output.write_text("{broken\n", encoding="utf-8")
        with self.assertRaises(history.HistoryError):
            history.read_history(self.output)

    def test_changed_event_content_is_rejected(self):
        self.import_once()
        events = self.events()
        events[0]["score"] = 99.0
        self.output.write_text(json.dumps(events[0]) + "\n", encoding="utf-8")
        with self.assertRaises(history.HistoryError):
            history.read_history(self.output)


if __name__ == "__main__":
    unittest.main()
