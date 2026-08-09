# tools/references - the reference archive tool

Dev-only tooling for this repository (the "Top 10 Web Hacking Techniques"
reading list). It builds a local **Markdown-plus-PDF archive** of every resource
the year lists cite, so a technique survives the article that described it going
offline. See `.claude/skills/webseclist-archive-references/SKILL.md` for the
operational guide; this file is the tool reference.

## The one rule (read this first)

The year lists - `2006.md` through `2025.md`, plus `2016-17.md` - are the input.
This tool **reads** them and **writes** the archive under `archived-references/`. It
never edits a year list. The flow is one way:

```text
year lists -> archive inventory -> acquisition -> Markdown -> PDF
```

What that means in practice:

- There is no command that writes a `20xx.md` file. Everything the archive learns
  about a citation is REPORTED; whether a list changes is a separate hand edit.
- A reference is filed under the year list that cites it, in
  `archived-references/md/<year>/`. That single decision lives in `refslib/collections.py`.
- `refs.py verify` fingerprints every year list before a run and FAILS if one
  changed during it, so the rule is asserted rather than merely promised.

## Requirements

Python 3 and the official Git CLI handle the ordinary routes. Docker is required
for rendered pages, Markdown-origin PDFs, video captions, insecure-TLS recovery,
and Poppler conversion. Those jobs run in the pinned toolbox image rather than
on the host. `dependency-policy.json` is the gate anything else has to pass first
(official upstream, clear licence, at least one month old, exact version and
artifact hashes). Nothing fetched by this tool may add to that file.

## Commands

```text
python tools/references/refs.py harvest        # every cited URL in the year lists
python tools/references/refs.py check          # probe each URL, record health   [NETWORK]
python tools/references/refs.py check-browser  # only the walled rows            [NETWORK]
python tools/references/refs.py acquire        # preserve, convert, render        [NETWORK]
python tools/references/refs.py pdf            # a PDF beside each Markdown file   [DOCKER]
python tools/references/refs.py wayback        # a better capture for a dead URL  [NETWORK]
python tools/references/refs.py transcripts    # a talk's captions, in a container [NETWORK]
python tools/references/refs.py translate      # prepare/apply a translation
python tools/references/refs.py index          # regenerate the folder index
python tools/references/refs.py verify         # the offline gate
python tools/references/refs.py import <dir>   # file documents obtained by hand
python tools/references/refs.py report         # advice about each citation
python tools/references/refs.py dependencies   # the admission policy
```

Useful flags: `harvest --json`, `harvest --show-excluded`, `check --limit N`,
`--only <text>` (on most commands), `acquire --force`, `acquire --prune-files`,
`pdf --force`, `index --prune-files`.

`harvest`, `translate`, `index`, `verify`, `report`, `import` and `dependencies`
are offline. `check`, `check-browser`, `acquire`, `pdf`, `wayback`, `insecure`
and `transcripts` are the ones that reach the network or a browser.

> `inventory` parses a document's SECTION structure and suits the upstream
> project's curated documents; the year lists here are flat link lists, so it
> reports zero entries. Use `harvest` - it is the discovery route for this repo.

### harvest

Walks `git ls-files`, so only TRACKED files are ever opened. Two guards keep
private material out of the report: a git-ignored path is not tracked and so is
never listed, and any path whose RESOLVED location is outside the repository is
skipped, which is what catches a directory junction pointing at another
repository.

Every URL it drops is printed with the rule that dropped it and that rule's
reason, so a wrong exclusion is a line in the report rather than a silent
disappearance. The rules live in the tracked, hand-edited `exclude.json`, and an
unmatched URL is KEPT: the classifier fails towards review.

### check

Classifies the health of every harvested reference and writes the verdict into
`archived-references/manifest.json`. It fetches no article content.

The vocabulary is driven by what a sweep of this corpus measured, not by what a
status code suggests:

- **`blocked` is not `gone`.** A bot wall answers 403 to a client that already
  sends a browser user agent and keeps cookies, and on this corpus every such
  page was alive. So `blocked` never selects a capture and never produces a
  repair suggestion: it describes the fetcher, not the page.
- **`js-rendered` is not empty.** A 200 whose body is built by JavaScript scores
  worst of all candidates if you let it get as far as scoring, so it is
  recognised first.
- **`archived-citation` is not a fetch target.** A citation that already points
  at a capture pins that timestamp; the tool never captures a capture.

A fresh row in the optional curation ledger may skip one probe. It can never
skip acquisition: a health verdict says a page answered once, which is not
preserved bytes.

### check-browser

The escalation ladder is scoped to blocked, script-rendered, and explicitly
allow-listed dynamic rows. It runs only headless Chromium in the locked-down
toolbox container, reads the DOM after five seconds, then retries at 15 seconds
and the configured budget while the page is still a shell or waiting screen.
There is no visible or host-browser fallback.

Page JavaScript executes only in the container: it receives the network and a
throwaway tmpfs, but no checkout, content store, home directory, credentials, or
host browser profile. A rendered wall is not a document; only settled visible
article text is stored. A row nothing confirms stays UNVERIFIED and still
selects no capture.

## What is tracked, and what is not

| Path | Tracked? | Why |
|---|---|---|
| `archived-references/md/<year>/*.md` | yes | the deliverable: full content plus a mandatory attribution block |
| `archived-references/pdf/<year>/*.pdf` | yes | a PDF copy of each Markdown file, in the parallel pdf tree |
| `archived-references/manifest.json` | yes | current state per URL, bounded (one row per step) |
| `archived-references/history.jsonl` | yes | append-only journal, one line per step per run |
| `tools/references/` code and config | yes | ordinary dev tooling |
| `tools/references/cache/` | no | the workspace copy of the content store |
| the content store | no | large, third-party in raw form, and re-derivable |

The manifest is deliberately split. Keeping an append-only log inside a tracked
JSON file rewrites the whole file on every run, so history moved to JSONL, which
appends: a run adds lines instead of re-adding 700 KB to git history.

Publishing at `full` depth means the tracked Markdown IS the durable copy. If
the store is lost and the source is offline, the content still exists in git,
and rendering DOWN to `excerpt` or `metadata` needs only the tracked Markdown.
The store keeps raw bytes for provenance and for re-rendering back UP, so point
`WEBSEC_REFS_STORE` at a durable location: `git clean -xfd` deletes ignored
paths, and `verify` warns while the store is the workspace cache.

## Attribution is enforced

The archive publishes full content, so every file has to point clearly at the
original. That makes attribution the mitigation, and the tool treats it as one:

- `render` REFUSES to write a file missing the title, original URL, retrieval
  route or retrieval date;
- every file names the author, publisher, publication date, original URL, the
  route and date it was preserved by, the licence (`unknown` when unknown, never
  omitted) and a rights line pointing at the original;
- `refs.py verify` re-checks every published file and FAILS on one whose block
  has been edited away.

## Configuration

| File | What it holds |
|---|---|
| `config.json` | archive folder, per-year collection pattern, the year lists, media and PDF policy, depth, host aliases |
| `exclude.json` | which addresses are not documents, one reason per rule |
| `overrides.json` | canonical sources, author copies, mirrors, per-URL pins |
| `dependency-policy.json` | the admission gate for anything outside the standard library |

All four are hand-edited. Generated state lives in the archive manifest, so a
re-run never conflicts with a human decision.

`WEBSEC_REFS_STORE` points at the durable content-addressed store. Without it
the store falls back to the git-ignored `cache/` folder here, which is a
convenience copy and must not be the only copy of an acquired document. No store
path is ever written into tracked output.

## Tests

Offline, standard library `unittest`, no network, nothing written outside a
temporary directory:

```text
python -m unittest discover -s tools/references/tests -t tools/references
```

`tests/test_boundary.py` is the one that matters most. It parses the tool's own
source and fails if a module imports from `.claude/skills`, hard-codes a path
into it, or extends `sys.path` towards it. Together with `verify`'s check that no
year list changed during a run, the one rule is asserted, not just described.
