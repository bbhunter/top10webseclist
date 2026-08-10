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


class TestSalesPanel(unittest.TestCase):
    """Removing furniture one block at a time cannot clear a sales panel: the
    sweep stops at the first block no rule matches, and a panel is mostly
    ordinary sentences. Six Searchlight Cyber write-ups ended with seven blocks
    of them."""

    PANEL = ("\n\n#### in this article\n\n"
             "## Book your demo: Identify cyber threats earlier\n\n"
             "Searchlight Cyber is used by security professionals to surface "
             "criminal activity.\n\n"
             "**Enhance your security** with automated dark web monitoring\n\n"
             "**Continuously monitor for threats**, including ransomware groups\n\n"
             "**Prevent costly cyber incidents** and meet compliance requirements\n\n"
             "## Fill in the form to get you demo\n")

    def test_the_whole_panel_goes_from_its_heading(self):
        text, removed = boilerplate.trim(ARTICLE + self.PANEL)
        for phrase in ("Book your demo", "Enhance your security",
                       "Fill in the form", "in this article"):
            self.assertNotIn(phrase, text)
        self.assertIn("smuggled prefix", text)
        self.assertIn("sales-panel", removed)

    def test_a_panel_is_never_taken_across_a_code_block(self):
        """A listing below the heading means it is not a sales panel."""
        text, _removed = boilerplate.trim(
            ARTICLE + "\n\n## Get your demo\n\n```\nGET / HTTP/1.1\n```\n")
        self.assertIn("GET / HTTP/1.1", text)

    def test_a_panel_may_not_take_most_of_the_document(self):
        text, _removed = boilerplate.trim("# T\n\n## Book your demo\n\n" + "x " * 20)
        self.assertIn("Book your demo", text)


class TestTrailingEmptySections(unittest.TestCase):
    """A heading with nothing under it, from a MEASURED vocabulary. "Any bare
    heading" would have taken `## evercookie, by samy kamkar, 2010/09/20` - the
    document's own title - and `# # # End Advisory # # #`."""

    def test_a_furniture_heading_left_empty_goes(self):
        text, removed = boilerplate.trim(ARTICLE + "\n\n## Related Research\n")
        self.assertNotIn("Related Research", text)
        self.assertIn("empty-section", removed)

    def test_the_documents_own_title_is_not_furniture(self):
        title = "## evercookie, by [samy kamkar](mailto:code@sa.my), 2010/09/20"
        text, _removed = boilerplate.trim(ARTICLE + "\n\n" + title + "\n")
        self.assertIn("evercookie", text)

    def test_an_advisorys_own_last_line_is_not_furniture(self):
        text, _removed = boilerplate.trim(ARTICLE + "\n\n# # # End Advisory # # #\n")
        self.assertIn("End Advisory", text)

    def test_a_missing_presentation_video_still_says_so(self):
        """Its body was an iframe that sanitisation removes by design, so the
        heading is the only trace that a recording exists."""
        text, _removed = boilerplate.trim(ARTICLE + "\n\n## Presentation Video\n")
        self.assertIn("Presentation Video", text)

    def test_a_bare_heading_at_the_head_is_never_touched(self):
        text, _removed = boilerplate.trim("## Related Research\n\n" + ARTICLE)
        self.assertIn("Related Research", text)


class TestPublisherLinkFurniture(unittest.TestCase):
    """Every archived Medium article opened with its byline avatar rendered as a
    literal `[`, the picture, and then the whole profile URL as text - because an
    anchor wrapping BLOCK content is not a Markdown link. 975 of those, and 3,980
    invisible sign-in buttons."""

    def test_a_block_anchor_becomes_a_link_on_one_line(self):
        text, removed = boilerplate.tidy_links(
            "[\n\n![Author](https://cdn.test/a.png)\n\n](https://author.test/profile)\n")
        self.assertEqual(
            text.strip(),
            "[![Author](https://cdn.test/a.png)](https://author.test/profile)")
        self.assertIn("block-anchor", removed)

    def test_an_anchor_with_nothing_to_click_goes(self):
        text, removed = boilerplate.tidy_links(
            "Body.\n\n[ ](https://medium.test/m/signin?operation=register)\n\nMore.\n")
        self.assertNotIn("signin", text)
        self.assertIn("Body.", text)
        self.assertIn("More.", text)
        self.assertIn("textless-link", removed)

    def test_an_image_with_no_alt_text_is_not_a_textless_link(self):
        """`![](figure.png)` ends in exactly the shape the textless-link rule
        matches. Without a `(?<!!)` guard it deleted the image and left the `!`:
        3,531 figures across 509 documents, while their preserved copies sat in
        the store with nothing left pointing at them."""
        source = "Before.\n\n![](https://cdn.test/encode.png)\n\nAfter.\n"
        text, removed = boilerplate.tidy_links(source)
        self.assertEqual(text, source)
        self.assertEqual(removed, [])

    def test_an_image_with_alt_text_is_also_untouched(self):
        source = "![a diagram](https://cdn.test/decode.png)\n"
        self.assertEqual(boilerplate.tidy_links(source)[0], source)

    def test_a_linked_image_with_no_alt_text_survives_whole(self):
        source = "[![](https://cdn.test/logo.png)](https://vendor.test/)\n"
        self.assertEqual(boilerplate.tidy_links(source)[0], source)

    def test_a_button_wearing_a_links_clothes_goes(self):
        text, removed = boilerplate.tidy_links(
            "[\n\nListen\n\n](https://medium.test/m/signin?dimension=post_audio_button)\n")
        self.assertNotIn("Listen", text)
        self.assertIn("social-button-link", removed)

    def test_a_real_link_that_happens_to_say_share_survives(self):
        """The label alone is not evidence; the target has to admit it too."""
        source = "Read [Share](https://research.test/sharing-sessions) for the detail.\n"
        text, _removed = boilerplate.tidy_links(source)
        self.assertEqual(text, source)

    def test_an_ordinary_inline_link_is_untouched(self):
        source = "See [the paper](https://example.test/p.pdf) for proof.\n"
        self.assertEqual(boilerplate.tidy_links(source)[0], source)

    def test_it_is_idempotent(self):
        once, _ = boilerplate.tidy_links(
            "[\n\n![A](https://cdn.test/a.png)\n\n](https://a.test/p)\n")
        twice, removed = boilerplate.tidy_links(once)
        self.assertEqual(once, twice)
        self.assertEqual(removed, [])

    def test_a_fenced_example_is_never_rewritten(self):
        source = "Payload:\n\n```\n[ ](https://x.test/signin)\n```\n\nDone.\n"
        self.assertEqual(boilerplate.tidy_links(source)[0], source)


class TestJunkLines(unittest.TestCase):
    """Lines that describe the website's behaviour rather than the document."""

    def test_the_reading_time_and_social_words_go(self):
        text, removed = boilerplate.drop_junk_lines(
            "# Title\n\nFollow\n\n9 min readFeb 21, 2022\n\nListen\n\nShare\n\n# TL;DR\n")
        for word in ("Follow", "Listen", "Share", "min read"):
            self.assertNotIn(word, text)
        self.assertIn("# TL;DR", text)
        self.assertIn("social-button", removed)
        self.assertIn("reading-time", removed)

    def test_a_clap_counter_goes_only_as_a_pair(self):
        text, removed = boilerplate.drop_junk_lines("a\n\n--\n\n3\n\nb\n")
        self.assertNotIn("--", text)
        self.assertIn("clap-counter", removed)

    def test_a_lone_sql_comment_line_is_not_a_clap_counter(self):
        """A line containing only `--` is a comment payload in this corpus."""
        source = "The payload ends with\n\n--\n\nand the rest is ignored.\n"
        text, removed = boilerplate.drop_junk_lines(source)
        self.assertEqual(text, source)
        self.assertEqual(removed, [])

    def test_a_payload_inside_a_fence_survives_all_of_it(self):
        source = "x\n\n```sql\nSELECT 1\n--\n\n7\nShare\n```\n\ny\n"
        text, removed = boilerplate.drop_junk_lines(source)
        self.assertIn("SELECT 1", text)
        self.assertIn("Share", text)
        self.assertEqual(removed, [])

    def test_prose_that_merely_contains_the_word_is_untouched(self):
        source = "Follow the redirect and share the session cookie.\n"
        self.assertEqual(boilerplate.drop_junk_lines(source)[0], source)


if __name__ == "__main__":
    unittest.main()
