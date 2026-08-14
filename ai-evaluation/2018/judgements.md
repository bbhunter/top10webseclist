# 2018 candidate judgements

These scorecards apply the repository's weighted judge rubric. `KEPT` means the
candidate met the historical 60-or-above inclusion rule as well as the
first-publication, originality-verdict and original-nomination exclusions.

## 94.2 — [Spectre Attacks: Exploiting Speculative Execution](https://spectreattack.com/spectre.pdf) — Paul Kocher et al.

**KEPT** · Original technique · confidence High

### Candidate

The coordinated paper and disclosure were published on 3 January 2018. Its
browser proof of concept executes from JavaScript, so the contribution is in
web scope despite the underlying processor flaw.

### Core contribution

Spectre mistrains speculative execution so transient instructions read data
outside the JavaScript program's intended authority and encode it into a cache
side channel. It demonstrates cross-origin memory disclosure from a browser and
establishes a reusable attack model spanning languages and processors.

### Prior art

CPU cache attacks, branch-predictor attacks and JavaScript timing channels were
known. No earlier public work combined predictor mistraining, transient
execution and a recoverable microarchitectural channel into this primitive.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 94 | 25% | 23.50 | Defines the transient-execution disclosure class. |
| Transferability | 94 | 20% | 18.80 | Applies across browsers, runtimes and processor families. |
| Lasting value | 98 | 20% | 19.60 | Permanently changed browser and hardware threat models. |
| Technical soundness | 96 | 15% | 14.40 | Multiple implementations and end-to-end demonstrations support it. |
| Practical usability | 85 | 10% | 8.50 | Exploitation is demanding but the JavaScript procedure is concrete. |
| Clarity and reproducibility | 94 | 10% | 9.40 | Attack stages, variants and mitigations are explicit. |

**Final score: 94.2/100.** Archive decision: include as a core technique.

### Verdict

Original technique. Earlier side channels supplied ingredients, not transient
execution as a cross-origin read primitive.

## 88.0 — [Browser history re:visited](https://www.usenix.org/conference/woot18/presentation/smith) — Michael Smith, Craig Disselkoen, Shravan Narayan, Fraser Brown, Deian Stefan

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed WOOT paper published in August 2018.

### Core contribution

The work develops four history-sniffing attacks through modern browser
features: CSS Paint, CSS/SVG behavior and JavaScript bytecode caches. One
visited-link oracle tests roughly 3,000 URLs per second, and two attacks affect
nearly every evaluated browser except Tor Browser.

### Prior art

Visited-link and cache history sniffing date to 2000 and browser vendors had
already restricted classic CSS probes. The new contribution is recovering the
same forbidden state through newly introduced browser subsystems and caches.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | Four novel oracles adapt a known goal to new browser state. |
| Transferability | 92 | 20% | 18.40 | Spans multiple features and browser families. |
| Lasting value | 87 | 20% | 17.40 | Durable lesson for privacy-sensitive browser caches and APIs. |
| Technical soundness | 91 | 15% | 13.65 | Cross-browser evaluation and assigned CVE validate the attacks. |
| Practical usability | 90 | 10% | 9.00 | Fast, scriptable probes need only a hostile page. |
| Clarity and reproducibility | 91 | 10% | 9.10 | Each oracle and its browser conditions are documented. |

**Final score: 88.0/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. The privacy target is old, but the modern-feature oracles
restore capabilities that browser defenses were designed to remove.

## 87.9 — [Bamboozling Certificate Authorities with BGP](https://www.usenix.org/conference/usenixsecurity18/presentation/birge-lee) — Henry Birge-Lee, Yixin Sun, Anne Edmundson, Jennifer Rexford, Prateek Mittal

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2018.

### Core contribution

The authors ethically perform real BGP hijacks against top certificate
authorities, obtain bogus certificates, analyze 1.8 million certificates and
show that most domains are exposed. They develop multi-vantage validation and
BGP-monitoring countermeasures grounded in the attack measurements.

### Prior art

BGP hijacking and a 2015 proposal for breaking HTTPS certificate validation via
BGP were public. This paper supplies the first controlled issuance experiments,
a rigorous attack taxonomy and Internet-scale exposure analysis.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78 | 25% | 19.50 | Converts a prior proposal into validated CA-issuance attacks. |
| Transferability | 94 | 20% | 18.80 | Affects domain validation across CAs and domains. |
| Lasting value | 92 | 20% | 18.40 | Multi-vantage validation remains a foundational mitigation. |
| Technical soundness | 94 | 15% | 14.10 | Ethical live tests and large datasets support the conclusions. |
| Practical usability | 80 | 10% | 8.00 | Requires routing capability but gives precise attack conditions. |
| Clarity and reproducibility | 91 | 10% | 9.10 | Taxonomy, measurements and mitigations are detailed. |

**Final score: 87.9/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It materially advances the 2015 BGP/HTTPS idea through
real certificate issuance and general countermeasures.

## 87.6 — [Study and Mitigation of Origin Stripping Vulnerabilities in Hybrid-postMessage Enabled Mobile Applications](https://ieeexplore.ieee.org/document/8418635/) — Guangliang Yang, Jeff Huang, Guofei Gu, Abner Mendoza

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published in May
2018.

### Core contribution

Hybrid `postMessage` bridges can discard the sender origin while moving a
message between WebView JavaScript and native code. OSV-Hunter found all 74
sampled hybrid-postMessage apps vulnerable, including frameworks and document
readers, enabling message interception and privileged native actions.

### Prior art

Missing target-origin checks, hostile WebView content and overprivileged native
bridges were known. Earlier work did not identify origin loss inside the hybrid
message-delivery abstraction itself or systematize its detection.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 88 | 25% | 22.00 | Defines origin stripping as a distinct cross-layer flaw. |
| Transferability | 88 | 20% | 17.60 | Recurs across frameworks, apps and native/Web bridges. |
| Lasting value | 86 | 20% | 17.20 | Durable model for preserving provenance across bridge boundaries. |
| Technical soundness | 92 | 15% | 13.80 | Tool, population study, exploits and replacement APIs align. |
| Practical usability | 82 | 10% | 8.20 | OSV-Hunter and concrete bridge patterns support audits. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Mechanism, examples and mitigation are explicit. |

**Final score: 87.6/100.** Archive decision: include as a core technique.

### Verdict

Original technique. The lost-origin condition is distinct from ordinary
postMessage validation mistakes and generic WebView bridge abuse.

## 86.8 — [Grand Pwning Unit: Accelerating Microarchitectural Attacks with the GPU](https://download.vusec.net/papers/glitch_sp18.pdf) — Pietro Frigo, Cristiano Giuffrida, Herbert Bos, Kaveh Razavi

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published in May
2018.

### Core contribution

The work reverse engineers an integrated mobile GPU and builds cache and
Rowhammer primitives exposed through WebGL. JavaScript orchestrates the first
end-to-end microarchitectural compromise of a mobile browser in under two
minutes, bypassing CPU-focused defenses.

### Prior art

Rowhammer, CPU cache attacks and JavaScript microarchitectural attacks were
known. The GPU execution, cache reverse engineering and remote WebGL delivery
are a material new attack path.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 88 | 25% | 22.00 | First complete WebGL/GPU microarchitectural browser compromise. |
| Transferability | 82 | 20% | 16.40 | General concept, though hardware details vary by GPU. |
| Lasting value | 91 | 20% | 18.20 | Extends browser threat models to accelerators. |
| Technical soundness | 93 | 15% | 13.95 | Reverse engineering and end-to-end exploitation are rigorous. |
| Practical usability | 74 | 10% | 7.40 | Requires device-specific shader and cache work. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Primitives and exploit chain are carefully described. |

**Final score: 86.8/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It moves established microarchitectural attacks onto a
browser-accessible accelerator and demonstrates a qualitatively stronger chain.

## 86.7 — [Cloud Strife: Mitigating the Security Risks of Domain-Validated Certificates](https://www.ndss-symposium.org/wp-content/uploads/2018/02/ndss2018_06A-4_Borgolte_paper.pdf) — Kevin Borgolte, Tobias Fiebig, Shuang Hao, Christopher Kruegel, Giovanni Vigna

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2018.

### Core contribution

Attackers reacquire released cloud IP addresses still referenced by stale DNS,
then inherit traffic and domain-validation trust. The study quantifies the
problem at scale, demonstrates DNS-cache use-after-free and proposes automatic
validation of certificate issuance against cloud address churn.

### Prior art

Dangling DNS records, cloud IP reuse and domain validation weaknesses were
known separately. The systematic reacquisition workflow, measured exposure and
certificate-issuance consequence form the qualifying extension.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | New practical IP-use-after-free path to residual domain trust. |
| Transferability | 91 | 20% | 18.20 | Applies across elastic clouds, DNS caches and DV CAs. |
| Lasting value | 86 | 20% | 17.20 | Durable cloud offboarding and certificate-validation lesson. |
| Technical soundness | 92 | 15% | 13.80 | Acquisition experiments and measurements substantiate impact. |
| Practical usability | 82 | 10% | 8.20 | Reproducible with cloud allocation and DNS inspection. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Lifecycle, attacks and mitigations are explicit. |

**Final score: 86.7/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It composes known dangling infrastructure into a measured
and certificate-backed takeover method.

## 86.7 — [Mobile Application Web API Reconnaissance: Web-to-Mobile Inconsistencies & Vulnerabilities](https://people.engr.tamu.edu/guofei/paper/WARDroid_SP18.pdf) — Abner Mendoza, Guofei Gu

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published in May
2018.

### Core contribution

WARDroid statically extracts request templates and client-side validation
constraints from Android apps, then black-box tests the corresponding HTTP APIs
for weaker server checks. Its 10,000-app study exposes Web API hijacking paths
that ordinary server-only testing cannot infer.

### Prior art

Never trust client validation and API parameter tampering were established.
The new contribution is mining the shipped client as an executable
specification for automated server-side differential testing.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 84 | 25% | 21.00 | Novel client-derived constraint oracle for remote APIs. |
| Transferability | 91 | 20% | 18.20 | General to mobile clients backed by HTTP services. |
| Lasting value | 84 | 20% | 16.80 | Durable method for client/server semantic comparison. |
| Technical soundness | 91 | 15% | 13.65 | Static extraction, black-box validation and scale support it. |
| Practical usability | 82 | 10% | 8.20 | Automates discovery otherwise requiring manual reversing. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Templates, constraints and testing stages are clear. |

**Final score: 86.7/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. The bug class is old; the transferable
advance is deriving targeted API tests from mobile client code.

## 86.6 — [SYNODE: Understanding and Automatically Preventing Injection Attacks on Node.js](https://www.software-lab.org/publications/ndss2018.pdf) — Cristian-Alexandru Staicu, Michael Pradel, Benjamin Livshits

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2018.

### Core contribution

The study maps `eval` and `exec` injection across 235,850 Node.js modules.
SYNODE statically derives value templates at dangerous APIs and synthesizes
grammar-based runtime policies that block injections with sub-millisecond
overhead and few false positives.

### Prior art

Server-side JavaScript injection and command injection were public, including a
2011 nomination. The large ecosystem analysis plus template-to-policy
mitigation is a new reusable method rather than a renamed injection bug.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 76 | 25% | 19.00 | New template-derived policy method for Node.js injection. |
| Transferability | 93 | 20% | 18.60 | Covers module composition and multiple dangerous API families. |
| Lasting value | 89 | 20% | 17.80 | Durable model for ecosystem-scale injection controls. |
| Technical soundness | 92 | 15% | 13.80 | Large study and measured enforcement support the claims. |
| Practical usability | 85 | 10% | 8.50 | Deploys without modifying the Node.js platform. |
| Clarity and reproducibility | 89 | 10% | 8.90 | Analysis and policy construction are well specified. |

**Final score: 86.6/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It advances known injection classes with
a Node-specific, module-aware discovery and enforcement pipeline.

## 86.5 — [NAVEX: Precise and Scalable Exploit Generation for Dynamic Web Applications](https://www-personal.umd.umich.edu/~birhanu/dsplab/publications/navex-2018/) — Abeer Alhuzali, Rigel Gjomemo, Birhanu Eshete, V. N. Venkatakrishnan

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in 2018; the author publication
record and open paper establish the date.

### Core contribution

NAVEX combines static analysis, crawling, concrete-symbolic execution and a
navigation graph to generate complete multi-request exploits for dynamic PHP
applications. It produced 204 working exploits across 3.2 million lines of
code, including injection and logic vulnerabilities.

### Prior art

Static taint analysis, concolic execution and earlier exploit generators were
known. NAVEX's qualifying contribution is joining dynamic content discovery to
path-sensitive server analysis and request-sequence generation at scale.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | New hybrid path-to-request-sequence exploit pipeline. |
| Transferability | 87 | 20% | 17.40 | Method spans several web vulnerability classes. |
| Lasting value | 87 | 20% | 17.40 | Durable blueprint for validated exploit generation. |
| Technical soundness | 93 | 15% | 13.95 | 204 concrete exploits provide strong confirmation. |
| Practical usability | 82 | 10% | 8.20 | Automated, though the implementation targets PHP. |
| Clarity and reproducibility | 91 | 10% | 9.10 | Components, graph and evaluation are detailed. |

**Final score: 86.5/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It makes dynamic multi-tier exploitability
testable rather than merely reporting potential sinks.

## 86.5 — [WPSE: Fortifying Web Protocols via Browser-Side Security Monitoring](https://www.usenix.org/conference/usenixsecurity18/presentation/calzavara) — Stefano Calzavara, Riccardo Focardi, Matteo Maffei, Clara Schneidewind, Marco Squarcina, Mauro Tempesta

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2018.

### Core contribution

WPSE turns intended OAuth and SAML flows into browser-side confidentiality,
integrity and sequencing monitors. Formalizing those flows found a new Google
SAML attack and flaws on 55 of 90 OAuth sites, including tracking-library
interference, while remaining compatible with most tested sites.

### Prior art

OAuth/SAML implementation flaws and formal protocol analysis were established.
The reusable browser monitor that both discovers and blocks deviations is the
qualifying methodology.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78 | 25% | 19.50 | Novel executable browser monitor for protocol invariants. |
| Transferability | 91 | 20% | 18.20 | Applies across sites and multiple web authentication protocols. |
| Lasting value | 88 | 20% | 17.60 | Durable model for client-observed protocol enforcement. |
| Technical soundness | 94 | 15% | 14.10 | Formal proof and broad empirical evaluation agree. |
| Practical usability | 80 | 10% | 8.00 | Deployable monitor with high compatibility. |
| Clarity and reproducibility | 91 | 10% | 9.10 | Policies, attacks and evaluation are explicit. |

**Final score: 86.5/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It systematizes protocol-flow testing and
enforcement beyond individual OAuth or SAML bugs.

## 85.0 — [Clock Around the Clock: Time-Based Device Fingerprinting](https://www.eurecom.edu/publication/5664/download/sec-publi-5664.pdf) — Iskander Sanchez-Rola, Igor Santos, Davide Balzarotti

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed ACM CCS paper published in October 2018.

### Core contribution

The technique measures execution-time variation caused by physical clock
crystal imperfections and ports the classifier to HTML5/JavaScript for remote
device fingerprinting. It identifies hardware without relying on the ordinary
software and configuration attributes exposed by browser APIs.

### Prior art

Clock-skew fingerprinting, performance timing and browser fingerprints were
known. Measuring manufacturing variation in the execution clock through a web
workload supplies a different physical identifier and oracle.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 87 | 25% | 21.75 | New remote fingerprint derived from clock-crystal variation. |
| Transferability | 88 | 20% | 17.60 | Web implementation applies across software identities. |
| Lasting value | 81 | 20% | 16.20 | Durable warning about hardware signals behind browser APIs. |
| Technical soundness | 87 | 15% | 13.05 | Native and web experiments support the physical model. |
| Practical usability | 78 | 10% | 7.80 | Requires repeated timing samples and calibration. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Measurement and classifier are described clearly. |

**Final score: 85.0/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It derives a browser-visible device identity from physical
clock variation rather than conventional browser attributes.

## 85.0 — [Vetting Single Sign-On SDK Implementations via Symbolic Reasoning](https://www.usenix.org/conference/usenixsecurity18/presentation/yang) — Ronghai Yang, Wing Cheong Lau, Jiongyi Chen, Kehuan Zhang

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2018.

### Core contribution

S3KVetter symbolically reasons over SDK APIs, protocol messages and attacker
actions to test the logical correctness of ten widely deployed SSO SDKs. It
finds seven flaw classes, including four previously unknown classes, at the
shared component layer used by many applications.

### Prior art

SSOScan and manual OAuth/SAML testing predate 2018. This work shifts systematic
reasoning into reusable SDK implementations and models their framework-specific
control and data flows.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 76 | 25% | 19.00 | New symbolic vetting method at the SSO SDK layer. |
| Transferability | 89 | 20% | 17.80 | One SDK finding propagates to many relying applications. |
| Lasting value | 86 | 20% | 17.20 | Durable supply-chain view of authentication logic. |
| Technical soundness | 92 | 15% | 13.80 | Ten SDKs and confirmed flaw classes support the method. |
| Practical usability | 83 | 10% | 8.30 | Automated tests target deployable components. |
| Clarity and reproducibility | 89 | 10% | 8.90 | Model, tool and findings are well documented. |

**Final score: 85.0/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. The advance is reusable symbolic testing
of SDK logic, not another isolated SSO implementation bug.

## 84.6 — [Deep Fingerprinting: Undermining Website Fingerprinting Defenses with Deep Learning](https://arxiv.org/abs/1801.02265) — Payap Sirinam, Mohsen Imani, Marc Juarez, Matthew Wright

**KEPT** · Meaningful extension · confidence High

### Candidate

The primary preprint was published on 7 January 2018 and the paper appeared at
ACM CCS in October 2018.

### Core contribution

Deep Fingerprinting applies a purpose-built convolutional network to encrypted
Tor traffic. It exceeds 98% accuracy without defenses, remains above 90%
against WTF-PAD, and achieves strong open-world precision and recall where
earlier attacks or hand-engineered features degraded.

### Prior art

Website fingerprinting and deep-learning classifiers were already public,
including a 2017 automated-feature paper. The defense-resistant architecture
and realistic open-world evaluation are the meaningful extension.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 75 | 25% | 18.75 | Material new CNN architecture and defense evaluation. |
| Transferability | 85 | 20% | 17.00 | Applies to encrypted web traffic and multiple Tor settings. |
| Lasting value | 91 | 20% | 18.20 | Became a durable baseline for website-fingerprinting defenses. |
| Technical soundness | 91 | 15% | 13.65 | Closed/open-world and defended experiments are rigorous. |
| Practical usability | 80 | 10% | 8.00 | Training is substantial but the classifier is actionable. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Architecture, datasets and metrics are explicit. |

**Final score: 84.6/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It is not the first learned website fingerprint, but it
changes the attack's effectiveness against then-current defenses.

## 84.5 — [O Single Sign-Off, Where Art Thou? An Empirical Analysis of Single Sign-On Account Hijacking and Session Management on the Web](https://www.usenix.org/conference/usenixsecurity18/presentation/ghasemisharif) — Mohammad Ghasemisharif, Amrutha Ramesh, Stephen Checkoway, Chris Kanich, Jason Polakis

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2018.

### Core contribution

The work shows that compromising an identity-provider session creates durable,
distributed relying-party accounts and sessions that password changes or IdP
logout do not reliably revoke. It validates attacks against 95 services and
proposes an OpenID Connect Single Sign-Off mechanism for global remediation.

### Prior art

Cookie theft, SSO account takeover and incomplete logout were known. The new
contribution is systematic cross-service persistence analysis and a protocol
mechanism to revoke the resulting account graph.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78 | 25% | 19.50 | Systematizes persistent SSO compromise across relying parties. |
| Transferability | 88 | 20% | 17.60 | Applies across major IdPs, web and mobile services. |
| Lasting value | 86 | 20% | 17.20 | Durable session-revocation and incident-response insight. |
| Technical soundness | 90 | 15% | 13.50 | Attacks against 95 services validate the model. |
| Practical usability | 78 | 10% | 7.80 | Testing is accessible; complete remediation needs protocol adoption. |
| Clarity and reproducibility | 89 | 10% | 8.90 | Attack and recovery states are clearly separated. |

**Final score: 84.5/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It broadens session hijacking into a reusable SSO
persistence and remediation model.

## 84.0 — [Adventures in Video Conferencing Part 1: The Wild World of WebRTC](https://projectzero.google/2018/12/adventures-in-video-conferencing-part-1.html) — Natalie Silvanovich

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Google Project Zero published the five-part primary research series from 4 to
13 December 2018.

### Core contribution

The research constructs packet recording, mutation and replay tooling around
RTP and encrypted video-call implementations, then finds 11 serious bugs in
WebRTC, FaceTime and WhatsApp. Many appeared within 15 minutes of live-stream
mutation fuzzing; the released Street Party tools make the workflow reusable.

### Prior art

Codec fuzzing, network mutation and individual WebRTC vulnerabilities were
known. The protocol-aware live-call capture/replay pipeline and its
cross-implementation results are the qualifying methodology.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 74 | 25% | 18.50 | New end-to-end RTP mutation workflow for calling stacks. |
| Transferability | 87 | 20% | 17.40 | Demonstrated across three major implementations. |
| Lasting value | 83 | 20% | 16.60 | Durable method for pre-answer media attack surfaces. |
| Technical soundness | 91 | 15% | 13.65 | Eleven fixed bugs and reproducible crashes validate it. |
| Practical usability | 88 | 10% | 8.80 | Released capture, replay and mutation tooling. |
| Clarity and reproducibility | 90 | 10% | 9.00 | The series explains architecture, setup and results. |

**Final score: 84.0/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. The novelty lies in making encrypted,
stateful video-call media streams efficiently fuzzable end to end.

## 83.9 — [A Sense of Time for JavaScript and Node.js: First-Class Timeouts as a Cure for Event Handler Poisoning](https://www.usenix.org/conference/usenixsecurity18/presentation/davis) — James C. Davis, Eric R. Williamson, Dongyoon Lee

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2018.

### Core contribution

The paper names and models Event Handler Poisoning: a small attacker workload
monopolizes a shared event-loop handler and denies service to all clients. It
maps vulnerable Node.js APIs and implements first-class timeouts throughout V8,
libuv and core libraries.

### Prior art

Algorithmic-complexity DoS, blocking calls and event-loop starvation were
known. The unified EDA threat model, ecosystem audit and framework-level timeout
semantics are a meaningful extension.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 72 | 25% | 18.00 | Unifies several blocking causes under an EDA security model. |
| Transferability | 89 | 20% | 17.80 | Applies to Node.js and other event-driven servers. |
| Lasting value | 88 | 20% | 17.60 | Durable availability model for cooperative event loops. |
| Technical soundness | 90 | 15% | 13.50 | Ecosystem evidence and full-stack prototype support it. |
| Practical usability | 82 | 10% | 8.20 | Guidance is immediate; full defense needs runtime changes. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Attack taxonomy and timeout design are clear. |

**Final score: 83.9/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It turns familiar blocking bugs into a general event-loop
attack model with enforceable resource boundaries.

## 83.3 — [Mystique: Uncovering Information Leakage from Browser Extensions](https://www.kapravelos.com/publications/mystique-CCS18.pdf) — Quan Chen, Alexandros Kapravelos

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

The author announced acceptance in July 2018 and the peer-reviewed paper
appeared at ACM CCS in October 2018.

### Core contribution

Mystique combines static dependencies with full V8 runtime taint tracking for
extension APIs and DOM flows. It analyzed 181,683 Chrome and Opera extensions,
flagged 3,868 potential privacy leaks, and detected obfuscation missed by prior
source-pattern approaches.

### Prior art

Malicious extensions, Firefox taint tracking and signature-based extension
auditing were known. Full hybrid information-flow tracking inside Chromium/V8
and extension-specific sources and sinks form the new method.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 75 | 25% | 18.75 | First complete hybrid taint framework for Chromium extensions. |
| Transferability | 86 | 20% | 17.20 | Covers many extension APIs, data types and obfuscations. |
| Lasting value | 83 | 20% | 16.60 | Durable model for privileged browser add-on analysis. |
| Technical soundness | 91 | 15% | 13.65 | Large-scale run and manual validation support it. |
| Practical usability | 82 | 10% | 8.20 | Open framework supports store-scale triage. |
| Clarity and reproducibility | 89 | 10% | 8.90 | Taint propagation and evaluation are detailed. |

**Final score: 83.3/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It is semantically distinct from the
existing general Chrome-extension auditing nomination.

## 82.7 — [Automated Generation of Event-Oriented Exploits in Android Hybrid Apps](https://www.ndss-symposium.org/wp-content/uploads/2018/02/ndss2018_04B-3_Yang_paper.pdf) — Guangliang Yang, Jeff Huang, Guofei Gu

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2018.

### Core contribution

EOEDroid models WebView callbacks as event-oriented gadgets, searches state and
ordering combinations, and synthesizes triggering inputs. Across 3,652 hybrid
apps it found 97 vulnerabilities in 58 apps, including cross-frame DOM changes,
credential phishing, native resource access and intent abuse.

### Prior art

WebView bridge flaws and individual callback mistakes were known. Automatic
composition of callback ordering and program state into exploit sequences is a
new reusable analysis method.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78 | 25% | 19.50 | New event-gadget model and exploit-sequence generation. |
| Transferability | 86 | 20% | 17.20 | Applies across hybrid apps and callback families. |
| Lasting value | 82 | 20% | 16.40 | Durable model for stateful bridge exploitation. |
| Technical soundness | 88 | 15% | 13.20 | Population study and 97 findings support the approach. |
| Practical usability | 79 | 10% | 7.90 | Automated but tied to Android/WebView analysis. |
| Clarity and reproducibility | 85 | 10% | 8.50 | Events, gadgets and evaluation are clearly presented. |

**Final score: 82.7/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It advances known WebView problems with
state- and order-aware automatic exploit generation.

## 82.6 — [Riding out DOMsday: Towards Detecting and Preventing DOM Cross-Site Scripting](https://www.ndss-symposium.org/wp-content/uploads/2018/02/ndss2018_07A-4_Melicher_paper.pdf) — William Melicher, Anupam Das, Mahmood Sharif, Lujo Bauer, Limin Jia

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2018.

### Core contribution

An instrumented browser tracks attacker-controlled URL flows through the
JavaScript engine and improves concrete exploit confirmation. It finds 83% more
DOM-XSS flaws than the prior confirmation method and shows static tools miss 90%
of dynamically observed bugs.

### Prior art

DOMinator and a 2013 large-scale DOM-XSS detector were already nominated. The
qualifying advance is substantially better exploit confirmation plus a direct
comparison of dynamic and static failure modes.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 70 | 25% | 17.50 | Improves confirmation rather than inventing DOM-XSS analysis. |
| Transferability | 88 | 20% | 17.60 | Applies to modern client-side JavaScript at web scale. |
| Lasting value | 82 | 20% | 16.40 | Durable evidence for exploit-confirming dynamic analysis. |
| Technical soundness | 90 | 15% | 13.50 | Comparative crawl and manual analysis support it. |
| Practical usability | 86 | 10% | 8.60 | Produces confirmed, actionable flows. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Methodology, baselines and error rates are explicit. |

**Final score: 82.6/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It materially advances established
DOM-XSS detection rather than duplicating the original technique.

## 82.4 — [Freezing the Web: A Study of ReDoS Vulnerabilities in JavaScript-based Web Servers](https://www.usenix.org/conference/usenixsecurity18/presentation/staicu) — Cristian-Alexandru Staicu, Michael Pradel

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2018.

### Core contribution

The authors find 25 unknown ReDoS flaws in popular modules, infer how deployed
servers invoke them and craft targeted probes. Testing 2,846 sites confirms 339
vulnerable deployments, connecting library-level worst cases to remotely
reachable production paths.

### Prior art

ReDoS and algorithmic-complexity attacks long predate 2018. The new contribution
is a scalable library-to-deployment exploitability methodology with confirmed
live-site results.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 68 | 25% | 17.00 | Novel deployment-exploitability workflow for known ReDoS. |
| Transferability | 88 | 20% | 17.60 | Applies across modules and JavaScript web services. |
| Lasting value | 84 | 20% | 16.80 | Durable supply-chain-to-production testing model. |
| Technical soundness | 90 | 15% | 13.50 | 25 module flaws and 339 affected sites validate it. |
| Practical usability | 87 | 10% | 8.70 | Produces focused probes for deployed services. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Inference and validation stages are explicit. |

**Final score: 82.4/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. The method determines whether a known
library flaw is actually exposed through a site's request handling.

## 82.1 — [Security Risks in Asynchronous Web Servers: When Performance Optimizations Amplify the Impact of Data-Oriented Attacks](https://fabianmonrose.github.io/papers/morton18.pdf) — Micah Morton et al.

**KEPT** · Meaningful combination or adaptation · confidence High

### Candidate

Peer-reviewed IEEE EuroS&P paper published in April 2018.

### Core contribution

Because asynchronous servers handle unrelated clients inside one process,
small data-only corruptions can rewrite shared live configuration. The Nginx
case studies disable HSTS and access control, steal data or substitute content
without conventional control-flow hijacking.

### Prior art

Memory corruption, data-oriented programming and asynchronous server designs
were established. Connecting shared-request architecture to persistent,
cross-client security-policy corruption is the qualifying adaptation.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 83 | 25% | 20.75 | New cross-client consequences for data-only server corruption. |
| Transferability | 80 | 20% | 16.00 | General architecture issue, though demonstrated chiefly on Nginx. |
| Lasting value | 82 | 20% | 16.40 | Durable warning about isolation traded for throughput. |
| Technical soundness | 89 | 15% | 13.35 | Live-memory tracing and CVE case studies support it. |
| Practical usability | 70 | 10% | 7.00 | Requires a memory-corruption foothold and target analysis. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Data discovery and overwrite effects are detailed. |

**Final score: 82.1/100.** Archive decision: include as a core technique.

### Verdict

Meaningful combination or adaptation. It reveals a distinct security impact
created when data-oriented attacks meet shared asynchronous request state.

## 64.5 — [Security Analysis of eIDAS — The Cross-Country Authentication Scheme in Europe](https://www.usenix.org/conference/woot18/workshop-program) — Nils Engelbertz, Nurullah Erinola, David Herring, Juraj Somorovsky, Vladislav Mladenov, Jörg Schwenk

**KEPT** · Tooling or methodology contribution · confidence Medium

### Candidate

Peer-reviewed WOOT paper published in August 2018. The workshop program is the
primary conference record and links the paper and materials.

### Core contribution

The study adapts XML and SAML security testing to 15 interoperating national
eID services and packages automated and semi-automated checks as a Burp Suite
extension. Seven services allowed XML attacks and five allowed local-file
exfiltration to an attacker domain.

### Prior art

XXE, SSRF, SAML wrapping and XML denial-of-service techniques were well known,
including earlier nominations. The limited qualifying advance is a reusable
eIDAS-aware test harness plus the first cross-country implementation study.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 45 | 25% | 11.25 | Primarily adapts established XML/SAML attacks. |
| Transferability | 68 | 20% | 13.60 | Reusable across eIDAS nodes and related SAML services. |
| Lasting value | 60 | 20% | 12.00 | Valuable interoperability audit, but target-specific. |
| Technical soundness | 80 | 15% | 12.00 | Fifteen live services and confirmed effects support it. |
| Practical usability | 74 | 10% | 7.40 | Burp extension makes the checks accessible. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Attack set, affected services and guidance are clear. |

**Final score: 64.5/100.** Archive decision: include as qualifying material.

### Verdict

Tooling or methodology contribution. It narrowly clears the 60-point rule due
to the reusable test harness and cross-implementation method, not because the
underlying XML attacks are new.
## 88.1 — [Ruby 2.x Universal RCE Deserialization Gadget Chain](https://www.elttam.com/blog/ruby-deserialization) — Luke Jahnke, elttam

**KEPT** · Original technique · confidence High

### Candidate

Published 8 November 2018. A single `Marshal.load` of attacker-controlled bytes
is turned into command execution using only classes shipped with Ruby itself.

### Core contribution

The first public universal deserialization gadget chain for Ruby. It chains
`Gem::Requirement#marshal_load` into `Gem::DependencyList` sorting, through
`Gem::Source::SpecificFile` comparison, to `Gem::StubSpecification`, reaching
`Kernel.open` with a leading pipe character so the argument is executed as a
command. The write-up also introduced programmatic gadget hunting across the
Ruby standard library rather than hand-inspection.

### Prior art

Rails-specific chains existed from 2013 (Hailey Somerville), and Java and PHP
object-injection chains were well established. Every earlier Ruby result needed
ActiveSupport, ERB, or a method call made after deserialization, so it applied
only inside Rails. The distinct contribution is showing the standard library
alone suffices, which made every Ruby application reachable.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 88 | 25% | 22.00 | First universal Ruby chain; removed the Rails precondition entirely. |
| Transferability | 85 | 20% | 17.00 | Applies to any Ruby application reaching `Marshal.load`; the hunting method ports to other runtimes. |
| Lasting value | 92 | 20% | 18.40 | Eight years of successor chains (2019, 2021, 2022, 2024, 2026) descend from and cite it. |
| Technical soundness | 88 | 15% | 13.20 | Complete chain with working payload and version coverage for Ruby 2.0-2.5. |
| Practical usability | 90 | 10% | 9.00 | Directly usable; reproduced in PayloadsAllTheThings and a PentesterLab exercise. |
| Clarity and reproducibility | 85 | 10% | 8.50 | Each gadget is named with its source and the reasoning behind its selection. |

**Final score: 88.1/100.** Archive decision: include as a core technique.

### Verdict

Original technique. Ruby deserialization was considered impractical outside
Rails before this; afterwards it was a standing, universal risk.
