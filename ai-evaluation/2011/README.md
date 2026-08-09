# 2011 missed-technique audit

This folder records the fresh 2026-08-08 audit for web-security research first
published in 2011 but absent from the original 2011 nomination round. The
exclusion set contained 63 distinct URLs from [`2011.md`](../../2011.md). URL
filtering was followed by a semantic comparison against every mechanism already
represented there.

The historical-list gate for this audit is **60 or above plus a qualifying
non-duplicate verdict**. A score alone cannot rescue a prior disclosure, an
original nominee under another URL, or work published in the wrong year. Every
credible lead is retained below, including those resolved during screening.

## Coverage

- IEEE S&P, ACM CCS and CCSW, NDSS, USENIX Security, WOOT, ACSAC and the
  principal 2011 web-security sessions and primary papers.
- Black Hat USA and DC and DEF CON 19 archives, plus OWASP AppSec material and
  researcher-hosted whitepapers, slides and contemporary posts.
- Payment/API state confusion, access-control and workflow logic, redirects,
  HTTP parameter handling, NoSQL and server-side JavaScript injection,
  deserialisation, cloud interfaces and storage, DNS, encrypted-flow side
  channels, browser history and recommender-system privacy.
- Backward mechanism searches in the 2006–2010 lists and local reference
  archive, followed by bibliography and web checks for the closest prior art.
- A non-US sweep through the international academic venues and Ruhr, EURECOM,
  SBA Research and European Black Hat sources. Korean-language database and
  web-security results found in the sweep were defensive or applications of
  established injection classes, so none survived the gate.
- Bug-bounty-platform and CTF-originated work was checked separately. Public
  commercial bounty platforms were not yet a meaningful disclosure channel in
  2011; the strongest CTF lead, Execution After Redirect, proved to have been
  published in December 2010 and was not moved into this year.

Several personal sites and old conference assets are now intermittently
available, so their official conference records and surviving author copies were
used together. No archive capture was changed by this audit.

## Results

- 32 credible leads retained.
- 16 candidates received full scorecards and meet the numeric and verdict gate:
  2 existing missed entries were reassessed and 14 references were added.
- 16 additional leads were resolved during screening as pre-2011 disclosures,
  defensive-only work, known-technique surveys, scope mismatches or evidence too
  thin to support a distinct contribution.
- 1 newly added reference scores in the 60–69 band and would have been lost
  under the previous above-70 rule.

| Score | Decision | Verdict | Candidate |
|---:|---|---|---|
| 92.6 | added | Original technique | [How to Shop for Free Online](https://www.ieee-security.org/TC/SP2011/PAPERS/2011/paper029.pdf) |
| 85.7 | added | Meaningful combination or adaptation | [Server-Side JavaScript Injection](https://media.blackhat.com/bh-us-11/Sullivan/BH_US_11_Sullivan_Server_Side_WP.pdf) |
| 85.5 | added | Original technique | [Privacy Risks of Collaborative Filtering](https://www.ieee-security.org/TC/SP2011/PAPERS/2011/paper015.pdf) |
| 83.4 | added | Tooling or methodology contribution | [Fast and Precise Sanitizer Analysis with BEK](https://www.usenix.org/conference/usenix-security-11/presentation/fast-and-precise-sanitizer-analysis-bek) |
| 82.3 | added | Meaningful extension | [All Your Clouds Are Belong to Us](https://www.nds.rub.de/media/nds/veroeffentlichungen/2011/10/22/AmazonSignatureWrapping.pdf) |
| 81.2 | added | Tooling or methodology contribution | [Static Detection of Access Control Vulnerabilities](https://www.usenix.org/conference/usenix-security-11/static-detection-access-control-vulnerabilities-web-applications) |
| 81.1 | added | Original technique | [Bit-squatting](https://dinaburg.org/data/DC19_Dinaburg_Presentation.pdf) |
| 79.3 | already present; retained | Original technique | [How to Break XML Encryption](https://www.nds.rub.de/media/nds/veroeffentlichungen/2011/10/22/HowToBreakXMLenc.pdf) |
| 79.3 | added | Meaningful combination or adaptation | [Dark Clouds on the Horizon](https://www.usenix.org/conference/usenix-security-11/presentation/dark-clouds-horizon-using-cloud-storage-attack-vector-and) |
| 78.8 | added | Tooling or methodology contribution | [WAPTEC](https://www.cs.uic.edu/~hinrichs/papers/bisht2011waptec.pdf) |
| 78.2 | added | Tooling or methodology contribution | [Automated Discovery of Parameter Pollution Vulnerabilities](https://www.ndss-symposium.org/ndss2011/automated-discovery-of-parameter-pollution-vulnerabilities-in-web-applications/) |
| 77.4 | added | Tooling or methodology contribution | [Sour Pickles](https://media.blackhat.com/bh-us-11/Slaviero/BH_US_11_Slaviero_Sour_Pickles_WP.pdf) |
| 76.9 | added | Tooling or methodology contribution | [BLOCK](https://ptolemy.berkeley.edu/projects/truststc/pubs/883.html) |
| 74.4 | added | Meaningful extension | [I Still Know What You Visited Last Summer](https://research.owlfolio.org/pubs/2011-i-still-know.pdf) |
| 71.2 | already present; retained | Meaningful extension | [Crouching Tiger Hidden Payload](https://www.nds.ruhr-uni-bochum.de/media/hgi/veroeffentlichungen/2011/10/19/svgSecurity-ccs11.pdf) |
| 68.3 | added | Tooling or methodology contribution | [Automated Black-Box Detection of Side-Channel Vulnerabilities](https://www.cs.virginia.edu/~evans/pubs/ccs2011/) |

## Screened leads

| Candidate | Outcome | Screening evidence |
|---|---|---|
| [Fear the EAR](https://sites.cs.ucsb.edu/~chris/research/doc/ccs11_ear.pdf) | wrong year | The CCS paper is from 2011, but Bryce Boe's complete primary walkthrough named and demonstrated Execution After Redirect on 9 December 2010. It belongs in a 2010 audit, not here. |
| [Cryptography in the Web: The Case of Cryptographic Design Flaws in ASP.NET](https://www.ieee-security.org/TC/SP2011/PAPERS/2011/paper030.pdf) | prior disclosure | The practical ASP.NET padding-oracle break was publicly demonstrated in 2010 and combines Vaudenay's 2002 oracle with the 2010 CBC-R construction. The 2011 paper is a valuable analysis, not a first disclosure for this list. |
| [Slow HTTP POST Denial of Service](https://media.blackhat.com/bh-dc-11/Brennan/BlackHat_DC_2011_Brennan_Denial_Service-Slides.pdf) | prior disclosure | The slow-body technique and public tooling were already released in 2010; the Black Hat DC session does not move it into 2011. |
| Slow Read denial of service | wrong year / insufficient primary evidence | Contemporary references place the distinct slow-response-reading proof of concept in January 2012. A 2011 code-development claim is not enough to establish public disclosure. |
| Apache Killer Range-header denial of service | prior art | The August 2011 exploit operationalised a serious bug, but Michal Zalewski publicly documented the same overlapping-range amplification condition in 2007. |
| [Application-Level Denial of Service](https://media.blackhat.com/bh-dc-11/Sullivan/BlackHat_DC_2011_Sullivan_Application-Level_Denial_of_Service_Att_%26_Def-wp.pdf) | known-technique survey | ReDoS, XML expansion, entity attacks and application deadlocks were already public; the paper usefully groups them but does not add a qualifying new mechanism. |
| [ZOZZLE](https://www.usenix.org/legacy/events/sec11/tech/full_papers/Curtsinger.pdf) | defensive-only | A strong JavaScript malware classifier, but it adds neither an attack primitive nor an offensive vulnerability-discovery method. |
| [SCRIPTGARD](https://www.microsoft.com/en-us/research/publication/scriptgard-automatic-context-sensitive-sanitization-for-large-scale-legacy-web-applications/) | prior disclosure / defense | Its technical report was public in September 2010, and the CCS 2011 version is primarily an automatic defense. |
| WebShield | defensive architecture | Browser-side policy enforcement without a new attack or a mature offensive-testing contribution. |
| PiOS | scope / defensive analysis | A valuable iOS privacy-leak detector, but its transferable contribution is mobile application analysis rather than a web/API attack technique. |
| [Vulnerability Extrapolation](https://www.usenix.org/conference/woot11/vulnerability-extrapolation-assisted-discovery-vulnerabilities-using-machine) | scope mismatch | Similar-code vulnerability discovery is useful, but the 2011 work is a general binary/source method with no sufficiently specific web, HTTP, API or browser contribution. |
| MACE | scope mismatch | Model-inference-assisted concolic protocol exploration is technically strong but evaluated as a general protocol technique, not a distinct web-security contribution. |
| SPDY protocol analysis and tooling | insufficient evidence | The surviving Black Hat abstract promises protocol testing and server-push abuse, but no sufficiently complete primary artifact established a distinct reusable attack. |
| Faces of Facebook | useful case study | Web-scraped profile images plus commodity face recognition demonstrate a privacy risk, but the marginal technical contribution is an application of known scraping and recognition methods. |
| Fashion Crimes: Trending-Term Exploitation on the Web | measurement study | Careful evidence of search-engine poisoning and illicit campaigns, but no distinct attack primitive or testing methodology beyond the already-known SEO abuse. |
| Toward Secure Embedded Web Interfaces | defensive guidance | A useful assessment and design discussion, but it does not establish a qualifying new offensive technique. |

## Notes on the gate

Chapman and Evans's black-box side-channel detector is the only newly added
60–69.9 entry. Its 68.3 score reflects substantial overlap with 2010's
Sidebuster while crediting the distinct repeated-crawl, multi-dimensional
classifier and Fisher-criterion methodology. This audit did not run the
reference archiver or refresh either web application.
