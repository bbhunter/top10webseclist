"""The live-page PDF capture used to archive the announcement posts.

Everything here is provable without launching a browser: the guards, the option
assembly, and the archival policy in `tools/capture_pdf.py`. Driving a real
browser is what `capture_pdf.py doctor --smoke` is for.
"""

from . import support  # noqa: F401

import os
import sys
import unittest
from pathlib import Path

from refslib import browser as browser_module

# capture_pdf.py lives one level up from the reference tool, in tools/.
TOOLS_DIR = Path(support.TOOL_DIR).parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

import capture_pdf  # noqa: E402


class FakeSocket(object):
    """Answers Runtime.evaluate from a scripted queue; records every call."""

    def __init__(self, values=(), exception_on=None):
        self.values = list(values)
        self.exception_on = exception_on or ()
        self.calls = []

    def call(self, method, params=None, session=None, timeout=None):
        self.calls.append((method, params))
        if method != "Runtime.evaluate":
            return {}
        expression = (params or {}).get("expression", "")
        if any(marker in expression for marker in self.exception_on):
            return {"exceptionDetails": {"text": "boom"}}
        value = self.values.pop(0) if self.values else None
        return {"result": {"value": value}}


def ladder(browser="fake"):
    return browser_module.Ladder(browser=browser, sleep=lambda seconds: None)


class TestRenderGuards(unittest.TestCase):
    def test_no_browser_names_the_environment_variable(self):
        with self.assertRaises(RuntimeError) as caught:
            ladder(browser=None).render_url_pdf("https://example.org/")
        self.assertIn(browser_module.BROWSER_ENV, str(caught.exception))

    def test_evaluate_raises_on_a_thrown_expression(self):
        """A throw arrives as exceptionDetails with no value, so reading `value`
        alone would turn every failure into a silent empty result."""
        socket = FakeSocket(exception_on=("document.title",))
        with self.assertRaises(RuntimeError):
            ladder()._evaluate(socket, "session", "document.title")

    def test_await_ready_gives_up_rather_than_hanging(self):
        socket = FakeSocket(values=[False] * 200)
        self.assertFalse(ladder()._await_ready(socket, "session", budget=0))

    def test_await_ready_succeeds_once_the_document_is_complete(self):
        socket = FakeSocket(values=[False, True])
        self.assertTrue(ladder()._await_ready(socket, "session", budget=5))

    def test_page_stats_survives_a_page_that_answers_nonsense(self):
        self.assertEqual(ladder()._page_stats(FakeSocket(values=["not a dict"]),
                                             "session", 5), {})

    def test_page_stats_reports_an_error_instead_of_raising(self):
        socket = FakeSocket(exception_on=("performance",))
        stats = ladder()._page_stats(socket, "session", 5)
        self.assertIn("stats_error", stats)


class TestSandboxOptIn(unittest.TestCase):
    """Chrome's sandbox is a real boundary and these captures render hostile
    third-party pages, so dropping it is never inferred from the environment."""

    def setUp(self):
        self.original = os.environ.get(browser_module.NO_SANDBOX_ENV)
        self.addCleanup(self.restore)

    def restore(self):
        if self.original is None:
            os.environ.pop(browser_module.NO_SANDBOX_ENV, None)
        else:
            os.environ[browser_module.NO_SANDBOX_ENV] = self.original

    def test_it_is_absent_by_default(self):
        os.environ.pop(browser_module.NO_SANDBOX_ENV, None)
        self.assertEqual(browser_module.sandbox_args(), ())

    def test_it_appears_only_when_asked_for(self):
        os.environ[browser_module.NO_SANDBOX_ENV] = "1"
        self.assertIn("--no-sandbox", browser_module.sandbox_args())


class TestBrowserDiscovery(unittest.TestCase):
    def test_a_browser_on_path_is_found_when_no_fixed_location_matches(self):
        """Without this the tool is Windows-only, because every fixed candidate
        is a Windows install path."""
        original_candidates = browser_module.CANDIDATE_BROWSERS
        original_which = browser_module.shutil.which
        original_env = os.environ.pop(browser_module.BROWSER_ENV, None)
        browser_module.CANDIDATE_BROWSERS = ()
        browser_module.shutil.which = lambda name: (
            "/usr/bin/chromium" if name == "chromium" else None)
        try:
            self.assertEqual(browser_module.find_browser(), "/usr/bin/chromium")
        finally:
            browser_module.CANDIDATE_BROWSERS = original_candidates
            browser_module.shutil.which = original_which
            if original_env is not None:
                os.environ[browser_module.BROWSER_ENV] = original_env


class TestArchivalPolicy(unittest.TestCase):
    def test_an_archive_replay_waits_longer_than_a_live_host(self):
        """A replay waits on the archive as well as the page. This defaulting is
        why the manifest does not have to carry a settle for every Wayback row."""
        live = {"url": "https://portswigger.net/research/x"}
        replay = {"url": "https://web.archive.org/web/2017/https://x.test/y"}
        self.assertEqual(capture_pdf.settle_for(live, 3.0), 3.0)
        self.assertEqual(capture_pdf.settle_for(replay, 3.0),
                         capture_pdf.SLOW_HOST_SETTLE)

    def test_an_explicit_settle_wins_over_the_default(self):
        entry = {"url": "https://web.archive.org/web/x", "settle": 1.5}
        self.assertEqual(capture_pdf.settle_for(entry, 3.0), 1.5)

    def test_content_assertions_survive_extraction_whitespace(self):
        """Justified text extracts with non-breaking spaces and doubled gaps, so
        a raw substring test reports text missing that is plainly on the page."""
        extracted = "Current\xa0List  of 2015\nSubmissions"
        self.assertIn(capture_pdf.norm("Current List of 2015 Submissions"),
                      capture_pdf.norm(extracted))

    def test_the_file_name_is_the_year_and_the_kind(self):
        self.assertEqual(
            capture_pdf.out_name({"year": "2016-17", "kind": "nominees"}),
            "2016-17-nominees.pdf")

    def test_selection_filters_by_year_and_kind(self):
        entries = [{"year": "2025", "kind": "nominees", "url": "u"},
                   {"year": "2025", "kind": "top10", "url": "u"},
                   {"year": "2024", "kind": "nominees", "url": "u"}]
        self.assertEqual(len(capture_pdf.select(entries, only="2025")), 2)
        self.assertEqual(len(capture_pdf.select(entries, kind="nominees")), 2)
        self.assertEqual(
            len(capture_pdf.select(entries, only="2025", kind="top10")), 1)

    def test_a_multi_word_kind_is_selectable(self):
        """`nominees-and-top10` is a real kind: four years were published as one
        living post. A fixed choice list would have made them uncapturable."""
        entries = [{"year": "2015", "kind": "nominees-and-top10", "url": "u"}]
        self.assertEqual(
            len(capture_pdf.select(entries, kind="nominees-and-top10")), 1)

    def test_the_footer_carries_the_source_url_escaped(self):
        options = capture_pdf.print_options(
            "https://x.test/a?b=1&c=2", scale=0.7)
        self.assertIn("&amp;", options["footerTemplate"])
        self.assertNotIn("&c=2", options["footerTemplate"])
        self.assertEqual(options["scale"], 0.7)
        self.assertTrue(options["printBackground"])

    def test_the_prepare_scripts_scroll_and_then_tidy(self):
        """Order matters: furniture is removed after the scroll, because the
        scroll is what makes lazy images load."""
        self.assertEqual(len(capture_pdf.PREPARE), 2)
        self.assertIn("scrollTo", capture_pdf.PREPARE[0])
        self.assertIn("wm-ipp", capture_pdf.PREPARE[1])


class TestManifestValidation(unittest.TestCase):
    def write(self, body):
        import tempfile
        handle = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False,
                                            encoding="utf-8")
        handle.write(body)
        handle.close()
        self.addCleanup(os.unlink, handle.name)
        return handle.name

    def test_a_manifest_row_missing_a_url_is_refused(self):
        path = self.write('{"entries": [{"year": "2025", "kind": "top10"}]}')
        with self.assertRaises(SystemExit):
            capture_pdf.load_manifest(path)

    def test_an_empty_manifest_is_refused(self):
        path = self.write('{"entries": []}')
        with self.assertRaises(SystemExit):
            capture_pdf.load_manifest(path)

    def test_broken_json_is_refused_with_an_exit_not_a_traceback(self):
        path = self.write("{not json")
        with self.assertRaises(SystemExit):
            capture_pdf.load_manifest(path)

    def test_a_good_manifest_loads(self):
        path = self.write(
            '{"entries": [{"year": "2025", "kind": "top10", "url": "https://x"}]}')
        self.assertEqual(len(capture_pdf.load_manifest(path)["entries"]), 1)

    def test_the_repository_manifest_is_valid_and_covers_every_year(self):
        manifest = capture_pdf.load_manifest(capture_pdf.DEFAULT_MANIFEST)
        years = {entry["year"] for entry in manifest["entries"]}
        # 2016 has no list of its own: PortSwigger revived the series for 2017
        # and folded 2016 into it, so the pair share one set of files.
        expected = {str(y) for y in range(2006, 2026)} - {"2016", "2017"}
        expected.add("2016-17")
        self.assertEqual(years, expected)

    def test_every_manifest_row_names_a_file_the_archive_actually_has(self):
        manifest = capture_pdf.load_manifest(capture_pdf.DEFAULT_MANIFEST)
        missing = [capture_pdf.out_name(entry)
                   for entry in manifest["entries"]
                   if not os.path.exists(os.path.join(
                       capture_pdf.DEFAULT_OUTDIR, capture_pdf.out_name(entry)))]
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
