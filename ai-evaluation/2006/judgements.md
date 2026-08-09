# 2006 full judgements

Each score is the marginal contribution over prior art, not the impact of the named
targets. `KEPT` means the research satisfies the historical ≥60, non-duplicate and
year gates; `REMOVED` means it remains only in this evaluation record.

## 77.3 — [Subverting AJAX](https://fahrplan.events.ccc.de/congress/2006/Fahrplan/attachments/1158-Subverting_Ajax.pdf) [Event](https://fahrplan.events.ccc.de/congress/2006/Fahrplan/events/1602.en.html) — Stefano Di Paola and Giorgio Fedon

**KEPT** · Original technique · confidence High

### Core contribution

The December 2006 paper shows that injected script can replace or wrap native
`XMLHttpRequest` objects and prototype methods, transparently intercepting and changing
an AJAX application's requests and responses. It also combines browser/plugin request
splitting with frame injection into Auto Injecting Cross Domain Scripting (AICS), which
can seed script into subsequently visited origins through a forward proxy.

### Prior art

- Earlier 2006 AJAX work documented expanded attack surfaces and bridge abuse:
  [Ajax (in)security](https://www.blackhat.com/presentations/bh-usa-06/BH-US-06-Hoffman.pdf)
  and [Breaking AJAX Web Applications](https://www.blackhat.com/presentations/bh-jp-06/BH-JP-06-Stamos-Lackey.pdf).
- Amit Klein's 2005 HTTP request-smuggling/splitting work supplies the proxy-queue
  primitive used by AICS; ordinary XSS already supplied initial script execution.
- The distinct contribution is the explicit prototype/XHR interposition primitive and
  its worked transparent man-in-the-browser use. Later literature names Di Paola and
  Fedon as the introduction of “Prototype Hijacking.”

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78 | 25% | 19.50 | New reusable XHR/prototype interposition primitive; AICS is a non-obvious chain. |
| Transferability | 80 | 20% | 16.00 | Applies to prototype-based browser APIs and many AJAX applications. |
| Lasting value | 78 | 20% | 15.60 | Established a named client-side hijacking pattern cited by later work. |
| Technical soundness | 78 | 15% | 11.70 | Mechanisms, assumptions and code are explicit. |
| Practical usability | 70 | 10% | 7.00 | Directly testable, though AICS needs a vulnerable proxy/browser component. |
| Clarity and reproducibility | 75 | 10% | 7.50 | Eight-page paper includes code and attack sequences. |

**Final score: 77.3/100**

### Verdict

- **Archive decision:** Include as a core technique
- **Confidence:** High
- **Reasoning:** Prototype hijacking is distinct from the earlier general AJAX/XSS
  surveys; AICS is a meaningful combination even though request splitting predates it.
- **Evidence gaps:** The paper's “found by” claim cannot prove no obscure earlier use,
  but targeted pre-December searches found no equivalent publication.

---

## 74.2 — [Cross-Site Cooking](https://lcamtuf.coredump.cx/cross_site_cooking.txt) [Mirror](https://seclists.org/fulldisclosure/2006/Jan/943) — Michal Zalewski

**KEPT** · Meaningful extension · confidence High

### Core contribution

The January 2006 research systematically demonstrates that browser cookie-domain
handling lets one host set or overwrite cookies for unrelated sibling hosts under some
country-code and legacy domain structures, turning shared browser state into a
cross-site injection primitive.

### Prior art

- [RFC 2109 (1997)](https://www.rfc-editor.org/rfc/rfc2109) defined the domain-matching
  model and its security rationale.
- Zalewski explicitly credits Benjamin Franz with privately reporting a related cookie
  domain problem in 1998. The source therefore does not support an absolute first-ever
  primitive claim.
- Its distinct contribution is public, cross-browser systematization, practical test
  cases, and the general “cross-site cooking” attack model rather than one vendor bug.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 72 | 25% | 18.00 | Strong public generalization over an earlier private report. |
| Transferability | 80 | 20% | 16.00 | Browser cookie scope is a cross-site platform boundary. |
| Lasting value | 80 | 20% | 16.00 | Cookie tossing/domain confusion remains a durable testing concept. |
| Technical soundness | 72 | 15% | 10.80 | Concrete browser tests and limitations, though informal. |
| Practical usability | 74 | 10% | 7.40 | Reproducible wherever domain structures and browser behavior align. |
| Clarity and reproducibility | 60 | 10% | 6.00 | Plain-text advisory is understandable but not exhaustive. |

**Final score: 74.2/100**

### Verdict

- **Archive decision:** Include as a core technique
- **Confidence:** High
- **Reasoning:** The publication added a durable, transferable public attack model;
  “meaningful extension” is more accurate than the earlier “original technique” label
  because its own history names 1998 prior art.
- **Evidence gaps:** The 1998 vendor correspondence itself is not public.

---

## 73.9 — [BeEF: The Browser Exploitation Framework](https://github.com/beefproject/beef) [Project](https://beefproject.com/) — Wade Alcorn and contributors

**REMOVED** · Tooling or methodology contribution · confidence Low

### Core contribution

BeEF turns a browser hooked through injected JavaScript into a managed, modular testing
beachhead: an operator can enumerate victims and run targeted information-gathering,
social-engineering, network-discovery and exploitation modules through a control plane.

### Prior art

- Anton Rager's [XSS-Proxy announcement (2005)](https://seclists.org/webappsec/2005/q1/295)
  already demonstrated persistent, bidirectional browser command and control.
- BeEF's marginal contribution is productizing that concept as an extensible framework
  with victim management and reusable modules; its continued use supports lasting value.
- The current project carries a 2006 copyright and later bibliographies cite “BeEF,
  2006,” but another historical account places its inception/first public release in
  2005. No authoritative dated first release was recovered.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 48 | 25% | 12.00 | Major framework extension, but XSS browser C2 already existed. |
| Transferability | 82 | 20% | 16.40 | Modular across browsers, targets and client-side techniques. |
| Lasting value | 90 | 20% | 18.00 | Still maintained and widely used. |
| Technical soundness | 75 | 15% | 11.25 | Working open-source implementation. |
| Practical usability | 88 | 10% | 8.80 | Substantially operationalizes browser exploitation. |
| Clarity and reproducibility | 74 | 10% | 7.40 | Source and current documentation exist; 2006 artifact is missing. |

**Final score: 73.9/100**

### Verdict

- **Archive decision:** Include as a core technique
- **Confidence:** Low
- **Reasoning:** It clears the research-value gate but is not added to `2006.md`
  because genuinely first-published in 2006 is a mandatory independent gate and the
  surviving date evidence conflicts.
- **Evidence gaps:** A dated 2005/2006 release tarball, announcement, or Wayback capture
  would resolve the year.

---

## 73.3 — [SQL Injections by Truncation](https://www.blackhat.com/presentations/bh-usa-06/BH-US-06-Neerumalla.pdf) — Bala Neerumalla, Microsoft

**KEPT** · Original technique · confidence High

### Core contribution

The Black Hat USA 2006 deck shows that code can correctly quote attacker-controlled SQL
input and still become injectable when the escaped result or completed dynamic statement
is silently truncated. Carefully sized input discards the closing quote or trailing
constraints, converting a nominal mitigation into attacker-controlled syntax.

### Prior art

- Classic SQL injection and quote escaping were established well before 2006; 2005
  parse-tree validation work also addressed structural query changes.
- Generic fixed-buffer truncation was known as a software flaw, but targeted searches
  found no earlier primary publication turning truncation of the *escaped output* into
  this SQL-injection bypass.
- The official deck says it covers “new vulnerabilities” and gives distinct SQL
  modification and SQL-injection variants plus remediation.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 70 | 25% | 17.50 | New injection-bypass mechanism over established SQLi. |
| Transferability | 75 | 20% | 15.00 | General to dynamic-query builders with bounded intermediate buffers. |
| Lasting value | 73 | 20% | 14.60 | Durable audit rule: size transformed output, not raw input. |
| Technical soundness | 80 | 15% | 12.00 | Multiple worked T-SQL variants and precise mitigations. |
| Practical usability | 74 | 10% | 7.40 | Directly usable in code review and testing. |
| Clarity and reproducibility | 68 | 10% | 6.80 | Slides are concise; examples are sufficient though speaker detail is absent. |

**Final score: 73.3/100**

### Verdict

- **Archive decision:** Include as a core technique
- **Confidence:** High
- **Reasoning:** This is not merely another SQLi target; it identifies how a safety
  transform and downstream buffer interact to recreate syntax control.
- **Evidence gaps:** No transcript was located, so some code hidden in slide images is
  less accessible through text extraction.

---

## 67.5 — [Ajax (in)security](https://www.blackhat.com/presentations/bh-usa-06/BH-US-06-Hoffman.pdf) — Billy Hoffman, SPI Dynamics

**KEPT** · Meaningful extension · confidence High

### Core contribution

The August 2006 deck reframes AJAX bridges as security principals: a same-origin server
proxy can carry the application's partner credentials, quota and network position, so an
attacker can use it to dump third-party data, relay injection, hide attribution or induce
blocking. It also supplies a practical method for extracting an AJAX application's API
attack surface from exposed functions.

### Prior art

- XSS, blind SQL injection, open proxies and the Samy AJAX worm predate the talk.
- [XSS-Proxy (2005)](https://seclists.org/webappsec/2005/q1/295) used a victim browser
  as C2, but did not analyze server-side AJAX bridge trust and transformation layers.
- Later 2006 AJAX work overlaps the broader enumeration theme; Hoffman's bridge threat
  model is the distinct contribution scored here.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 55 | 25% | 13.75 | Meaningful trust-boundary extension built from known primitives. |
| Transferability | 76 | 20% | 15.20 | Applies to many mashup proxies and integration gateways. |
| Lasting value | 70 | 20% | 14.00 | Anticipates recurring server-side proxy/credential abuse. |
| Technical soundness | 72 | 15% | 10.80 | Clear causal model and attack examples. |
| Practical usability | 68 | 10% | 6.80 | Useful review/test checklist without a released scanner. |
| Clarity and reproducibility | 70 | 10% | 7.00 | Detailed 58-slide primary deck. |

**Final score: 67.5/100**

### Verdict

- **Archive decision:** Include as a supporting reference
- **Confidence:** High
- **Reasoning:** Known attacks gain a distinct capability when relayed through a
  privilege-bearing bridge; that transfer of trust clears the historical 60 gate.
- **Evidence gaps:** The deck does not measure how common vulnerable bridges were.

---

## 65.7 — [Breaking AJAX Web Applications: Vulns 2.0 in Web 2.0](https://www.blackhat.com/presentations/bh-jp-06/BH-JP-06-Stamos-Lackey.pdf) — Alex Stamos and Zane Lackey, iSEC Partners

**KEPT** · Tooling or methodology contribution · confidence High

### Core contribution

The October 2006 deck gives a repeatable AJAX assessment method: fingerprint the
framework from client scripts, enumerate generated RPC methods, mutate richer upstream
calls, test downstream JavaScript/JSON serialization contexts, and assess two-way XSRF
through dynamic script nodes. It applies the method to DWR, Microsoft Atlas and GWT.

### Prior art

- Jesse Burns's 2005 XSRF paper and HTML form/image request forgery are explicitly
  credited; XSS and parameter tampering are older still.
- Hoffman's August 2006 deck already argued that exposed AJAX functions expand the
  attack surface.
- The marginal contribution is systematic framework fingerprinting/RPC enumeration,
  serialized-response testing, two-way XSRF analysis and comparative framework evidence.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 48 | 25% | 12.00 | Mostly known classes, reorganized into a new AJAX methodology. |
| Transferability | 74 | 20% | 14.80 | Works across multiple RPC/serialization frameworks. |
| Lasting value | 68 | 20% | 13.60 | Client-exposed API discovery remains a testing pattern. |
| Technical soundness | 74 | 15% | 11.10 | Concrete traffic, framework cases and limitations. |
| Practical usability | 70 | 10% | 7.00 | Immediately usable manual assessment workflow. |
| Clarity and reproducibility | 72 | 10% | 7.20 | Detailed examples across three frameworks. |

**Final score: 65.7/100**

### Verdict

- **Archive decision:** Include as a supporting reference
- **Confidence:** High
- **Reasoning:** It does not invent XSS or CSRF, but systematizes how to discover and
  test their new RPC/serialization surfaces in AJAX frameworks.
- **Evidence gaps:** The advertised released attack framework was not recovered, so
  this score rests on the deck's reproducible manual method.

---

## 63.9 — [Self-contained XSS Attacks](https://www.gnucitizen.org/blog/self-contained-xss-attacks/) — Petko D. Petkov

**KEPT** · Meaningful combination or adaptation · confidence Medium

### Core contribution

The September 2006 post weaponizes `data:` URLs as single-link active documents. An
attacker can embed HTML, JavaScript or even binary document payloads entirely in the URL,
making the payload portable, independent of attacker hosting, and useful against filters
or redirectors that validate hosts but not schemes.

### Prior art

- [RFC 2397 (1998)](https://www.rfc-editor.org/rfc/rfc2397) standardized `data:` URLs;
  JavaScript URLs and ordinary reflected XSS were also long known.
- The post does not discover the scheme. Its distinct contribution is the security
  composition: use executable media types and Base64 to carry a complete active document
  or secondary exploit in a link, with worked browser examples.
- Later commentary correctly notes this is a payload form, not a new server-side XSS
  vulnerability class; the verdict is therefore adaptation, not original technique.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 50 | 25% | 12.50 | Security adaptation of a known URL scheme. |
| Transferability | 75 | 20% | 15.00 | Cross-cutting wherever URLs are accepted or redirected. |
| Lasting value | 60 | 20% | 12.00 | Scheme validation and active data URLs remain relevant lessons. |
| Technical soundness | 68 | 15% | 10.20 | Mechanism and limitations are substantially correct. |
| Practical usability | 72 | 10% | 7.20 | Directly testable with compact payloads. |
| Clarity and reproducibility | 70 | 10% | 7.00 | Clear syntax and examples. |

**Final score: 63.9/100**

### Verdict

- **Archive decision:** Include as a supporting reference
- **Confidence:** Medium
- **Reasoning:** It clears the broad historical gate as a meaningful, reusable
  adaptation, while avoiding the source's overstatement that it is a new XSS class.
- **Evidence gaps:** Browser origin treatment varied in 2006, and the post does not
  give a complete browser/version matrix.

---

## 55.8 — [AttackAPI](https://www.gnucitizen.org/blog/attackapi/) [2.0 announcement](https://seclists.org/pen-test/2006/Nov/173) — Petko D. Petkov

**REMOVED** · Tooling or methodology contribution · confidence Medium

### Core contribution

AttackAPI packages reusable JavaScript routines for composing browser and web attack
vectors and supplied demonstrations and a channel component for client-side research.

### Prior art

- [XSS-Proxy (2005)](https://seclists.org/webappsec/2005/q1/295) already provided
  persistent, remotely controlled browser exploitation.
- BeEF was a contemporary modular framework. AttackAPI's distinction is a lightweight
  programmer-facing JavaScript library, not a new browser-control primitive.
- The current primary post calls the project a placeholder and its historical source and
  documentation links no longer provide a complete artifact.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 45 | 25% | 11.25 | Useful library abstraction over known browser-attack primitives. |
| Transferability | 70 | 20% | 14.00 | Generic client/server routines. |
| Lasting value | 55 | 20% | 11.00 | Influential in its era but superseded and no longer maintained. |
| Technical soundness | 60 | 15% | 9.00 | Contemporary release evidence, incomplete surviving code. |
| Practical usability | 65 | 10% | 6.50 | Originally usable and extensible. |
| Clarity and reproducibility | 40 | 10% | 4.00 | Primary post is too thin for full reconstruction. |

**Final score: 55.8/100**

### Verdict

- **Archive decision:** Include as a supporting reference
- **Confidence:** Medium
- **Reasoning:** Worth retaining as period tooling history, but it does not clear the
  ≥60 curated-list gate.
- **Evidence gaps:** Historical SVN tags and full documentation were not recovered.

---

## 55.4 — [Google Search API Worms](https://www.gnucitizen.org/blog/google-search-api-worms/) — Petko D. Petkov

**REMOVED** · Meaningful combination or adaptation · confidence Medium

### Core contribution

The September 2006 post shows browser malware using a search API to discover vulnerable
sites, then blind image/form requests to inject its own script and continue propagation.

### Prior art

- The Santy worm used search engines to locate and exploit phpBB targets in 2004.
- The [Samy technical explanation (2005)](https://samy.pl/myspace/tech.html) established
  self-propagating XSS/AJAX malware within one social network.
- The candidate moves search-driven propagation into browser JavaScript and cross-origin
  blind requests, but combines two already-public worm patterns and remains partly
  hypothetical.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 38 | 25% | 9.50 | Incremental browser-side combination of known worm mechanisms. |
| Transferability | 68 | 20% | 13.60 | Applies to searchable classes of GET/POST-injectable sites. |
| Lasting value | 56 | 20% | 11.20 | Useful web-worm design pattern, limited later influence. |
| Technical soundness | 58 | 15% | 8.70 | Plausible code path, but no deployed end-to-end worm. |
| Practical usability | 60 | 10% | 6.00 | Concrete search and infection snippets. |
| Clarity and reproducibility | 64 | 10% | 6.40 | Mechanism is clear, target-specific pieces omitted. |

**Final score: 55.4/100**

### Verdict

- **Archive decision:** Include as a supporting reference
- **Confidence:** Medium
- **Reasoning:** A credible period lead, but the marginal novelty does not reach 60.
- **Evidence gaps:** No contemporary in-the-wild implementation was found.

---

## 46.2 — [Hacking Intranets Via Brute Force](http://ha.ckers.org/blog/20061228/hacking-intranets-via-brute-force/) — Robert Hansen

**REMOVED** · Useful application or case study · confidence High

### Core contribution

The December 2006 post enumerates common `internal`/`intranet` DNS names across popular
domains, identifies externally resolvable internal services, derives likely enterprise
usernames from public email addresses, and proposes direct password brute force.

### Prior art

- Browser-based intranet port scanning and blind fingerprinting were already presented
  and nominated in 2006.
- Public DNS enumeration, username harvesting and password brute force are all older
  techniques. This post's contribution is measurement and workflow composition, not a
  new primitive.
- The entry later appeared in the 2007 nomination file, but its actual publication date
  is 28 December 2006.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 25 | 25% | 6.25 | Familiar recon and brute-force steps. |
| Transferability | 55 | 20% | 11.00 | Reusable across organizations with exposed names/services. |
| Lasting value | 42 | 20% | 8.40 | Solid period datapoint, limited methodological novelty. |
| Technical soundness | 62 | 15% | 9.30 | Concrete Alexa-500 enumeration supports the premise. |
| Practical usability | 55 | 10% | 5.50 | Actionable but noisy and dependent on weak authentication. |
| Clarity and reproducibility | 58 | 10% | 5.80 | Workflow and examples are clear; collection script absent. |

**Final score: 46.2/100**

### Verdict

- **Archive decision:** Do not include
- **Confidence:** High
- **Reasoning:** Useful case study, but below the gate because the component techniques
  and their combination were already routine.
- **Evidence gaps:** None material to the novelty verdict.
