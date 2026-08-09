"""Selection rules for the Docker-only browser recovery pass."""

from . import support  # noqa: F401

import unittest

from refslib import browser, check


class TestBrowserSelection(unittest.TestCase):
    def test_a_dead_row_is_not_rendered_by_a_broad_forced_pass(self):
        entry = {"kind": "article", "health": {"status": "dead"}}
        self.assertFalse(check.browser_wanted(entry, force=True,
                                              explicit_only=False))

    def test_force_and_an_explicit_filter_can_retry_a_misclassified_row(self):
        entry = {"kind": "article", "health": {"status": "dead"}}
        self.assertTrue(check.browser_wanted(entry, force=True,
                                             explicit_only=True))

    def test_force_and_an_explicit_filter_can_render_an_html_slide_viewer(self):
        entry = {"kind": "slides", "health": {"status": "dead"}}
        self.assertTrue(check.browser_wanted(entry, force=True,
                                             explicit_only=True))

    def test_a_whitepaper_is_not_sent_to_a_browser_viewer(self):
        entry = {"kind": "whitepaper", "health": {"status": "dead"}}
        self.assertFalse(check.browser_wanted(entry, force=True,
                                              explicit_only=True))

    def test_video_players_are_never_sent_to_the_browser(self):
        entry = {"kind": "video", "health": {"status": "dead"}}
        self.assertFalse(check.browser_wanted(entry, force=True,
                                              explicit_only=True))

    def test_each_completed_browser_row_is_checkpointed(self):
        class Manifest(object):
            data = {"urls": {"https://example.test/report": {
                "kind": "article", "health": {"status": "blocked"}}}}

            def record(self, *_args, **_kwargs):
                pass

        class Store(object):
            def put_text(self, _text):
                return "a" * 64

        class Ladder(object):
            def fetch(self, url, budget=30):
                html = "<html><title>Report</title><body>" + ("research " * 100) + "</body></html>"
                return browser.BrowserResult(url, html, url, "docker-headless-5s", 1)

        checkpoints = []
        check.run_browser(Manifest(), Store(), Ladder(), checkpoint=lambda: checkpoints.append(1))
        self.assertEqual([1], checkpoints)


if __name__ == "__main__":
    unittest.main()
