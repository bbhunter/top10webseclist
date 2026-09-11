#!/usr/bin/env python3
"""Render outcome-only calibration records; full calibration scoring is private."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIELDS = {'year', 'title', 'url', 'decision'}


def read_rows(path):
    rows = json.loads(path.read_text())
    if not isinstance(rows, list):
        raise ValueError(f'{path}: expected decision records')
    for row in rows:
        if set(row) != FIELDS or row['decision'] not in {'added', 'not-added'}:
            raise ValueError(f'{path}: only candidate identity and inclusion outcome may be published')
    return rows


def report(rows, title):
    lines = [f'# {title}', '',
             'These entries were already present in the original community lists.',
             'Calibration was performed privately and does not change those rankings.',
             'Only inclusion outcomes are published; future assessments use the judging skill’s current merit criteria.',
             '', '| Year | Candidate | Outcome |', '|---|---|---|']
    for row in rows:
        label = row['title'].replace('[', '\\[').replace(']', '\\]').replace('|', '\\|')
        outcome = 'Added' if row['decision'] == 'added' else 'Not added'
        lines.append(f"| {row['year']} | [{label}](<{row['url']}>) | {outcome} |")
    return '\n'.join(lines) + '\n'


if __name__ == '__main__':
    for path in sorted(ROOT.glob('20*.json')):
        path.with_suffix('.md').write_text(report(read_rows(path), f'Inclusion outcomes — {path.stem}'))
    rows = read_rows(ROOT / 'results.json')
    (ROOT / 'README.md').write_text(report(rows, 'Calibration candidate outcomes'))
    with (ROOT / 'results.csv').open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=['year', 'title', 'url', 'decision'], lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)
    print(f'Published {len(rows)} calibration outcomes without scores.')
