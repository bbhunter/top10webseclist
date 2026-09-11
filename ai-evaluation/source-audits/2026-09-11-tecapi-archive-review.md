# TECAPI preservation review — 11 September 2026

Scope: the six newly cited documents from the [completed source audit](2026-09-11-tecapi.md).
Four new historical entries and the expanded existing SDRF/Bitrix entry are in
2010.md, 2012.md, 2013.md and 2014.md. Existing rankings are unchanged.

## Published documents

| Source | Published copies | Review result |
|---|---|---|
| AJAX Hammer | Markdown and original 17-page PDF | Complete source prose, Oren Ofer cover attribution and 9 January 2012 date verified. The original PDF preserves screenshots and code layout. |
| Diviner | Markdown and 13-page rendered PDF | Complete article, credited researchers, 30 July 2012 date and all six source images preserved. |
| Invisibility Purge | Repaired Markdown and original 65-page PDF | All 65 pages represented in the transcription, with 20 labeled figure descriptions/code transcriptions; original PDF retained unchanged. |
| .NET Havoc | Native PowerPoint text and 68-page visual PDF | All 68 original slide positions covered. Original PowerPoint retained in the content store. |
| EL 3.0/Lambda Injection | Markdown and 7-page rendered PDF | Complete article, Shay Chen attribution, 17 December 2014 date and all three source screenshots preserved. |
| SDRF | Markdown and original 7-page PDF | Full paper recovered from the author's disclosure attachment; 18 August cover date distinguished from 22 August public disclosure. |

All six have current mechanism summaries and controlled search tags, source dates,
bylines, preserved source bytes and complete PDF files. Original PDF hashes match
their published copies. New English documents need no translation; the previously
preserved Russian Bitrix article already has an English translation.

## Repairs and provenance

The first Invisibility Purge extraction contained incorrect font mappings
(`HackCcs`, `ExecuJon`, `hOp`) and broken whitespace. This was filed as a faulty
capture in the manifest and generated gap report before repair. A complete
transcription was checked against the original 65 rendered pages and imported
through the archive workflow. Its stored body is now 27,608 characters. Source
wording and visible source typos such as `OriginalRespone` and `Shotdown Missing`
remain. Opaque sample ViewState/EventValidation strings, source-cropped edges and
decorative artwork remain visible in the original PDF. The repaired capture's
current verdict is valid; the fault and repair remain in archive history.

The .NET Havoc PowerPoint has 68 slides; the conference's public SlideShare copy
has 65. Three image-only original slides (22, 24 and 26) contain additional
ViewState-editor screenshots. The published visual PDF combines the 65 verified
conference slide images with those three original screenshots at their proper
positions. All raster images were decoded and re-encoded. The manifest explicitly
records this as an archive-assembled visual PDF, **not a publisher-supplied PDF**,
and retains the original PowerPoint hash. This preserves the code and diagrams
that a text-only PowerPoint rendering omitted.

Four small screenshots were misclassified as furniture by the generic image-size
filter: Diviner's request history and EL3's three output demonstrations. They were
visually checked, decoded to pixels and re-encoded as fresh JPEGs, then recorded
individually with their source URLs and dimensions. No global image threshold was
changed. The final article PDFs contain them; inspected rendered pages show the
article text and output screenshots together.

## Fidelity limits and cleared false positives

- PDF-origin Markdown is a text reading; the preserved original PDF remains the
  source for layout, figures and exact screenshot contents. AJAX's repeated page
  headers and EY endmatter belong to the original PDF and were retained.
- The original article examples contain malformed quotes, parentheses and other
  source errors. These were not silently corrected.
- Diviner/EL3's flattened HTML layout tables leave visible pipes and some bold
  markers. The rendered examples remain readable, raw HTML is displayed, and
  figures are present. No global converter change was introduced for this run.
- Original slide closing credits, company slides and acknowledgements were
  retained. They are part of the source, not appended website navigation.
- No publisher tail was cut and no translated source was replaced.

## Checks

- Full source and prior-art scorecards: eight candidates; two further screening
  decisions. The four affected years pass the missed-list audit: 91 current
  scorecards, 88 kept. Immutable judgement history validates.
- All six new files pass title/byline/date checks against their manifest records,
  digest content-hash checks, raw/content-store existence checks, PDF signature
  checks and original-PDF hash comparisons where applicable.
- Offline PDF inspection confirms page counts of 17, 13, 65, 68, 7 and 7 and
  preserved images. Figure counts in original PDFs include masks/backgrounds,
  so they are not interpreted as counts of research figures.
- Website refresh and smoke tests pass: 1,658 records, comprising 1,555 historical
  entries and 103 preliminary 2026 leads; 1,863 reference identities.
- README counts now agree with the current source lists and generated catalogue.
  Stale duplicated archive-coverage numbers were replaced by a link to the
  authoritative generated archive index.
- The refresh retains an existing warning about the 2026 preliminary `asOf`
  date versus the file's last commit. This task adds historical research only;
  it does not assert a new 2026 research cutoff.

The initial archive verification reported 127 missing-store-object failures.
These are pre-existing byte-store gaps, not missing published documents, and
remain assigned to the generated store-gap report.

Final verification reports the identical 127 pre-existing failures and one
unreferenced-store-object warning. None names a newly added document. No new
failure class appeared, and the generated document-gap report returned to its
baseline content after the slide repair. Both host builds pass: Cloudflare stages
4,797 files (1,632,797,799 bytes); GitHub stages 214 files (169,607,336 bytes).
All new PDFs fit Cloudflare’s per-file limit; no fallback mapping changed.
