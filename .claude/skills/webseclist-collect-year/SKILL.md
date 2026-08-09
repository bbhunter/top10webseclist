---
name: webseclist-collect-year
description: Sweeps the internet for a given year's novel web/HTTP/API/browser security research and writes or extends that year's AI-collected candidate list at YEAR-ai.md, skipping every link already recorded in YEAR.md or YEAR-ai.md. Use when asked to collect, gather, sweep, compile, refresh, extend or "find all the techniques for" a year (2026, 2027, last year, this year so far); to build or update a YEAR-ai.md file; or to catch a year up before nominations open. Do NOT use it to score a single candidate's novelty (that is webseclist-judge-reference), to download or convert sources into archived-references/ (that is webseclist-archive-references), or to snapshot nomination and results pages (that is webseclist-archive-listings). It never edits the hand-curated year lists 2006.md..2025.md.
---

# Collect a year's web hacking techniques

You are building `<YEAR>-ai.md`: a machine-assembled, unranked, explicitly
provisional collection of candidate research published in one calendar year.
It sits beside the hand-curated year lists and never replaces them.

Two failure modes make a run worthless, and both are easy to fall into:

1. **Citing the wrong thing.** A news article about research is not the
   research. A roundup, a vendor advisory with no analysis, or a CVE record is
   not a technique writeup. The deliverable is the *original* source.
2. **Re-collecting what is already there.** The curated list for the year, and
   any previous run of this skill, already hold links. Re-adding them inflates
   the file and hides the genuinely new finds. This is what the exclusion step
   exists to prevent — do not skip it because the year "looks empty".

## Process

### 1. Resolve the year and build the exclusion set

Do this **first**, before any searching, so every downstream step can filter
against it.

```bash
python .claude/skills/webseclist-collect-year/scripts/known_links.py <YEAR> --raw
```

This reads `<YEAR>.md` and `<YEAR>-ai.md` (and handles the shared `2016-17.md`)
and prints every URL already recorded, normalised so that trailing slashes,
`www.`, http-vs-https, tracking parameters and Wayback wrappers do not produce
false "new" finds.

Read the existing `<YEAR>-ai.md` if there is one. Its **Watchlist** and
**Explicitly excluded** sections are the previous run's notes to you: they say
which artifacts had not been published yet and which candidates were already
chased down and rejected, with reasons. Start from those rather than
rediscovering them.

Fix the date window now and state it: 1 January to 31 December of the year, or
to today if the year is still running.

### 2. Sweep, split across beats

Read [references/source-map.md](references/source-map.md) — it lists the beats,
names the blogs that are currently productive, records which sources are
**confirmed dead** (so you do not spend a sweep on them), and documents the
API endpoints and workarounds for sources that block automated fetching.

Run the beats **in parallel as subagents**, one beat each, rather than
sequentially. A year is far too much ground for one context, and the beats are
independent. Give every subagent: the year and date window, the rules in
step 3, and an instruction to return structured lines plus a list of sources it
swept that produced nothing.

Subagents commonly exhaust their web-search budget mid-sweep. Tell them to fall
back to fetching index pages, feeds, sitemaps and the JSON APIs in the source
map, and to report explicitly which beats ended up under-covered — an honest
gap recorded in the Watchlist is worth more than a silent one.

Any file saved to disk while probing — a page fetched with `curl -o` to
inspect, a bot-wall response kept for a second look, a `candidates.txt`
working list — goes in the session scratchpad or the OS temp directory,
**never inside the repository**. A stray download at the repo root gets
committed and published with the list. Pass this rule to every subagent.

### 3. Rules every candidate must pass

- **Original source only.** The researcher's own blog post, the whitepaper, the
  full slide deck, the talk video, or the disclosed report. Never a news site
  (BleepingComputer, The Hacker News, SecurityWeek, DarkReading), never Reddit,
  Hacker News or an X thread, never a newsletter. Those are fine to *find*
  things through — chase the link back and cite the original.
- **A new technique**, attack class, primitive, or a meaningful extension of
  one. Exclude vendor patch announcements, plain CVE disclosures with no
  analysis, routine bug bounty writeups, product marketing, and roundups.
- **In the date window.** Verify by fetching the page; do not trust a feed's
  `<updated>` timestamp, a sitemap `lastmod`, or a search result snippet, all of
  which are known to lie. The most common error is work **disclosed the previous
  year** and merely *presented* at a conference in the target year — that
  belongs to the year of disclosure.
- **Not already recorded.** Filter candidates through the exclusion set:

  ```bash
  cat candidates.txt | python .claude/skills/webseclist-collect-year/scripts/known_links.py <YEAR> --filter --verbose
  ```

- **Grouped.** One piece of work with a blog post, slides, a video and a tool is
  **one entry** with related links, not four entries.

Apply the judging criteria from `webseclist-judge-reference` as you triage —
especially its central rule: **impact is not research value**. A CVSS 10.0 on a
famous target can teach nothing new, and an obscure parser quirk can introduce a
primitive that reshapes a class. Score the contribution, not the headline. You
do not need a full scorecard for every candidate at this stage; use the criteria
as a filter, and reach for the full skill when a call is genuinely close.

- **Keep-cut: score 60 or above.** A candidate stays in `<YEAR>-ai.md` only if a
  full `webseclist-judge-reference` scorecard puts it at **≥ 60/100** with a
  non-duplicate verdict; below 60 it is recorded in the evaluation folder but its
  link is removed from the displayed list. This cut is above the judge skill's
  general ≥ 50 supporting-reference bar and below its ≥ 70 core-technique label.
  Both provisional lists and the separately review-gated historical missed-item
  path use ≥ 60, while the historical path additionally requires publication-year
  verification and proof that the work was never nominated. Out-of-window work is
  excluded regardless of score.

### 4. Preserve every lead and judgement

Never erase a discovered candidate merely because it missed the display cut.
Maintain `ai-evaluation/<YEAR>/` as three complementary records:

- `README.md` indexes every credible lead and URL, including screened-out,
  out-of-window, removed and still-unavailable candidates;
- `judgements.md` holds every completed scorecard, whether kept or removed;
- `history.jsonl` is append-only and records each initial or changed judgement.

After changing `judgements.md`, append only changed scorecards to history:

```bash
python .claude/skills/webseclist-judge-reference/scripts/history.py \
  import-markdown --year <YEAR> --file ai-evaluation/<YEAR>/judgements.md \
  --event-type judgement
python .claude/skills/webseclist-judge-reference/scripts/history.py verify
```

Use `--event-type rejudgement` when the run deliberately revisits existing
evidence. Never edit or sort `history.jsonl` by hand; an unchanged import is a
no-op and a changed candidate links to its previous event with `supersedes`.

### 5. Verify the links

```bash
python .claude/skills/webseclist-collect-year/scripts/check_links.py <YEAR>-ai.md --only-problems
```

Read the output with judgement — the script's own docstring explains the codes.
`403` and `429` are usually anti-bot defences rather than dead links; `404` is
real and must be fixed or dropped. For a host that is down, a Wayback snapshot
is an acceptable citation **if** you say so in the entry.

### 6. Write the file

Write `<YEAR>-ai.md`. On a re-run, **merge** — keep the existing entries, add
the new ones to their sections, and update the Watchlist and exclusions rather
than starting over.

The file opens with two notices, and neither is optional. The first says a
machine assembled it; the second says it is provisional. Both exist so a reader
arriving from a search engine cannot mistake this for the curated list.

````markdown
# Web Hacking Techniques <YEAR> — AI-collected

> ## 🤖 Collected by an AI agent, not by the community
>
> **This file was assembled by an AI agent**, not by nominations, a community
> vote, or an expert panel. That is why it is named `<YEAR>-ai.md` and kept
> separate from the curated year lists (`2006.md` … ), which are maintained by
> hand. Nothing here has been reviewed by a human, so treat every line as a lead
> to check rather than a settled fact.
>
> The known failure modes of a collection built this way: a link may be
> misattributed, a date may be wrong, the "novel" claim may not survive a real
> prior-art search, and the coverage is uneven — it is biased toward sources that
> publish in English on the open web and reachable without a login.
>
> It was produced with the `webseclist-collect-year` skill, which can be re-run
> to extend it.
>
> ## ⚠️ Work in progress — this is not a Top 10
>
> <state whether the year's voting round has happened; give the exact date
> window covered; say it is unranked and incomplete.>
>
> **Judge it yourself.** Do not take inclusion here as endorsement. Use the
> `webseclist-judge-reference` skill to score any entry on its own evidence —
> original contribution, transferability, lasting value, technical soundness,
> practical usability, and clarity — and to check the prior art before treating
> something as new.
>
> Links point at the **original source**, not at news coverage of it. Where one
> piece of work has several artifacts, they are grouped on a single line.

## <Theme>

-   [Title](url) [Slides](url) [Tool](url) — Author, org

… repeat per theme …

## Watchlist — in scope but no primary artifact yet

<Confirmed to exist and in-window, but slides/paper/writeup not published.
Say what you checked and what signal you used, so the next run resumes
instead of re-searching.>

## Explicitly excluded

<Recorded so the same items are not re-chased. Group by reason: published in a
different year, not a new technique, out of web scope, source unreachable.>
````

Group entries by theme, not by source or by date. Themes that have worked:
HTTP and protocol; client-side and browser; frameworks, injection and
server-side; authentication, identity and session; AI agents and MCP as web
attack surface; CI/CD and supply chain with a web mechanism; academic papers.
Adapt them to what the year actually produced — an empty section is noise.

Match the list style of the curated year files: `-   [Title](url)` with three
spaces after the dash. Wrap any URL containing parentheses in angle brackets,
`[Title](<url>)`, or the markdown link will break.

## Handling finds from other years

A sweep for one year always surfaces work from the year before. Do not silently
drop it and do not quietly add it to a curated list.

- Record it in the **Explicitly excluded** section with its actual publication
  date, so the next run does not re-chase it.
- If it looks genuinely significant *and* is missing from that year's list, run
  the full `webseclist-judge-reference` skill on it. Only if it scores **≥ 60**
  with a non-duplicate verdict is it a candidate for the curated `<YEAR>.md`,
  and then it is added as a single reviewed line under "Other nominations" with
  the score noted in the collecting file. Below 60, it stays excluded but the
  source and judgement remain in `ai-evaluation/<YEAR>/` for audit history.

This is the **only** circumstance in which this workflow touches a curated year
list. Never bulk-add to one.

## What this skill does not do

It collects and writes `<YEAR>-ai.md`. It does **not** rank or vote, does not
produce a top ten, does not fetch or convert sources into `archived-references/`
(that is `webseclist-archive-references`), does not snapshot nomination or
results pages (that is `webseclist-archive-listings`), and does not rewrite the
hand-curated lists `2006.md`..`2025.md` beyond the single review-gated addition
path above.
