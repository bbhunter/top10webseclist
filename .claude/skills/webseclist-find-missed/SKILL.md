---
name: webseclist-find-missed
description: Finds web hacking techniques published in a past year (2006..2025) but never nominated in that year's Top 10 Web Hacking Techniques round, records every credible lead and judgement under ai-evaluation/YEAR, and adds only review-gated finds scoring 60 or above with a non-duplicate verdict under "Missed from the original list." Use when asked to find, recover, backfill, catch up on, or audit missed research for one year, a range, or all historical years. Use webseclist-collect-year for the current year, webseclist-judge-reference to score one reference without editing a list, and the archive skills to preserve sources or announcement pages.
---

# Find techniques the original nomination round missed

You are auditing one or more **past** years of the Top 10 Web Hacking Techniques
list for research that was published that year, qualifies as a web hacking
technique, was **never nominated**, and is strong enough to belong in the record.
The bar is deliberately evidence-based: a find is added to a curated year list only when a
**full `webseclist-judge-reference` evaluation scores it at least 60** with a
non-duplicate verdict — i.e. core-technique material. Everything weaker is
recorded under `ai-evaluation/<YEAR>/`, not added and never silently discarded.

This is the one workflow whose whole purpose is to make a **review-gated edit to a
curated year list** (`2006.md` .. `2025.md`). Treat that responsibility seriously:
the lists are otherwise curated by hand and are described as complete, so a weak
or wrong addition does real damage. When in doubt, do not add.

Three failure modes make a run worse than useless:

1. **Adding something that was already nominated.** The whole point is *missed*
   work. Re-adding a link already in the year file is a factual error. The
   exclusion step exists to prevent this — never skip it.
2. **Adding a duplicate or rediscovery of prior art.** A technique published in
   the target year may already have been public earlier, or may restate a known
   primitive. That is exactly what the full judge run is for. A high impact or a
   famous target is not novelty.
3. **Wrong year.** Work disclosed the year before and merely *presented* at a
   conference in the target year belongs to the year of disclosure, and is
   probably already covered there. Verify the publication date on the page.

## Inputs

The skill accepts one argument:

- a single year — `2019`
- an inclusive range — `2011-2015`
- `all` — every year from 2006 to 2025

2026 is **out of range** on purpose: its vote has not happened, so "missed" is
not yet meaningful. Collect the current year with `webseclist-collect-year`
instead. If asked for "all", or a range that spills past the ends, it is clamped
to 2006..2025.

## Process

Run the years **independently**. For a range or `all`, sweep the years in
parallel as subagents (one year per subagent) — a single context cannot hold
twenty years of research, and the years share nothing. Give each subagent the
year, the exclusion set for that year, the sweep beats, and the candidate rules
below, and have it return structured candidate lines plus the sources it swept
that produced nothing. Then judge the survivors and edit the files yourself, in
the main context, so the review-gated edits are made in one place.

### 1. Resolve the targets

```bash
python .claude/skills/webseclist-find-missed/scripts/targets.py <all|YEAR|YYYY-YYYY>
```

Each line is `YEAR<TAB>FILE` — the calendar year to search and the curated list
to append a missed entry to. 2016 and 2017 are searched separately but both
append to `2016-17.md`.

### 2. Build the exclusion set for the year

Before searching, list everything already recorded for the year so every
candidate can be filtered against it. Reuse the collect-year helper:

```bash
python .claude/skills/webseclist-collect-year/scripts/known_links.py <YEAR> --raw
```

Read the year file itself too. You are looking for gaps in what it *nominated*,
so knowing what it already holds — by technique, not just by URL — keeps you from
proposing a renamed version of an entry that is already there.

### 3. Sweep for candidates published that year

Read [the collect-year source map](../webseclist-collect-year/references/source-map.md)
for the beats, the productive blogs, the dead sources, and the API workarounds.
Search by **mechanism**, not by name, and chase every lead back to its **original
source** — never cite a news article, roundup, CVE record, or social post.

Auditing a *past* year differs from collecting the current one in two ways that
matter:

- **Prior-art direction flips.** For a missed-technique audit, the danger is that
  the candidate was *already known by the target year* (published earlier, or a
  restatement of an existing primitive). Search backward from the candidate's
  date as hard as you search for the candidate itself.
- **Sources shift with the era.** The source map is oriented to recent research.
  For 2006–2015, lean on the venues and archives that were active then —
  Black Hat / DEF CON / OWASP proceedings, `ha.ckers.org`, `blog.jeremiahgrossman.com`,
  `portswigger.net/research`, full-disclosure and bugtraq archives, academic
  proceedings (USENIX, NDSS, IEEE S&P, CCS, WWW), and the Wayback Machine for
  hosts that are gone. Many primary sources from that era survive only in the
  archive; a Wayback citation is acceptable if you say so in the entry.

Filter every candidate URL through the exclusion set:

```bash
cat candidates.txt | python .claude/skills/webseclist-collect-year/scripts/known_links.py <YEAR> --filter --verbose
```

### 4. Rules every candidate must pass before it is judged

- **Original source only** — the researcher's own post, whitepaper, slides, talk,
  or disclosed report. News coverage is a way to *find* work, never the citation.
- **A web hacking technique** — an attack class, primitive, or meaningful
  extension with a credible connection to web/HTTP/API/browser security (the
  `webseclist-judge-reference` scope section governs this). Not a vendor patch
  note, a plain CVE disclosure with no analysis, a routine bounty writeup, or a
  product roundup.
- **Published in the target calendar year** — verified by fetching the page, not
  trusting a feed or search snippet. Presented-this-year but disclosed-last-year
  belongs to last year.
- **Not already recorded** — survived the exclusion filter in step 3.
- **Plausibly 60 or above** — use the judge's rubric as a pre-screen. This is
  also the finalized-list addition gate; fully judging the 60–70 band preserves
  useful supporting research and makes close historical calls
  reviewable. Impact is not novelty; a scary CVE on a big target usually is not
  a missed *technique*. Record credible leads screened below 60 in the yearly
  evaluation index with the original URL and screening reason.

### 5. Judge each survivor in full

For every candidate that clears the pre-screen, run the complete
`webseclist-judge-reference` skill: read the source in full, search prior art in
**both** the local archive (`archived-references/md/`) and the web, compare
contributions, score the six categories, and compute the total:

```bash
python .claude/skills/webseclist-judge-reference/scripts/score.py \
  --original N --transferability N --lasting N \
  --technical N --practical N --clarity N
```

Keep the full scorecard and verdict for each — you will cite the number, and the
rejected ones are recorded so a re-run does not re-chase them.

Persist the sweep under `ai-evaluation/<YEAR>/`: `README.md` indexes every
credible lead (including candidates never advanced to a full scorecard), while
`judgements.md` contains every completed kept or rejected scorecard. Then append
the current state to the immutable history:

```bash
python .claude/skills/webseclist-judge-reference/scripts/history.py \
  import-markdown --year <YEAR> --file ai-evaluation/<YEAR>/judgements.md \
  --event-type judgement
python .claude/skills/webseclist-judge-reference/scripts/history.py verify
```

For an explicit repeat audit, use `--event-type rejudgement`. Never rewrite or
sort `history.jsonl`; unchanged scorecards add nothing, and changed ones append
with a `supersedes` link.

After a range or all-years run, audit score arithmetic, latest history state,
the 60-point gate, and the projection into every curated missed section:

```bash
python .claude/skills/webseclist-find-missed/scripts/audit.py
```

The audit is read-only. Fix any reported mismatch in the readable scorecard and
curated entry, then re-import the corrected card as `rejudgement` so history
records the change instead of hiding it.

**Addition gate:** add to the year file only if **final score >= 60** *and* the
verdict is a novelty verdict (Original technique, Meaningful extension, Meaningful
combination/adaptation, or Tooling/methodology). A score below 60,
or a Duplicate / Independent-rediscovery / Insufficient-evidence verdict, does
**not** qualify — record it as a rejected lead instead. The historical
missed-technique workflow deliberately uses a broader gate than the judge
skill's general ≥70 default while still requiring a full scorecard and a
non-duplicate verdict for every list addition.

### 6. Add the passers to the end of the year file

Edit `<YEAR>.md` **by hand** (with the editor, not a script — the year lists are
hand-curated and no tooling writes them). Append a single new section at the very
end of the file, after `## Other nominations`:

```markdown
## Missed from the original list

> These techniques were **not** part of this year's original nomination round.
> Each was found in a later audit, evaluated in full with the
> `webseclist-judge-reference` skill, and scored **60 or above** (qualifying
> material) with a non-duplicate verdict before being added here. The judge score
> and verdict are noted per entry. Added <YYYY-MM-DD>.

-   [Title](url) [Slides](url) — **judge NN/100**, <verdict> — Author, org
```

Rules for the entries, matching the house style of the year files:

- One `-   ` bullet per technique (three spaces after the dash), no trailing
  backslashes, no blank lines inside the list.
- Group multiple artifacts of one piece of work (post, slides, video, tool) on a
  single line with adjacent `[Label](url)` links, exactly as the curated lists do.
- Wrap any URL containing parentheses as `[Title](<url>)` so the link does not
  break.
- **Non-English source:** give the entry an English title (translate it, and keep
  the original-language title in parentheses if useful), so the list stays
  readable. The English gloss in the list is not a substitute for the archive's
  full translation — see the Downstream note below.
- State the judge score and the one-line verdict for each entry — this is what
  distinguishes a review-gated addition from an ordinary nomination.
- If the section already exists from a previous run, **merge** into it (add new
  bullets, keep the date line as the earliest run and note the new date if you
  like) rather than creating a second section.
- If a year yields nothing at or above 60, **add nothing** and say so in the report.
  An empty result is the correct and common outcome for a well-curated year.

### 7. Report

For each year, report: how many candidates were swept, how many were judged in
full, each judged candidate's score and verdict, what was added, and what was
rejected and why. Be honest about coverage gaps — an unswept beat is a lead for
next time, not a silent omission. Do not inflate the yield; most years will
add zero or one.

## Downstream

Adding links to a year list can leave generated website data stale. It is not
edited by hand:

- `website/data/catalogue.json` and `website/data/collections/*.json` are
  regenerated by `node website/build-data.mjs`. Re-run it after adding entries.
- The archived-references archive (`archived-references/`) may not yet hold the
  newly added sources. Preserving them is the separate `webseclist-archive-references`
  workflow, not this one — run it for each newly added entry so the missed finds
  get the same Markdown-plus-PDF treatment as the rest of that year.
- **A non-English added source MUST be archived with an English translation.**
  When `webseclist-archive-references` preserves a non-English find, it has to
  produce the translated English Markdown file **and** a translated (English)
  title alongside the original-language capture — the same translation pair every
  other non-English archived reference carries (the `reference-translator` agent
  handles the prose; record both the original and the translated title). Never
  leave a non-English missed find archived without its English translation and
  translated title.

If a sweep turns up a **faulty capture** in the reference archive (a file the
manifest advertises but the tree lacks, a capture of the wrong page, a junk
render), file it per the repository rule: set `content_gap` on the entry in
`archived-references/manifest.json` and re-run `python tools/references/refs.py index`.
Do not edit `archived-references/document-gaps.md` by hand.

## What this skill does not do

It finds missed techniques for **past** years and makes the review-gated addition
to a curated list. It does **not** collect the current year into `YEAR-ai.md`
(that is `webseclist-collect-year`), does not re-rank or re-vote a year, does not
touch 2026, does not fetch or convert sources into `archived-references/` (that is
`webseclist-archive-references`), and does not snapshot announcement pages (that
is `webseclist-archive-listings`). A below-60 result is a recommendation to leave
the list unchanged, not a licence to lower the bar.
