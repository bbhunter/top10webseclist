# 2006 missed-technique audit

This folder records the fresh 2026-08-08 sweep for web hacking research first
published in 2006 but absent from the original 2006 nomination set. The known-link
filter contained **72 distinct URLs** from [`2006.md`](../../2006.md). A URL surviving
that filter was still compared by underlying technique, so a differently linked copy
of an existing nomination did not become a false "miss."

The historical addition gate is **score 60 or above**, a qualifying non-duplicate
verdict, verified first publication in 2006, and no prior nomination. All credible
leads remain below even when they failed one of those gates. Full evaluations are in
[`judgements.md`](judgements.md); immutable states are in
[`history.jsonl`](history.jsonl).

## Coverage

- **Conference circuit:** complete web/appsec pass over the official Black Hat USA,
  Japan, Europe and Federal 2006 archive; 23C3; DEF CON 14 and OWASP AppSec 2006
  programme/search results. The productive primary artifacts were the Black Hat and
  23C3 decks below.
- **Researcher and era blogs:** ha.ckers.org, GNUCITIZEN, Jeremiah Grossman,
  Hardened-PHP/PHP Security and the WebAppSec/Full Disclosure archives. Dead pages
  were checked through the repository's preserved copies and search-indexed primary
  pages.
- **Academic venues:** USENIX Security 2006, WWW 2006, NDSS 2006, IEEE S&P 2006 and
  CCS 2006, searched by web/browser/HTTP/AJAX/XSS/CSRF mechanism. The in-scope papers
  found were defenses, surveys, or the already nominated history-sniffing mechanism.
- **Mechanism pass:** request splitting/smuggling, caches and proxies, SQL and other
  injection, XSS/CSRF, AJAX/JSON/XML, same-origin and cross-domain behavior, browser
  plugins, cookies, DNS rebinding/intranet pivoting, web worms, and offensive tooling.
- **Non-English pass:** German/CCC and European primary archives were productive;
  Japanese Black Hat was covered through the English primary deck. No independently
  verifiable 2006 Chinese, Japanese, Korean or Russian primary source cleared the
  pre-screen.

Coverage gap: several 2006 OWASP and DEF CON mirrors expose titles without surviving
decks. Those title-only items were searched individually; none supplied enough primary
evidence to advance. This is recorded as a gap rather than treated as proof that no
other work existed.

## Credible leads

| Score | Outcome | Lead | Screening or judgement result |
|---:|---|---|---|
| 77.3 | **added** | [Subverting AJAX](https://fahrplan.events.ccc.de/congress/2006/Fahrplan/attachments/1158-Subverting_Ajax.pdf) | Original prototype hijacking of `XMLHttpRequest`, plus AICS; dated December 2006. |
| 74.2 | **kept** | [Cross-Site Cooking](https://lcamtuf.coredump.cx/cross_site_cooking.txt) | Existing audited miss; reassessed as a meaningful extension because the source credits a 1998 cookie-domain report. |
| 73.9 | held on year gate | [BeEF](https://github.com/beefproject/beef) | Strong, lasting tooling, but evidence conflicts between a 2005 inception claim and the project's 2006 copyright/publication references; not safe to add as genuinely first-published in 2006. |
| 73.3 | **added** | [SQL Injections by Truncation](https://www.blackhat.com/presentations/bh-usa-06/BH-US-06-Neerumalla.pdf) | New escaping-bypass mechanism caused by silently truncated quoted buffers. |
| 67.5 | **added** | [Ajax (in)security](https://www.blackhat.com/presentations/bh-usa-06/BH-US-06-Hoffman.pdf) | Meaningful extension: treats AJAX bridges as privilege-bearing open proxies and attack indirection. |
| 65.7 | **added** | [Breaking AJAX Web Applications](https://www.blackhat.com/presentations/bh-jp-06/BH-JP-06-Stamos-Lackey.pdf) | Reusable AJAX attack-surface enumeration, two-way XSRF analysis, and framework-testing methodology. |
| 63.9 | **added** | [Self-contained XSS Attacks](https://www.gnucitizen.org/blog/self-contained-xss-attacks/) | Meaningful adaptation of `data:` URLs into portable active documents/filter-bypass payloads. |
| 55.8 | retained only | [AttackAPI](https://www.gnucitizen.org/blog/attackapi/) | Useful browser-attack library, but the surviving primary page is thin and the C2 primitive was public in XSS-Proxy in 2005. |
| 55.4 | retained only | [Google Search API Worms](https://www.gnucitizen.org/blog/google-search-api-worms/) | Browser-side adaptation, but search-driven exploitation (Santy) and XSS worms (Samy) were already public. |
| 46.2 | retained only | [Hacking Intranets Via Brute Force](http://ha.ckers.org/blog/20061228/hacking-intranets-via-brute-force/) | Combines public DNS-name discovery with ordinary password brute force; no new attack primitive. |
| — | conceptually excluded | [Traversing the Web](https://www.gnucitizen.org/blog/traversing-the-web/) | The fragment/proxy channel is explicitly used by the already nominated “Attack of the TINY URLs.” |
| — | screened below 60 | [Backdooring Web Pages](https://www.gnucitizen.org/blog/backdooring-web-pages/) | Greasemonkey/widget trojaning and persistent script polling restate established malicious-extension/C2 behavior. |
| — | screened below 60 | [Backframe](https://www.gnucitizen.org/projects/backframe/) | Contemporary browser attack console, but surviving primary evidence is incomplete and its C2 model follows XSS-Proxy/AttackAPI. |
| — | already represented | [Invasive Browser Sniffing and Countermeasures](https://dl.acm.org/doi/10.1145/1135777.1135834) | Academic analysis of the CSS/cache history-sniffing mechanism already nominated as “I know where you've been.” |
| — | defense/out of scope | [Preventing Cross Site Request Forgery Attacks](https://dl.acm.org/doi/10.1145/1180405.1180449) | Security defense rather than a hacking technique; CSRF itself predates 2006. |
| — | defense/out of scope | [BrowserShield](https://www.microsoft.com/en-us/research/publication/browsershield-vulnerability-driven-filtering-of-dynamic-html/) | Browser-side exploit filtering, not an offensive technique. |
| — | already represented | [Zero Day Subscriptions](https://www.blackhat.com/html/bh-usa-06/bh-usa-06-speakers.html) | RSS/Atom exploit delivery is covered by the original “Hacking RSS Feeds” nomination. |

**17 credible leads** were retained: 10 advanced to full scorecards, six qualified
on score/verdict, five were newly added, and one was the existing Cross-Site Cooking
entry. BeEF would clear the score gate but failed the mandatory year-proof gate.
