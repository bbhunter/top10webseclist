# 2015 missed-technique audit

Audit run 2026-08-08 with the `webseclist-find-missed` and
`webseclist-judge-reference` workflows. The inclusion gate was a score of 60 or
above, a qualifying non-duplicate verdict, first public publication in 2015,
and absence from the original 2015 nomination set.

The audit began with 56 distinct URLs already present in [`2015.md`](../../2015.md)
and one existing missed entry. Exact-link exclusion was followed by semantic
comparison against the Top 10, other nominations and earlier year lists. The
existing Clock entry was reassessed instead of duplicated.

## Coverage

- NDSS, IEEE S&P, USENIX Security and WOOT, ACM CCS, AsiaCCS, ACSAC,
  ESORICS, RAID, IFIP SEC and the principal browser/web-security papers.
- Black Hat USA, Europe and Asia, DEF CON, OWASP/AppSec, 31C3-era material,
  researcher posts, proof-of-concept repositories and contemporary advisories.
- Browser timing, cache and microarchitectural channels; AppCache, WebRTC and
  JavaScript execution; JIT and code-reuse exploitation; HTTPS cache integrity;
  TLS state machines, RC4 and certificate handling; JWT and cloud/API trust;
  cross-site requests, search and evidence planting; cloud-origin discovery,
  browser DDoS, XML Encryption and dynamic web-application testing.
- Backward mechanism searches through the 2006–2014 lists, candidate
  bibliographies and standards records. This separated new work from earlier
  cache timing, cookie forcing, JIT spraying, browser DDoS, HSTS storage,
  certificate-validation, RPO, Website fingerprinting and WebView research.
- A non-US sweep through European and Asian venues, Ruhr, KU Leuven, TU Graz,
  CISPA, Bar-Ilan, Peking/Indiana collaborations and surviving researcher sites.
  Primary sources from Belgium, China, Germany, Israel, the Netherlands and
  Austria are represented in the kept set.

Older event sites and personal domains are uneven, so official proceedings and
author-hosted papers were paired when possible. No archived capture was opened
or found faulty, and this iteration did not run the archive or web-app refresh.

## Outcome

- 43 credible leads are retained in this report.
- 29 candidates received full scorecards: the existing Clock entry was
  reassessed and 28 new references were added to `2015.md`.
- 14 additional leads were resolved during screening as original nominations,
  pre-2015 disclosures, same-mechanism companions, defensive/measurement work
  or scope mismatches.
- 4 additions score in the 60–69 band and would have been lost under the former
  above-70 wording.

## Judged lead index

| Score | Decision | Verdict | Candidate |
|---:|---|---|---|
| 89.7 | added | Original technique | [Critical Vulnerabilities in JSON Web Token Libraries](https://www.chosenplaintext.ca/2015/03/31/jwt-algorithm-confusion.html) |
| 89.3 | added | Tooling or methodology contribution | [A Messy State of the Union](https://www.ieee-security.org/TC/SP2015/papers-archived/6949a535.pdf) |
| 88.6 | added | Original technique | [The Spy in the Sandbox](https://arxiv.org/abs/1502.07373) |
| 88.0 | added | Original technique | [Rowhammer.js](https://arxiv.org/abs/1507.06955) |
| 87.5 | added | Tooling or methodology contribution | [Protocol State Fuzzing of TLS Implementations](https://www.usenix.org/conference/usenixsecurity15/technical-sessions/presentation/de-ruiter) |
| 87.2 | added | Original technique | [Identifying Cross-origin Resource Status Using Application Cache](https://www.ndss-symposium.org/ndss2015/ndss-2015-programme/identifying-cross-origin-resource-status-using-application-cache/) |
| 86.6 | added | Meaningful extension | [Cookies Lack Integrity](https://www.usenix.org/conference/usenixsecurity15/technical-sessions/presentation/zheng) |
| 85.9 | added | Original technique | [Second Order Denial-of-Service](https://dl.acm.org/doi/10.1145/2810103.2813680) |
| 85.2 | added | Meaningful combination or adaptation | [Maneuvering Around Clouds](https://dl.acm.org/doi/10.1145/2810103.2813633) |
| 84.8 | added | Original technique | [On Subnormal Floating Point and Abnormal Timing](https://www.ieee-security.org/TC/SP2015/papers-archived/6949a623.pdf) |
| 84.5 | added | Meaningful extension | [All Your Biases Belong to Us](https://www.usenix.org/conference/usenixsecurity15/technical-sessions/presentation/vanhoef) |
| 84.2 | added | Original technique | [Counterfeit Object-oriented Programming](https://www.ieee-security.org/TC/SP2015/papers-archived/6949a745.pdf) |
| 83.8 | added | Tooling or methodology contribution | [Perplexed Messengers from the Cloud](https://dl.acm.org/doi/10.1145/2810103.2813652) |
| 82.7 | added | Tooling or methodology contribution | [jÄk](https://publications.cispa.saarland/538/) |
| 82.3 | added | Meaningful combination or adaptation | [Cross-Site Search Attacks](https://dl.acm.org/doi/10.1145/2810103.2813688) |
| 82.3 | added | Original technique | [Practical Memory Deduplication Attacks](https://gruss.cc/files/dedup.pdf) |
| 82.2 | added | Meaningful extension | [The Devil is in the Constants](https://www.ndss-symposium.org/wp-content/uploads/2017/09/09_1_2.pdf) |
| 81.9 | retained | Original technique | [The Clock is Still Ticking](https://dl.acm.org/doi/10.1145/2810103.2813632) |
| 81.8 | added | Tooling or methodology contribution | [SSLINT](https://www.ieee-security.org/TC/SP2015/papers-archived/6949a519.pdf) |
| 80.9 | added | Original technique | [Exploiting and Protecting Dynamic Code Generation](https://www.ndss-symposium.org/ndss2015/ndss-2015-programme/exploiting-and-protecting-dynamic-code-generation/) |
| 80.7 | added | Tooling or methodology contribution | [How to Break XML Encryption – Automatically](https://www.usenix.org/conference/woot15/workshop-program/presentation/kupser) |
| 79.3 | added | Original technique | [Cross-Site Framing Attacks](https://dl.acm.org/doi/10.1145/2818000.2818029) |
| 77.7 | added | Meaningful combination or adaptation | [WebRTC IP Address Leaks](https://diafygi.github.io/webrtc-ips/) |
| 77.0 | added | Meaningful extension | [Man-in-the-Browser-Cache](https://doi.org/10.1016/j.cose.2015.07.004) |
| 75.9 | added | Meaningful extension | [Too LeJIT to Quit](https://www.ndss-symposium.org/wp-content/uploads/2017/09/09_3_2.pdf) |
| 68.3 | added | Meaningful extension | [Cache Timing Attacks Revisited](https://doi.org/10.1007/978-3-319-18467-8_7) |
| 65.6 | added | Tooling or methodology contribution | [Automatically Detecting SSL Error-Handling Vulnerabilities](https://lilicoding.github.io/SA3Repo/papers/2015_zuo2015automatically.pdf) |
| 63.8 | added | Meaningful combination or adaptation | [Cashing Out the Great Cannon?](https://www.usenix.org/conference/woot15/workshop-program/presentation/pellegrino) |
| 60.3 | added | Meaningful combination or adaptation | [HTTPS Bicycle Attack](https://guidovranken.files.wordpress.com/2015/12/https-bicycle-attack.pdf) |

Full evidence, prior-art comparisons and weighted category scores are in
[`judgements.md`](judgements.md).

## Screened leads

| Candidate | Outcome | Screening evidence |
|---|---|---|
| [Relative Path Overwrite](http://www.thespanner.co.uk/2014/03/21/rpo/) | already represented / year gate | The 2014 disclosure is already an original 2015 nominee and is first-publication-year material for 2014. |
| [The Unexpected Dangers of Dynamic JavaScript](https://www.usenix.org/system/files/conference/usenixsecurity15/sec15-paper-lekies.pdf) | already represented | The original nomination list links the same USENIX paper. |
| From Facepalm to Brain Bender | overlap / measurement | Large-scale client-side XSS replay and classification overlaps the year's nominated DOM Flow and automated-XSS-analysis work without a separable attack primitive. |
| Attacks Only Get Better: Password Recovery Attacks Against RC4 in TLS | same-mechanism companion | A narrower same-year RC4 recovery result; the more general new-bias paper scored here covers TLS cookie recovery and WPA-TKIP. |
| [Network-Based Origin Confusion Attacks against HTTPS Virtual Hosting](https://doi.org/10.1145/2736277.2741083) | year gate | This is the WWW 2015 publication of the Virtual Host Confusion mechanism first publicly disclosed and already audited under 2014. |
| BrowserID primary-IdP attacks | year gate | The primary paper was publicly posted as arXiv:1411.7210 in November 2014 despite its 2015 conference appearance. |
| HSTS supercookies | prior art | RFC 6797 section 16.9 explicitly described encoding a tracking identifier across HSTS-enabled subdomains in 2012. |
| Client-side template injection in AngularJS | year gate | The reusable public PortSwigger article was published in January 2016; private 2015 reporting does not move it into this year. |
| k-fingerprinting | same-family extension | A stronger website-fingerprinting classifier, but the archive already represents the transferable website-fingerprinting attack and open-world advance in 2014. |
| Stickler | defensive-only | Client-side integrity verification for untrusted CDN delivery; no new offensive technique. |
| Cache-based side-channel detector for browsers | defensive-only | Detection of established cache probing rather than a new attack or offensive testing method. |
| Model Inversion Attacks that Exploit Confidence Information | scope mismatch | Foundational ML privacy work, but its contribution is model/API inference rather than a specifically web, HTTP or browser technique. |
| Cross-App Resource Access | scope mismatch | A mobile operating-system resource isolation attack without a distinct web-origin, HTTP or browser mechanism. |
| The Risks of WebGL | publication gate | The substantive paper surfaced after 2015; no qualifying 2015 primary disclosure was found during this sweep. |

## Gate notes

The four additions recovered only because the threshold is now 60 or above are
Cache Timing Attacks Revisited (68.3), hybrid-WebView SSL error handling (65.6),
Cashing Out the Great Cannon (63.8), and HTTPS Bicycle Attack (60.3). Their
lower originality scores explicitly account for earlier cache timing,
certificate-validation, browser-DDoS and encrypted-length leakage. They cross
the gate only because their robust probing, large-scale hybrid analysis,
browser-bot economics and password-length workflow are qualifying extensions,
methodologies or adaptations.
