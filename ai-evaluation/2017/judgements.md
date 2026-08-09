# 2017 research judgements

These scorecards apply the repository's six weighted categories to calendar-year
2017 candidates that survived the exclusion, date, scope and plausibility gates.

## 88.4 — [The Wolf of Name Street: Hijacking Domains Through Their Nameservers](https://acmccs.github.io/papers/p957-vissersA.pdf) — Thomas Vissers, Timothy Barron, Tom Van Goethem, Wouter Joosen, Nick Nikiforakis

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed ACM CCS paper published in October 2017.

### Core contribution

The work identifies dangling nameserver delegation as a domain-takeover
primitive: an attacker re-registers an expired nameserver domain and thereby
controls resolution for dependent victim domains. It supplies Internet-scale
measurement, takeover demonstrations and a new lifecycle boundary distinct from
ordinary dangling host records.

### Prior art

Expired-domain residual trust and dangling DNS were known, including 2016
[Domain-Z](https://coeus.ece.gatech.edu/articles/domain-z-ieee.pdf). The new
contribution is taking over third-party domains through the authority delegated
to an expired nameserver domain, with systematic measurement of that mechanism.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | Distinct nameserver-delegation takeover primitive. |
| Transferability | 92 | 20% | 18.40 | Applies wherever domains delegate to externally owned nameservers. |
| Lasting value | 90 | 20% | 18.00 | Durable DNS lifecycle and authority-boundary lesson. |
| Technical soundness | 93 | 15% | 13.95 | Measurement and controlled takeovers support the mechanism. |
| Practical usability | 85 | 10% | 8.50 | Discovery and exploitation steps are operationally clear. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Threat model, method and validation are documented. |

**Final score: 88.4/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It exploits delegated DNS authority rather than merely
re-registering an expired content domain or dangling host record.

## 87.8 — [ASLR on the Line: Practical Cache Attacks on the MMU](https://www.ndss-symposium.org/ndss2017/ndss-2017-programme/aslrcache-practical-cache-attacks-mmu/) — Ben Gras, Kaveh Razavi, Erik Bosman, Herbert Bos, Cristiano Giuffrida

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed NDSS paper published on 27 February 2017.

### Core contribution

AnC uses cache effects from MMU page-table walks to locate virtual-address
mappings and defeat code and heap ASLR. A JavaScript implementation works from
two major browsers without a software vulnerability or privileged instruction.

### Prior art

Browser cache attacks and JavaScript timing channels were established by 2015,
including [The Spy in the Sandbox](https://dl.acm.org/doi/10.1145/2810103.2813708).
AnC is distinct in targeting cached page-table translation itself to recover
address layout across Intel, AMD and ARM systems.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 90 | 25% | 22.50 | New MMU page-table cache attack against ASLR. |
| Transferability | 85 | 20% | 17.00 | Applies across architectures and sandboxed JavaScript engines. |
| Lasting value | 90 | 20% | 18.00 | Changed assumptions about ASLR under shared caches. |
| Technical soundness | 94 | 15% | 14.10 | Cross-browser and cross-architecture experiments are rigorous. |
| Practical usability | 72 | 10% | 7.20 | Exploit construction is demanding but concretely demonstrated. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Mechanism, implementation and limitations are explicit. |

**Final score: 87.8/100.** Archive decision: include as a core technique.

### Verdict

Original technique. Existing browser cache attacks did not use MMU translation
caches as a direct address-layout oracle.

## 87.6 — [Loophole: Timing Attacks on Shared Event Loops in Chrome](https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/vila) — Pepe Vila, Boris Köpf

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2017.

### Core contribution

A spy measures delay in attacker-enqueued events to observe contention in
Chrome's shared I/O and renderer event loops. The resulting low-overhead oracle
supports page identification, user-action detection and covert communication.

### Prior art

Browser timing, cache and resource-contention channels predate 2017. Loophole's
shared FIFO event-loop oracle is a different browser scheduling primitive, not a
faster clock for an existing cache attack.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 84 | 25% | 21.00 | New shared-event-loop side-channel primitive. |
| Transferability | 90 | 20% | 18.00 | Event loops recur across browsers and event-driven systems. |
| Lasting value | 88 | 20% | 17.60 | Durable isolation and scheduler-contention insight. |
| Technical soundness | 94 | 15% | 14.10 | Two loops and several attacks validate the oracle. |
| Practical usability | 78 | 10% | 7.80 | Low-overhead browser measurement is directly usable. |
| Clarity and reproducibility | 91 | 10% | 9.10 | Attack construction and evaluation are detailed. |

**Final score: 87.6/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It turns shared event scheduling into an observation surface
that was not captured by earlier browser timing channels.

## 86.9 — [Finding and Preventing Bugs in JavaScript Bindings](https://mlfbrown.com/malicious.pdf) — Fraser Brown, Shravan Narayan, Riad S. Wahby, Dawson Engler, Ranjit Jhala, Deian Stefan

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published in May
2017.

### Core contribution

The paper systematizes exploitable type, state and failure-translation bugs at
the JavaScript-to-C++ binding boundary, builds simple static checkers, and
proposes a compatible safer API. It produces 81 proof-of-concept exploits in
Node.js and Chrome binding code.

### Prior art

Foreign-function interfaces, native-extension memory safety and runtime API
validation were established concerns. The new contribution is a binding-specific
bug taxonomy plus lightweight automated detection and prevention at Web scale.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78 | 25% | 19.50 | New binding-layer taxonomy and checkers. |
| Transferability | 88 | 20% | 17.60 | Applies across JavaScript runtimes and native binding APIs. |
| Lasting value | 89 | 20% | 17.80 | Binding boundaries remain a recurring implementation risk. |
| Technical soundness | 94 | 15% | 14.10 | 81 exploits and preventive API validate the analysis. |
| Practical usability | 88 | 10% | 8.80 | Checkers are deliberately simple and actionable. |
| Clarity and reproducibility | 91 | 10% | 9.10 | Bug patterns and analyses are precisely described. |

**Final score: 86.9/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It turns scattered runtime-boundary bugs
into a reusable offensive audit method and prevention model.

## 86.8 — [Rewriting History: Changing the Archived Web from the Present](https://acmccs.github.io/papers/p1741-lernerAT3.pdf) — Ada Lerner, Tadayoshi Kohno, Franziska Roesner

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed ACM CCS paper published in October 2017.

### Core contribution

Archived pages can execute or load present-day live resources, allowing a
current resource owner to alter what an old capture displays. The work measures
the exposure, demonstrates retroactive content changes and provides an audit
method for mutable dependencies in supposedly immutable records.

### Prior art

Web-archive replay, missing-resource fallback and live-Web dependencies were
known operational problems. This work is the first systematic security framing
and exploitation of live dependencies as present control over historical pages.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 85 | 25% | 21.25 | New retroactive Web-archive manipulation primitive. |
| Transferability | 88 | 20% | 17.60 | Applies across archives and mutable embedded resources. |
| Lasting value | 86 | 20% | 17.20 | Durable provenance and evidence-preservation lesson. |
| Technical soundness | 92 | 15% | 13.80 | Measurement and demonstrations establish the attack. |
| Practical usability | 80 | 10% | 8.00 | Resource ownership makes exploitation concrete. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Cases and measurement method are well documented. |

**Final score: 86.8/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It reveals a new temporal trust boundary between archived
documents and resources controlled on the live Web.

## 86.3 — [Fantastic Timers and Where to Find Them: High-Resolution Microarchitectural Attacks in JavaScript](https://misc0110.net/files/timers.pdf) — Michael Schwarz, Clémentine Maurice, Daniel Gruss, Stefan Mangard

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed Financial Cryptography paper published in April 2017.

### Core contribution

The authors construct high-resolution timers from shared memory, message
passing and other browser features after vendors reduced official JavaScript
clock resolution. Their timers restore microarchitectural attacks in major and
privacy-focused browsers and quantify precision gains of several orders.

### Prior art

JavaScript cache attacks and high-resolution `performance.now()` timing were
known. The contribution is a systematic set of substitute clocks that defeats
the deployed coarse-timer mitigation rather than a new cache attack itself.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 75 | 25% | 18.75 | New substitute clocks defeat timer-reduction defenses. |
| Transferability | 90 | 20% | 18.00 | Multiple timer sources work across major browsers. |
| Lasting value | 90 | 20% | 18.00 | Reframed timer removal as an incomplete defense. |
| Technical soundness | 93 | 15% | 13.95 | Precision and attacks are experimentally validated. |
| Practical usability | 84 | 10% | 8.40 | Techniques directly restore browser side-channel tooling. |
| Clarity and reproducibility | 92 | 10% | 9.20 | Implementations and comparisons are detailed. |

**Final score: 86.3/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It restores and broadens earlier microarchitectural Web
attacks under a new defensive constraint.

## 86.2 — [NEZHA: Efficient Domain-Independent Differential Testing](https://www.ieee-security.org/TC/SP2017/papers/390.pdf) — Theofilos Petsios, Adrian Tang, Salvatore Stolfo, Angelos D. Keromytis, Suman Jana

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published in May
2017.

### Core contribution

NEZHA guides input generation by maximizing delta-diversity: behavioral
asymmetries across equivalent programs. Its format-independent black- and
gray-box variants find 778 discrepancies in TLS libraries, PDF viewers and
parsers far more efficiently than prior differential tools.

### Prior art

Differential testing, Frankencerts, Mucerts and coverage-guided fuzzing were
established. NEZHA's contribution is cross-program asymmetry as the general,
domain-independent guidance signal.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 72 | 25% | 18.00 | New delta-diversity guidance for differential testing. |
| Transferability | 90 | 20% | 18.00 | Input-format-independent across many parser families. |
| Lasting value | 88 | 20% | 17.60 | Durable semantic-differential fuzzing method. |
| Technical soundness | 95 | 15% | 14.25 | Extensive comparisons and 778 discrepancies support it. |
| Practical usability | 92 | 10% | 9.20 | Open implementation substantially improves discovery rate. |
| Clarity and reproducibility | 92 | 10% | 9.20 | Algorithm, baselines and results are explicit. |

**Final score: 86.2/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It generalizes semantic-difference hunting
beyond the domain-specific generators used by prior tools.

## 86.1 — [AUTHSCOPE: Towards Automatic Discovery of Vulnerable Access Control in Online Services](https://acmccs.github.io/papers/p799-zuoA.pdf) — Chaoshun Zuo, Qingchuan Zhao, Zhiqiang Lin

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed ACM CCS paper published in October 2017.

### Core contribution

AUTHSCOPE infers the semantics and authorization dependencies of mobile-backed
online-service requests, forges authenticated variants, and automatically tests
servers for missing ownership and identity checks without source code.

### Prior art

IDOR testing, mobile API interception and 2016 AUTOFORGE predate the paper.
AUTHSCOPE adds scalable inference of authorization fields and principals rather
than focusing on cryptographically valid message mutation.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 75 | 25% | 18.75 | New automatic authorization-semantics inference. |
| Transferability | 92 | 20% | 18.40 | Applies across stateful mobile and Web service APIs. |
| Lasting value | 87 | 20% | 17.40 | Authorization automation remains a core testing challenge. |
| Technical soundness | 92 | 15% | 13.80 | System evaluation and new findings validate the method. |
| Practical usability | 88 | 10% | 8.80 | Black-box request mutation lowers manual effort. |
| Clarity and reproducibility | 89 | 10% | 8.90 | Inference and test generation are documented. |

**Final score: 86.1/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It automates semantic authorization testing,
not merely another IDOR case study.

## 85.4 — [Side-Channel Attacks on Shared Search Indexes](https://www.ieee-security.org/TC/SP2017/papers/449.pdf) — Liang Wang, Paul Grubbs, Jiahui Lu, Vincent Bindschaedler, David Cash, Thomas Ristenpart

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published in May
2017.

### Core contribution

STRESS abuses relevance scores from multi-tenant search indexes to infer index
placement, terms in other tenants' private documents, and document counts. It
turns shared TF-IDF statistics into a practical SaaS isolation failure.

### Prior art

A decade-old local-search observation noted that document frequencies could
leak. No prior work had overcome multi-index placement and filtering to extract
cross-tenant information from deployed search services.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 80 | 25% | 20.00 | First practical cross-tenant search-relevance attack. |
| Transferability | 88 | 20% | 17.60 | Applies to shared Elasticsearch, Solr and similar SaaS indexes. |
| Lasting value | 86 | 20% | 17.20 | Durable warning about filtered shared statistics. |
| Technical soundness | 92 | 15% | 13.80 | Controlled and service experiments support extraction. |
| Practical usability | 78 | 10% | 7.80 | Requires co-tenancy work but uses ordinary search APIs. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Placement and inference stages are explicit. |

**Final score: 85.4/100.** Archive decision: include as a core technique.

### Verdict

Original technique. The attack creates a practical information oracle from
shared relevance metadata that access-control filtering does not isolate.

## 85.1 — [HVLearn: Automated Black-box Analysis of Hostname Verification in SSL/TLS Implementations](http://www.cs.columbia.edu/~suman/docs/hvlearn.pdf) — Suphannee Sivakorn, George Argyros, Kexin Pei, Angelos D. Keromytis, Suman Jana

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published in May
2017.

### Core contribution

HVLearn uses active automata learning to infer the language of hostnames accepted
by a TLS implementation for certificate templates, then compares learned DFAs
against specifications and peers. It found eight unique violations with better
coverage than contemporary fuzzers.

### Prior art

Certificate fuzzing and differential validation testing were known. Treating
hostname acceptance as a learnable regular language supplies a distinct,
specification-comparable black-box method.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 70 | 25% | 17.50 | New automata-learning model for hostname verification. |
| Transferability | 92 | 20% | 18.40 | Works across languages, libraries and applications. |
| Lasting value | 88 | 20% | 17.60 | Model learning remains useful for protocol validators. |
| Technical soundness | 94 | 15% | 14.10 | Coverage comparison and confirmed flaws validate it. |
| Practical usability | 85 | 10% | 8.50 | Black-box operation avoids source and instrumentation. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Templates, inference and checks are described. |

**Final score: 85.1/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It introduces a reusable learned-language
approach to a security-critical Web identity check.

## 83.8 — [(Cross-)Browser Fingerprinting via OS and Hardware Level Features](https://www.ndss-symposium.org/ndss2017/ndss-2017-programme/cross-browser-fingerprinting-os-and-hardware-level-features/) — Yinzhi Cao, Song Li, Erik Wijmans

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed NDSS paper published on 27 February 2017.

### Core contribution

JavaScript tasks expose OS- and hardware-level graphics, CPU, audio and writing-
system features that remain stable across different browsers on one machine.
The combined fingerprint identifies 99.24% of evaluated users and crosses the
browser boundary that constrained prior fingerprints.

### Prior art

Panopticlick, canvas/audio fingerprinting and 2016 modern-browser measurements
predate this work. The qualifying advance is deliberate selection of underlying
machine features to link otherwise separate browser profiles.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 75 | 25% | 18.75 | New cross-browser OS/hardware feature construction. |
| Transferability | 92 | 20% | 18.40 | Features span browsers on common desktop systems. |
| Lasting value | 82 | 20% | 16.40 | Advanced tracking analysis beyond per-browser state. |
| Technical soundness | 90 | 15% | 13.50 | Comparative user study supports uniqueness and stability. |
| Practical usability | 79 | 10% | 7.90 | Runs through ordinary JavaScript APIs. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Features and evaluation are sufficiently detailed. |

**Final score: 83.8/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It crosses a tracking boundary that earlier browser-
specific fingerprints did not reliably bridge.

## 83.7 — [Unleashing the Walking Dead: Understanding Cross-App Remote Infections on Mobile WebViews](https://acmccs.github.io/papers/p829-liA.pdf) — Tongxin Li, Xueqiang Wang, Mingming Zha, Kai Chen, XiaoFeng Wang, Luyi Xing, Xiaolong Bai, Nan Zhang, Xinhui Han

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed ACM CCS paper published in October 2017.

### Core contribution

The paper shows how remotely supplied Web content can exploit shared or exposed
WebView state to move across application boundaries, revive vulnerable embedded
components and infect other apps. It supplies systematic detection and concrete
cross-app exploit chains.

### Prior art

WebView bridge flaws, intent abuse and vulnerable app components were known.
The new capability is remote Web content using the mobile WebView ecosystem as a
cross-application infection path rather than compromising one host app only.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | New remote cross-app WebView infection model. |
| Transferability | 84 | 20% | 16.80 | Applies to recurring embedded-Web component patterns. |
| Lasting value | 83 | 20% | 16.60 | Durable warning about shared mobile Web surfaces. |
| Technical soundness | 91 | 15% | 13.65 | Analysis and exploit chains validate the model. |
| Practical usability | 74 | 10% | 7.40 | Exploitation needs app-specific paths but is automatable. |
| Clarity and reproducibility | 87 | 10% | 8.70 | Components and infection stages are documented. |

**Final score: 83.7/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It establishes WebView-mediated remote infection across app
boundaries, beyond a conventional single-app bridge flaw.

## 83.6 — [Deemon: Detecting CSRF with Dynamic Analysis and Property Graphs](https://acmccs.github.io/papers/p1757-pellegrinoA.pdf) — Giancarlo Pellegrino, Martin Johns, Simon Koch, Michael Backes, Christian Rossow

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed ACM CCS paper published in October 2017.

### Core contribution

Deemon learns data-flow and session relationships from browser-driven execution,
represents them in a property graph, and generates CSRF tests for state-changing
requests without manually supplied specifications or source annotations.

### Prior art

CSRF scanners, dynamic tainting and workflow crawling were known. The new method
infers security-relevant session properties and mines graph patterns to recognize
state changes and missing request authenticity checks.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 68 | 25% | 17.00 | New property-graph inference for CSRF discovery. |
| Transferability | 90 | 20% | 18.00 | Applies across stateful Web workflows. |
| Lasting value | 86 | 20% | 17.20 | Durable semantic approach to business-flow testing. |
| Technical soundness | 93 | 15% | 13.95 | System and real findings validate detection. |
| Practical usability | 84 | 10% | 8.40 | Automated browser execution reduces specifications. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Graph model and test construction are explicit. |

**Final score: 83.6/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. The advance is automated semantic inference
for a known vulnerability class, not another CSRF payload.

## 82.8 — [Tail Attacks on Web Applications](https://acmccs.github.io/papers/p1725-shanAemb.pdf) — Huasong Shan, Qingyang Wang, Calton Pu

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed ACM CCS paper published in October 2017.

### Core contribution

Short bursts of legitimate expensive requests create millisecond bottlenecks in
one tier of an n-tier application, propagate queue pressure upstream and damage
tail latency while average resource use remains moderate. A feedback controller
adapts the stealthy burst parameters to system state.

### Prior art

Low-rate and application-layer DoS attacks predate 2017. Tail Attacks add the
unsaturated cross-tier millibottleneck mechanism and optimize specifically for
long-tail degradation rather than sustained exhaustion.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78 | 25% | 19.50 | New unsaturated cross-tier tail-latency attack. |
| Transferability | 86 | 20% | 17.20 | N-tier queues and expensive endpoints are widespread. |
| Lasting value | 80 | 20% | 16.00 | Useful model for stealthy application DoS. |
| Technical soundness | 90 | 15% | 13.50 | Analytical, simulated and cloud experiments agree. |
| Practical usability | 78 | 10% | 7.80 | Controller makes dynamic targeting feasible. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Model, parameters and experiments are detailed. |

**Final score: 82.8/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It attacks distributed queue dependencies and percentile
latency, a different objective and signal from established flooding attacks.

## 82.3 — [Extension Breakdown: Security Analysis of Browsers Extension Resources Control Policies](https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/sanchez-rola) — Iskander Sanchez-Rola, Igor Santos, Davide Balzarotti

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2017.

### Core contribution

The paper shows that extension resource-access controls can be bypassed through
a timing side channel against resource policy and, in Safari, through an unsafe
resource-handling pattern. The attacks enumerate installed extensions across
major browsers despite their deployed anti-fingerprinting policies.

### Prior art

Extension enumeration, fingerprinting and malicious extensions were known. The
qualifying advance is defeating browsers' resource-control policies themselves,
including a policy timing oracle and a separate Safari-specific path.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 70 | 25% | 17.50 | New bypasses of extension resource-access controls. |
| Transferability | 90 | 20% | 18.00 | Evaluated across the major browser extension systems. |
| Lasting value | 82 | 20% | 16.40 | Durable lesson about observable policy decisions. |
| Technical soundness | 90 | 15% | 13.50 | Multiple attacks and browser evaluations support it. |
| Practical usability | 82 | 10% | 8.20 | Enumeration is remotely deployable from Web content. |
| Clarity and reproducibility | 87 | 10% | 8.70 | Policies, attacks and results are documented. |

**Final score: 82.3/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It bypasses controls intended to stop an established
fingerprinting technique rather than introducing extension enumeration itself.

## 80.7 — [Same Origin Policy: Evaluation in Modern Browsers](https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/schwenk) — Jörg Schwenk, Marcus Niemietz, Christian Mainka

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2017.

### Core contribution

The authors formalize DOM same-origin checks across embedding elements, sandbox
settings and CORS, then execute 544 tests against ten browsers. They find that
23 percent of the tested cases diverge across implementations and report issues
acknowledged by Microsoft.

### Prior art

The same-origin policy and cross-browser origin quirks were longstanding. The
contribution is a systematic, executable access-control model and comparative
test suite rather than a newly invented origin-bypass primitive.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 55 | 25% | 13.75 | Systematic executable model, not a new policy concept. |
| Transferability | 94 | 20% | 18.80 | Tests cover common Web primitives and ten browsers. |
| Lasting value | 86 | 20% | 17.20 | Cross-engine access-control conformance remains important. |
| Technical soundness | 93 | 15% | 13.95 | Large comparative test matrix and confirmed issues. |
| Practical usability | 80 | 10% | 8.00 | Test cases are directly useful for browser auditing. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Model, cases and discrepancies are explicit. |

**Final score: 80.7/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It makes browser origin enforcement
systematically testable and comparable across complex embedding conditions.

## 80.3 — [PDF Mirage: Content Masking Attack Against Information-Based Online Services](https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/markwood) — Ian Markwood, Dakun Shen, Yao Liu, Zhuo Lu

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2017.

### Core contribution

PDF Mirage constructs documents whose human-visible rendering differs from the
text extracted by automated services. It demonstrates attacks against reviewer
assignment, plagiarism checks and search indexing, and proposes a lightweight
comparison-based mitigation.

### Prior art

Parser differentials, file polyglots and adversarial documents were known. This
work specifically weaponizes PDF representation differences against services
that make security- or integrity-relevant decisions from extracted content.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | New content-masking attack against document services. |
| Transferability | 78 | 20% | 15.60 | Applies to many PDF extraction and ranking pipelines. |
| Lasting value | 75 | 20% | 15.00 | Durable warning about render-versus-extract semantics. |
| Technical soundness | 88 | 15% | 13.20 | Several real service classes validate the attack. |
| Practical usability | 72 | 10% | 7.20 | Crafted files are usable but service-specific tuning helps. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Constructions and targets are well explained. |

**Final score: 80.3/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It creates a deliberate semantic split between human review
and automated content processing in online services.

## 79.5 — [Fake Co-visitation Injection Attacks to Recommender Systems](https://www.ndss-symposium.org/ndss2017/ndss-2017-programme/fake-co-visitation-injection-attacks-recommender-systems/) — Guolei Yang, Neil Zhenqiang Gong, Ying Cai

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed NDSS paper published on 27 February 2017.

### Core contribution

The attack injects optimized fake co-visitation events to make an item appear
alongside selected products or content in item-to-item recommendations. A
constrained linear optimization chooses visits under attacker limits, with
experiments covering YouTube, eBay, Amazon, Yelp and LinkedIn.

### Prior art

Shilling attacks based on fake profiles and ratings were established. This work
targets co-visitation-only recommenders where the attacker need not submit a
rating or construct the traditional fake-user profile.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78 | 25% | 19.50 | New co-visitation-only recommendation manipulation. |
| Transferability | 80 | 20% | 16.00 | Relevant to many item-to-item recommendation services. |
| Lasting value | 76 | 20% | 15.20 | Captures a durable behavioral-data poisoning risk. |
| Technical soundness | 88 | 15% | 13.20 | Optimization and multi-service evaluation support it. |
| Practical usability | 70 | 10% | 7.00 | Requires repeat visits but no privileged service access. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Threat model and optimization are documented. |

**Final score: 79.5/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It manipulates the implicit behavioral signal used by
co-visitation recommenders rather than established rating or profile inputs.

## 78.2 — [Beauty and the Burst: Remote Identification of Encrypted Video Streams](https://beautyburst.github.io/) — Roei Schuster, Vitaly Shmatikov, Eran Tromer

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed USENIX Security paper first published on 9 April 2017.

### Core contribution

The work identifies MPEG-DASH videos from segment burst patterns using a neural
classifier. It extends video identification to a remote Web attacker whose
JavaScript, such as an advertisement on a nearby machine, observes coarse shared
network contention rather than directly capturing the victim's packets.

### Prior art

Encrypted adaptive-stream title classification was demonstrated in 2016 by
*I Know What You Saw Last Minute*. This work's advance is the coarser remote
contention observer, Web delivery model and broader service-scale evaluation.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 62 | 25% | 15.50 | New observer and delivery model for a known goal. |
| Transferability | 86 | 20% | 17.20 | Applies across adaptive video services and browsers. |
| Lasting value | 78 | 20% | 15.60 | Durable traffic-analysis and shared-network lesson. |
| Technical soundness | 91 | 15% | 13.65 | Classifier and remote experiments support the claims. |
| Practical usability | 74 | 10% | 7.40 | Web deployment is easy but network conditions matter. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Features, model and evaluation are explained. |

**Final score: 78.2/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It turns an existing video-classification result into a
remote browser-delivered observation attack.

## 74.1 — [SoK: Exploiting Network Printers](https://www.ieee-security.org/TC/SP2017/program-papers.html#sok-exploiting-network-printers) — Jens Müller, Vladislav Mladenov, Juraj Somorovsky, Jörg Schwenk

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published in May
2017.

### Core contribution

The work systematizes printer attack primitives and releases the Printer
Exploitation Toolkit (PRET), evaluating twenty devices. Its Web-facing paths
include cross-site printing and spoofed printer CORS behavior that let browser
content reach devices otherwise treated as internal peripherals.

### Prior art

Printer attacks and cross-site printing had been published years earlier. The
qualifying contribution is the reusable toolkit, broad device evaluation and
systematized inclusion of browser and cloud-print attack paths.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 45 | 25% | 11.25 | Primarily systematizes and extends known printer attacks. |
| Transferability | 82 | 20% | 16.40 | Toolkit spans protocols and many printer models. |
| Lasting value | 76 | 20% | 15.20 | Durable internal-device and browser-reachability lesson. |
| Technical soundness | 90 | 15% | 13.50 | Twenty-device evaluation validates the methodology. |
| Practical usability | 88 | 10% | 8.80 | PRET makes the techniques directly operational. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Attack taxonomy and tooling are well documented. |

**Final score: 74.1/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. Its value is a reusable offensive workflow
and comparative evidence, not priority over earlier cross-site printing.

## 74.1 — [ROBOT: Return Of Bleichenbacher's Oracle Threat](https://robotattack.org/) — Hanno Böck, Juraj Somorovsky, Craig Young

**KEPT** · Meaningful extension · confidence High

### Candidate

Public research and coordinated disclosure published in December 2017.

### Core contribution

ROBOT finds modern RSA PKCS#1 v1.5 decryption oracles in widely deployed TLS
implementations by distinguishing error behavior or timing. It demonstrates
that practical private-key and session-decryption consequences remained across
contemporary servers long after the original countermeasure guidance.

### Prior art

Bleichenbacher's adaptive chosen-ciphertext attack dates to 1998 and subsequent
work adapted it to TLS. ROBOT is a large-scale practical revival with new
implementation oracles and deployment evidence, not a new cryptographic class.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 30 | 25% | 7.50 | Revival and new instances of a known attack family. |
| Transferability | 92 | 20% | 18.40 | Affected diverse products and common TLS deployments. |
| Lasting value | 88 | 20% | 17.60 | Reinforced the danger of observable crypto errors. |
| Technical soundness | 92 | 15% | 13.80 | Coordinated findings and demonstrations support it. |
| Practical usability | 78 | 10% | 7.80 | Scanning is straightforward; exploitation can be costly. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Tests, affected products and mechanics are published. |

**Final score: 74.1/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It re-establishes a known oracle attack against modern
implementations with new practical evidence and instances.

## 73.2 — [The Adventures of AV and the Leaky Sandbox](https://blackhat.com/us-17/briefings.html#the-adventures-of-av-and-the-leaky-sandbox) — Itzik Kotler, Amit Klein

**KEPT** · Original technique · confidence High

### Candidate

Black Hat USA research presented in July 2017.

### Core contribution

An attacker induces cloud-connected antivirus software to upload or inspect a
crafted local file or URL. Execution in the vendor's cloud sandbox then calls
back with encoded information, making the trusted AV service an exfiltration
relay from a restricted endpoint; the authors demonstrate the technique against
real products.

### Prior art

DNS and HTTP covert channels, cloud sandboxes and abuse of security products
were known independently. Using the endpoint AV's cloud-analysis path as a
trusted outbound relay is the distinct technique.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 75 | 25% | 18.75 | New AV-cloud exfiltration relay construction. |
| Transferability | 70 | 20% | 14.00 | Depends on product upload and sandbox behavior. |
| Lasting value | 68 | 20% | 13.60 | Useful third-party analysis trust-boundary lesson. |
| Technical soundness | 78 | 15% | 11.70 | Real-product demonstrations establish feasibility. |
| Practical usability | 76 | 10% | 7.60 | Technique is operational where cloud analysis is enabled. |
| Clarity and reproducibility | 75 | 10% | 7.50 | Presentation describes the attack and demonstrations. |

**Final score: 73.2/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It turns a defensive cloud-analysis channel into attacker-
controlled egress from the protected system.

## 72.1 — [Stealing PINs via Mobile Sensors: Actual Risk versus User Perception](https://pure.york.ac.uk/portal/en/publications/stealing-pins-via-mobile-sensors-actual-risk-versus-user-percepti/) — Maryam Mehrnezhad, Ehsan Toreini, Siamak F. Shahandashti, Feng Hao

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed International Journal of Information Security article published
in December 2017.

### Core contribution

Permissionless motion and orientation readings collected by JavaScript in a
mobile browser are used to infer a victim's PIN taps. The work combines the
browser-delivered attack with an empirical security and user-perception study.

### Prior art

Native-app sensor keystroke and PIN inference predated this work, as did 2016
browser motion-sensor fingerprinting. The advance is demonstrating the PIN
inference path through permissionless Web APIs.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 58 | 25% | 14.50 | Web delivery extends known sensor PIN inference. |
| Transferability | 78 | 20% | 15.60 | Applies to mobile browsers exposing sensor streams. |
| Lasting value | 70 | 20% | 14.00 | Durable warning about permissionless high-rate sensors. |
| Technical soundness | 84 | 15% | 12.60 | Attack and user study provide empirical support. |
| Practical usability | 70 | 10% | 7.00 | Browser delivery is simple; model accuracy is contextual. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Collection, classifier and study are described. |

**Final score: 72.1/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It ports a known mobile sensor inference class into the
permissionless browser environment.

## 70.1 — [Breaking Out HSTS (and HPKP) on Firefox, IE/Edge and (Possibly) Chrome](https://blackhat.com/archive/europe/2017/briefings.html#breaking-out-hsts) — Sheila Berta, Sergio de los Santos

**KEPT** · Meaningful extension · confidence High

### Candidate

Black Hat Europe research presented in December 2017.

### Core contribution

The researchers reverse engineer browser HSTS and HPKP state and demonstrate
remote corruption or overwrite paths in Firefox, with related Chrome findings
and analysis of IE/Edge. In affected configurations, manipulating persistent
transport-security state can restore local-network SSL stripping opportunities.

### Prior art

SSL stripping, HSTS deployment failures, clock attacks such as Delorean and
state-manipulation ideas were known. The contribution is browser-specific
storage attacks and implementation evidence rather than the underlying downgrade
goal.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 62 | 25% | 15.50 | New implementation paths to corrupt security state. |
| Transferability | 75 | 20% | 15.00 | Covers several major engines but paths are browser-specific. |
| Lasting value | 68 | 20% | 13.60 | Useful lesson about persistent browser security metadata. |
| Technical soundness | 78 | 15% | 11.70 | Reverse engineering and demonstrations support the claims. |
| Practical usability | 68 | 10% | 6.80 | Requires affected browser behavior and network position. |
| Clarity and reproducibility | 75 | 10% | 7.50 | Presentation documents mechanisms and affected browsers. |

**Final score: 70.1/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It adds concrete browser state-corruption routes to the
established HSTS downgrade and local-network attack family.

## 68.3 — [Game of Registrars: An Empirical Analysis of Post-Expiration Domain Name Takeovers](https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/lauinger) — Tobias Lauinger, Abdelberi Chaabane, Ahmet Salih Buyukkayhan, Kaan Onarlioglu, William Robertson

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2017.

### Core contribution

The study measures deletion, drop-catching and registrar pre-release behavior
that controls when expired domains become attacker-acquirable. It finds rapid
and highly competitive reuse, including same-day acquisition for roughly ten
percent of observed `.com` domains and much faster competition for `.org`.

### Prior art

Expired-domain takeover was established and 2016 Domain-Z showed residual trust
after re-registration. This paper extends the technique with operational
registrar lifecycle evidence, timing and acquisition constraints.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 35 | 25% | 8.75 | Measurement extends a known takeover mechanism. |
| Transferability | 82 | 20% | 16.40 | Registrar lifecycle applies across many domain dependencies. |
| Lasting value | 75 | 20% | 15.00 | Durable operational evidence about domain reuse. |
| Technical soundness | 90 | 15% | 13.50 | Longitudinal empirical study supports its findings. |
| Practical usability | 60 | 10% | 6.00 | Useful targeting data, though acquisition is competitive. |
| Clarity and reproducibility | 87 | 10% | 8.70 | Collection and lifecycle stages are documented. |

**Final score: 68.3/100.** Archive decision: include as qualifying material.

### Verdict

Meaningful extension. It does not originate expired-domain takeover, but adds
actionable registrar-process and timing evidence missing from earlier work.

## 80.1 — [FP-STALKER: Tracking Browser Fingerprint Evolutions](https://hal.inria.fr/hal-01652021) — Antoine Vastel, Pierre Laperdrix, Walter Rudametkin, Romain Rouvoy

**KEPT** · Meaningful extension · confidence High

### Candidate

Complete manuscript deposited in HAL on 2 December 2017; subsequently published
at the 2018 IEEE Symposium on Security and Privacy.

### Core contribution

FP-STALKER treats a browser fingerprint as a changing lineage rather than a
fixed identifier. It measures fingerprint evolution over time and supplies
rule-based and hybrid rule/random-forest algorithms that link a new fingerprint
to an earlier observation or identify it as a previously unseen browser. The
authors evaluate the approach on 98,598 fingerprints from 1,905 browser
instances collected over two years and show that update and configuration
changes do not reliably end stateless tracking.

### Prior art

Eckersley's 2010 Panopticlick study established the uniqueness and linkability
of browser attributes. The 2016 *Beauty and the Beast* work expanded the
attributes available to a browser fingerprint, and 2017 cross-browser
fingerprinting linked devices through operating-system and hardware features.
FP-STALKER does not originate browser fingerprinting; its distinct contribution
is a general longitudinal method for linking fingerprints as their constituent
attributes evolve.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 62 | 25% | 15.50 | Adds longitudinal linkage algorithms to a known tracking class. |
| Transferability | 88 | 20% | 17.60 | Applies across sites and browser fingerprints with evolving attributes. |
| Lasting value | 82 | 20% | 16.40 | Durability remains central to evaluating fingerprint-based tracking. |
| Technical soundness | 91 | 15% | 13.65 | 98,598 observations over two years support the linkage evaluation. |
| Practical usability | 80 | 10% | 8.00 | Published algorithms make changing fingerprints operationally linkable. |
| Clarity and reproducibility | 89 | 10% | 8.90 | Dataset, algorithms, evaluation and open-source implementation are described. |

**Final score: 80.1/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It advances known browser fingerprinting from static
uniqueness measurements to reusable linkage of changing fingerprints.

## 81.1 — [Automated Website Fingerprinting through Deep Learning](https://arxiv.org/abs/1708.06376) — Vera Rimmer, Davy Preuveneers, Marc Juarez, Tom Van Goethem, Wouter Joosen

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Complete arXiv manuscript first submitted on 21 August 2017; subsequently
published at NDSS 2018.

### Core contribution

The paper replaces manually engineered website-fingerprinting features with
deep models that learn representations directly from encrypted Tor traffic.
Its evaluation uses more than three million traces, reports over 96 percent
closed-world accuracy for 100 websites and over 94 percent for 900 classes,
and finds the learned features more resilient to changing Web content.

### Prior art

Website fingerprinting from encrypted traffic dates at least to 2002. By 2016,
*Website Fingerprinting at Internet Scale* had tested efficient classification
under realistic scale assumptions, while *k-fingerprinting* used random forests
for robust open-world classification. The 2017 manuscript's distinct advance is
automated representation and feature learning over raw traffic traces, not the
underlying packet-metadata observation attack.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 70 | 25% | 17.50 | Automates feature learning for an established traffic-analysis attack. |
| Transferability | 78 | 20% | 15.60 | Models transfer across many Tor sites, classes and content changes. |
| Lasting value | 86 | 20% | 17.20 | Deep sequence learning became an enduring fingerprinting methodology. |
| Technical soundness | 94 | 15% | 14.10 | Multi-model experiments over three million traces provide strong evidence. |
| Practical usability | 76 | 10% | 7.60 | The method is implementable but needs traffic vantage and training data. |
| Clarity and reproducibility | 91 | 10% | 9.10 | Architectures, datasets, comparisons and evaluation settings are detailed. |

**Final score: 81.1/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It applies automated representation
learning to replace brittle hand-engineered features in an established attack.
The observation point is network-layer, but the target and result—identifying
the website a user visits—give the method direct Web-security bearing consistent
with the retained 2016 website-fingerprinting work.
