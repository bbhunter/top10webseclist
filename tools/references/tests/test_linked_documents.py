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


if __name__ == "__main__":
    unittest.main()
