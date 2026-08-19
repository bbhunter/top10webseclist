"""Document conversion, and the gate that stops confident nonsense."""

from . import support  # noqa: F401

import unittest
import zlib

from refslib import extract_doc


def pdf_with(stream_text):
    stream = zlib.compress(stream_text)
    header = (b"%PDF-1.4\n1 0 obj\n<< /Length " + str(len(stream)).encode("ascii")
              + b" /Filter /FlateDecode >>\nstream\n")
    return header + stream + b"\nendstream\nendobj\n%%EOF"


REAL = (b"BT (Request smuggling past the front end lets an attacker reach the back.) Tj ET "
        b"BT (The front end forwards the smuggled prefix to the back end here-oh.) Tj ET "
        b"BT (This paragraph exists so the sample clears the word count floor easily.) Tj ET")

# What a custom /Differences or CID font produces when the encoding map is
# ignored: the right shape, the right length, and not a word of it real.
GIBBERISH = (b"BT (kfjw qxzb mnpr wxvz kfjw qxzb mnpr wxvz kfjw qxzb mnpr) Tj ET "
             b"BT (wxvz kfjw qxzb mnpr wxvz kfjw qxzb mnpr wxvz kfjw qxzb) Tj ET "
             b"BT (mnpr wxvz kfjw qxzb mnpr wxvz kfjw qxzb mnpr wxvz kfjw) Tj ET")


class TestMismappedLigatures(unittest.TestCase):
    """A face whose ligature table was read at the wrong code points."""

    # Sized like the paper it comes from: a mis-mapped face breaks every
    # ligature in the document, which is exactly what the floor tests for.
    BROKEN = ("Browser €ngerprinting remains a topic of interest, and various "
              "anti-€ngerprinting countermeasures have drawn signi€cant "
              "a‹ention. ‘ese a‹ributes are implicitly inferred, and di‚erent "
              "elements have di‚erent sizes, which demonstrates the "
              "e‚ectiveness of the overƒow-block dra‰ we cra‰ed. ") * 5

    def test_the_ligatures_are_put_back(self):
        fixed, changes = extract_doc.repair_ligatures(self.BROKEN)
        self.assertGreater(changes, 8)
        for word in ("fingerprinting", "significant", "attention", "attributes",
                     "These", "different", "effectiveness", "overflow-block",
                     "draft", "crafted"):
            self.assertIn(word, fixed)
        for glyph in extract_doc.LIGATURE_EVIDENCE:
            self.assertNotIn(glyph, fixed)

    def test_a_bullet_list_in_the_same_face_is_left_alone(self):
        """Two papers set list markers in this face; `€` there is a bullet.

        They spell their own fi as "certi“cate", so `€` cannot also be fi, and
        rewriting it would turn a correct sentence into "fiwe define".
        """
        bullets = ("Contributions In this paper,€we de“ne a composite state "
                   "machine;€we present tools to test implementations;€we "
                   "report ”aws and countermeasures;€we develop a veri“ed "
                   "state machine that renders three different forms:€a "
                   "sphere€a cube€a Torus knot, as described below.")
        fixed, changes = extract_doc.repair_ligatures(bullets)
        self.assertEqual(0, changes)
        self.assertEqual(bullets, fixed)

    def test_an_ordinary_price_and_quotation_are_untouched(self):
        plain = ("The service costs €25 a month, and the author called it "
                 "‘a reasonable price' in the report, twice over.")
        self.assertEqual((plain, 0), extract_doc.repair_ligatures(plain))

    def test_stacked_ligatures_resolve(self):
        """"fifth" is set as fi + ft + h, so one pass leaves `€fth`."""
        text = self.BROKEN + (" Iframe A is in the €‰h row of the grid, and "
                              "the €‰h column repeats it.")
        fixed, _n = extract_doc.repair_ligatures(text)
        self.assertIn("fifth", fixed)
        self.assertNotIn("€", fixed)

    def test_a_lost_glyph_is_read_from_the_letter_that_follows(self):
        """U+FFFD stood for both `ffi` and `Qu`; only the next letter tells."""
        text = self.BROKEN + (" The system rea�rms that it is di�cult and "
                              "su�ciently distinct, so we reduce network "
                              "tra�c. See Media �eries Level 5 and "
                              "�antifying the rest of it.")
        fixed, _n = extract_doc.repair_ligatures(text)
        for word in ("reaffirms", "difficult", "sufficiently", "traffic",
                     "Queries", "Quantifying"):
            self.assertIn(word, fixed)
        self.assertNotIn("�", fixed)


class TestPdfConversion(unittest.TestCase):
    def test_real_text_converts_with_page_markers(self):
        markdown = extract_doc.pdf_to_markdown(pdf_with(REAL), "A Paper")
        self.assertIn("# A Paper", markdown)
        self.assertIn("--- page 1 ---", markdown)
        self.assertIn("Request smuggling past the front end", markdown)

    def test_something_that_is_not_a_pdf_is_refused(self):
        with self.assertRaises(extract_doc.Unconvertible) as caught:
            extract_doc.pdf_to_markdown(b"<html>not a pdf</html>")
        self.assertIn("not a PDF", str(caught.exception))

    def test_an_image_only_pdf_says_it_needs_ocr(self):
        with self.assertRaises(extract_doc.Unconvertible) as caught:
            extract_doc.pdf_to_markdown(b"%PDF-1.4\nno streams\n%%EOF")
        self.assertIn("OCR", str(caught.exception))

    def test_reading_a_fraction_of_the_pages_goes_to_the_external_tool(self):
        """Reading SOME of a paper is the quiet failure: what comes back is real
        text and passes every check made on it. One 95-page paper published as
        2,131 characters of page one this way."""
        one_page = pdf_with(REAL) + b"\n/Type /Page \n" * 40
        with self.assertRaises(extract_doc.ExternalPdfToolRequired) as caught:
            extract_doc.pdf_to_markdown(one_page)
        self.assertIn("40 pages", str(caught.exception))

    def test_a_short_document_is_not_second_guessed(self):
        """The test is lopsided on purpose. A handful of pages read as one
        stream is ordinary, and sending those to a container would be a cost
        paid on every short write-up in the archive."""
        short = pdf_with(REAL) + b"\n/Type /Page \n" * 3
        self.assertIn("Request smuggling", extract_doc.pdf_to_markdown(short))

    def test_a_page_tree_it_cannot_count_never_fires_the_guard(self):
        """A compressed page tree counts zero pages, and zero must not be read
        as "read none of it"."""
        self.assertEqual(extract_doc.declared_pages(pdf_with(REAL)), 0)
        self.assertIn("Request smuggling", extract_doc.pdf_to_markdown(pdf_with(REAL)))

    def test_finding_no_text_is_raised_as_its_own_kind(self):
        """"No text HERE" is not "no text". This parser skips any stream it
        cannot inflate or decode, and a sweep filed 36 ordinary conference
        papers as scans on its word alone - every one just under the size that
        would have sent it to Poppler, which reads them in full. The distinct
        class is what lets `acquire` go and ask before believing the verdict."""
        with self.assertRaises(extract_doc.NoTextLayer):
            extract_doc.pdf_to_markdown(b"%PDF-1.4\nno streams\n%%EOF")
        # Still an Unconvertible, so every existing handler keeps working.
        self.assertTrue(issubclass(extract_doc.NoTextLayer, extract_doc.Unconvertible))
        # ...and it must NOT be the safety-limit signal, which routes the same
        # way but means something else.
        self.assertFalse(issubclass(extract_doc.NoTextLayer,
                                    extract_doc.ExternalPdfToolRequired))

    def test_gibberish_is_refused_rather_than_archived(self):
        """A custom font encoding decodes to nonsense of the right shape.
        Archiving it would store confident nonsense in place of the paper."""
        with self.assertRaises(extract_doc.Unconvertible) as caught:
            extract_doc.pdf_to_markdown(pdf_with(GIBBERISH))
        self.assertIn("gibberish", str(caught.exception))

    def test_unreadable_font_is_sent_to_the_external_tool(self):
        """Damaged prose reads as prose, so the quality gate passes it.

        The paper is handed to poppler instead of archived with holes in its
        words. `acquire` catches this and re-reads the PDF in the container.
        """
        damaged = (b"BT (The system reafrms that the certi\xe2\x80\x9ccate is di\xef\xbf\xbdcult "
                   b"to validate here.) Tj ET "
                   b"BT (We identi\xef\xbf\xbded a speci\xe2\x80\x9cc \xef\xbf\xbdaw in the "
                   b"implementation of the parser.) Tj ET "
                   b"BT (This paragraph exists so the sample clears the word count "
                   b"floor easily enough.) Tj ET")
        with self.assertRaises(extract_doc.ExternalPdfToolRequired) as caught:
            extract_doc.pdf_to_markdown(pdf_with(damaged))
        self.assertIn("font's encoding", str(caught.exception))

    def test_a_lost_glyph_with_one_reading_is_put_back(self):
        """`h?p://` is "http://" and can be nothing else.

        Poppler cannot recover it either, because the font maps the `tt`
        ligature to a code point with no Unicode meaning at all.
        """
        text = ("Send the token to h\ufffdp://example.test/a and then to "
                "h\ufffdps://example.test/b over h\ufffdp as well.")
        fixed, changes = extract_doc.repair_lost_words(text)
        self.assertEqual(3, changes)
        self.assertIn("http://example.test/a", fixed)
        self.assertIn("https://example.test/b", fixed)
        self.assertNotIn("\ufffd", fixed)

    def test_a_lost_glyph_with_several_readings_is_left_alone(self):
        text = "The rea\ufffdrms and di\ufffdcult cases stay as they are here."
        self.assertEqual((text, 0), extract_doc.repair_lost_words(text))

    def test_healthy_prose_with_ordinary_quotes_is_not_escalated(self):
        """A quotation is not damage: only a quote BETWEEN letters is."""
        quoted = ("The author called it “a reasonable defence” and the "
                  "report said “this works”, which we don’t dispute "
                  "at all. The front end forwards the smuggled prefix onward.")
        self.assertEqual(0, extract_doc.font_damage(quoted))

    def test_a_deleted_ligature_is_sent_to_the_external_tool(self):
        """The damage that leaves nothing behind to count.

        A face whose `fi`/`ff`/`fl` map to nothing DELETES them, so there is no
        replacement character for `font_damage` to find and every quality gate
        passes text reading "signicant" and "congurations".
        """
        damaged = (b"BT (The cache is signicant here and its congurations are "
                   b"specic to one deployment.) Tj ET "
                   b"BT (We conrm the result and dene the threshold used "
                   b"throughout the evaluation section.) Tj ET "
                   b"BT (This paragraph exists so the sample clears the word "
                   b"count floor easily enough.) Tj ET")
        with self.assertRaises(extract_doc.ExternalPdfToolRequired) as caught:
            extract_doc.pdf_to_markdown(pdf_with(damaged))
        self.assertIn("ligatures were dropped", str(caught.exception))

    def test_english_words_that_merely_look_damaged_are_left_alone(self):
        """`identical`, `classic` and `notice` are words, not lost ligatures.

        A suffix-wildcard version of this test matched all three, plus the
        company name Prolexic, across 709 archived documents.
        """
        healthy = ("The two responses are identical, which is a classic sign "
                   "that nobody would notice the classical padding oracle or "
                   "the identification header Prolexic adds.")
        self.assertEqual((0, 0), extract_doc.dropped_ligatures(healthy))

    def test_one_damaged_word_alone_is_a_typo_rather_than_a_font(self):
        self.assertEqual((1, 1), extract_doc.dropped_ligatures(
            "The result is signicant."))

    def test_oversized_decoded_stream_is_sent_to_external_tool(self):
        payload = b"x" * (extract_doc.MAX_LIGHTWEIGHT_STREAM_BYTES + 1)
        with self.assertRaises(extract_doc.ExternalPdfToolRequired):
            extract_doc.pdf_to_markdown(pdf_with(payload))


class TestTextQuality(unittest.TestCase):
    def test_ordinary_technical_prose_passes(self):
        ok, _reason = extract_doc.text_quality(
            "The front end forwards a request whose chunked length has been "
            "rewritten, which poisons the socket and serves the smuggled prefix. " * 4)
        self.assertTrue(ok)

    def test_vowelless_word_soup_fails(self):
        ok, reason = extract_doc.text_quality("kfjw qxzb mnpr wxvz " * 40)
        self.assertFalse(ok)
        self.assertIn("vowel", reason)

    def test_replacement_characters_fail(self):
        ok, reason = extract_doc.text_quality("Some text " + ("�" * 60))
        self.assertFalse(ok)
        self.assertIn("decode", reason)

    def test_symbol_soup_fails(self):
        ok, reason = extract_doc.text_quality("#$%^&*()_+{}|<>?~" * 40)
        self.assertFalse(ok)

    def test_non_latin_text_is_not_judged_on_vowels(self):
        """CJK has no ASCII vowels at all, and is perfectly good prose."""
        ok, _reason = extract_doc.text_quality("请求走私漏洞利用分析与防御方法研究" * 20)
        self.assertTrue(ok)

    def test_empty_text_fails(self):
        self.assertFalse(extract_doc.text_quality("")[0])


class TestCaptions(unittest.TestCase):
    def test_timing_and_cue_numbers_are_stripped(self):
        vtt = ("WEBVTT\n\n1\n00:00:01.000 --> 00:00:03.000\nHello there\n\n"
               "2\n00:00:03.000 --> 00:00:05.000\nsecond line\n")
        text = extract_doc.captions_to_markdown(vtt, "A talk")
        self.assertIn("Hello there second line", text)
        self.assertNotIn("00:00", text)
        self.assertNotIn("WEBVTT", text)

    def test_an_auto_generated_track_is_labelled(self):
        text = extract_doc.captions_to_markdown(
            "1\n00:00:01.000 --> 00:00:03.000\nWords here\n", "T", auto_generated=True)
        self.assertIn("auto-generated caption track", text)

    def test_an_empty_track_is_refused(self):
        with self.assertRaises(extract_doc.Unconvertible):
            extract_doc.captions_to_markdown("WEBVTT\n\n")


if __name__ == "__main__":
    unittest.main()


class TestUnreadablePagesAreFoundPerPage(unittest.TestCase):
    """A whole-document gate averages a broken page away: a deck with seven
    unreadable pages out of eight passed, because the eighth carried enough
    prose to lift the mean. Damage in a PDF is per page by nature."""

    def page(self, number, body):
        return "\n--- page %d ---\n%s\n" % (number, body)

    PROSE = ("The front end forwards the smuggled prefix to the back end here. " * 6)
    FONT_SOUP = "?" * 40 + "8ZJ??CR6N%GkQ??;XC&s=gR>*',TzM.TG8 5Rn/L5]#;O??:X<?87Ra??9???+X?"
    GLYPH_SOUP = "!\"#$%&'()*'+,()-'./01'2((%345!\"#$%&'()*&+',-./012312%45\"263$07%(8%&3"

    def test_one_broken_page_among_good_ones_is_found(self):
        text = (self.page(1, self.PROSE) + self.page(2, self.FONT_SOUP)
                + self.page(3, self.PROSE))
        found = extract_doc.unreadable_pages(text)
        self.assertEqual([number for number, _why in found], [2])

    def test_glyph_index_soup_is_found(self):
        found = extract_doc.unreadable_pages(self.page(1, self.GLYPH_SOUP))
        self.assertEqual(len(found), 1)

    def test_a_title_slide_with_no_spaces_between_runs_is_NOT_damage(self):
        """Measured: a PDF routinely emits "Desync AttacksJust the Tip of the
        IcebergA New Attack Surface", which is readable and has almost no
        word-shaped runs in it. Judging pages on the vowel test called 46
        readable title slides damaged."""
        run_together = ("Desync AttacksJust the Tip of the IcebergA New Attack Surface "
                        "on Reverse ProxiesA ResearcherUSA 2021")
        self.assertEqual(extract_doc.unreadable_pages(self.page(1, run_together)), [])

    def test_a_link_only_slide_is_not_damage(self):
        slide = "Web Cache Deceptionhttps://example.org/some/path/to/a/writeup/page"
        self.assertEqual(extract_doc.unreadable_pages(self.page(1, slide)), [])

    def test_a_very_short_page_is_not_judged(self):
        self.assertEqual(extract_doc.unreadable_pages(self.page(1, "Q&A")), [])

    def test_a_document_with_no_page_markers_reports_nothing(self):
        self.assertEqual(extract_doc.unreadable_pages(self.PROSE), [])


class TestATruncatedPdfIsRefused(unittest.TestCase):
    """Seven PDFs were stored at exactly 2,097,152 bytes - the fetcher's probe
    cap applied to a document - each still starting with %PDF- and so passing
    every magic-number check. The pages before the cut extracted fine and the
    pages after it came out as glyph soup, and nothing noticed."""

    def test_a_pdf_that_does_not_end_with_eof_is_reported(self):
        cut = extract_doc.looks_truncated(b"%PDF-1.4\n" + b"x" * 5000)
        self.assertIn("cut off", cut)

    def test_a_whole_pdf_is_accepted(self):
        self.assertEqual(extract_doc.looks_truncated(b"%PDF-1.4\nbody\n%%EOF\n"), "")

    def test_something_that_is_not_a_pdf_is_not_this_function_s_business(self):
        self.assertEqual(extract_doc.looks_truncated(b"<html></html>"), "")

    def test_the_reason_names_the_size_so_a_cap_is_recognisable(self):
        cut = extract_doc.looks_truncated(b"%PDF-1.4\n" + b"x" * (2 * 1024 * 1024))
        self.assertIn("2097161", cut.replace(",", ""))


class TestKerningDrawnWordSpaces(unittest.TestCase):
    """A TJ array interleaves strings with horizontal adjustments, and plenty of
    typesetters - TeX above all - never emit a space character at all, drawing
    every word gap with one of those numbers. Dropping them cost a 566,247
    character doctoral thesis all but 951 of its spaces: `dataflow` survived as
    `data ow` and the title as `Code-ReuseAttacksinManagedProgramming`."""

    def test_a_wide_negative_adjustment_becomes_a_space(self):
        text = extract_doc._show_array(b"(Code)-278(Reuse)-278(Attacks)")
        self.assertEqual(text, "Code Reuse Attacks")

    def test_ordinary_kerning_does_not_become_a_space(self):
        """A letter pair is nudged by a few thousandths of an em."""
        self.assertEqual(extract_doc._show_array(b"(A)-30(V)-25(a)"), "AVa")

    def test_a_positive_adjustment_is_never_a_space(self):
        self.assertEqual(extract_doc._show_array(b"(A)120(B)"), "AB")

    def test_a_document_that_does_emit_spaces_is_unchanged(self):
        self.assertEqual(extract_doc._show_array(b"(Hello world)"), "Hello world")

    def test_a_fractional_adjustment_is_read(self):
        self.assertEqual(extract_doc._show_array(b"(a)-250.5(b)"), "a b")

    def test_the_threshold_sits_between_the_two_uses(self):
        """Below it is kerning, above it is a word break. Stated here so the
        number cannot drift without a test saying so."""
        self.assertGreater(extract_doc.SPACE_KERN, 100)
        self.assertLess(extract_doc.SPACE_KERN, 250)
