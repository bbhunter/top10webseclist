"""Trimming the publisher's furniture off a converted document.

Every pattern here came from counting the trailing blocks of all 503 archived
documents, and so did every case that must SURVIVE.
"""

from . import support  # noqa: F401

import unittest

from refslib import boilerplate

ARTICLE = ("# Exploiting the parser\n\n"
           + "The front end forwards the smuggled prefix to the back end here. " * 30)


class TestTheRealTails(unittest.TestCase):
    """The exact endings found in the corpus."""

    def test_a_consultancy_call_to_action_footer_goes(self):
        text, removed = boilerplate.trim(
            ARTICLE + "\n\n## Ready to engage\nwith our team?\n\n"
            "[ Get in touch ](https://vendor.example/contact)\n\n Copyright 2026 The Vendor\n")
        self.assertNotIn("Get in touch", text)
        self.assertNotIn("Copyright 2026", text)
        self.assertIn("smuggled prefix", text)
        self.assertIn("call-to-action", removed)
        self.assertIn("copyright", removed)

    def test_the_vendor_panel_goes(self):
        text, removed = boilerplate.trim(
            ARTICLE + "\n\nSubmit a vulnerability\n\n](https://example.org/portal/login/) [\n\n"
            "#### VENDORS\n\nLearn how it works\n\n](https://example.org/about/benefits/)\n")
        self.assertNotIn("Learn how it works", text)
        self.assertNotIn("VENDORS", text)
        self.assertIn("smuggled prefix", text)

    def test_the_medium_image_hint_goes_wherever_it_is(self):
        text, removed = boilerplate.trim(
            "Press enter or click to view image in full size\n\n" + ARTICLE
            + "\n\nPress enter or click to view image in full size\n")
        self.assertNotIn("Press enter or click", text)
        self.assertIn("image-caption-hint", removed)


class TestWhatMustSurvive(unittest.TestCase):
    """The headings a sweep of the corpus found at the end of real documents."""

    def test_a_references_section_is_not_furniture(self):
        for heading in ("## References", "## See also", "## Conclusion",
                        "### Disclosure timeline", "### Credit", "## Transcript"):
            text, _removed = boilerplate.trim(ARTICLE + "\n\n" + heading
                                              + "\n\n- Something worth keeping\n")
            self.assertIn(heading, text, heading)

    def test_a_slide_whose_alt_text_is_the_slide_survives(self):
        """On a slide host every slide is an image whose ALT TEXT is the slide.
        A rule that matched any image-only block deleted 2,115 characters of one
        deck: the mitigations, the conclusions and the questions slide."""
        deck = (ARTICLE + "\n\n![ACTUAL MITIGATIONS\nNEVER FORWARD AN AMBIGUOUS REQUEST]"
                "(https://example.org/slide-40.jpg)\n")
        text, _removed = boilerplate.trim(deck)
        self.assertIn("NEVER FORWARD", text)

    def test_a_decorative_image_with_no_alt_text_goes(self):
        text, removed = boilerplate.trim(ARTICLE + "\n\n![](https://example.org/spacer.gif)\n")
        self.assertIn("image-only", removed)

    def test_furniture_in_the_MIDDLE_of_an_article_stays(self):
        """Trimming works inward from the edges and stops at the first real
        block. An advert mid-article is the price of not guessing."""
        text, _removed = boilerplate.trim(
            ARTICLE + "\n\nContact us today!\n\n" + ARTICLE)
        self.assertIn("Contact us today!", text)

    def test_a_code_block_is_never_furniture(self):
        text, _removed = boilerplate.trim(
            ARTICLE + "\n\n```\n// contact us for the full exploit\n```\n")
        self.assertIn("contact us for the full exploit", text)

    def test_a_long_block_is_never_furniture(self):
        essay = "Get in touch with the vendor because " * 40
        text, _removed = boilerplate.trim(ARTICLE + "\n\n" + essay + "\n")
        self.assertIn("Get in touch with the vendor", text)


class TestTheShareLimit(unittest.TestCase):
    """No trim may take a large share of the document, the same rule the
    container chrome removal already lives under."""

    def test_a_document_that_is_mostly_furniture_is_left_alone(self):
        text, _removed = boilerplate.trim(
            "A short note.\n\nGet in touch\n\nContact us\n\nCopyright 2026 X\n")
        self.assertIn("Get in touch", text)

    def test_nothing_is_removed_from_an_empty_document(self):
        self.assertEqual(boilerplate.trim("")[1], [])


class TestDeadLinks(unittest.TestCase):
    """`[Data request]()` is what a table of contents, a footnote arrow and a
    collapsible toggle convert to, and 6,132 of them were published as literal
    brackets across 425 files. A link with no target is not a link."""

    def test_a_dead_link_keeps_its_label_and_loses_its_brackets(self):
        text, removed = boilerplate.drop_dead_links(
            "- [Data request]()\n- [Data fetching]()\n")
        self.assertEqual(text, "- Data request\n- Data fetching\n")
        self.assertEqual(removed, ["dead-link"])

    def test_a_live_link_is_untouched(self):
        source = "See [the paper](https://example.test/paper.pdf) for the proof.\n"
        text, removed = boilerplate.drop_dead_links(source)
        self.assertEqual(text, source)
        self.assertEqual(removed, [])

    def test_an_anchor_around_block_content_loses_only_its_brackets(self):
        text, removed = boilerplate.drop_dead_links("[\n\nTOC Element\n\n]()\n")
        self.assertEqual(text.strip(), "TOC Element")
        self.assertIn("dead-block-anchor", removed)

    def test_an_image_with_no_source_goes(self):
        text, removed = boilerplate.drop_dead_links("![diagram]()\n\nThe proof.\n")
        self.assertEqual(text.strip(), "The proof.")
        self.assertIn("dead-image", removed)

    def test_the_glyph_a_dead_anchor_wrapped_goes_with_it(self):
        text, _removed = boilerplate.drop_dead_links("Body.\n\n[  ►  ]()\n\nMore.\n")
        self.assertNotIn("►", text)
        self.assertIn("More.", text)

    def test_a_horizontal_rule_is_not_decoration(self):
        text, _removed = boilerplate.drop_dead_links("One.\n\n***\n\n[x]()\n\nTwo.\n")
        self.assertIn("***", text)

    def test_markdown_quoted_inside_a_fence_is_never_rewritten(self):
        """A write-up about Markdown injection quotes this syntax on purpose."""
        source = "Payload:\n\n```\n[click]()\n```\n\nThat is the bug.\n"
        text, removed = boilerplate.drop_dead_links(source)
        self.assertIn("[click]()", text)
        self.assertEqual(removed, [])

    def test_it_is_idempotent(self):
        once, _removed = boilerplate.drop_dead_links("- [A]()\n- [B](https://x.test)\n")
        twice, removed = boilerplate.drop_dead_links(once)
        self.assertEqual(once, twice)
        self.assertEqual(removed, [])

    def test_a_document_cannot_forge_the_token_that_holds_a_code_block(self):
        """The fenced blocks are held behind `\\x00N\\x00` while the rest is
        rewritten, and this runs before control characters are stripped."""
        text, _removed = boilerplate.drop_dead_links(
            "```\nreal payload\n```\n\nforged: \x000\x00\n\n[x]()\n")
        self.assertEqual(text.count("real payload"), 1)
        self.assertNotIn("\x00", text)

    def test_a_stray_bracket_cannot_swallow_the_article(self):
        source = "[\n\n" + ("Real content. " * 200) + "\n\n]()\n"
        text, _removed = boilerplate.drop_dead_links(source)
        self.assertIn("Real content.", text)
        self.assertGreater(len(text), 2000)


if __name__ == "__main__":
    unittest.main()
