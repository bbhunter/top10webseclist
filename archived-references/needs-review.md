<!-- WRITTEN BY HAND on 2026-08-10. Unlike needs-work.md and store-gaps.md,
     nothing generates this file: it records what one archive session changed
     without being able to judge the result. Delete a pack when it has been
     reviewed, and delete the file when they all have. -->

# References that were changed but not reviewed

**Nothing here is known to be wrong.** This is the other list: the work a sweep
could verify MECHANICALLY but not judge. A rule that removed 6,132 dead links
can prove none remain; it cannot tell you the prose reads correctly. A converter
that embedded 2,712 figures can prove each one decoded; it cannot tell you the
right picture landed in the right place.

The distinction matters because a mechanical pass reports success loudly. Every
count below came back clean, and every count below is also a place where a
confident number stands in for something nobody looked at.

Packed by the SHAPE of the review each one needs, with one real sample apiece.
Reviewing a pack means opening the sample, deciding whether the class is sound,
and then either spot-checking further or clearing the pack. Reviewing 1,326
documents one at a time is not the intent and never will be affordable.

## Written by

`refs.py acquire`, `papers`, `images`, `pdf`, `translate` and a Markdown sweep,
run 2026-08-09 to 2026-08-10. The faults they were fixing are described in the
commits `5c0a8ae` and `c5d55d8`.

---

## 1. Rendered PDFs, reprinted whole — 1,326 documents

Every PDF the archive renders was reprinted, because the converter changed:
link targets are now escaped once rather than twice, `javascript:` and `data:`
targets print as text, and preserved figures are embedded.

Two were opened and checked page by page. The other 1,324 were not.

- **Check:** the document is complete, figures sit where the prose refers to
  them, code blocks did not reflow into paragraphs, links resolve.
- **Sample:** `pdf/2025/0day-click-reveal-js.pdf`
- **Cheapest useful pass:** the widest and the narrowest, then a random ten.

## 2. Embedded figures — 2,712 images across 431 documents

Each image was fetched, decoded, resized and re-encoded. Decoding proves it was
an image; it proves nothing about WHICH image. A host that answers a hotlink
with a "no hotlinking" banner, a watermark, or a generic placeholder returns a
perfectly valid JPEG, and the pipeline would keep it.

- **Check:** the figure is the author's, not a placeholder or an anti-hotlink
  notice; the 1,100px cap left screenshots of terminals and requests readable.
- **Sample:** `md/2025/0day-click-reveal-js.md` and its PDF
- **Cheapest useful pass:** the documents with the most figures, where a
  placeholder would repeat.

## 3. Figures the reader will see fail — 992 images across 254 documents

The Markdown hotlinks the publisher's copy, and for these the archive holds
nothing: 582 hosts answered empty and 410 served something that would not
decode. The reader now gets a note naming the host instead of a broken icon.

These are the genuinely lost pictures. Whether the research survives without
them is a judgement per document, not a rule.

- **Check:** does the write-up still carry its technique with the figures gone?
  If a diagram was the finding, the reference needs a Wayback pass or a note.
- **Sample:** `2024-0x999-exploring-javascript-events-bypassing-wafs-character-normalization`
- **Route:** `refs.py wayback --only <ref>`, then `images --force --only <ref>`.

## 4. Figures refused by policy — 1,006 images

848 fell below the 200x150 figure floor and 158 were SVG, refused rather than
rasterised because rasterising an SVG means running it. Both are deliberate.
Neither has been checked for a false positive.

- **Check:** the floor did not drop a small but real diagram; no document's only
  figures were SVG.
- **Sample (floor):** `https://0day.click/parser-diff-talk-oc25/img/lol.png`
- **Sample (SVG):** a Webflow-hosted diagram on
  `aikido-security-prompt-injection-inside-github-actions-new-frontier-attacks`

## 5. Swept Markdown — 559 files

Empty-target link syntax was reduced to its label, and orphaned glyphs removed.
Zero remain, which is verified. What the sweep did NOT do is judge the prose it
left behind.

- **Check:** a former list of links still reads as a list; nothing lost meaning
  by losing its brackets.
- **Sample:** `md/2024/2024-zhero-web-security-next-js-cache-poisoning-quest-black-hole.md`

## 6. Publisher furniture still in the body — 42 documents

Related but separate: the sweep removed dead LINK SYNTAX, not site chrome. 39
documents still carry Medium's "Follow / Listen / N min read" run and 3 carry a
navigation menu. `boilerplate.trim` works inward from the edges and cannot reach
furniture sitting in the article's flow.

- **Check:** whether these are worth a rule, or whether a rule would cost more
  articles than it saves. The trim's own history says the second, twice.
- **Sample:** `md/2016-17/2017-medium-how-i-found-5-000-google-maps-xss-fiddling-protobuf.md`

## 7. Adopted publisher papers — 18 references

Where an article named a PDF of itself, that PDF is now the published document
instead of our text render. The match required the link to be same-site AND its
label to claim the document ("printable whitepaper", "print/download friendly").
Each was checked to be a valid PDF. None was read.

- **Check:** the paper is the same research as the article, not a different
  paper by the same publisher. A whitepaper is often a REWRITE of the blog post,
  which is fine and worth knowing.
- **Sample:** `blog-doyensec-com-exploiting-client-side-path-traversal-perform-cross-forgery`
- **Note:** `ibm-application-security-insider-flash-parameter-injection` took its
  paper from a hand-supplied file, its host having been dead for years. Nothing
  online can corroborate that file; it is trusted because the maintainer supplied it.

## 8. Translation pairs — 25 documents

Placeholder integrity is machine-checked: every `{{PH_n}}` came back
byte-identical, so no payload was rewritten. Meaning was not checked. Four pairs
were applied from drafts prepared in an earlier session and were not re-read at
all.

- **Check:** the English says what the original says, and the technique survives.
- **Sample:** `tttang-com-magic-way-xss-http-2`
- **Route:** the `reference-translator` agent, one chunk at a time.

## 9. Withdrawn translation pairs — 52 documents

52 English documents that quoted another script had a machine "translation" of
themselves, which the website opened INSTEAD of the original. They were removed
by a calibrated rule, not by reading each one. The threshold sits in a measured
gap (0.148 against 0.360), so no pair is near it — but the rule, not a reader,
made all 52 calls.

- **Check:** none of the 52 was genuinely bilingual in a way that made its
  English file worth keeping.
- **Sample:** `usa-25-barnett-lost-translation-exploiting-unicode-compressed`
- **Recovery:** `git show 5c0a8ae^ -- <path>` restores any of them.

## 10. Language unknown — 131 references

Their stored text is gone, so nothing can measure what language they are in.
They are reported as unknown rather than English. If any is a foreign-language
write-up, it is invisible to the translation backlog.

- **Check:** covered by fixing the store gap below; not separately reviewable.
- **Sample:** `authscope-towards-automatic-discovery-vulnerable-access-control-online-services`

## 11. Store gaps — 1,002 references

Long-standing and not from this session: the published Markdown and PDF exist,
but the content store no longer holds the bytes they were made from, so nothing
can be re-derived or compared against its source. Enumerated in
[store-gaps.md](store-gaps.md).

- **Check:** exclude the store AND the repository from the antivirus first, or
  the next sweep undoes the recovery.
- **Sample:** `2024-0x999-exploring-javascript-events-bypassing-wafs-character-normalization`
- **Route:** `refs.py acquire --force` where the source still answers,
  `wayback --missing-store` where it does not.

## 12. References kept with no document — 63

A CVE row, a vendor advisory, release notes, a package page: records by nature,
listed in [excluded.md](excluded.md). None was revisited this session, and some
were classified years of site redesigns ago.

- **Check:** the page is still a record rather than an article that has since
  grown one.
- **Sample:** `mazin-ahmed-evading-all-web-application-firewalls-xss-filters`
