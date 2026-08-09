"""Offline collection promotion keeps Markdown honest and PDFs rebuildable."""

from . import support  # noqa: F401

import tempfile
import unittest
from pathlib import Path

import refs


class ManifestStub(object):
    def __init__(self, entry):
        self.data = {"urls": {"https://example.org/research": entry}}


class TestRefiling(unittest.TestCase):
    def test_markdown_moves_and_updates_citations_while_pdf_is_left_to_rebuild(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            old_md = root / "archive/md/2026-ai/research.md"
            old_pdf = root / "archive/pdf/2026-ai/research.pdf"
            old_md.parent.mkdir(parents=True)
            old_pdf.parent.mkdir(parents=True)
            old_md.write_text(
                "---\ncited_by:\n  - \"2026-ai.md:53\"\n---\n# Research\n",
                encoding="utf-8",
            )
            old_pdf.write_bytes(b"%PDF-old-citation")
            entry = {
                "slug": "research",
                "grade": "research",
                "cited_by": ["2026.md:14"],
                "steps": {
                    "acquire": {"result": "stored"},
                    "render": {"result": "ok", "file": "archive/md/2026-ai/research.md",
                               "translation_file": "", "chars": 60},
                    "pdf": {"result": "rendered", "file": "archive/pdf/2026-ai/research.pdf"},
                },
            }
            config = {
                "archive_dir": "archive",
                "collections": {"pattern": r"^(?P<name>\d{4}(?:-\d{2}|-ai)?)\.md$"},
            }

            moved = refs._relocate_published(root, config, ManifestStub(entry))

            new_md = root / "archive/md/2026/research.md"
            self.assertEqual(moved, 1)
            self.assertTrue(new_md.exists())
            self.assertFalse(old_md.exists())
            self.assertIn('  - "2026.md:14"', new_md.read_text(encoding="utf-8"))
            self.assertNotIn("2026-ai.md", new_md.read_text(encoding="utf-8"))
            self.assertTrue(old_pdf.exists())
            self.assertNotIn("file", entry["steps"]["pdf"])


if __name__ == "__main__":
    unittest.main()
