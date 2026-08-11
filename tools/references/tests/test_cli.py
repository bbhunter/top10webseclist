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

    def test_a_stated_byline_reaches_both_the_entry_and_the_rendered_record(self):
        entry, record = {"authors": []}, {"authors": []}
        applied = refs._apply_attribution_override(
            entry, {"authors": ["Alex Example"]}, record)
        self.assertTrue(applied)
        self.assertEqual(["Alex Example"], entry["authors"])
        self.assertEqual(["Alex Example"], record["authors"])

    def test_a_stated_publisher_outranks_the_squatter_that_answered(self):
        entry = {"publisher": "DomainsForSale"}
        refs._apply_attribution_override(entry, {"publisher": "example.test"})
        self.assertEqual("example.test", entry["publisher"])

    def test_an_absent_decision_leaves_extracted_attribution_alone(self):
        entry = {"authors": ["Extracted Name"], "publisher": "example.test"}
        self.assertFalse(refs._apply_attribution_override(entry, None))
        self.assertFalse(refs._apply_attribution_override(entry, {"title": "Only a title"}))
        self.assertEqual(["Extracted Name"], entry["authors"])
        self.assertEqual("example.test", entry["publisher"])

    def test_a_blank_curated_name_is_not_an_attribution(self):
        entry = {"authors": ["Extracted Name"]}
        self.assertFalse(refs._apply_attribution_override(entry, {"authors": ["", "  "]}))
        self.assertEqual(["Extracted Name"], entry["authors"])

    def test_curated_names_are_copied_not_shared_with_the_decision(self):
        judged = {"authors": ["Alex Example"]}
        entry = {}
        refs._apply_attribution_override(entry, judged)
        entry["authors"].append("Someone Else")
        self.assertEqual(["Alex Example"], judged["authors"])

    def test_an_emptied_decision_withdraws_a_name_the_archive_got_wrong(self):
        # Reading only truthy values left a misattribution un-retractable: the
        # correction restored silence, and silence read as "nothing to say".
        entry = {"authors": ["Wrong Person"], "publisher": "wrong.example"}
        self.assertTrue(refs._apply_attribution_override(entry, {"authors": []}))
        self.assertEqual([], entry["authors"])
        self.assertTrue(refs._apply_attribution_override(entry, {"publisher": ""}))
        self.assertEqual("", entry["publisher"])

    def test_a_stated_publisher_moving_a_corrected_slug_is_reported(self):
        entry = {"slug": "2008-hugedomains-com-recovered-title",
                 "publisher": "Aspect Security", "published": "2008-05-16"}
        self.assertEqual("2008-aspect-security-recovered-title",
                         refs._slug_after_attribution(entry, {"title": "Recovered title"}))

    def test_attribution_without_a_title_correction_renames_nothing(self):
        entry = {"slug": "2008-aspect-security-recovered-title",
                 "publisher": "Aspect Security", "published": "2008-05-16"}
        self.assertEqual("", refs._slug_after_attribution(entry, {"authors": ["Alex Example"]}))
        self.assertEqual("", refs._slug_after_attribution(
            entry, {"title": "Recovered title"}))

    def test_recording_attribution_twice_finds_nothing_the_second_time(self):
        urls = {"https://one.example/a": {"authors": [], "publisher": "squatter.example"}}
        decisions = {"https://one.example/a": {"authors": ["Alex Example"],
                                               "publisher": "example.test"}}
        first = refs._attribution_changes(urls, decisions)
        self.assertEqual(1, len(first))
        self.assertEqual((["Alex Example"], "example.test"), first[0][2])
        self.assertEqual([], refs._attribution_changes(urls, decisions))

    def test_a_withdrawal_counts_as_a_change_to_record(self):
        urls = {"https://one.example/a": {"authors": ["Wrong Person"]}}
        changes = refs._attribution_changes(urls, {"https://one.example/a": {"authors": []}})
        self.assertEqual(1, len(changes))
        self.assertEqual([], changes[0][2][0])

    def test_attribution_accepts_the_dry_run_selector(self):
        self.assertTrue(refs.build_parser().parse_args(["attribution", "--check"]).check)

    def test_the_byline_excerpt_starts_after_our_own_attribution_block(self):
        # Handing a reader our "Author not stated" line gets it read back.
        from refslib import render as render_module
        text = ('---\nslug: example\nauthors: []\n---\n\n# Example\n\n'
                '**Example** - Author not stated, example.test.\n\n'
                + render_module.BANNER + '\nBy Alex Example. The real article.\n')
        excerpt = refs._byline_excerpt(text)
        self.assertNotIn("Author not stated", excerpt)
        self.assertTrue(excerpt.startswith("By Alex Example"), excerpt[:40])

    def test_the_byline_excerpt_keeps_link_text_and_drops_the_target(self):
        text = "Posted by [Alex Example](https://tracker.example/u?id=1) today."
        self.assertEqual("Posted by Alex Example today.", refs._byline_excerpt(text))

    def test_the_byline_excerpt_keeps_a_head_and_a_tail(self):
        # A whitepaper names its authors under the title and again in a closing
        # biography, so a head-only excerpt misses half the evidence.
        text = "HEAD " + ("filler " * 600) + "TAIL"
        excerpt = refs._byline_excerpt(text, head=40, tail=20)
        self.assertTrue(excerpt.startswith("HEAD"))
        self.assertTrue(excerpt.endswith("TAIL"))
        self.assertIn("[…]", excerpt)

    def test_a_read_byline_is_refused_without_the_words_it_was_read_from(self):
        known = {"https://one.example/a": {}}
        good = {"authors": ["Alex Example"], "evidence": "By Alex Example",
                "confidence": "high"}
        self.assertEqual("", refs._accept_byline("https://one.example/a", good, known))
        self.assertTrue(refs._accept_byline("https://two.example/b", good, known))
        self.assertTrue(refs._accept_byline(
            "https://one.example/a", dict(good, evidence=" "), known))
        self.assertTrue(refs._accept_byline(
            "https://one.example/a", dict(good, confidence="medium"), known))
        self.assertTrue(refs._accept_byline(
            "https://one.example/a",
            dict(good, authors=["https://spam.example/buy"]), known))

    def test_reading_that_the_document_names_nobody_is_a_real_answer(self):
        # Kept, so the next run does not ask the same question again; and it
        # needs no quotation, because there is nothing to quote.
        known = {"https://one.example/a": {}}
        self.assertEqual("", refs._accept_byline(
            "https://one.example/a", {"authors": [], "confidence": "low"}, known))

    def test_bylines_takes_exactly_one_of_queue_or_apply(self):
        parser = refs.build_parser()
        self.assertEqual("q.json", parser.parse_args(["bylines", "--queue", "q.json"]).queue)
        self.assertEqual("r.json", parser.parse_args(["bylines", "--apply", "r.json"]).apply)
        with self.assertRaises(SystemExit):
            parser.parse_args(["bylines"])

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
