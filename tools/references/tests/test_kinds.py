"""Reference kinds, and what they change.

"Full content" means something different per kind, and the kind decides whether
a walled page is even worth a browser. The measured case: 13 YouTube pages were
classified `js-rendered`, which is true and useless. A video is metadata,
description and captions; a browser waiting 90 seconds for its DOM obtains a
player.
"""

from . import support  # noqa: F401

import unittest

from refslib import kinds


class TestKindFromUrl(unittest.TestCase):
    def test_video_hosts(self):
        for url in ("https://www.youtube.com/watch?v=ZBfBYoK_Wr0",
                    "https://youtu.be/ZBfBYoK_Wr0",
                    "https://vimeo.com/12345"):
            self.assertEqual(kinds.from_url(url), "video", url)

    def test_a_repository_root_is_a_repo_and_a_source_file_in_it_is_code(self):
        self.assertEqual(kinds.from_url("https://github.com/example-org/example-tool"), "repo")
        self.assertEqual(kinds.from_url("https://github.com/owner/name/"), "repo")
        self.assertEqual(
            kinds.from_url("https://github.com/owner/name/blob/main/exploit.py"), "code")

    def test_a_document_in_a_repository_is_the_document_not_code(self):
        """A repository is a fine place to publish a paper. Calling a `.pdf`
        blob "code" sent three browser security whitepapers down the source-file
        route, which read megabytes of PDF as text and stored the replacement
        characters as the document."""
        self.assertEqual(
            kinds.from_url("https://github.com/thezdi/presentations/blob/main/a/whitepaper.pdf"),
            "whitepaper")
        self.assertEqual(
            kinds.from_url("https://github.com/owner/name/blob/main/talk.pptx"), "slides")

    def test_a_pdf_is_a_whitepaper_and_a_pptx_is_slides(self):
        self.assertEqual(kinds.from_url("https://example.org/paper.pdf"), "whitepaper")
        self.assertEqual(kinds.from_url("https://example.org/deck.pptx"), "slides")

    def test_a_slide_host_is_slides(self):
        self.assertEqual(kinds.from_url("https://speakerdeck.com/example/attacking"), "slides")

    def test_public_google_editors_are_documents_not_application_pages(self):
        self.assertEqual(kinds.from_url(
            "https://docs.google.com/presentation/d/deck-id/edit"), "slides")
        self.assertEqual(kinds.from_url(
            "https://docs.google.com/document/d/paper-id/edit"), "whitepaper")

    def test_vendor_documentation_is_recognised_by_path_not_by_host(self):
        """Keyed on the path so a fork inherits the rule rather than a list of
        one corpus's documentation hosts."""
        for url in ("https://vendor.example/docs/api/httprequest",
                    "https://other-vendor.example/documentation/module/x"):
            self.assertEqual(kinds.from_url(url), "vendor-doc", url)

    def test_an_ordinary_article_url_is_not_guessed(self):
        self.assertEqual(kinds.from_url("https://blog.example.org/2019/08/getting-shell/"), "")


class TestAWaybackReplayIsNotItsOwnKind(unittest.TestCase):
    """The replay carries the ARCHIVE's host, so every host rule read the
    wrapper: YouTube talks cited as replays were filed as `article`, which sent
    a video into the browser ladder and onto the document-gaps list as though a
    write-up were missing."""

    def test_a_captured_video_is_still_a_video(self):
        self.assertEqual(kinds.from_url(
            "http://web.archive.org/web/20160507023636/"
            "https://www.youtube.com/watch?v=ERJmkLxGRC0"), "video")

    def test_a_captured_pdf_is_still_a_whitepaper(self):
        self.assertEqual(kinds.from_url(
            "https://web.archive.org/web/20170903113359id_/"
            "http://media.blackhat.com/bh-us-12/Briefings/x/paper.pdf"), "whitepaper")

    def test_a_captured_ordinary_article_is_still_not_guessed(self):
        self.assertEqual(kinds.from_url(
            "https://web.archive.org/web/20160403035045/"
            "http://blog.example.org/2014/10/post.html"), "")

    def test_the_archive_itself_is_not_mistaken_for_a_capture(self):
        self.assertEqual(kinds.from_url("https://web.archive.org/"), "")


class TestExecutablesAreNeverDownloaded(unittest.TestCase):
    """A program is not a document. Fetching one gains nothing - the technique
    lives in the write-up - and puts an executable on the maintainer's disk and
    into the content store."""

    def test_executables_across_every_platform(self):
        for url in ("https://example.org/tool.exe", "https://example.org/lib.dll",
                    "https://example.org/app.dmg", "https://example.org/pkg.deb",
                    "https://example.org/pkg.rpm", "https://example.org/app.apk",
                    "https://example.org/tool.jar", "https://example.org/mod.so",
                    "https://example.org/x.appimage", "https://example.org/disk.iso"):
            self.assertEqual(kinds.from_url(url), "executable", url)

    def test_a_format_that_only_looks_harmless(self):
        """`.chm` reads as a help file and is a compiled, scriptable Windows
        binary. Judge by what a format can execute, not by how its name sounds."""
        for url in ("https://example.org/manual.chm", "https://example.org/page.hta",
                    "https://example.org/shortcut.lnk", "https://example.org/x.scr"):
            self.assertEqual(kinds.from_url(url), "executable", url)

    def test_an_archive_is_refused_because_its_contents_are_unknown(self):
        for url in ("https://sensepost.com/research/reDuh/SensePost_2008.tgz",
                    "https://secforce.co.uk/media/tools/socket_attack.zip",
                    "https://example.org/x.7z", "https://example.org/x.tar.gz"):
            self.assertEqual(kinds.from_url(url), "executable", url)

    def test_source_text_is_not_an_executable(self):
        """Source is read as text and never run, so it stays archivable."""
        for url, kind in (("https://example.org/exploit.py", "code"),
                          ("https://example.org/poc.ps1", "code"),
                          ("https://example.org/x.cs", "code"),
                          ("https://example.org/paper.pdf", "whitepaper")):
            self.assertEqual(kinds.from_url(url), kind, url)

    def test_the_ban_beats_every_other_rule(self):
        """A `.zip` on a video host, a slide host or GitHub is still an archive."""
        self.assertEqual(kinds.from_url("https://speakerdeck.com/x/deck.zip"), "executable")
        self.assertEqual(
            kinds.from_url("https://github.com/owner/name/blob/main/tool.exe"), "executable")

    def test_never_download_names_the_kind(self):
        self.assertTrue(kinds.never_download("executable"))
        for kind in ("article", "whitepaper", "slides", "video", "code", "repo"):
            self.assertFalse(kinds.never_download(kind), kind)


class TestKindFromResponse(unittest.TestCase):
    def test_an_unremarkable_page_falls_back_to_article(self):
        self.assertEqual(kinds.from_response("https://blog.example.org/x", "text/html"), "article")

    def test_a_pdf_content_type_wins_over_a_pathless_url(self):
        self.assertEqual(kinds.from_response("https://example.org/download?id=7",
                                             "application/pdf"), "whitepaper")

    def test_the_url_still_decides_when_it_is_unambiguous(self):
        self.assertEqual(kinds.from_response("https://youtube.com/watch?v=x", "text/html"), "video")


class TestBrowserScope(unittest.TestCase):
    def test_a_video_is_never_worth_the_browser_ladder(self):
        self.assertFalse(kinds.wants_browser("video"))

    def test_an_article_and_an_advisory_are(self):
        self.assertTrue(kinds.wants_browser("article"))
        self.assertTrue(kinds.wants_browser("advisory"))


if __name__ == "__main__":
    unittest.main()
