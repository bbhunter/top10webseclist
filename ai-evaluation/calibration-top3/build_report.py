#!/usr/bin/env python3
"""Validate and summarize this fixed, publication-time calibration run."""
from decimal import Decimal
import csv
import json
from pathlib import Path
import re
import statistics
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
BATCHES = ['2014-2015', '2018-2020', '2021-2023', '2024-2025']
KEYS = ['original', 'transferability', 'lasting', 'technical', 'practical', 'clarity']
WEIGHTS = [25, 20, 20, 15, 10, 10]
SKILL = HERE / 'rubric-snapshot'


def main():
    candidates = json.loads((HERE / 'candidates.json').read_text())
    expected = {(r['year'], r['rank']): r for r in candidates}
    assert len(expected) == 30
    rows = []
    for batch in BATCHES:
        report = (HERE / f'{batch}.md').read_text()
        batch_rows = json.loads((HERE / f'{batch}.json').read_text())
        for row in batch_rows:
            key = (row['year'], row['rank'])
            candidate = expected[key]
            assert row['title'] == candidate['title'], key
            assert row['url'] == candidate['url'], key
            assert f'id="{key[0]}-{key[1]}"' in report, key
            section = report.split(f'<a id="{key[0]}-{key[1]}"></a>', 1)[1].split('<a id=', 1)[0]
            # Verify selection against the curated source, not only generated data.
            source = (ROOT / f'{key[0]}.md').read_text()
            ranked_lines = [line for line in source.splitlines()
                            if re.search(rf'\*\*#{key[1]}\*\*(?:\s|$)', line)]
            assert len(ranked_lines) == 1, key
            assert candidate['url'] in ranked_lines[0], key
            vals = [row['scores'][k] for k in KEYS]
            assert all(0 <= s <= 100 for s in vals), key
            helper = subprocess.check_output(
                ['python3', str(SKILL / 'scripts/score.py'), *map(str, vals)],
                text=True)
            displayed = re.search(r'Final score: ([\d.]+)/100', helper).group(1)
            assert float(displayed) == row['total'], (key, displayed, row['total'])
            assert f'Final score: {displayed}/100' in section, key
            card = [line for line in section.splitlines()
                    if line.startswith('| ') and '/100 |' in line]
            assert len(card) == 6, key
            for line, val in zip(card, vals):
                assert float(line.split('|')[2].strip().split('/')[0]) == val, key
            exact = sum(Decimal(str(s)) * w for s, w in zip(vals, WEIGHTS)) / 100
            row['exact_total'] = float(exact)
            row['archive_decision'] = re.search(r'\*\*Archive decision:\*\* (.+)', section).group(1)
            if isinstance(row['evidence_gaps'], str):
                row['evidence_gaps'] = [row['evidence_gaps']]
            row['report'] = f'{batch}.md#{key[0]}-{key[1]}'
            rows.append(row)
    rows.sort(key=lambda r: (r['year'], r['rank']))
    assert len(rows) == 30 and len({(r['year'], r['rank']) for r in rows}) == 30
    values = [r['exact_total'] for r in rows]
    counts = {str(t): sum(v >= t for v in values) for t in (50, 55, 60, 70, 80, 90)}
    stats = dict(count=30, mean=statistics.mean(values), median=statistics.median(values),
                 minimum=min(values), maximum=max(values),
                 above_80=sum(v > 80 for v in values), at_least=counts,
                 category_means={k: statistics.mean(r['scores'][k] for r in rows) for k in KEYS})
    (HERE / 'results.json').write_text(json.dumps(dict(
        evaluation_date='2026-09-09', selection_years=sorted({r['year'] for r in rows}),
        weights=dict(zip(KEYS, WEIGHTS)), statistics=stats, results=rows), indent=2,
        ensure_ascii=False) + '\n')
    with (HERE / 'results.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['year','rank','title',*KEYS,'total',
            'exact_total','verdict','confidence','cutoff','evidence_gaps','url','report'])
        writer.writeheader()
        for row in rows:
            writer.writerow({k: v for k, v in {**row, **row['scores'],
                'evidence_gaps': '; '.join(row['evidence_gaps'])}.items()
                             if k in writer.fieldnames})

    lines = ['# Top-three historical calibration', '',
        'Evaluation date: 9 September 2026. These are judgements of research value, not measurements of severity or observed historical influence.', '',
        '**30 evaluations completed.** '
        f"Mean **{stats['mean']:.1f}**, median **{stats['median']:.1f}**, range **{min(values):.1f}–{max(values):.1f}**. "
        f"**{stats['above_80']}/30 score above 80**; **{30-counts['60']}/30 score below 60**.", '',
        'The sample uses ranks 1–3 from the last ten available editions: **2014, 2015, and 2018–2025**. '
        'There are no 2016 or 2017 lists in this repository, so this is ten available editions, not ten consecutive calendar years. '
        'Selection is checked against the curated year-list Markdown.', '',
        'The skill was updated before scoring: all six categories use the original technical disclosure and earlier knowledge. '
        'Lasting value means technically grounded potential for future research. Later adoption, neglect, awards, fixes, '
        'replications and corrections contribute no points or penalties. Distinct contributions disclosed at different dates '
        'have separate cutoffs. Later document revisions are excluded.', '',
        '**Weights and thresholds were unchanged.** Originality 25%, transferability 20%, lasting value 20%, technical soundness 15%, '
        'practical usability 10%, clarity/reproducibility 10%. The skill has supporting-reference and core-technique defaults of 50 and 70 '
        '(subject to verdict); the separate preliminary-list cutoff under discussion is 60.', '',
        '## All 30 scores', '',
        'Each research title opens its full evaluation, including prior art, score reasons, confidence, and evidence gaps. '
        'O = originality; T = transferability; L = potential lasting value; S = technical soundness; P = practicality; C = clarity.', '',
        '| Year | Rank | Research | O | T | L | S | P | C | Total | Confidence |',
        '|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|']
    for row in rows:
        title = row['title'].replace('|', '\\|')
        scores = ' | '.join(str(row['scores'][k]) for k in KEYS)
        lines.append(f"| {row['year']} | {row['rank']} | [{title}]({row['report']}) | {scores} | **{row['total']:.1f}** | {row['confidence']} |")
    lines += ['', '## Threshold sensitivity', '',
        'These counts apply only a numeric cutoff to this selected sample; they do not override each report’s verdict.', '',
        '| Numeric cutoff | At or above | Below |', '|---:|---:|---:|']
    for threshold, count in counts.items():
        lines.append(f'| {threshold} | {count}/30 | {30-count}/30 |')
    additions = [r for r in rows if 55 <= r['exact_total'] < 60]
    lines += ['', f"Moving 60 to 55 would admit **{len(additions)} additional entries** in this sample:"]
    lines += ['', *[f"- [{r['title']}]({r['report']}): {r['total']:.1f}" for r in additions]]
    lines += ['', '## Interpretation and limits', '',
        'This run does not show an inability to award scores above 80. The lower-scoring winners deserve review of their '
        'specific contribution comparisons; their historical rank does not establish an obligatory score under a research-value rubric. '
        'The scores were not adjusted to make winners pass or to produce a desired distribution.', '',
        'This is a first calibration run, with one primary judge per entry and an internal skeptical second pass. '
        'Evaluators knew the sample consisted of past winners. It is not a blinded experiment, an independent consensus rating, '
        'or a measurement of repeat-run reliability. Source-version and chronology limits remain visible in each report; '
        'no historical exploit was independently rerun for this exercise.', '',
        'A positives-only sample cannot determine whether 55 or 60 best separates useful from low-value work. '
        'To estimate that boundary, add independently labelled ordinary, borderline, and duplicate work, '
        'hide reputation/rank where feasible, repeat ratings to measure disagreement, and compare missed useful work '
        'against admitted low-value work on held-out entries. Choose the tradeoff before selecting the cutoff. '
        'No threshold change is made by this run.', '',
        '## Reproduction', '',
        '- [Machine-readable results](results.json) and [CSV](results.csv).',
        '- [Selection manifest](candidates.json).',
        '- [Frozen skill](rubric-snapshot/SKILL.md), [rubric](rubric-snapshot/references/scoring-rubric.md), '
        'and [checksums](rubric-snapshot/checksums.json).',
        '- `python3 ai-evaluation/calibration-top3/build_report.py` verifies all 30 identities, source-list ranks, '
        'score ranges and helper totals, then regenerates this summary and exports. '
        'This recalculates arithmetic; it does not reproduce the research judgement.', '',
        'Reports are kept separate from the year-sweep judgement history and do not alter curated lists. '
        'Totals are shown to one decimal exactly as the helper prints them; threshold counts and descriptive statistics '
        'use unrounded weighted totals. Decimal precision reflects arithmetic, not certainty in the ratings.', '']
    (HERE / 'README.md').write_text('\n'.join(lines))
    print(json.dumps(stats, indent=2))


if __name__ == '__main__':
    main()
