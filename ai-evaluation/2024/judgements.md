# 2024 candidate judgements

These scorecards apply the repository's weighted judge rubric. `KEPT` means the
candidate met the historical 60-or-above rule together with the calendar-year,
originality-verdict and original-nomination exclusions.

## 90.8 — [SnailLoad: Exploiting Remote Network Latency Measurements without JavaScript](https://www.usenix.org/conference/usenixsecurity24/presentation/gast) — Stefan Gast et al.

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed USENIX Security paper and primary project disclosure published in
2024; no complete earlier public version was found.

### Core contribution

A deliberately slow cross-origin asset lets its server measure congestion-driven
round-trip changes and infer the victim's simultaneous network activity. It lifts
website and video fingerprinting from an on-path observer to a remote server
without JavaScript or user interaction.

### Prior art

Traffic fingerprinting and remote timing were established. Using a slow HTTP
transfer as a continuously remote latency probe, without an on-path position, is
the distinct mechanism.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 93 | 25% | 23.25 | Converts shared last-mile latency into a remote activity oracle. |
| Transferability | 92 | 20% | 18.40 | Applies to ordinary assets, videos and websites across networks. |
| Lasting value | 90 | 20% | 18.00 | Changes the assumed observer needed for traffic analysis. |
| Technical soundness | 92 | 15% | 13.80 | Open- and closed-world evaluations validate the channel. |
| Practical usability | 82 | 10% | 8.20 | A hostile server can deploy it, though classification needs traces. |
| Clarity and reproducibility | 91 | 10% | 9.10 | Paper, project site and proof of concept document the method. |

**Final score: 90.8/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It removes both script execution and the on-path vantage
point from a practical Web-activity side channel.

## 89.7 — [Generic and Automated Drive-by GPU Cache Attacks from the Browser](https://www.rolandczerny.com/publications/2024-webgpu/) — Lukas Giner et al.

**KEPT** · Original technique · confidence High

### Candidate

Publicly disclosed in March 2024 and published at AsiaCCS 2024; the author page,
paper and coordinated vendor bulletin agree on the year.

### Core contribution

WebGPU compute shaders build self-configuring GPU eviction sets inside the
browser. The resulting drive-by cache channel recovers keystroke timing, leaks a
GPU AES key and supports native-to-browser exfiltration across varied GPUs.

### Prior art

Native GPU cache attacks and browser CPU-cache attacks existed. This is the
first automated GPU-cache attack from WebGPU's restricted browser environment.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 94 | 25% | 23.50 | Establishes browser WebGPU as a generic GPU-cache attack surface. |
| Transferability | 88 | 20% | 17.60 | Self-configures across 11 GPUs, generations and two vendors. |
| Lasting value | 90 | 20% | 18.00 | WebGPU exposes a durable new browser hardware boundary. |
| Technical soundness | 92 | 15% | 13.80 | Three end-to-end attacks substantiate the primitives. |
| Practical usability | 80 | 10% | 8.00 | Drive-by delivery is easy; useful leakage remains workload-specific. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Primary paper and project page provide design and results. |

**Final score: 89.7/100.** Archive decision: include as a core technique.

### Verdict

Original technique. WebGPU supplies a browser-native path to hardware cache
attacks that prior JavaScript and native-GPU work did not provide.

## 89.2 — [Web Platform Threats: Automated Detection of Web Security Issues With WPT](https://www.usenix.org/conference/usenixsecurity24/presentation/bernardo) — Pedro Bernardo et al.

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

USENIX published the paper and artifact in 2024; no earlier complete disclosure
was located.

### Core contribution

The framework converts Web Platform Tests into browser traces and checks them
against first-order security invariants. Nine invariants found security-relevant
violations in 104 Chromium, Firefox and Safari tests, producing eight reports
and a Safari CVE.

### Prior art

Differential browser testing and the 2023 DiffCSP work were known. This method
generalises beyond CSP by coupling standards tests to explicit security-property
oracles rather than relying only on cross-browser disagreement.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 84 | 25% | 21.00 | Turns conformance traces into formal security checks. |
| Transferability | 92 | 20% | 18.40 | Applies across mechanisms, tests and the three major engines. |
| Lasting value | 91 | 20% | 18.20 | Reuses a maintained standards corpus as browsers evolve. |
| Technical soundness | 93 | 15% | 13.95 | Confirmed reports and a CVE validate the invariants. |
| Practical usability | 86 | 10% | 8.60 | Artifact automates trace collection and solver checks. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Invariants, workflow and artifact are explicit. |

**Final score: 89.2/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It materially expands semantic browser
testing from policy-specific differential checks to reusable security invariants.

## 89.2 — [CDN Cannon: Exploiting CDN Back-to-Origin Strategies for Amplification Attacks](https://www.usenix.org/conference/usenixsecurity24/presentation/lin-ziyu) — Ziyu Lin et al.

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in 2024; primary author and venue
records show no earlier complete release.

### Core contribution

Back-to-Origin Amplification abuses CDN image optimisation, request rewriting,
HEAD-to-GET conversion and connection decoupling so small client traffic forces
vastly larger origin traffic, with measured amplification above 100,000×.

### Prior art

CDN cache attacks and amplification DoS were established. Weaponising CDN
performance transformations against the protected origin is a separate class.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 92 | 25% | 23.00 | Defines CDN back-to-origin behaviour as an amplifier. |
| Transferability | 90 | 20% | 18.00 | Four strategies affect major CDNs and hosted origins. |
| Lasting value | 88 | 20% | 17.60 | Performance transformations remain central to CDN design. |
| Technical soundness | 90 | 15% | 13.50 | Fourteen-CDN evaluation and disclosures substantiate impact. |
| Practical usability | 83 | 10% | 8.30 | Low attacker bandwidth can trigger large amplification. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Attack variants and amplification measurements are detailed. |

**Final score: 89.2/100.** Archive decision: include as a core technique.

### Verdict

Original technique. The amplification comes from CDN-to-origin transformations,
not conventional reflection or a renamed cache-poisoning case.

## 88.5 — [GHunter: Universal Prototype Pollution Gadgets in JavaScript Runtimes](https://www.usenix.org/conference/usenixsecurity24/presentation/cornelissen) — Eric Cornelissen, Mikhail Shcherbakov, Musard Balliu

**KEPT** · Meaningful extension · confidence High

### Candidate

The complete arXiv paper was first posted on 15 July 2024 and the work appeared
at USENIX Security 2024.

### Core contribution

GHunter instruments V8 and drives Node.js and Deno test suites with lightweight
taint tracking to discover universal runtime prototype-pollution gadgets. It
found 123 new gadgets spanning RCE, privilege escalation and path traversal.

### Prior art

Prototype pollution and application/library gadget scanners were already known
and appear in the original list. Runtime-wide gadget discovery driven by the
runtimes' own test suites materially broadens reach and consequence analysis.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 84 | 25% | 21.00 | Extends gadget discovery into shared JavaScript runtimes. |
| Transferability | 92 | 20% | 18.40 | Runtime gadgets affect many applications on Node.js and Deno. |
| Lasting value | 88 | 20% | 17.60 | Universal gadgets remain relevant across dependency changes. |
| Technical soundness | 93 | 15% | 123 validated gadgets and a high-severity CVE support it. |
| Practical usability | 86 | 10% | 8.60 | Open artifacts and test-suite driving make it actionable. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Pipeline, artifacts and validation process are documented. |

**Final score: 88.5/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It is not another application gadget finder: it maps the
universal gadget layer supplied by the runtime itself.

## 87.0 — [Argus: All your (PHP) Injection-sinks are belong to us](https://www.usenix.org/conference/usenixsecurity24/presentation/jahanshahi) — Rasoul Jahanshahi, Manuel Egele

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in 2024; no earlier complete
public version was found.

### Core contribution

Argus analyses PHP interpreter internals to derive injection sinks automatically
instead of trusting incomplete hand-curated lists. Feeding the results into
Psalm, RIPS and FUGIO exposed 13 previously unknown WordPress/plugin flaws.

### Prior art

Taint analysis and exploit generation already consumed sink lists. Automatically
recovering deserialisation, command-execution and output sinks from the language
runtime addresses a different and foundational blind spot.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | Derives security sinks from interpreter semantics. |
| Transferability | 91 | 20% | 18.20 | Improves multiple analysers and three injection classes. |
| Lasting value | 87 | 20% | 17.40 | Avoids brittle, manually maintained sink inventories. |
| Technical soundness | 92 | 15% | 13.80 | Hundreds of sinks and confirmed CVEs validate the method. |
| Practical usability | 83 | 10% | 8.30 | Results integrate into existing analysis and exploit tools. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Runtime analysis and downstream evaluation are explicit. |

**Final score: 87.0/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. The technique improves the completeness of
whole families of PHP injection analyses rather than adding a narrow payload.

## 87.0 — [A Flushing Attack on the DNS Cache](https://www.usenix.org/conference/usenixsecurity24/presentation/afek) — Yehuda Afek, Anat Bremler-Barr, Shoham Danino, Yuval Shavitt

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in 2024; the venue paper and
artifact are the first complete public records located.

### Core contribution

DNS CacheFlush uses seemingly valid referral or CNAME-heavy answers to force a
resolver to insert records at high rate, evict benign entries from LRU caches and
turn modest request traffic into sustained resolver cache misses and delay.

### Prior art

DNS cache poisoning, flooding and eviction pressure were known. This attack
amplifies cache insertion work through valid-looking answer structure to thrash
even frequently queried entries without poisoning their values.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 91 | 25% | 22.75 | Introduces answer-amplified resolver cache thrashing. |
| Transferability | 88 | 20% | 17.60 | Targets common resolver caches and DNS response structures. |
| Lasting value | 84 | 20% | 16.80 | Cache-capacity pressure persists across resolver designs. |
| Technical soundness | 91 | 15% | 13.65 | Controlled experiments quantify misses and throughput loss. |
| Practical usability | 74 | 10% | 7.40 | Requires authoritative response control and sustained queries. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Paper and isolated simulator artifact explain the attack. |

**Final score: 87.0/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It is cache eviction by DNS answer expansion, not another
poisoned-record or ordinary volumetric DNS attack.

## 86.5 — [Pixel Thief: Exploiting SVG Filter Leakage in Firefox and Chrome](https://www.usenix.org/conference/usenixsecurity24/presentation/oconnell) — Sioli O'Connell et al.

**KEPT** · Meaningful extension · confidence High

### Candidate

The primary paper record is from January 2024 and the work appeared at USENIX
Security in August 2024.

### Core contribution

Pixel Thief forces CPU SVG-filter rendering and applies a cache side channel to
recover cross-origin text and browsing history. It leaks multiple bits per
display refresh, bypassing mitigations aimed at filter-rendering timing.

### Prior art

SVG filter timing and pixel stealing date to earlier work. Monitoring the
renderer’s data-dependent cache accesses supplies a faster channel that survives
the timing equalisation browsers deployed against those attacks.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 86 | 25% | 21.50 | Replaces mitigated filter timing with renderer cache leakage. |
| Transferability | 88 | 20% | 17.60 | Demonstrated in Firefox and Chrome for two leak goals. |
| Lasting value | 86 | 20% | 17.20 | Shows timing equalisation does not close rendering leakage. |
| Technical soundness | 91 | 15% | 13.65 | Text recovery and high-speed history sniffing validate it. |
| Practical usability | 78 | 10% | 7.80 | Web delivery is direct but hardware and rendering conditions matter. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Attack construction and primary artifact are documented. |

**Final score: 86.5/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It changes the observable from frame time to cache access
and materially improves both rate and resistance to existing mitigation.

## 85.7 — [Internet's Invisible Enemy: Detecting and Measuring Web Cache Poisoning in the Wild](https://doi.org/10.1145/3658644.3690361) — Yuejia Liang et al.

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed ACM CCS paper first published in 2024; no complete earlier public
version was located.

### Core contribution

HCache generates cache-key-aware mutations and safely validates poisoning with
normal, attack and validation requests. Its Internet-scale study found seven new
header vectors and vulnerable sites across 17% of measured top domains.

### Prior art

Web cache poisoning and manual unkeyed-input probing were established and well
represented in the original list. Systematic, cache-key-aware and non-disruptive
large-scale vector discovery is the meaningful methodological extension.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | Adds safe cache-key-aware discovery and seven vectors. |
| Transferability | 91 | 20% | 18.20 | Applies across caches, headers, domains and deployments. |
| Lasting value | 85 | 20% | 17.00 | Cache-key disagreement remains a broad Web risk. |
| Technical soundness | 90 | 15% | 13.50 | Large-scale results and vendor confirmations support it. |
| Practical usability | 78 | 10% | 7.80 | Automation is useful, though Internet scanning needs care. |
| Clarity and reproducibility | 87 | 10% | 8.70 | Generation, isolation and validation steps are described. |

**Final score: 85.7/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It turns case-by-case cache poisoning into systematic and
safely measurable attack-surface discovery.

## 85.0 — [Vulnerability-oriented Testing for RESTful APIs](https://www.usenix.org/conference/usenixsecurity24/presentation/du) — Wenlong Du et al.

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in 2024; no earlier complete
public version was found.

### Core contribution

VOAPI2 infers API functionality from identifiers, generates stateful request
sequences with vulnerability-specific payloads and verifies flaws from feedback.
It found 26 real-world bugs, 23 with CVEs, across seven REST APIs.

### Prior art

OpenAPI fuzzing and stateful API testing existed. Selecting sequences and attack
oracles from inferred endpoint functionality is the distinct contribution.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 80 | 25% | 20.00 | Couples inferred endpoint function to targeted attack testing. |
| Transferability | 88 | 20% | 17.60 | Supports varied APIs and vulnerability classes. |
| Lasting value | 84 | 20% | 16.80 | Stateful semantic API testing remains broadly useful. |
| Technical soundness | 91 | 15% | 13.65 | Real deployments and 23 CVEs substantiate results. |
| Practical usability | 82 | 10% | 8.20 | Automated sequences and feedback reduce manual testing. |
| Clarity and reproducibility | 87 | 10% | 8.70 | Stages and evaluation are clearly documented. |

**Final score: 85.0/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It adds vulnerability-oriented semantic
guidance to API testing rather than merely increasing request volume.

## 84.9 — [Peeking through the window: Fingerprinting Browser Extensions through Page-Visible Execution Traces and Interactions](https://doi.org/10.1145/3658644.3670339) — Shubham Agarwal, Aurore Fass, Ben Stock

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed ACM CCS paper first published in 2024; no earlier complete release
was found.

### Core contribution

A website identifies installed extensions from page-visible execution traces
and interactions caused by content scripts, without relying on web-accessible
extension resources. Existing anti-fingerprinting defenses miss these vectors.

### Prior art

Extension fingerprinting through resources and DOM artefacts was known. Using
observable script execution and interaction behaviour supplies a distinct oracle.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 84 | 25% | 21.00 | Introduces execution-trace and interaction fingerprints. |
| Transferability | 88 | 20% | 17.60 | Applies to many content-script behaviours and extensions. |
| Lasting value | 84 | 20% | 16.80 | Page/extension interaction remains intrinsic to extensions. |
| Technical soundness | 88 | 15% | 13.20 | Large extension analysis and validated vectors support it. |
| Practical usability | 78 | 10% | 7.80 | A hostile page can probe visitors with some profiling. |
| Clarity and reproducibility | 85 | 10% | 8.50 | Threat model and vector construction are documented. |

**Final score: 84.9/100.** Archive decision: include as a core technique.

### Verdict

Original technique. The observed signal is extension execution behaviour, not
another URL probe for exposed package resources.

## 83.7 — [FuzzCache: Optimizing Web Application Fuzzing Through Software-Based Data Cache](https://zhangmx1997.github.io/papers/ccs24_fuzzcache.pdf) — Penghui Li, Mingxue Zhang

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed ACM CCS paper first published in 2024.

### Core contribution

FuzzCache shares safely invalidated database and network results across PHP
fuzzing trials and adds JIT execution. Integrated into black- and grey-box Web
fuzzers, it raises throughput 3–4× and code coverage by about 25%.

### Prior art

Web fuzzing and process snapshots existed. Caching repeated external data access
across isolated Web trials is a complementary performance method.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 73 | 25% | 18.25 | Adds cross-trial data caching tailored to Web state. |
| Transferability | 90 | 20% | 18.00 | Complements black- and grey-box Web fuzzers. |
| Lasting value | 82 | 20% | 16.40 | Database/network latency is a durable Web-testing bottleneck. |
| Technical soundness | 90 | 15% | 13.50 | Measured throughput, coverage and bug gains support it. |
| Practical usability | 89 | 10% | 8.90 | Integrates with existing fuzzers rather than replacing them. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Cache model, invalidation and evaluation are explicit. |

**Final score: 83.7/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It is a reusable Web-fuzzing accelerator,
not a new vulnerability class.

## 83.6 — [ReactAppScan: Mining React Application Vulnerabilities via Component Graph](https://www.yinzhicao.org/reactappscan/reactappscan.pdf) — Zhiyong Guo et al.

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed ACM CCS paper first published in 2024.

### Core contribution

ReactAppScan models component lifecycles, props, state and client/server flows
in a component graph, then queries source-to-sink paths. It found 61 zero-days
that ordinary JavaScript/JSX analysis missed.

### Prior art

JavaScript abstract interpretation and CodeQL supported portions of JSX. The
component-lifecycle graph makes React-specific cross-component flows tractable.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 79 | 25% | 19.75 | Models React lifecycle, props and state as security flow. |
| Transferability | 86 | 20% | 17.20 | Covers common React applications and packages. |
| Lasting value | 84 | 20% | 16.80 | Component-based SPAs remain widespread. |
| Technical soundness | 90 | 15% | 13.50 | 61 findings and comparison with CodeQL substantiate it. |
| Practical usability | 79 | 10% | 7.90 | Open source, though it needs application source. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Graph construction and evaluation are documented. |

**Final score: 83.6/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It adds React-native data-flow semantics
that generic JavaScript analysis lacks.

## 82.8 — [AuthSaber: Automated Safety Verification of OpenID Connect Programs](https://ucla-sec-lab.netlify.app/publication/2024-authsaber/) — Tamjid Al Rahat, Yu Feng, Yuan Tian

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

The primary author page dates the work to July 2024 and ACM CCS 2024; no earlier
complete public version was found.

### Core contribution

AuthSaber turns OpenID Connect safety properties into automated program checks,
including authentication ordering, token algorithm, issuer and code-use rules,
to expose implementation-level authentication flaws.

### Prior art

OIDC protocol analysis and individual OAuth/OIDC bugs were known. Automated
verification of concrete relying-party/provider programs against a property set
is the distinct methodology.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 80 | 25% | 20.00 | Maps OIDC safety requirements to implementation checks. |
| Transferability | 82 | 20% | 16.40 | Applies across implementations sharing OIDC flows. |
| Lasting value | 86 | 20% | 17.20 | OIDC program logic remains complex and security-critical. |
| Technical soundness | 90 | 15% | 13.50 | Formalised properties and evaluated programs support it. |
| Practical usability | 74 | 10% | 7.40 | Automation helps, but program modelling remains specialised. |
| Clarity and reproducibility | 83 | 10% | 8.30 | Paper, code and dataset are linked by the authors. |

**Final score: 82.8/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It verifies protocol invariants in real
OIDC code rather than presenting another single OAuth misconfiguration.

## 82.7 — [Spider-Scents: Grey-box Database-aware Web Scanning for Stored XSS](https://www.usenix.org/conference/usenixsecurity24/presentation/olsson) — Eric Olsson, Benjamin Eriksson, Adam Doupé, Andrei Sabelfeld

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in 2024; no earlier complete
public version was found.

### Core contribution

Spider-Scents injects markers and XSS payloads directly into the database, maps
values to rendered outputs and identifies unprotected stored-XSS paths. It
reached 79–100% database coverage and found 85 vulnerabilities.

### Prior art

Black-box stored-XSS scanning and database-aware test generation existed. Direct
database injection deliberately bypasses hard-to-reach write paths to audit all
later render paths.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 83 | 25% | 20.75 | Reverses stored-XSS testing by seeding the database. |
| Transferability | 79 | 20% | 15.80 | Useful across database-backed apps with deployment access. |
| Lasting value | 80 | 20% | 16.00 | Stored rendering paths remain difficult for scanners. |
| Technical soundness | 91 | 15% | 13.65 | Twelve-app comparison and 85 findings validate it. |
| Practical usability | 78 | 10% | 7.80 | Effective in grey-box assessments with database access. |
| Clarity and reproducibility | 87 | 10% | 8.70 | Mapping, smells and exploitability analysis are clear. |

**Final score: 82.7/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. Direct database seeding exposes stored-XSS
render paths unreachable to conventional front-door scanners.

## 82.4 — [Rise of Inspectron: Automated Black-box Auditing of Cross-platform Electron Apps](https://www.usenix.org/conference/usenixsecurity24/presentation/ali) — Mir Masood Ali et al.

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in 2024.

### Core contribution

Inspectron dynamically audits packaged Electron applications without source for
dangerous browser-to-OS configurations and deviations from Electron hardening
guidance, making cross-platform desktop-Web review scalable.

### Prior art

The 2023 list already retains an Electron security study and programming method.
Black-box auditing of packaged applications is a meaningful operational extension,
not a duplicate of source-guided DOM taming.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 76 | 25% | 19.00 | Adds packaged-app black-box auditing for Electron. |
| Transferability | 86 | 20% | 17.20 | Works across apps and desktop platforms. |
| Lasting value | 82 | 20% | 16.40 | Browser/OS privilege bridging remains central to Electron. |
| Technical soundness | 87 | 15% | 13.05 | Ecosystem study demonstrates practical findings. |
| Practical usability | 82 | 10% | 8.20 | Requires only packaged applications, not source. |
| Clarity and reproducibility | 85 | 10% | 8.50 | Audit model and evaluated practices are documented. |

**Final score: 82.4/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. Its black-box packaged-app model materially
extends the earlier Electron work.

## 79.2 — [Arcanum: Detecting and Evaluating the Privacy Risks of Browser Extensions on Web Pages and Web Content](https://www.usenix.org/conference/usenixsecurity24/presentation/xie-qinge) — Qinge Xie et al.

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in 2024.

### Core contribution

Arcanum adds dynamic taint tracking to modern Chrome-extension execution so
specific sensitive page content can be followed to extension sinks. Its full
store study found hundreds of extensions extracting user content.

### Prior art

Extension permissions, metadata leakage and older taint analyses were known.
Tracking actual modern Web-page content through Manifest-era extension APIs is
the practical extension.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 72 | 25% | 18.00 | Modernises taint analysis around page-content leakage. |
| Transferability | 84 | 20% | 16.80 | Covers the Chrome store and diverse sensitive sites. |
| Lasting value | 78 | 20% | 15.60 | Extension access to page content remains a privacy boundary. |
| Technical soundness | 88 | 15% | 13.20 | Store-wide deployment produces substantial measured findings. |
| Practical usability | 74 | 10% | 7.40 | Research instrumentation is heavier than ordinary testing. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Sources, sinks and deployment are explained. |

**Final score: 79.2/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It makes sensitive Web-content extraction
by extensions observable at ecosystem scale.

## 78.9 — [Introducing the URL Validation Bypass Cheat Sheet](https://portswigger.net/research/introducing-the-url-validation-bypass-cheat-sheet) — Zakhar Fedotkin

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

PortSwigger published the primary interactive methodology on 3 September 2024;
the October payload article is treated as an update, not a second candidate.

### Core contribution

The tool contextually generates encoded domain-confusion, fake-relative,
loopback, Origin and normalisation payloads for URL validators, exporting
Intruder-ready wordlists from a maintained machine-readable corpus.

### Prior art

Nearly all underlying URL parser tricks predate the work. The qualifying value
is the interactive, context-aware and maintainable testing methodology.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 54 | 25% | 13.50 | Mostly consolidates known URL ambiguity payloads. |
| Transferability | 92 | 20% | 18.40 | Supports SSRF, CORS, redirects, hosts and WAF tests. |
| Lasting value | 82 | 20% | 16.40 | A maintained parser corpus stays useful as stacks evolve. |
| Technical soundness | 78 | 15% | 11.70 | Payload categories are grounded in parser behaviour. |
| Practical usability | 96 | 10% | 9.60 | Interactive generation and wordlist export are immediately usable. |
| Clarity and reproducibility | 93 | 10% | 9.30 | Contexts, encodings and source data are public. |

**Final score: 78.9/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. Low payload originality is outweighed by a
highly reusable testing system; it is not claimed as a new vulnerability class.

## 77.1 — [Fickle PDFs: exploiting browser rendering discrepancies](https://portswigger.net/research/fickle-pdfs-exploiting-browser-rendering-discrepancies) — Zakhar Fedotkin

**KEPT** · Meaningful combination or adaptation · confidence High

### Candidate

PortSwigger published the article and generator on 9 July 2024.

### Core contribution

Hybrid PDFs give form defaults and widget annotations conflicting values, so
Safari/Preview, Chrome/Drive and Firefox can show different invoice content.
The ambiguity supports cross-viewer document deception and AI-review mismatch.

### Prior art

Kobold Letters and PDF parser/rendering disagreement existed. Combining widget
annotations with form appearance precedence supplies a compact, reproducible
cross-viewer deception variant.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78 | 25% | 19.50 | Exploits widget/default precedence across current viewers. |
| Transferability | 70 | 20% | 14.00 | Broad viewers are affected, but the medium is PDF-specific. |
| Lasting value | 72 | 20% | 14.40 | Ambiguous PDF rendering is persistent but specialised. |
| Technical soundness | 82 | 15% | 12.30 | Multiple engines and generated examples validate it. |
| Practical usability | 80 | 10% | 8.00 | Generator makes deceptive documents easy to reproduce. |
| Clarity and reproducibility | 89 | 10% | 8.90 | Construction, screenshots and code are supplied. |

**Final score: 77.1/100.** Archive decision: include as a core technique.

### Verdict

Meaningful combination or adaptation. It advances prior document ambiguity with
a current cross-browser form/widget construction and reusable generator.

## 76.2 — [Concealing payloads in URL credentials](https://portswigger.net/research/concealing-payloads-in-url-credentials) — Gareth Heyes

**KEPT** · Meaningful extension · confidence High

### Candidate

PortSwigger published the article on 23 October 2024; it credits the initial
credential-concealment observation from the preceding year but adds the first
complete exploitation analysis located in 2024.

### Core contribution

Although browsers hide credentials in the address bar and `location`,
`document.URL` retains them. Payloads can survive same-origin navigation, feed
DOM-XSS sinks and clobber inherited anchor username/password properties.

### Prior art

URL credentials, DOM XSS and DOM clobbering were known. The retained contribution
is the 2024 analysis of property disagreement, inheritance and exploit chains;
the earlier observation prevents an original-technique verdict.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 79 | 25% | 19.75 | Develops credential retention into several exploit primitives. |
| Transferability | 72 | 20% | 14.40 | Useful in Chrome/Firefox flows but not Safari. |
| Lasting value | 70 | 20% | 14.00 | Property disagreement persists but browsers may converge. |
| Technical soundness | 78 | 15% | 11.70 | Concrete DOM-XSS and clobbering demonstrations support it. |
| Practical usability | 76 | 10% | 7.60 | Payload delivery is simple when a suitable sink exists. |
| Clarity and reproducibility | 87 | 10% | 8.70 | Browser differences and examples are explicit. |

**Final score: 76.2/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. The 2023 observation is not relabelled as new; the scored
contribution is the later browser-property analysis and exploitation chains.

## 73.0 — [Introducing SignSaboteur: forge signed web tokens with ease](https://portswigger.net/research/introducing-signsaboteur-forge-signed-web-tokens-with-ease) — Zakhar Fedotkin

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

PortSwigger published the open-source Burp extension and methodology on 22 May
2024.

### Core contribution

SignSaboteur detects, edits, brute-forces, re-signs and attacks signed tokens
from Django, Flask, Express and other frameworks, including unknown formats,
key derivations and automated authorization-claim mutations.

### Prior art

Signed-cookie/JWT key guessing and claim forgery were well established. The
contribution is unified framework-aware detection and mutation beyond JWT.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 48 | 25% | 12.00 | Primarily automates established signed-token attacks. |
| Transferability | 85 | 20% | 17.00 | Handles multiple frameworks, formats and transports. |
| Lasting value | 70 | 20% | 14.00 | Signed application tokens remain common, though formats evolve. |
| Technical soundness | 80 | 15% | 12.00 | Implemented extension and laboratory examples validate the flow. |
| Practical usability | 93 | 10% | 9.30 | Direct Burp integration makes the methodology operational. |
| Clarity and reproducibility | 87 | 10% | 8.70 | Modes, derivations, claims and source are documented. |

**Final score: 73.0/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It clears 60 on breadth and usability,
while the low originality score explicitly avoids claiming new token attacks.
