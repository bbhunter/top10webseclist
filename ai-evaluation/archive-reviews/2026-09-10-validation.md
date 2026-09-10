# Validation — 10 September 2026

- Archive test suite: 953 tests passed using the Windows Docker fallback and temporary Pillow test dependencies.
- Published review artifacts: all 40 initial PDF transcriptions and all 57 additional capture repairs passed full reviewed-body containment, curated frontmatter, and local-figure checks. Recovered original PDF copies matched their verified source hashes. The timing-channel PDF matched its reconstructed 50-slide artifact.
- Final archive-wide `refs.py verify`: 127 missing-store-object failures and one warning for 3,276 unreferenced stored objects; no other failures. Unreferenced bytes were retained. This is an integrity result, not a claim that unresolved source captures have become available.
- Archive indexes and generated document/store gap reports regenerated. The handwritten review queue was retained and updated with explicit completed-scope notes.
- Website refresh and all smoke checks passed: security 86/86, constellation 29/29, requested views 100/100, mobile/deployment 79/79, contribution 46/46, room filter 21/21.
- Progressive website data: 1,613 records in 20 collections; 8,753-byte catalogue and 3,011,494 bytes of collection data, within the configured budgets.
- Cloudflare build: 4,701 files staged, 1,571,996,681 bytes; configured large-PDF fallbacks delegated to GitHub Pages. GitHub build: 214 files staged, 169,607,336 bytes.

The fresh Top 10 work reviewed 2,130 PDF pages plus 50 original slide images. Its 193 Mermaid occurrences use 171 unique inert, hash-verified SVG assets. Visual checks repaired missing-glyph labels and two hidden edges; source topology and original figures were preserved. One generated six-page article PDF was inspected to verify all four recovered PNG images render correctly.

Remaining limitations are explicit: 127 source-store fields, three partially repaired Top 10 references missing illustrations, and two inaccessible supporting Zenodo records from the newly added research. Earlier full review was retained for 111 unchanged Top 10 bodies after complete body comparison; these were not freshly reread. Additional nomination/preliminary layout-review work stays on the handwritten review queue.

See [threshold review](2026-09-10-threshold-review.md), [store recovery](2026-09-10-store-recovery.md), and [Top 10 coverage](2026-09-10-top10-coverage.md). These checks were completed locally before publication.
