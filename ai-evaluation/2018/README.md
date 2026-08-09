# 2018 missed-technique audit

This folder records the fresh 2026-08-08 audit for web-security research first
published in 2018 but absent from the original 2018 nomination round. The
exclusion set contained 57 distinct URLs from [`2018.md`](../../2018.md). Exact
URL filtering was followed by semantic comparison against every mechanism in
that file and backward checks through the 2006–2017 lists.

The historical-list gate is **60 or above plus a qualifying non-duplicate
verdict**. A score alone cannot rescue prior disclosure, an original nominee
under another URL, or work first published in a different year. All credible
screened leads are retained below, including leads excluded on date or scope.

## Coverage

- Full programs and primary papers from IEEE S&P, ACM CCS, NDSS, USENIX
  Security, IEEE EuroS&P and WOOT.
- Black Hat USA, PortSwigger Research and Google Project Zero's 2018 archive,
  plus author-hosted papers, tools and disclosure posts.
- Browser state and history, fingerprinting, JavaScript and Node.js,
  DOM-XSS, extensions, WebGL/GPU and speculative-execution side channels.
- OAuth, SAML, SSO SDKs, eIDAS, domain validation, BGP, cloud address reuse,
  Web PKI and certificate linting.
- Hybrid WebView bridges, `postMessage`, mobile-backed HTTP APIs, event-driven
  exploit generation, WebRTC/video calling and browser-accessible media stacks.
- Server request sequences, ReDoS, event-loop exhaustion, asynchronous-server
  memory sharing, proxy behavior, service workers and web attack forensics.
- Backward mechanism searches through the local 2006–2017 lists and archive,
  followed by primary-paper related-work and first-publication checks.
- A non-US sweep through EuroS&P, European research groups, Asian institutions
  represented in the major programs and international eID deployments. No
  additional non-English primary source cleared all gates.

No archive capture was opened, validated or changed during this audit.

## Results

- 40 credible leads retained.
- 22 candidates received full scorecards and were added to the missed section.
- 18 additional leads were resolved during screening as prior-year disclosure,
  defensive/measurement-only work, scope mismatch, prior art or a narrower
  same-mechanism companion.
- 1 addition is in the 60–69.9 band and would have been lost under the former
  above-70 rule.

| Score | Decision | Verdict | Candidate |
|---:|---|---|---|
| 94.2 | added | Original technique | [Spectre](https://spectreattack.com/spectre.pdf) |
| 88.0 | added | Meaningful extension | [Browser history re:visited](https://www.usenix.org/conference/woot18/presentation/smith) |
| 87.9 | added | Meaningful extension | [Bamboozling Certificate Authorities with BGP](https://www.usenix.org/conference/usenixsecurity18/presentation/birge-lee) |
| 87.6 | added | Original technique | [Origin Stripping Vulnerabilities](https://ieeexplore.ieee.org/document/8418635/) |
| 86.8 | added | Meaningful extension | [Grand Pwning Unit](https://download.vusec.net/papers/glitch_sp18.pdf) |
| 86.7 | added | Meaningful extension | [Cloud Strife](https://www.ndss-symposium.org/wp-content/uploads/2018/02/ndss2018_06A-4_Borgolte_paper.pdf) |
| 86.7 | added | Tooling or methodology contribution | [WARDroid](https://people.engr.tamu.edu/guofei/paper/WARDroid_SP18.pdf) |
| 86.6 | added | Tooling or methodology contribution | [SYNODE](https://www.software-lab.org/publications/ndss2018.pdf) |
| 86.5 | added | Tooling or methodology contribution | [NAVEX](https://www-personal.umd.umich.edu/~birhanu/dsplab/publications/navex-2018/) |
| 86.5 | added | Tooling or methodology contribution | [WPSE](https://www.usenix.org/conference/usenixsecurity18/presentation/calzavara) |
| 85.0 | added | Original technique | [Clock Around the Clock](https://www.eurecom.edu/publication/5664/download/sec-publi-5664.pdf) |
| 85.0 | added | Tooling or methodology contribution | [S3KVetter](https://www.usenix.org/conference/usenixsecurity18/presentation/yang) |
| 84.6 | added | Meaningful extension | [Deep Fingerprinting](https://arxiv.org/abs/1801.02265) |
| 84.5 | added | Meaningful extension | [O Single Sign-Off](https://www.usenix.org/conference/usenixsecurity18/presentation/ghasemisharif) |
| 84.0 | added | Tooling or methodology contribution | [Adventures in Video Conferencing](https://projectzero.google/2018/12/adventures-in-video-conferencing-part-1.html) |
| 83.9 | added | Meaningful extension | [A Sense of Time for JavaScript and Node.js](https://www.usenix.org/conference/usenixsecurity18/presentation/davis) |
| 83.3 | added | Tooling or methodology contribution | [Mystique](https://www.kapravelos.com/publications/mystique-CCS18.pdf) |
| 82.7 | added | Tooling or methodology contribution | [Event-Oriented Exploits in Android Hybrid Apps](https://www.ndss-symposium.org/wp-content/uploads/2018/02/ndss2018_04B-3_Yang_paper.pdf) |
| 82.6 | added | Tooling or methodology contribution | [Riding out DOMsday](https://www.ndss-symposium.org/wp-content/uploads/2018/02/ndss2018_07A-4_Melicher_paper.pdf) |
| 82.4 | added | Tooling or methodology contribution | [Freezing the Web](https://www.usenix.org/conference/usenixsecurity18/presentation/staicu) |
| 82.1 | added | Meaningful combination or adaptation | [Security Risks in Asynchronous Web Servers](https://fabianmonrose.github.io/papers/morton18.pdf) |
| 64.5 | added | Tooling or methodology contribution | [Security Analysis of eIDAS](https://www.usenix.org/conference/woot18/workshop-program) |

## Screened leads

| Candidate | Outcome | Screening evidence |
|---|---|---|
| [FP-STALKER](https://hal.inria.fr/hal-01652021) | wrong year | The primary HAL record was public on 2 December 2017; the 2018 conference appearance cannot reset first publication. |
| [Automated Website Fingerprinting through Deep Learning](https://arxiv.org/abs/1708.06376) | wrong year | The primary preprint was public on 21 August 2017. |
| [I Spy with My Little Eye](https://arxiv.org/abs/1612.00766) | wrong year | The primary preprint was public in December 2016, despite its EuroS&P 2018 appearance. |
| Rendered Insecure: GPU Side Channel Attacks are Practical | scope mismatch / companion | Requires a co-resident native OpenGL or CUDA spy; Grand Pwning Unit supplies the stronger remotely delivered browser/GPU mechanism. |
| [An Empirical Study of Web Resource Manipulation](https://www.usenix.org/conference/usenixsecurity18/presentation/zhang-xiaohan) | measurement of known mechanism | XPMChecker measures previously described host-app manipulation of WebView resources; it does not introduce a distinct offensive primitive. |
| Tracking Certificate Misissuance in the Wild / ZLint | defensive validation | Strong standards linting and ecosystem measurement, but not an offensive web technique. |
| JSgraph | forensic methodology | Reconstructs already-executed JavaScript attacks for investigation rather than finding or performing a new attack. |
| [Rampart](https://www.usenix.org/conference/usenixsecurity18/presentation/meng) | defensive system | Profiles PHP functions and blocks CPU-exhaustion attacks; the distinct offensive models are captured by Event Handler Poisoning and Freezing the Web. |
| JavaScript Zero | defensive architecture | Removes or mediates JavaScript timing sources; no separate attack contribution. |
| Veil | defensive architecture | Provides private-browsing semantics without browser changes rather than a new web attack. |
| [Fp-Scanner](https://www.usenix.org/conference/usenixsecurity18/presentation/vastel) | privacy analysis / defensive detection | Detects inconsistent or randomized browser fingerprints and sometimes recovers attributes; it does not define a sufficiently distinct attack beyond the scored fingerprint work. |
| Static Evaluation of Noninterference using Approximate Model Counting | general analysis | The method includes web examples but its core contribution is general quantitative information-flow analysis, outside the list's offensive web focus. |
| A Formal Treatment of Accountable Proxying over TLS | defensive protocol design | Exposes ambiguity in prior accountable-TLS designs but principally proposes and proves a replacement protocol. |
| A Large-scale Analysis of Content Modification by Open HTTP Proxies | measurement study | Measures known proxy injection and manipulation behavior without a new reusable attack method. |
| [Hackability Inspector](https://portswigger.net/research/hackability-inspector) | below originality gate | Useful runtime enumeration of JavaScript objects and events, but too narrow an adaptation of established devtools inspection to qualify independently. |
| Zip Slip | prior art | The 2018 branding and ecosystem study cover path traversal during archive extraction, a long-established mechanism. |
| ROBOT | wrong year | The primary Return Of Bleichenbacher's Oracle Threat disclosure was public in December 2017. |
| ClickShield | defensive system | Detects and prevents Android clickjacking; the offensive clickjacking primitive long predates 2018. |

## Notes on the gate

The eIDAS study is the only 60–69.9 addition. Its 64.5 score deliberately gives
low originality credit because XXE, SSRF and SAML attacks were established. It
qualifies narrowly for the reusable Burp testing extension and the systematic
cross-implementation workflow. This audit did not run the reference archiver
or refresh either web application.
