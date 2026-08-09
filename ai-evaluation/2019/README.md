# 2019 missed-technique audit

This folder records the fresh 2026-08-09 audit for web-security research first
published in 2019 but absent from the original 2019 nomination round. The
exclusion set contained 54 distinct URLs from [`2019.md`](../../2019.md). Exact
URL filtering was followed by semantic comparison against every mechanism in
that file and backward checks through the 2006–2018 lists.

The historical-list gate is **60 or above plus a qualifying non-duplicate
verdict**. A score alone cannot rescue prior disclosure, an original nominee
under another URL, or work first published in a different year. All credible
screened leads are retained below, including leads excluded on date or scope.

## Coverage

- Primary programs and papers from IEEE S&P, ACM CCS, NDSS/MADWeb and USENIX
  Security, including related-work and first-publication checks.
- PortSwigger Research's 2019 archive and primary author, project and tool
  pages for browser, HTTP and testing-methodology work.
- Cross-origin state, browser and extension fingerprinting, WebView context,
  autocomplete traffic analysis, click interception, CSP and cache behaviour.
- Phishing-evasion measurement, search poisoning, TLS oracle scanning, cloud
  backend discovery, JavaScript fuzzing and targeted exploit preparation.
- Backward mechanism searches through the local 2006–2018 lists and archive;
  renamed variants of the 54 known 2019 references were excluded semantically.
- A non-US sweep through European and international authors represented in the
  major programs and MADWeb. No additional non-English primary source cleared
  the date, scope, novelty and evidence gates.

No archive capture was opened, validated or changed during this audit.

## Results

- 30 credible leads retained.
- 16 candidates received full scorecards and were added to the missed section.
- 14 additional leads were resolved during screening as prior-year disclosure,
  scope mismatch, defensive/measurement-only work or same-mechanism overlap.
- No qualifying 2019 candidate landed in the 60–69.9 band; the lower gate was
  nevertheless applied to every retained lead.

| Score | Decision | Verdict | Candidate |
|---:|---|---|---|
| 89.2 | added | Tooling or methodology contribution | [Turbo Intruder](https://portswigger.net/research/turbo-intruder-embracing-the-billion-request-attack) |
| 88.9 | added | Tooling or methodology contribution | [Cross-Origin State Inference attacks](https://arxiv.org/abs/1908.02204) |
| 87.3 | added | Original technique | [Differential Context Vulnerabilities in mobile WebViews](https://www.usenix.org/conference/usenixsecurity19/presentation/yang-guangliang) |
| 86.5 | added | Meaningful combination or adaptation | [Leaky Images](https://www.usenix.org/conference/usenixsecurity19/presentation/staicu) |
| 83.8 | added | Meaningful extension | [CSP policy injection](https://portswigger.net/research/bypassing-csp-with-policy-injection) |
| 83.5 | added | Tooling or methodology contribution | [JavaScript Template Attacks](https://www.ndss-symposium.org/wp-content/uploads/2019/02/ndss2019_01B-4_Schwarz_paper.pdf) |
| 83.2 | added | Meaningful combination or adaptation | [Remote keylogging through search autocomplete](https://www.usenix.org/conference/usenixsecurity19/presentation/monaco) |
| 82.6 | added | Meaningful combination or adaptation | [Cross-Site Challenge-Response Attacks](https://madweb.work/papers/2019/paper4.pdf) |
| 81.5 | added | Tooling or methodology contribution | [PhishFarm](https://doi.org/10.1109/SP.2019.00049) |
| 80.7 | added | Tooling or methodology contribution | [Click interception on the web](https://www.usenix.org/conference/usenixsecurity19/presentation/zhang) |
| 79.9 | added | Meaningful extension | [Latex Gloves](https://www.ndss-symposium.org/wp-content/uploads/2019/02/ndss2019_01B-5_Sjosten_paper.pdf) |
| 79.9 | added | Tooling or methodology contribution | [Scalable TLS padding-oracle scanning](https://www.usenix.org/conference/usenixsecurity19/presentation/merget) |
| 79.2 | added | Tooling or methodology contribution | [Postcards from the Post-HTTP World](https://ieeexplore.ieee.org/document/8835223) |
| 79.1 | added | Tooling or methodology contribution | [The Betrayal at Cloud City](https://www.usenix.org/conference/usenixsecurity19/presentation/alrawi) |
| 74.6 | added | Tooling or methodology contribution | [Behavioural browser fuzzing](https://portswigger.net/research/provoking-browser-quirks-with-behavioural-fuzzing) |
| 72.0 | added | Meaningful extension | [Search poisoning of linguistic collisions](https://doi.org/10.1109/SP.2019.00025) |

## Screened leads

| Candidate | Outcome | Screening evidence |
|---|---|---|
| [Don't Trust The Locals](https://www.ndss-symposium.org/ndss-paper/dont-trust-the-locals-investigating-the-prevalence-of-persistent-client-side-cross-site-scripting-in-the-wild/) | wrong year | The CISPA record was public on 9 November 2018 and the work was presented at German OWASP Day 2018. |
| [Master of Web Puppets](https://arxiv.org/abs/1810.00464) | wrong year | The primary preprint was public on 30 September 2018. |
| [Robust Website Fingerprinting Through the Cache Occupancy Channel](https://arxiv.org/abs/1811.07153) | wrong year | The primary preprint was public on 17 November 2018. |
| CodeAlchemist | wrong year | The public project repository was created in November 2018; the 2019 venue does not reset first disclosure. |
| The 9 Lives of Bleichenbacher's CAT | wrong year | The cache-oracle result and prepublication reporting were public in December 2018. |
| Unveiling Your Keystrokes | scope mismatch | Its spy is a co-resident native process probing shared graphics libraries, not a browser-delivered or web-adjacent technique. |
| Responsible denial of service with web cache poisoning | already represented | The 2019 nominations already contain CPDoS and cache-poisoning work with the same persistent cached-error outcome. |
| Abusing jQuery for CSS-powered timing attacks | prior art / same mechanism | The post explicitly extends the CSS timing technique already retained in the 2018 list; the new library targets do not create a distinct primitive. |
| Portal and focus/window-name XS-Leaks | already represented | These are constituent 2019 cross-site leak oracles; the original list already includes the broader Cross-Site Leaks entry. |
| HideNoSeek | scope mismatch | Obfuscating malicious JavaScript is an evasion study, not a distinct web exploitation primitive. |
| DorkPot | measurement system | The search-engine honeypot measures malicious search traffic rather than introducing an offensive technique. |
| Page Cache Attacks | scope mismatch | The demonstrated attacker is a local native process and the contribution is an operating-system memory side channel. |
| A Large-Scale Study on Risks of HTML5 WebAPI for Mobile Sensor-Based Attacks | measurement of known mechanisms | It systematises browser-sensor exposure and known sensor attacks without a distinct new offensive primitive. |
| Small World with High Risks / Anything to Hide? | measurement studies | The npm-ecosystem and minified-code studies quantify risk but do not add a reusable attack mechanism. |

## Notes on the gate

The 2019 pass produced no 60–69.9 recovery. The closest qualifying result was
the 72.0 linguistic-collision search-poisoning extension; narrower target-only
adaptations were screened instead of inflating originality to force inclusion.
This audit did not run the reference archiver or refresh either web application.
