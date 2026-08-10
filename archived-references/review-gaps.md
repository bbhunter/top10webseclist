<!-- WRITTEN BY HAND on 2026-08-10. Unlike document-gaps.md and store-gaps.md,
     nothing generates this file: it records what one archive session changed
     without being able to judge the result. Delete a pack when it has been
     reviewed, and delete the file when they all have. -->

# References that are archived but unjudged

**Nothing here is known to be wrong, and nothing here is missing.** Every
reference below HAS its document. What it does not have is anybody's judgement
that the document came out right - the work a sweep could verify MECHANICALLY but
not judge. A rule that removed 6,132 dead links can prove none remain; it cannot
tell you the prose reads correctly. A converter that embedded 2,712 figures can
prove each one decoded; it cannot tell you the right picture landed in the right
place.

Its two sibling reports answer different questions, and confusing them is what
prompted this table:

| Report | The document | What is missing |
|---|---|---|
| [document-gaps.md](document-gaps.md) | not archived | the document itself |
| review-gaps.md | archived | a judgement that it came out right |
| [store-gaps.md](store-gaps.md) | archived | the source bytes it was made from |

So: a fully broken or missing reference belongs on `document-gaps.md`. If you
find one while working a pack here, file it there - by setting `content_gap` on
its manifest entry and re-running `refs.py index` - rather than describing it in
this file.

The distinction matters because a mechanical pass reports success loudly. Every
count below came back clean, and every count below is also a place where a
confident number stands in for something nobody looked at.

Packed by the SHAPE of the review each one needs, with one real sample apiece.
Reviewing a pack means opening the sample, deciding whether the class is sound,
and then either spot-checking further or clearing the pack. Reviewing 1,283
documents one at a time is not the intent and never will be affordable.

## Written by

`refs.py acquire`, `papers`, `images`, `pdf`, `translate` and a Markdown sweep,
run 2026-08-09 to 2026-08-10. The faults they were fixing are described in the
commits `5c0a8ae`, `c5d55d8` and `4034057`, and in the one that adds this line.

---

## 0. The Top 10 entries, 2006-2025, HAVE now been read — 205 documents

Not a pack: a subtraction from every pack below. Each of the 205 archived
documents cited by a `## Top 10` section was read and judged, and every fault
found was re-checked by two independent readers asked to REFUTE it. 35 findings
survived that; 11 did not and were dropped.

The judged set is the Top 10 lines only. **The other ~1,330 documents of
2006-2025 — the "Other nominations" and "Missed from the original list"
sections — remain unread**, and everything each pack below says still applies to
them in full.

What it corrected: 32 recorded titles that were site chrome, a blog masthead or
a PDF's file stem; 28 files renamed after their documents; and 11 captures that
were not the cited document at all — a corporate about-page filed as a 2006
Secunia advisory, `learn.microsoft.com`'s homepage as an MSRC IIS advisory, a
Blogger label sidebar as the 2009 HTTP Parameter Pollution post, an author's
faculty homepage as "Bypassing Chrome's Anti-XSS filter".

Two of those repairs found a converter fault rather than a capture fault, now
fixed in `sanitise.py` and `extract_html.py`: **a listing wrapped in an HTML
comment**, which is how Webflow's code widget escapes one. Stripping comments —
right everywhere else — had emptied all 47 request/response listings in the 2021
header-smuggling article while leaving its 47 fences in place, so the file
measured as code-bearing and read as prose above blank boxes. **A fence count is
not a listing count**; 14 more documents outside the Top 10 still show the
symptom and are a re-extraction away from the fix.

What it did NOT settle, and what the packs below should be read against:

- **Figures on the repaired documents are gone for good.** Recapturing the
  document does not recapture its pictures: the hosts that served them redirect
  to their roots. 20 screenshots for the 2023 Akamai/F5/NTLM chain, 8 for the
  2021 header-smuggling article, 4 for the securitee post, 1 for Safari Carpet
  Bomb. `images` refuses them, and it has no Wayback route. See pack 3.
- **A recapture leaves the old capture's figure rows behind.** Five entries were
  asserting the discarded page's pictures as their own — Flexera's marketing
  icons as the Secunia advisory's figures, Network Solutions' service icons as
  Safari Carpet Bomb's. Pruned for those five; two more outside the Top 10 still
  have it (`weixin-official-accounts-platform-make-xxe-attacks-brilliant` and
  one other), and any future recapture will do it again unless `acquire` learns
  to clear them.
- **Six of 17 sampled rendered PDFs are not faithful to their Markdown**, which
  narrows pack 1 without closing it. In all six the PROSE is complete and code
  blocks are not reflowed — the renderer is sound on text. Five fail only on
  pictures the archive never held, which is pack 3 again rather than a print
  fault. The sixth is a genuine renderer gap and the one worth chasing:
  `2018-slideshare-owasp-appseceu-2018-attacking-modern-web-technologies` is a
  deck whose slides ARE its content, and the archive holds 60 slide images, all
  60 present in the store and none a duplicate of another — yet the printed PDF
  embeds 52. Eight preserved slides do not reach the page, and re-running
  `images --force` then `pdf --force` does not change the count, so the loss is
  in `makepdf`, not in acquisition.
- Two documents keep a filed fault because part of the document is still
  missing: Bugzilla 369814's comment thread, and the two listings in the Struts
  S2-020 Workaround section. Both are on
  [document-gaps.md](document-gaps.md), which is where they belong.

---

## 1. Rendered PDFs, reprinted whole — 1,283 documents

Every PDF the archive renders was reprinted, because the converter changed:
link targets are now escaped once rather than twice, `javascript:` and `data:`
targets print as text, and preserved figures are embedded.

Four were opened and checked page by page. The other 1,279 were not.

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

## 6. Publisher furniture still in the body — none left

Mostly fixed since this file was written. 649 files were swept of 444,124
characters of link furniture: 3,980 invisible sign-in buttons, 975 byline
anchors that rendered as a literal `[` and a bare URL because an anchor wrapping
block content is not a Markdown link, Medium's reading-time and
Follow/Listen/Share lines, and its clap counter.

A later pass closed the rest: a call-to-action HEADING now ends a document, so a
vendor's seven-block sales panel goes whole instead of losing only the one block
a rule happened to match, and a trailing heading from a measured furniture
vocabulary goes with it. 89 files, 19,942 more characters.

Nothing in the corpus now carries two or more chrome lines. The pack is kept so
the next reader knows it was looked at rather than missed.

- **Check:** nothing outstanding. A vendor's "About <product>" closing section
  survives deliberately - over 400 characters, so the furniture rules refuse it,
  which is the guard that stops a long block being mistaken for an advert.
- **Sample:** `md/2025/2025-searchlight-cyber-novel-sql-injection-technique-pdo-prepared-statements.md`

## 6b. A stray `[` on its own line — 48 documents

The residue of the same sweep, and deliberately left alone. Of the 48, only
about 7 are an anchor wrapped around a card or an image that the collapse rule
could not reach; the rest are a `[` that OPENS DATA - a JSON array quoted in a
slide, a set-builder expression in a paper - where the line is the research.

No regex told those apart reliably, and this corpus punishes the attempt: the
same `[` begins a link and a JSON array.

- **Check:** by eye, one at a time, or not at all.
- **Sample (an anchor):** `md/2006/2006-infoworld-governator-hack-investigated.md`
- **Sample (data, leave it):** `md/2008/json-hijacking-utf-7.md`

## 7. Adopted publisher papers — 61 references

Where an article named a PDF of itself, that PDF is now the published document
instead of our text render. The match required the link to be same-site AND its
label to claim the document ("printable whitepaper", "print/download friendly",
or a label that is nothing but "Paper"). Each was checked to be a valid PDF. Two
were read; the rest were not.

43 of them are conference abstract pages - 37 from NDSS alone - which were
published as our render of a ~4,000-character abstract while the paper sat one
link away. Those are the ones where the archived Markdown and the archived PDF
now differ MOST: the abstract is what the page said, the PDF is the research.

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
