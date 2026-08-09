# 2014 missed-technique audit

This folder records the fresh 2026-08-08 audit for web-security research first
published in 2014 but absent from the original 2014 nomination round. The
exclusion set contained 52 distinct URLs from [`2014.md`](../../2014.md). Exact
URL filtering was followed by a semantic comparison with every mechanism
already represented in that file.

The historical-list gate is **60 or above plus a qualifying non-duplicate
verdict**. A score alone cannot rescue prior disclosure, an original nominee
under another URL, or work first published in a different year. Every credible
lead is retained below, including those resolved during screening.

## Coverage

- IEEE S&P, ACM CCS, NDSS, USENIX Security, WOOT and the principal 2014
  web-security papers, programs and author copies.
- Black Hat USA, Europe and Asia, DEF CON, OWASP AppSec and researcher-hosted
  posts, whitepapers, slides and tools.
- Browser origins and new HTML5 APIs, TLS/HTTPS composition, certificate
  validation, password managers, SSO, hybrid mobile/Web stacks, authorization,
  payment logic, second-order flows, string solving and black-box testing.
- Path interpretation, relative resource loading, HSTS, encrypted-traffic
  analysis, website fingerprinting, CDN delegation and GPU/browser leakage.
- Backward searches through the 2006–2013 lists and local reference archive,
  followed by bibliography and web checks for the closest prior mechanisms.
- A non-US sweep through European and Asian academic venues, Ruhr, EURECOM,
  NUS, Tsinghua, Black Hat Europe/Asia and surviving researcher sites. No
  additional non-English primary source cleared the originality gate.
- Bug-bounty and CTF-originated disclosures were checked separately. The
  strongest 2014 bounty mechanisms were already nominated; no additional
  platform report supplied a reusable, first-published technique above the
  gate.

Several old personal sites are intermittent or redirect today, so official
conference records and surviving author papers were used together. This audit
did not change or validate any archive capture.

## Results

- 35 credible leads retained.
- 20 candidates received full scorecards and meet the numeric and verdict gate:
  1 existing missed entry was reassessed and 19 references were added.
- 15 additional leads were resolved during screening as prior art,
  defensive/measurement-only work, a scope mismatch, a same-mechanism companion
  paper or a target-specific application without enough transferable novelty.
- 1 newly added reference is in the 60–69 band and would have been lost under
  the previous above-70 rule.

| Score | Decision | Verdict | Candidate |
|---:|---|---|---|
| 89.0 | added | Original technique | [Virtual Host Confusion](https://www.blackhat.com/docs/us-14/materials/us-14-Delignat-The-BEAST-Wins-Again-Why-TLS-Keeps-Failing-To-Protect-HTTP-wp.pdf) |
| 88.0 | added | Original technique | [Triple Handshakes and Cookie Cutters](https://www.ieee-security.org/TC/SP2014/papers/TripleHandshakesandCookieCutters_c_BreakingandFixingAuthenticationoverTLS.pdf) |
| 86.8 | added | Tooling or methodology contribution | [Using Frankencerts](https://www.ieee-security.org/TC/SP2014/papers/UsingFrankencertsforAutomatedAdversarialTestingofCertificateValidationinSSL_s_TLSImplementations.pdf) |
| 86.7 | added | Original technique | [Relative Path Overwrite](http://www.thespanner.co.uk/2014/03/21/rpo/) |
| 85.8 | added | Original technique | [Breaking and Fixing Origin-Based Access Control in Hybrid Web/Mobile Application Frameworks](https://www.ndss-symposium.org/ndss2014/ndss-2014-programme/breaking-and-fixing-origin-based-access-control-hybrid-webmobile-application-frameworks/) |
| 85.2 | added | Tooling or methodology contribution | [Static Detection of Second-Order Vulnerabilities](https://www.usenix.org/conference/usenixsecurity14/technical-sessions/presentation/dahse) |
| 85.1 | added | Original technique | [All Your Screens Are Belong to Us](https://www.ieee-security.org/TC/SP2014/papers/AllYourScreensareBelongtoUs_c_AttacksExploitingtheHTML5ScreenSharingAPI.pdf) |
| 81.7 | added | Meaningful extension | [Password Managers: Attacks and Defenses](https://www.usenix.org/conference/usenixsecurity14/technical-sessions/presentation/silver) |
| 80.9 | added | Tooling or methodology contribution | [An Expressive Model for the Web Infrastructure](https://www.ieee-security.org/TC/SP2014/papers/AnExpressiveModelfortheWebInfrastructure_c_DefinitionandApplicationtotheBrowserIDSSOSystem.pdf) |
| 79.6 | added | Tooling or methodology contribution | [S3](https://trinhmt.github.io/home/S3/ccs14-trinh.pdf) |
| 77.4 | added | Tooling or methodology contribution | [MACE](https://research.ibm.com/publications/mace-detecting-privilege-escalation-vulnerabilities-in-web-applications) |
| 76.7 | added | Meaningful extension | [New Bleichenbacher Side Channels and Attacks](https://www.usenix.org/conference/usenixsecurity14/technical-sessions/presentation/meyer) |
| 76.2 | added | Original technique | [A Web Traffic Analysis Attack Using Only Timing Information](https://arxiv.org/abs/1410.2087) |
| 75.9 | added | Tooling or methodology contribution | [Toward Black-Box Detection of Logic Flaws](https://www.ndss-symposium.org/ndss2014/ndss-2014-programme/toward-black-box-detection-logic-flaws-web-applications/) |
| 75.1 | added | Tooling or methodology contribution | [SSOScan](https://www.usenix.org/conference/usenixsecurity14/technical-sessions/presentation/zhou) |
| 73.0 | added | Tooling or methodology contribution | [Detecting Logic Vulnerabilities in E-Commerce Applications](https://www.ndss-symposium.org/ndss2014/ndss-2014-programme/detecting-logic-vulnerabilities-e-commerce-applications/) |
| 72.6 | already present; retained | Original technique | [Same Origin Method Execution](http://www.benhayak.com/2015/06/same-origin-method-execution-some.html) |
| 71.9 | added | Meaningful extension | [Effective Attacks and Provable Defenses for Website Fingerprinting](https://www.usenix.org/conference/usenixsecurity14/technical-sessions/presentation/wang_tao) |
| 71.0 | added | Meaningful combination or adaptation | [The Emperor's New Password Manager](https://www.usenix.org/conference/usenixsecurity14/technical-sessions/presentation/li_zhiwei) |
| 65.4 | added | Meaningful extension | [Bypassing HTTP Strict Transport Security](https://blackhat.com/docs/eu-14/materials/eu-14-Selvi-Bypassing-HTTP-Strict-Transport-Security-wp.pdf) |

## Screened leads

| Candidate | Outcome | Screening evidence |
|---|---|---|
| [When HTTPS Meets CDN](https://www.ieee-security.org/TC/SP2014/papers/WhenHTTPSMeetsCDN_c_ACaseofAuthenticationinDelegatedService.pdf) | measurement / defensive design | Important evidence of certificate sharing, stale delegation and insecure origin links, but the work primarily measures deployment and proposes DANE rather than introducing a reusable attack procedure. |
| [Stealing Webpages Rendered on Your Browser by Exploiting GPU Vulnerabilities](https://www.ieee-security.org/TC/SP2014/papers/StealingWebpagesRenderedonYourBrowserbyExploitingGPUVulnerabilities.pdf) | scope mismatch | A novel local cross-process GPU-memory attack demonstrated on browser textures; the attacker needs local GPU-compute access, so the transferable primitive is system/GPU isolation rather than web hacking. |
| Blended Web and Database Attacks on Real-Time, In-Memory Platforms | target-specific adaptation | The SAP HANA “time travel” SQL-injection payload and SQL-triggered server-side JavaScript are useful target adaptations, but temporal queries, SQL injection and server-side JavaScript injection were already public. |
| Session Identifiers Are for Now, Passwords Are Forever | prior art | XSS-driven extraction from browser password managers was already demonstrated before 2014; the talk develops impact and cases without a sufficiently distinct primitive beyond the two stronger password-manager papers scored here. |
| Hunting the Red Fox Online | defensive methodology | Strong detection and measurement of mass redirect-script injections, not a new offensive technique or offensive-testing method. |
| Analyzing Forged SSL Certificates in the Wild | measurement study | Measures deployed TLS interception and forged certificates; it does not add a new certificate-forgery or interception mechanism. |
| On the Effective Prevention of TLS Man-in-the-Middle Attacks in Web Applications | defensive architecture | A valuable prevention system, but no qualifying offensive primitive. |
| HULK: Eliciting Malicious Behavior in Browser Extensions | defensive analysis | Dynamic elicitation of malicious-extension behavior is malware detection rather than web-vulnerability discovery or exploitation. |
| Understanding the Dark Side of Domain Parking | measurement study | Characterizes malicious parking ecosystems without introducing a distinct web attack primitive. |
| xRay: Enhancing the Web's Transparency with Differential Correlation | privacy/transparency defense | Helps users infer how services use their data; it is not an offensive web-security technique. |
| Detection Method of the Second-Order SQL Injection in Web Applications | companion / narrower mechanism | A same-year, SQL-specific treatment of stored second-order flows. Dahse and Holz's broader static method covers persistent stores and multiple vulnerability classes with stronger evidence. |
| Simulation of Built-in PHP Features for Precise Static Code Analysis | supporting analysis | Improves PHP semantic modeling, but its transferable contribution is general static-analysis precision rather than a distinct offensive web-testing technique. |
| OAuth Demystified for Mobile Application Developers | analysis and guidance | Clarifies SDK assumptions and OAuth integration risks; SSOScan and the hybrid-framework work supply the distinct automated method and attack mechanism. |
| I Know Why You Went to the Clinic | established attack family | A careful HTTPS traffic-analysis methodology study, but its privacy inference mechanism is website fingerprinting; the stronger open-world classifier and timing-only primitive are separately scored. |
| A Large-Scale Analysis of the Security of Embedded Firmwares | scope mismatch | Valuable firmware extraction and vulnerability measurement, but the reusable method is firmware/system analysis rather than a specifically web, HTTP, API or browser contribution. |

## Notes on the gate

Selvi's HSTS bypass is the only newly added 60–69.9 entry. Its 65.4 score
explicitly accounts for the 2012 HSTS draft already warning that a manipulated
clock could weaken policy expiry. The qualifying extension is the demonstrated
NTP man-in-the-middle workflow, Delorean tool and finding that most tested
preload entries were finite and therefore also expirable. This audit did not run
the reference archiver or refresh either web application.
