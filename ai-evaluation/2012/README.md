# 2012 missed-technique audit

This folder records the fresh 2026-08-08 audit for web-security research first
published in 2012 but absent from the original 2012 nomination round. The
exclusion set contained 75 distinct URLs from [`2012.md`](../../2012.md). URL
filtering was followed by a semantic comparison against every mechanism already
represented there.

The historical-list gate for this audit is **60 or above plus a qualifying
non-duplicate verdict**. A score alone cannot rescue a prior disclosure, an
original nominee under another URL, or work published in the wrong year. Every
credible lead is retained below, including those resolved during screening.

## Coverage

- IEEE S&P, ACM CCS and AsiaCCS, NDSS, USENIX Security, WOOT, NSDI, PETS,
  ACSAC, W2SP, WebApps and the principal web-security workshop programs.
- Black Hat USA and Abu Dhabi archives, DEF CON-era practitioner material,
  OWASP/AppSec sources, author publication pages and surviving primary papers.
- SSO and federated identity, XML signatures, browser rendering and parser
  fingerprinting, state-aware scanning, language fuzzing, WAF side channels,
  TLS API misuse, third-party JavaScript, tracking, traffic analysis, mobile
  TLS, browser information-flow controls and client-side encrypted storage.
- Backward mechanism searches through the 2006–2011 lists and candidate
  bibliographies to distinguish new mechanisms from earlier disclosures.
- A non-US sweep through European and Asian venues and researcher collections.
  The strongest surviving non-US work includes SAML wrapping, scriptless data
  theft, Flash analysis, Android TLS analysis and WAF rule fingerprinting.

Old workshop sites and personal publication pages are unevenly available. The
audit therefore paired official programs with author-hosted papers wherever
possible. No archived reference was changed or recaptured during this pass.

## Results

- 36 credible leads retained.
- 20 candidates received full scorecards and meet the numeric and verdict gate:
  the existing Scriptless Attacks entry was reassessed and 19 references were
  added.
- 16 additional leads were resolved during screening as original nominations,
  pre-2012 disclosures, defensive-only work, known-technique applications or
  scope mismatches.
- 2 newly added references score in the 60–69 band and would have been lost
  under the previous 70-point gate.

| Score | Decision | Verdict | Candidate |
|---:|---|---|---|
| 86.2 | added | Tooling or methodology contribution | [Signing Me onto Your Accounts](https://www.ieee-security.org/TC/SP2012/papers/4681a365.pdf) |
| 86.0 | added | Tooling or methodology contribution | [Fuzzing with Code Fragments](https://www.usenix.org/conference/usenixsecurity12/technical-sessions/presentation/holler) |
| 85.9 | added | Original technique | [Pixel Perfect](https://hovav.net/ucsd/papers/ms12.html) |
| 85.2 | added | Meaningful extension | [On Breaking SAML](https://www.usenix.org/conference/usenixsecurity12/technical-sessions/presentation/somorovsky) |
| 85.1 | added | Tooling or methodology contribution | [Enemy of the State](https://www.usenix.org/conference/usenixsecurity12/technical-sessions/presentation/doupe) |
| 84.9 | added | Tooling or methodology contribution | [The Most Dangerous Code in the World](https://www.cs.utexas.edu/~shmat/shmat_ccs12.pdf) |
| 84.4 | added | Original technique | [Self-Exfiltration](https://www.ieee-security.org/TC/W2SP/2012/papers/w2sp12-final11.pdf) |
| 83.9 | added | Meaningful combination or adaptation | [Off-Path Attacking the Web](https://www.usenix.org/conference/woot12/workshop-program/presentation/gilad) |
| 83.6 | added | Tooling or methodology contribution | [Detecting and Defending Against Third-Party Tracking](https://www.usenix.org/conference/nsdi12/technical-sessions/presentation/roesner) |
| 80.6 | added | Tooling or methodology contribution | [You Are What You Include](https://www.securitee.org/files/jsinclusions_ccs2012.pdf) |
| 80.3 | already present; retained | Original technique | [Scriptless Attacks](https://www.nds.rub.de/media/emma/veroeffentlichungen/2012/08/16/scriptlessAttacks-ccs2012.pdf) |
| 80.1 | added | Tooling or methodology contribution | [The Devil is in the (Implementation) Details](https://css.csail.mit.edu/6.858/2012/readings/oauth-sso.pdf) |
| 79.3 | added | Original technique | [WAFFle](https://www.usenix.org/conference/woot12/workshop-program/presentation/schmitt) |
| 79.2 | added | Meaningful extension | [Touching from a Distance](https://www.freehaven.net/anonbib/cache/ccs2012-fingerprinting.pdf) |
| 77.5 | added | Tooling or methodology contribution | [FlashOver](https://www.securitee.org/files/flashover_asiaccs2012.pdf) |
| 76.8 | added | Tooling or methodology contribution | [Why Eve and Mallory Love Android](https://teamusec.de/publications/conf-ccs-fahlhmsbf12/) |
| 76.4 | added | Tooling or methodology contribution | [Host Fingerprinting and Tracking on the Web](https://www.ndss-symposium.org/ndss2012/ndss-2012-programme/host-fingerprinting-and-tracking-web-privacy-and-security-implications/) |
| 70.7 | added | Original technique | [XSS-FP](https://arxiv.org/abs/1211.4812) |
| 65.1 | added | Meaningful combination or adaptation | [Web-based Attacks on Host-Proof Encrypted Storage](https://www.usenix.org/conference/woot12/workshop-program/presentation/bhargavan) |
| 60.9 | added | Meaningful extension | [Cruel Intentions](https://www.ieee-security.org/TC/W2SP/2012/papers/w2sp12-final10.pdf) |

## Screened leads

| Candidate | Outcome | Screening evidence |
|---|---|---|
| [Chrome Extensions: Threat Analysis and Countermeasures](https://www.ndss-symposium.org/ndss2012/ndss-2012-programme/chrome-extensions-threat-analysis-and-countermeasures/) | already represented | The original list's “Chrome addon hacking” nomination and linked series already represent malicious-extension privileges and exploitation. |
| [Analyzing the Security of Chrome Extensions](https://www.usenix.org/conference/usenixsecurity12/technical-sessions/presentation/carlini) | already represented | Strong architecture evaluation, but semantically inside the original Chrome-addon mechanism cluster. |
| I Forgot Your Password: Randomness Attacks Against PHP Applications | already represented | The original “Bruteforce of PHPSESSID” nomination covers the same weak-PHP-randomness attack family. |
| Abusing Cloud Browsers for Fun and Profit | already represented | The original nominations explicitly include parasitic computing through cloud browsers. |
| Moving-object CAPTCHA recognition attack | already represented | The year already contains CAPTCHA re-riding, provider impersonation, Stiltwalker and general CAPTCHA-breaking nominations; the contribution is incremental within that cluster. |
| [Clickjacking: Attacks and Defenses](https://www.usenix.org/conference/usenixsecurity12/technical-sessions/presentation/huang) | already represented | The original list has multiple clickjacking, cursorjacking, CSS-only and UI-redressing nominations. Its systematic treatment is valuable but not missing as a technique family. |
| [On the Fragility and Limitations of Current Browser-Provided Clickjacking Protection Schemes](https://www.usenix.org/conference/woot12/workshop-program/presentation/luo) | already represented | Frame-busting and X-Frame-Options limitations fall inside the original year's dense clickjacking cluster. |
| [A Security Analysis of Emerging Web Standards](https://www.scitepress.org/papers/2012/40495/index.html) | prior disclosure | The authors' cited ENISA analysis disclosed the central standards findings in 2011; the 2012 paper is not the first public source. |
| Privilege Separation in HTML5 Applications | defensive architecture | A compartmentalisation design without a new attack primitive or offensive testing method. |
| FlowFox | defensive architecture | Browser information-flow enforcement; Self-Exfiltration was kept because it contributes the transferable attack that defeats this class of destination policy. |
| JSand | defensive architecture | A JavaScript isolation design rather than a distinct offensive mechanism. |
| Treehouse | defensive architecture | A browser-isolation architecture without a qualifying attack or testing contribution. |
| Origin-Bound Certificates | defensive protocol proposal | Authentication design work, not a new web attack or offensive discovery method. |
| EvilSeed and Rozzle | defensive-only | Both advance malicious-page discovery or detection but do not contribute a reusable offensive web-security technique. |
| [You Are What You Like!](https://www.ndss-symposium.org/ndss2012/ndss-2012-programme/you-are-what-you-information-leakage-through-users-interests/) | scope / known-method application | Important privacy evidence, but the marginal method applies established attribute inference to social-network interests rather than creating a distinct web-hacking mechanism. |
| Cross-protocol attacks on TLS | scope mismatch | The protocol-confusion result is technically strong but not sufficiently specific to HTTP, browsers or web applications for this historical list. |

## Notes on the gate

Cruel Intentions (60.9) and Web-based Attacks on Host-Proof Encrypted Storage
(65.1) are the two newly recovered 60–69.9 entries. Both qualify because they
make a defensible extension or combination claim, not merely because they cross
the numeric threshold. This audit did not run the reference archiver or refresh
either web application.

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

**One addition.** Scorecard in [judgements.md](judgements.md).

| Score | Verdict | List decision | Candidate |
|---:|---|---|---|
| 84.2 | Original technique | added | [Are You My Type? Breaking .NET Through Serialization](https://media.blackhat.com/bh-us-12/Briefings/Forshaw/BH_US_12_Forshaw_Are_You_My_Type_WP.pdf) |

James Forshaw's Black Hat USA 2012 talk is the first public exploitation of .NET
serialization and the origin of the gadget-hunting method that later produced
ViewState, SharePoint, Exchange and Telerik RCE. Its 2012 delivery vectors are
XBAP, Partial Trust sandboxes and .NET Remoting rather than an HTTP parameter, so
scope is borderline; the transferable core was scored and transferability was
held at 78 rather than raised. The repository already treats this class as in
scope, having nominated PHP unserialization in 2018, .NET Remoting over HTTP in
2019 and hardened .NET deserialization at number two in 2023.
