# 2021 missed-technique audit

This folder records the bounded 2026-08-09 audit for web-security research first
published in 2021 but absent from the original 2021 nomination round. The
exclusion set contained 41 distinct URLs from [`2021.md`](../../2021.md) before
this pass. Exact URL filtering was followed by semantic comparison against that
file and backward mechanism checks through the 2006–2020 lists and local
reference text.

The historical-list gate is **60 or above plus a qualifying non-duplicate
verdict**. A score alone cannot rescue prior disclosure, an existing nomination
under another URL, or work outside offensive web scope. ALPACA, the entry found
by the earlier audit, was retained and reassessed alongside the fresh leads.

## Coverage

- Primary programs, papers and author pages for NDSS, IEEE S&P, ACM CCS and
  USENIX Security, plus the original PortSwigger nomination set.
- Browser process isolation and speculative execution, scriptless cache side
  channels, extension and browser fingerprinting, favicon caches and URL
  auto-linkification.
- Client-side CSRF, Node.js object-property propagation, object injection,
  ReDoS, DNS poisoning and PDF action/file-path processing.
- Backward mechanism searches for Spectre and Site Isolation, CSS and cache
  side channels, extension detection, CSRF, prototype pollution, serialization
  gadgets, ReDoS, DNS poisoning, PDF attacks, URL parsing and fingerprinting.
- Strict first-publication checks: a 2021 venue appearance did not override an
  earlier public preprint, and a later venue did not exclude a 2021 disclosure.

No archive capture was opened, validated or changed during this audit.

## Results

- 28 credible leads were retained.
- 13 candidates received full scorecards: ALPACA was reassessed and 12 fresh
  qualifying techniques were added.
- 15 other leads were resolved during screening as wrong-year, later-year,
  already covered, defensive/measurement work or scope-adjacent research.
- No full scorecard fell below 60. One fresh addition scored between 60 and 70;
  the screened table preserves the rejected leads for future audits.

| Score | Decision | Verdict | Candidate |
|---:|---|---|---|
| 85.5 | added | Meaningful extension | [Spook.js](https://www.spookjs.com/) |
| 84.4 | added | Meaningful extension | [Prime+Probe 1, JavaScript 0](https://arxiv.org/abs/2103.04952) |
| 83.7 | added | Original technique | [Tales of Favicons and Caches](https://www.ndss-symposium.org/ndss-paper/tales-of-favicons-and-caches-persistent-tracking-in-modern-browsers/) |
| 83.5 | added | Original technique | [JAW](https://www.usenix.org/conference/usenixsecurity21/presentation/khodayari) |
| 82.3 | added | Original technique | [Abusing Hidden Properties to Attack Node.js](https://www.usenix.org/conference/usenixsecurity21/presentation/xiao) |
| 81.8 | added | Meaningful extension | [DNS Cache Poisoning Attack: Resurrections with Side Channels](https://www.cs.ucr.edu/~zhiyunq/pub/ccs21_dns_poisoning.pdf) |
| 80.4 | added | Meaningful extension | [Processing Dangerous Paths](https://www.ndss-symposium.org/ndss-paper/processing-dangerous-paths-on-security-and-privacy-of-the-portable-document-format/) |
| 80.0 | retained; reassessed | Original technique | [ALPACA](https://alpaca-attack.com/) |
| 78.7 | added | Tooling or methodology contribution | [SerialDetector](https://www.ndss-symposium.org/ndss-paper/serialdetector-principled-and-practical-exploration-of-object-injection-vulnerabilities-for-the-web/) |
| 78.4 | added | Meaningful extension | [Fingerprinting in Style](https://www.usenix.org/conference/usenixsecurity21/presentation/laperdrix) |
| 78.1 | added | Tooling or methodology contribution | [Revealer](https://research.cuhk.edu.hk/en/publications/revealer-detecting-and-exploiting-regular-expression-denial-of-se-2/) |
| 71.8 | added | Meaningful extension | [Gummy Browsers](https://arxiv.org/abs/2110.10129) |
| 69.4 | added | Meaningful extension | [To Err.Is Human](https://www.ndss-symposium.org/ndss-paper/to-err-is-human-characterizing-the-threat-of-unintended-urls-in-social-media/) |

## Screened leads

| Candidate | Outcome | Screening evidence |
|---|---|---|
| [Awakening the Web's Sleeper Agents](https://www.ndss-symposium.org/ndss-paper/awakening-the-webs-sleeper-agents-misusing-service-workers-for-privacy-leakage/) | wrong year | The author-hosted full text was public on 29 November 2020; its NDSS 2021 appearance does not move first publication. |
| [Can I Take Your Subdomain?](https://arxiv.org/abs/2012.01946) | wrong year | The primary preprint was public on 3 December 2020. |
| [Shadow Attacks](https://pdf-insecurity.org/signature-shadow/evaluation_2020.html) | wrong year | The researchers publicly described the attack on 21 July 2020 before NDSS 2021. |
| [Cross-Origin State Inference Attacks](https://arxiv.org/abs/1908.02204) | wrong year | The primary preprint was public on 6 August 2019. |
| Reining in the Web's Inconsistencies with Site Policy | wrong year | The author upload was public on 22 September 2020. |
| Do (Not) Follow the White Rabbit | later year | A broad search surfaced later work rather than a 2021 first publication. |
| Are Your Sites Truly Isolated? | later year | This Site Isolation implementation-testing paper is a later publication, not a 2021 lead. |
| Continuous User Behavior Monitoring using DNS Cache Timing Attacks | later year | The search result belongs to a later NDSS program. |
| insecure:// URI schemes in Android | later year | The broad mechanism sweep surfaced later-year Android work. |
| Favocado: Fuzzing the Binding Code of JavaScript Engines | scope-adjacent | Finds native engine binding bugs; it does not supply a distinct reusable web-hacking primitive. |
| Who's Hosting the Block Party? | measurement / defensive | Measures tracking prevention behavior and breakage rather than introducing an offensive mechanism. |
| Catching Transparent Phish | measurement / defensive | Detects and characterizes reverse-proxy phishing kits; it does not add a separate attack technique. |
| Out of Sight, Out of Mind: Detecting Orphaned Web Pages | defensive | Discovers forgotten pages but does not define a new offensive primitive. |
| Trojan Source | scope-adjacent | The source-code bidirectional-text attack can affect web languages but is not specifically a web-hacking technique. |
| SoK: On the Analysis of Web Browser Security | survey | Organizes prior browser-security work and defenses without a new offensive method. |

## Gate note

The fresh additions include one score of 69.4. This audit deliberately applies
the repository's current **60-or-above** historical gate, and the wording in
`2021.md` was corrected accordingly. This pass did not run the reference
archiver or refresh either web application.
