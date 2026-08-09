<!-- Hand-maintained. Curation decisions about the year lists, kept beside the
     archive so they are visible. Not written by refs.py; not an archived
     reference, so it carries no attribution block. -->

# Curation notes

Decisions taken about what belongs in a year list, recorded so the same question
is not re-investigated from scratch later. The year lists themselves are edited
by hand and never by tooling.

## Articles published before the year list that cites them

**Question.** `2024.md` cites a Zero Day Initiative article whose URL and
publication date are both 2022. Is that a transcription error, and are there
others like it?

**Answer: no error. All fifteen are faithful to the official announcement.**

Every entry below was checked against the nomination list published by the
curator for that year — PortSwigger for 2018 onwards, Jeremiah Grossman's blog
and WhiteHat Security for the earlier years. In all fifteen cases the article
appears in the nominations for the *later* year, exactly as this repository
records it. Research is nominated in the year it came to prominence, which is
not always the year it was published, and the curators accepted those
nominations.

**Decision (2026-08-06): leave every one of them as-is.** This repository's
value is being a faithful mirror of the official lists. Re-filing an entry under
its publication year would make the list disagree with the announcement it
mirrors — for the ZDI article specifically, the 2022 nominations contain no
`zerodayinitiative.com` links at all, so moving it to `2022.md` would invent a
nomination that never happened.

| Cited at | Published | Article | Upstream nomination |
|---|---|---|---|
| [2007.md:14](../2007.md#L14) | 2006 | Port Scan without JavaScript | in the 2007 nominations (and the 2007 top ten, at #10) |
| [2009.md:35](../2009.md#L35) | 2008 | Location based XSS attacks | in the 2009 nominations |
| [2009.md:48](../2009.md#L48) | 2008 | About CSS Attacks | in the 2009 nominations |
| [2010.md:46](../2010.md#L46) | 2009 | Generic cross-browser cross-domain theft | in the 2010 nominations |
| [2012.md:32](../2012.md#L32) | 2010 | Stuffing Javascript into DNS names | in the 2012 nominations |
| [2012.md:37](../2012.md#L37) | 2011 | How to upload arbitrary file contents cross-domain | in the 2012 nominations |
| [2012.md:45](../2012.md#L45) | 2011 | CSS :visited may be a bit overrated | in the 2012 nominations |
| [2012.md:52](../2012.md#L52) | 2011 | Bypassing Flash's local-with-filesystem Sandbox | in the 2012 nominations |
| [2015.md:46](../2015.md#L46) | 2014 | Relative Path Overwrite | in the 2015 nominations |
| [2020.md:18](../2020.md#L18) | 2019 | Write-up for a Path Traversal on Gravitee.io | in the 2020 nominations |
| [2022.md:29](../2022.md#L29) | 2021 | The great SameSite confusion | in the 2022 nominations |
| [2024.md:98](../2024.md#L98) | 2023 | Leaking Jupyter instance auth token (CVE-2023-39968) | in the 2024 nominations |
| [2024.md:107](../2024.md#L107) | 2023 | Cloudflare Pages privilege escalation and page tampering | in the 2024 nominations |
| [2024.md:121](../2024.md#L121) | 2022 | Abusing Arbitrary File Deletes to Escalate Privilege | in the 2024 nominations |
| [2025.md:62](../2025.md#L62) | 2024 | VESTA Admin Takeover via bash `$RANDOM` | in the 2025 nominations |

### How the list was produced

A year is called a mismatch when the archived document's own `published` date, or
failing that the year in its URL path, is earlier than the year list citing it.
The publication date is read from the archived copy's frontmatter, so re-running
the check after the archive grows may surface entries whose metadata was missing
before. Nine of the fifteen have no publication date in their captured metadata
and rest on the URL path alone.

## A cited host that was taken over

`secniche.org` lapsed and now serves a Thai online-gambling page. Two 2009
citations therefore fetched cleanly, passed every content check — the spam page
is full of ordinary prose — and were archived under titles like *"Google Docs
Cookie Hijacking ... Sport777 เดิมพันกีฬาออนไลน์"*. A live 200 is not evidence
that a page is still the document it was cited for.

Both were recovered from pre-hijack captures and re-filed under their real
titles, *Gmail - Google Docs Cookie Hijacking* and *IE8 Link Spoofing: Broken
Status Bar Integrity*. The Wayback digest shows exactly where the takeover
happened: the genuine page has one unchanging digest from 2009 to early 2021,
and from 2023–2024 both the digest and the size change.

The size-based capture chooser could not fix this on its own, because the spam
page (87 KB) is an order of magnitude larger than the real article (3.7 KB), and
the chooser prefers the largest capture. The recovery was done by fetching the
last genuine capture and filing it with `refs.py import`.

**Worth re-checking periodically**: any other citation whose host has since
changed ownership will have the same shape — a healthy fetch, plausible prose,
and a title that has nothing to do with web security.

### A file named for two different years is not a duplicate

An archived reference is stored as `md/<citing year>/<publication year>-<publisher>-<title>.md`.
The ZDI article is therefore at
`md/2024/2022-zero-day-initiative-...md`: filed under 2024 because `2024.md`
cites it, named `2022-` because that is when it was published. Both numbers are
correct and they mean different things. Its `cited_by` field lists `2024.md:121`
and nothing else, which is the authoritative check for whether a reference is
cited twice.
