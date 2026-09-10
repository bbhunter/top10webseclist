# 2021 missed-technique audit

This folder records the bounded 2026-08-09 audit for web-security research first
published in 2021 but absent from the original 2021 nomination round. The
exclusion set contained 41 distinct URLs from [`2021.md`](../../2021.md) before
this pass. Exact URL filtering was followed by semantic comparison against that
file and backward mechanism checks through the 2006–2020 lists and local
reference text.

The historical-list gate is **55 or above plus a qualifying non-duplicate
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

## Threshold reconciliation — 2026-09-09

The current historical gate is **55 or above plus a qualifying non-duplicate
verdict**. All 13 full evaluations, including every score above the former
60-point gate, were compared with the original nominations, the missed section,
and the latest state of the immutable history. All 13 qualifying candidates are
already represented in the missed section; the lowest score is 69.4. No full
evaluations fall in the newly eligible 55–59.9 band, and history contains no
additional candidate absent from the readable cards.

This bounded reconciliation added no techniques and changed no numerical scores
or decisions. The 15 screened leads above remain screening outcomes, not full
evaluations; their original date, coverage and scope reasons were not rejudged in
this threshold-only pass. No fresh source verification was needed for an
addition, because there were no additions. The stale gate wording was corrected
in this index and the scorecards, and the changed card was appended to history.
Reference preservation and website refresh remain separate work.

## Independent repeat sweep — 2026-09-10

[Detailed coverage, every lead, primary evidence and draft scores](2026-09-10-sweep.md): 12 lead groups, comprising 2 survivors for main-reviewer judgement, 2 held prescreens and 8 screened groups. Read the 53-URL exclusion set and triaged research-bearing citations from an inventory of 1,848 outbound occurrences. New survivor URLs both passed the exclusion helper.

- [Talking About My Generation](https://www.ias.cs.tu-bs.de/publications/talking_about_my_generation.pdf) — draft **70.3**, tooling/methodology; precise in-place URL/sink span mapping improves DOM XSS exploit generation. Full source and closest 2013/2018 methods read; note legacy-encoding validation browser and only 846 cases exclusive to the new method.
- [Towards a Lightweight, Hybrid Approach for Detecting DOM XSS Vulnerabilities with Machine Learning](https://clementfung.me/gallery/papers/www2021-domxss-ml.pdf) — draft **63.6**, tooling/methodology; full twelve-page source read. Classifier prefilter contribution, with projected rather than deployed end-to-end speedups; prior comparison needs final reviewer verification.

These are evidence handoffs, not final scorecards or authorized additions. The detailed ledger retains all screened and held leads, including older Go XML disclosure, Exchange companion chains, alternate Japanese artifacts and incompletely verified Chinese CSRF/Alexa research. No final judgements, history or curated list changed in this delegated sweep.

## Final all-years adjudication — 2026-09-10

This concludes the discovery handoff above. 2 new full judgements completed; 2 qualifying techniques added. The current addition gate is **55 plus a qualifying novelty verdict**. The [dated lead ledger](2026-09-10-sweep.md) retains the screened and held sources; the [all-years report](../2026-09-10-all-years.md) records coverage and archive outcomes.

| Research | Final score | Final verdict / disposition |
|---|---:|---|
| [Talking About My Generation: Targeted DOM-based XSS Exploit Generation using Dynamic Data Flow Analysis](https://www.ias.cs.tu-bs.de/publications/talking_about_my_generation.pdf) | 70.3 | Tooling or methodology contribution; added — [full card](judgements.md) |
| [Towards a Lightweight, Hybrid Approach for Detecting DOM XSS Vulnerabilities with Machine Learning](https://clementfung.me/gallery/papers/www2021-domxss-ml.pdf) | 63.6 | Tooling or methodology contribution; added — [full card](judgements.md) |

Late date handoff: [The State of the SameSite](https://publications.cispa.saarland/3504/) records an accepted-version deposit on 13 October 2021 at 11:32 despite 2022 S&P proceedings. It remains a 2021 evidence hold for full method/prior-art judgement, not a 2022 addition and not a completed rejection.

These final cards and additions supersede provisional scores and advance/hold states for the named survivors only. Other credible leads remain prescreens, with no invented numerical scores or completed rejection verdicts.
