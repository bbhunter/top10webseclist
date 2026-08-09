"""Which per-year collection a reference belongs to, and where its files live.

This repository is the "Top 10 Web Hacking Techniques" reading list, and it is
one list PER YEAR: `2006.md` through `2025.md`, plus the two-year `2016-17.md`.
The archive is organised the same way, split by format first so the binary PDFs
stay out of the Markdown tree: a rendered file lands in
`archived-references/md/<year>/` and its PDF in `archived-references/pdf/<year>/`,
decided by the year LIST that cites it - not by its research/records grade,
which the upstream tool used for its folders.

One function owns that decision, `collection_of`, and one pair owns the layout,
`md_relpath`/`pdf_relpath`, so acquisition, import, the PDF run, the index and
the orphan sweep all agree on where a file lives and a file never has to be
moved by hand.

Two rules follow from the shape of the data:

* The citing file is the evidence. `cited_by` is a list of `path:line` strings
  filled in by `check`, and the year is read off the file name (`2016-17.md` ->
  `2016-17`). No network, no manifest field to keep in sync.
* A reference cited by more than one year is filed under the FIRST year that
  cites it, so its folder is stable across runs. `cited_by` preserves harvest
  order, and harvest reads the year files in `git ls-files` order.
"""

import os
import re

# The default folder for anything a year list does not claim. Nothing should
# land here in normal use, because harvest skips the non-list files (README and
# the tooling) - but a stray citation is filed rather than dropped, so it is
# visible instead of lost.
FALLBACK = "misc"

# A finalized year list, the two-year 2016-17 list, or a provisional 2026-ai list.
DEFAULT_PATTERN = r"^(?P<name>\d{4}(?:-\d{2}|-ai)?)\.md$"


def _settings(config):
    section = (config or {}).get("collections") or {}
    return (section.get("pattern") or DEFAULT_PATTERN,
            section.get("fallback") or FALLBACK)


def name_for_file(relative, config=None):
    """The collection a tracked file belongs to, or "" if it is not a year list.

    `relative` is a repository-relative path (or a bare file name); only the base
    name is matched, so `2019.md` and `some/dir/2019.md` both resolve to `2019`.
    """
    pattern, _fallback = _settings(config)
    base = os.path.basename(str(relative or "").replace("\\", "/"))
    match = re.match(pattern, base)
    return match.group("name") if match else ""


def collection_of(entry, config=None):
    """The per-year folder for one manifest entry.

    Reads the entry's citation sites in order and returns the first that is a
    year list. Falls back to the configured `fallback` when none is.
    """
    _pattern, fallback = _settings(config)
    for site in (entry.get("cited_by") or []):
        path = str(site).rsplit(":", 1)[0]
        name = name_for_file(path, config)
        if name:
            return name
    return fallback


def folder_of(entry, config=None):
    """The per-year folder name a rendered file for this entry belongs in.

    Today that is exactly the collection. It is a named function so that callers
    read as "the folder this file lives in" rather than reaching for a field,
    the same way the upstream tool used the grade.
    """
    return collection_of(entry, config)


# The two format trees under the archive root. Split so the binary PDFs stay
# out of the Markdown tree: a diff, a sparse checkout or an exclusion rule can
# then treat prose and print separately.
MD_TREE = "md"
PDF_TREE = "pdf"


def md_tree(config=None):
    return ((config or {}).get("layout") or {}).get("md_tree") or MD_TREE


def pdf_tree(config=None):
    return ((config or {}).get("layout") or {}).get("pdf_tree") or PDF_TREE


def md_relpath(entry, config, slug):
    """Where this entry's rendered Markdown lives, relative to the archive root:
    `md/<year>/<slug>.md`."""
    return os.path.join(md_tree(config), folder_of(entry, config), slug + ".md")


def pdf_relpath(entry, config, slug):
    """Where this entry's PDF lives, relative to the archive root:
    `pdf/<year>/<slug>.pdf`."""
    return os.path.join(pdf_tree(config), folder_of(entry, config), slug + ".pdf")


# An English translation is a SECOND FILE beside the original rather than a
# section inside it, so a reader can open, link and print the English on its own
# while the source's own words stay a whole document. Both files belong to one
# artifact: same entry, same slug, same folder, distinguished by this suffix.
TRANSLATION_SUFFIX = "_translate"


def translated_slug(slug):
    return str(slug or "") + TRANSLATION_SUFFIX


def is_translation_slug(slug):
    return str(slug or "").endswith(TRANSLATION_SUFFIX)


def translated_md_relpath(entry, config, slug):
    """`md/<year>/<slug>_translate.md`."""
    return md_relpath(entry, config, translated_slug(slug))


def translated_pdf_relpath(entry, config, slug):
    """`pdf/<year>/<slug>_translate.pdf`."""
    return pdf_relpath(entry, config, translated_slug(slug))
