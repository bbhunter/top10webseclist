# 2022 missed-technique audit

This folder records the fresh 2026-08-09 audit for web-security research first
published in 2022 but absent from the original 2022 nomination round. The
exclusion set contained 50 distinct URLs from [`2022.md`](../../2022.md),
including one retrospective entry from an earlier audit. Exact URL filtering
was followed by semantic comparison against every listed mechanism and backward
checks through the 2006–2021 lists.

The historical-list gate is **60 or above plus a qualifying non-duplicate
verdict**. A score alone cannot rescue prior disclosure, an original nominee
under another URL, or work first published in a different year. All credible
screened leads are retained below, including leads excluded on date or scope.

## Coverage

- Primary programs and papers from IEEE S&P, USENIX Security, NDSS, ACM CCS
  and AsiaCCS, including author pages, artifacts and first-publication checks.
- PortSwigger Research's complete 2022 archive plus primary project and
  disclosure pages for browser, HTTP and testing-methodology work.
- Browser origin, rendering, cache, CPU-port and GPU side channels; extension
  and risk-based-authentication fingerprinting; WebView identity boundaries.
- HTTP/2 and HTTP/3 connection state, censorship evasion, ReDoS, Node.js
  analysis, prototype pollution, CI workflows and collaboration-app access.
- Web privacy and policy consistency, form-data exfiltration, account creation,
  malware obfuscation and static/dynamic testing blind spots.
- Backward mechanism searches through the local 2006–2021 lists and archive.
  Candidate names were not treated as proof that the underlying idea was new.
- A non-US sweep through European and Asian institutions represented in the
  major programs and AsiaCCS. No additional non-English primary source cleared
  the date, scope, novelty and evidence gates.

No archive capture was opened, validated or changed during this audit.

## Results

- 38 credible leads retained.
- 23 candidates received full scorecards and appear in the missed section.
- 22 are fresh additions; the existing Pre-hijacked Accounts entry was
  reassessed, retained once, and given a durable scorecard/history event.
- 15 additional leads were resolved during screening as prior-year disclosure,
  defensive/measurement-only work, scope mismatch or same-mechanism overlap.
- No qualifying 2022 candidate landed in the 60–69.9 band; the lower gate was
  nevertheless applied to every retained lead.

| Score | Decision | Verdict | Candidate |
|---:|---|---|---|
| 88.8 | added | Original technique | [Hertzbleed](https://www.usenix.org/conference/usenixsecurity22/presentation/wang-yingchen) |
| 88.0 | added | Tooling or methodology contribution | [FuzzOrigin](https://www.usenix.org/conference/usenixsecurity22/presentation/kim) |
| 87.6 | added | Original technique | [Rendering Contention Channel](https://www.usenix.org/conference/usenixsecurity22/presentation/wu-shujiang) |
| 87.0 | added | Meaningful combination or adaptation | [Targeted Deanonymization via the Cache Side Channel](https://www.usenix.org/conference/usenixsecurity22/presentation/zaheri) |
| 86.7 | added | Meaningful extension | [DRAWN APART](https://orenlab.cis.bgu.ac.il/p/DrawnApart) |
| 86.3 | added | Meaningful combination or adaptation | [Phish in Sheep's Clothing](https://www.usenix.org/conference/usenixsecurity22/presentation/lin-xu) |
| 86.0 | added | Original technique | [Port Contention Goes Portable](https://thomasrokicki.github.io/publications/wpc.pdf) |
| 85.8 | added | Original technique | [Identity Confusion in WebView-based App-in-app Ecosystems](https://www.usenix.org/conference/usenixsecurity22/presentation/zhang-lei) |
| 85.3 | added | Meaningful combination or adaptation | [HTTP/3 connection contamination](https://portswigger.net/research/http-3-connection-contamination) |
| 84.4 | added | Meaningful extension | [Timing-Based Browsing Privacy Vulnerabilities Via Site Isolation](https://www.microsoft.com/en-us/research/publication/timing-based-browsing-privacy-vulnerabilities-via-site-isolation/) |
| 83.6 | added | Meaningful extension | [The Dangers of Human Touch](https://www.usenix.org/conference/usenixsecurity22/presentation/solomos) |
| 83.2 | added | Tooling or methodology contribution | [Probe the Proto](https://www.ndss-symposium.org/ndss-paper/auto-draft-207/) |
| 83.0 | added | Original technique | [Wobfuscator](https://doi.org/10.1109/SP46214.2022.00064) |
| 83.0 | added | Tooling or methodology contribution | [GET /out](https://www.usenix.org/conference/usenixsecurity22/presentation/harrity) |
| 82.9 | added | Meaningful extension | [Counting in Regexes Considered Harmful](https://www.usenix.org/conference/usenixsecurity22/presentation/turonova) |
| 82.2 | added | Tooling or methodology contribution | [Mining Node.js Vulnerabilities via Object Dependence Graph](https://www.usenix.org/conference/usenixsecurity22/presentation/li-song) |
| 81.7 | added | Original technique | [Silent Spring](https://arxiv.org/abs/2207.11171) |
| 80.3 | retained | Meaningful extension | [Pre-hijacked Accounts](https://arxiv.org/abs/2205.10174) |
| 80.2 | added | Tooling or methodology contribution | [Testability Tarpits](https://www.ndss-symposium.org/ndss-paper/auto-draft-206/) |
| 79.8 | added | Meaningful extension | [Security of Business Collaboration Platform Apps](https://www.usenix.org/conference/usenixsecurity22/presentation/chen-yunang-experimental) |
| 79.2 | added | Tooling or methodology contribution | [The Security Lottery](https://www.usenix.org/conference/usenixsecurity22/presentation/roth) |
| 76.9 | added | Tooling or methodology contribution | [Security of GitHub CI Workflows](https://www.usenix.org/conference/usenixsecurity22/presentation/koishybayev) |
| 75.3 | added | Tooling or methodology contribution | [Leaky Forms](https://www.usenix.org/conference/usenixsecurity22/presentation/senol) |

## Screened leads

| Candidate | Outcome | Screening evidence |
|---|---|---|
| [Awakening the Web's Sleeper Agents](https://www.ndss-symposium.org/ndss-paper/awakening-the-webs-sleeper-agents-misusing-service-workers-for-privacy-leakage/) | wrong year | The primary NDSS paper and repository record are from 2021. |
| [Remote Memory-Deduplication Attacks](https://arxiv.org/abs/2111.08553) | wrong year | The primary preprint was public on 16 November 2021. |
| Cross-Origin State Inference (COSI) Attacks | wrong year | The primary preprint was public in August 2019; its later venue cannot reset first disclosure. |
| Detecting web-message misconfigurations for credential theft | already represented / tooling companion | It automates the URL-token `postMessage` weakness used by the #1 Dirty Dancing OAuth entry rather than adding a separate mechanism. |
| Hijacking service workers via DOM Clobbering | original nominee | Already present in `2022.md`; it cannot be re-added through a differently described candidate. |
| How to turn security research into profit: a CL.0 case study | already represented | A scanner/permutation follow-up to the original year's browser-powered desync and HTTP conversion work. |
| Hunting evasive vulnerabilities | survey / synthesis | Valuable research advice, but it synthesises earlier cases rather than introducing one auditable mechanism. |
| Bypassing CSP with dangling iframes / Framing without iframes | narrow payload variants | Useful payloads, but not sufficiently distinct from established dangling-markup, CSP and framing primitives. |
| [XDRI Attacks](https://www.usenix.org/conference/usenixsecurity22/presentation/jeitner) | adjacent-network overlap | Special-character DNS injection and router cache weaknesses overlap the year's nominated DNS cache-poisoning research and do not add a clearer web primitive. |
| Time Does Not Heal All Wounds | defensive measurement | Measures mobile-browser policy support and vulnerable windows rather than introducing an offensive technique. |
| SWAPP | defensive framework | Uses service workers to deploy client-side defenses; no new attack contribution. |
| ScriptChecker | defensive framework | Enforces task capabilities on third-party scripts rather than introducing an offensive technique. |
| SKYPORT | defensive framework | Backports injection patches to legacy web applications; it is remediation methodology. |
| WtaGraph / Surakav | defensive systems | Detect web tracking or generate traces for a fingerprinting defense, without a distinct offensive primitive. |
| New XSS vectors / Firefox Sanitizer API bypass | narrow case studies | Individual parser and payload cases do not clear the marginal-originality gate against the year's existing XSS and WAF-bypass nominations. |

## Notes on the gate

The 2022 pass produced no 60–69.9 recovery. The lowest qualifying result was the
75.3 Leaky Forms methodology; narrower case studies were screened instead of
inflating originality to force inclusion. A later cross-year check promoted
Silent Spring from the generic prototype-pollution screening row after confirming
that its 2022 server-side universal-gadget method is distinct from Probe the Proto.
This audit did not run the reference archiver or refresh either web application.
