"""Preparing an archived document for translation, and putting one back.

The whole point of this module is that a translator must never touch the
payload. These documents are made of type names, CVE identifiers, base64 blobs
and shell commands, and every one of them is the research.
"""

from . import support  # noqa: F401

import unittest

from refslib import translate


class TestProtection(unittest.TestCase):
    """`XMLHttpRequest.prototype.open` translated into another language is not a
    smaller mistake than a mistranslated sentence - it is a corrupted payload."""

    def masked(self, text):
        return translate.protect(text)

    def test_a_fenced_block_is_taken_whole(self):
        masked, held = self.masked(
            "Prosa\n\n```javascript\nfetch('/collect?c=' + document.cookie);\n```\n")
        self.assertNotIn("document.cookie", masked)
        self.assertEqual(len(held), 1)

    def test_inline_code_a_url_and_a_cve_are_each_protected(self):
        masked, held = self.masked(
            "Vedi `document.cookie` su https://example.org/a per CVE-2025-53770.")
        self.assertNotIn("document.cookie", masked)
        self.assertNotIn("example.org", masked)
        self.assertNotIn("CVE-2025-53770", masked)
        self.assertEqual(len(held), 3)

    def test_a_dotted_identifier_is_protected(self):
        masked, _held = self.masked("Il tipo Object.prototype.toString e pericoloso.")
        self.assertNotIn("Object.prototype.toString", masked)

    def test_a_document_containing_our_own_placeholder_shape_cannot_collide(self):
        """A page that literally contains `{{PH_1}}` would otherwise have it
        restored as somebody else's code."""
        masked, held = self.masked("Testo {{PH_1}} altro testo")
        self.assertEqual(translate.restore(masked, held), "Testo {{PH_1}} altro testo")

    def test_everything_comes_back_byte_identical(self):
        original = ("Il payload usa `XMLHttpRequest.prototype.open` per "
                    "raggiungere /admin. Vedi https://example.org/x e CVE-2025-53770.\n\n"
                    "```http\nGET /admin HTTP/1.1\nHost: target.example\n```\n")
        masked, held = self.masked(original)
        self.assertEqual(translate.restore(masked, held), original)


class TestLostPlaceholders(unittest.TestCase):
    """A lost placeholder is a corrupted payload, so applying must refuse."""

    def test_a_dropped_placeholder_is_reported(self):
        held = {"{{PH_1}}": "`code`", "{{PH_2}}": "https://example.org"}
        lost = translate.missing_placeholders("The payload uses {{PH_1}}.", held)
        self.assertEqual(lost, ["{{PH_2}}"])

    def test_a_complete_translation_reports_nothing(self):
        held = {"{{PH_1}}": "`code`"}
        self.assertEqual(translate.missing_placeholders("Uses {{PH_1}} here.", held), [])


class TestLanguage(unittest.TestCase):
    def test_a_declared_foreign_language_is_believed(self):
        """A page that says it is Chinese is Chinese. Nobody sets that by
        accident, so it is better evidence than counting characters."""
        self.assertFalse(translate.looks_english("Any text at all", declared="zh"))

    def test_a_declared_english_still_has_to_survive_the_measurement(self):
        """A BLOGGING PLATFORM SETS `lang` ONCE FOR THE WHOLE SITE. Medium
        serves every post as `lang="en"`, so a Vietnamese write-up on it
        declared English and sat in the archive untranslated."""
        self.assertFalse(translate.looks_english("任意のテキスト" * 20, declared="en"))

    def test_a_vietnamese_post_declaring_english_is_caught(self):
        """The case that found this: a Vietnamese write-up hosted on Medium.
        Vietnamese is Latin script, so only the words give it away."""
        vietnamese = ("Trong bai viet nay chung ta se tim hieu ve lo hong "
                      "request smuggling cua may chu va cach khai thac no. "
                      "Khi doc du lieu, ung dung khong kiem tra do dai. " * 8)
        self.assertFalse(translate.looks_english(vietnamese, declared="en"))

    def test_an_english_page_declaring_english_is_left_alone(self):
        self.assertTrue(translate.looks_english(
            "The front end forwards the smuggled prefix to the back end here. " * 20,
            declared="en"))

    def test_a_conference_name_does_not_make_a_page_portuguese(self):
        """A short Romance stop word collides with English technical writing, and
        the cost of one collision is a whole English document queued for
        translation. Calibration: in the corpus these rules were tuned on, the
        worst offender fired 226 times across 22 English documents. That is why
        `com`, `con`, `des` and the rest are left out of the stop-word list -
        here it is `con`, which every DEF CON write-up carries."""
        self.assertTrue(translate.looks_english(
            "Presented at DEF CON, the talk walks the desync end to end. "
            "The DEF CON demo poisons the socket, then the DEF CON slides "
            "show the queued response. " * 8))

    def test_a_place_name_does_not_make_a_deck_spanish(self):
        """Half the conference decks in the archive say "Las Vegas"."""
        self.assertTrue(translate.looks_english(
            "Presented at the conference in Las Vegas, covering the desync "
            "and the socket it poisons during a read. " * 10))

    def test_a_terse_english_deck_is_not_foreign(self):
        """Slides, code listings and reference pages are made of fragments, so
        they carry few English function words. Judging on the ABSENCE of those
        flagged four plainly English documents for translation."""
        self.assertTrue(translate.looks_english(
            "Smuggled prefix. Socket poisoned. Response queued. Victim served. "
            "Nonce reflected. Header split. Cache keyed. Origin trusted. " * 8))

    def test_a_foreign_page_padded_with_english_is_still_foreign(self):
        """Exposing link text as translatable prose diluted a Vietnamese
        write-up below the old threshold and it reported itself English."""
        vietnamese = ("Trong bai viet nay chung ta se tim hieu ve lo hong cua "
                      "ung dung khi doc du lieu tu nguoi dung. " * 4)
        # Fifteen words per repetition, as the measurement above depended on:
        # this dilutes the Vietnamese share to 0.0299, just over the threshold.
        padding = ("The front end reads the chunked body and forwards "
                   "headers through its parser before dispatch. " * 12)
        self.assertFalse(translate.looks_english(vietnamese + padding))

    def test_too_little_prose_to_measure_falls_back_to_the_declaration(self):
        """A one-line page is not evidence of anything. Guessing "foreign" there
        would queue every stub in the archive for translation."""
        self.assertTrue(translate.looks_english("Read more", declared="en"))

    def test_a_non_latin_document_is_not_english(self):
        self.assertFalse(translate.looks_english("请求走私漏洞的利用方式与防御措施分析报告" * 8))

    def test_an_english_document_is(self):
        self.assertTrue(translate.looks_english(
            "The front end forwards the smuggled prefix to the back end here. " * 20))

    def test_a_latin_script_document_is_judged_on_its_words(self):
        italian = ("Il payload che viene usato per la richiesta ambigua non e sicuro "
                   "e questo articolo spiega come una applicazione con questo tipo di "
                   "configurazione puo essere attaccata con una richiesta contrabbandata. " * 6)
        self.assertFalse(translate.looks_english(italian))


class TestChunking(unittest.TestCase):
    def test_segments_are_numbered_and_every_block_appears_once(self):
        prepared = translate.prepare("漏洞分析。\n\n利用方式。\n\n防御措施。\n")
        identifiers = [identifier for chunk in prepared.chunks for identifier, _ in chunk]
        self.assertEqual(identifiers, [1, 2, 3])

    def test_a_long_document_is_split_into_several_chunks(self):
        # "richiesta ambigua" is the same 17 characters as the phrase it replaced,
        # so the chunk-size arithmetic this asserts on is unchanged.
        prepared = translate.prepare(("Una frase abbastanza lunga da contare "
                                      "che parla della richiesta ambigua. " * 30
                                      + "\n\n") * 12)
        self.assertGreater(len(prepared.chunks), 1)


class TestOnlyCodeIsProtected(unittest.TestCase):
    """Everything a human wrote to be READ is prose, even inside punctuation.
    Masking whole links and table rows left 2,064 Chinese characters
    untranslated in documents that reported themselves fully translated."""

    def _masked(self, text):
        masked, held = translate.protect(text)
        self.assertEqual(translate.restore(masked, held), text,
                         "protect/restore must be lossless")
        return masked

    def test_link_text_stays_in_the_prose_and_the_target_is_masked(self):
        masked = self._masked("Read [请求走私漏洞分析](https://x.test/b) first.")
        self.assertIn("请求走私漏洞分析", masked)
        self.assertNotIn("x.test", masked)

    def test_a_table_row_is_prose(self):
        self.assertIn("名称", self._masked("| 名称 | 说明 |"))

    def test_a_link_target_carrying_a_title_is_masked_whole(self):
        """82 targets in this archive are `(path "Title")`. A pattern that stops
        at the first space misses the construct and hands the PATH over."""
        masked = self._masked('![界面](./images/x.png "Select Options")')
        self.assertIn("界面", masked)
        self.assertNotIn("images", masked)

    def test_a_bracket_followed_by_a_parenthesis_is_not_a_link(self):
        text = "The list ended] (which is prose) here."
        self.assertEqual(self._masked(text), text)

    def test_image_alt_text_is_prose(self):
        """On a slide host the alt text IS the slide."""
        self.assertIn("架构图", self._masked("![架构图](https://x.test/i.png)"))

    def test_inline_code_is_still_code(self):
        self.assertNotIn("chunkSize", self._masked("Use `chunkSize` here."))

    def test_a_dotted_identifier_is_still_code(self):
        self.assertNotIn("Object.prototype",
                         self._masked("The Object.prototype.toString trick."))

    def test_an_identifier_rule_cannot_eat_the_sentence_after_it(self):
        """`\\w` is Unicode-aware in Python, so an ASCII code rule must say so."""
        self.assertIn("影响所有版本", self._masked("MS16-032 影响所有版本。"))

    def test_a_whole_cve_id_is_masked_not_half_of_one(self):
        masked = self._masked("CVE-2025-53770 是一个请求走私漏洞。")
        self.assertNotIn("53770", masked)
        self.assertIn("是一个请求走私漏洞", masked)

    def test_the_advisory_families_are_masked(self):
        for identifier in ("GHSA-aaaa-bbbb-cccc", "ZDI-CAN-12345", "MS16-032"):
            self.assertNotIn(identifier, self._masked(identifier + " applies."))

    def test_an_ordinary_word_starting_with_MS_is_not_an_advisory(self):
        self.assertIn("MSDN", self._masked("See MSDN for detail."))


class TestNestedPlaceholdersAreNotDemandedBack(unittest.TestCase):
    """Masking runs longest-construct first, so a Markdown link whose text is
    inline code masks the code and then the whole link around it. The inner
    token then appears nowhere in the prose, and demanding it from the
    translation reported nine intact documents as corrupted."""

    HELD = {"{{PH_1}}": "`XMLHttpRequest`",
            "{{PH_2}}": "[{{PH_1}}](https://x.test/a)"}
    PROSE = {1: "See {{PH_2}} for the request."}

    def test_a_token_that_only_lives_inside_another_is_not_demanded(self):
        self.assertEqual(sorted(translate.standing_alone(self.HELD, self.PROSE)),
                         ["{{PH_2}}"])

    def test_the_nested_token_still_comes_back_on_restore(self):
        self.assertEqual(
            translate.restore("See {{PH_2}} for the request.", self.HELD),
            "See [`XMLHttpRequest`](https://x.test/a) for the request.")

    def test_a_translation_that_keeps_the_outer_token_is_not_a_refusal(self):
        standing = translate.standing_alone(self.HELD, self.PROSE)
        self.assertEqual(
            translate.missing_placeholders("Voir {{PH_2}} pour la requete.", standing), [])

    def test_a_genuinely_dropped_token_is_still_caught(self):
        standing = translate.standing_alone(self.HELD, self.PROSE)
        self.assertEqual(translate.missing_placeholders("Voir la requete.", standing),
                         ["{{PH_2}}"])

    def test_no_segment_map_falls_back_to_demanding_everything(self):
        self.assertEqual(translate.standing_alone(self.HELD, {}), self.HELD)


class TestRebuild(unittest.TestCase):
    """The document is assembled from the FULL segment map, never from what the
    translator returned. Otherwise a dropped segment deletes a paragraph."""

    ORIGINAL = {1: "First.", 2: "Second.", 3: "Third."}

    def test_a_translated_segment_wins(self):
        body = translate.rebuild({2: "SECOND."}, self.ORIGINAL, {})
        self.assertEqual(body, "First.\n\nSECOND.\n\nThird.")

    def test_a_dropped_segment_falls_back_to_the_original(self):
        self.assertEqual(translate.rebuild({}, self.ORIGINAL, {}),
                         "First.\n\nSecond.\n\nThird.")

    def test_segments_keep_reading_order_whatever_order_they_came_back_in(self):
        body = translate.rebuild({3: "THIRD.", 1: "FIRST."}, self.ORIGINAL, {})
        self.assertEqual(body, "FIRST.\n\nSecond.\n\nTHIRD.")

    def test_a_comment_segment_is_not_part_of_the_prose(self):
        """It belongs inside its code block, which `apply_comments` handles."""
        original = dict(self.ORIGINAL)
        original[4] = "//explanation"
        body = translate.rebuild({4: "//explanation"}, original, {4: ["{{PH_1}}", "x"]})
        self.assertNotIn("explanation", body)


class TestOnlyForeignSegmentsAreHandedOver(unittest.TestCase):
    """A document is rarely uniformly one language, and re-translating a
    sentence that is already English is a chance to alter it for no reason."""

    MIXED = ("The generator writes the payload to disk before the run.\n\n"
             "漏洞分析: 该漏洞允许攻击者执行任意代码。\n\n"
             "This second English paragraph explains the same sink again.\n")

    def test_the_english_paragraphs_are_left_out(self):
        prepared = translate.prepare(self.MIXED, language="en")
        handed = [text for chunk in prepared.chunks for _identifier, text in chunk]
        self.assertEqual(len(handed), 1)
        self.assertIn("漏洞分析", handed[0])
        self.assertEqual(prepared.skipped, 2)

    def test_every_segment_is_kept_so_apply_can_rebuild(self):
        prepared = translate.prepare(self.MIXED, language="en")
        self.assertEqual(sorted(prepared.original), [1, 2, 3])

    def test_a_wholly_english_document_produces_no_work(self):
        prepared = translate.prepare(
            "The front end forwards the smuggled prefix to the back end here. " * 20,
            language="en")
        self.assertEqual(prepared.chunks, [])

    def test_a_mostly_english_block_holding_a_few_foreign_cells_is_handed_over(self):
        """A segment is a unit of WORK, so presence decides, not share. Judging
        by share left the Chinese cells inside a large mostly-English table
        untranslated, because the block averaged out as English."""
        table = ("| CVE-2019-99991 (暂无域环境) | Jun 11, 2019 | Web cache "
                 "deception allows an attacker to read another user's page. |\n"
                 "| CVE-2019-99992 | Jun 11, 2019 | The same keying issue "
                 "reached through a second path that was patched later. |")
        prepared = translate.prepare(table, language="en")
        handed = [text for chunk in prepared.chunks for _identifier, text in chunk]
        self.assertEqual(len(handed), 1)

    def test_a_link_list_with_one_foreign_title_is_handed_over(self):
        listing = ("- [ProxyShell 漏洞分析](https://a.test/one)\n"
                   "- [Reading the patch and diffing it](https://a.test/two)\n"
                   "- [Notes on the chunked parser](https://a.test/three)")
        prepared = translate.prepare(listing, language="en")
        self.assertEqual(len(prepared.chunks), 1)

    def test_an_english_block_with_no_foreign_letters_is_still_skipped(self):
        prepared = translate.prepare(
            "| CVE-2019-99991 | Jun 11, 2019 | Web cache deception issue. |",
            language="en")
        self.assertEqual(prepared.chunks, [])

    def test_greek_notation_is_mathematics_not_a_language(self):
        """`σ∈State` in a formal-methods paper sent it for translation."""
        maths = ("A state σ ∈ State is a tuple (E, h, s, φ, ψ) representing "
                 "the calling context in a symbolic configuration.")
        prepared = translate.prepare(maths, language="en")
        self.assertEqual(prepared.chunks, [])

    def test_a_stray_symbol_from_a_broken_extractor_is_not_a_language(self):
        """A PDF whose text layer decoded to symbols is damaged, not foreign,
        and `malformed` is what reports that."""
        prepared = translate.prepare("# \U00013029", language="en")
        self.assertEqual(prepared.chunks, [])

    def test_the_scripts_that_do_mean_another_language_are_caught(self):
        # A long English body, so it measures as English on its own and only the
        # foreign paragraph is handed over.
        english = ("The front end forwards the smuggled prefix to the back  "
                   "during read, and the back end never sees the split. " * 10)
        for sample in ("漏洞分析报告", "この記事では説明します", "취약점 분석", "Контрабанда запросов"):
            prepared = translate.prepare(english + "\n\n" + sample, language="en")
            handed = [text for chunk in prepared.chunks for _i, text in chunk]
            self.assertEqual(handed, [sample], sample)

    def test_a_short_heading_inherits_the_documents_verdict(self):
        """`## 分析` is unmeasurable on its own. In a Japanese article a two-word
        heading is Japanese; guessing per-segment sent every heading over."""
        japanese = ("この記事では、リクエストスマグリングの脆弱性について説明します。" * 6
                    + "\n\n## 概要\n")
        prepared = translate.prepare(japanese, language="ja")
        handed = [text.strip() for chunk in prepared.chunks for _identifier, text in chunk]
        self.assertIn("## 概要", handed)


if __name__ == "__main__":
    unittest.main()


class TestCommentsInCode(unittest.TestCase):
    """A COMMENT IS PROSE THAT HAPPENS TO LIVE IN CODE. Masking a fenced block
    whole protects the payload and also hides the author's explanation of it,
    which left `//ここでトークンを検証する` sitting in the English rendering of a
    Japanese write-up."""

    FENCE = ("```javascript\n//\u3053\u3053\u3067\u30c8\u30fc\u30af\u30f3\u3092"
             "\u691c\u8a3c\u3059\u308b\n"
             "const token = readToken();\n/* Blocco di commento lungo */\n```")

    def test_comments_become_their_own_segments(self):
        prepared = translate.prepare("Prosa italiana.\n\n" + self.FENCE + "\n")
        self.assertEqual(len(prepared.comments), 2)

    def test_a_translated_comment_goes_back_into_its_own_block(self):
        prepared = translate.prepare("Prosa.\n\n" + self.FENCE + "\n")
        identifiers = sorted(prepared.comments)
        held = translate.apply_comments(
            prepared.placeholders, prepared.comments,
            {identifiers[0]: "//Validate the token here",
             identifiers[1]: "/* A long comment block */"})
        fence = [value for value in held.values() if value.startswith("```")][0]
        self.assertIn("//Validate the token here", fence)
        self.assertIn("/* A long comment block */", fence)
        self.assertIn("const token = readToken();", fence)

    def test_the_code_itself_is_never_altered(self):
        prepared = translate.prepare("Prosa.\n\n" + self.FENCE + "\n")
        held = translate.apply_comments(
            prepared.placeholders, prepared.comments,
            {identifier: "// translated" for identifier in prepared.comments})
        fence = [value for value in held.values() if value.startswith("```")][0]
        self.assertIn("const token = readToken();", fence)
        self.assertTrue(fence.startswith("```javascript"))

    def test_a_cjk_comment_is_not_mistaken_for_a_url_fragment(self):
        """Japanese and Chinese comments have no spaces, and a "no spaces means
        it is a `//host/path` leftover" rule skipped every one of them."""
        found = translate.comments_in("//\u30ea\u30af\u30a8\u30b9\u30c8\u306e\u8aac\u660e\ncode();")
        self.assertEqual(len(found), 1)

    def test_a_real_url_fragment_is_still_skipped(self):
        self.assertEqual(translate.comments_in("//example.org/some/path\ncode();"), [])

    def test_a_preprocessor_directive_is_not_a_comment(self):
        for directive in ("#if DEBUG", "#region Handlers", "#pragma warning disable"):
            self.assertEqual(translate.comments_in(directive + "\ncode();"), [], directive)

    def test_a_marker_too_short_to_be_a_sentence_is_left_alone(self):
        self.assertEqual(translate.comments_in("// x\ncode();"), [])


class TestTheRecordsOwnProseIsTranslatedToo(unittest.TestCase):
    """A title is the first thing a researcher reads and the thing they scan a
    folder for. Left in the source language it tells them nothing, so it is
    translated with the body - unlike an author, which is an identifier."""

    BODY = "漏洞分析：该漏洞允许攻击者执行任意代码。" * 4

    def test_a_foreign_title_is_handed_over(self):
        prepared = translate.prepare(
            self.BODY, language="zh-cn",
            metadata={"title": "深入解析 HTTP 请求走私与缓存投毒"})
        self.assertEqual(list(prepared.metadata.values()), ["title"])

    def test_an_english_title_on_a_foreign_page_is_left_alone(self):
        prepared = translate.prepare(
            self.BODY, language="zh-cn",
            metadata={"title": "Exploiting a CL.0 Desync Through a Reverse Proxy"})
        self.assertEqual(prepared.metadata, {})

    def test_a_foreign_publisher_is_handed_over(self):
        prepared = translate.prepare(self.BODY, language="zh-cn",
                                     metadata={"publisher": "码坊"})
        self.assertEqual(list(prepared.metadata.values()), ["publisher"])

    def test_an_author_is_never_handed_over(self):
        """Translating a name or a handle produces a credit matching nothing."""
        self.assertNotIn("authors", translate.METADATA_FIELDS)

    def test_a_title_is_masked_into_the_same_numbering_as_the_body(self):
        """Two placeholder sets with independent numbering collide, and
        restoring one then corrupts the other."""
        prepared = translate.prepare(
            "使用 Object.prototype.toString 进行攻击。" * 4, language="zh-cn",
            metadata={"title": "详解 XMLHttpRequest.prototype.open 的利用"})
        tokens = list(prepared.placeholders)
        self.assertEqual(len(tokens), len(set(tokens)), "a token was reused")
        # The title's identifier is held once, alongside the body's, in one map.
        values = list(prepared.placeholders.values())
        self.assertEqual(values.count("XMLHttpRequest.prototype.open"), 1)
        self.assertIn("Object.prototype.toString", values)

    def test_metadata_is_not_joined_into_the_document_body(self):
        prepared = translate.prepare(self.BODY, language="zh-cn",
                                     metadata={"title": "标题在这里"})
        identifier = next(iter(prepared.metadata))
        body = translate.rebuild({identifier: "The title"}, prepared.original,
                                 set(prepared.metadata))
        self.assertNotIn("The title", body)


class TestAPlaceholderIsCheckedWhereItLands(unittest.TestCase):
    """A placeholder living only in the title is not missing from the body - it
    was never in it. Demanding it there refused three intact documents over
    `Transfer-Encoding` appearing in a heading."""

    HELD = {"{{PH_1}}": "Transfer-Encoding", "{{PH_2}}": "`Object.prototype`"}
    TITLE_ID, BODY_ID = 29, 1
    ORIGINAL = {BODY_ID: "The sink is reached through {{PH_2}} on read.",
                TITLE_ID: "玩轉 {{PH_1}} CHUNKED 請求走私攻擊"}

    def test_the_body_is_checked_against_the_bodys_own_segments(self):
        prose = {self.BODY_ID: self.ORIGINAL[self.BODY_ID]}
        standing = translate.standing_alone(self.HELD, prose)
        body = "The sink is reached through {{PH_2}} on read."
        self.assertEqual(translate.missing_placeholders(body, standing), [])

    def test_a_title_keeps_its_own_placeholder_requirement(self):
        title = {self.TITLE_ID: self.ORIGINAL[self.TITLE_ID]}
        standing = translate.standing_alone(self.HELD, title)
        self.assertEqual(sorted(standing), ["{{PH_1}}"])
        self.assertEqual(
            translate.missing_placeholders("Playing with {{PH_1}} CHUNKED", standing),
            [])

    def test_a_title_that_drops_its_placeholder_is_still_caught(self):
        title = {self.TITLE_ID: self.ORIGINAL[self.TITLE_ID]}
        standing = translate.standing_alone(self.HELD, title)
        self.assertEqual(
            translate.missing_placeholders("Playing with CHUNKED", standing),
            ["{{PH_1}}"])


class TestMinifiedCodeIsNotProse(unittest.TestCase):
    """An inline script that masking cannot see is still not translatable. One
    WeChat article carried a bundle that survived as a single 500,444-character
    segment, and preparing it produced a half-megabyte chunk for a translator."""

    BUNDLE = ("var __INLINE__=(function(e,t){'use strict';function r(n){return n&&"
              "typeof n==='object'&&'default'in n?n:{'default':n}}var o=r(t),"
              "i='上传成功';return{a:o,b:i}})(exports,window);" * 40)

    def test_the_real_shape_is_what_is_measured(self):
        """Characters-per-word would call this bundle MORE prose-like than a
        Chinese paragraph, because CJK has no Latin words. Syntax share does not."""
        self.assertGreaterEqual(
            sum(1 for c in self.BUNDLE if c in translate.CODE_PUNCTUATION_CHARS)
            / len(self.BUNDLE), translate.CODE_PUNCTUATION_SHARE)

    def test_a_minified_bundle_with_foreign_strings_is_not_sent_to_a_translator(self):
        self.assertGreater(len(self.BUNDLE), 2000)
        self.assertFalse(translate._segment_is_foreign(self.BUNDLE, True))

    def test_a_long_foreign_paragraph_is_still_translated(self):
        """The guard must not swallow ordinary prose that happens to be long."""
        paragraph = "本系列是笔者对 HTTP 请求走私的学习笔记。" * 200
        self.assertGreater(len(paragraph), 2000)
        self.assertTrue(translate._segment_is_foreign(paragraph, True))

    def test_a_long_english_sentence_run_is_not_machine_text(self):
        prose = ("The front end and the back end disagree about where the request ends, "
                 "which is what makes the desync possible. ") * 40
        self.assertGreater(len(prose), 2000)
        self.assertFalse(translate._is_unbroken_machine_text(prose))

    def test_ordinary_short_segments_are_unaffected(self):
        self.assertTrue(translate._segment_is_foreign("本系列是笔者", True))
