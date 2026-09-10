# Store recovery review — 10 September 2026

The starting backlog contained 219 missing object fields across 181 references. The recovery pass resolved 92 fields; 127 fields across 101 references remain unavailable. These are source-store gaps, not missing published documents.

| Result | Fields |
| --- | ---: |
| Original bytes restored with the exact historical SHA-256 | 31 |
| Replacement raw capture verified against the complete held document | 35 |
| Verified browser capture (including shared raw/DOM pointers) | 18 |
| Extraction object recovered from published Markdown or a visually corrected PDF transcription | 8 |
| Still unavailable | 127 |

The 31 exact fields refer to 29 unique restored objects. Replacement captures are new objects: their historical hashes and recovery provenance remain in the append-only history. Complete body comparison was required before accepting changed HTML or DOM captures. Extraction reconstruction does not claim to recover historical source bytes.

The pass checked the configured store and local caches, attempted original and recorded/Wayback retrieval routes for 173 source URLs, and tried browser rendering for all 44 missing DOM objects using Windows Docker. Eight missing extracted-content objects were recovered through published-body reconstruction or the PDF review. Failed requests, changed pages, incomplete bodies and captures that could not be matched to the held document were not substituted for the source.

Remaining fields comprise 93 raw captures, 32 browser DOM captures and two landing pages. The generated [store gaps](../../archived-references/store-gaps.md) are the current queue; [field-by-field evidence](2026-09-10-store-recovery.json) records baseline hashes, outcomes, bounded network attempts and accepted recovery events.

The subsequent Top 10 review resolved three additional raw-source fields through complete recovered decks and a visually verified slide-host capture; these are included in the 35 replacement raw captures above.

Published bodies and PDFs were retained during store recovery. Separately documented PDF transcription repairs intentionally update the Markdown after visual comparison with the original pages. No broad forced re-extraction was used.

The archive-wide offline verification returned exactly 127 missing-store-object failures and one warning for unreferenced store objects. It reported no other failures. Unreferenced stored bytes were retained.
