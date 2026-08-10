---
name: webseclist-remove-reference
description: Removes a reference from the "Top 10 Web Hacking Techniques" archive cleanly - the citation's manifest entry, its archived Markdown, its PDF and any translation pair - after the link is taken out of the list that cited it. Use whenever the user wants to remove, delete, drop, retract, un-archive or "take back out" a reference or its archived files - a link added to a year list by mistake, a candidate scrapped from a YEAR-ai.md file, a duplicate entry, or a document the maintainer decided should stay link-only. Also covers the keep-the-citation-but-drop-the-file case (a derivative video, a page judged not worth a local copy). Do NOT use for a BROKEN or WRONG capture that should be recaptured - that is webseclist-archive-references (recapture, not removal) - and never let the archive tooling edit a year list; removing the link itself is a hand edit made only on the user's explicit request.
---

# Remove a reference and its archived files

## What this is

The archive under `archived-references/` mirrors what the lists cite. When a
citation was a mistake - or a maintainer decides a local copy should not be
kept - the archive has to let go of it cleanly: the manifest entry, the
Markdown, the PDF, any `_translate` pair, and the generated reports that
mention it. Deleting the files by hand does half the job and leaves the
manifest advertising documents that are not there, which the next `verify`
reports as faults.

The tooling already knows how to do this. Removal is: take the link out of the
list, then let the tool notice nothing cites the entry any more and sweep what
it owned. Never delete an archive file directly.

There are two shapes, and the first question is which one this is:

- **A. The citation goes.** The link was a mistake, a duplicate, or is being
  withdrawn. The list edit removes it, and the archive follows.
- **B. The citation stays, only the local copy goes.** The list still points at
  the source, but the archive should hold no file for it (a derivative video,
  a page judged records-only, a maintainer exclusion).

## Before touching anything

1. **Find the entry.** Search `archived-references/manifest.json` for the URL
   by substring, not exact spelling - the manifest key is the NORMALIZED url
   (`www.` stripped, tracking noise removed), so the list's spelling and the
   key can differ.
2. **Read its `cited_by`.** If the same URL is cited by more than one line or
   more than one list, removing one citation does not orphan the entry -
   the files stay, correctly, and only the list edit happens. Say so instead
   of forcing anything.
3. **Look at the whole list line.** The list's idiom puts siblings on one line
   (a paper, its blog series, its demo videos). Removing the LINE removes
   every reference on it; removing one LINK keeps the rest. Confirm which one
   the user means when the line carries more than the target.
4. **Note the slug and check for a translation.** `md/<year>/<slug>.md` may
   have `md/<year>/<slug>_translate.md` and a `_translate.pdf` beside it.
   All of them belong to the entry and all will be swept together.
5. **Back up the manifest.** `archived-references/` is not git-tracked, so
   there is no checkout to restore from. Copy `manifest.json` to the session
   scratchpad first; it is the only cheap undo.

## A. Removing the citation and everything it owned

The list edit comes first and is a HAND edit, made because the user asked for
this removal - the archive tooling never writes a year list. Then, with
`WEBSEC_REFS_STORE` set (see the webseclist-archive-references skill) and one
command at a time:

```text
python tools/references/refs.py check --prune --limit 0
python tools/references/refs.py index --prune-files
python tools/references/refs.py verify
```

- `check --prune --limit 0` drops every manifest entry whose URL is no longer
  cited anywhere. `--limit 0` is what keeps it OFFLINE: without it, `check`
  re-probes every reference over the network. The prune itself runs on the
  full harvest before the probe loop starts, so nothing is fetched.
- **Read the prune output before going on.** It prunes ALL uncited entries,
  not just the target. An unexpected URL in that list means some other
  citation is broken - a mis-pasted link, a line lost in an earlier edit.
  Stop, restore the manifest backup, and report the finding; a stale entry
  someone did not ask to remove is a symptom to investigate, not a bonus
  cleanup. (This is how a real one was found: a list line carrying the same
  URL twice had silently uncited its second article.)
- `index --prune-files` deletes the orphaned files in BOTH trees - the
  Markdown, the PDF, any translation pair - and regenerates `README.md`,
  `document-gaps.md`, `excluded.md` and `store-gaps.md` without them.
- `verify` must end `0 failure(s)`. Expect the `unreferenced store objects`
  WARNING to grow by the removed entry's objects - that is correct (below).

## B. Keeping the citation, dropping only the file

When the list keeps the link but the archive should hold no document, the
record is a maintainer decision, not a deletion: add the URL under
`decisions` in `tools/references/overrides.json` with `outcome: skip`, the
fitting `class` (`derivative`, `records`, maintainer exclusion) and a reason a
future run can trust. Then:

```text
python tools/references/refs.py acquire --force --only <substring>
python tools/references/refs.py index --prune-files
python tools/references/refs.py verify
```

The entry stays in the manifest as excluded-with-reason, appears in
`excluded.md`, and is never fetched again. This is the same route the
archive-references skill uses for companion videos.

## What is deliberately NOT deleted

- **Store bytes.** The content-addressed store never deletes - that is an
  invariant of `refslib/store.py`, because an automatic sweep would be one
  manifest bug away from destroying the only copy of a page that no longer
  exists online. A removed entry's objects simply become "unreferenced store
  objects" in the `verify` report: reported, never deleted. Do not "finish
  the job" by deleting them by hand.
- **`history.jsonl`.** Append-only journal. The removal is recorded on top of
  the acquisition history, never by rewriting it.
- **Generated reports by hand.** `README.md`, `document-gaps.md`, `excluded.md`
  and `store-gaps.md` are rewritten by `index`; hand edits are overwritten and
  forbidden.

Because the store keeps the bytes and the journal keeps the provenance, a
mistaken removal is recoverable: restore the manifest backup (or re-add the
citation and re-run `check`/`acquire`), and nothing was actually lost.

## A candidate in a YEAR-ai.md file

`YEAR-ai.md` files (e.g. `2026-ai.md`) are AI-collected candidate lists. While
untracked by git they are never harvested, so nothing is archived for them
and removal is a plain edit to the file - no archive step at all. If such a
file has been committed, its URLs harvest like any citation (filed under
`misc`), and route A applies unchanged.

## Aftercare

- `git status --short` - the diff should be exactly the list edit (if route A)
  plus the regenerated archive reports and manifest. Nothing else.
- If a `decisions` entry in `tools/references/overrides.json` names ONLY the
  removed URL, drop it too; a decision about a URL nothing cites is inert
  clutter. Leave shared or rule-like entries alone.
- Run `node website/build-data.mjs` so the production website stops listing the
  removed reference; its catalogue and collection shards are generated, never edited.
