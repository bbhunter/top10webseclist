"""Generated work-list remedies."""

from . import support  # noqa: F401

import unittest

from refslib import indexer


class TestRemedies(unittest.TestCase):
    def test_a_video_points_to_written_counterpart_research_first(self):
        advice = indexer.remedy_for("the video page declares no caption track", "video")
        self.assertIn("written counterpart", advice)
        self.assertIn("release date", advice)
        self.assertIn("description", advice)
        self.assertIn("speaker and conference", advice)
        self.assertIn("only when no written counterpart exists", advice)

    def test_a_filed_fault_points_at_its_own_recorded_remedy(self):
        """Whoever filed the fault wrote what is wrong and what would fix it
        into `content_gap`; "unknown cause, read the reason and decide" threw
        that away. It outranks the kind, so a bad capture of a talk is still a
        capture problem."""
        advice = indexer.remedy_for("faulty capture: the file is the consent wall; "
                                    "recapture through the browser ladder", "video")
        self.assertIn("names its own remedy", advice)
        self.assertIn("--faulty-captures", advice)

    def test_an_article_keeps_its_failure_specific_remedy(self):
        advice = indexer.remedy_for("extraction produced 20 characters, below the floor",
                                    "article")
        self.assertIn("JavaScript", advice)


class FakeStore(object):
    """Holds exactly the hashes it was given."""

    def __init__(self, held=()):
        self.held = set(held)

    def has(self, sha):
        return sha in self.held


class FakeManifest(object):
    def __init__(self, urls):
        self.data = {"urls": urls}


def archived(**over):
    """An entry that acquired cleanly and published a document."""
    entry = {
        "slug": "desync-endgame",
        "grade": "research",
        "kind": "article",
        "raw_sha256": "raw1",
        "content_sha256": "text1",
        "cited_by": ["2019.md:7"],
        "steps": {"acquire": {"result": "stored"}},
    }
    entry.update(over)
    return entry


class TestNeedsWorkIsOnlyWhatCouldNotBeArchived(unittest.TestCase):
    """`needs-work.md` answers ONE question: could the archive not get the
    document? Lost store bytes were listed there too, and 1,011 fully archived
    references - every one of them with its Markdown and PDF published - buried
    the handful that genuinely have no document. Those belong on
    `store-gaps.md`."""

    def test_an_archived_reference_whose_bytes_are_gone_is_not_work(self):
        manifest = FakeManifest({"https://x.test/a": archived()})
        text = indexer.build_unresolved(manifest, store=FakeStore())
        self.assertIn("Nothing unresolved", text)
        self.assertFalse(indexer.needs_work(archived()))

    def test_a_reference_with_no_document_is_still_listed(self):
        entry = archived(steps={"acquire": {"result": "failed",
                                            "reason": "the fetch returned 403"}})
        text = indexer.build_unresolved(FakeManifest({"https://x.test/a": entry}),
                                        store=FakeStore({"raw1", "text1"}))
        self.assertIn("https://x.test/a", text)
        self.assertNotIn("Nothing unresolved", text)

    def test_needs_work_selector_matches_the_generated_queue(self):
        self.assertTrue(indexer.needs_work(archived(content_gap="transcript missing")))

    def test_an_excluded_reference_stays_excluded_whatever_the_store_holds(self):
        entry = archived(decision={"outcome": "skip", "class": "derivative"})
        text = indexer.build_unresolved(FakeManifest({"https://x.test/a": entry}),
                                        store=FakeStore())
        self.assertIn("Nothing unresolved", text)

    def test_have_bytes_means_the_store_can_actually_produce_them(self):
        """"Already have the bytes" promises an offline re-run. A recorded hash
        whose object is gone would fail the moment that re-run was tried."""
        entry = archived(content_gap="the converted text is the consent wall")
        held = indexer.build_unresolved(FakeManifest({"https://x.test/a": entry}),
                                        store=FakeStore({"raw1", "text1"}))
        self.assertNotIn("(no bytes stored)", held)
        gone = indexer.build_unresolved(FakeManifest({"https://x.test/a": entry}),
                                        store=FakeStore())
        self.assertIn("(no bytes stored)", gone)


class TestStoreGaps(unittest.TestCase):
    """A PUBLISHED FILE IS NOT PROOF THE ARCHIVE STILL HAS THE SOURCE. An
    antivirus scanner deleted store objects - exploit write-ups read as malware
    by their own text - leaving references with a good Markdown file and nothing
    behind it. Every acquisition rule counts those as done, so this report is
    the only thing that notices."""

    def test_a_reference_whose_bytes_are_gone_is_listed(self):
        manifest = FakeManifest({"https://x.test/a": archived()})
        text = indexer.build_store_gaps(manifest, store=FakeStore())
        self.assertIn("https://x.test/a", text)
        self.assertNotIn("No gaps", text)

    def test_the_same_reference_with_its_bytes_present_is_not_listed(self):
        manifest = FakeManifest({"https://x.test/a": archived()})
        text = indexer.build_store_gaps(manifest, store=FakeStore({"raw1", "text1"}))
        self.assertIn("No gaps", text)

    def test_the_missing_field_is_named_so_the_reader_knows_what_went(self):
        manifest = FakeManifest({"https://x.test/a": archived()})
        text = indexer.build_store_gaps(manifest, store=FakeStore({"raw1"}))
        row = [line for line in text.splitlines() if "https://x.test/a" in line][0]
        self.assertIn("`content_sha256`", row)
        self.assertNotIn("`raw_sha256`", row)

    def test_an_excluded_reference_is_listed_when_its_bytes_are_gone(self):
        """The maintainer's decision was made about a document the archive can
        no longer show the evidence for."""
        entry = archived(decision={"outcome": "skip", "class": "derivative"})
        text = indexer.build_store_gaps(FakeManifest({"https://x.test/a": entry}),
                                        store=FakeStore())
        self.assertIn("https://x.test/a", text)

    def test_a_translation_or_browser_dom_counts_too(self):
        entry = archived(browser_dom_sha256="dom1", translation_sha256="tr1")
        text = indexer.build_store_gaps(FakeManifest({"https://x.test/a": entry}),
                                        store=FakeStore({"raw1", "text1", "tr1"}))
        self.assertIn("browser_dom_sha256", text)

    def test_without_a_store_the_check_cannot_run_and_says_nothing(self):
        """An offline caller with no store must not report every reference as
        lost just because it cannot look."""
        text = indexer.build_store_gaps(FakeManifest({"https://x.test/a": archived()}))
        self.assertIn("No gaps", text)

    def test_it_says_plainly_that_these_are_archived(self):
        text = indexer.build_store_gaps(FakeManifest({"https://x.test/a": archived()}),
                                        store=FakeStore())
        self.assertIn("IS archived", text)
        self.assertIn("needs-work.md", text)


if __name__ == "__main__":
    unittest.main()
