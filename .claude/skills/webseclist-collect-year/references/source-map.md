# Where to look, and how to reach it

Split the sweep across the beats below rather than issuing one broad search.
Web-security research does not live in one place, and a generic "best web
hacking techniques of YEAR" query returns roundups and news, which are exactly
what this workflow must not cite.

Everything in the **How to reach awkward sources** section was worked out the
hard way. Read it before fighting a 403.

---

## Beat 1 — PortSwigger and the conference circuit

- `portswigger.net/research` — the single densest source. Its RSS feed is the
  reliable way to enumerate a year.
- Black Hat USA / Asia / Europe, DEF CON, OffensiveCon, Troopers, Nullcon,
  HITB/OOTB, Hexacon, POC, SAS, OWASP Global AppSec, Pwn2Own.
- Only the web/appsec tracks. Skip kernel, firmware, baseband, TEE, hardware.

Conference dates move, and several fall late in the calendar. Check which ones
have actually happened before treating a year as thin — POC (November),
Hexacon (October), SAS (October) and Nullcon Berlin (November) all land after
a mid-year sweep.

## Beat 2 — Researcher blogs

Check each blog's own index or feed for the target year. As of August 2026 the
following were producing qualifying work:

`portswigger.net/research`, `labs.watchtowr.com`, `slcyber.io/research-center`
(Searchlight/Assetnote), `blog.trailofbits.com`, `swarm.ptsecurity.com`,
`blog.slonser.info`, `zhero-web-sec.github.io`, `blog.arkark.dev`,
`lyra.horse/blog`, `mizu.re`, `w4ke.info`, `kibty.town`, `lab.ctbb.show`
(Critical Thinking — its `feed.xml` is unusually productive),
`jorianwoltjer.com/blog`, `adragos.ro`, `blog.includesecurity.com`,
`elttam.com/blog`, `marektoth.com`, `nastystereo.com`, `blog.flomb.net`,
`blog.babelo.xyz`, `sideni.xyz`, `assured.se`, `blog.isec.pl`,
`fortbridge.co.uk/research`, `galbarnahum.com`, `blog.doyensec.com`,
`blog.quarkslab.com`, `projectzero.google`, `blog.calif.io`,
`spaceraccoon.dev`, `samcurry.net`, `ian.sh`, `flatt.tech/research`,
`blog.flatt.tech`, `synacktiv.com/en/publications`, `atredis.com/blog`,
`starlabs.sg/blog`, `blog.lexfo.fr` / `ambionics.io/blog`, `wiz.io/blog`,
`research.checkpoint.com`, `labs.zenity.io`, `labs.boostsecurity.io`,
`adnanthekhan.com`, `embracethered.com`, `guard.io/labs`,
`securitylabs.datadoghq.com`, `unit42.paloaltonetworks.com`,
`brave.com/blog`, `ethiack.com/info-hub/research`, `cyera.com/research`,
`sonarsource.com/blog`, `trufflesecurity.com/blog`, `endorlabs.com/learn`,
`oasis.security/blog`, `appomni.com/ao-labs`, `astrix.security`,
`dsinternals.com`, `dirkjanm.io`, `xlab.tencent.com`, `bentkowski.info`.

**Confirmed dead or dormant — do not spend time here** (verified August 2026):

| Source | State |
|---|---|
| `research.securitum.com` | 302s to a URL that 404s. The whole research blog is gone from the live web. Michał Bentkowski's copies survive at `bentkowski.info`. Any `archived-references/` entry citing it is now a dead link. |
| `gosecure.net` / `gosecure.ai` | Rebuilt as an SPA with no blog path at all in its sitemap. Public research publishing retired. |
| `terjanq.me` | Expired TLS certificate, 301s to X. No blog remains. |
| Bug Bounty Reports Explained | On hiatus since June 2026; RSS newest post June 2025. |
| `pentester.land` | `writeups.json` stale since late 2024. |
| `xsleaks.dev` | Last modified December 2024. |
| `ankursundara.com` | Newest post August 2024. |
| `tttang.com` | Offline (connection refused). |
| `paper.seebug.org` | Web安全 category newest post August 2025; 2026 output is almost entirely arXiv translations. |
| `blog.orange.tw` | No 2026 posts. **Trap:** its feed's `<updated>` timestamps show the current year because of a site-wide rebuild. Never infer a date from that feed. |
| `bugbountyhunter.com` | Dormant. Its own homepage banner says the content is outdated; the newest disclosed report it links dates to 2021. |
| `forum.butian.net` | Geo-blocked (`403 reason:GeoBL`) from outside China, including via reader proxies. Not empty — unreachable. |

**Reachable in a browser but not from a script:** `swarm.ptsecurity.com` (PT SWARM)
fails at the TLS/connection layer for curl from some networks while serving fine
in a browser. A `000` from the link checker on that host means the environment,
not a dead page.

### Date traps

Beyond `blog.orange.tw`, three more sources have lied about dates in practice:

- **YesWeHack** sitemap `lastmod` values are wrong — a post published October
  2025 carried a July 2026 `lastmod`. Read the date off the page.
- **Intigriti**'s `sitemap-0.xml` stamps every blog URL with the fetch date.
- **Ethiack** rendered a July 2026 research post as "July 31, **2027**" — a typo
  on their own site, not a future publication.
- A researcher's site can also carry a wrong date in its own frontmatter:
  `mizu.re`'s FCSC 2026 writeup declares September 2025, copy-pasted from the
  previous post. Cross-check against the event the post describes.

## Beat 3 — Search by mechanism, not by name

The same idea gets published under a different name years apart, so query the
*mechanism* and vary the phrasing. Sweep at minimum: request smuggling and
desync; HTTP/2, HTTP/3 and QUIC; cache poisoning and cache deception; parser
differentials and RFC ambiguity; reverse proxy, CDN and API gateway confusion;
SSRF; URL parsing confusion; GraphQL, WebSocket, SSE and webhooks; SSTI,
deserialization and SQL injection; OAuth, OIDC, SAML, passkeys and WebAuthn;
XSS, mXSS and sanitizer bypasses; CSP and Trusted Types bypasses; XS-Leaks;
CSS injection and exfiltration; clickjacking; prototype pollution; client-side
path traversal; postMessage and CORS; service workers and BFCache; browser
extensions; cookie attacks; prompt injection in agentic browsers and MCP.

## Beat 4 — Academic venues

USENIX Security, NDSS, IEEE S&P, CCS, WWW, ACSAC. Papers carry a venue date
and an embargo: USENIX cycle PDFs commonly stay embargoed until the first day
of the conference, so an abstract may be public months before the paper. Record
the abstract as a Watchlist item rather than citing a URL that does not resolve.

Watch for work whose *venue* is in the target year but whose *disclosure* was
the year before. That is the single most common date error in this workflow.

## Beat 5 — Bug bounty platform disclosures

Genuinely productive and almost never swept. See the API notes below for how to
enumerate them. Most disclosures are routine; look for the ones introducing a
primitive rather than applying a known class to a new target.

## Beat 6 — Non-English research

Chinese (`xz.aliyun.com`, `mp.weixin.qq.com`, `xlab.tencent.com`,
`security.tencent.com`, `anquanke.com`, `leavesongs.com`), Japanese
(`blog.flatt.tech`, `gmo-cybersecurity.com`, Qiita, Zenn, hatena),
Korean (`theori.io/ko`, `hackyboiz.github.io`), Russian (`habr.com`
security hub, `xakep.ru`, PT SWARM).

A standing caution learned from `xz.aliyun.com`: eight candidates from that
source were read in full and **all eight** turned out to be tutorials or
reproductions of documented behaviour, several by one author with an identical
formulaic skeleton. Non-English sources are worth sweeping, but verify against
full text before treating an abstract as a finding.

## Beat 7 — CTF-originated primitives

Occasionally a CTF produces a genuinely reusable primitive. The test is whether
the precondition exists outside the challenge: a TOCTOU in *framework* code is
reusable, a bug in challenge code is not. Judge each one explicitly rather than
including or excluding the whole category.

---

## How to reach awkward sources

These are the workarounds that turn a blocked sweep into a productive one.

**Black Hat.** `blackhat.com` HTML 403s automated fetches, but the schedule
viewer loads its data from the same directory:

    https://blackhat.com/us-26/briefings/schedule/sessions.json
    https://blackhat.com/asia-26/briefings/schedule/sessions.json

That JSON gives the complete machine-readable schedule including a `bh_files`
array of slide and whitepaper URLs, and a `recording` field. An empty
`bh_files` is a reliable signal that the deck genuinely has not been published,
which is what distinguishes a Watchlist item from a missing search.

Individual PDFs at `i.blackhat.com/<EVENT>/Presentations/<name>.pdf` return 200
even though the directory index 403s. Probing a known-good filename alongside a
bogus one confirms the probe is working before you trust a negative.

**DEF CON.** The media server path is **doubly nested** — this is not a typo:

    https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/

Village decks (AppSec, Bug Bounty, Cloud, Recon) are **not** mirrored there;
those need the village's own site. Decks land progressively across the
conference and for weeks afterwards, so a sweep during the event will be
incomplete by design.

**HackerOne.** Hacktivity is JS-rendered. Use the GraphQL endpoint:

    POST https://hackerone.com/graphql
    operationName: HacktivitySearchQuery
    index: CompleteHacktivityReportIndex
    query_string: "disclosed:true"     (sort by latest_disclosable_activity_at)

Report bodies are at `https://hackerone.com/reports/<id>.json`. Introspection is
disabled and the older `hacktivity_items` field has been removed.

**Bugcrowd.** `https://bugcrowd.com/crowdstream.json?page=N&filter_by=disclosures`

**YesWeHack.** `/learn-bug-bounty` 404s to automated fetch; enumerate via
`https://www.yeswehack.com/server-sitemap.xml`. Its `lastmod` values are
unreliable — verify the publication date on the page itself.

**xz.aliyun.com.** Listing via the undocumented JSON API
`https://xz.aliyun.com/api/v2/news?page=N` (title, author, date, abstract).
Article **bodies** sit behind an Alibaba WAF JS challenge that defeats curl,
`r.jina.ai` and Chrome `--dump-dom` alike; reading them requires driving a real
browser over CDP and polling until `#markdown-body` populates. The repo's own
`tools/references/refslib/browser.py` already does this.

**habr.com.** The `kek/v2` content API returns full article text and a `lang`
field. Check `lang: ru` and the absence of a "Перевод" label to avoid citing a
translation of English research as an original source.

**Generic fallbacks,** roughly in order of usefulness: the site's own
`feed.xml` / `atom.xml` / `rss`, then `sitemap.xml` or `sitemap_index.xml`,
then `r.jina.ai/<url>` as a reader proxy, then the Wayback CDX API
(`http://web.archive.org/cdx/search/cdx?url=example.com/post*&output=json`)
to recover a post inventory from a host that is down.
