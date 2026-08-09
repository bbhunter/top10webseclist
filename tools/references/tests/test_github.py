"""Reading GitHub through its API instead of its JavaScript shell.

Measured: a repository security advisory reached the extractor as 264
characters, another as 139, and a source file as 150. All three failed the
content floor, which is right - the document really is not in that HTML.
"""

from . import support  # noqa: F401

import json
import unittest

from refslib import github
from refslib.fetcher import Response

ADVISORY_URL = ("https://github.com/example-org/example-app/security/advisories/"
                "GHSA-aaaa-bbbb-cccc")
GLOBAL_ADVISORY_URL = "https://github.com/advisories/GHSA-dddd-eeee-ffff"
BLOB_URL = ("https://github.com/example-org/example-app/blob/main/"
            "src/proxy/chunked-parser.js#L323")
ISSUE_URL = "https://github.com/example-org/example-app/issues/1280"

ADVISORY_JSON = {
    "ghsa_id": "GHSA-aaaa-bbbb-cccc",
    "cve_id": "CVE-2024-00000",
    "summary": "Request smuggling in example-app",
    "description": "The `example-proxy` package forwards a request carrying both\n"
                   "`Content-Length` and `Transfer-Encoding: chunked`, which lets an\n"
                   "attacker smuggle a second request past the front end.",
    "severity": "critical",
    "published_at": "2024-03-04T10:00:00Z",
    "updated_at": "2024-03-05T10:00:00Z",
    "references": ["https://example.org/writeup"],
    "vulnerabilities": [{"package": {"ecosystem": "npm", "name": "example-proxy"},
                         "vulnerable_version_range": "< 6.13",
                         "first_patched_version": {"identifier": "6.13"}}],
}

ISSUE_JSON = {
    "title": "Security Risk in the recursive merge default",
    "user": {"login": "someone"},
    "created_at": "2022-06-01T09:00:00Z",
    "state": "closed",
    "body": "Using the recursive merge lets an attacker reach `Object.prototype`.",
}


class FakeFetcher(object):
    """Answers by endpoint, and records what was asked for."""

    def __init__(self, answers):
        self.answers = answers
        self.calls = []

    def get(self, url, extra_headers=None, max_bytes=None):
        self.calls.append(url)
        for prefix, (status, body) in self.answers.items():
            if url.startswith(prefix):
                payload = body if isinstance(body, bytes) else json.dumps(body).encode()
                return Response(url, status, {"Content-Type": "application/json"},
                                payload, [])
        return Response(url, 404, {}, b"", [])


class TestRouting(unittest.TestCase):
    def test_the_three_shapes_are_recognised(self):
        self.assertEqual(github.route(ADVISORY_URL), "advisory")
        self.assertEqual(github.route(GLOBAL_ADVISORY_URL), "advisory")
        self.assertEqual(github.route(BLOB_URL), "file")
        self.assertEqual(github.route(ISSUE_URL), "conversation")

    def test_an_ordinary_repository_page_is_left_to_the_repository_route(self):
        self.assertEqual(github.route("https://github.com/example-org/example-tool"), "")

    def test_a_release_page_and_a_non_github_url_are_untouched(self):
        self.assertEqual(github.route("https://github.com/jgm/pandoc/releases"), "")
        self.assertEqual(github.route("https://example.org/advisories/GHSA-x"), "")


class TestAdvisory(unittest.TestCase):
    def test_the_global_endpoint_answers_for_a_repository_advisory(self):
        """One endpoint covers both spellings of the same page, so a repository
        advisory does not need its own request."""
        fetcher = FakeFetcher({"https://api.github.com/advisories/": (200, ADVISORY_JSON)})
        markdown, facts = github.to_markdown(ADVISORY_URL, fetcher)
        self.assertEqual(len(fetcher.calls), 1)
        self.assertIn("Transfer-Encoding: chunked", markdown)
        self.assertIn("Request smuggling in example-app", facts["title"])
        self.assertEqual(facts["published"], "2024-03-04")

    def test_the_repository_endpoint_is_the_fallback(self):
        fetcher = FakeFetcher({
            "https://api.github.com/repos/example-org/example-app/security-advisories/":
                (200, ADVISORY_JSON)})
        markdown, _facts = github.to_markdown(ADVISORY_URL, fetcher)
        self.assertEqual(len(fetcher.calls), 2)
        self.assertIn("Transfer-Encoding: chunked", markdown)

    def test_the_severity_cve_affected_packages_and_references_are_all_kept(self):
        fetcher = FakeFetcher({"https://api.github.com/advisories/": (200, ADVISORY_JSON)})
        markdown, _facts = github.to_markdown(ADVISORY_URL, fetcher)
        for expected in ("CVE-2024-00000", "critical", "`example-proxy`", "< 6.13",
                         "fixed in 6.13", "https://example.org/writeup"):
            self.assertIn(expected, markdown, expected)

    def test_a_rate_limited_api_is_reported_as_a_refusal(self):
        """Never as "this page has no content": the difference decides whether a
        human retries or goes looking for another source."""
        fetcher = FakeFetcher({"https://api.github.com/": (403, b"{}")})
        with self.assertRaises(github.Unavailable) as caught:
            github.to_markdown(ADVISORY_URL, fetcher)
        self.assertIn("60 an hour", str(caught.exception))

    def test_an_advisory_with_no_text_is_a_refusal_rather_than_an_empty_document(self):
        fetcher = FakeFetcher({"https://api.github.com/advisories/":
                               (200, {"ghsa_id": "GHSA-x"})})
        with self.assertRaises(github.Unavailable):
            github.to_markdown(ADVISORY_URL, fetcher)


class TestFile(unittest.TestCase):
    def test_the_source_is_fetched_raw_and_fenced(self):
        fetcher = FakeFetcher({"https://raw.githubusercontent.com/":
                               (200, b"function readChunkSize() { }\n")})
        markdown, facts = github.to_markdown(BLOB_URL, fetcher)
        self.assertIn("```javascript", markdown)
        self.assertIn("function readChunkSize()", markdown)
        self.assertIn("chunked-parser.js", facts["title"])

    def test_the_cited_line_is_recorded(self):
        """The citation points at a line for a reason, even though the whole
        file is preserved."""
        fetcher = FakeFetcher({"https://raw.githubusercontent.com/": (200, b"x = 1\n")})
        markdown, _facts = github.to_markdown(BLOB_URL, fetcher)
        self.assertIn("line 323", markdown)

    def test_a_missing_file_is_a_refusal(self):
        with self.assertRaises(github.Unavailable):
            github.to_markdown(BLOB_URL, FakeFetcher({}))


class TestConversation(unittest.TestCase):
    def test_the_body_and_comments_are_preserved(self):
        fetcher = FakeFetcher({
            "https://api.github.com/repos/example-org/example-app/issues/1280/comments":
                (200, [{"user": {"login": "other"}, "created_at": "2022-06-02T00:00:00Z",
                        "body": "Confirmed, the setting is unsafe by default."}]),
            "https://api.github.com/repos/example-org/example-app/issues/1280":
                (200, ISSUE_JSON)})
        markdown, facts = github.to_markdown(ISSUE_URL, fetcher)
        self.assertIn("Object.prototype", markdown)
        self.assertIn("Confirmed, the setting is unsafe", markdown)
        self.assertEqual(facts["authors"], ["someone"])

    def test_a_discussion_says_why_it_cannot_be_read(self):
        """It is GraphQL only, and this tool deliberately sends no credentials."""
        with self.assertRaises(github.Unavailable) as caught:
            github.to_markdown("https://github.com/o/r/discussions/5", FakeFetcher({}))
        self.assertIn("token", str(caught.exception))


class TestNoCredentials(unittest.TestCase):
    """An archive run must behave the same for every contributor. A tool that
    quietly used one person's token would produce results nobody else can
    reproduce, and would leak that token's reach into the corpus."""

    def test_no_authorization_header_is_ever_sent(self):
        self.assertNotIn("Authorization", github.API_HEADERS)
        with open(github.__file__, encoding="utf-8") as handle:
            source = handle.read()
        for forbidden in ("GITHUB_TOKEN", "GH_TOKEN", "Authorization"):
            self.assertNotIn(forbidden, source, forbidden)


if __name__ == "__main__":
    unittest.main()


class TestEncodedPaths(unittest.TestCase):
    """A repository really does contain files with spaces in their names.
    Matching on the decoded path keeps the rules readable, but a literal space in
    the request line is not a request: `Request Smuggling.md` failed with "http 0"
    until it was quoted back."""

    def test_a_path_with_a_space_is_requested_encoded(self):
        fetcher = FakeFetcher({"https://raw.githubusercontent.com/": (200, b"# notes\n")})
        github.to_markdown("https://github.com/example-org/example-notes/blob/main/"
                           "Request%20Smuggling.md", fetcher)
        self.assertEqual(fetcher.calls, [
            "https://raw.githubusercontent.com/example-org/example-notes/main/"
            "Request%20Smuggling.md"])

    def test_the_displayed_path_stays_readable(self):
        fetcher = FakeFetcher({"https://raw.githubusercontent.com/": (200, b"# notes\n")})
        markdown, facts = github.to_markdown(
            "https://github.com/example-org/example-notes/blob/main/Request%20Smuggling.md",
            fetcher)
        self.assertIn("Request Smuggling.md", markdown)
        self.assertIn("Request Smuggling.md", facts["title"])


class TestABinaryBlobIsNotReadAsText(unittest.TestCase):
    """A `.pdf` blob wrapped in a code fence and decoded with errors="replace"
    is not the document: three whitepapers were stored that way. Those fall
    through to the ordinary document route and are fetched as bytes."""

    PDF = "https://github.com/cure53/browser-sec-whitepaper/blob/master/browser-security-whitepaper.pdf"
    SOURCE = "https://github.com/owner/name/blob/main/exploit.py"

    def test_a_binary_blob_is_not_claimed_by_the_api_route(self):
        self.assertEqual(github.route(self.PDF), "")

    def test_a_text_blob_still_goes_through_the_api_route(self):
        self.assertEqual(github.route(self.SOURCE), "file")

    def test_a_binary_blob_resolves_to_its_raw_url(self):
        self.assertEqual(
            github.raw_url(self.PDF),
            "https://raw.githubusercontent.com/cure53/browser-sec-whitepaper/master/"
            "browser-security-whitepaper.pdf")

    def test_a_text_blob_has_no_raw_url(self):
        self.assertEqual(github.raw_url(self.SOURCE), "")

    def test_a_non_github_url_has_no_raw_url(self):
        self.assertEqual(github.raw_url("https://example.org/paper.pdf"), "")
