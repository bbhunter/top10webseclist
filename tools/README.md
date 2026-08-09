# tools/

Dev-only tooling. Nothing here is part of the reading list itself, and no command
in this directory ever writes a `20xx.md` year list.

There are **two** tools, and they preserve different things. Getting them mixed up
is the easiest mistake to make here, because both end up producing PDFs:

| Tool | Preserves | Output |
| --- | --- | --- |
| **`capture_pdf.py`** | the **announcement posts** — each year's nominee list and the post naming the winning ten | [`original-listings/`](../original-listings/) |
| **`references/`** | the **cited research itself** — every technique the year lists link to | `archived-references/` |

So `capture_pdf.py` archives the *index* of the list; `references/` archives the
*articles on it*. This file documents the first. For the second see
[`references/README.md`](references/README.md).

## capture_pdf.py

### Setup

- **Python 3.9+**
- **Chrome, Chromium or Edge** — auto-detected on Windows, Linux and macOS.
  Override with `WEBSEC_REFS_BROWSER=/path/to/browser`.
- **`pypdf`**, optional but wanted: it is what reads a finished PDF back, so
  `verify` can count pages and assert the expected text is really there.

```bash
pip install -r tools/requirements.txt
python tools/capture_pdf.py doctor --smoke
```

`doctor` reports the browser it found, whether `pypdf` is present, how many
manifest entries exist and how many are already captured. `--smoke` additionally
captures `example.com`, which proves the whole path works before you blame a
source page.

### Everyday use

```bash
python tools/capture_pdf.py list                  # manifest, and what is present
python tools/capture_pdf.py run                   # capture whatever is missing
python tools/capture_pdf.py run --only 2025        # just one year
python tools/capture_pdf.py run --kind nominees    # just the nominee lists
python tools/capture_pdf.py run --dry-run          # what would happen
python tools/capture_pdf.py run --force            # re-capture, overwriting
python tools/capture_pdf.py verify                 # check the whole archive
python tools/capture_pdf.py text FILE.pdf --grep "one,two"
python tools/capture_pdf.py url URL OUT.pdf        # something not in the manifest
```

`run` skips entries that already have a PDF, so it is cheap to repeat and safe to
re-run after adding a year. `--manifest` and `--outdir` point either command
somewhere else, which is also how you try a capture without touching the real
archive:

```bash
python tools/capture_pdf.py run --only 2025 --outdir /tmp/try
python tools/capture_pdf.py verify --only 2025 --outdir /tmp/try
```

Exit codes are meaningful: `run` and `verify` return non-zero if any file is
missing, thin, or fails its content assertions.

### Adding a year

Append to [`sources.json`](sources.json) and capture it:

```json
{
  "year": "2026",
  "kind": "nominees",
  "url": "https://portswigger.net/research/top-10-web-hacking-techniques-of-2026-nominations-open",
  "note": "Full nominee list for 2026.",
  "expect": ["nomination", "2026"]
}
```

```bash
python tools/capture_pdf.py run --only 2026
python tools/capture_pdf.py verify
```

Fields:

| Field | Meaning |
| --- | --- |
| `year` | Groups the files. `2016-17` is one "year", matching `2016-17.md`. |
| `kind` | `nominees`, `top10`, or an explanatory variant (`voting`, `finalists`, `nominees-and-top10`) when that year's process did not split into two pages. Free text — the output file is `<year>-<kind>.pdf`. |
| `url` | What actually gets rendered. May be a `web.archive.org` replay. |
| `original_url` | The dead original, when `url` is a replay. Recorded, never fetched. |
| `note` | Why this page, and any snapshot caveat. |
| `expect` | Strings that must appear in the rendered PDF's extracted text. |
| `scale`, `settle` | Optional per-entry overrides. |

**`expect` is the part worth caring about.** A capture that renders a 404, a
consent wall or a nominations-stage snapshot with no winners still produces a
perfectly tidy PDF. Naming a couple of strings only the real page contains — the
#1 technique, a section heading — turns that from an invisible problem into a
`SUSPECT` row. Matching is case-insensitive and whitespace-normalised, because
justified text extracts with stray non-breaking spaces.

### How the capture works, and why not `--print-to-pdf`

`chrome --headless --print-to-pdf URL` is one line and gets this wrong: it prints
through the site's **print** stylesheet, which on these pages drops the content —
a nominee list is exactly the sort of thing print CSS hides — and it cannot
scroll, so lazy-loaded images never arrive.

So the browser is driven over the DevTools Protocol instead, by
[`references/refslib/browser.py`](references/refslib/browser.py), which already
owned a hardened browser lifecycle for the other tool. `capture_pdf.py` supplies
the archival policy and calls `Ladder.render_url_pdf()`:

- **`screen` media is emulated**, so pages archive as a reader saw them.
- **The page is scrolled top to bottom** and `document.images` awaited, forcing
  lazy images to load.
- **Furniture is removed**: the Wayback Machine toolbar (injected into every
  replayed page), cookie walls, newsletter modals.
- **`fixed`/`sticky` elements are demoted to `static`**, or the site header
  reprints on every page of the PDF and covers the text under it.
- **`<details>` blocks are opened**, or they print as a summary line and silently
  lose their body.
- **The real HTTP status is recorded** via the navigation timing entry, so a
  silently-404ing URL is visible in the provenance log.
- **Archive replays get a longer settle** automatically, since a replay waits on
  the archive as well as the page.

Pages are printed to A4 at `scale: 0.7`. That is deliberate rather than cosmetic:
`printToPDF` lays out at the paper width, so A4 alone gives Chrome ~794 CSS px
and a mobile breakpoint. At 0.7 it lays out at ~1100 px and renders that at 70% —
a desktop layout at a readable size.

The browser itself gets a throwaway profile per capture, no extensions, downloads
denied, and is closed over CDP rather than by killing the launcher (which strands
the real browser process). Chrome's sandbox stays on unless you explicitly set
`WEBSEC_REFS_NO_SANDBOX=1`, which containers and most CI images need.

### Provenance

[`capture-report.json`](capture-report.json) records, per file: source URL, HTTP
status, byte size, page count, extracted-text length, capture timestamp, and any
`expect` string that was missing. It is rewritten incrementally as `run`
progresses, so an interrupted run still leaves a truthful record.

### Tests

Both tools share one suite:

```bash
python -m pytest tools/references/tests -q
```

Everything about the capture path that can be proved without launching a browser
is in `tests/test_capture_listings.py` — the guards, the option assembly, the
archival policy, and the manifest's agreement with what is actually on disk. For
the parts that need a real browser, use `doctor --smoke`.
