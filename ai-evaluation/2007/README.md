# 2007 missed-technique audit

This folder records the fresh 2026-08-08 audit for web-security research first
published in 2007 but absent from the original 2007 nomination round. The
exclusion set contained 88 distinct URLs from [`2007.md`](../../2007.md). URL
filtering was followed by a semantic check, because several conference papers
describe techniques already represented by a different nomination URL.

The historical-list gate for this audit is **60 or above plus a non-duplicate
novelty verdict**. A score alone cannot rescue work published in the wrong year,
an original nominee, or a rediscovery. All credible leads remain below whether
or not they advanced or qualified.

## Coverage

- Black Hat USA and Europe 2007 proceedings, with relevant browser, web-service,
  XML, timing, and web-malware presentations read from the original archive.
- USENIX Security, HotSec, HotBots, and WOOT 2007 proceedings.
- ACM CCS, NDSS, IEEE S&P, W2SP, and WWW 2007 web-security programs.
- Mechanism searches for browser-origin isolation, frames, AJAX/JSON, timing
  side channels, database behavior, web worms, XML signatures, malware
  analysis, and web-testing automation.
- Backward prior-art searches against `archived-references/md/` and primary
  online sources, including the candidates' own bibliographies.

Older personal blogs and Bugtraq/Full Disclosure archives are incompletely
indexed on the live web. Their best-known 2007 web items are already unusually
well represented by the 88-link nomination set; this remains the main coverage
gap, especially for non-English personal sites whose 2007 archives no longer
resolve.

## Results

Twenty-one credible leads were retained. Eleven received full scorecards in
[`judgements.md`](judgements.md): nine meet the gate (the existing timing entry
plus eight newly recovered references), while two fall below 60. Ten more were
resolved during screening because they were already nominated by mechanism,
were first published outside 2007, or did not contain a distinct attack or
testing contribution.

| Score | Decision | Verdict | Candidate |
|---:|---|---|---|
| 84.8 | added | Original technique | [Heap Feng Shui in JavaScript](https://www.blackhat.com/presentations/bh-europe-07/Sotirov/Whitepaper/bh-eu-07-sotirov-WP.pdf) |
| 78.2 | already present; retained | Original technique | [Exposing Private Information by Timing Web Applications](https://crypto.stanford.edu/~dabo/pubs/abstracts/webtiming.html) |
| 71.5 | added | Original technique | [The ND2DB Attack](https://www.usenix.org/legacy/event/woot07/tech/full_papers/futoransky/futoransky.pdf) |
| 69.3 | added | Meaningful extension | [Protecting Browsers from Frame Hijacking Attacks](https://seclab.stanford.edu/websec/frames/) |
| 68.2 | added | Meaningful extension | [JavaScript Hijacking](https://seclists.org/securecoding/2007/q2/0) |
| 67.7 | added | Tooling or methodology contribution | [The Ghost in the Browser](https://www.usenix.org/conference/hotbots-07/ghost-browser-analysis-web-based-malware) |
| 66.5 | added | Tooling or methodology contribution | [CaffeineMonkey](https://blackhat.com/presentations/bh-usa-07/Feinstein_and_Peck/Presentation/bh-usa-07-feinstein_and_peck.pdf) |
| 64.8 | added | Tooling or methodology contribution | [An Analysis of Browser Domain-Isolation Bugs](https://www.microsoft.com/en-us/research/?p=153771) |
| 64.5 | added | Meaningful combination or adaptation | [Transaction Generators: Root Kits for Web](https://www.usenix.org/conference/hotsec-07/transaction-generators-root-kits-web) |
| 58.1 | evaluation only | Tooling or methodology contribution | [A Taxonomy of Attacks against XML Digital Signatures & Encryption](https://blackhat.com/presentations/bh-usa-07/Hill/Whitepaper/bh-usa-07-hill-WP.pdf) |
| 55.8 | evaluation only | Meaningful combination or adaptation | [The Little Hybrid Web Worm that Could](https://www.blackhat.com/presentations/bh-usa-07/Hoffman_and_Terrill/Whitepaper/bh-usa-07-hoffman_and_terrill-WP.pdf) |

## Screened leads

| Candidate | Outcome | Screening evidence |
|---|---|---|
| [Protecting Browsers from DNS Rebinding Attacks](https://crypto.stanford.edu/dns/) | original nomination by mechanism | The 2007 list already nominates anti-DNS pinning, Flash rebinding, Java rebinding, LocalRodeo, and related intranet attacks. The paper is valuable consolidation and defense, but not missed technique material. |
| [Dynamic pharming attacks and locked same-origin policies](https://www.sigsac.org/ccs/CCS2007/research-program.html) | semantic duplicate | Another DNS-rebinding/pharming treatment in the same CCS program; the mechanism is already extensively nominated. |
| [SpyProxy: Execution-based Detection of Malicious Web Content](https://www.usenix.org/conference/16th-usenix-security-symposium/presentation/spyproxy-execution-based-detection-malicious-) | below pre-screen | Disposable-VM execution before delivery is a solid defense, but closely extends client honeypots and overlaps the stronger 2007 malware-analysis leads. |
| [Cross Site Scripting Prevention with Dynamic Data Tainting and Static Analysis](https://www.ndss-symposium.org/ndss2007/ndss-2007-programme/) | below pre-screen | Defensive hybrid analysis against an established class; no distinct hacking primitive and limited marginal methodology beyond prior taint-analysis work. |
| [Sphinx: An Anomaly-based Web Intrusion Detection System](https://blackhat.com/html/bh-usa-07/bh-usa-07-speakers.html) | below pre-screen | Combines parameter typing, grammars, and n-grams in a WIDS; useful engineering but an incremental anomaly-detection composition. |
| [ScarabMon: Automating Web Application Penetration Tests](https://blackhat.com/html/bh-europe-07/bh-eu-07-speakers.html) | below pre-screen | Extensible passive checks around WebScarab improved workflow but did not establish a durable new testing method. |
| [Extensible Web Browser Security](https://www.usenix.org/legacy/event/sec07/wips.html) | below pre-screen | BrowserSpy demonstrates the already-understood full privilege of malicious extensions; the novel material is primarily installation integrity defense. |
| [A Systematic Approach to Uncover GUI Logic Flaws for Web Security](https://www.microsoft.com/en-us/research/wp-content/uploads/2006/12/tr-2006-182.pdf) | wrong year | Strong methodology, but the primary technical report is dated December 2006; later 2007 publication does not move first disclosure. |
| [End-to-End Web Application Security](https://www.usenix.org/conference/hotos-xi/end-end-web-application-security) | below pre-screen | A forward-looking architecture paper rather than a demonstrated attack or mature testing technique. |
| [JavaScript Breaks Free](https://www.ieee-security.org/TC/W2SP/2007/) | below pre-screen | W2SP position material identifies emerging JavaScript risks but lacks the evidence and distinct contribution of the fully judged AJAX/browser candidates. |

## Notes on the gate

The six qualifying 60–69.9 entries are supporting-reference grade under the
general judge defaults. They appear in the historical list because this audit's
explicit gate is 60, while their entry text preserves both the exact score and
the narrower verdict. The two sub-60 scorecards remain discoverable here and in
the immutable history rather than being discarded.
