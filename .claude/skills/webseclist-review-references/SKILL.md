---
name: webseclist-review-references
description: Audits references the Top 10 Web Hacking Techniques archive ALREADY holds, for one collection (a year like 2019, a preliminary YYYY-ai, or 2016-17), and repairs what it finds - wrong-page captures, binary or mojibake gibberish, titles that are a file stem or site chrome, missing bylines, broken PDFs, orphaned files and stale metadata. Use whenever someone asks to review, audit, validate, verify, QA, sanity-check, proofread or "check that they are all valid" for archived references; when they report gibberish, junk, garbled text, bad formatting, wrong titles, a document that is not the cited article, or missing data in archived-references/md/; when a year needs checking before a release or a website rebuild; or when they ask to add authors that the archive is missing. Do NOT use it to archive NEW citations or recapture a reference that was never fetched (that is webseclist-archive-references), to remove a reference (webseclist-remove-reference), to credit one researcher from a name the user supplies (webseclist-credit-author), to judge research value (webseclist-judge-reference), or to snapshot announcement pages (webseclist-archive-listings). It reads the year lists and never writes them.
---

# Review an archived collection and repair what is wrong

## What this is

The archive holds a Markdown and PDF copy of every cited resource. Acquisition is
mechanical, so it succeeds loudly: a run reports "stored" whether it captured the
research or a consent wall, a product page or a decoded font stream. This workflow
is the pass that reads what was actually published and fixes it.

You are auditing documents that already exist. If a reference has no document at
all, that is an acquisition job — hand it to `webseclist-archive-references`.

## Ask for what you need; never hardcode it

**The collection.** Take it from the invocation arguments. If none was given, ask
which collection to review, and offer what is on disk (`archived-references/md/*/`).
Reviewing "everything" is rarely what someone means and is rarely affordable —
confirm before sweeping more than two collections.

**The content store.** Every `refs.py` command needs `WEBSEC_REFS_STORE` pointing
at the durable store. If it is already set in the environment, use it. If not, ask
the user for the path — do not guess and do not write one into any tracked file.
Without it the tool silently falls back to a git-ignored workspace cache, and a
`git clean -xfd` then destroys the only copy of bytes for pages that are already
gone from the web.

**Scratch space.** Put scanners, extracts and import staging in a temporary
directory outside the repository, so a half-finished audit never lands in a diff.

## Check nobody else is running first

Every `refs.py` command loads the whole manifest at start and writes it whole at
exit, so two concurrent runs mean last-writer-wins and one of them silently loses
its work. Before you start, check whether `archived-references/manifest.json` was
modified in the last few minutes; if it was, ask the user whether another session
is running rather than assuming. Run one `refs.py` command at a time throughout,
and never a corpus-wide `acquire --force`.

## Sweep mechanically, then judge

Write a scanner into scratch space rather than opening files one by one — a
collection is 80-100 documents and the interesting faults are rare. Worth checking:

| Class | What to look for |
|---|---|
| Frontmatter | missing `type`/`title`/`resource`/`slug`/`kind`, empty title, slug that disagrees with the filename |
| Gibberish | mojibake (`Ã©`, `â€™`), runs of U+FFFD, control characters |
| Binary garbage | decoded font/image streams published as prose |
| Titles | a PDF's file stem (`BHUS26 Heyes CSS WP`), site chrome (`… › Vendor`, `Owner/Repo: file.md`), a blog masthead |
| Body | empty or implausibly thin, truncated mid-sentence, page furniture as content |
| Attribution | no author where the document names one |
| Files | manifest entries whose md/pdf is absent, and published files no entry claims |
| PDFs | `%PDF-` header, `%%EOF` trailer, plausible size |
| Metadata | `cited_by` line numbers that land on a line with no link; translation pairs not cross-linked by `translation_file`/`translation_of` |
| Coverage | a link in the list with no manifest entry (unwrap `web.archive.org/…/<url>` first — the archive files a capture under the CAPTURED url) |

**Detecting binary garbage is the one worth getting right.** Decoded font bytes
are mostly accented Latin-1, so a test based on character class calls them
"alphanumeric" and sees nothing. What separates them from prose is shape: almost
no runs of three or more ASCII letters, combined with a high share of bytes above
0x7F. Require both, and exclude CJK first — CJK prose also lacks Latin word runs
and is perfectly legitimate.

## Expect false positives, and verify before acting

Most of what a scanner flags in this corpus is real content. Confirm each class
against the actual text before changing anything:

- Very long unbroken tokens are encoded payloads, ffmpeg protocol strings and CDN
  URLs — the substance of the research, not corruption.
- Repeated paragraphs are usually a slide deck's build-up slides, or a writeup
  restating its exploit as it evolves.
- Non-Latin text usually means a genuinely foreign document; check for a
  translation pair before treating it as a fault.
- A body that does not end in punctuation is usually just an acknowledgements
  slide, a licence section or a byline.
- Titles like `Code`, `Tool`, `Slides` or `PoC` come from the citing list's own
  idiom, where a technique's siblings are `[Slides](…) [Code](…)` on one line.
  Those are intended. A PDF's *file stem* is not.

Report the false-positive classes you cleared. A reviewer needs to know what was
looked at, not only what was changed.

## Wrong-page captures are the most valuable find

A capture of the wrong page reads as a healthy document: full frontmatter, real
prose, a plausible title. The strongest signal is a cross-host redirect — compare
each entry's `original_url` against its `retrieved_from`. Acquisitions have
published a vendor's product page in place of research whose company was acquired,
and a blog's post index in place of an article whose URL moved.

When you find one, file it before anything else, exactly as CLAUDE.md requires:
set `content_gap` on the manifest entry to
`faulty capture: <what is wrong>; <remedy> (reported <date>)`, then run
`refs.py index`. That file is generated; never hand-edit it.

Then try to recover it with `wayback --only <substring>`. Scope it with `--only`:
`--faulty-captures`, `--document-gaps` and `--missing-store` select every entry in
that state across the whole archive, so filing one fault and running the flag form
works the entire pre-existing backlog. If a recovered capture then extracts as
binary noise, check the stored object for a `1f 8b` gzip magic number before
concluding the snapshot was bad — a capture can be stored still-compressed.

## Publishing a correction

Published `.md` files are generated. Correct the source of truth instead: state
the fix in `tools/references/overrides.json` under `decisions[<url>]`, keyed by the
manifest's normalized URL. Match the existing entries' shape, preserve the file's
formatting and key order so the diff shows only your change, and always include
`outcome` and `class` — a decision with no `outcome` is read as "keep no document"
and will strip the entry's grade.

Then pick the route that fits what you are publishing:

| To publish | Route | Why this one |
|---|---|---|
| `authors` / `publisher` | `refs.py attribution --rewrite` | offline and in place; needs no store and no fetch, so it is the only route that reaches hand imports and references whose stored bytes are gone |
| `title` | re-render the reference; for a hand-imported one, `refs.py import --redo --only <substring> <dir>` | the import path honours a curated title, rebuilds the slug and renames the file |

Never reach for `--replace-imports` to force a title through. An import exists
because no fetch worked, and that flag throws the hand-obtained copy away.

**On naming a researcher:** take a name only when you can quote the words you read
it from, and put that quote in `reason`. A missing byline says the archive does not
know; a wrong one credits a stranger with someone's work and reads as fact. A
handle the author publishes under is a real credit — a hostname is not. Most
unattributed documents genuinely name nobody, and leaving those alone is the
correct outcome, not a gap.

## Two traps that will cost you a document

**`acquire --force` is offline only until the bytes are missing.** It is documented
as a re-extract from the content store, and it is — but when the raw object it
wants is absent it goes back to the network and publishes whatever answers. A
JavaScript-driven page answers with its app shell. Store objects go missing often
in this archive (antivirus has deleted them in bulk), so check the entry's
`raw_sha256` is actually present in the store before re-rendering, and afterwards
compare every document's body length against `HEAD` and investigate anything that
shrank. A silent 2,000-character loss looks exactly like success.

**A run's success count is not evidence.** `acquire --force` skips hand-imports
silently and by design, so a pass can report every reference processed while a
curated title reached none of them. Verify against the published files: every
stated `title` and every stated author should appear in the frontmatter of the file
its manifest entry names. Check this before you believe the work is done.

If you drive `refs.py` from a shell loop, make sure the selector values carry no
trailing carriage return — a `--only` argument with a stray `\r` matches nothing,
the command exits 0, and the loop reports success having done nothing.

## Renames, collisions and cleanup

A corrected title rebuilds the slug, so the file is renamed on the next re-render
and the old one is orphaned; `index --prune-files` clears them. Two siblings given
the SAME corrected title — a talk's slides and its whitepaper, a paper and its
project page — collide, and the second becomes `<slug>-2`, a name that identifies
nothing. Keep them apart with the format word the citation itself uses, in
parentheses: `… (Slides)`, `… (Whitepaper)`, `… (Paper)`.

## Finishing

```text
refs.py pdf --collection <collection>     # fills in PDFs for renamed files
refs.py index --prune-files               # regenerates the reports, clears orphans
refs.py verify
git status --short
```

`verify` will report a standing set of `missing store object` failures that belong
to `store-gaps.md` and are not this review's work. Record the count before you start
so you can say whether it moved, confirm none of them names a reference you touched,
and confirm no new failure class appeared. Reporting "verify is clean" when it never
was is worse than reporting the real number.

`git status` must show no change to any year list (`YYYY.md`, `YYYY-ai.md`). The
archive tooling never writes them; if one is modified, find out why before going
further — another session may be editing the repository.

## Report

Say what was actually wrong and what you did about it, then:

- the false-positive classes you cleared, so nobody re-investigates them;
- anything you deliberately left, and why;
- judgement calls the maintainer should review — a new convention, an invented
  disambiguation, a credit resting on a handle rather than a stated name;
- any mistake you made and corrected mid-run, plainly. A repair you had to make is
  the most useful thing in the report, because it is what the next run must avoid.
