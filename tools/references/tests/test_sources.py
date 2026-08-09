"""Preliminary source discovery and archive boundaries."""

from . import support  # noqa: F401

import unittest

from refslib import collections, paths, sources


CONFIG = {
    "collections": {"pattern": r"^(?P<name>\d{4}(?:-\d{2}|-ai)?)\.md$"},
    "curated_documents": ["2025.md"],
    "preliminary_documents": {
        "pattern": r"^\d{4}-ai\.md$",
        "start_marker": "<!-- archived-references:start -->",
        "end_marker": "<!-- archived-references:end -->",
    },
}


class TestPreliminarySources(unittest.TestCase):
    def test_tracked_ai_files_are_discovered_without_enumerating_each_year(self):
        found = sources.source_files(
            CONFIG, ["README.md", "2025.md", "2026-ai.md", "notes.md"])
        self.assertEqual(found, ["2025.md", "2026-ai.md"])

    def test_only_lines_inside_the_markers_are_publishable(self):
        text = (
            "[intro](https://example.org/intro)\n"
            "<!-- archived-references:start -->\n"
            "- [kept](https://example.org/kept)\n"
            "<!-- archived-references:end -->\n"
            "- [watch](https://example.org/watch)\n"
        )
        self.assertEqual(sources.bounded_lines("2026-ai.md", text, CONFIG),
                         [(3, "- [kept](https://example.org/kept)")])

    def test_a_preliminary_file_without_boundaries_is_refused(self):
        with self.assertRaises(paths.SetupError):
            sources.bounded_lines(
                "2026-ai.md", "- [unsafe](https://example.org/all)\n", CONFIG)

    def test_preliminary_citations_file_into_their_own_collection(self):
        entry = {"cited_by": ["2026-ai.md:52"]}
        self.assertEqual(collections.collection_of(entry, CONFIG), "2026-ai")


if __name__ == "__main__":
    unittest.main()
