# 2008 missed-technique audit

Audit run 2026-08-08 with the `webseclist-find-missed` and
`webseclist-judge-reference` workflows. The inclusion gate for this pass was a
score of 60 or above, a qualifying non-duplicate verdict, first public
publication in 2008, and absence from the original 2008 nomination set.

The audit compared candidates against the 79 URLs already present in `2008.md`.
It searched academic and conference proceedings (USENIX Security, WOOT, WWW,
CCS, NDSS, DIMVA, IEEE S&P, Black Hat and DEF CON), contemporary researcher
sites and Bugtraq, and the browser, TLS/cookie, DNS, injection, redirect,
business-logic race and parser-normalisation topic families. Black Hat Japan
provided a bilingual/non-US venue check. No distinct non-English or
CTF-originated technique survived screening; modern bug-bounty platforms did
not yet provide a meaningful 2008 source pool.

## Outcome

- 17 credible leads retained below.
- 11 candidates received full scorecards.
- 10 scorecards were kept: the existing CSRF entry plus 9 new additions.
- 1 scored candidate was removed as an independent rediscovery.
- 7 additional leads were screened before full scoring.
- 2 of the new additions score in the 60–69 band and would have been lost under
  the previous above-70 rule.

## Lead index

| Candidate and primary source | Disposition | Reason |
|---|---|---|
| [Creating a rogue CA certificate](http://www.phreedom.org/research/rogue-ca/) | Added — 93.7 | First published on 30 December 2008 and therefore a 2008 technique under the strict calendar-year rule. It remains in the official 2009 ranking, but that later placement is not an exclusion from this audit. |
| [Securing Frame Communication in Browsers](https://www.usenix.org/legacy/event/sec08/tech/full_papers/barth/barth_html/index.html) | Added — 85.6 | The 2008-specific contribution is the cross-frame messaging confidentiality race and target-origin control; the authors' 2007 frame-navigation work is excluded. |
| [ForceHTTPS](https://archives.iw3c2.org/www2008/papers/pdf/p525-jacksonA.pdf) | Added — 87.1 | Deployable site-controlled strict-HTTPS policy and the canonical precursor to HSTS. |
| [Black Ops 2008](https://blackhat.com/presentations/bh-jp-08/bh-jp-08-Kaminsky/BlackHat-Japan-08-Kaminsky-DNS08-BlackOps.pdf) | Added — 86.2 | Meaningful extension that removes the DNS cache retry/TTL barrier with random child labels. |
| [Robust Defenses for CSRF](https://seclab.stanford.edu/websec/csrf/csrf.pdf) | Retained — 84.8 | Existing missed entry; introduced login CSRF analysis and the Origin-header defence. |
| [On Race Vulnerabilities in Web Applications](https://roberto.greyhats.it/pubs/dimva08-web.pdf) and [Concurrency Attacks in Web Applications](https://www.blackhat.com/presentations/bh-usa-08/Stender_Vidergar/BH_US_08_Stender_Vidergar_Concurrency_Attacks_in%20Web_Applications_Whitepaper.pdf) | Added — 82.2 | Independent 2008 treatments turned generic races into a reusable web business-logic testing technique. |
| [Increased DNS Forgery Resistance Through 0x20-Bit Encoding](https://coeus.ece.gatech.edu/2008/10/01/DNS_Forgery/) | Added — 78.2 | New backwards-compatible DNS query entropy channel. |
| [Automatic Generation of XSS and SQL Injection Attacks](https://www.usenix.org/legacy/event/sec08/tech/full_papers/martin/martin_html/index.html) | Added — 77.0 | First practical goal-directed model-checking workflow producing concrete multi-request web attack traces. |
| [CookieMonster](https://fscked.org/projects/cookiemonster) | Added — 68.5 | The active cookie-injection primitive was known, but the automated exploitation tool and workflow qualify as a methodology contribution. |
| [Exploitable Redirects on the Web](https://www.usenix.org/event/woot08/tech/full_papers/shue/shue.pdf) | Added — 68.0 | First large systematic identification and measurement method for exploitable redirects. |
| [Cookie forcing](https://scarybeastsecurity.blogspot.com/2008/11/cookie-forcing.html) | Removed — 66.5 | The author credits Filipe Almeida with the same HTTPS-cookie integrity issue about two years earlier. |
| [Corrupted DNS Resolution Paths](https://research.google/pubs/corrupted-dns-resolution-paths-the-rise-of-a-malicious-resolution-authority/) | Screened | The paper appeared in 2008, but the work was already public at the 2007 DNS-OARC workshop. |
| [SessionLock](https://archives.iw3c2.org/www2008/papers/pdf/p517-adida.pdf) | Screened | Defensive session protocol overlapping the already-public sidejacking problem and the stronger ForceHTTPS contribution. |
| [Owning the paranoid: browser background traffic](https://scarybeastsecurity.blogspot.com/2008/11/owning-paranoid-browser-background.html) | Screened | Useful active-network enabler, but not a separately durable technique beyond CookieMonster and cookie forcing. |
| [Encoded, Layered, and Transcoded Syntax Attacks](https://blackhat.com/html/bh-usa-08/bh-usa-08-archive.html) | Screened | Relevant parser/WAF-evasion lead, but no sufficiently substantive original primary material was recoverable for a defensible score. |
| [SQL Injection Worms for Fun and Profit](https://blackhat.com/html/bh-usa-08/bh-usa-08-archive.html) | Screened | Automation of already-known SQL injection and web-worm ideas; overlaps the nominated Diminutive web worm. |
| [Secure Web Browsing with the OP Browser](https://bob.cs.ucdavis.edu/assets/dl/op.pdf) | Screened | Important browser architecture, but a defensive system rather than a distinct reusable web-hacking technique. |

## Evidence gaps and follow-up

The original fscked.org CookieMonster pages are currently unreliable and will
need archive capture in the reference-archiving phase. Several old Black Hat
pages expose only an archive listing, which is why the parser-evasion and SQLi
worm leads were retained but not promoted. This audit deliberately did not run
the reference archiver or refresh either web application.

## Rogue-CA cross-year note

The original 2008 nominations post opened on 26 January 2009 and continued to
accept additions into February; the final results appeared on 23 February.
The rogue-CA work was publicly presented and published on 30 December 2008, so
it was available before the nomination round and was not made ineligible by a
cutoff. Its omission from that round is precisely a missed-list case. The same
resource remains the official number-one item in `2009.md`, because this audit
does not rewrite historical rankings; its presence there does not change its
first-publication year.
