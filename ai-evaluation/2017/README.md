# 2017 missed-technique audit

This folder records the bounded 2026-08-09 audit for web-security research first
published in calendar year 2017 but absent from the original combined 2016/2017
nomination round. The exclusion set contained 71 distinct URLs from
[`2016-17.md`](../../2016-17.md); the audit additionally compared mechanisms so
renamed copies and companion artifacts were not treated as new candidates.

The historical-list gate is **60 or above plus a qualifying non-duplicate
verdict**. Venue year was not accepted as publication year when a complete
preprint was already public in 2016.

## Coverage

- The complete Web-security sessions and relevant attack, privacy, browser,
  TLS, API and tooling papers at NDSS, USENIX Security, IEEE S&P and ACM CCS.
- Black Hat USA, Asia and Europe Web, HTTP, browser, TLS and cloud-service
  research, plus PortSwigger's 2017 research and nomination/result pages.
- Browser isolation and side channels, JavaScript bindings, extensions,
  fingerprinting, mobile sensors, HSTS/HPKP, cross-origin policy and WebViews.
- TLS hostname validation and Bleichenbacher oracles, semantic differential
  testing, CSRF and authorization discovery, HTTP/2, PDF/parser differentials,
  low-volume application DoS, recommender manipulation and shared SaaS indexes.
- DNS lifecycle and nameserver takeover, cross-site printing, cloud-mediated
  exfiltration, encrypted-video recognition and Web-connected mobile flows.
- Backward mechanism searches through the local 2006–2016 reference archive,
  with special checks for browser timing, extension enumeration, expired-domain
  trust, certificate-validation testing, cross-site printing and fingerprinting.
- A cross-year correction checked longitudinal browser-fingerprint linkage and
  deep-learning classification of Tor traffic against the same scope, novelty
  and first-public-date gates.
- Practitioner, bounty and non-US conference beats were checked. The strongest
  surviving sources were European academic and Black Hat work; no additional
  non-English original source cleared the gate in the bounded sweep.

The sweep used first-public dates. It did not run the reference archiver, change
archive captures, or refresh either Web application.

## Results

- 41 credible leads retained in this ledger.
- 27 candidates received full scorecards and passed the numeric, verdict and
  Web-bearing scope gates.
- 14 leads were resolved during screening as wrong-year, already represented,
  defensive or measurement-only, target-specific, scope-mismatched, or a weaker
  companion to a fully judged methodology.
- One qualifying addition, *Game of Registrars*, is in the recovered 60–69 band.

| Score | Verdict | Candidate |
|---:|---|---|
| 88.4 | Original technique | [The Wolf of Name Street](https://acmccs.github.io/papers/p957-vissersA.pdf) |
| 87.8 | Original technique | [ASLR on the Line](https://www.ndss-symposium.org/ndss2017/ndss-2017-programme/aslrcache-practical-cache-attacks-mmu/) |
| 87.6 | Original technique | [Loophole](https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/vila) |
| 86.9 | Tooling or methodology contribution | [Finding and Preventing Bugs in JavaScript Bindings](https://mlfbrown.com/malicious.pdf) |
| 86.8 | Original technique | [Rewriting History](https://acmccs.github.io/papers/p1741-lernerAT3.pdf) |
| 86.3 | Meaningful extension | [Fantastic Timers and Where to Find Them](https://misc0110.net/files/timers.pdf) |
| 86.2 | Tooling or methodology contribution | [NEZHA](https://www.ieee-security.org/TC/SP2017/papers/390.pdf) |
| 86.1 | Tooling or methodology contribution | [AUTHSCOPE](https://acmccs.github.io/papers/p799-zuoA.pdf) |
| 85.4 | Original technique | [Side-Channel Attacks on Shared Search Indexes](https://www.ieee-security.org/TC/SP2017/papers/449.pdf) |
| 85.1 | Tooling or methodology contribution | [HVLearn](http://www.cs.columbia.edu/~suman/docs/hvlearn.pdf) |
| 83.8 | Meaningful extension | [(Cross-)Browser Fingerprinting](https://www.ndss-symposium.org/ndss2017/ndss-2017-programme/cross-browser-fingerprinting-os-and-hardware-level-features/) |
| 83.7 | Original technique | [Unleashing the Walking Dead](https://acmccs.github.io/papers/p829-liA.pdf) |
| 83.6 | Tooling or methodology contribution | [Deemon](https://acmccs.github.io/papers/p1757-pellegrinoA.pdf) |
| 82.8 | Original technique | [Tail Attacks on Web Applications](https://acmccs.github.io/papers/p1725-shanAemb.pdf) |
| 82.3 | Meaningful extension | [Extension Breakdown](https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/sanchez-rola) |
| 81.1 | Tooling or methodology contribution | [Automated Website Fingerprinting through Deep Learning](https://arxiv.org/abs/1708.06376) |
| 80.7 | Tooling or methodology contribution | [Same-Origin Policy: Evaluation in Modern Browsers](https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/schwenk) |
| 80.3 | Original technique | [PDF Mirage](https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/markwood) |
| 80.1 | Meaningful extension | [FP-STALKER](https://hal.inria.fr/hal-01652021) |
| 79.5 | Original technique | [Fake Co-visitation Injection Attacks](https://www.ndss-symposium.org/ndss2017/ndss-2017-programme/fake-co-visitation-injection-attacks-recommender-systems/) |
| 78.2 | Meaningful extension | [Beauty and the Burst](https://beautyburst.github.io/) |
| 74.1 | Tooling or methodology contribution | [SoK: Exploiting Network Printers](https://www.ieee-security.org/TC/SP2017/program-papers.html#sok-exploiting-network-printers) |
| 74.1 | Meaningful extension | [ROBOT](https://robotattack.org/) |
| 73.2 | Original technique | [The Adventures of AV and the Leaky Sandbox](https://blackhat.com/us-17/briefings.html#the-adventures-of-av-and-the-leaky-sandbox) |
| 72.1 | Meaningful extension | [Stealing PINs via Mobile Sensors](https://pure.york.ac.uk/portal/en/publications/stealing-pins-via-mobile-sensors-actual-risk-versus-user-percepti/) |
| 70.1 | Meaningful extension | [Breaking Out HSTS and HPKP](https://blackhat.com/archive/europe/2017/briefings.html#breaking-out-hsts) |
| 68.3 | Meaningful extension | [Game of Registrars](https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/lauinger) |

## Cross-year correction

*FP-STALKER* was publicly deposited on 2 December 2017, before its IEEE S&P
2018 appearance. Its rule-based and hybrid linkage of changing browser
fingerprints is a direct browser-side tracking method and clears the 2017 list
gate at 80.1.

*Automated Website Fingerprinting through Deep Learning* was publicly submitted
on 21 August 2017 and earns 81.1 for its automated feature-learning methodology.
Although its observation point is the network path between a Tor client and its
entry guard, its target and output are Web-specific: it infers which website the
user visited. That credible Web bearing, and the same audit's treatment of 2016
*Website Fingerprinting at Internet Scale*, place it inside the repository's
scope rather than among network-only findings with no Web bearing.

## Screened leads

| Candidate | Outcome | Screening evidence |
|---|---|---|
| [Membership Inference Attacks against Machine Learning Models](https://arxiv.org/abs/1610.05820) | wrong year | The complete public preprint was submitted 18 October 2016; its IEEE S&P 2017 appearance does not move first publication into 2017. |
| Code-reuse Attacks for the Web / Script Gadgets | already represented | The combined file already includes the talk and whitepaper under “Don't Trust the DOM.” |
| Hacking HTTP/2 — New Attacks on the Internet's Next Generation Foundation | wrong-year mechanisms | The presentation's named zero-days are CVE-2016-1544 and CVE-2016-1546; the 2017 talk is a useful synthesis, not first publication of those attacks. |
| OSS-Fuzz | wrong year / scope | The service launched in December 2016 and is general continuous fuzzing rather than a 2017 Web technique. |
| CCSP: Controlled Relaxation of Content Security Policies | defensive architecture | Proposes a CSP policy-composition defense and no offensive testing primitive. |
| Deterministic Browser / DeterFox | defensive architecture | Removes timing nondeterminism to resist side channels; Loophole and Fantastic Timers supply the offensive contributions. |
| Enabling Reconstruction of Attacks via Efficient Browsing Snapshots | defensive forensics | ChromePic reconstructs attacks after the event rather than introducing an attack or testing technique. |
| Thou Shalt Not Depend on Me | measurement study | Quantifies outdated JavaScript-library use but does not add an offensive primitive. |
| Hindsight: Evolution of UI Vulnerabilities in Mobile Browsers | measurement study | A useful historical analysis of known UI weaknesses, without a distinct transferable attack. |
| Game of Chromes: Zombie Chrome Extensions | useful application | Chains known extension XSS, store distribution and social propagation; Extension Breakdown provides the stronger new extension-enumeration mechanism. |
| SymCerts | same-beat companion | Symbolic X.509 validation testing is valuable, but HVLearn and NEZHA cover the distinct black-box and domain-independent advances selected in this bounded audit. |
| Skyfire | scope / stronger companion | Strong general seed-generation work whose Web-adjacent evaluations are browser and XML fuzzing; NEZHA is the more transferable semantic-differential contribution. |
| From Trash to Treasure: Timing-Sensitive Garbage Collection | borderline scope | Establishes a garbage-collector channel, including a datacenter network observation, but not a sufficiently direct Web/API attack in this bounded pass. |
| SHAttered | scope mismatch | A landmark SHA-1 collision demonstration, but the underlying contribution is general cryptanalysis rather than a Web-hacking technique. |

## Gate note

*Game of Registrars* is intentionally retained below 70. Expired-domain abuse
and residual trust predate 2017, including the 2016 Domain-Z work, but the
registrar/drop-catch ecosystem measurement materially extends how attackers can
reason about the timing and availability of post-expiration takeovers.
