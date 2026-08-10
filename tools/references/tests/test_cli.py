"""Command-line recovery selectors."""

import types
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import refs


class _Store(object):
    def __init__(self, held=()):
        self.held = set(held)

    def has(self, digest):
        return digest in self.held


class RecoverySelectorTests(unittest.TestCase):
    def test_missing_store_keys_only_names_rows_with_lost_evidence(self):
        manifest = types.SimpleNamespace(data={"urls": {
            "complete": {"raw_sha256": "raw", "content_sha256": "content"},
            "lost": {"raw_sha256": "gone", "content_sha256": "content"},
            "never-acquired": {},
        }})
        self.assertEqual({"lost"}, refs._missing_store_keys(
            manifest, _Store(("raw", "content"))))

    def test_a_lost_store_object_reopens_a_hand_import_without_redo(self):
        entry = {"raw_sha256": "gone", "content_sha256": "content",
                 "grade": "research", "steps": {
                     "acquire": {"result": "stored"},
                     "import": {"result": "stored"}}}
        self.assertTrue(refs._import_needs_content(
            entry, _Store(("content",)), redo=False))

    def test_check_and_acquire_accept_missing_store_selector(self):
        parser = refs.build_parser()
        self.assertTrue(parser.parse_args(["check", "--missing-store"]).missing_store)
        self.assertTrue(parser.parse_args(["acquire", "--missing-store"]).missing_store)
        self.assertTrue(parser.parse_args(["acquire", "--browser-dom"]).browser_dom)
        acquired = parser.parse_args(
            ["acquire", "--faulty-captures", "--wayback-capture", "--document-gaps",
             "--linked-document-url", "https://authors.example/paper.pdf",
             "--also-at", "https://authors.example/code"])
        self.assertTrue(acquired.faulty_captures)
        self.assertTrue(acquired.wayback_capture)
        self.assertTrue(acquired.document_gaps)
        self.assertEqual("https://authors.example/paper.pdf",
                         acquired.linked_document_url)
        self.assertEqual(["https://authors.example/code"], acquired.also_at)
        self.assertTrue(parser.parse_args(
            ["acquire", "--clear-linked-document"]).clear_linked_document)
        self.assertTrue(parser.parse_args(["translate", "--render"]).render)
        self.assertTrue(parser.parse_args(
            ["pdf", "--translations-only"]).translations_only)
        imported = parser.parse_args(
            ["import", "--redo", "--only", "one.example", "/tmp/import"])
        self.assertTrue(imported.redo)
        self.assertEqual("one.example", imported.only)
        wayback = parser.parse_args(
            ["wayback", "--faulty-captures", "--after", "old.example", "--limit", "25"])
        self.assertTrue(wayback.faulty_captures)
        self.assertEqual("old.example", wayback.after)
        self.assertEqual(25, wayback.limit)
        historical = parser.parse_args(
            ["historical-urls", "--only", "old.example",
             "--limit-requests", "12", "--limit-results", "34"])
        self.assertEqual("old.example", historical.only)
        self.assertEqual(12, historical.limit_requests)
        self.assertEqual(34, historical.limit_results)

    def test_acquire_after_selector_resumes_strictly_after_match(self):
        entries = [("alpha", {}), ("legacy.example/dead", {}), ("omega", {})]
        self.assertEqual([("omega", {})], refs._entries_after(entries, "LEGACY.EXAMPLE"))
        with self.assertRaisesRegex(Exception, "matched no manifest identity"):
            refs._entries_after(entries, "absent")

    def test_faulty_capture_never_sets_a_replacement_size_floor(self):
        entry = {"steps": {"acquire": {"result": "stored"}},
                 "content_gap": "faulty capture: parked domain; recover it"}
        self.assertFalse(refs._held_capture_is_readable(entry))
        entry["content_gap"] = ""
        self.assertTrue(refs._held_capture_is_readable(entry))

    def test_title_override_rebuilds_a_stale_slug_without_suffix_creep(self):
        record = {"title": "Recovered title", "slug": "casino-sale",
                  "publisher": "SecTheory", "published": "2008-05-16"}
        entry = {"slug": "casino-sale"}
        refs._apply_title_override(record, entry, "Recovered title", {"casino-sale"})
        self.assertEqual("2008-sectheory-recovered-title", record["slug"])

    def test_frontmatter_scalar_reader_keeps_only_top_level_values(self):
        text = ('---\nslug: example\noriginal_url: "https://example.test/a:b"\n'
                'sources:\n  - id: original\nempty: ""\n---\n\n# Example\n')
        self.assertEqual(
            {"slug": "example", "original_url": "https://example.test/a:b",
             "empty": ""},
            refs._frontmatter_scalars(text))

    def test_completed_pdf_clears_only_a_pdf_absence_fault(self):
        with TemporaryDirectory() as folder:
            pdf = Path(folder) / "document.pdf"
            pdf.write_bytes(b"%PDF-1.7\n" + b"x" * 600)
            entry = {"content_gap":
                     "faulty capture: the generated PDF is absent; rebuild it"}
            self.assertTrue(refs._clear_completed_pdf_gap(entry, pdf))
            self.assertEqual("", entry["content_gap"])

            interactive = {"content_gap":
                           "faulty capture: the interactive citation redirects away "
                           "and the advertised PDF is absent"}
            self.assertFalse(refs._clear_completed_pdf_gap(interactive, pdf))
            self.assertTrue(interactive["content_gap"])

            not_pdf = Path(folder) / "wall.pdf"
            not_pdf.write_bytes(b"<html>" + b"x" * 600)
            missing = {"content_gap":
                       "faulty capture: the generated PDF is absent; rebuild it"}
            self.assertFalse(refs._clear_completed_pdf_gap(missing, not_pdf))


if __name__ == "__main__":
    unittest.main()
