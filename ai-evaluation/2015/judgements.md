# 2015 candidate judgements

These scorecards apply the repository's weighted judge rubric. `KEPT` means
the candidate met the 60-or-above gate plus the first-publication-year,
qualifying-verdict and original-nomination exclusions. Screened leads remain in
the companion README.

## 89.7 — [Critical Vulnerabilities in JSON Web Token Libraries](https://www.chosenplaintext.ca/2015/03/31/jwt-algorithm-confusion.html) — Tim McLean

**KEPT** · Original technique · confidence High

### Candidate

Primary researcher disclosure published 31 March 2015, with an April update and
contemporaneous library fixes.

### Core contribution

An attacker changes a JWT algorithm to `none`, or changes RSA/ECDSA to HMAC so
the verifier's public key becomes an attacker-known MAC secret. Vulnerable
libraries then accept unsigned or attacker-signed identity and authorization
claims despite correct application-level key configuration.

### Prior Art

Algorithm downgrades and signature-confusion bugs existed, but no earlier public
source located described this attacker-controlled JWT verification dispatch or
the asymmetric-public-key-as-HMAC-secret construction across libraries.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 92/100 | 25% | 23.00/25 | Defines two new JWT verification-confusion attacks. |
| Transferability | 94/100 | 20% | 18.80/20 | Applies across languages, frameworks and token consumers. |
| Lasting value | 92/100 | 20% | 18.40/20 | Algorithm pinning remains fundamental JWT guidance. |
| Technical soundness | 89/100 | 15% | 13.35/15 | Multiple libraries and working constructions corroborate it. |
| Practical usability | 86/100 | 10% | 8.60/10 | Simple token edits make the test directly actionable. |
| Clarity and reproducibility | 76/100 | 10% | 7.60/10 | Concise code and examples identify both conditions. |

**Final score: 89.7/100.** Archive decision: include as a core technique.

### Verdict

Original technique. The security boundary broken is JWT's attacker-selected
verification algorithm, not generic weak cryptography.

## 89.3 — [A Messy State of the Union: Taming the Composite State Machines of TLS](https://www.ieee-security.org/TC/SP2015/papers-archived/6949a535.pdf) — Benjamin Beurdouche, Karthikeyan Bhargavan, Antoine Delignat-Lavaud, Cédric Fournet, Markulf Kohlweiss, Alfredo Pironti, Pierre-Yves Strub, Jean Karim Zinzindohoue

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published May 2015.

### Core contribution

The work derives a composite TLS state machine, builds a systematic message-
sequence test harness, and finds skipped, reordered and unauthenticated states
in six of eight major implementations. Ten attacks, including eight
impersonations, show why correct cryptographic primitives do not guarantee a
correct protocol implementation.

### Prior Art

TLS state machines, message fuzzing and individual downgrade flaws predate the
paper; FREAK is also separately nominated. The qualifying advance is the
cross-implementation compositional model and sequence-testing methodology that
revealed several additional, independent state-machine attacks.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 87/100 | 25% | 21.75/25 | New compositional TLS testing model and attack set. |
| Transferability | 90/100 | 20% | 18.00/20 | General to complex protocol implementations and versions. |
| Lasting value | 92/100 | 20% | 18.40/20 | State-machine conformance remains a core protocol audit. |
| Technical soundness | 96/100 | 15% | 14.40/15 | Formal model, broad implementation study and vendor fixes. |
| Practical usability | 78/100 | 10% | 7.80/10 | Requires protocol expertise but gives concrete sequences. |
| Clarity and reproducibility | 89/100 | 10% | 8.90/10 | Machines, traces, implementations and fixes are detailed. |

**Final score: 89.3/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. Its reusable value exceeds the already
nominated FREAK instance and covers a distinct class of sequence errors.

## 88.6 — [The Spy in the Sandbox: Practical Cache Attacks in JavaScript and their Implications](https://arxiv.org/abs/1502.07373) — Yossef Oren, Vasileios P. Kemerlis, Simha Sethumadhavan, Angelos D. Keromytis

**KEPT** · Original technique · confidence High

### Candidate

First publicly posted 25 February 2015 and peer-reviewed at ACM CCS 2015; an
author-hosted paper corroborates the conference version.

### Core contribution

Ordinary JavaScript in a remote page constructs an eviction set and performs a
last-level-cache Prime+Probe attack without native code or shared memory. The
page observes cross-process, cross-user and cross-VM activity, defeating the
assumption that the browser sandbox excludes microarchitectural attackers.

### Prior Art

Native cache attacks and browser timing channels were known. Earlier web work
did not implement a general last-level-cache attack entirely in sandboxed
JavaScript or demonstrate activity monitoring across these isolation borders.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 92/100 | 25% | 23.00/25 | First general LLC attack from sandboxed JavaScript. |
| Transferability | 91/100 | 20% | 18.20/20 | Crosses processes, users, VMs and browser targets. |
| Lasting value | 90/100 | 20% | 18.00/20 | Founded the modern browser microarchitecture line. |
| Technical soundness | 91/100 | 15% | 13.65/15 | End-to-end implementation and experiments validate it. |
| Practical usability | 75/100 | 10% | 7.50/10 | Hardware calibration is needed but the page is remote. |
| Clarity and reproducibility | 82/100 | 10% | 8.20/10 | Construction and experimental conditions are explicit. |

**Final score: 88.6/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It introduces a browser-delivered microarchitectural attack
primitive, not merely another server-response timing test.

## 88.0 — [Rowhammer.js: A Remote Software-Induced Fault Attack in JavaScript](https://arxiv.org/abs/1507.06955) — Daniel Gruss, Clémentine Maurice, Stefan Mangard

**KEPT** · Original technique · confidence High

### Candidate

Primary paper first publicly posted 24 July 2015. Its later DIMVA 2016 venue does
not displace the repository's first-publication-year rule.

### Core contribution

A website uses JavaScript cache-eviction strategies instead of privileged flush
instructions to induce DRAM bit flips, with automated physical-memory templating
and no local binary. This turns Rowhammer into a remote browser-delivered fault
attack capable of breaking sandbox and memory isolation assumptions.

### Prior Art

The 2014 native Rowhammer mechanism and cache eviction were known separately.
The remote JavaScript delivery, eviction construction and automated end-to-end
browser attack were new.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 92/100 | 25% | 23.00/25 | First remote JavaScript Rowhammer construction. |
| Transferability | 82/100 | 20% | 16.40/20 | General browser path, subject to vulnerable DRAM/hardware. |
| Lasting value | 90/100 | 20% | 18.00/20 | Durable example of web-to-hardware exploitation. |
| Technical soundness | 92/100 | 15% | 13.80/15 | Automated experiments and working faults support it. |
| Practical usability | 80/100 | 10% | 8.00/10 | Remote delivery is simple though hardware-sensitive. |
| Clarity and reproducibility | 88/100 | 10% | 8.80/10 | Algorithms, assumptions and results are detailed. |

**Final score: 88.0/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It creates a distinct browser-based route to software-
induced hardware faults.

## 87.5 — [Protocol State Fuzzing of TLS Implementations](https://www.usenix.org/conference/usenixsecurity15/technical-sessions/presentation/de-ruiter) — Joeri de Ruiter, Erik Poll

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published August 2015.

### Core contribution

Active automata learning probes TLS clients and servers as black boxes, infers
their actual state machines and makes unexpected transitions visually obvious.
The method found new logic flaws in GnuTLS, JSSE and OpenSSL and also produced
implementation fingerprints.

### Prior Art

Message fuzzing and manual protocol-state review existed. The distinct advance
is black-box state-machine inference over message sequences, rather than
mutating one message or assuming the implementation follows its specification.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 80/100 | 25% | 20.00/25 | New automated state-learning audit for deployed TLS. |
| Transferability | 90/100 | 20% | 18.00/20 | Applies to clients, servers and other stateful protocols. |
| Lasting value | 91/100 | 20% | 18.20/20 | Protocol-state fuzzing remains an active methodology. |
| Technical soundness | 94/100 | 15% | 14.10/15 | Multiple implementations and confirmed flaws validate it. |
| Practical usability | 82/100 | 10% | 8.20/10 | Automated inference reduces a difficult manual task. |
| Clarity and reproducibility | 90/100 | 10% | 9.00/10 | Harness, machines and findings are documented. |

**Final score: 87.5/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It is separable from the white-box and
formal composite-state analysis scored above.

## 87.2 — [Identifying Cross-origin Resource Status Using Application Cache](https://www.ndss-symposium.org/ndss2015/ndss-2015-programme/identifying-cross-origin-resource-status-using-application-cache/) — Sangho Lee, Hyungsub Kim, Jong Kim

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed NDSS paper published 8 February 2015.

### Core contribution

An attacker-controlled AppCache manifest turns cache-selection behavior into a
scriptless cross-origin oracle that distinguishes resource existence,
redirection and error states. Concurrent probes infer login status, intranet
resources and private application state.

### Prior Art

AppCache poisoning was public in 2010, and browser-history or timing probes were
known. Those do not use AppCache fallback/selection semantics as a status oracle
or provide this concurrent, scriptless cross-origin probing mechanism.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 88/100 | 25% | 22.00/25 | New AppCache-based cross-origin status oracle. |
| Transferability | 87/100 | 20% | 17.40/20 | Targets many resources and state-dependent endpoints. |
| Lasting value | 84/100 | 20% | 16.80/20 | Foundational pattern despite AppCache retirement. |
| Technical soundness | 93/100 | 15% | 13.95/15 | Formal cases and broad browser demonstrations agree. |
| Practical usability | 82/100 | 10% | 8.20/10 | Straightforward manifest and resource probes. |
| Clarity and reproducibility | 88/100 | 10% | 8.80/10 | Attack states and examples are precise. |

**Final score: 87.2/100.** Archive decision: include as a core technique.

### Verdict

Original technique. The AppCache status primitive is distinct from both earlier
cache poisoning and the later post-download timing channels in Clock.

## 86.6 — [Cookies Lack Integrity: Real-World Implications](https://www.usenix.org/conference/usenixsecurity15/technical-sessions/presentation/zheng) — Xiaofeng Zheng, Jian Jiang, Jinjin Liang, Haixin Duan, Shuo Chen, Tao Wan, Nicholas Weaver

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed USENIX Security paper published August 2015.

### Core contribution

An HTTP network attacker or related-domain attacker injects cookies that a
browser later sends over HTTPS, overriding application state and enabling
account compromise, privacy loss and financial attacks. The paper systematically
maps browser rules and demonstrates exploitable Google and banking workflows.

### Prior Art

Cookie forcing and the absence of a cookie integrity attribute were public by
2006. This is not credited as the original primitive; it qualifies through the
first broad browser/application study, new overwrite variants, real high-impact
exploit chains and implementation fixes.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 76/100 | 25% | 19.00/25 | Major systematisation and new exploit variants. |
| Transferability | 91/100 | 20% | 18.20/20 | General to HTTP/HTTPS sites and related domains. |
| Lasting value | 90/100 | 20% | 18.00/20 | Cookie integrity remains a deployment concern. |
| Technical soundness | 94/100 | 15% | 14.10/15 | Browser analysis, live attacks and fixes corroborate it. |
| Practical usability | 85/100 | 10% | 8.50/10 | Concrete injection and overwrite cases guide testing. |
| Clarity and reproducibility | 88/100 | 10% | 8.80/10 | Rules, traces and demonstrations are explicit. |

**Final score: 86.6/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. Prior cookie forcing is expressly preserved; the 2015
contribution is the transferable modern attack and evaluation framework.

## 85.9 — [Detecting and Exploiting Second Order Denial-of-Service Vulnerabilities in Web Applications](https://dl.acm.org/doi/10.1145/2810103.2813680) — Oswaldo Olivo, Isil Dillig, Calvin Lin

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed ACM CCS paper published October 2015; the author PDF supplies the
complete paper and evaluation.

### Core contribution

A low-rate attacker first stores many small records, then triggers an endpoint
whose work grows pathologically over those records. Torpedo combines double
tainting and symbolic execution to find these multi-request amplification paths,
discovering 37 vulnerabilities across six PHP applications.

### Prior Art

Algorithmic-complexity DoS, stored inputs and second-order injection were known.
No earlier source located defined stored-state workload amplification as a web
DoS class or automated its two-stage discovery and exploit construction.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 86/100 | 25% | 21.50/25 | New second-order web DoS class and detector. |
| Transferability | 84/100 | 20% | 16.80/20 | General to persistent records and expensive operations. |
| Lasting value | 86/100 | 20% | 17.20/20 | Durable model for low-rate state amplification. |
| Technical soundness | 92/100 | 15% | 13.80/15 | Static analysis and 37 confirmed findings support it. |
| Practical usability | 80/100 | 10% | 8.00/10 | Tool-generated flows are directly exploitable. |
| Clarity and reproducibility | 86/100 | 10% | 8.60/10 | Threat model, algorithms and cases are detailed. |

**Final score: 85.9/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It is not ordinary volumetric or per-request complexity DoS;
the stored first stage creates the later amplification.

## 85.2 — [Maneuvering Around Clouds: Bypassing Cloud-based Security Providers](https://dl.acm.org/doi/10.1145/2810103.2813633) — Thomas Vissers, Tom Van Goethem, Wouter Joosen, Nick Nikiforakis

**KEPT** · Meaningful combination or adaptation · confidence High

### Candidate

Peer-reviewed ACM CCS paper published October 2015.

### Core contribution

The work combines historical DNS, subdomains, mail infrastructure, certificate
and address-space evidence to rediscover a protected site's origin server, then
connects directly to bypass its cloud WAF and DDoS provider. A measurement study
and practical attacks show widespread incomplete origin hiding.

### Prior Art

Origin-IP discovery tricks, DNS history and direct-origin requests existed
individually. The qualifying contribution is their systematic multi-source
workflow, validation at scale and explicit cloud-security bypass model; it is
not the nominated CDN-based SSRF mechanism.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 81/100 | 25% | 20.25/25 | Coherent new origin-discovery and bypass workflow. |
| Transferability | 89/100 | 20% | 17.80/20 | Applies across cloud security and reverse-proxy providers. |
| Lasting value | 85/100 | 20% | 17.00/20 | Origin exposure remains a common cloud-control failure. |
| Technical soundness | 90/100 | 15% | 13.50/15 | Multi-provider measurement and attacks validate it. |
| Practical usability | 82/100 | 10% | 8.20/10 | Uses accessible data sources and direct tests. |
| Clarity and reproducibility | 85/100 | 10% | 8.50/10 | Discovery channels and validation are documented. |

**Final score: 85.2/100.** Archive decision: include as a core technique.

### Verdict

Meaningful combination or adaptation. Familiar reconnaissance components become
a reusable technique for bypassing a distinct delegated-security boundary.

## 84.8 — [On Subnormal Floating Point and Abnormal Timing](https://www.ieee-security.org/TC/SP2015/papers-archived/6949a623.pdf) — Marc Andrysco, David Kohlbrenner, Keaton Mowery, Ranjit Jhala, Sorin Lerner, Hovav Shacham

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published May 2015.

### Core contribution

x86 floating-point operations take radically different time on subnormal
operands. Carefully selected values and amplification expose cross-origin
Firefox rendering data and defeat timing protections in a differentially private
service, establishing operand-dependent floating point as a remote data channel.

### Prior Art

General timing attacks and the archive's 2013 CSS-filter pixel-recovery attack
predate this paper. The new primitive is same-instruction, same-memory-location
timing dependent on floating-point operand values, with independent browser and
service demonstrations.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 88/100 | 25% | 22.00/25 | First practical floating-point data timing channel. |
| Transferability | 82/100 | 20% | 16.40/20 | Affects browsers and computation over attacker-shaped values. |
| Lasting value | 85/100 | 20% | 17.00/20 | Durable constant-time lesson beyond cryptographic branches. |
| Technical soundness | 94/100 | 15% | 14.10/15 | Benchmarks and two real systems substantiate it. |
| Practical usability | 65/100 | 10% | 6.50/10 | Exploitation needs careful numeric amplification. |
| Clarity and reproducibility | 88/100 | 10% | 8.80/10 | Mechanism, experiments and mitigation library are clear. |

**Final score: 84.8/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It supplies a new processor-level timing primitive rather
than repeating the 2013 CSS-filter attack family.

## 84.5 — [All Your Biases Belong to Us: Breaking RC4 in WPA-TKIP and TLS](https://www.usenix.org/conference/usenixsecurity15/technical-sessions/presentation/vanhoef) — Mathy Vanhoef, Frank Piessens

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed USENIX Security paper published August 2015 and awarded best
student paper.

### Core contribution

New short- and long-term RC4 biases plus improved recovery algorithms let an
attacker inject predictable browser requests and recover an HTTPS secure cookie
with roughly 9×2^27 ciphertexts. The analysis also improves WPA-TKIP plaintext
recovery and unifies exploitation of the newly characterized biases.

### Prior Art

RC4 statistical weaknesses and earlier TLS cookie-recovery attacks were public,
including work already represented in 2013. The qualifying advance is the new
bias set, substantially improved algorithms and experimentally complete HTTPS
cookie recovery, not the original discovery that RC4 is biased.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 75/100 | 25% | 18.75/25 | New biases and recovery procedures extend known RC4 attacks. |
| Transferability | 85/100 | 20% | 17.00/20 | Applies to repeated-secret RC4 uses in TLS and WPA. |
| Lasting value | 90/100 | 20% | 18.00/20 | Strong evidence for removing RC4 from protocols. |
| Technical soundness | 96/100 | 15% | 14.40/15 | Rigorous statistics and full recovery experiments. |
| Practical usability | 72/100 | 10% | 7.20/10 | High sample count, but browser injection is concrete. |
| Clarity and reproducibility | 91/100 | 10% | 9.10/10 | Algorithms and experiments are fully specified. |

**Final score: 84.5/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It materially advances an existing RC4 attack family and
is retained separately from its narrower same-year companion paper.

## 84.2 — [Counterfeit Object-oriented Programming: On the Difficulty of Preventing Code Reuse Attacks in C++ Applications](https://www.ieee-security.org/TC/SP2015/papers-archived/6949a745.pdf) — Felix Schuster, Thomas Tendyck, Christopher Liebchen, Lucas Davi, Ahmad-Reza Sadeghi, Thorsten Holz

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published May 2015.

### Core contribution

COOP corrupts C++ object pointers and chains legitimate virtual-function calls
through existing dispatcher loops. The authors build Turing-complete counterfeit
object programs and end-to-end Internet Explorer 10 and Firefox 36 exploits that
bypass defenses focused on returns or illegal indirect-call targets.

### Prior Art

ROP, vtable corruption and C++ use-after-free exploitation were established.
The distinct primitive is programming with whole legitimate virtual functions
and valid call sites, including a systematic gadget model and browser exploits.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 86/100 | 25% | 21.50/25 | New counterfeit-object code-reuse paradigm. |
| Transferability | 78/100 | 20% | 15.60/20 | General to complex C++ programs, including browsers. |
| Lasting value | 88/100 | 20% | 17.60/20 | Influenced forward-edge CFI and exploit analysis. |
| Technical soundness | 92/100 | 15% | 13.80/15 | Formal expressiveness and two browser exploits support it. |
| Practical usability | 73/100 | 10% | 7.30/10 | Requires memory corruption and target-specific gadgets. |
| Clarity and reproducibility | 84/100 | 10% | 8.40/10 | Object layouts, dispatchers and chains are detailed. |

**Final score: 84.2/100.** Archive decision: include as a core technique.

### Verdict

Original technique. COOP is a distinct browser-relevant code-reuse model, not a
rename of ROP or ordinary vtable hijacking.

## 83.8 — [Perplexed Messengers from the Cloud: Automated Security Analysis of Push-Messaging Integrations](https://dl.acm.org/doi/10.1145/2810103.2813652) — Yangyi Chen, Tongxin Li, Xiaofeng Wang, Kai Chen, Xinhui Han

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed ACM CCS paper published October 2015.

### Core contribution

Seminal extracts security semantics from cloud push-service sample code, then
checks SDKs and 35,173 app integrations for sender, recipient and message-binding
failures. Confused integrations allow attackers to inject trusted-looking
content or intercept private messages across widely deployed cloud APIs.

### Prior Art

Push-token theft, API authorization errors and manual SDK review existed. The
new contribution is a semantic, service-guided integration analysis that finds
cross-party identity confusions across 30 providers at scale.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78/100 | 25% | 19.50/25 | New sample-code-guided semantic analysis and flaw set. |
| Transferability | 88/100 | 20% | 17.60/20 | General to cloud messaging SDKs and API integrations. |
| Lasting value | 82/100 | 20% | 16.40/20 | Durable warning about service/client identity binding. |
| Technical soundness | 94/100 | 15% | 14.10/15 | Thirty services and 35,173 apps support the claims. |
| Practical usability | 77/100 | 10% | 7.70/10 | Automation is strong but service modeling is specialized. |
| Clarity and reproducibility | 85/100 | 10% | 8.50/10 | Properties, analysis and exploit classes are described. |

**Final score: 83.8/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. The reusable advance is auditing trust in
cloud/API integrations, not merely a collection of mobile application bugs.

## 82.7 — [jÄk: Using Dynamic Analysis to Crawl and Test Modern Web Applications](https://publications.cispa.saarland/538/) — Giancarlo Pellegrino, Constantin Tschürtz, Eric Bodden, Christian Rossow

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed RAID paper published November 2015.

### Core contribution

jÄk instruments JavaScript APIs, events, forms, URL construction and network
activity to build a navigation graph of stateful modern applications. Its guided
crawler reaches substantially more dynamic attack surface than four established
scanners and couples exploration with security tests.

### Prior Art

AJAX crawling, event exploration and Crawljax predate the paper. The qualifying
advance is the runtime instrumentation and state/navigation model that recovers
dynamic links and event-driven actions missed by conventional crawlers.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 72/100 | 25% | 18.00/25 | Material dynamic-analysis advance over AJAX crawlers. |
| Transferability | 90/100 | 20% | 18.00/20 | Applies broadly to client-heavy web applications. |
| Lasting value | 83/100 | 20% | 16.60/20 | Dynamic state discovery remains central to scanners. |
| Technical soundness | 90/100 | 15% | 13.50/15 | Comparative evaluation on real apps substantiates it. |
| Practical usability | 80/100 | 10% | 8.00/10 | Produces usable navigation graphs and tests. |
| Clarity and reproducibility | 86/100 | 10% | 8.60/10 | Instrumentation and evaluation are detailed. |

**Final score: 82.7/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It does not invent crawling; it makes
event-driven JavaScript application state materially more discoverable.

## 82.3 — [Cross-Site Search Attacks](https://dl.acm.org/doi/10.1145/2810103.2813688) — Nethanel Gelernter, Amir Herzberg

**KEPT** · Meaningful combination or adaptation · confidence High

### Candidate

Peer-reviewed ACM CCS paper published October 2015.

### Core contribution

Cross-origin timing is amplified through server-side search work and response
behavior, while statistical tests and divide-and-conquer dictionaries recover a
victim's private search terms from services such as Gmail and Bing.

### Prior Art

Web timing attacks, cross-site request triggering and search interfaces were
known, and a generic timing method is an original nominee. The qualifying
advance is the application-level amplification and optimized secret-recovery
algorithm for private search, not a new clock source.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 75/100 | 25% | 18.75/25 | New search-specific amplification and extraction method. |
| Transferability | 86/100 | 20% | 17.20/20 | General to stateful search and dictionary-shaped secrets. |
| Lasting value | 82/100 | 20% | 16.40/20 | Foundational application pattern in XS-Leaks. |
| Technical soundness | 92/100 | 15% | 13.80/15 | Statistical analysis and live services validate it. |
| Practical usability | 76/100 | 10% | 7.60/10 | Query volume and noise matter, but workflow is concrete. |
| Clarity and reproducibility | 86/100 | 10% | 8.60/10 | Tests, algorithms and demonstrations are explicit. |

**Final score: 82.3/100.** Archive decision: include as a core technique.

### Verdict

Meaningful combination or adaptation. It is distinct from Clock's post-download
browser channels and from generic remote timing measurement.

## 82.3 — [Practical Memory Deduplication Attacks in Sandboxed JavaScript](https://gruss.cc/files/dedup.pdf) — Daniel Gruss, David Bidner, Stefan Mangard

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed ESORICS paper published September 2015; the author-hosted accepted
paper and proceedings metadata establish publication.

### Core contribution

A website creates candidate memory pages and times copy-on-write behavior to
detect whether page deduplication merged them with data elsewhere on the system.
It infers running applications and open sites across processes and virtual
machines on servers, desktops and phones without a local attacker binary.

### Prior Art

Native cross-VM deduplication side channels and browser timing attacks existed.
The first sandboxed-JavaScript memory-disclosure construction and cross-platform
remote website delivery are distinct.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82/100 | 25% | 20.50/25 | First deduplication disclosure attack in sandboxed JS. |
| Transferability | 84/100 | 20% | 16.80/20 | Demonstrated across systems, devices and VM boundaries. |
| Lasting value | 81/100 | 20% | 16.20/20 | Durable cross-layer isolation lesson. |
| Technical soundness | 88/100 | 15% | 13.20/15 | Multi-platform experiments substantiate the oracle. |
| Practical usability | 72/100 | 10% | 7.20/10 | Requires page templates and enabled deduplication. |
| Clarity and reproducibility | 84/100 | 10% | 8.40/10 | Page construction and timings are documented. |

**Final score: 82.3/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It exploits memory deduplication rather than the cache-set
primitive used by The Spy in the Sandbox.

## 82.2 — [The Devil is in the Constants: Bypassing Defenses in Browser JIT Engines](https://www.ndss-symposium.org/wp-content/uploads/2017/09/09_1_2.pdf) — Michalis Athanasakis, Elias Athanasopoulos, Michalis Polychronakis, Georgios Portokalidis, Sotiris Ioannidis

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed NDSS paper published February 2015.

### Core contribution

Attacker-chosen constants cause browser JITs to emit useful instruction streams
and dynamically assembled ROP gadgets even under constant blinding and code
randomization. End-to-end Firefox and 64-bit Internet Explorer attacks avoid
depending on reusable gadgets in the browser or libraries.

### Prior Art

JIT spraying, ROP and constant blinding were known. The paper's advance is the
dynamic gadget construction and bypass of defenses designed for classic JIT
spraying, not the original idea of influencing JIT output.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 84/100 | 25% | 21.00/25 | New dynamically generated ROP and blinding bypass. |
| Transferability | 75/100 | 20% | 15.00/20 | Applies to multiple JITs with target-specific details. |
| Lasting value | 82/100 | 20% | 16.40/20 | Durable warning for JIT hardening and CFI. |
| Technical soundness | 91/100 | 15% | 13.65/15 | Two major-browser exploit chains validate it. |
| Practical usability | 78/100 | 10% | 7.80/10 | Requires a control-flow flaw but automates gadgets. |
| Clarity and reproducibility | 84/100 | 10% | 8.40/10 | Generated layouts and exploit paths are explicit. |

**Final score: 82.2/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It materially advances JIT exploitation beyond the
established spraying primitive.

## 81.9 — [The Clock is Still Ticking: Timing Attacks in the Modern Web](https://dl.acm.org/doi/10.1145/2810103.2813632) — Tom Van Goethem, Wouter Joosen, Nick Nikiforakis

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed ACM CCS paper published October 2015. This is a fresh reassessment
of the sole existing missed-list entry.

### Core contribution

Four browser mechanisms—video parsing, AppCache behavior, Service Worker cache
and script parsing—create cross-origin timing channels after data is downloaded.
They reveal response size and resource/application state independently of
network latency, establishing a foundational XS-Leaks family.

### Prior Art

Remote server timing, cache history probes and the original list's general web-
timing methodology predate the work. They do not provide these post-download,
browser-internal parsers and caches as network-independent cross-origin oracles.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78/100 | 25% | 19.50/25 | Four distinct browser-internal timing primitives. |
| Transferability | 85/100 | 20% | 17.00/20 | Applies across resource types and stateful web apps. |
| Lasting value | 85/100 | 20% | 17.00/20 | Foundational XS-Leaks model and mitigations. |
| Technical soundness | 90/100 | 15% | 13.50/15 | Browser demonstrations and disclosures support it. |
| Practical usability | 74/100 | 10% | 7.40/10 | Timing classification needs calibration and repetition. |
| Clarity and reproducibility | 75/100 | 10% | 7.50/10 | Paper and artifacts explain the four channels. |

**Final score: 81.9/100.** Archive decision: include as a core technique.

### Verdict

Original technique. The existing entry remains, with its browser-internal XS-
Leak mechanism distinguished from the year's nominated server timing work.

## 81.8 — [Vetting SSL Usage in Applications with SSLINT](https://www.ieee-security.org/TC/SP2015/papers-archived/6949a519.pdf) — Boyuan He, Vaibhav Rastogi, Yinzhi Cao, Yan Chen, V.N. Venkatakrishnan, Runqing Yang, Zhenrui Zhang

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published May 2015.

### Core contribution

SSLINT builds interprocedural program and call graphs that encode correct TLS
certificate/hostname verification and error-handling logic, then checks 381
Ubuntu applications. It found 27 previously unknown exploitable SSL misuse bugs
that ordinary API-name scanning would miss.

### Prior Art

TLS API misuse and certificate-validation studies were public by 2012. SSLINT
qualifies through its scalable graph-based logic verification across complex
native applications, not by rediscovering permissive trust managers.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 72/100 | 25% | 18.00/25 | New scalable logic-aware TLS misuse analysis. |
| Transferability | 87/100 | 20% | 17.40/20 | General to applications and multiple TLS APIs. |
| Lasting value | 82/100 | 20% | 16.40/20 | API-correctness analysis remains valuable. |
| Technical soundness | 92/100 | 15% | 13.80/15 | Large corpus and confirmed unknown bugs validate it. |
| Practical usability | 77/100 | 10% | 7.70/10 | Static analysis produces actionable misuse paths. |
| Clarity and reproducibility | 85/100 | 10% | 8.50/10 | Rules, graphs and evaluation are documented. |

**Final score: 81.8/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It complements, rather than duplicates,
the TLS state-machine methods by analyzing application API use.

## 80.9 — [Exploiting and Protecting Dynamic Code Generation](https://www.ndss-symposium.org/ndss2015/ndss-2015-programme/exploiting-and-protecting-dynamic-code-generation/) — Chengyu Song, Chao Zhang, Tielei Wang, Wenke Lee, David Melski

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed NDSS paper published 7 February 2015.

### Core contribution

Code-cache injection writes shellcode while a JIT or dynamic translator exposes
its generated-code cache as writable, including a multithreaded race when W⊕X
alternates permissions. A browser Web Worker exploit revives direct shellcode
injection despite DEP, and a split-process architecture mitigates it.

### Prior Art

JIT spraying, writable/executable JIT windows and code injection were known.
The distinct attack writes into the code generator's cache during generation or
permission races rather than compiling attacker-shaped instruction constants.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 84/100 | 25% | 21.00/25 | New code-cache injection and multithreaded W⊕X race. |
| Transferability | 72/100 | 20% | 14.40/20 | Applies to JITs/DBTs with writable cache windows. |
| Lasting value | 82/100 | 20% | 16.40/20 | Durable dynamic-code isolation lesson. |
| Technical soundness | 89/100 | 15% | 13.35/15 | Browser exploit and two-engine defense support it. |
| Practical usability | 75/100 | 10% | 7.50/10 | Requires a memory-write primitive and timing window. |
| Clarity and reproducibility | 83/100 | 10% | 8.30/10 | Threat, exploit and architecture are described. |

**Final score: 80.9/100.** Archive decision: include as a core technique.

### Verdict

Original technique. Code-cache injection is separable from both JIT spraying
and the generated-ROP technique scored above.

## 80.7 — [How to Break XML Encryption – Automatically](https://www.usenix.org/conference/woot15/workshop-program/presentation/kupser) — Dennis Kupser, Christian Mainka, Jörg Schwenk, Juraj Somorovsky

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed WOOT paper published August 2015.

### Core contribution

An algorithm inspects an arbitrary encrypted XML message, determines which
chosen-ciphertext oracle and transformations apply, tests the service and can
automatically recover plaintext. Its WS-Attacker plugin found new exploitable
problems in four of five Web Services stacks, including CXF and DataPower.

### Prior Art

XML Encryption CBC and RSA oracles were public from 2011–2013. The qualifying
advance is automated configuration discovery, vulnerability classification and
end-to-end exploitation across arbitrary messages and implementations.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 68/100 | 25% | 17.00/25 | Automates an established but complex attack family. |
| Transferability | 85/100 | 20% | 17.00/20 | Covers diverse XML messages and service stacks. |
| Lasting value | 82/100 | 20% | 16.40/20 | Durable oracle-testing methodology. |
| Technical soundness | 92/100 | 15% | 13.80/15 | Four new real-stack findings validate it. |
| Practical usability | 79/100 | 10% | 7.90/10 | Open plugin performs detection and plaintext recovery. |
| Clarity and reproducibility | 86/100 | 10% | 8.60/10 | Algorithm, messages and implementation are detailed. |

**Final score: 80.7/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It preserves the earlier oracle prior art
while adding a reusable automated attack workflow.

## 79.3 — [Cross-Site Framing Attacks](https://dl.acm.org/doi/10.1145/2818000.2818029) — Nethanel Gelernter, Yoel Grinstein, Amir Herzberg

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed ACSAC paper published December 2015; an author manuscript was
publicly uploaded before the conference.

### Core contribution

Cross-site requests plant false incriminating searches, posts and other records
in reputable service logs under a victim's identity. Browser and filesystem
quirks additionally place files and history artifacts on the victim machine in
forms that forensic tools attribute to the user, without malware or local access.

### Prior Art

CSRF, drive-by downloads and anti-forensics were known. Earlier CSRF work sought
unauthorized actions or victim harm, not a systematic construction for planting
corroborating remote and local forensic evidence while concealing browser origin.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 84/100 | 25% | 21.00/25 | New web-to-forensic evidence-planting attack class. |
| Transferability | 73/100 | 20% | 14.60/20 | Demonstrated across major services and local artifacts. |
| Lasting value | 74/100 | 20% | 14.80/20 | Durable warning for CSRF and forensic provenance. |
| Technical soundness | 88/100 | 15% | 13.20/15 | Service cases, tools and law-enforcement review support it. |
| Practical usability | 77/100 | 10% | 7.70/10 | Uses ordinary browser requests with target-specific setup. |
| Clarity and reproducibility | 80/100 | 10% | 8.00/10 | Attack artifacts and validation are documented. |

**Final score: 79.3/100.** Archive decision: include as a core technique.

### Verdict

Original technique. Its objective and construction are distinct from ordinary
CSRF even though cross-site requests are an ingredient.

## 77.7 — [WebRTC IP Address Leaks](https://diafygi.github.io/webrtc-ips/) — Daniel Roesler

**KEPT** · Meaningful combination or adaptation · confidence Medium

### Candidate

Primary proof of concept and public source repository published in January 2015;
contemporaneous issue reports establish the date and affected browsers.

### Core contribution

A webpage creates an `RTCPeerConnection` and reads ICE/STUN candidates to reveal
private interface addresses and the public address used outside a proxy or VPN,
without a media permission prompt. The compact PoC made the browser/network
identity leak directly testable.

### Prior Art

ICE and STUN necessarily discover addresses, and implementers had discussed the
privacy risk. The qualifying contribution is the public, cross-browser web-page
construction showing silent exposure and VPN/proxy bypass; it is not credited as
inventing ICE address discovery.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 54/100 | 25% | 13.50/25 | Practical web adaptation of known ICE semantics. |
| Transferability | 90/100 | 20% | 18.00/20 | Broadly affected WebRTC-capable browsers and networks. |
| Lasting value | 88/100 | 20% | 17.60/20 | Became a standard privacy and VPN leak check. |
| Technical soundness | 82/100 | 15% | 12.30/15 | Source PoC and browser reports corroborate it. |
| Practical usability | 88/100 | 10% | 8.80/10 | Minimal JavaScript demonstrates the leak immediately. |
| Clarity and reproducibility | 75/100 | 10% | 7.50/10 | Code is clear, though historical narrative is sparse. |

**Final score: 77.7/100.** Archive decision: include as a core technique.

### Verdict

Meaningful combination or adaptation. Confidence is Medium because protocol-
design prior art is strong, but the 2015 browser PoC is a distinct reusable test.

## 77.0 — [Man-in-the-Browser-Cache: Persisting HTTPS Attacks via Browser Cache Poisoning](https://doi.org/10.1016/j.cose.2015.07.004) — Yaoqi Jia, Yue Chen, Xinshu Dong, Prateek Saxena, Jian Mao, Zhenkai Liang

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed Computers & Security paper published online in 2015.

### Core contribution

After one user-approved certificate warning or transient network interception,
an attacker poisons persistent same-origin, cross-origin or extension-assisted
browser cache entries so malicious content survives after HTTPS connectivity is
restored. The work maps desktop/mobile caching and AppCache persistence.

### Prior Art

Browser cache poisoning and persistent MITM concepts were discussed by 2010,
which the paper acknowledges. The qualifying advance is the systematic HTTPS
persistence model, new browser/extension variants and evaluation across five
desktop and sixteen mobile browsers.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 62/100 | 25% | 15.50/25 | New systematic variants over acknowledged prior concept. |
| Transferability | 82/100 | 20% | 16.40/20 | Covers multiple caches, origins, browsers and devices. |
| Lasting value | 78/100 | 20% | 15.60/20 | Durable lesson on secure-state recovery and persistence. |
| Technical soundness | 89/100 | 15% | 13.35/15 | Broad browser study and fixes validate the behavior. |
| Practical usability | 76/100 | 10% | 7.60/10 | Requires one interception/warning event but then persists. |
| Clarity and reproducibility | 85/100 | 10% | 8.50/10 | Variants, platforms and conditions are well specified. |

**Final score: 77.0/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It does not claim the first cache-poisoning idea; it adds
the reusable cross-browser HTTPS persistence analysis.

## 75.9 — [Too LeJIT to Quit: Extending JIT Spraying to ARM](https://www.ndss-symposium.org/wp-content/uploads/2017/09/09_3_2.pdf) — Wilson Lian, Hovav Shacham, Stefan Savage

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed NDSS paper published February 2015.

### Core contribution

Gadget chaining makes fixed-width ARM instructions behave like callable pieces
of attacker-shaped JIT output, overcoming JIT spraying's dependence on x86
unaligned decoding. An end-to-end WebKit JavaScriptCore exploit also bypasses
mitigations considered sufficient against x86 spraying.

### Prior Art

JIT spraying and code-reuse gadgets were established. The qualifying advance is
the ARM gadget-chaining construction and complete browser exploit, not a new
claim over the general spraying concept.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 70/100 | 25% | 17.50/25 | New architecture-specific gadget-chaining extension. |
| Transferability | 70/100 | 20% | 14.00/20 | Relevant to ARM JITs, with engine-specific details. |
| Lasting value | 76/100 | 20% | 15.20/20 | Useful lesson for fixed-width JIT hardening. |
| Technical soundness | 90/100 | 15% | 13.50/15 | End-to-end JavaScriptCore exploit validates it. |
| Practical usability | 73/100 | 10% | 7.30/10 | Requires control-flow corruption and JIT shaping. |
| Clarity and reproducibility | 84/100 | 10% | 8.40/10 | Gadget construction and mitigation bypass are detailed. |

**Final score: 75.9/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. ARM gadget chaining materially broadens the established
JIT-spraying family.

## 68.3 — [Cache Timing Attacks Revisited: Efficient and Repeatable Browser History, OS and Network Sniffing](https://doi.org/10.1007/978-3-319-18467-8_7) — Chetan Bansal, Sören Preibusch, Natasa Milic-Frayling

**KEPT** · Meaningful extension · confidence Medium

### Candidate

Peer-reviewed IFIP SEC paper published May 2015.

### Core contribution

Web Workers parallelize roughly 300 cache probes per second, while request
timeouts prevent probes from polluting the cache. The resulting robust method
infers browser, operating-system and proxy cache state across private browsing,
HTTPS, intranets, banking, search and social-media cases.

### Prior Art

Browser cache timing and history sniffing date to 2000. This lower-band entry
qualifies only through the repeatable parallel probing and anti-pollution method
that materially broadens affected cache layers and operational cases.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 42/100 | 25% | 10.50/25 | Robust engineering over a long-established attack. |
| Transferability | 82/100 | 20% | 16.40/20 | Works across cache layers and application contexts. |
| Lasting value | 65/100 | 20% | 13.00/20 | Useful method, though browser caches continue changing. |
| Technical soundness | 85/100 | 15% | 12.75/15 | Multiple cache layers and case studies support it. |
| Practical usability | 79/100 | 10% | 7.90/10 | Parallel worker probes are directly implementable. |
| Clarity and reproducibility | 78/100 | 10% | 7.80/10 | Parameters and cases are adequately documented. |

**Final score: 68.3/100.** Archive decision: include under the 60-or-above gate.

### Verdict

Meaningful extension. Confidence is Medium because originality is limited, but
the anti-pollution and parallelization workflow is separable and reusable.

## 65.6 — [Automatically Detecting SSL Error-Handling Vulnerabilities in Hybrid Mobile Web Apps](https://lilicoding.github.io/SA3Repo/papers/2015_zuo2015automatically.pdf) — Chaoshun Zuo, Jianliang Wu, Shanqing Guo

**KEPT** · Tooling or methodology contribution · confidence Medium

### Candidate

Peer-reviewed AsiaCCS paper published April 2015.

### Core contribution

The analyzer first statically identifies Android WebView certificate-error
handlers that may call `proceed`, then dynamically verifies whether an invalid-
certificate HTTPS page actually loads. It confirmed 645 vulnerable apps among
13,820 while avoiding the false positives of either phase alone.

### Prior Art

Permissive certificate callbacks, Android TLS mistakes and static/dynamic app
analysis were established. This lower-band entry qualifies for its WebView-
specific hybrid verification pipeline and scale, not a new MITM mechanism.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 38/100 | 25% | 9.50/25 | New combined detector for a known validation bug. |
| Transferability | 72/100 | 20% | 14.40/20 | Applies to many Android hybrid applications. |
| Lasting value | 70/100 | 20% | 14.00/20 | Error-path verification remains a useful audit pattern. |
| Technical soundness | 86/100 | 15% | 12.90/15 | 13,820-app study and confirmations support it. |
| Practical usability | 70/100 | 10% | 7.00/10 | Automation is valuable but Android-version specific. |
| Clarity and reproducibility | 78/100 | 10% | 7.80/10 | Analysis stages and results are documented. |

**Final score: 65.6/100.** Archive decision: include under the 60-or-above gate.

### Verdict

Tooling or methodology contribution. Confidence is Medium and the known TLS
misuse is not re-labelled as an original technique.

## 63.8 — [Cashing Out the Great Cannon? On Browser-Based DDoS Attacks and Economics](https://www.usenix.org/conference/woot15/workshop-program/presentation/pellegrino) — Giancarlo Pellegrino, Christian Rossow, Fabrice J. Ryba, Thomas C. Schmidt, Matthias Wählisch

**KEPT** · Meaningful combination or adaptation · confidence Medium

### Candidate

Peer-reviewed WOOT paper published August 2015.

### Core contribution

The work measures three browser APIs capable of producing thousands of HTTP
requests per second, combines them with typosquatting or malicious-ad bot
acquisition, and models costs against malware botnets. It turns anecdotal
browser DDoS into a testable capability and operational threat model.

### Prior Art

Browser-based DDoS was demonstrated before 2015, including HTML5 and ad-driven
concepts, and the Great Cannon supplied a live example. This borderline entry
qualifies only for the systematic API measurement and economic combination.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 42/100 | 25% | 10.50/25 | Systematizes rather than invents browser DDoS. |
| Transferability | 76/100 | 20% | 15.20/20 | General APIs and acquisition channels are reusable. |
| Lasting value | 58/100 | 20% | 11.60/20 | Economics and browser throttling are time-sensitive. |
| Technical soundness | 70/100 | 15% | 10.50/15 | Preliminary but measured experiments support it. |
| Practical usability | 80/100 | 10% | 8.00/10 | Request-generation techniques are straightforward. |
| Clarity and reproducibility | 80/100 | 10% | 8.00/10 | APIs, rates, assumptions and costs are explicit. |

**Final score: 63.8/100.** Archive decision: include under the 60-or-above gate.

### Verdict

Meaningful combination or adaptation. Confidence is Medium because the attack
principle is old; the 2015 measurement/economics package is the retained advance.

## 60.3 — [HTTPS Bicycle Attack](https://guidovranken.files.wordpress.com/2015/12/https-bicycle-attack.pdf) — Guido Vranken

**KEPT** · Meaningful combination or adaptation · confidence Medium

### Candidate

Primary researcher whitepaper published 30 December 2015.

### Core contribution

A passive TLS observer subtracts stable request and browser overhead from
ciphertext record lengths to estimate a submitted password's length, then uses
that length to prune an offline guessing dictionary. The paper supplies HTTP
request models and browser demonstrations under encrypted transport.

### Prior Art

Encrypted packet-length leakage, website fingerprinting and traffic analysis
long predate 2015. This threshold entry qualifies narrowly as a concrete HTTPS
password-length and dictionary-pruning workflow, not as discovery of length
leakage itself.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 34/100 | 25% | 8.50/25 | Narrow adaptation of established encrypted-length leakage. |
| Transferability | 70/100 | 20% | 14.00/20 | Applies where password requests have stable framing. |
| Lasting value | 62/100 | 20% | 12.40/20 | Durable metadata lesson but mitigations/protocols vary. |
| Technical soundness | 70/100 | 15% | 10.50/15 | Models and demonstrations support a conditional attack. |
| Practical usability | 72/100 | 10% | 7.20/10 | Passive observation is simple; ambiguity limits recovery. |
| Clarity and reproducibility | 77/100 | 10% | 7.70/10 | Request accounting and experiments are documented. |

**Final score: 60.3/100.** Archive decision: include under the 60-or-above gate.

### Verdict

Meaningful combination or adaptation. Confidence is Medium; the entry sits just
above the threshold because its reusable password workflow is narrow but real.
