# 2008 candidate judgements

These scorecards apply the repository's weighted judge rubric. `KEPT` means the
candidate met the historical 60-or-above inclusion rule as well as the
first-publication, originality-verdict and original-nomination exclusions.

## 93.7 — [Creating a Rogue CA Certificate](http://www.phreedom.org/research/rogue-ca/) — Alexander Sotirov, Marc Stevens, Jacob Appelbaum, Arjen Lenstra, David Molnar, Dag Arne Osvik, Benne de Weger

**KEPT** · Meaningful combination or adaptation · confidence High

### Candidate

The researchers' primary disclosure is dated 30 December 2008 and documents
the 25C3 presentation and live demonstration that day. The 2008 nominations
post did not open until 26 January 2009 and accepted additions into February,
so there was no cutoff that made this late-December work ineligible.

### Core contribution

The team predicts RapidSSL certificate fields, constructs a chosen-prefix MD5
collision between a benign end-entity request and a malicious intermediate-CA
certificate, obtains the CA's legitimate signature on the benign half, and
transfers that signature to the rogue CA. The resulting trusted intermediate
can issue certificates for any web site.

### Prior art

Practical MD5 collisions, colliding X.509 certificates and chosen-prefix
collision algorithms all predate this disclosure. Earlier work warned of rogue
certificate scenarios. The qualifying advance is the first demonstrated
end-to-end combination against a commercial CA: predicted serial and validity
fields, collision construction, real issuance and browser-trusted delegation.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 88 | 25% | 22.00 | First practical rogue-CA construction from known cryptographic pieces. |
| Transferability | 96 | 20% | 19.20 | Compromises the shared browser PKI trust model, not one site. |
| Lasting value | 96 | 20% | 19.20 | Drove retirement of MD5 certificate issuance and remains canonical. |
| Technical soundness | 98 | 15% | 14.70 | Real CA issuance, certificate chain and live browser demonstration. |
| Practical usability | 92 | 10% | 9.20 | End-to-end attack was executed with commodity trust stores. |
| Clarity and reproducibility | 94 | 10% | 9.40 | Primary disclosure precisely documents constraints, process and artifacts. |

**Final score: 93.7/100.** Archive decision: include as a core technique.

### Verdict

Meaningful combination or adaptation. The cryptographic primitives were known,
but their engineered combination into a browser-trusted rogue CA is a distinct
and exceptionally consequential 2008 technique. It remains untouched in the
official 2009 ranking; that cross-year placement is historical evidence, not a
reason to assign the technique's first-publication year to 2009.

## 85.6 — [Securing Frame Communication in Browsers](https://www.usenix.org/legacy/event/sec08/tech/full_papers/barth/barth_html/index.html) — Adam Barth, Collin Jackson, John C. Mitchell

**KEPT** · Meaningful extension · confidence High

### Candidate

USENIX Security 2008 paper, published July 2008. The full primary paper and
conference record establish the date, authorship, attacks and browser changes.

### Core contribution

The qualifying 2008 contribution is the cross-frame messaging confidentiality
race: a recipient window can be navigated between sender checks and delivery,
leaking the message to a new origin. The paper's `postMessage` target-origin
control closes that race and became a lasting browser security primitive.

### Prior art

Frame spoofing dates to Guninski (1999), fragment-identifier messaging to 2006,
and Subspace/MashupOS to 2007. The authors also published their frame-hijacking
and descendant-navigation-policy work in December 2007, and that material is
already represented in the 2007 missed list. This score credits only the new
messaging race, origin authentication analysis and destination-origin binding.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 76 | 25% | 19.00 | New messaging race and binding, with navigation work excluded as 2007 prior art. |
| Transferability | 86 | 20% | 17.20 | Applies across framed applications, gadgets and mashups. |
| Lasting value | 92 | 20% | 18.40 | The policy and `postMessage` model remain foundational. |
| Technical soundness | 92 | 15% | 13.80 | Formal policy analysis plus browser implementation evidence. |
| Practical usability | 82 | 10% | 8.20 | Clear browser and application remedies. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Attacks, causes and fixes are precisely documented. |

**Final score: 85.6/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. The 2007 frame-navigation contribution is excluded; the
2008 messaging-confidentiality attack and target-origin control are the distinct
qualifying advance.

## 87.1 — [ForceHTTPS: Protecting High-Security Web Sites from Network Attacks](https://archives.iw3c2.org/www2008/papers/pdf/p525-jacksonA.pdf) — Collin Jackson, Adam Barth

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed WWW 2008 paper, published April 2008.

### Core contribution

ForceHTTPS lets a site opt into an enforceable browser policy: rewrite HTTP to
HTTPS, treat certificate errors as fatal, and block mixed content. It turns
strict transport from a user-side workaround into a deployable site-controlled
security contract and directly anticipates HSTS.

### Prior art

HTTPSSR (2007), locked same-origin proposals and GMailSecure address downgrade
and user-side enforcement. None supplies this complete site-declared policy,
browser enforcement model and deployment analysis.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 84 | 25% | 21.00 | New deployable strict-transport policy combination. |
| Transferability | 90 | 20% | 18.00 | General to HTTPS sites and browser implementations. |
| Lasting value | 96 | 20% | 19.20 | Direct conceptual precursor to HSTS. |
| Technical soundness | 88 | 15% | 13.20 | Detailed threat model, design and implementation. |
| Practical usability | 72 | 10% | 7.20 | Requires browser support but gives migration mechanics. |
| Clarity and reproducibility | 85 | 10% | 8.50 | Policy behavior and evaluation are clear. |

**Final score: 87.1/100.** Archive decision: include as a core technique.

### Verdict

Original technique. Earlier pieces existed, but the site-controlled strict
HTTPS contract is a new and historically consequential contribution.

## 86.2 — [Black Ops 2008: It's The End Of The Cache As We Know It](https://blackhat.com/presentations/bh-jp-08/bh-jp-08-Kaminsky/BlackHat-Japan-08-Kaminsky-DNS08-BlackOps.pdf) — Dan Kaminsky

**KEPT** · Meaningful extension · confidence High

### Candidate

Primary Black Hat 2008 presentation documenting the coordinated 2008 DNS cache
poisoning disclosure.

### Core contribution

Random nonexistent child labels force fresh resolver queries and remove the
usual cache TTL retry barrier. Repeated transaction-ID/source-port guesses can
then inject an authority referral and glue, escalating one answer race into
control of an entire zone.

### Prior art

DNS cache poisoning and transaction-ID guessing were longstanding, including
Bellovin's 1995 work. CERT explicitly describes poisoning as an old concept.
The new value is the reusable, high-speed retry and referral escalation method.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 76 | 25% | 19.00 | Major new exploitation method atop an old primitive. |
| Transferability | 95 | 20% | 19.00 | Broad resolver and web trust impact. |
| Lasting value | 92 | 20% | 18.40 | Changed resolver hardening and DNS threat models. |
| Technical soundness | 84 | 15% | 12.60 | Mechanics and entropy consequences are concrete. |
| Practical usability | 92 | 10% | 9.20 | Immediately operational and widely testable. |
| Clarity and reproducibility | 80 | 10% | 8.00 | Deck clearly conveys the attack sequence. |

**Final score: 86.2/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It does not invent cache poisoning, but transforms its
reliability and impact with a novel retry and zone-takeover technique.

## 84.8 — [Robust Defenses for Cross-Site Request Forgery](https://seclab.stanford.edu/websec/csrf/csrf.pdf) — Adam Barth, Collin Jackson, John C. Mitchell

**KEPT** · Original technique · confidence High

### Candidate

ACM CCS 2008 paper already present in the missed section, re-recorded here so
the 2008 judgement trail is complete.

### Core contribution

The paper develops login CSRF as a distinct threat, evaluates existing CSRF
defences, and proposes the Origin header as a privacy-preserving request-origin
signal that servers can validate.

### Prior art

CSRF and token/referer defences predate 2008. The systematic login-CSRF model
and Origin-header design are the distinct contributions.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 84 | 25% | 21.00 | Distinct login-CSRF analysis and Origin defence. |
| Transferability | 88 | 20% | 17.60 | Applies across authenticated web applications. |
| Lasting value | 88 | 20% | 17.60 | Origin validation remains central to CSRF defence. |
| Technical soundness | 86 | 15% | 12.90 | Strong threat and compatibility analysis. |
| Practical usability | 76 | 10% | 7.60 | Deployable server policy, initially browser-dependent. |
| Clarity and reproducibility | 81 | 10% | 8.10 | Attacks and defence behavior are well specified. |

**Final score: 84.8/100.** Archive decision: include as a core technique.

### Verdict

Original technique. The qualifying novelty is not CSRF itself but login CSRF
as a security class plus the Origin-header defence.

## 82.2 — [On Race Vulnerabilities in Web Applications](https://roberto.greyhats.it/pubs/dimva08-web.pdf) and [Concurrency Attacks in Web Applications](https://www.blackhat.com/presentations/bh-usa-08/Stender_Vidergar/BH_US_08_Stender_Vidergar_Concurrency_Attacks_in%20Web_Applications_Whitepaper.pdf) — Roberto Paleari et al.; Scott T. Stender, Alexander G. Vidergar

**KEPT** · Meaningful combination or adaptation · confidence High

### Candidate

Independent DIMVA and Black Hat publications from mid-2008, treated together
because both establish the web-specific technique in the same year.

### Core contribution

They adapt concurrency exploitation to web business logic: identify
transaction candidates, send parallel HTTP requests to violate quotas or state
assumptions, and detect or automate the resulting races. Tested targets include
SMS services and mainstream PHP applications.

### Prior art

TOCTOU and concurrency bugs were long known in systems software. The new value
is the systematic web-session/business-logic adaptation, black-box testing
workflow and application evidence.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 70 | 25% | 17.50 | New web-specific synthesis of a known bug class. |
| Transferability | 88 | 20% | 17.60 | General to multi-request state transitions. |
| Lasting value | 88 | 20% | 17.60 | Web race testing remains a major technique. |
| Technical soundness | 86 | 15% | 12.90 | Multiple applications, methods and concrete exploits. |
| Practical usability | 80 | 10% | 8.00 | Gives repeatable identification and testing workflows. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Strong technical detail across both publications. |

**Final score: 82.2/100.** Archive decision: include as a core technique.

### Verdict

Meaningful combination or adaptation. Generic races were old, but these works
independently established their systematic exploitation in web workflows.

## 78.2 — [Increased DNS Forgery Resistance Through 0x20-Bit Encoding](https://coeus.ece.gatech.edu/2008/10/01/DNS_Forgery/) — David Dagon, Manos Antonakakis, Paul Vixie, Tatuya Jinmei, Wenke Lee

**KEPT** · Original technique · confidence High

### Candidate

ACM CCS 2008 paper and institutional publication page dated October 2008.

### Core contribution

Resolvers randomize alphabetic case in query names and verify that authorities
echo it, extracting extra entropy from DNS's case-insensitive namespace without
breaking compatible servers. The paper measures compatibility and describes
implementation and deployment.

### Prior art

Transaction IDs, source-port randomization and DNSSEC predate this work. They do
not use QNAME case as a backward-compatible authentication signal.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78 | 25% | 19.50 | Novel practical entropy channel. |
| Transferability | 72 | 20% | 14.40 | Broad resolver use, subject to name length and compatibility. |
| Lasting value | 70 | 20% | 14.00 | Durable defence-in-depth despite stronger modern controls. |
| Technical soundness | 90 | 15% | 13.50 | Careful measurement, analysis and implementation. |
| Practical usability | 80 | 10% | 8.00 | Backward-compatible and incrementally deployable. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Algorithm and evaluation are explicit. |

**Final score: 78.2/100.** Archive decision: include as a core technique.

### Verdict

Original technique. No earlier source was found using DNS case preservation as
this resolver-side anti-forgery mechanism.

## 77.0 — [Automatic Generation of XSS and SQL Injection Attacks with Goal-Directed Model Checking](https://www.usenix.org/legacy/event/sec08/tech/full_papers/martin/martin_html/index.html) — Michael Martin, Monica S. Lam

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

USENIX Security 2008 paper, published July 2008.

### Core contribution

QED combines goal-directed static analysis with concrete model checking to
generate session-aware, multi-request XSS and SQL-injection attack sequences.
It tested 130K lines across three Java applications and emitted concrete traces
for 10 SQLi and 13 XSS findings without false-positive reports.

### Prior art

XSS, SQL injection, black-box scanners, WAVES and SecuBat all predate this work.
The contribution is the first successful model-checking workflow on real web
applications that produces executable multi-request attacks.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78 | 25% | 19.50 | New attack-generation analysis workflow. |
| Transferability | 72 | 20% | 14.40 | General method, initially constrained to Java models. |
| Lasting value | 76 | 20% | 15.20 | Influential foundation for automated exploit validation. |
| Technical soundness | 86 | 15% | 12.90 | Substantial implementation and empirical evaluation. |
| Practical usability | 66 | 10% | 6.60 | Research prototype with modelling costs. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Algorithm, goals and experiments are detailed. |

**Final score: 77.0/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. The individual vulnerability classes are
old; the qualifying novelty is concrete, goal-directed attack generation.

## 68.5 — [CookieMonster: Fully Automated Active HTTPS Cookie Hijacking](https://fscked.org/projects/cookiemonster) — Mike Perry

**KEPT** · Tooling or methodology contribution · confidence Medium

### Candidate

DEF CON 16-era project and August 2008 disclosure. The original project page is
currently unreliable, so surviving contemporary descriptions and the author's
2007 Bugtraq disclosure were used to separate primitive from tooling novelty.

### Core contribution

CookieMonster automates an active MITM workflow: inject HTTP resources for
target domains, capture cookies accepted into HTTPS sessions, and use target
configuration to turn cookie integrity failures into practical hijacking.

### Prior art

Mike Perry publicly disclosed active Gmail sidejacking in August 2007 and did
not claim the underlying cookie-injection primitive as new in 2008. The 2008
qualification is automation, targeting and an operational exploitation chain.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 45 | 25% | 11.25 | Old primitive, materially new automation. |
| Transferability | 85 | 20% | 17.00 | Applies to many mixed HTTP/HTTPS deployments. |
| Lasting value | 68 | 20% | 13.60 | Historically useful; reduced by universal HTTPS. |
| Technical soundness | 72 | 15% | 10.80 | Coherent attack chain with contemporary demonstrations. |
| Practical usability | 90 | 10% | 9.00 | Automation is the project's central strength. |
| Clarity and reproducibility | 68 | 10% | 6.80 | Original source loss limits present reproducibility. |

**Final score: 68.5/100.** Archive decision: include as a supporting reference;
the historical 60-or-above gate qualifies it for the missed list.

### Verdict

Tooling or methodology contribution. It is not credited with inventing active
cookie injection; the reusable automated exploitation workflow is the advance.

## 68.0 — [Exploitable Redirects on the Web: Identification, Prevalence, and Defense](https://www.usenix.org/event/woot08/tech/full_papers/shue/shue.pdf) — Craig A. Shue, Andrew J. Kalafut, Minaxi Gupta

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Primary WOOT 2008 paper, published July 2008.

### Core contribution

It develops heuristics to identify exploitable redirects without visiting the
destination, crawls 2.5 million pages, and measures 557,646 redirect links with
161,142 simply manipulable instances. It also gives client- and server-side
mitigations.

### Prior art

Open redirects and phishing abuse were already known. The paper claims and
supports the first systematic identification and prevalence methodology rather
than invention of the flaw.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 52 | 25% | 13.00 | New systematic method for a known vulnerability. |
| Transferability | 74 | 20% | 14.80 | Heuristics generalize across redirect implementations. |
| Lasting value | 65 | 20% | 13.00 | Open-redirect discovery remains relevant. |
| Technical soundness | 80 | 15% | 12.00 | Large crawl and measured evaluation. |
| Practical usability | 70 | 10% | 7.00 | Actionable identification and mitigation ideas. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Dataset, heuristics and limitations are clear. |

**Final score: 68.0/100.** Archive decision: include as a supporting reference;
the historical 60-or-above gate qualifies it for the missed list.

### Verdict

Tooling or methodology contribution. It systematizes discovery and measurement
of open redirects but does not claim the underlying vulnerability as new.

## 66.5 — [Cookie forcing](https://scarybeastsecurity.blogspot.com/2008/11/cookie-forcing.html) — Chris Evans

**REMOVED** · Independent rediscovery · confidence High

### Candidate

Original researcher post dated 24 November 2008.

### Core contribution

The post clearly demonstrates that an HTTP response can overwrite, plant or
delete cookies used by an HTTPS origin, enabling session manipulation, login
CSRF, denial of service and related attacks.

### Prior art

The post itself credits Filipe Almeida with finding the same issue roughly two
years earlier and notes an independent Stanford discovery. That explicit prior
art defeats the first-publication gate even though the 2008 explanation is
excellent.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 48 | 25% | 12.00 | Clear independent treatment, but explicitly predated. |
| Transferability | 80 | 20% | 16.00 | General browser cookie integrity weakness. |
| Lasting value | 70 | 20% | 14.00 | Important to HTTPS and cookie threat modelling. |
| Technical soundness | 70 | 15% | 10.50 | Mechanism and consequences are sound. |
| Practical usability | 65 | 10% | 6.50 | Reproducible but less developed than CookieMonster. |
| Clarity and reproducibility | 75 | 10% | 7.50 | Concise and technically clear. |

**Final score: 66.5/100.** Archive decision: retain as a supporting reference,
but do not add it to the year list.

### Verdict

Independent rediscovery. It passes the numeric threshold but fails the required
non-duplicate/first-publication gate.
