# 2023 missed-technique audit

This folder records the bounded 2026-08-09 audit for web-security research
first published in calendar year 2023 but absent from the original nomination
round. The URL exclusion set contained 69 distinct references from
[`2023.md`](../../2023.md); candidates were also compared by mechanism so URL
aliases, later proceedings copies and companion artifacts were not re-added.

The historical-list gate is **60 or above plus a qualifying non-duplicate
verdict**. First public release controls the year, not the later venue date.

## Coverage

- The complete Web/browser-relevant programs at NDSS, USENIX Security, IEEE
  S&P and ACM CCS, including browser isolation, CSP, XS-Leaks, extensions,
  Electron, JavaScript analysis, browser APIs, HTTP/3/QUIC and mini-app APIs.
- PortSwigger's 2023 research, the original nomination/result set, and the Web,
  HTTP, browser, identity and API portions of Black Hat, practitioner research
  blogs and bounty disclosures represented in the source map.
- Backward mechanism checks in `archived-references/md/` for XS-Leaks,
  fingerprinting, DOM clobbering, extension privilege boundaries, JavaScript
  static analysis, browser side channels, File System Access, database-assisted
  Web testing and client-side request forgery.
- Strict date checks for papers with older preprints. This removed several
  attractive venue-year false positives, including the previously added
  *Silent Spring* entry.

The sweep did not archive references or refresh either Web application.

## Results

- 31 credible leads are retained in this ledger.
- 17 candidates received full scorecards: 16 passed every gate and one strong
  paper failed the 2023 date gate.
- 14 additional leads were screened as wrong-year, already represented,
  defensive/measurement-only, scope-mismatched, or a weaker companion.
- No qualifying 2023 addition landed in the recovered 60–69 band.

| Score | Verdict | List decision | Candidate |
|---:|---|---|---|
| 90.2 | Tooling or methodology contribution | add | [The Leaky Web](https://trouge.net/papers/xsleaks_sp2023.pdf) |
| 89.3 | Tooling or methodology contribution | add | [DiffCSP](https://www.ndss-symposium.org/ndss-paper/diffcsp-finding-browser-bugs-in-content-security-policy-enforcement-through-differential-testing/) |
| 87.4 | Original technique | add | [Isolated and Exhausted](https://www.usenix.org/conference/usenixsecurity23/presentation/gierlings) |
| 86.7 | Tooling or methodology contribution | add | [Scaling JavaScript Abstract Interpretation](https://www.yinzhicao.org/FAST/ODGen-FAST.pdf) |
| 86.1 | Original technique | add | [RøB](https://www.usenix.org/conference/usenixsecurity23/presentation/oz) |
| 85.8 | Meaningful extension | add | [It's (DOM) Clobbering Time](https://trouge.net/publication/domclob-sp-2023/) |
| 85.0 | Tooling or methodology contribution | add | [Finding All Cross-Site Needles](https://casa.rub.de/en/research/publications/detail/finding-all-cross-site-needles-in-the-dom-stack-a-comprehensive-methodology-for-the-automatic-xs-leak-detection-in-web-browsers) |
| 84.8 | Tooling or methodology contribution | add | [SynthDB](https://www.ndss-symposium.org/ndss-paper/synthdb-synthesizing-database-via-program-analysis-for-security-testing-of-web-applications/) |
| 84.5 | Meaningful extension | add | [Fashion Faux Pas](https://www.cs.uic.edu/~polakis/papers/lin-sp23.pdf) |
| 84.5 | Tooling or methodology contribution | add | [Navigating Murky Waters](https://www.ndss-symposium.org/ndss-paper/navigating-murky-waters-automated-browser-feature-testing-for-uncovering-tracking-vectors/) |
| 84.5 | Tooling or methodology contribution | add | [CoCo](https://yinzhicao.org/CoCo/CoCo.pdf) |
| 82.9 | Original technique | add | [QUICforge](https://www.ndss-symposium.org/ndss-paper/quicforge-client-side-request-forgery-in-quic/) |
| 82.3 | Tooling or methodology contribution | add | [Uncovering Hidden APIs in Mobile Super Apps](https://arxiv.org/abs/2306.08134) |
| 80.7 | Meaningful extension | add | [Checking Passwords on Leaky Computers](https://www.usenix.org/conference/usenixsecurity23/presentation/kwong) |
| 80.5 | Tooling or methodology contribution | add | [A Security Study about Electron Applications](https://www.ndss-symposium.org/ndss-paper/a-security-study-about-electron-applications-and-a-programming-methodology-to-tame-dom-functionalities/) |
| 81.7 | Original technique | remove: first public in 2022 | [Silent Spring](https://arxiv.org/abs/2207.11171) |
| 79.2 | Tooling or methodology contribution | add | [Extending a Hand to Attackers](https://www.usenix.org/conference/usenixsecurity23/presentation/kim-young-min) |

## Screened leads

| Candidate | Outcome | Evidence |
|---|---|---|
| [Pool-Party](https://arxiv.org/abs/2112.06324) | wrong year | Complete preprint published 12 December 2021. |
| [WebSpec](https://arxiv.org/abs/2201.01649) | wrong year | Complete preprint published 5 January 2022. |
| [Awakening the Web's Sleeper Agents](https://www.ndss-symposium.org/ndss-paper/awakening-the-webs-sleeper-agents-misusing-service-workers-for-privacy-leakage/) | wrong year | NDSS 2021 paper, not a 2023 disclosure. |
| [Cross-Origin State Inference attacks](https://arxiv.org/abs/1908.02204) | wrong year | Public in August 2019 and presented at NDSS 2020. |
| [Cross-Origin Web Attacks via HTTP/2 Server Push and SXG](https://www.ndss-symposium.org/ndss-paper/cross-origin-web-attacks-via-http-2-server-push-and-signed-http-exchange/) | wrong year | NDSS and primary paper are from 2025. |
| [Are Your Sites Truly Isolated?](https://www.ndss-symposium.org/ndss-paper/are-your-sites-truly-isolated-automatically-detecting-logic-bugs-in-site-isolation-implementations/) | wrong year | Accepted at NDSS 2026. |
| [Cookie Crumbles](https://www.usenix.org/conference/usenixsecurity23/presentation/squarcina) | already represented | Already ranked #9 in the 2023 list. |
| [Server-side prototype pollution](https://portswigger.net/research/server-side-prototype-pollution) | already represented | Already present in the original nominations. |
| [CONQUER](https://www.ndss-symposium.org/ndss-paper/do-not-give-a-dog-bread-every-time-he-wags-his-tail-stealing-passwords-through-content-queries-conquer-attacks/) | scope mismatch | Android accessibility-service password theft has no sufficiently direct Web/API mechanism. |
| [Accountable JavaScript Code Delivery](https://www.ndss-symposium.org/ndss-paper/accountable-javascript-code-delivery/) | defensive architecture | Supplies accountability and auditing rather than an offensive testing primitive. |
| [Browser Permission Mechanisms Demystified](https://www.ndss-symposium.org/ndss-paper/browser-permission-mechanisms-demystified/) | measurement/systematization | Useful permissions study without a distinct offensive capability. |
| Robust Multi-tab Website Fingerprinting Attacks in the Wild | scope mismatch | Network-level Tor website fingerprinting is too remote from Web/API testing for this list. |
| TeSec: Accurate Server-side Attack Investigation for Web Applications | defensive forensics | Reconstructs attacks after compromise rather than introducing an attack or testing method. |
| SoK: A Critical Evaluation of Efficient Website Fingerprinting Defenses | survey | Synthesizes defenses and contributes no new offensive primitive. |

## Existing-entry reassessment

The prior missed section contained *Silent Spring* at 81.7. Its technical
judgement remains strong, but arXiv records the complete work on 22 July 2022.
The 2023 USENIX appearance cannot move its first-publication year, so this audit
removes it from `2023.md` while retaining the full scorecard and history event.

## Single-publisher sweep — `blog.voorivex.team` (10 August 2026)

A later, separate pass from the audit above: rather than sweeping a year, it swept
one publisher across all years. Every post on `blog.voorivex.team` was enumerated
from the site's sitemap so pagination could not hide any. Five fall in the 2023
window — the blog's earliest year. **Nothing was added.** Two are technique
writeups and were scored; the other three are bug-bounty narratives and a career
guide with no candidate contribution to judge. Scorecards are in
[judgements.md](judgements.md).

| Score | Verdict | List decision | Candidate |
|---:|---|---|---|
| 47.4 | Meaningful combination or adaptation | below gate | [Hijacking OAuth Code via Reverse Proxy for Account Takeover](https://blog.voorivex.team/hijacking-oauth-code-via-reverse-proxy-for-account-takeover) |
| 32.9 | Useful application or case study | below gate | [Uncovering a Command Injection, $2400 Bounty](https://blog.voorivex.team/uncovering-a-command-injection-2400-bounty) |

### Screened leads

| Candidate | Outcome | Screening evidence |
|---|---|---|
| [$7000 Bounty on a Single Web Application](https://blog.voorivex.team/7000-bounty-on-a-single-web-application) | not a technique candidate | Bug-bounty narrative by Amir Abbas (ImAyrix). Nine findings across standard classes (reflected and stored XSS, IDOR, upload content-type bypass) presented as a tally; the stated lesson is a recon strategy, not a technique. |
| [$9240 Bounty in 30 days Hunt Challenge](https://blog.voorivex.team/9240-bounty-in-30-days-hunt-challenge) | not a technique candidate | Bug-bounty narrative by Omid Rezaei. Twelve findings on one program (CORS, cache deception, CSV injection, 2FA bypasses) reported as outcomes; the article is about the hunt, not about a mechanism. |
| [Bug Bounty Roadmap from Scratch](https://blog.voorivex.team/bug-bounty-roadmap-from-scratch) | out of scope | A five-tier learning roadmap by Yashar Shahinzadeh that curates external resources. No security technique is described, so there is nothing for the rubric to measure. |

The three screened posts are listed rather than silently dropped so a later sweep
does not re-fetch and re-read them. They are excluded for having no candidate
contribution, which is a scope judgement rather than a low score.

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

**Two additions**, and one candidate scored below the gate. Scorecards in
[judgements.md](judgements.md).

| Score | Verdict | List decision | Candidate |
|---:|---|---|---|
| 80.7 | Original technique | added | [Second Breakfast: Implicit and Mutation-Based Serialization Vulnerabilities in .NET](https://media.defcon.org/DEF%20CON%2031/DEF%20CON%2031%20presentations/Jonathan%20Birch%20-%20Second%20Breakfast%20Implicit%20and%20Mutation-Based%20Serialization%20Vulnerabilities%20in%20.NET-whitepaper.pdf) |
| 79.5 | Original technique | added | [Exploiting ASP.NET TemplateParser — Part I](https://code-white.com/blog/exploiting-asp.net-templateparser-part-1/) |
| 57.4 | Useful application or case study | below gate | [Generating deserialization payloads for MessagePack C# Typeless mode](https://www.netwrix.com/en/resources/blog/generating-deserialization-payloads-for-messagepack-cs-typeless-mode/) |

The TemplateParser pair is judged as one piece of work (Part I, 25 September
2023; Part II, 29 September 2023). Its lasting value is evidenced inside this
repository rather than asserted: Viettel's SharePoint ToolShell writeup for
CVE-2025-53770, already archived for 2025, names Part I as the source of the
technique it used, and Mirosh's 2026 Black Hat type-conversion paper cites Part
II. Neither addition duplicates the 2023 number-two entry "Exploiting Hardened
.NET Deserialization", which is about blocklist bypass through new gadgets.

### Screened leads

| Candidate | Outcome | Screening evidence |
|---|---|---|
| [Finding Deserialization Bugs in the SolarWinds Platform](https://www.thezdi.com/blog/2023/9/21/finding-deserialization-bugs-in-the-solarwind-platform) | already represented | Same author, same year; the general method is the nominated Hexacon whitepaper. |
| [HEXACON2023 recording of Exploiting Hardened .NET Deserialization](https://www.youtube.com/watch?v=_CJmUh0_uOM) | duplicate artifact | Conference recording of the 2023 number-two nomination. |
| [Introducing Badsecrets](https://blog.blacklanternsecurity.com/p/introducing-badsecrets) | tooling for known technique | Detects known-key cryptographic material; the ViewState and machine-key techniques it checks are already nominated. |
| [Microsoft Exchange PowerShell Remoting Deserialization leading to RCE (CVE-2023-21707)](https://starlabs.sg/blog/2023/04-microsoft-exchange-powershell-remoting-deserialization-leading-to-rce-cve-2023-21707/) | product advisory | One Exchange CVE; the PowerShell-remoting attack surface is covered by the 2024 nominations. |
| [Programming with XAML: Assembly.Load for .NET deserialization](https://russtone.io/2023/05/30/programming-with-xaml/) | already represented | XAML gadget construction restating the ObjectDataProvider technique established in 2017. |
