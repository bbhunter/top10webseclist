# 2007 research evaluations

The scores below assess each candidate's marginal contribution over prior art,
not the impact of the vulnerabilities it discusses. `KEPT` means the candidate
passes the 2007 missed-list policy (score at least 60, correct year,
non-duplicate novelty verdict); `REMOVED` means it remains only in this audit.

## 84.8 — [Heap Feng Shui in JavaScript](https://www.blackhat.com/presentations/bh-europe-07/Sotirov/Whitepaper/bh-eu-07-sotirov-WP.pdf) [Slides](https://www.blackhat.com/presentations/bh-europe-07/Sotirov/Presentation/bh-eu-07-sotirov-apr19.pdf) — Alexander Sotirov

**KEPT** · Original technique · confidence High

### Candidate

- **Publication date:** 2007-03-29, Black Hat Europe 2007.
- **Problem and method:** Makes browser heap-corruption exploitation reliable by
  using JavaScript allocations and garbage collection to arrange application
  objects precisely before triggering corruption.
- **Underlying idea:** An attacker-controlled scripting runtime can be used as a
  deterministic heap-layout API, not merely as a way to spray payload bytes.

### Prior Art

- **Earliest close work:** SkyLined's Internet Explorer heap-spraying technique,
  explicitly credited in the paper, filled broad address ranges with repeated
  shellcode but did not provide precise allocation and free control.
- **Closest equivalent:** Generic native heap grooming pre-dated this work, but
  it did not show a reusable JavaScript library that controls the shared browser
  process heap across script, DOM, and ActiveX allocations.
- **Distinct contribution:** The allocator analysis, cache-flushing "plunger"
  technique, HeapLib abstraction, and two exploit demonstrations turn unreliable
  browser corruption into controlled object replacement.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 85/100 | 25% | 21.25/25 | Introduces precise JavaScript heap grooming beyond heap spray. |
| Transferability | 75/100 | 20% | 15.00/20 | Demonstrated on IE but the allocator-control model generalises to scripted runtimes. |
| Lasting value | 88/100 | 20% | 17.60/20 | Heap grooming became a standard browser-exploitation stage and vocabulary. |
| Technical soundness | 90/100 | 15% | 13.50/15 | Detailed allocator internals, algorithms, and exploit demonstrations. |
| Practical usability | 85/100 | 10% | 8.50/10 | HeapLib exposes immediately reusable primitives. |
| Clarity and reproducibility | 90/100 | 10% | 9.00/10 | Exact layouts, code, preconditions, and case studies are supplied. |

**Final score: 84.8/100**

### Verdict

- **Archive decision:** Include as a core technique.
- **Reasoning:** This is a clear new exploitation primitive over the cited heap
  spray baseline, with high technical depth and durable influence.
- **Evidence gaps:** The original phreedom.org project page is no longer the most
  reliable live copy; the Black Hat whitepaper and slides preserve the work.

---

## 78.2 — [Exposing Private Information by Timing Web Applications](https://crypto.stanford.edu/~dabo/pubs/abstracts/webtiming.html) [Paper](https://archives.iw3c2.org/www2007/papers/paper555.pdf) — Andrew Bortz, Dan Boneh, Palash Nandy

**KEPT** · Original technique · confidence High

### Candidate

- **Publication date:** May 2007, WWW 2007.
- **Problem and method:** Recovers cross-origin private state by measuring a web
  application's response time directly or through browser-observable timing and
  response-size effects.
- **Underlying idea:** A cross-origin response need not be readable for its
  latency to disclose authenticated state selected by attacker-controlled input.

### Prior Art

- **Earliest close work:** Paul Kocher's 1996 timing attack established timing as
  a cryptographic side channel; Brumley and Boneh's 2003 work showed remote
  timing could be practical.
- **Closest equivalent:** Earlier browser history and cache probes inferred
  visited state from client-side behavior, but did not establish the paper's
  target-controlled web-application timing model.
- **Distinct contribution:** Formalises direct and cross-site web timing attacks,
  validates them against real applications, and analyses response padding and
  timing equalisation countermeasures.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 84/100 | 25% | 21.00/25 | Establishes cross-site web timing as a distinct information-leak primitive. |
| Transferability | 80/100 | 20% | 16.00/20 | Applies wherever secret-dependent web paths produce measurable latency. |
| Lasting value | 78/100 | 20% | 15.60/20 | Became a foundation for the cross-site leak research line. |
| Technical soundness | 80/100 | 15% | 12.00/15 | Provides models, measurements, and countermeasure analysis. |
| Practical usability | 70/100 | 10% | 7.00/10 | Network noise raises cost, but the tests are actionable. |
| Clarity and reproducibility | 66/100 | 10% | 6.60/10 | Sufficient method detail, though some evaluated deployments are historical. |

**Final score: 78.2/100**

### Verdict

- **Archive decision:** Include as a core technique.
- **Reasoning:** The paper moves timing attacks into the cross-origin web threat
  model with a reusable technique rather than a target-specific observation.
- **Evidence gaps:** None material. This scorecard confirms, without duplicating,
  the missed entry already added by the earlier audit.

---

## 71.5 — [The ND2DB Attack: Database Content Extraction Using Timing Attacks on the Indexing Algorithms](https://www.usenix.org/legacy/event/woot07/tech/full_papers/futoransky/futoransky.pdf) [Black Hat paper](https://www.blackhat.com/presentations/bh-usa-07/Waissbein_Futoransky_and_Saura/Whitepaper/bh-usa-07-waissbein_futoransky_and_saura-WP.pdf) — Ariel Futoransky, Damián Saura, Ariel Waissbein

**KEPT** · Original technique · confidence High

### Candidate

- **Publication date:** 2007-07-31; presented at WOOT on 2007-08-06 and Black
  Hat USA in the same week.
- **Problem and method:** Extracts values from a private indexed database column
  when an attacker can only insert or update chosen values and measure operation
  time.
- **Underlying idea:** B-tree page access and split behavior makes the physical
  index an ordering oracle for otherwise unreadable application data.

### Prior Art

- **Earliest close work:** Timing attacks against cryptographic implementations
  and remote services were established well before 2007.
- **Closest equivalent:** The WWW 2007 web-timing paper studies secret-dependent
  application response paths. ND2DB instead derives an oracle from the database
  index algorithm and chosen insertions, even without a vulnerable query.
- **Distinct contribution:** A theory and working MySQL/InnoDB experiment for
  extracting indexed values from insertion latency alone.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78/100 | 25% | 19.50/25 | Introduces an indexing-algorithm timing oracle for database extraction. |
| Transferability | 60/100 | 20% | 12.00/20 | General model, but exploitation depends on indexed chosen inserts and stable timing. |
| Lasting value | 68/100 | 20% | 13.60/20 | Durable warning that data structures can leak through web-facing operations. |
| Technical soundness | 85/100 | 15% | 12.75/15 | Algorithm, complexity, and successful MySQL measurements are given. |
| Practical usability | 55/100 | 10% | 5.50/10 | Strong preconditions and noise limit routine exploitation. |
| Clarity and reproducibility | 82/100 | 10% | 8.20/10 | The paper provides enough detail to reconstruct the oracle. |

**Final score: 71.5/100**

### Verdict

- **Archive decision:** Include as a core technique.
- **Reasoning:** This is not merely "timing against another target"; the B-tree
  insertion oracle is the new reusable mechanism.
- **Evidence gaps:** Claims about other database engines are reasoned rather than
  experimentally verified; the demonstrated result is MySQL/InnoDB.

---

## 69.3 — [Protecting Browsers from Frame Hijacking Attacks](https://seclab.stanford.edu/websec/frames/) [WebKit disclosure](https://bugs.webkit.org/show_bug.cgi?id=15936) — Adam Barth, Collin Jackson

**KEPT** · Meaningful extension · confidence High

### Candidate

- **Publication date:** December 2007; the WebKit issue was filed 2007-11-10.
- **Problem and method:** Demonstrates that permissive frame navigation lets a
  malicious page replace framed login or gadget content while the trustworthy
  top-level address remains visible, then derives and deploys a stricter
  descendant navigation policy.
- **Underlying idea:** Same-origin read isolation is insufficient when an
  attacker can still navigate another origin's security-sensitive subframe.

### Prior Art

- **Earliest credible work:** Georgi Guninski reported cross-window frame
  navigation password theft in 1999; Mozilla responded with a window policy in
  2001. The authors explicitly preserve that attribution in their later full
  paper.
- **Closest equivalent:** The old cross-window attack replaced a framed login
  from a separate window. The 2007 work studies contemporary policies, Flash
  circumvention, same-window/gadget cases, and site exposure.
- **Distinct contribution:** Systematic navigation-policy analysis, new modern
  cases, a compatibility-aware descendant policy, and fixes shipped in browsers.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 46/100 | 25% | 11.50/25 | Extends a 1999 primitive rather than originating frame navigation abuse. |
| Transferability | 76/100 | 20% | 15.20/20 | Applies to framed login, payment, and mashup designs across browsers. |
| Lasting value | 80/100 | 20% | 16.00/20 | Helped establish modern frame navigation isolation. |
| Technical soundness | 80/100 | 15% | 12.00/15 | Browser-policy comparison, real sites, and vendor fixes support the claims. |
| Practical usability | 70/100 | 10% | 7.00/10 | Demonstrations and concrete policy make the result actionable. |
| Clarity and reproducibility | 76/100 | 10% | 7.60/10 | The research page, bug, and later full paper preserve the method. |

**Final score: 69.3/100**

### Verdict

- **Archive decision:** Include as a supporting reference.
- **Reasoning:** Prior art prevents an Original verdict, but the expanded threat
  model and deployed policy are a meaningful extension, not a rediscovery.
- **Evidence gaps:** The compact December 2007 artifact was later expanded for
  USENIX Security 2008; only the material demonstrably disclosed in 2007 is
  credited here.

---

## 68.2 — [JavaScript Hijacking](https://seclists.org/securecoding/2007/q2/0) [Whitepaper](https://img2.helpnetsecurity.com/dl/articles/JavaScript_Hijacking.pdf) — Brian Chess, Yekaterina Tsipenyuk O'Neil, Jacob West

**KEPT** · Meaningful extension · confidence High

### Candidate

- **Publication date:** Whitepaper dated 2007-03-12; public announcement
  2007-04-01.
- **Problem and method:** Shows how an attacker origin can load authenticated
  JavaScript/JSON through a script tag and intercept sensitive data by replacing
  language constructors, then surveys twelve AJAX frameworks and mitigations.
- **Underlying idea:** Cross-origin script inclusion plus ambient cookies turns
  executable data formats into read-capable CSRF.

### Prior Art

- **Earliest close work:** Jeremiah Grossman's 2006 Gmail/JavaScript object
  overwriting demonstration and Di Paola and Fedon's [Subverting AJAX](https://fahrplan.events.ccc.de/congress/2006/Fahrplan/events/1602.en.html)
  disclosed prototype hijacking at 23C3 in December 2006.
- **Closest equivalent:** Those demonstrations contain the underlying object or
  prototype interception primitive. Grossman's contemporary review explicitly
  said the attack itself was not new.
- **Distinct contribution:** Names and systematises the class, tests twelve major
  AJAX frameworks, defines vulnerable response conditions, and gives a coherent
  two-part mitigation strategy.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 43/100 | 25% | 10.75/25 | The core interception primitive was public in 2006. |
| Transferability | 80/100 | 20% | 16.00/20 | The vulnerable design pattern spans frameworks and custom AJAX endpoints. |
| Lasting value | 65/100 | 20% | 13.00/20 | The systematisation informed JSON response hardening for years. |
| Technical soundness | 80/100 | 15% | 12.00/15 | Clear browser mechanism and framework evidence. |
| Practical usability | 80/100 | 10% | 8.00/10 | Simple attack conditions and concrete mitigations. |
| Clarity and reproducibility | 85/100 | 10% | 8.50/10 | Payloads, affected patterns, and defenses are explicit. |

**Final score: 68.2/100**

### Verdict

- **Archive decision:** Include as a supporting reference.
- **Reasoning:** It cannot be credited as the original JSON-hijacking primitive,
  but its framework-wide evaluation and durable systematisation are a meaningful
  extension over the 2006 demonstrations.
- **Evidence gaps:** Some original 2006 blog artifacts survive only indirectly;
  the 23C3 primary event page and the candidate's contemporary peer-review thread
  are sufficient to establish precedence.

---

## 67.7 — [The Ghost in the Browser: Analysis of Web-based Malware](https://www.usenix.org/conference/hotbots-07/ghost-browser-analysis-web-based-malware) [Paper](https://www.usenix.org/legacy/event/hotbots07/tech/full_papers/provos/provos.pdf) — Niels Provos, Dean McNamee, Panayiotis Mavrommatis, Ke Wang, Nagendra Modadugu

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

- **Publication date:** April 2007, HotBots 2007.
- **Problem and method:** Uses a large web crawl and instrumented analysis
  pipeline to identify drive-by-download pages, reconstruct exploit chains, and
  measure how malicious content reaches users through compromised sites and ads.
- **Underlying idea:** Web malware can be studied as an ecosystem by joining
  large-scale crawling, active-content execution, and redirection-chain analysis.

### Prior Art

- **Earliest close work:** Microsoft's 2005 Strider HoneyMonkey automated visits
  to exploit sites in vulnerable browsers; the authors also cite earlier crawler
  measurements of drive-by downloads.
- **Closest equivalent:** Client honeypots detected whether a page compromised a
  browser. The candidate broadens this into an operational measurement method for
  infection prevalence, landing pages, exploit servers, and distribution paths.
- **Distinct contribution:** Large-scale ecosystem analysis and a repeatable way
  to connect compromised web pages to exploit infrastructure.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 50/100 | 25% | 12.50/25 | Extends client-honeypot crawling into ecosystem analysis. |
| Transferability | 70/100 | 20% | 14.00/20 | The pipeline generalises to web malware campaigns and redirect networks. |
| Lasting value | 72/100 | 20% | 14.40/20 | Established an influential measurement model for drive-by malware. |
| Technical soundness | 85/100 | 15% | 12.75/15 | Large dataset, explicit pipeline, and careful empirical analysis. |
| Practical usability | 60/100 | 10% | 6.00/10 | Requires substantial crawling infrastructure but is operationally useful. |
| Clarity and reproducibility | 80/100 | 10% | 8.00/10 | Method and limitations are well documented. |

**Final score: 67.7/100**

### Verdict

- **Archive decision:** Include as a supporting reference.
- **Reasoning:** The detector is not a new attack, but the web-malware ecosystem
  measurement methodology is distinct, rigorous, and lasting.
- **Evidence gaps:** Google's complete internal corpus and infrastructure are not
  reproducible by an independent researcher at the reported scale.

---

## 66.5 — [CaffeineMonkey: Automated Collection, Detection and Analysis of Malicious JavaScript](https://blackhat.com/presentations/bh-usa-07/Feinstein_and_Peck/Presentation/bh-usa-07-feinstein_and_peck.pdf) — Ben Feinstein, Daniel Peck

**KEPT** · Tooling or methodology contribution · confidence Medium

### Candidate

- **Publication date:** 2007-08-02, Black Hat USA 2007.
- **Problem and method:** Instruments Mozilla's standalone SpiderMonkey engine,
  supplies browser-like objects, and distributes collection to execute,
  deobfuscate, classify, and compare malicious JavaScript at scale.
- **Underlying idea:** Observe runtime values at the scripting-engine boundary so
  layers of `eval`, string decoding, and document writes reveal the final payload
  without requiring signatures for each obfuscator.

### Prior Art

- **Earliest close work:** Client honeypots such as Strider HoneyMonkey (2005)
  executed full pages in browsers or VMs to find exploitation.
- **Closest equivalent:** Execution-based web-malware systems observed system
  compromise. CaffeineMonkey focuses on script-level instrumentation and
  normalized payload analysis across a distributed collection network.
- **Distinct contribution:** A practical instrumented-runtime workflow for
  recovering and clustering obfuscated malicious JavaScript.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 55/100 | 25% | 13.75/25 | Meaningful script-level analysis extension to established client honeypots. |
| Transferability | 75/100 | 20% | 15.00/20 | Runtime interception applies across many JavaScript packers and payloads. |
| Lasting value | 65/100 | 20% | 13.00/20 | Dynamic deobfuscation remained a useful malware-analysis pattern. |
| Technical soundness | 72/100 | 15% | 10.80/15 | Architecture and deployed findings support the approach. |
| Practical usability | 70/100 | 10% | 7.00/10 | Tool-driven workflow lowers analyst effort. |
| Clarity and reproducibility | 70/100 | 10% | 7.00/10 | Slides expose the design, though old dependencies hinder reproduction. |

**Final score: 66.5/100**

### Verdict

- **Archive decision:** Include as a supporting reference.
- **Reasoning:** The marginal value is the instrumented JavaScript analysis
  method, not the already-known fact that browser scripts deliver malware.
- **Evidence gaps:** The original SecureWorks tool download is no longer a stable
  live source, reducing present-day reproducibility and confidence one level.

---

## 64.8 — [An Analysis of Browser Domain-Isolation Bugs and a Light-Weight Transparent Defense Mechanism](https://www.microsoft.com/en-us/research/?p=153771) [Paper](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ScriptAccenting.pdf) — Shuo Chen, David Ross, Yi-Min Wang

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

- **Publication date:** October 2007, ACM CCS 2007.
- **Problem and method:** Systematically analyses heterogeneous browser
  same-origin isolation failures and prototypes "script accenting," which tags
  scripts and object names with origin-specific accents to block interference.
- **Underlying idea:** Instead of relying on every complex browser path to apply
  isolation correctly, encode origin identity into the objects and names that
  cross those paths.

### Prior Art

- **Earliest close work:** Numerous browser SOP bypasses and universal-XSS bugs
  were public before 2007, including several represented in the year's original
  nominations.
- **Closest equivalent:** Individual bug reports fixed isolated navigation,
  aliasing, event, or component-interaction mistakes. They did not provide this
  cross-case taxonomy and origin-accent enforcement primitive.
- **Distinct contribution:** A mechanism-focused isolation-bug study and a
  working transparent defense evaluated against known attacks.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 45/100 | 25% | 11.25/25 | Individual attacks were known; the taxonomy and accenting defense are new. |
| Transferability | 72/100 | 20% | 14.40/20 | Addresses a broad browser-origin enforcement problem. |
| Lasting value | 68/100 | 20% | 13.60/20 | Durable methodology for reasoning about isolation failures. |
| Technical soundness | 82/100 | 15% | 12.30/15 | Formal motivation, IE prototype, attack tests, and performance evaluation. |
| Practical usability | 55/100 | 10% | 5.50/10 | Browser-engine adoption is required; testers mainly gain the taxonomy. |
| Clarity and reproducibility | 78/100 | 10% | 7.80/10 | Mechanism and evaluation are documented in depth. |

**Final score: 64.8/100**

### Verdict

- **Archive decision:** Include as a supporting reference.
- **Reasoning:** This does not re-add the nominated browser bugs. It preserves a
  distinct analysis and defense methodology built from them.
- **Evidence gaps:** The prototype targets the contemporary Internet Explorer
  architecture, so deployment portability was argued rather than demonstrated.

---

## 64.5 — [Transaction Generators: Root Kits for Web](https://www.usenix.org/conference/hotsec-07/transaction-generators-root-kits-web) [Paper](https://www.usenix.org/legacy/event/hotsec07/tech/full_papers/jackson/jackson.pdf) — Collin Jackson, Dan Boneh, John C. Mitchell

**KEPT** · Meaningful combination or adaptation · confidence High

### Candidate

- **Publication date:** August 2007, HotSec 2007; an earlier Stanford workshop
  presentation is dated 2007-03-19.
- **Problem and method:** Models malware inside a browser that waits for a user to
  authenticate, then issues and hides fraudulent transactions in the legitimate
  session, bypassing stronger login authentication and risk analytics.
- **Underlying idea:** Authentication integrity does not imply transaction
  integrity when client-resident code can act after authentication and rewrite
  the user's view.

### Prior Art

- **Earliest close work:** The paper itself cites 2006 reports of banking trojans
  performing account transactions, and malicious browser extensions already had
  access to session state.
- **Closest equivalent:** CSRF generates authenticated requests but is defeated
  server-side with request tokens. A client-resident transaction generator sees
  those tokens, uses the normal IP and session, and can hide the resulting UI.
- **Distinct contribution:** Unifies observed malware behavior into a transaction
  integrity threat model, documents stealth variants, and prototypes trusted
  confirmation with SpyBlock.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 50/100 | 25% | 12.50/25 | Existing trojans supply precedence; the integrity model and combination are distinct. |
| Transferability | 72/100 | 20% | 14.40/20 | Applies across authenticated banking, retail, and identity systems. |
| Lasting value | 65/100 | 20% | 13.00/20 | Transaction confirmation remains relevant beyond stronger login factors. |
| Technical soundness | 75/100 | 15% | 11.25/15 | Threat analysis and prototype support the argument. |
| Practical usability | 58/100 | 10% | 5.80/10 | Attack requires client compromise; defense requires a trusted path. |
| Clarity and reproducibility | 76/100 | 10% | 7.60/10 | Short paper clearly defines attack, stealth, and defense. |

**Final score: 64.5/100**

### Verdict

- **Archive decision:** Include as a supporting reference.
- **Reasoning:** Not the first malware to transact from a victim machine, but a
  meaningful combination and durable reframing from authentication to transaction
  integrity.
- **Evidence gaps:** The paper anticipates growth from a small observed sample;
  prevalence is not part of this novelty score.

---

## 58.1 — [A Taxonomy of Attacks against XML Digital Signatures & Encryption](https://blackhat.com/presentations/bh-usa-07/Hill/Whitepaper/bh-usa-07-hill-WP.pdf) [Slides](https://www.blackhat.com/presentations/bh-usa-07/Hill/Presentation/bh-usa-07-hill.pdf) — Brad Hill

**REMOVED** · Tooling or methodology contribution · confidence Medium

### Candidate

- **Publication date:** 2007-08-02, Black Hat USA 2007.
- **Problem and method:** Enumerates XML Signature and Encryption attack surfaces,
  canonicalisation and transform abuse, reference indirection, denial of service,
  and implementation failure modes for web-service and SAML assessments.
- **Underlying idea:** Complex message-security processing creates multiple views
  and attacker-controlled transformations that must be constrained end to end.

### Prior Art

- **Earliest close work:** XML entity-expansion denial of service and canonical
  representation problems pre-date 2007; McIntosh and Austel described XML
  Signature wrapping in 2005.
- **Closest equivalent:** Existing XML-signature attacks already supplied the
  main primitives catalogued here.
- **Distinct contribution:** A compact practitioner taxonomy and assessment aid,
  plus contemporary implementation observations, rather than a clearly isolated
  new technique.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 40/100 | 25% | 10.00/25 | Primarily organises attacks that were already public. |
| Transferability | 68/100 | 20% | 13.60/20 | Useful across XML Signature, Encryption, SAML, and SOAP implementations. |
| Lasting value | 60/100 | 20% | 12.00/20 | The multiple-view warning endured, though later work systematised it more rigorously. |
| Technical soundness | 70/100 | 15% | 10.50/15 | Technically informed taxonomy with primary specifications and references. |
| Practical usability | 50/100 | 10% | 5.00/10 | Helps review but is not a complete scanner or reproduction corpus. |
| Clarity and reproducibility | 70/100 | 10% | 7.00/10 | Clear enumeration, with uneven proof depth across items. |

**Final score: 58.1/100**

### Verdict

- **Archive decision:** Include as a supporting reference.
- **Reasoning:** Useful methodology, but below the historical list gate because
  its marginal contribution is mainly taxonomy over known attacks.
- **Evidence gaps:** The presentation abstract claims several critical design
  flaws, but the surviving materials do not cleanly separate every claimed new
  case from older XML-signature work.

---

## 55.8 — [The Little Hybrid Web Worm that Could](https://www.blackhat.com/presentations/bh-usa-07/Hoffman_and_Terrill/Whitepaper/bh-usa-07-hoffman_and_terrill-WP.pdf) — Billy Hoffman, John Terrill

**REMOVED** · Meaningful combination or adaptation · confidence High

### Candidate

- **Publication date:** 2007-08-02, Black Hat USA 2007.
- **Problem and method:** Proposes a hybrid client/server web worm that crosses
  domains, mutates its source, and downloads new vulnerability information to
  update its propagation methods.
- **Underlying idea:** Combine browser and server infection stages with
  polymorphism and live exploit updates so a web worm is not tied to one site or
  one vulnerability.

### Prior Art

- **Earliest close work:** Santy (2004) used search to find and infect web
  servers; Samy (2005) demonstrated self-propagating browser-side XSS; polymorphic
  malware and updateable exploit frameworks were established concepts.
- **Closest equivalent:** Existing web worms provided each major component. The
  candidate's value is assembling the client/server, mutation, and update stages.
- **Distinct contribution:** A useful hybrid architecture and isolated demos,
  but the paper states that no fully functioning hybrid worm was built.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 48/100 | 25% | 12.00/25 | Non-obvious combination, but all major primitives had precedents. |
| Transferability | 65/100 | 20% | 13.00/20 | Architecture spans browser and server ecosystems. |
| Lasting value | 55/100 | 20% | 11.00/20 | Useful threat modelling, with limited later methodological dependence. |
| Technical soundness | 55/100 | 15% | 8.25/15 | Components were demonstrated, not the full claimed system. |
| Practical usability | 45/100 | 10% | 4.50/10 | No complete implementation and many environment-specific exploit stages. |
| Clarity and reproducibility | 70/100 | 10% | 7.00/10 | Architecture and component techniques are clearly described. |

**Final score: 55.8/100**

### Verdict

- **Archive decision:** Include as a supporting reference.
- **Reasoning:** The combination is meaningful enough to preserve, but the
  incomplete prototype and prior-art-heavy components keep it below 60.
- **Evidence gaps:** No end-to-end worm or independent reproduction validates the
  complete propagation and live-update claim.
