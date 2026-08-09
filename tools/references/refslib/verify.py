"""The offline gate. No network, and it never changes anything.

It answers one question: is what the archive published still bound to what it
actually acquired? Plus the boundary questions, because a boundary nobody checks
is a paragraph in a README.

Reference-page structure (the short list being a subset of the wide one,
duplicate URLs, placement review) is deliberately NOT checked here. Those are
curation questions and the curation skill has its own audit for them. Re-running
somebody else's invariants is how two tools start disagreeing about whose answer
is authoritative.
"""

import hashlib
import os
import re

# A Windows drive letter or a POSIX home path. The lookbehind is load-bearing:
# without it this matched the "s:/" inside every "https://..." and reported all
# 519 references as leaking a local path, which is the shape of false positive
# that gets a check switched off rather than fixed.
ABSOLUTE_PATH = re.compile(r"(?<![A-Za-z])(?:[A-Za-z]:[\\/]|/(?:home|Users|mnt|root)/)")

# Fields that hold repository paths. A URL field is never checked, because a URL
# legitimately contains things that look like paths.
PATH_FIELDS = ("cited_by", "file", "files", "material_paths")

# Pages ABOUT the archive, not archived references. They carry no third-party
# content, so requiring an attribution block on them is nonsense - and no
# manifest entry claims them, so without this they would be swept as orphans.
# `curation-notes.md` is the one that is hand-maintained rather than generated:
# it records decisions about the year lists, which is exactly the kind of thing
# a run must never overwrite or delete.
GENERATED_PAGES = ("readme.md", "index.md", "needs-work.md", "unresolved.md",
                   "excluded.md", "store-gaps.md", "log.md", "curation-notes.md")


class Finding(object):
    def __init__(self, level, what, detail=""):
        self.level = level          # "fail" or "warn"
        self.what = what
        self.detail = detail

    def __str__(self):
        return "%-5s %-46s %s" % (self.level.upper(), self.what, self.detail)


def run(root, config, manifest, store, curated_hashes=None):
    """Every offline check. Returns a list of findings; empty means clean."""
    findings = []
    stale = orphans(root, config, manifest)
    if stale:
        findings.append(Finding(
            "fail", "orphan published files",
            "%d file(s) no manifest entry points at, e.g. %s. Remove them with "
            "'acquire --prune-files'." % (len(stale), os.path.basename(stale[0]))))
    findings.extend(_check_curated_untouched(root, config, curated_hashes))
    findings.extend(_check_boundary(root))
    findings.extend(_check_manifest(manifest))
    findings.extend(_check_store(manifest, store))
    findings.extend(check_published_attribution(root, config))
    findings.extend(_check_translations(manifest, store))
    return findings


def _check_translations(manifest, store):
    """A document not in English must carry an English translation.

    THIS IS THE STEP THAT GETS FORGOTTEN. Acquiring, classifying and rendering a
    foreign-language write-up all succeed on their own, and the result looks
    finished: a file with frontmatter, attribution and content. Only a reader who
    cannot read the content finds out, long after the run. So the gate asks the
    question every time rather than trusting whoever ran the pipeline to notice.
    """
    from refslib import translate

    missing = []
    for key, entry in (manifest.data.get("urls") or {}).items():
        if (entry.get("decision") or {}).get("outcome") == "skip":
            continue
        sha = entry.get("content_sha256")
        if not sha or not store.has(sha):
            # Already reported as a missing store object by `_check_store`.
            continue
        if entry.get("translation_sha256"):
            continue
        if not translate.has_foreign_prose(
                store.get_text(sha), entry.get("language") or "",
                {field: entry.get(field) or ""
                 for field in translate.METADATA_FIELDS}):
            continue
        missing.append(entry.get("slug") or key)
    findings = []
    if missing:
        findings.append(Finding(
            "warn", "untranslated documents",
            "%d document(s) are not in English and have no translation, e.g. %s. "
            "Run 'refs.py translate --prepare'." % (len(missing), missing[0])))
    return findings


def published_files(root, config, suffix=".md"):
    """Every rendered reference file, excluding the generated index.

    Defaults to the Markdown tree because that is what the attribution gate
    reads; the orphan sweep also asks for `.pdf`, which carries no attribution
    block of its own and so must never reach that gate.
    """
    archive_dir = os.path.join(str(root), config.get("archive_dir") or "archived-references")
    found = []
    if not os.path.isdir(archive_dir):
        return found
    for current, _directories, files in os.walk(archive_dir):
        for name in sorted(files):
            if name.endswith(suffix) and name.lower() not in GENERATED_PAGES:
                found.append(os.path.join(current, name))
    return found


def orphans(root, config, manifest):
    """Published files no manifest entry points at.

    A better extraction produces a better title, which produces a different
    slug, which leaves the previous file behind. Nobody notices, because the
    folder still looks full. An orphan is a page nothing cites and nothing can
    re-render, so it is a defect rather than a leftover.
    """
    # Compared on TREE, FOLDER and name, not name alone: a file left in the
    # wrong folder after a re-grade is an orphan too, and so is one left at a
    # previous layout's location (the pre-rename `<year>/<slug>.md`, without the
    # `md/` tree) - matching on the basename would have called both current.
    # An entry claims a file only when its LAST acquire produced one. Three
    # references whose acquire had since FAILED still carried a file from an
    # earlier successful run: the index already refused to list them, so nothing
    # linked to them and nothing swept them. The same rule governs both, so a
    # file is listed exactly when it exists.
    # THE PDF TREE IS SWEPT TOO. Renaming 69 references left 69 stale PDFs
    # behind: the sweep only read `.md`, so the Markdown was corrected and the
    # PDF beside it kept the old name and the old content. A reader opening the
    # pdf/ folder saw both. A PDF has no owning entry exactly when its Markdown
    # would not have one, so the same expectation set answers for both trees -
    # a kind that never renders a PDF (video) simply never appears in it.
    from . import collections as collections_module
    from . import indexer
    claimed = [entry for entry in (manifest.data.get("urls") or {}).values()
               if indexer.has_document(entry)
               or (entry.get("slug") and entry.get("grade")
                   and ((entry.get("steps") or {}).get("acquire") or {}).get("result")
                   == "link-only")]
    expected = set()
    for entry in claimed:
        folder = collections_module.folder_of(entry, config)
        expected.add((collections_module.md_tree(config), folder, entry["slug"] + ".md"))
        expected.add((collections_module.pdf_tree(config), folder, entry["slug"] + ".pdf"))
        # The English half of the artifact is claimed by the SAME entry, and
        # only while a translation is actually held: drop the translation and
        # its two files become orphans on the next sweep, which is what should
        # happen to English nothing stands behind any more.
        if entry.get("translation_sha256"):
            translated = collections_module.translated_slug(entry["slug"])
            expected.add((collections_module.md_tree(config), folder, translated + ".md"))
            expected.add((collections_module.pdf_tree(config), folder, translated + ".pdf"))
    stale = []
    for suffix in (".md", ".pdf"):
        for path in published_files(root, config, suffix):
            folder = os.path.dirname(path)
            tree = os.path.basename(os.path.dirname(folder))
            if (tree, os.path.basename(folder), os.path.basename(path)) not in expected:
                stale.append(path)
    return sorted(stale)


def check_published_attribution(root, config):
    """Every published file must name its source.

    The archive publishes the full content, and the answer to copyright is that
    each file points clearly at the original. That makes attribution the
    mitigation rather than a nicety, so a file missing it FAILS the gate. A hand
    edit that removes the block is caught here even though `render` would have
    refused to write it.
    """
    from . import render

    findings = []
    archive_dir = os.path.join(str(root), config.get("archive_dir") or "archived-references")
    if not os.path.isdir(archive_dir):
        return findings
    for current, _directories, files in os.walk(archive_dir):
        for name in sorted(files):
            if not name.endswith(".md") or name.lower() in GENERATED_PAGES:
                continue
            path = os.path.join(current, name)
            with open(path, "r", encoding="utf-8") as handle:
                text = handle.read()
            missing = render.check_attribution(text)
            if missing:
                findings.append(Finding(
                    "fail", "published file is missing attribution",
                    "%s -> %s" % (name, ", ".join(missing))))
            leaked = local_paths_in(text, root)
            if leaked:
                findings.append(Finding("fail", "local path in a published file",
                                        "%s -> %s" % (name, leaked[0])))
            for level, what, detail in malformed(text):
                findings.append(Finding(level, what, "%s -> %s" % (name, detail)))
    return findings


# What a published file must not contain. Each of these was found in the corpus
# by a sweep, and each names a bug upstream rather than a taste preference.
COMPRESSED_MARKERS = "�"
ENTITY = re.compile(r"&(?:amp|lt|gt|quot|apos|nbsp|#\d{2,5});")
# A fence line: ``` opening a line with no SECOND ``` on it. The info string is
# nearly unconstrained - `c#` broke a character class and turned four balanced
# fences into "three", reporting eight correct files as unclosed - and the
# second-``` test is what excludes an inline ```span```.
#
# Two shapes cost a false warning each, so both are handled here rather than
# left to a reader to re-derive:
#   - CommonMark allows a fence up to THREE spaces in. One article's second
#     block was indented a single space, so nine of its ten fences were counted
#     and a balanced file was reported unclosed.
#   - A PDF whose embedded images decoded as text carries runs like
#     ```GGGÿÿÿÿÿ. That is image bytes, not an info string; requiring the info
#     string to be ordinary text keeps binary noise from counting as a fence.
FENCE = re.compile(r"^ {0,3}```(?!.*```)[\x20-\x7e]*$", re.M)

# Entities inside a fenced block may be the CODE. A markdown source file
# fetched whole is one big fence, and a PDF's text is not HTML at all;
# both were reported for carrying "unescaped entities" that are content.
FENCED_BLOCK = re.compile(r"^```.*?^```", re.M | re.S)


def malformed(text):
    """[(level, what, detail)] for a rendered file that will not read correctly.

    Deliberately narrow. A sweep with looser rules produced 138 "ends
    mid-sentence" findings that were all page footers, and called an inline
    ```code``` span an unbalanced fence. Only signals that were checked against
    the file they flagged are here.
    """
    at = text.find("\n## Content\n")
    document = text[at:] if at >= 0 else text
    found = []

    replacements = document.count(COMPRESSED_MARKERS)
    if replacements and replacements / max(len(document), 1) > 0.02:
        # 2,977 of 6,230 characters: a gzip body decoded as if it were text.
        found.append(("fail", "published file is mostly replacement characters",
                      "%d of %d characters" % (replacements, len(document))))

    entities = len(ENTITY.findall(FENCED_BLOCK.sub("", document)))
    if entities > 20:
        # `&lt;`/`&gt;` written into the archive verbatim, so a reader sees the
        # markup instead of the code being quoted.
        found.append(("warn", "published file carries unescaped HTML entities",
                      "%d" % entities))

    # A fence ALONE ON ITS LINE. An inline ```span``` is not a block, and
    # counting it made two correct files look unbalanced.
    if len(FENCE.findall(document)) % 2:
        found.append(("warn", "published file has an unclosed code fence",
                      "%d block fences" % len(FENCE.findall(document))))
    return found


def local_paths_in(text, root):
    """Paths that identify THIS machine, found in third-party content.

    Deliberately NOT the shape-based rule used on the manifest. An archived
    article about the SharePoint ToolShell chain is full of `C:\\Windows\\Temp\\x.dll`,
    and that is the research material, not a leak. What `CLAUDE.md` forbids is a
    path identifying the developer's own machine, so this compares against the
    real ones: the repository location, the user's home directory, and the
    content store. Testing the shape instead reported seven perfectly good
    payload examples as leaks.
    """
    # A path inside a fenced block belongs to the cited research. Real write-ups
    # routinely show shell transcripts from the same Linux distribution as the
    # archive host, including /home/ubuntu stack traces. Only prose/metadata can
    # leak a path introduced by this machine.
    lowered = FENCED_BLOCK.sub("", text).lower()
    candidates = [str(root), os.path.expanduser("~")]
    store = os.environ.get("WEBSEC_REFS_STORE")
    if store:
        candidates.append(store)
    found = []
    for candidate in candidates:
        if not candidate or len(candidate) < 6:
            continue
        for spelling in (candidate, candidate.replace("\\", "/"), candidate.replace("/", "\\")):
            if spelling.lower() in lowered:
                found.append(spelling)
                break
    return found


def curated_fingerprints(root, config):
    """Hashes of finalized and preliminary source documents before a run."""
    from . import harvest, sources

    prints = {}
    tracked = harvest.tracked_files(root) if config.get("preliminary_documents") else []
    for relative in sources.source_files(config, tracked):
        path = root / relative
        if path.exists():
            prints[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
    return prints


def _check_curated_untouched(root, config, before):
    """The boundary, as an assertion rather than a promise."""
    if not before:
        return []
    findings = []
    after = curated_fingerprints(root, config)
    for relative, digest in before.items():
        if after.get(relative) != digest:
            findings.append(Finding(
                "fail", "curated document modified", relative +
                " changed during a run. This tool must never write it: link"
                " curation belongs to the reading-list maintainers."))
    return findings


# The marker this looks for. A detector has to be able to name what it forbids,
# which is why THIS file is the one file the scan skips: otherwise the check
# reports itself, and the only ways out are exempting it or obfuscating the
# literal. `tests/test_verify.py` plants a violation and asserts this fires, so
# the exemption cannot hide a broken detector.
SKILL_MARKER = ".claude/skills"
SELF = os.path.basename(__file__)


def executable_strings(path):
    """Every string literal a module evaluates, docstrings excluded.

    Parsing rather than grepping, because prose MAY describe the boundary and
    code may not encode it. A line-based scan cannot tell those apart: it
    flagged this tool's own docstrings, which is the shape of false positive
    that gets a check deleted rather than fixed.
    """
    import ast

    with open(str(path), "r", encoding="utf-8") as handle:
        source = handle.read()
    tree = ast.parse(source, filename=str(path))
    docstrings = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            body = getattr(node, "body", None)
            if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) \
                    and isinstance(body[0].value.value, str):
                docstrings.add(id(body[0].value))
    return [(node.lineno, node.value) for node in ast.walk(tree)
            if isinstance(node, ast.Constant) and isinstance(node.value, str)
            and id(node) not in docstrings]


def boundary_offenders(paths_to_scan):
    """(file, line, why) for every real boundary violation in these files."""
    import ast

    offenders = []
    for path in paths_to_scan:
        name = os.path.basename(str(path))
        if name == SELF:
            continue
        for line, value in executable_strings(path):
            if SKILL_MARKER in value or SKILL_MARKER.replace("/", "\\") in value:
                offenders.append((name, line, "skill path in code"))
        with open(str(path), "r", encoding="utf-8") as handle:
            tree = ast.parse(handle.read(), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module and "claude" in node.module:
                offenders.append((name, node.lineno, "import from the skill"))
            if isinstance(node, ast.Call) and hasattr(ast, "unparse"):
                target = ast.unparse(node.func)
                if target in ("sys.path.insert", "sys.path.append") \
                        and "__file__" not in ast.unparse(node):
                    offenders.append((name, node.lineno, "sys.path towards something else"))
    return offenders


def tool_sources(root, tool_dir=None):
    """The tool's own modules: no tests, no cache, no bytecode."""
    tool_dir = tool_dir or os.path.join(str(root), "tools", "references")
    found = []
    for current, directories, files in os.walk(tool_dir):
        directories[:] = [name for name in directories
                          if name not in ("cache", "__pycache__", "tests")]
        for name in sorted(files):
            if name.endswith(".py"):
                found.append(os.path.join(current, name))
    return found


def _check_boundary(root, tool_dir=None):
    """No hard-coded path into the curation skill, no import from it, and no
    sys.path pointing anywhere but this tool's own directory."""
    return [Finding("fail", "boundary: " + why, "%s:%d" % (name, line))
            for name, line, why in boundary_offenders(tool_sources(root, tool_dir))]


def _check_manifest(manifest):
    findings = []
    for key, entry in (manifest.data.get("urls") or {}).items():
        if not entry.get("steps"):
            findings.append(Finding("warn", "no step recorded", key))
        if not entry.get("cited_by"):
            findings.append(Finding("warn", "no citation site recorded", key))
        for field in PATH_FIELDS:
            values = entry.get(field)
            values = values if isinstance(values, list) else ([values] if values else [])
            for value in values:
                if ABSOLUTE_PATH.search(str(value)):
                    findings.append(Finding("fail", "absolute path in the manifest",
                                            "%s -> %s" % (key, value)))
        health = entry.get("health") or {}
        # A wall is not rot. A row that never answered must not have been given a
        # capture, because there is no evidence anything is wrong with the page.
        if health.get("status") in ("blocked", "js-rendered") and entry.get("snapshot"):
            findings.append(Finding(
                "fail", "a blocked row selected a capture", key +
                " is unreadable over plain HTTP, which says nothing about the page."))
    return findings


def _check_store(manifest, store):
    """Every hash the manifest names must exist and still hash to its name."""
    findings = []
    referenced = set()
    for key, entry in (manifest.data.get("urls") or {}).items():
        for field, value in entry.items():
            if field.endswith("_sha256") and value:
                referenced.add(value)
                if not store.has(value):
                    findings.append(Finding("fail", "missing store object",
                                            "%s -> %s" % (key, value[:16])))
                elif not store.verify(value):
                    findings.append(Finding("fail", "store object does not match its hash",
                                            "%s -> %s" % (key, value[:16])))
    orphans = store.unreferenced(referenced)
    if orphans:
        findings.append(Finding("warn", "unreferenced store objects",
                                "%d object(s). Reported, never deleted." % len(orphans)))
    return findings
