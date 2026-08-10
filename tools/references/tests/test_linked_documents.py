"""Conservative discovery of a paper behind its publication landing page."""

from . import support  # noqa: F401

import unittest

from refslib import linked_documents


class TestLinkedDocuments(unittest.TestCase):
    def test_pdf_code_and_slides_are_recognised(self):
        page = ('<a href="paper.pdf">PDF</a>'
                '<a href="https://github.com/example/tool">Code</a>'
                '<a href="slides.pdf">Slides</a>')
        result = linked_documents.discover(page, "https://lab.test/publication/")
        self.assertEqual(result.primary, "https://lab.test/publication/paper.pdf")
        self.assertEqual(result.companions, [
            "https://lab.test/publication/paper.pdf",
            "https://github.com/example/tool",
            "https://lab.test/publication/slides.pdf",
        ])

    def test_an_unlabelled_cv_is_not_guessed_as_the_paper(self):
        result = linked_documents.discover(
            '<a href="author-cv.pdf">Author biography</a>', "https://lab.test/")
        self.assertEqual(result.primary, "")

    def test_two_labelled_papers_require_a_human_choice(self):
        result = linked_documents.discover(
            '<a href="a.pdf">PDF</a><a href="b.pdf">Full paper</a>',
            "https://lab.test/")
        self.assertEqual(result.primary, "")


class TestThePagesOwnPaper(unittest.TestCase):
    """A research post that offers itself as a PDF should be archived as that
    PDF, not as our text render of it. Same-site alone matched 215 documents in
    this archive - a DMCA form, a CV, an affidavit; with the phrase test, 18."""

    ARTICLE = "https://portswigger.net/research/splitting-the-email-atom"

    def test_a_print_download_friendly_pdf_is_the_paper(self):
        found = linked_documents.paper_link(
            "You can also get this paper as a [print/download friendly]"
            "(https://portswigger.net/kb/papers/rclapqr/splitting-the-email-atom.pdf)"
            " PDF.", self.ARTICLE)
        self.assertEqual(
            found,
            "https://portswigger.net/kb/papers/rclapqr/splitting-the-email-atom.pdf")

    def test_somebody_elses_paper_is_not_this_documents_paper(self):
        found = linked_documents.paper_link(
            "Read [the original paper](https://example.test/other-research.pdf).",
            self.ARTICLE)
        self.assertEqual(found, "")

    def test_a_same_site_pdf_with_no_claim_on_the_document_is_ignored(self):
        found = linked_documents.paper_link(
            "See our [Downloadable CV](https://portswigger.net/files/cv.pdf).",
            self.ARTICLE)
        self.assertEqual(found, "")

    def test_a_recovered_page_is_compared_with_what_it_captured(self):
        """A Wayback capture IS `web.archive.org`, which made every link on the
        page look same-site."""
        found = linked_documents.paper_link(
            "Get the [whitepaper](https://web.archive.org/web/2016id_/"
            "http://lab.test/paper.pdf).",
            "https://web.archive.org/web/2016id_/http://lab.test/research")
        self.assertEqual(found, "http://lab.test/paper.pdf")

    def test_nothing_is_found_without_a_source_url_to_compare_against(self):
        self.assertEqual(
            linked_documents.paper_link("[whitepaper](https://x.test/p.pdf)", ""), "")


if __name__ == "__main__":
    unittest.main()
