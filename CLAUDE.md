# Repository rules

- **Faulty captures are filed, not worked around.** If any work in this
  repository — app development, data rebuilds, list edits, anything — finds an
  archived reference that needs recapturing (a file the manifest advertises but
  the tree lacks, a capture of the wrong page such as a parked domain, consent
  wall or homepage, a junk render), it MUST end up listed in
  `archived-references/document-gaps.md`. That file is generated — never edit it
  by hand. Record the fault instead: set `content_gap` on the entry in
  `archived-references/manifest.json` to
  `faulty capture: <what is wrong>; <remedy> (reported <date>)`, then run
  `python tools/references/refs.py index` with the `WEBSEC_REFS_STORE`
  environment variable set (see the webseclist-archive-references skill for the
  store location and full workflow). If the store is unavailable in the
  session, leave the manifest record in place and state in the final report
  that `refs.py index` still has to be run.

  **Three gap reports, and putting a reference on the wrong one hides it.** Each
  answers a different question, so check which before you write anything:

  | Report | The document | What is missing |
  |---|---|---|
  | `document-gaps.md` | not archived | the document itself — generated |
  | `review-gaps.md` | archived | a judgement that it came out right — by hand |
  | `store-gaps.md` | archived | the source bytes it was made from — generated |

  So `document-gaps.md` lists ONLY references the archive could not get a
  document for. A reference whose Markdown and PDF are published is archived,
  even when the content store no longer holds the bytes behind them: `index`
  files that fault on `store-gaps.md`. And a document that is present but
  unverified is neither — it belongs on `review-gaps.md`, which is written by
  hand and is the one of the three a run must never overwrite or delete.

  Never put a reference on the wrong list — 1,011 fully archived references once
  buried the two that had no document at all.

- **A `--force` re-render can quietly make a document worse.** `refs.py acquire
  --force` is documented as an offline re-extract, and it is — until the raw
  object it wants is missing from the content store, at which point it goes back
  to the network and publishes whatever answers. A JS-driven report page answered
  with its app shell, and a 2,189-character document became a 9-character one.
  Around 286 references archive-wide have missing store bytes, so this is the
  common case, not a corner. Before re-rendering, check the entry's `raw_sha256`
  is actually present under `WEBSEC_REFS_STORE`; after re-rendering, compare each
  document's body length against `HEAD` and investigate everything that shrank.

  **`--force` also SKIPS hand-imports**, silently and on purpose — an import
  exists because no fetch worked. A curated `title` or `authors` in
  `overrides.json` therefore never reaches an imported document by that route.
  Reach for `--replace-imports` and you throw the hand-obtained copy away; use
  the route that fits what you are publishing instead:

  | To publish | Use | Because |
  |---|---|---|
  | a curated `authors`/`publisher` | `attribution --rewrite` | offline, in place, needs no store and no fetch — the only route that reaches hand imports AND references whose store bytes are gone |
  | a curated `title` | `import --redo --only <substring> <dir>` | the import path honours the title, rebuilds the slug and renames the file |

  `attribution --rewrite` is the one to remember: without it a byline sits
  recorded in the manifest while every published file still reads the old one,
  and the obvious fix — a re-render — is exactly the trap above.

  **Never trust a run's own success count.** One deck reported nothing wrong and
  still kept its file-stem title through a whole re-render pass, because it was
  an import and was skipped. Verify against the published files instead: every
  stated `title` and every stated author should appear in the frontmatter of the
  file its manifest entry names.

- **The queue selectors mean the whole backlog, not the row you just filed.**
  `--faulty-captures`, `--document-gaps` and `--missing-store` select every entry
  in that state. Filing one fault and running `wayback --faulty-captures` works
  all of them — one such run rewrote 30 references when two were intended. Scope
  with `--only` whenever the intent is one reference, and expect a diff far wider
  than what you filed whenever you don't.

  A recovered capture can also arrive gzip-encoded and be stored undecoded, which
  then extracts as binary noise and reads like a bad snapshot. Check the stored
  object for a `1f 8b` magic number before concluding a recovery failed.

- **A corrected title rebuilds the slug.** Stating `title` in `overrides.json`
  renames the file on the next re-render and orphans the old one, which
  `index --prune-files` clears. Two siblings given the SAME corrected title — a
  talk's slides and its whitepaper, a paper and its project page — collide, and
  the second becomes `<slug>-2`, a name that says nothing. The archive currently
  keeps them apart with the format word the citation itself uses, in parentheses:
  `... (Slides)`, `... (Whitepaper)`, `... (Paper)`.

- The year lists (`2006.md` … `2025.md`) are curated by hand; the archive
  tooling never writes them. `website/data/catalogue.json` and
  `website/data/collections/*.json` are generated by `website/build-data.mjs`
  — regenerate them, don't edit them.
