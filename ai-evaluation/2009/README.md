# 2009 missed-technique audit

Audit run 2026-08-08 with the `webseclist-find-missed` and
`webseclist-judge-reference` workflows. The inclusion gate was a score of 60
or above, a qualifying non-duplicate verdict, first public publication in
2009, and absence from the original 2009 nomination set.

The audit began with 88 distinct URLs already present in `2009.md`. It searched
IEEE S&P, USENIX Security, W2SP, NDSS, Black Hat Europe/DC/USA, DEF CON,
OWASP/AppSec and SecTor material; contemporary researcher and standards sites;
and mechanism-specific prior art for TLS, same-origin JavaScript, MIME
sniffing, mashups, embedded management interfaces, OAuth, browser storage,
Unicode transformations, drive-by exploitation and CSRF. Black Hat Europe and
the 26C3/European scene supplied the non-US venue check. No independent
non-English primary source survived the year, technique and novelty gates.

## Outcome

- 20 credible leads are retained below.
- 14 candidates received full scorecards.
- 11 scorecards were kept: 2 existing entries were reassessed and 9 new
  entries were added to `2009.md`.
- 3 scored candidates were removed below the 60-point gate.
- 1 otherwise relevant lead failed the calendar-year gate, and 5 additional
  leads were screened before full scoring.
- 1 new addition scores in the 60–69 band and would have been lost under the
  former above-70 wording.

## Lead index

| Candidate and primary source | Disposition | Reason |
|---|---|---|
| [New Tricks for Defeating SSL in Practice](https://blackhat.com/presentations/bh-dc-09/Marlinspike/BlackHat-DC-09-Marlinspike-Defeating-SSL.pdf) | Retained — 87.3 | Operationalizes pre-TLS HTTPS downgrade as `sslstrip` and documents the null-prefix certificate-name bypass. |
| [TLS Renegotiation authentication gap](https://www.kb.cert.org/vuls/id/120541/) | Retained — 84.4 | Protocol composition flaw splices attacker-controlled bytes into a victim-authenticated TLS connection. |
| [Pretty-Bad-Proxy](https://www.microsoft.com/en-us/research/publication/pretty-bad-proxy-an-overlooked-adversary-in-browsers-https-deployments/) | Added — 84.4 | Malicious HTTP proxies exploit browser behavior above TLS, including executable `CONNECT` errors and cross-origin script redirects. |
| [Cross-Origin JavaScript Capability Leaks](https://www.usenix.org/conference/usenixsecurity09/technical-sessions/presentation/cross-origin-javascript-capability-leaks) | Added — 82.4 | Defines and detects browser implementation flaws that leak JavaScript object capabilities across origins. |
| [OAuth Security Advisory 2009.1](https://oauth.net/advisories/2009-1/) | Added — 80.4 | Adapts session fixation to OAuth 1.0's unbound request-token authorization flow and motivated OAuth 1.0a. |
| [Secure Content Sniffing for Web Browsers](https://webblaze.cs.berkeley.edu/contentsniff.html) | Added — 79.7 | Systematically models browser MIME inference, constructs content-sniffing XSS attacks and derives a safer algorithm. |
| [Cross-Channel Scripting](https://www.blackhat.com/presentations/bh-usa-09/BOJINOV/BHUSA09-Bojinov-EmbeddedMgmt-PAPER.pdf) | Added — 78.8 | Moves stored script through non-web services into embedded web-management interfaces, plus the reverse direction. |
| [Attacks on JavaScript Mashup Communication](https://www.ieee-security.org/TC/W2SP/2009/papers/s1p3.pdf) | Added — 75.2 | Exposes privilege escalation and confused-deputy flaws in explicit mashup communication APIs. |
| [Code-Injection Attacks in Browsers Supporting Policies](https://www.ieee-security.org/TC/W2SP/2009/papers/s3p1.pdf) | Added — 72.9 | Introduces return-to-JavaScript: rearranging trusted existing code to bypass script whitelists. |
| [Unraveling Unicode](https://www.blackhat.com/presentations/bh-usa-09/WEBER/BHUSA09-Weber-UnicodeSecurityPreview-SLIDES.pdf) | Added — 70.8 | Turns best-fit mappings, normalization, malformed decoding and casing behavior into a reusable filter-bypass test method. |
| [A Wolf in Sheep's Clothing](https://blackhat.com/presentations/bh-dc-09/Sutton/blackhat-dc-09-Sutton-persistent-storage.pdf) | Added — 63.5 | Broadens client-side SQL injection into a worked audit of persistent browser-storage attack surfaces. |
| [XSS Anonymous Browser](https://www.blackhat.com/presentations/bh-dc-09/Flick/BlackHat-DC-09-Flick-XAB-wp.pdf) | Removed — 53.8 | Useful relay implementation, but primarily combines XSS-Proxy, XSS Shell, proxying and rebinding ideas already public. |
| [Weaponizing the Web / MonkeyFist](https://www.blackhat.com/presentations/bh-usa-09/HAMIEL/BHUSA09-Hamiel-WeaponizingWeb-SLIDES.pdf) | Removed — 54.0 | Automates dynamic CSRF chains but does not clear the originality and lasting-value threshold. |
| [Breaking the Security Myths of Extended Validation SSL](https://www.blackhat.com/presentations/bh-usa-09/SOTIROV/BHUSA09-Sotirov-AttackExtSSL-SLIDES.pdf) | Removed — 59.3 | EV-specific demonstrations are valuable, but mainly apply rogue certificates, mixed content and same-origin attacks already represented. |
| [Using Guided Missiles in Drive-Bys / Browser Autopwn](https://blackhat.com/html/bh-usa-09/bh-usa-09-speakers.html) | Year gate | The Black Hat 2009 talk is relevant, but Metasploit's primary mailing-list record establishes Browser Autopwn in August 2008. |
| [How I Learned to Stop Worrying and Love Plugins](https://www.ieee-security.org/TC/W2SP/2009/) | Screened | A browser/plugin security architecture rather than a reusable hacking technique. |
| [Document Structure Integrity and Noncespaces](https://www.ieee-security.org/TC/W2SP/2009/) | Screened | Primarily defensive script-injection policies; the separate return-to-JavaScript attack on policy assumptions was judged instead. |
| [Blueprint: Robust Prevention of Cross-site Scripting Attacks](https://www.ieee-security.org/TC/W2SP/2009/) | Screened | Important defence, but not a distinct offensive technique under this archive's inclusion rules. |
| [The Veiled Browser](https://www.ieee-security.org/TC/W2SP/2009/) | Screened | Privacy-preserving communication architecture, outside the web-hacking-technique scope. |
| [Characterizing JavaScript execution and security](https://www.usenix.org/conference/usenixsecurity09) | Screened | Measurement and defensive-analysis work without a separable new offensive mechanism. |

## Prior-art and date controls

The scorecards distinguish the Pretty-Bad-Proxy attacks from ordinary TLS
interception and the nominated active MITM item; cross-channel scripting from
the nominated browser-to-nonstandard-port attack; OAuth request-token fixation
from classic 2002 web session fixation; and mashup API confused deputies from
the same-year browser capability-leak class. The Unicode and persistent-storage
entries receive reduced originality scores because the underlying encodings,
Flash storage and client-side SQL injection already existed.

Browser Autopwn was not promoted because primary Metasploit list traffic dates
it to 2008. The public date for the OAuth advisory is 23 April 2009; the
conference records establish the remaining research dates. Where a paper
acknowledges an older primitive, only its separately evidenced method is scored.

## Evidence gaps and follow-up

DEF CON's older program and artifact mirrors are incomplete, and several 2009
conference entries expose only a title or deck. Those leads were not promoted
without sufficient primary evidence. During comparison, the archived capture
for the nominated i8jesus cross-protocol item was found to be a parked domain;
the fault was recorded centrally in the archive manifest and the generated
needs-work index. This audit did not run the reference archiver or refresh
either web application.
