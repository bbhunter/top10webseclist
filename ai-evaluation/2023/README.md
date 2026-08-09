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
