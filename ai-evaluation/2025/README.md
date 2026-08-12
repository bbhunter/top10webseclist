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

## Coverage gap: ACM CCS 2025

The audit above swept NDSS, IEEE S&P and USENIX Security. **It did not sweep
ACM CCS**, and until 2026-08-10 `2025.md` carried no CCS paper at all - while
the 2024 audit did cover CCS and that year's missed list carries four of its
papers.

RebirthDay was added on 2026-08-10 from that unswept conference: it surfaced
during a sweep of Black Hat Asia 2026 decks, where it turned out to be a
re-presentation of CCS '25 work. It qualifies on its own merits, but it is one
arbitrary paper from a programme nobody has been through.

**CCS 2025 remains unaudited.** A `webseclist-find-missed` pass over that
programme is the outstanding work; this note exists so the imbalance is visible
rather than closed over by a single entry.

## CCS 2025 sweep (2026-08-11)

The gap noted above, worked. The programme was taken from dblp rather than the
ACM DL, which is walled: **396 entries**, filtered by mechanism keywords to **28**
touching a web, HTTP, browser or DNS beat, and **25** after dropping posters.
Abstracts and open-access links came from the Semantic Scholar graph API, paced,
with 429 backing off rather than being recorded as absence. No throttling
occurred.

One correction worth recording, because it nearly poisoned the sweep. The first
title-to-DOI mapping paired each dblp title with the *next* DOI in the document,
which silently shifts whenever an entry has none — "Styled to Steal" came back
with an abstract about Ethereum rollups. The reliable pairing is the COinS
`Z3988` span, which carries `rft.atitle` and `rft_id` in one attribute. It was
verified against RebirthDay, the one DOI already known independently.

### Judged in full

| Score | Verdict | List decision | Candidate |
|---:|---|---|---|
| 76.4 | Meaningful extension | add | [Styled to Steal: The Overlooked Attack Surface in Email Clients](https://doi.org/10.1145/3719027.3765189) |

### Candidates that need the paper before they can be judged

Four clear the abstract screen as offensive web technique work but resolve only
to the ACM DL, which serves a single human request and walls a script. They are
**not** rejected — they are unjudged, and each needs one pass through the reader:

| Candidate | Why it screens in |
|---|---|
| [In the DOM We Trust](https://doi.org/10.1145/3719027.3765117) | Generalises script gadgets to "DOM gadgets": benign markup injection reaching request hijacking, CSRF and UI manipulation rather than only XSS. 2.6M DOM-to-sink flows across the top 15k. |
| [Exploiting the Shared Storage API](https://doi.org/10.1145/3719027.3744848) | Attacks on a deployed Privacy Sandbox API achieving the cross-site reidentification it was built to prevent; most still work in Chrome after disclosure. |
| [The Power to Never Be Wrong](https://doi.org/10.1145/3719027.3765051) | Two threat models against web archives — crawler-evading and anachronistic adversaries who retain control of their own snapshots. Directly relevant to an archive that relies on Wayback. |
| [Be Aware of What You Let Pass](https://doi.org/10.1145/3719027.3765199) | URL-based authentication bypass in Java web apps: routing and authentication disagreeing about `/../`. 53 real vulnerabilities studied, 35 verified 0-days. |

### Screened out

Defensive, measurement or non-web: BACScan, NodeShield, Wanilla, JsDeObsBench,
Byte by Byte, the dead-drop-resolver remediation and the FIDO2 channel are
defences or detectors; the robots.txt, DNS-abuse and divergent-JavaScript papers
are measurement; CROSS-X, BASTAG, ExfilState and GhostCache are CPU and kernel
side channels with no web bearing; Swallow and GAPDiS are website-fingerprinting
attack and defence on traffic rather than web technique; Lock the Door But Keep
the Window Open is Android accessibility with a browser-rendered component, kept
as a borderline lead. RebirthDay was added separately on 2026-08-10.

## Source-set sweep — ysonet .NET deserialization references (12 August 2026)

A later, separate pass from the audit above. Rather than sweeping the year, it
swept one external corpus: the 26,422-line acquisition log
(`docs/references-md/history.jsonl`) behind the ysonet project's .NET
deserialization reference archive. That log resolves to 519 distinct documents;
16 were already recorded in this repository, and the remaining 503 were filtered
to 274 research-grade articles, whitepapers, slide decks and talks, then
title-matched against the year lists and the reference manifest to remove eight
mirrors of entries already present. The residue was pre-screened against the
judge rubric; product advisories, vendor knowledge-base articles, news coverage,
threat-intelligence reports, framework documentation, CTF and HTB writeups, and
duplicate recordings of already-listed talks were resolved during screening
rather than scored.

**Nothing was added.** Four candidates were scored, three of them above 60 but
all excluded on verdict. Scorecards in [judgements.md](judgements.md).

| Score | Verdict | List decision | Candidate |
|---:|---|---|---|
| 63.0 | Useful application or case study | not added | [More Than DoS: Progress Telerik UI for ASP.NET AJAX Unsafe Reflection (CVE-2025-3600)](https://labs.watchtowr.com/more-than-dos-progress-telerik-ui-for-asp-net-ajax-unsafe-reflection-cve-2025-3600/) |
| 62.7 | Useful application or case study | not added | [Bypassing Authentication Like It Is The 90s: Pre-Auth RCE Chains in Kentico Xperience CMS](https://labs.watchtowr.com/bypassing-authentication-like-its-the-90s-pre-auth-rce-chain-s-in-kentico-xperience-cms/) |
| 61.5 | Useful application or case study | not added | [Cache Me If You Can: Sitecore Experience Platform Cache Poisoning to RCE](https://labs.watchtowr.com/cache-me-if-you-can-sitecore-experience-platform-cache-poisoning-to-rce/) |
| 56.1 | Useful application or case study | below gate | [By Executive Order, We Are Banning Blacklists: Domain-Level RCE in Veeam (CVE-2025-23120)](https://labs.watchtowr.com/by-executive-order-we-are-banning-blacklists-domain-level-rce-in-veeam-backup-replication-cve-2025-23120/) |

Three clear the numeric gate on execution quality and are still excluded, because
the historical gate requires both a score of 60 or above **and** a novelty
verdict; "useful application or case study" is not one. The Kentico case is the
clearest: a mechanism search rather than a product search surfaced Apache CXF
CVE-2012-0803 and CVE-2013-0239, the same failure — a WS-Security UsernameToken
implementation letting the message select its own password-verification mode —
from 2012. That prior art cut the draft originality score from 66 to 48 and
changed the verdict.

### Screened leads

| Candidate | Outcome | Screening evidence |
|---|---|---|
| [SharePoint Unknown CVE Unveiled: RCE via WebPart Properties Deserialization](https://blog.viettelcybersecurity.com/sharepoint_properties_deser/) | already represented | Same team and surface as the nominated ToolShell entry for CVE-2025-53770. |
| [ViewState Deserialization Zero-Day in Sitecore (CVE-2025-53690)](https://cloud.google.com/blog/topics/threat-intelligence/viewstate-deserialization-zero-day-vulnerability/) | threat intelligence | In-the-wild exploitation reporting of sample machine keys; the technique is the 2019 ViewState entry. |
| [ASP.NET Cryptography for Pentesters](https://blog.blacklanternsecurity.com/p/aspnet-cryptography-for-pentesters) | synthesis | Consolidates machine-key and ViewState cryptography already represented from 2019 onward. |
| [Code injection attacks using publicly disclosed ASP.NET machine keys](https://www.microsoft.com/en-us/security/blog/2025/02/06/code-injection-attacks-using-publicly-disclosed-asp-net-machine-keys/) | threat intelligence | Vendor reporting on exploitation of published keys, not a new technique. |
| [SOAPwn whitepaper and slides (Black Hat EU 2025)](https://i.blackhat.com/BH-EU-25/eu-25-Bazydlo-SOAPwn-wp.pdf) | already represented | Conference artifacts of the SOAPwn research already nominated for 2025. |
| [GoldMelody Hidden Chords: in-memory IIS modules](https://unit42.paloaltonetworks.com/initial-access-broker-exploits-leaked-machine-keys/) | threat intelligence | Actor reporting on leaked-machine-key exploitation. |
