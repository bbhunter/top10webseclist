# 2016 missed-technique audit

This folder records the fresh 2026-08-08 audit for web-security research first
published in 2016 but absent from the original combined 2016/2017 nomination
round. The exclusion set contained 43 distinct URLs from
[`2016-17.md`](../../2016-17.md). Exact URL filtering was followed by a semantic
comparison with every mechanism already represented in that shared file.

The historical-list gate is **60 or above plus a qualifying non-duplicate
verdict**. A score alone cannot rescue prior disclosure, an original nominee
under another URL, or work first published in a different year. Every credible
lead is retained below, including those resolved during screening.

## Coverage

- NDSS, USENIX Security, IEEE S&P, ACM CCS and the principal 2016 Web,
  browser, TLS, DNS, CDN and authentication papers and programs.
- Black Hat USA, Europe and Asia, DEF CON, OWASP AppSec, PortSwigger and
  surviving researcher papers, slides, tools and disclosure posts.
- Cross-origin policy, browser storage and timing, encrypted-resource size,
  XS-search, CSP, browser fingerprinting, motion sensors and extension reuse.
- TLS interception, transcript collisions, SSLv2 cross-protocol oracles,
  64-bit block-cipher collisions, compression side channels, PAC/WPAD and
  partial-HTTPS cookie exposure.
- Multi-party Web workflows, OAuth, mobile-service APIs, embedded Web
  interfaces, sanitizer/WAF model learning, CAPTCHA automation, JNDI/LDAP and
  dangling or expired DNS resources.
- Backward searches through the 2006–2015 lists and local reference archive,
  then bibliography and primary-source checks for the closest earlier
  mechanisms. Candidate dates are first public dates, not later presentation
  or proceedings dates.
- A non-US sweep through European and Asian researchers and venues, including
  KU Leuven, INRIA, Ruhr, Tsinghua, Xidian, Zhejiang, Black Hat Europe/Asia and
  author-hosted papers. No additional non-English primary source cleared the
  gate.
- Bug-bounty, CTF and practitioner disclosures were checked independently.
  The strongest PortSwigger work not already named in the combined list was the
  CORS research; product-only incidents and routine bounties did not clear the
  novelty gate.

Some old conference artifact URLs are now backed by migrated PDF locations or
conference index pages. This audit did not change or validate archive captures.

## Results

- 43 credible leads retained.
- 29 candidates received full scorecards and meet the numeric and verdict gate:
  1 existing missed entry was reassessed and 28 references were added.
- 14 additional leads were resolved during screening as prior art, wrong-year
  work, already represented, defensive/measurement-only work, a scope mismatch,
  or a same-mechanism companion.
- 8 newly added references are in the 60–69 band and would have been lost under
  the previous above-70 rule.

| Score | Decision | Verdict | Candidate |
|---:|---|---|---|
| 93.2 | added | Original technique | [JNDI/LDAP Manipulation to RCE](https://www.blackhat.com/docs/us-16/materials/us-16-Munoz-A-Journey-From-JNDI-LDAP-Manipulation-To-RCE-wp.pdf) |
| 92.4 | added | Original technique | [DROWN](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/aviram) |
| 90.4 | added | Original technique | [All Your DNS Records Point to Us](https://scholarworks.wm.edu/aspubs/823/) |
| 89.4 | added | Original technique | [Forwarding-Loop Attacks in CDNs](https://www.ndss-symposium.org/wp-content/uploads/2017/09/forwarding-loop-attacks-content-delivery-networks.pdf) |
| 87.3 | added | Original technique | [Transcript Collision Attacks](https://www.ndss-symposium.org/wp-content/uploads/2017/09/transcript-collision-attacks-breaking-authentication-tls-ike-ssh.pdf) |
| 87.3 | added | Meaningful extension | [Exploiting CORS Misconfigurations](https://portswigger.net/research/exploiting-cors-misconfigurations-for-bitcoins-and-bounties) |
| 87.0 | added | Tooling or methodology contribution | [Back in Black](https://www.ieee-security.org/TC/SP2016/papers/0824a091.pdf) |
| 86.8 | added | Original technique | [Trusted Browsers for Uncertain Times](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/kohlbrenner) |
| 85.7 | added | Tooling or methodology contribution | [Formal Analysis of OAuth 2.0](https://arxiv.org/abs/1601.01229) |
| 85.6 | added | Tooling or methodology contribution | [Attack Patterns for Multi-Party Web Applications](https://www.ndss-symposium.org/wp-content/uploads/2017/09/attack-patterns-black-box-security-testing-multi-party-web-applications.pdf) |
| 85.4 | added | Tooling or methodology contribution | [FIRMADYNE](https://www.ndss-symposium.org/wp-content/uploads/2017/09/towards-automated-dynamic-analysis-linux-based-embedded-firmware.pdf) |
| 84.9 | added | Tooling or methodology contribution | [AUTOFORGE](https://www.ndss-symposium.org/wp-content/uploads/2017/09/automatic-forgery-cryptographically-consistent-messages-identify-security-vulnerabilities.pdf) |
| 84.8 | added | Meaningful extension | [SWEET32](https://sweet32.info/) |
| 84.7 | added | Original technique | [Request and Conquer](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/vangoethem) |
| 84.5 | added | Meaningful extension | [Advanced Cross-Site Search Attacks](https://www.blackhat.com/docs/us-16/materials/us-16-Gelernter-Timing-Attacks-Have-Never-Been-So-Practical-Advanced-Cross-Site-Search-Attacks.pdf) |
| 84.0 | added | Meaningful extension | [CSP Is Dead, Long Live CSP!](https://research.google/pubs/csp-is-dead-long-live-csp-on-the-insecurity-of-whitelists-and-the-future-of-content-security-policy/) |
| 82.9 | added | Meaningful extension | [MitM Attack by Name Collision](https://www.ieee-security.org/TC/SP2016/papers/0824a675.pdf) |
| 82.8 | added | Original technique | [CrossFire](https://www.ndss-symposium.org/wp-content/uploads/2017/09/crossfire-analysis-firefox-extension-reuse-vulnerabilities.pdf) |
| 82.0 | added | Meaningful extension | [Tracking Mobile Web Users Through Motion Sensors](https://www.ndss-symposium.org/wp-content/uploads/2017/09/tracking-mobile-web-users-through-motion-sensors-attacks-defenses.pdf) |
| 80.9 | added | Original technique | [Crippling HTTPS with Unholy PAC](https://blackhat.com/us-16/briefings.html#crippling-https-with-unholy-pac) |
| 73.1 | already present; retained | Meaningful extension | [HEIST](https://www.blackhat.com/docs/us-16/materials/us-16-VanGoethem-HEIST-HTTP-Encrypted-Information-Can-Be-Stolen-Through-TCP-Windows-wp.pdf) |
| 69.3 | added | Meaningful extension | [Practical New Developments in BREACH](https://www.blackhat.com/docs/asia-16/materials/asia-16-Karakostas-Practical-New-Developments-In-The-BREACH-Attack-wp.pdf) |
| 69.1 | added | Tooling or methodology contribution | [A Simple Generic Attack on Text Captchas](https://www.ndss-symposium.org/wp-content/uploads/2017/09/simple-generic-attack-text-captchas.pdf) |
| 69.1 | added | Tooling or methodology contribution | [Killed by Proxy](https://www.ndss-symposium.org/wp-content/uploads/2017/09/killed-proxy-analyzing-client-end-tls-interception-software.pdf) |
| 69.0 | added | Meaningful extension | [The Cracked Cookie Jar](https://www.ieee-security.org/TC/SP2016/papers/0824a724.pdf) |
| 68.3 | added | Meaningful extension | [Domain-Z](https://coeus.ece.gatech.edu/articles/domain-z-ieee.pdf) |
| 68.0 | added | Meaningful extension | [Website Fingerprinting at Internet Scale](https://www.ndss-symposium.org/wp-content/uploads/2017/09/website-fingerprinting-internet-scale.pdf) |
| 66.2 | added | Meaningful extension | [Beauty and the Beast](https://www.ieee-security.org/TC/SP2016/papers/0824a878.pdf) |
| 65.5 | added | Meaningful extension | [I Know What You Saw Last Minute](https://arxiv.org/abs/1602.00490) |

## Screened leads

| Candidate | Outcome | Screening evidence |
|---|---|---|
| [httpoxy](https://httpoxy.org/) | prior art / rediscovery | The 2016 campaign coordinated fixes and naming, but CGI-to-`HTTP_PROXY` poisoning had public reports dating to 2001; the mechanism was not first disclosed in 2016. |
| On the Security of Modern Single Sign-On Protocols: Second-Order Vulnerabilities in OpenID Connect | wrong year | The NDSS 2016 presentation followed an author preprint first published in August 2015, so it belongs to the 2015 audit. |
| 1000 Ways to Die in Mobile OAuth | wrong year / repeat | The Black Hat 2016 talk presents the authors' OAuth study published at ACM CCS in 2014 rather than a new 2016 contribution. |
| [Cracking the Lens](https://portswigger.net/blog/cracking-the-lens-targeting-https-hidden-attack-surface) | already represented | The combined file already records it as excluded from the competition; it cannot also be a missed entry. |
| [XSS without HTML](https://portswigger.net/blog/xss-without-html-client-side-template-injection-with-angularjs) | already represented | The combined file already records it as excluded from the competition. |
| [Binary Webshell Through OPcache](https://gosecure.net/2016/04/27/binary-webshell-through-opcache-in-php-7/) | already nominated | It is the original combined list's #10 entry. |
| Bypassing Browser Security Policies for Fun and Profit | target-specific bundle | Useful mobile-browser test cases and implementation bugs, but no single transferable mechanism beyond the separately judged browser-policy work. |
| Web Application Firewalls: Analysis of Detection Logic | same-mechanism companion | Regex review and fuzzing are useful, but Back in Black supplies the stronger formal black-box learning method and reproducible contribution. |
| Are These Ads Safe? | defensive / measurement methodology | Automates discovery and provenance of malicious app-to-Web destinations; it does not contribute an offensive Web-testing primitive. |
| Over the Edge: Silently Owning Windows 10's Secure Browser | scope mismatch | A strong deduplication and Rowhammer exploit chain whose reusable core is local memory/hardware exploitation, not Web, HTTP or application testing. |
| ImageTragick | target-specific vulnerability | High-impact product flaws and payloads, but no sufficiently distinct reusable technique beyond established command injection and parser abuse. |
| Verena: End-to-End Integrity Protection for Web Applications | defensive architecture | Provides verifiable Web-query integrity without adding an offensive technique. |
| Cloak of Visibility | defensive detection | Detects cloaking against security crawlers; it is not an offensive vulnerability-discovery or exploitation method. |
| TLS in the Wild | measurement study | Valuable Internet-wide deployment evidence, but it does not introduce an attack primitive or offensive testing method. |

## Notes on the gate

The eight additions below 70 are deliberately visible rather than rounded up.
Their contribution scores account for substantial prior art: CAPTCHA breaking,
website and browser fingerprinting, TLS proxy failures, cookie hijacking,
BREACH, expired-domain abuse and encrypted-stream classification all predate
2016. What qualifies is the distinct generic method, new attack adaptation or
systematic testing contribution documented in each scorecard. This audit did
not run the reference archiver or refresh either web application.
