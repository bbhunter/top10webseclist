# 2025 missed-technique audit

This folder records the bounded 2026-08-09 audit for web-security research first
published in 2025 but absent from the original 2025 nomination round. The
exclusion set contained 74 distinct URLs from [`2025.md`](../../2025.md) before
this pass. Exact URL filtering was followed by semantic comparison against that
file and backward mechanism checks through the 2006–2024 lists and local
reference text.

The historical-list gate is **60 or above plus a qualifying non-duplicate
verdict**. A score alone cannot rescue prior disclosure, an existing nomination
under another URL, or work outside offensive web scope. SAML Roulette and
Universal Cross-app Attacks were retained and reassessed with the fresh leads.

## Coverage

- Primary programs and papers from NDSS, IEEE S&P and USENIX Security, plus
  the original nomination set and researcher-hosted 2025 publications.
- HTTP/2 push and signed exchanges, TLS session tickets, ZIP parsers, email
  auto-configuration, CSS fingerprinting and browser-based Rowhammer.
- Web crawling, request races, Node.js exploit synthesis, open redirects,
  password-manager extension UI, SAML and cross-app OAuth.
- Backward searches for shared-certificate HTTP/2 push attacks, parser
  differentials, CSS and extension fingerprinting, Autodiscover, TLS resumption,
  request races, Rowhammer.js, open redirects, DOM clobbering, prototype-
  pollution gadgets, SSO and state-aware Web scanning.
- Strict first-publication checks used the primary 2025 paper or disclosure;
  the 2022 shared-certificate HTTP/2 push XSS was treated as prior art rather
  than erased by the later systematic CrossPUSH/CrossSXG publication.

No archive capture was opened, validated or changed during this audit.

## Results

- 25 credible leads were retained.
- 13 candidates received full scorecards: two existing missed entries were
  reassessed and 11 fresh qualifying techniques were added.
- 12 other leads were resolved during screening as an already-represented
  mechanism, a same-beat tooling companion, defensive work or scope-adjacent.
- No full scorecard fell below 60; the screened table preserves the bounded
  exclusions so later audits need not rediscover them.

| Score | Decision | Verdict | Candidate |
|---:|---|---|---|
| 86.9 | added | Meaningful extension | [My ZIP isn't your ZIP](https://www.usenix.org/conference/usenixsecurity25/presentation/you) |
| 86.3 | added | Original technique | [STEK Sharing is Not Caring](https://www.usenix.org/conference/usenixsecurity25/presentation/hebrok) |
| 84.6 | added | Meaningful extension | [Cascading Spy Sheets](https://www.ndss-symposium.org/ndss-paper/cascading-spy-sheets-exploiting-the-complexity-of-modern-css-for-email-and-browser-fingerprinting/) |
| 84.0 | added | Original technique | [Automatic Insecurity](https://www.ndss-symposium.org/ndss-paper/automatic-insecurity-exploring-email-auto-configuration-in-the-wild/) |
| 83.0 | added | Meaningful extension | [Posthammer](https://www.usenix.org/conference/usenixsecurity25/presentation/de-ridder) |
| 80.5 | added | Tooling or methodology contribution | [EvoCrawl](https://www.ndss-symposium.org/ndss-paper/evocrawl-exploring-web-application-code-and-state-using-evolutionary-search/) |
| 80.1 | retained; reassessed | Original technique | [SAML Roulette](https://portswigger.net/research/saml-roulette-the-hacker-always-wins) |
| 79.6 | added | Tooling or methodology contribution | [RaceDB](https://doi.org/10.1109/SP61157.2025.00029) |
| 78.8 | added | Tooling or methodology contribution | [NodeMedic-FINE](https://www.ndss-symposium.org/ndss-paper/nodemedic-fine-automatic-detection-and-exploit-synthesis-for-node-js-vulnerabilities/) |
| 78.4 | added | Meaningful extension | [Cross-Origin Web Attacks](https://www.ndss-symposium.org/ndss-paper/cross-origin-web-attacks-via-http-2-server-push-and-signed-http-exchange/) |
| 77.3 | added | Tooling or methodology contribution | [Do (Not) Follow the White Rabbit](https://www.ndss-symposium.org/ndss-paper/do-not-follow-the-white-rabbit-challenging-the-myth-of-harmless-open-redirection/) |
| 76.8 | added | Meaningful extension | [Phishing Attacks against Password Manager Browser Extensions](https://www.usenix.org/conference/usenixsecurity25/presentation/anliker) |
| 75.0 | retained; reassessed | Meaningful extension | [Universal Cross-app Attacks](https://www.usenix.org/conference/usenixsecurity25/presentation/luo-kaixuan) |

## Screened leads

| Candidate | Outcome | Screening evidence |
|---|---|---|
| [YuraScanner](https://www.ndss-symposium.org/ndss-paper/yurascanner-leveraging-llms-for-task-driven-web-app-scanning/) | same-beat tooling companion | LLM goal selection improves state exploration, but EvoCrawl is the retained general state-reachability methodology from this bounded scanner beat. |
| Only as Strong as the Weakest Link: Brokered SSO | already represented mechanism | Redirect-chain and broker identity failures substantially overlap the retained cross-app OAuth and SAML architecture-confusion entries. |
| Follow My Flow | already represented tooling line | Client-side prototype-pollution gadget discovery extends a line already represented by Probe the Proto, 2024 gadget finders and the 2025 `toString` gadget nomination. |
| The DOMino Effect | already represented tooling line | Concolic DOM-clobbering gadget search improves automation, but DOM clobbering and its gadget chains are repeatedly represented from 2013 through 2024. |
| Predator: Directed Web Application Fuzzing | same-beat tooling companion | Vulnerability-validation scheduling is retained as a scanner companion rather than a separate technique beside EvoCrawl and RaceDB. |
| MOCGuard | defensive / analysis tooling | Detects missing-owner-check bugs in Java applications without introducing a distinct offensive primitive. |
| Detecting Taint-Style Vulnerabilities in Microservice-Structured Web Applications | defensive / analysis tooling | Cross-service taint analysis is useful detection engineering rather than a separate attack method. |
| XSSky | same-beat tooling companion | Local path-persistent XSS fuzzing remains a narrower scanner contribution in a year already rich in XSS techniques. |
| The Silent Danger in HTTP | already represented mechanism | Gray-box desync discovery is crowded by the nominated HTTP/1.1, chunk-terminator, trailer and reset/desync research. |
| Email Spoofing with SMTP Smuggling | earlier mechanism | SMTP smuggling was publicly established before 2025; shared-provider measurements do not create a new primitive. |
| HyTrack | scope-adjacent extension | Cross-app/Web tracking persistence is credible privacy research but is less directly an offensive Web-hacking technique than the retained CSS fingerprinting work. |
| EAGLEYE | defensive discovery | Routing analysis exposes hidden IoT Web interfaces but does not itself add an exploitation primitive. |

## Gate note

All fresh additions scored above 70, but this audit applies the repository's
current **60-or-above** historical gate. The wording in `2025.md` was corrected
accordingly. This pass did not run the reference archiver or refresh either Web
application.

## Single-publisher sweep — `blog.voorivex.team` (10 August 2026)

A later, separate pass from the audit above: rather than sweeping a year, it swept
one publisher across all years. Every post on `blog.voorivex.team` was enumerated
from the site's sitemap so pagination could not hide any — 28 posts, of which two
are already in [`2024.md`](../../2024.md) and one was judged in the 2026 round.
Six fall in the 2025 window and were read in full and judged; scorecards are in
[judgements.md](judgements.md).

| Score | Verdict | List decision | Candidate |
|---:|---|---|---|
| 61.1 | Meaningful extension | add | [Cloudflare Image Proxy as a CSPT Gadget](https://blog.voorivex.team/cloudflare-image-proxy-as-a-cspt-gadget-a-cross-origin-cspt-exploit) |
| 54.2 | Meaningful combination or adaptation | below gate | [CSS Data Exfiltration to Steal OAuth Token](https://blog.voorivex.team/css-data-exfiltration-to-steal-oauth-token) |
| 53.0 | Useful application or case study | below gate | [DOM XSS to Account Takeover: not-so-dirty dancing in a GIS SDK](https://blog.voorivex.team/not-so-dirty-dancing-in-gis-sdk) |
| 50.6 | Independent rediscovery | below gate | [Puny-Code, 0-Click Account Takeover](https://blog.voorivex.team/puny-code-0-click-account-takeover) |
| 50.5 | Meaningful combination or adaptation | below gate | [Stealing oAuth Token via Referrer Policy Override](https://blog.voorivex.team/leaking-oauth-token-via-referrer-leakage) |
| 45.0 | Useful application or case study | below gate; wrong year | [Hacking Veeam: Several CVEs and $30k Bounties](https://blog.voorivex.team/hacking-veeam-several-cves-and-30k-bounties) |

The single addition is the first entry this repository has added to a curated year
list in the 60–69.9 band, and it is marginal within that band: the load-bearing
question was whether it duplicates the Renwa CSPT roundup already cited in
`2025.md`. It does not — Renwa chains open redirects to control a *response*, this
chains a method-preserving 307 to move a state-changing *request* to another
origin — but the overlap cost it six points on reverification and the confidence
is Medium. It is a reasonable candidate for re-judging if earlier
method-preserving CSPT work surfaces.

The Veeam post is recorded here because that is where the writeup falls, but its
findings all carry 2024 CVEs and were fixed in 2024; it would fail the
first-publication gate for 2025 regardless of score.
