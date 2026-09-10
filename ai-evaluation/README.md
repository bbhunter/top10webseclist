# AI evaluation records

This directory keeps the evidence and decision history for AI-assisted candidate
reviews. It is separate from the finalized year lists: finding or judging a lead
does not make it part of a historical Top 10.

Each evaluated year uses:

```text
ai-evaluation/<year>/
  README.md       searchable candidate index, including rejected and screened leads
  judgements.md   complete human-readable scorecards
  history.jsonl   append-only machine-readable judgement events
```

`history.jsonl` never replaces an earlier decision. Re-judging the same primary
URL appends an event whose `supersedes` field points to that candidate's previous
event. An initial import of an existing `judgements.md` is labelled
`baseline-import`, because its recording time is known but its original decision
time may not be.

Record all credible discovered leads in the yearly index, even when they are not
kept. Record every completed scorecard in `judgements.md`, then append changed
decisions to history:

```text
python .claude/skills/webseclist-judge-reference/scripts/history.py \
  import-markdown --year <year> --file ai-evaluation/<year>/judgements.md \
  --event-type judgement

python .claude/skills/webseclist-judge-reference/scripts/history.py verify
```

The historical missed-item gate is **55 or above plus a qualifying non-duplicate
verdict**. A past curated list also requires a verified publication year and
evidence that the technique was never nominated. Provisional `YEAR-ai.md`
collections follow their own collection workflow. Falling below an addition
threshold is never permission to erase the candidate or its judgement.

The [10 September 2026 all-years audit](2026-09-10-all-years.md) records 41 new
qualifying techniques from independent 2006–2025 searches and selected research
citation tracing, with each year's lead ledger, full scores and unresolved work.
