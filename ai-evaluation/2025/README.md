# 2025 missed-technique audit

This folder records the bounded 2026-08-09 audit for web-security research first
published in 2025 but absent from the original 2025 nomination round. The
exclusion set contained 74 distinct URLs from [`2025.md`](../../2025.md) before
this pass. Exact URL filtering was followed by semantic comparison against that
file and backward mechanism checks through the 2006–2024 lists and local
reference text.

The historical-list gate is **55 or above plus a qualifying non-duplicate
verdict**. A score alone cannot rescue prior disclosure, an existing nomination
under another URL, or work outside offensive web scope. SAML Roulette and
Universal Cross-app Attacks were retained and reassessed with the fresh leads.

## Threshold reconciliation — 9 September 2026

The current report has **32 full scorecards: 21 kept and 11 excluded**.
The missed section of `2025.md` contains **21 grouped entries**, matching the
21 qualifying cards. The dated audit results below describe their original
passes, whose threshold was 60; this section records the current 55-point gate.

All existing full cards were checked for score, verdict, original year and
nomination overlap. No previously excluded card in the 55–59.9 range qualifies:
the 56.1 Veeam case remains excluded on verdict. No stronger qualifying full
card was omitted. Three list/evaluation inconsistencies received full primary
source review and explicit evidence-based rejudgements, rather than inferred
arithmetic for the old compact scores.

| Score | Current verdict | Change | Candidate |
|---:|---|---|---|
| 69.5 | Meaningful extension | added; original August 2025 v1, not the 2026 revision | [Network-Level Prompt and Trait Leakage in Local Research Agents](https://arxiv.org/abs/2508.20282v1) |
| 56.8 | Useful application or case study | removed; replaces compact 76.8 assessment | [RebirthDay Attack](https://doi.org/10.1145/3719027.3744832) |
| 56.3 | Useful application or case study | removed; replaces full 60.1 assessment | [Gotchas in Email Parsing — Lessons From Jakarta Mail](https://www.elttam.com/blog/jakarta-mail-primitives) |

RebirthDay is correctly a 2025 publication, but RFC 7871 §11.2 (2016) already
describes both the ECS-induced concurrent queries and the missing-ECS reply
attack. Its original paper supplies useful implementation experiments and
measurements without a distinct new attack or discovery method. Jakarta's audit
checklist similarly maps established email-identity confusion into a Java
ecosystem; the review considered its tooling claim and source-level details
before excluding it. These are verdict exclusions even though both exceed 55.
The full comparisons, limits and six fresh scores are in
[judgements.md](judgements.md), with append-only history in
[history.jsonl](history.jsonl). Other scores were unchanged.

This was a bounded reconciliation, not a new conference sweep. The four
unjudged CCS leads below remain unjudged and are not displayed as techniques.
The RebirthDay and Jakarta archive texts were inspected and appeared intact;
no faulty capture was discovered. Archive and generated-site changes are handled
separately by the parent workflow.

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
then-current **60-or-above** historical gate. The wording in `2025.md` was corrected
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
re-presentation of CCS '25 work. It was provisionally accepted then; the full
9 September rejudgement above removes it after checking explicit earlier ECS
attack descriptions.

At that point CCS 2025 remained unaudited. The 11 August sweep below subsequently
addressed the programme, leaving four full-paper acquisition leads unresolved.

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
| 56.1 | Useful application or case study | excluded on verdict under current 55 gate | [By Executive Order, We Are Banning Blacklists: Domain-Level RCE in Veeam (CVE-2025-23120)](https://labs.watchtowr.com/by-executive-order-we-are-banning-blacklists-domain-level-rce-in-veeam-backup-replication-cve-2025-23120/) |

Three cleared the numeric gate at that audit, and all four clear today's 55-point
gate. They remain excluded because inclusion requires a qualifying novelty
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

## Bullseye year correction — 9 September 2026

[Bullseye’s full thesis](https://spectrum.library.concordia.ca/id/eprint/996198/) was publicly deposited on 4 November 2025. The 2026 conference paper repeats its methods and study. A fresh full review scores the original thesis **64.6**, a tooling/methodology contribution, and adds one grouped entry to the 2025 missed section after checking the original nominations. Test-guided exploitation predates it; the retained contribution is its integrated discovery workflow. The complete comparison with JSGo (2024) and PoCGen v1 (June 2025) is in [judgements.md](judgements.md).

### TranSPArent publication-year migration — 10 September 2026

[TranSPArent](https://zenodo.org/records/17822391) is retained at **69.1**, a tooling/methodology contribution first publicly preserved on 4 December 2025. Its [immutable source release](https://github.com/diwangs/transparent-ae/tree/v1.0.0) already implements test-trace call-edge stitching and template-to-JavaScript sink mapping; the February 2026 conference paper is the same contribution. A fresh six-category review, local and primary web prior-art checks and the original nomination comparison support this historical addition. The later paper was read to establish identity; its later reception was excluded from scoring. This extends the historical list to 20 grouped missed entries.

One Email, Many Faces was also migrated from the 2026 compact records after verification of its April 2025 OriginMail implementation and July 2025 full preprint. Its fresh full score is **61.3**, a supporting methodology contribution; the later conference copy is excluded from 2026. See the full evidence and qualifications in [judgements.md](judgements.md).

## Final all-years adjudication — 2026-09-10

This concludes the discovery handoff above. 3 new full judgements completed; 3 qualifying techniques added. The current addition gate is **55 plus a qualifying novelty verdict**. The [dated lead ledger](2026-09-10-sweep.md) retains the screened and held sources; the [all-years report](../2026-09-10-all-years.md) records coverage and archive outcomes.

| Research | Final score | Final verdict / disposition |
|---|---:|---|
| [Be Aware of What You Let Pass: Demystifying URL-based Authentication Bypass Vulnerability in Java Web Applications](https://racerz-fighting.github.io/paper/uabscan-ccs25.pdf) | 67.8 | Tooling or methodology contribution; added — [full card](judgements.md) |
| [The Power to Never Be Wrong: Evasions and Anachronistic Attacks Against Web Archives](https://www.securitee.org/files/kirchner_power_ccs2025.pdf) | 69.5 | Meaningful extension; added — [full card](judgements.md) |
| [In the DOM We Trust: Exploring the Hidden Dangers of Reading from the DOM on the Web](https://trouge.net/papers/in_the_dom_we_trust_ccs25.pdf) | 60.7 | Tooling or methodology contribution; added — [full card](judgements.md) |

The DOM paper was narrowed to **60.7** after comparison with 2017 script gadgets, 2023 hybrid analysis and the exact 2022 body/html lookup-order payload. The Shared Storage paper remains held for a separately established 2025 increment; its substantive earlier issue disclosures were evaluated in 2022, 2023 and 2024.

These final cards and additions supersede provisional scores and advance/hold states for the named survivors only. Other credible leads remain prescreens, with no invented numerical scores or completed rejection verdicts.
