# 2010 missed-technique audit

This folder records the fresh 2026-08-08 audit for web-security research first
published in 2010 but absent from the original 2010 nomination round. The
exclusion set contained 83 distinct URLs from [`2010.md`](../../2010.md). URL
filtering was followed by a semantic comparison against the mechanisms already
represented there.

The historical-list gate for this audit is **60 or above plus a qualifying
non-duplicate verdict**. A score alone cannot rescue a prior disclosure, an
original nominee under another URL, or work published in the wrong year. Every
credible lead is retained below, including those resolved during screening.

## Coverage

- IEEE S&P, ACM CCS, NDSS, USENIX Security, WOOT, LEET, WebApps, WWW,
  EuroSys, PETS and W2SP 2010 programs and primary papers.
- Black Hat USA, Europe and DC schedules/archives, with a mechanism-level
  comparison against the unusually broad practitioner nomination set.
- Browser-origin and access-control policy, CSS/content-type confusion,
  extension and JavaScript sandbox boundaries, history/private-mode privacy,
  browser fingerprinting, encrypted-traffic side channels, parameter
  tampering, client-side injection, redirect termination and black-box testing.
- Backward prior-art checks in earlier year lists and candidate bibliographies;
  later lists were checked to avoid moving a technique into the wrong year.
- A non-US check through Black Hat Europe and the international academic
  venues. A Russian-language treatment of PHP object injection was traced back
  to Stefan Esser's 2009 primary disclosure rather than counted independently.

DEF CON's live archive is poorly indexable and some personal-site material is
now available only through surviving copies. That is the principal coverage
gap. The original 83-link set already captures most prominent practitioner
browser and HTML5 disclosures from those channels.

## Results

- 30 credible leads retained.
- 19 candidates received full scorecards and all meet the numeric and verdict
  gate: 2 existing missed entries were reassessed and 17 references were added.
- 11 more leads were resolved during screening as semantic duplicates,
  pre-2010 disclosures, defensive-only proposals, or insufficiently distinct
  contributions.
- 1 newly added reference scores in the 60–69 band and would have been lost
  under the previous above-70 rule.

| Score | Decision | Verdict | Candidate |
|---:|---|---|---|
| 85.8 | added | Tooling or methodology contribution | [How Unique Is Your Web Browser?](https://coveryourtracks.eff.org/static/browser-uniqueness.pdf) |
| 85.3 | added | Tooling or methodology contribution | [A Symbolic Execution Framework for JavaScript](https://webblaze.cs.berkeley.edu/papers/kudzu.pdf) |
| 84.5 | added | Meaningful combination or adaptation | [A Practical Attack to De-Anonymize Social Network Users](https://iseclab.org/publications/wondracek2010a_practical/) |
| 82.9 | added | Original technique | [FLAX](https://www.ndss-symposium.org/ndss2010/flax-systematic-discovery-client-side-validation-vulnerabilities-rich-web-applications/) |
| 81.7 | added | Meaningful extension | [Protecting Browsers from Extension Vulnerabilities](https://www.ndss-symposium.org/ndss2010/protecting-browsers-extension-vulnerabilities/) |
| 81.1 | added | Meaningful extension | [Regular Expressions Considered Harmful in Client-Side XSS Filters](https://www.adambarth.com/papers/2010/bates-barth-jackson.pdf) |
| 81.0 | already present; retained | Meaningful extension | [Busting Frame Busting](https://seclab.stanford.edu/websec/framebusting/framebust.pdf) |
| 78.9 | added | Meaningful combination or adaptation | [Fear the EAR](https://bryceboe.com/2010/12/09/ucsbs-international-capture-the-flag-competition-2010-challenge-6-fear-the-ear/) |
| 78.7 | added | Tooling or methodology contribution | [NoTamper](https://www.cs.uic.edu/~venkat/research/papers/NoTamper-ccs2010.pdf) |
| 78.4 | added | Tooling or methodology contribution | [On the Incoherencies in Web Browser Access Control Policies](https://www.microsoft.com/en-us/research/publication/incoherencies-web-browser-access-control-policies/) |
| 78.1 | added | Meaningful extension | [Protecting Browsers from Cross-Origin CSS Attacks](https://www.linshunghuang.com/papers/css.pdf) |
| 77.6 | added | Tooling or methodology contribution | [An Analysis of Private Browsing Modes in Modern Browsers](https://www.usenix.org/conference/usenixsecurity10/analysis-private-browsing-modes-modern-browsers) |
| 77.1 | added | Tooling or methodology contribution | [Residue Objects](https://www.microsoft.com/en-us/research/publication/residue-objects-a-challenge-to-web-browser-security/) |
| 76.3 | added | Meaningful extension | [Preventing Capability Leaks in Secure JavaScript Subsets](https://webblaze.cs.berkeley.edu/blancura.html) |
| 75.2 | added | Tooling or methodology contribution | [An Empirical Study of Privacy-Violating Information Flows](https://www.cs.cornell.edu/~lerner/papers/ccs10-jsc.pdf) |
| 74.0 | added | Tooling or methodology contribution | [State of the Art: Automated Black-Box Web Application Vulnerability Testing](https://web.stanford.edu/~jcm/papers/pci_oakland10.pdf) |
| 73.0 | already present; retained | Meaningful combination or adaptation | [The Emperor's New APIs](https://www.comp.nus.edu.sg/~prateeks/papers/w2sp10-primitives.pdf) |
| 72.3 | added | Tooling or methodology contribution | [Sidebuster](https://www.microsoft.com/en-us/research/publication/sidebuster-automated-detection-and-quantification-of-side-channel-leaks-in-web-application-development/) |
| 68.2 | added | Meaningful extension | [DNS Prefetching and Its Privacy Implications](https://www.usenix.org/conference/leet-10/dns-prefetching-and-its-privacy-implications-when-good-things-go-bad) |

## Screened leads

| Candidate | Outcome | Screening evidence |
|---|---|---|
| [Side-Channel Leaks in Web Applications](https://www.microsoft.com/en-us/research/publication/side-channel-leaks-in-web-applications-a-reality-today-a-challenge-tomorrow/) | semantic duplicate | The original list's “Side Channel Attacks in SSL” and “Improving HTTPS Side Channel Attacks” point to this exact encrypted-web-traffic mechanism. Sidebuster is retained separately only for its new automated analysis method. |
| [Feasibility and Real-World Implications of Web Browser History Detection](https://www.ieee-security.org/TC/W2SP/2010/papers/p26.pdf) | overlap | Browser history detection predates 2010 and the 2009 list includes private-mode detection; the distinct 2010 identity-inference advance is better represented by Wondracek et al. |
| [Utilizing Code Reuse/ROP in PHP Application Exploits](https://media.blackhat.com/bh-us-10/presentations/Esser/BlackHat-USA-2010-Esser-Utilizing-Code-Reuse-Or-Return-Oriented-Programming-In-PHP-Application-Exploits-slides.pdf) | prior disclosure | The dangerous `unserialize`/magic-method object-injection and gadget-chain groundwork was already public in Esser's November 2009 “Shocking News in PHP Exploitation.” The 2010 talk is valuable elaboration, not a first disclosure for this year. |
| [Reining in the Web with Content Security Policy](https://archives.iw3c2.org/www2010/www/program/papers/privacy.html) | prior disclosure / defense | Mozilla's CSP design and implementation were already public in 2009, when the year list even nominated a CSP bypass. The 2010 WWW publication cannot be moved forward a year. |
| [ConScript](https://www.ieee-security.org/TC/SP2010/archived/program.html) | defensive architecture | Fine-grained JavaScript policy enforcement is technically strong, but it does not add a distinct attack or mature offensive-testing method to this list. |
| [Alhambra](https://archives.iw3c2.org/www2010/www/program/papers/browsers-2.html) | defensive architecture | A browser policy enforcement and compatibility-testing framework; useful, but incremental beside the stronger browser-analysis candidates and without a distinct hacking primitive. |
| [xJS: Practical XSS Prevention](https://www.usenix.org/conference/webapps-10/xjs-practical-xss-prevention-web-application-development) | defensive architecture | A server/development-time XSS prevention system rather than a new attack or reusable vulnerability-discovery contribution. |
| [Symbolic Security Analysis of Ruby-on-Rails Web Applications](https://www.sigsac.org/ccs/CCS2010/paper_list.shtml) | formal verification | Important formal modelling, but less directly actionable as a web-hacking or vulnerability-discovery technique than Kudzu, FLAX and NoTamper. |
| [The Case for JavaScript Transactions](https://www.csa.iisc.ac.in/~vg/papers/plas2010/) | position paper | Forward-looking isolation proposal without a demonstrated new attack or mature evaluated testing technique. |
| [Detection and Analysis of Drive-by-Download Attacks and Malicious JavaScript](https://archives.iw3c2.org/www2010/www/program/papers.html) | incremental methodology | A strong detection paper, but drive-by execution analysis and malicious-JavaScript instrumentation were already represented by earlier Ghost-in-the-Browser and CaffeineMonkey work. |
| [Fine-Grained Privilege Separation for Web Applications](https://archives.iw3c2.org/www2010/www/program/papers.html) | defensive architecture | A useful application design, but no distinct attack contribution and limited offensive-testing applicability. |

## Notes on the gate

DNS-prefetch inference is the only newly added 60–69.9 entry. It appears in the
historical list because this audit's explicit gate is 60, while its exact score
and narrower “meaningful extension” verdict remain visible. This audit did not
run the reference archiver or refresh either web application.
