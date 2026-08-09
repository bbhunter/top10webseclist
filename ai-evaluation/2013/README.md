# 2013 missed-technique audit

Audit run 2026-08-08 with the `webseclist-find-missed` and
`webseclist-judge-reference` workflows. The inclusion gate was a score of 60 or
above, a qualifying non-duplicate verdict, first public publication in 2013,
and absence from the original 2013 nomination set.

The audit began with 39 distinct URLs already present in [`2013.md`](../../2013.md)
and one existing missed entry. URL exclusion was followed by a semantic
comparison against the mechanisms in the Top 10, other nominations and earlier
year lists. The existing Host Header entry was reassessed rather than duplicated.

## Coverage

- NDSS, IEEE S&P and W2SP, USENIX Security, WOOT, LEET, ACM CCS, WWW,
  ACSAC and the principal web/browser security programs.
- Black Hat USA and Europe, AppSec/OWASP material, DEF CON-era practitioner
  sources, 30C3/HITB searches and contemporary researcher publication pages.
- HTTP host trust, browser messaging and named properties, TLS state and
  algorithm agility, off-path injection, DNS rebinding, authentication/SSO,
  password managers, REST APIs, personalisation, social privacy inference,
  fingerprinting, WebView and app/web origin boundaries, and business logic.
- Backward mechanism searches through the 2006–2012 lists and candidate
  bibliographies. This separated new 2013 extensions from browser fingerprinting,
  flow redirection, bitsquatting, DNS rebinding, TCP injection, WebView bridges,
  XSS and password-manager work already public.
- A non-US sweep through European, Chinese, Korean, Israeli and Brazilian-hosted
  venues and author collections. The kept set includes primary work from Austria,
  Belgium, China, France, Germany, Israel, South Korea and the United Kingdom as
  well as North America.

Older practitioner indexes and event mirrors remain uneven, so conference
programs were paired with author-hosted or standards-body artifacts. No faulty
archived capture was encountered, and no archive or web-app refresh was run.

## Outcome

- 37 credible leads are retained in this report.
- 19 candidates received full scorecards: the existing Host Header entry was
  reassessed and 18 new references were added to `2013.md`.
- 18 additional leads were resolved during screening as original nominations,
  pre-2013 disclosures, same-mechanism overlaps, defensive/measurement-only work
  or scope mismatches.
- 4 new additions score in the 60–69 band and would have been lost under the
  former above-70 wording.

## Judged lead index

| Score | Decision | Verdict | Candidate |
|---:|---|---|---|
| 85.2 | retained | Original technique | [Practical HTTP Host Header Attacks](https://www.skeletonscribe.net/2013/05/practical-http-host-header-attacks.html) |
| 82.5 | added | Original technique | [One Bad Apple](https://www.ndss-symposium.org/ndss2013/ndss-2013-programme/one-bad-apple-backwards-compatibility-attacks-state-art-cryptography/) |
| 81.9 | added | Tooling or methodology contribution | [The Postman Always Rings Twice](https://www.ndss-symposium.org/ndss2013/ndss-2013-programme/postman-always-rings-twice-attacking-and-defending-postmessage-html5-websites/) |
| 81.0 | added | Original technique | [Unauthorized Origin Crossing on Mobile Platforms](https://www.microsoft.com/en-us/research/publication/unauthorized-origin-crossing-on-mobile-platforms-threats-and-mitigation/) |
| 80.6 | added | Tooling or methodology contribution | [Explicating SDKs](https://www.cs.virginia.edu/~evans/pubs/usenix2013/) |
| 79.7 | added | Tooling or methodology contribution | [AUTHSCAN](https://www.ndss-symposium.org/ndss2013/ndss-2013-programme/authscan-automatic-extraction-web-authentication-protocols-implementations/) |
| 78.1 | added | Meaningful combination or adaptation | [Automated Password Extraction Attack on Modern Password Managers](https://arxiv.org/abs/1309.1416) |
| 76.7 | added | Meaningful extension | [Truncating TLS Connections to Violate Beliefs in Web Applications](https://www.usenix.org/conference/woot13/workshop-program/presentation/smyth) |
| 75.5 | added | Meaningful extension | [DOM Clobbering](https://thespanner.co.uk/2013/05/16/dom-clobbering) |
| 75.4 | added | Meaningful extension | [When Tolerance Causes Weakness](https://archives.iw3c2.org/www2013/proceedings/p435.pdf) |
| 74.5 | added | Meaningful extension | [Cookieless Monster](https://seclab.cs.ucsb.edu/publications/nikiforakis2013cookieless_monster/) |
| 74.0 | added | Tooling or methodology contribution | [Language-based Defenses Against Untrusted Browser Origins](https://www.usenix.org/conference/usenixsecurity13/technical-sessions/presentation/bhargavan) |
| 73.0 | added | Meaningful combination or adaptation | [Take This Personally](https://www.usenix.org/conference/usenixsecurity13/technical-sessions/paper/xing) |
| 71.9 | added | Meaningful combination or adaptation | [Exploiting Innocuous Activity for Correlating Users Across Sites](https://archives.iw3c2.org/www2013/proceedings/p447.pdf) |
| 70.4 | added | Meaningful combination or adaptation | [I Know the Shortened URLs You Clicked on Twitter](https://archives.iw3c2.org/www2013/proceedings/p1191.pdf) |
| 68.4 | added | Tooling or methodology contribution | [A View to a Kill](https://www.usenix.org/conference/leet13/workshop-program/presentation/neugschwandtner) |
| 68.3 | added | Tooling or methodology contribution | [Cross-Site Scripting Attacks in Social Network APIs](https://www.ieee-security.org/TC/W2SP/2013/papers/s3p1.pdf) |
| 67.3 | added | Meaningful extension | [FireDrill](https://www.usenix.org/conference/woot13/workshop-program/presentation/dai) |
| 62.3 | added | Tooling or methodology contribution | [Analyzing Unique-Bid Auction Sites for Fun and Profit](https://www.ndss-symposium.org/ndss2013/ndss-2013-programme/analyzing-unique-bid-auction-sites-fun-and-profit/) |

Full evidence, prior-art comparisons and weighted category scores are in
[`judgements.md`](judgements.md).

## Screened leads

| Candidate | Outcome | Screening evidence |
|---|---|---|
| [Cross-Origin Pixel Stealing](https://dl.acm.org/doi/10.1145/2508859.2516712) | already represented | The Top 10's Pixel Perfect Timing Attacks entry is the same 2013 CSS-filter pixel-recovery mechanism and paper family. |
| [mXSS Attacks](https://www.sigsac.org/ccs/CCS2013/program/accepted-papers/index.html) | already represented | Mutation XSS is the year's #1 result. |
| [25 Million Flows Later](https://doi.org/10.1145/2508859.2516703) | already represented | The Top 10 explicitly contains Large Scale Detection of DOM based XSS, the same system and result. |
| [Bitsquatting](https://archives.iw3c2.org/www2013/proceedings/p989.pdf) | year gate | The technique was publicly introduced by Artem Dinaburg in 2011; the 2013 WWW paper is later analysis and measurement. |
| [Flow Stealing](https://journals.sagepub.com/doi/pdf/10.3233/JCS-130466?download=true) | year gate | The journal article appeared in 2013, but the same timing/redirection attack was publicly presented as “Timing is Everything” at ESORICS 2011. |
| [Off-Path Hacking: Illusion of Challenge-Response](https://arxiv.org/abs/1305.0854) | overlap / survey | Synthesises the authors' 2011–2013 line. The distinct 2013 injection-friendly mechanism was judged directly. |
| [Fast and Reliable Browser Identification with JavaScript Engine Fingerprinting](https://www.ieee-security.org/TC/W2SP/2013/papers/s2p1.pdf) | same-mechanism overlap | A strong speed improvement over 2011 JavaScript fingerprinting, but semantically overlaps the broader, fully judged Cookieless Monster contribution in the same year. |
| [FPDetective: Dusting the Web for Fingerprinters](https://doi.org/10.1145/2508859.2516674) | defensive / overlap | Automated detection and measurement of an already represented fingerprinting mechanism; it adds no separable offensive primitive beyond Cookieless Monster. |
| Rethinking SSL Development in an Appified World | prior mechanism / defensive | Extends the 2012 Android TLS validation studies to iOS and developer causes, with its main contribution in developer support and platform design rather than a new attack. |
| [InteGuard](https://www.ndss-symposium.org/ndss2013/ndss-2013-programme/integuard-toward-automatic-protection-third-party-web-service-integrations/) | defensive | Proxy enforcement for vulnerable third-party integrations; the underlying integration attacks were already public and the new contribution is protection. |
| [Behind the Scenes of Online Attacks](https://www.ndss-symposium.org/ndss2013/ndss-2013-programme/behind-scenes-online-attacks-analysis-exploitation-behaviors-web/) | measurement | Valuable honeypot analysis of exploitation behavior, but not a distinct attack or offensive testing method. |
| [Fix Me Up](https://www.ndss-symposium.org/ndss2013/ndss-2013-programme/fix-me-repairing-access-control-bugs-web-applications/) | defensive | Automated repair of access-control bugs rather than a new attack technique. |
| [Cross-site Scripting Attacks on Android WebView](https://arxiv.org/abs/1304.7451) | same-mechanism overlap | A narrower application of known XSS/WebView behavior; the stronger LEET WebView threat model and large-scale method was judged. |
| [Browser Extension Password Managers](https://www.nccgroup.com/research/white-paper-browser-extension-password-managers/) | same-mechanism case study | Useful vendor testing, but unintended autofill and hostile-page extraction overlap the stronger Lupin and shared-origin component analyses judged above. |
| [ZMap](https://www.usenix.org/conference/usenixsecurity13/technical-sessions/paper/durumeric) | scope mismatch | Foundational Internet-wide scanning, but its underlying contribution is network measurement rather than a web-specific attack or web testing method. |
| [Revolver](https://www.usenix.org/conference/usenixsecurity13/technical-sessions/paper/kapravelos) | defensive-only | Detects evasive web malware; it does not add a reusable offensive web mechanism. |
| Delta: Automatic Identification of Unknown Web-Based Infection Campaigns | defensive-only | Detection and campaign clustering rather than a new technique for attacking web applications. |
| Here's My Cert, So Trust Me, Maybe? | measurement | Measures TLS certificate errors and user exposure without a separable new offensive mechanism. |

## Gate notes

The four additions recovered only because the threshold is now 60 or above are
A View to a Kill (68.4), Cross-Site Scripting Attacks in Social Network APIs
(68.3), FireDrill (67.3), and Analyzing Unique-Bid Auction Sites (62.3). Each
crosses the gate through a qualifying extension, combination or methodology—not
through score alone. The unique-bid result is the most borderline: it remains
included because its side-signal extraction plus simulation-guided business-logic
abuse is a demonstrated reusable method, but its transferability is narrow and
confidence is therefore Medium.
