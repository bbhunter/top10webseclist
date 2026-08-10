"""Importing documents obtained by hand: grouping, matching, joining.

Every case here is one that actually went wrong on the maintainer's own import
directory, which is why each has a measurement attached rather than an opinion.
"""

from . import support  # noqa: F401

import os
import tempfile
import unittest
from unittest import mock

from refslib import manual_import


class TestPdfConversionFallback(unittest.TestCase):
    def test_a_pdf_the_in_process_parser_cannot_read_uses_docker_poppler(self):
        from refslib import extract_doc

        # A file inside a temporary DIRECTORY, not a NamedTemporaryFile: the
        # converter opens the path by name, and Windows refuses a second open
        # while the first handle is still held.
        with tempfile.TemporaryDirectory() as folder:
            source = os.path.join(folder, "deck.pdf")
            with open(source, "wb") as handle:
                handle.write(b"%PDF-1.4 test")
            with mock.patch.object(extract_doc, "pdf_to_markdown",
                                   side_effect=extract_doc.Unconvertible("glyph map")), \
                    mock.patch("refslib.toolbox.pdf_text",
                               return_value="Recovered presentation text") as fallback:
                self.assertEqual(manual_import._to_markdown(source),
                                 "Recovered presentation text")
        fallback.assert_called_once_with(b"%PDF-1.4 test")

    def test_one_complete_imported_pdf_is_adopted_as_the_original(self):
        with tempfile.TemporaryDirectory() as folder:
            source = os.path.join(folder, "paper.pdf")
            body = b"%PDF-1.7\nresearch\n%%EOF\n"
            with open(source, "wb") as handle:
                handle.write(body)
            candidate = manual_import.Candidate(source, "# Paper\n\nResearch " * 30,
                                                True, "")
            self.assertEqual(body, manual_import.original_pdf_bytes(
                [candidate], ["paper.pdf"]))

    def test_competing_imported_pdfs_are_not_guessed_between(self):
        candidates = [manual_import.Candidate("one.pdf", "one " * 100, True, ""),
                      manual_import.Candidate("two.pdf", "two " * 100, True, "")]
        self.assertEqual(b"", manual_import.original_pdf_bytes(
            candidates, ["one.pdf", "two.pdf"]))

# The real pair. One DEF CON talk leaves two PDFs whose URLs differ by a single
# trailing word, and the maintainer's converter produced five files across them.
DECK_URL = ("https://media.defcon.org/DEF%20CON%2031/DEF%20CON%2031%20presentations/"
            "Ada%20Example%20-%20Second%20Helpings%20Implicit%20and%20Mutation-Based"
            "%20Request%20Smuggling%20Vulnerabilities%20in%20Proxies.pdf")
PAPER_URL = DECK_URL.replace("Proxies.pdf", "Proxies-whitepaper.pdf")

DECK_FILES = ("Ada%20Example%20-%20Second%20Helpings%20Implicit%20and%20Mutation-Based"
              "%20Request%20Smuggling%20Vulnerabilities%20in%20Proxies[2].md")
PAPER_FILES = ("Ada%20Example%20-%20Second%20Helpings%20Implicit%20and%20Mutation-Based"
               "%20Request%20Smuggling%20Vulnerabilities%20in%20Proxies-whitepaper.pdf.md")


def group_of(*names):
    """A group holding these file names, without touching the disk."""
    group = manual_import.Group(manual_import.group_key(names[0]))
    return group


class TestGroupingKeepsTwoDocumentsApart(unittest.TestCase):
    """Measured: five files from two different DEF CON 31 PDFs collapsed into
    one group, because `whitepaper` was treated as a word carrying no signal. The
    paper and the deck were joined into a single archive file and the deck stayed
    on the document-gaps list, still listed as never acquired."""

    def test_the_paper_and_the_deck_of_one_talk_are_different_groups(self):
        self.assertNotEqual(manual_import.group_key(PAPER_FILES),
                            manual_import.group_key(DECK_FILES))

    def test_every_converter_spelling_of_one_document_is_one_group(self):
        keys = {manual_import.group_key(name) for name in (
            PAPER_FILES,
            PAPER_FILES.replace(".pdf.md", "[2].md"),
            PAPER_FILES.replace(".pdf.md", ".pdf_PDF to Markdown.html"))}
        self.assertEqual(len(keys), 1)

    def test_the_kind_is_read_from_the_file_name_not_the_whole_path(self):
        """Every DEF CON URL lives under /presentations/, so a path-wide read
        calls the whitepaper a deck."""
        self.assertEqual(manual_import.kind_of(PAPER_URL), "paper")
        self.assertEqual(manual_import.kind_of(DECK_URL), "")


class TestSimilarNamesAreMerged(unittest.TestCase):
    """A converter renames what it produces, so two attempts at one document
    arrive under names that share most but not all of their words."""

    def merge(self, *names):
        groups = {}
        for name in names:
            key = manual_import.group_key(name)
            groups.setdefault(key, manual_import.Group(key)).candidates.append(name)
        return manual_import.merge_similar(groups)

    def test_a_renamed_conversion_joins_the_document_it_belongs_to(self):
        merged = self.merge("2023_Hexacon_whitepaper-desync.pdf_PDF to Markdown.html",
                            "_MConverter.eu_whitepaper-desync (5).md")
        self.assertEqual(len(merged), 1)
        self.assertEqual(sum(len(group.candidates) for group in merged.values()), 2)

    def test_a_paper_and_a_deck_are_never_merged_however_alike_the_names(self):
        merged = self.merge(PAPER_FILES, DECK_FILES)
        self.assertEqual(len(merged), 2)

    def test_a_one_word_name_is_not_evidence_enough_to_absorb(self):
        merged = self.merge("ndss21.pdf_PDF to Markdown.html",
                            "attacking-http-parsers_PDF to Markdown.html")
        self.assertEqual(len(merged), 2)


class TestMatching(unittest.TestCase):
    def references(self):
        return [("paper", {"spellings": [PAPER_URL], "kind": "whitepaper"}),
                ("deck", {"spellings": [DECK_URL], "kind": "whitepaper"})]

    def matched(self, name):
        key = manual_import.group_key(name)
        groups = manual_import.match({key: manual_import.Group(key)}, self.references())
        group = list(groups.values())[0]
        return group.reference[0] if group.reference else None

    def test_the_paper_file_goes_to_the_paper_citation(self):
        self.assertEqual(self.matched(PAPER_FILES), "paper")

    def test_the_deck_file_goes_to_the_deck_citation(self):
        self.assertEqual(self.matched(DECK_FILES), "deck")

    def test_a_near_miss_spelling_still_counts_as_the_same_word(self):
        """A saved file name is a rewrite of a title, not a copy of it."""
        self.assertTrue(manual_import._near("vulnerability", "vulnerabilities"))
        self.assertTrue(manual_import._near("normalization", "normalisation"))

    def test_two_different_words_that_merely_start_alike_do_not(self):
        self.assertFalse(manual_import._near("sitecore", "sitefinity"))
        self.assertFalse(manual_import._near("prototype", "protection"))

    def test_a_name_that_shares_nothing_is_reported_rather_than_guessed(self):
        self.assertIsNone(self.matched("some-unrelated-page-about-cats.md"))

    def test_the_urls_own_file_name_beats_a_page_that_merely_talks_about_it(self):
        """Measured: a talk cited three times - the PDF, the forum thread, the
        video - scored 0.90 against all three on word overlap alone, and the coin
        flip put the deck's files on the forum thread."""
        references = [("forum", {"spellings": ["https://forum.defcon.org/node/245716"],
                                 "cited_title": "Second Helpings Implicit and Mutation-Based "
                                                "Request Smuggling Vulnerabilities in Proxies"}),
                      ("pdf", {"spellings": [DECK_URL]})]
        key = manual_import.group_key(DECK_FILES)
        groups = manual_import.match({key: manual_import.Group(key)}, references)
        self.assertEqual(list(groups.values())[0].reference[0], "pdf")

    def test_a_file_lands_on_its_own_citation_even_when_that_one_is_finished(self):
        """Measured: matching only against references that still need content
        re-homed a file whose own citation was already archived onto the
        next-best needy one. A Chinese article about request smuggling was filed
        under a different Chinese article about request smuggling, overwriting
        50,091 bytes of the right document with 27,687 bytes of the wrong one.
        Deciding whether the winner may be written belongs to the caller, not to
        the match."""
        references = [
            ("right", {"spellings": ["https://rivers.example.cn/blog/http-chunked"],
                       "title": "HTTP Request Smuggling Chunked Changting"}),
            ("other", {"spellings": ["https://notes.example.io/posts/http-request-smuggling/"],
                       "title": "HTTP request smuggling chunked"}),
        ]
        key = manual_import.group_key("_HTTP Request Smuggling -- Chunked _ "
                                      "Changting Baichuan Cloud.html")
        groups = manual_import.match({key: manual_import.Group(key)}, references)
        self.assertEqual(list(groups.values())[0].reference[0], "right")


class TestContentVetoesTheName(unittest.TestCase):
    """A file name can lie. Two conversions saved under one blog post's title
    were the blog post and the Black Hat whitepaper it describes: 39,962 and
    126,742 characters with 2% of their text in common. Joining them would file
    one document under the other's citation."""

    def group(self, *texts):
        group = manual_import.Group("soapwn pwning applications through client proxies wsdl")
        for index, text in enumerate(texts):
            group.candidates.append(
                manual_import.Candidate("file%d.md" % index, text, True, ""))
        return manual_import.split_unlike({group.key: group})

    def test_two_unlike_documents_are_split_apart(self):
        blog = "The watchTowr blog post about the bug. " * 60
        paper = "Table of contents disclaimer introduction theory of client proxies. " * 60
        self.assertEqual(len(self.group(blog, paper)), 2)

    def test_two_conversions_of_one_document_stay_together(self):
        full = "The front end forwards the smuggled prefix downstream once. " * 60
        truncated = full[:1500]
        split = self.group(full, truncated)
        self.assertEqual(len(split), 1)
        self.assertEqual(len(list(split.values())[0].candidates), 2)

    def test_a_split_document_is_matched_on_its_own_first_page_only(self):
        """Its file name describes its sibling, so believing the name would file
        it under the sibling's citation."""
        paper = ("SOAPwn Pwning Framework Applications Through Client Proxies WSDL "
                 "whitepaper Black Hat EU 2025. Disclaimer. Introduction. " * 8)
        group = manual_import.Group("something else entirely", name_is_borrowed=True)
        group.candidates.append(manual_import.Candidate("wrong-name.md", paper, True, ""))
        references = [
            ("paper", {"spellings": ["https://i.blackhat.com/BH-EU-25/eu-25-x-SOAPwn-wp.pdf"],
                       "cited_title": "SOAPwn: Pwning Framework Applications Through "
                                      "Client Proxies and WSDL (Black Hat EU 2025 whitepaper)"}),
            ("unrelated", {"spellings": ["https://example.org/other"],
                           "cited_title": "An entirely different article about caching"}),
        ]
        groups = manual_import.match({"g": group}, references)
        self.assertEqual(groups["g"].reference[0], "paper")

    def test_a_split_document_that_names_nothing_stays_unmatched(self):
        group = manual_import.Group("borrowed", name_is_borrowed=True)
        group.candidates.append(
            manual_import.Candidate("x.md", "Some prose with no title on it. " * 40, True, ""))
        references = [("other", {"spellings": ["https://example.org/other"],
                                 "cited_title": "An entirely different article about caching"})]
        groups = manual_import.match({"g": group}, references)
        self.assertIsNone(groups["g"].reference)


class TestPagesNotCopied(unittest.TestCase):
    """"Save page as, complete" writes Thing.html next to Thing_files/. Copying
    only the folder leaves nothing importable, and that looks exactly like not
    having supplied the page at all."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def make(self, *names):
        for name in names:
            path = os.path.join(self.tmp.name, name)
            if name.endswith("_files"):
                os.mkdir(path)
            else:
                open(path, "w").close()
        return manual_import.pages_not_copied(self.tmp.name)

    def test_a_resources_folder_with_no_page_is_named(self):
        self.assertEqual(self.make("Article_files"), ["Article_files"])

    def test_a_folder_beside_its_page_is_not_reported(self):
        self.assertEqual(self.make("Article_files", "Article.html"), [])


class TestJoin(unittest.TestCase):
    """Converters truncate and mangle, so the maintainer often has two or three
    attempts at one document. Nothing another attempt found may be dropped."""

    def candidate(self, name, markdown):
        return manual_import.Candidate(name, markdown, True, "")

    def test_text_only_one_attempt_caught_is_kept_and_labelled(self):
        """One converter truncates before the appendix, another mangles the body
        but reaches it. Picking either alone loses something real."""
        shared = "# Paper\n\n" + ("The front end forwards the smuggled prefix onward. " * 20)
        appendix = ("The appendix lists every affected assembly version, its build date, "
                    "and the exact patch that removed the type from the allow list.")
        text, used = manual_import.join([
            self.candidate("truncated.md", shared + "\n\n" + ("More body text. " * 20)),
            self.candidate("mangled.md", shared[:400] + "\n\n" + appendix)])
        self.assertIn(appendix, text)
        self.assertIn("second conversion", text)
        self.assertEqual(len(used), 2)

    def test_a_duplicate_conversion_adds_nothing(self):
        base = "# Paper\n\n" + ("The front end forwards the smuggled prefix onward. " * 20)
        text, used = manual_import.join([self.candidate("a.md", base),
                                         self.candidate("b.md", base)])
        self.assertEqual(len(used), 1)
        self.assertNotIn("second conversion", text)

    def test_ordered_transcription_parts_are_concatenated_without_loss(self):
        second = "## Page 30\n\nShort heading\n\n- final bullet"
        first = "## Page 1\n\nOpening page"
        text, used = manual_import.join([
            self.candidate("deck.part02.md", second),
            self.candidate("deck.part01.md", first)])
        self.assertEqual(first + "\n\n" + second, text)
        self.assertEqual(["deck.part01.md", "deck.part02.md"], used)

    def test_part_suffixes_group_as_one_document(self):
        self.assertEqual(manual_import.group_key("deck.part01.md"),
                         manual_import.group_key("deck.part02.md"))

    def test_ordered_parts_are_not_split_for_having_disjoint_page_text(self):
        group = manual_import.Group("deck")
        group.candidates = [
            self.candidate("deck.part01.md", "opening words " * 80),
            self.candidate("deck.part02.md", "different closing words " * 80),
        ]
        split = manual_import.split_unlike({"deck": group})
        self.assertEqual(["deck"], list(split))
        self.assertEqual(2, len(split["deck"].candidates))


if __name__ == "__main__":
    unittest.main()


class TestIndexPages(unittest.TestCase):
    """A blog's index page shares its site title with every article on that
    site, so it matches those citations by NAME almost perfectly. Twice it was
    filed as an article. Measured: 1,768 characters, 10 links, 206 words of
    prose - while a documentation page with 373 links carries 75,569 characters
    of prose with them."""

    def test_a_link_list_is_reported_as_an_index(self):
        markdown = "# Blog\n\n" + "".join(
            "- [Some post title here](https://example.org/post%d)\n" % n for n in range(10))
        self.assertIn("list of links", manual_import.looks_like_an_index(markdown))

    def test_a_long_document_full_of_links_is_not_an_index(self):
        body = ("The front end forwards the smuggled prefix to the back end here. " * 200)
        markdown = body + "".join(
            "\n- [reference](https://example.org/r%d)" % n for n in range(60))
        self.assertEqual(manual_import.looks_like_an_index(markdown), "")

    def test_an_index_page_is_refused_by_the_import_quality_gate(self):
        markdown = "# Blog\n\n" + "".join(
            "- [Some post title here](https://example.org/post%d)\n" % n for n in range(10))
        ok, reason = manual_import._quality(markdown)
        self.assertFalse(ok)
        self.assertIn("list of links", reason)
