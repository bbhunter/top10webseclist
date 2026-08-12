# 2019 candidate judgements

These scorecards apply the repository's weighted judge rubric. `KEPT` means the
candidate met the historical 60-or-above inclusion rule as well as the
first-publication, originality-verdict and original-nomination exclusions.

## 89.2 — [Turbo Intruder: Embracing the billion-request attack](https://portswigger.net/research/turbo-intruder-embracing-the-billion-request-attack) — James Kettle

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

PortSwigger Research published the project and method on 25 January 2019.

### Core contribution

Turbo Intruder combines a purpose-built HTTP stack, flat-memory response
handling, programmable request generation, connection gating and differential
response analysis so attacks involving enormous request volumes or tight timing
can be tested from an ordinary workstation.

### Prior art

High-rate scanners, Burp extensions and race testing existed. The distinct
contribution is an integrated, scriptable architecture that removes their
request-count and timing bottlenecks for web-security experiments.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78 | 25% | 19.50 | Introduces a specialised high-scale request engine and workflow. |
| Transferability | 94 | 20% | 18.80 | Supports many endpoints, protocols and attack hypotheses. |
| Lasting value | 92 | 20% | 18.40 | Established a durable platform for races and high-volume testing. |
| Technical soundness | 94 | 15% | 14.10 | Architecture and real attack cases validate the design. |
| Practical usability | 96 | 10% | 9.60 | Public, scriptable tooling is directly usable. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Implementation, examples and operating model are documented. |

**Final score: 89.2/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It makes previously impractical request
volumes and timing experiments reproducible across web targets.

## 88.9 — [Cross-Origin State Inference (COSI) Attacks](https://arxiv.org/abs/1908.02204) — Avinash Sudhodanan, Soheil Khodayari, Juan Caballero

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

The primary preprint was first public on 6 August 2019; its conference venue was
NDSS 2020.

### Core contribution

COSI formalises cross-origin state inference, composes multiple XS-Leak classes
across browsers and victim states, adds a `postMessage` leak, and implements
Basta-COSI to generate practical multi-state attacks.

### Prior art

Individual cross-site leaks and the original list's broad Cross-Site Leaks entry
precede it. The distinct contribution is the systematic multi-state model,
browser composition and automated attack generation.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | Adds a systematic state-inference model and a new leak class. |
| Transferability | 92 | 20% | 18.40 | Applies across sites, states, leaks and browser families. |
| Lasting value | 91 | 20% | 18.20 | Durable vocabulary and workflow for XS-Leak research. |
| Technical soundness | 94 | 15% | 14.10 | Taxonomy, generated attacks and site evaluation agree. |
| Practical usability | 87 | 10% | 8.70 | Basta-COSI turns the model into testable attacks. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Classes, constraints and experiments are explicit. |

**Final score: 88.9/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It is not a duplicate of a single XS-Leak;
it adds a reusable model and automated composition capability.

## 87.3 — [Iframes/Popups Are Dangerous in Mobile WebView](https://www.usenix.org/conference/usenixsecurity19/presentation/yang-guangliang) — GuangLiang Yang, Jeff Huang, Guofei Gu

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2019.

### Core contribution

The paper defines differential context vulnerabilities: iframe and popup
behaviour that differs between browsers and embedded WebViews can hide origin,
bypass bridge or `postMessage` validation, overlap trusted UI and enable
privileged navigation. DCV-Hunter detects these conditions in applications.

### Prior art

Hostile WebView content, bridge abuse and origin-stripping attacks were known.
The new contribution is treating regular-browser/WebView context divergence as
an attack class with several concrete primitives and an analyser.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 85 | 25% | 21.25 | Defines a distinct differential-context vulnerability class. |
| Transferability | 88 | 20% | 17.60 | Recurs across apps, bridges, iframes and popups. |
| Lasting value | 87 | 20% | 17.40 | Durable model for embedded-browser security boundaries. |
| Technical soundness | 94 | 15% | 14.10 | Tooling, experiments and application findings support it. |
| Practical usability | 82 | 10% | 8.20 | DCV-Hunter and patterns guide audits. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Context differences and exploit paths are explicit. |

**Final score: 87.3/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It generalises several attacks around an overlooked
cross-environment security boundary rather than merely finding another bridge bug.

## 86.5 — [Leaky Images: Targeted Privacy Attacks in the Web](https://www.usenix.org/conference/usenixsecurity19/presentation/staicu) — Cristian-Alexandru Staicu, Michael Pradel

**KEPT** · Meaningful combination or adaptation · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2019.

### Core contribution

An attacker privately shares an attacker-controlled image with a chosen account,
then embeds that image cross-origin to learn whether the exact target visits an
attacker page. Scriptless and cross-site identity-linking variants broaden the
targeted state oracle.

### Prior art

Cross-origin loading oracles and history/state inference were established. The
distinct contribution is binding a personalised image capability to a chosen
identity, turning a general leak into targeted presence and identity linkage.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 84 | 25% | 21.00 | Creates a targeted oracle from personalised image sharing. |
| Transferability | 88 | 20% | 17.60 | Applies to many sharing sites and attacker-controlled resources. |
| Lasting value | 86 | 20% | 17.20 | Reveals a durable risk in personalised cross-origin assets. |
| Technical soundness | 91 | 15% | 13.65 | Site evaluation and attack variants substantiate it. |
| Practical usability | 83 | 10% | 8.30 | Requires only sharing and a hostile page on affected sites. |
| Clarity and reproducibility | 87 | 10% | 8.70 | Preconditions and variants are clearly described. |

**Final score: 86.5/100.** Archive decision: include as a core technique.

### Verdict

Meaningful combination or adaptation. The component oracle is known, but the
identity-bound capability creates a distinct targeted attack.

## 83.8 — [Bypassing CSP with policy injection](https://portswigger.net/research/bypassing-csp-with-policy-injection) — Gareth Heyes

**KEPT** · Meaningful extension · confidence High

### Candidate

PortSwigger Research published the work on 5 June 2019.

### Core contribution

When input is reflected inside a Content-Security-Policy header, injected
directives and browser parsing differences can discard the policy or override
script restrictions, including Edge policy truncation and Chrome's
`script-src-elem` precedence.

### Prior art

CSP misconfiguration and nonce/source bypasses were known. This work isolates
policy text itself as an injection surface and demonstrates reusable directive-
precedence and parse-failure primitives.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | Identifies concrete CSP policy-injection primitives. |
| Transferability | 82 | 20% | 16.40 | Applies wherever attacker input reaches policy text. |
| Lasting value | 84 | 20% | 16.80 | Durable lesson about policy grammar and directive precedence. |
| Technical soundness | 83 | 15% | 12.45 | Browser-specific demonstrations support the claims. |
| Practical usability | 88 | 10% | 8.80 | Payloads are concise and readily testable. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Conditions and proof payloads are explicit. |

**Final score: 83.8/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It adds an injection and parsing attack surface distinct
from ordinary weak-policy or allowed-source CSP bypasses.

## 83.5 — [JavaScript Template Attacks](https://www.ndss-symposium.org/wp-content/uploads/2019/02/ndss2019_01B-4_Schwarz_paper.pdf) — Michael Schwarz, Florian Lackner, Daniel Gruss

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2019.

### Core contribution

The method automatically learns JavaScript behavioural templates whose results
vary by host implementation, then uses them to infer target properties relevant
to exploit selection, including CPU architecture and allocator behaviour.

### Prior art

Browser fingerprinting and hand-built JavaScript feature tests were known. The
distinct contribution is automated differential template generation and its use
for low-level exploit-environment inference.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 76 | 25% | 19.00 | Automates discovery of host-dependent JavaScript templates. |
| Transferability | 87 | 20% | 17.40 | Generalises across hosts and implementation properties. |
| Lasting value | 84 | 20% | 16.80 | Useful model for fingerprinting and exploit preparation. |
| Technical soundness | 91 | 15% | 13.65 | Generated templates and evaluated inferences support it. |
| Practical usability | 80 | 10% | 8.00 | Method is usable though generation takes specialist setup. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Pipeline and examples are sufficiently documented. |

**Final score: 83.5/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It scales fingerprint discovery beyond
manual feature inventories and reaches exploit-relevant implementation details.

## 83.2 — [What Are You Searching For? A Remote Keylogging Attack on Search Engine Autocomplete](https://www.usenix.org/conference/usenixsecurity19/presentation/monaco) — John V. Monaco

**KEPT** · Meaningful combination or adaptation · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2019.

### Core contribution

The attack combines packet timing, visible length changes caused by encoded
spaces and HTTP/2 static Huffman-code lengths to infer search queries from TLS-
encrypted autocomplete traffic.

### Prior art

Encrypted-traffic analysis, keystroke timing and compression length leakage were
known. Their combination against autocomplete creates a remote query-recovery
capability not supplied by any one antecedent.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | Combines three observables into remote query inference. |
| Transferability | 82 | 20% | 16.40 | Applies across autocomplete services with similar traffic. |
| Lasting value | 84 | 20% | 16.80 | Durable warning for encrypted interactive protocols. |
| Technical soundness | 92 | 15% | 13.80 | Controlled and real-data evaluation support the inference. |
| Practical usability | 70 | 10% | 7.00 | Requires network observation and service-specific models. |
| Clarity and reproducibility | 87 | 10% | 8.70 | Features, model and limits are documented. |

**Final score: 83.2/100.** Archive decision: include as a core technique.

### Verdict

Meaningful combination or adaptation. Established channels are assembled into a
new practical attack on encrypted web interaction.

## 82.6 — [Cross-Site Challenge-Response Attacks](https://madweb.work/papers/2019/paper4.pdf) — Nethanel Gelernter, Itamar Peretz

**KEPT** · Meaningful combination or adaptation · confidence High

### Candidate

Peer-reviewed MADWeb paper published on 24 February 2019.

### Core contribution

A hostile site uses cross-origin response differentiation to brute-force a
challenge-response value that a service mistakenly treats as CSRF protection.
Authenticated and visitor-powered unauthenticated variants can distribute work
and evade ordinary account or source rate limits.

### Prior art

CSRF, cross-origin response oracles and brute force were known. The distinct
contribution is turning visitors' browsers into a cross-site challenge-response
guesser and analysing both authenticated and distributed variants.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 79 | 25% | 19.75 | Produces a distinct cross-site brute-force capability. |
| Transferability | 84 | 20% | 16.80 | Applies to many challenge-response CSRF substitutes. |
| Lasting value | 82 | 20% | 16.40 | Durable lesson about confusing authentication with request intent. |
| Technical soundness | 88 | 15% | 13.20 | Survey, proofs and experiments support the model. |
| Practical usability | 80 | 10% | 8.00 | Concrete response oracles and variants guide testing. |
| Clarity and reproducibility | 85 | 10% | 8.50 | Preconditions and attack flow are explicit. |

**Final score: 82.6/100.** Archive decision: include as a core technique.

### Verdict

Meaningful combination or adaptation. Known ingredients create a reusable
cross-site guessing attack with different rate-limit economics.

## 81.5 — [PhishFarm](https://doi.org/10.1109/SP.2019.00049) — Adam Oest, Yeganeh Safaei, Adam Doupé, Gail-Joon Ahn, Brad Wardman, Kevin Tyers

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published in May 2019.

### Core contribution

PhishFarm safely deploys live controlled phishing pages and systematically tests
real HTTP cloaking filters against browser blacklists, measuring how crawler
evasion changes detection time and coverage.

### Prior art

Phishing cloaking and blacklist measurement existed. The distinct contribution
is a scalable, ethically controlled framework for causal evaluation of individual
evasion mechanisms against production blacklist systems.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 68 | 25% | 17.00 | Systematises known cloaking in a controlled live framework. |
| Transferability | 86 | 20% | 17.20 | Supports filters, browsers and blacklist providers. |
| Lasting value | 81 | 20% | 16.20 | Durable method for evaluating anti-abuse systems. |
| Technical soundness | 94 | 15% | 14.10 | Large controlled deployment and comparative results are strong. |
| Practical usability | 82 | 10% | 8.20 | Framework concepts transfer directly to evaluations. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Design, filters and ethics are carefully specified. |

**Final score: 81.5/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. Its value is rigorous scalable evasion
testing, not novelty credit for the underlying cloaking tricks.

## 80.7 — [All Your Clicks Belong to Me](https://www.usenix.org/conference/usenixsecurity19/presentation/zhang) — Mingxue Zhang, Wei Meng, Sangho Lee, Byoungyoung Lee, Xinyu Xing

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2019.

### Core contribution

The Observer browser records event registration and dispatch to identify three
ways third-party JavaScript intercepts user clicks, then attributes interception
at scale across a large site population.

### Prior art

Clickjacking, event listeners and malicious third-party scripts were known. The
contribution is a browser-level observation and classification methodology for
same-page click interception that prior crawlers could not reliably attribute.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 68 | 25% | 17.00 | Adds an interception taxonomy and observation mechanism. |
| Transferability | 88 | 20% | 17.60 | Applies broadly to sites and third-party scripts. |
| Lasting value | 79 | 20% | 15.80 | Useful for studying event abuse and supply-chain scripts. |
| Technical soundness | 92 | 15% | 13.80 | Instrumented-browser and large-scale evidence align. |
| Practical usability | 78 | 10% | 7.80 | Requires a modified browser but yields actionable attribution. |
| Clarity and reproducibility | 87 | 10% | 8.70 | Techniques and detection logic are documented. |

**Final score: 80.7/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It makes a previously opaque class of
in-page input interception observable and measurable.

## 79.9 — [Latex Gloves](https://www.ndss-symposium.org/wp-content/uploads/2019/02/ndss2019_01B-5_Sjosten_paper.pdf) — Alexander Sjösten, Steven Van Acker, Pablo Picazo-Sanchez, Andrei Sabelfeld

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2019.

### Core contribution

Randomised browser-extension identifiers can become stable per-user identifiers,
while extension-injected DOM changes reveal extensions without relying solely on
web-accessible resources. The work combines probing and revelation channels and
evaluates their uniqueness.

### Prior art

Extension fingerprinting through web-accessible resources was known. The new
revelation channel and the finding that randomisation can strengthen uniqueness
extend the threat model beyond static identifier probing.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 70 | 25% | 17.50 | Adds DOM revelation and random-ID fingerprint effects. |
| Transferability | 84 | 20% | 16.80 | Applies across extensions and browser families. |
| Lasting value | 80 | 20% | 16.00 | Durable guidance for extension isolation and identifiers. |
| Technical soundness | 91 | 15% | 13.65 | Extension study and attack combinations support it. |
| Practical usability | 74 | 10% | 7.40 | Attacks are usable but depend on extension behaviour. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Channels and mitigations are explicit. |

**Final score: 79.9/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It expands extension fingerprinting beyond the established
web-accessible-resource probe.

## 79.9 — [Scalable Scanning and Automatic Classification of TLS Padding Oracle Vulnerabilities](https://www.usenix.org/conference/usenixsecurity19/presentation/merget) — Robert Merget et al.

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2019.

### Core contribution

The work reduces the probes needed to identify TLS padding oracles, represents
response behaviour as graphs, clusters implementations automatically and scales
the analysis to Internet-wide scanning.

### Prior art

Bleichenbacher and CBC padding oracles were established. The distinct contribution
is a practical low-probe classification method that discovers and groups unknown
oracle behaviour at Internet scale.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 58 | 25% | 14.50 | Advances discovery and classification, not the oracle primitive. |
| Transferability | 88 | 20% | 17.60 | Covers many TLS products and response behaviours. |
| Lasting value | 83 | 20% | 16.60 | General method for scalable protocol-oracle discovery. |
| Technical soundness | 94 | 15% | 14.10 | Validation and broad scanning substantiate it. |
| Practical usability | 83 | 10% | 8.30 | Reduced probes make large scans feasible. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Probe and clustering methodology are detailed. |

**Final score: 79.9/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It systematises discovery of known oracle
families rather than claiming the underlying cryptographic attack as new.

## 79.2 — [Postcards from the Post-HTTP World](https://ieeexplore.ieee.org/document/8835223) — Stefano Calzavara, Riccardo Focardi, Matus Nemec, Alvise Rabitti, Marco Squarcina

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published in May 2019.

### Core contribution

Attack trees model how HTTPS weaknesses in dependencies, related origins and
subdomains amplify compromise of an otherwise secure site through cookies,
scripts and trust relationships; a crawler then measures those composed paths.

### Prior art

HTTPS downgrade, weak dependencies and cookie/domain scope were known. The new
contribution is a systematic compositional model and measurement workflow for
transitive ecosystem exposure.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 60 | 25% | 15.00 | Systematises composition of established HTTPS weaknesses. |
| Transferability | 91 | 20% | 18.20 | Applies across dependency and related-origin ecosystems. |
| Lasting value | 80 | 20% | 16.00 | Durable model for transitive web-security risk. |
| Technical soundness | 93 | 15% | 13.95 | Attack trees and large crawl support the claims. |
| Practical usability | 74 | 10% | 7.40 | Requires ecosystem crawling but yields concrete paths. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Model and measurements are well specified. |

**Final score: 79.2/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. Its novelty is compositional analysis, not
another individual HTTPS bug.

## 79.1 — [The Betrayal at Cloud City](https://www.usenix.org/conference/usenixsecurity19/presentation/alrawi) — Omar Alrawi, Chaoshun Zuo, Ruian Duan, Ranjita Pai Kasturi, Zhiqiang Lin, Brendan Saltaformaggio

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2019.

### Core contribution

SkyWalker extracts cloud-backend URLs and ownership context from mobile
applications, remotely vets the backend software and web applications, and maps
findings back to the responsible developer or provider.

### Prior art

APK endpoint extraction, service fingerprinting and web vulnerability scanning
were known. The distinct contribution is their automated provenance-aware
pipeline for discovering otherwise invisible third-party backend attack surface.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 68 | 25% | 17.00 | Integrates extraction, remote vetting and ownership mapping. |
| Transferability | 84 | 20% | 16.80 | Generalises across apps, SDKs and backend technologies. |
| Lasting value | 78 | 20% | 15.60 | Durable methodology for client-derived API inventories. |
| Technical soundness | 90 | 15% | 13.50 | Large app study and validated findings support it. |
| Practical usability | 78 | 10% | 7.80 | Automated pipeline produces actionable inventories. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Stages and vetting logic are documented. |

**Final score: 79.1/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. The components are established, but the
client-to-backend discovery and responsibility workflow is a meaningful whole.

## 74.6 — [Provoking browser quirks with behavioural fuzzing](https://portswigger.net/research/provoking-browser-quirks-with-behavioural-fuzzing) — Gareth Heyes

**KEPT** · Tooling or methodology contribution · confidence Medium

### Candidate

PortSwigger Research published the work on 28 May 2019.

### Core contribution

The fuzzer generates and executes large numbers of Unicode and DOM variants,
compares browser behaviour and surfaces parser deviations that can become XSS,
sandbox or filter-bypass primitives.

### Prior art

Browser differential fuzzing and the author's earlier Shazzer project existed.
The 2019 contribution is behavioural rather than crash comparison and a much
broader Unicode/DOM generation workflow targeted at exploitable quirks.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 52 | 25% | 13.00 | Extends an established differential-fuzzing idea. |
| Transferability | 83 | 20% | 16.60 | Useful across browsers, parsers and markup contexts. |
| Lasting value | 76 | 20% | 15.20 | Durable workflow for finding parser differentials. |
| Technical soundness | 80 | 15% | 12.00 | Demonstrated quirks support the method, though evaluation is limited. |
| Practical usability | 88 | 10% | 8.80 | Generator and test strategy are directly actionable. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Implementation and examples are clear. |

**Final score: 74.6/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It is a substantial browser-security
fuzzing extension, not a claim to have invented differential fuzzing.

## 72.0 — [Measuring and Analyzing Search Engine Poisoning of Linguistic Collisions](https://doi.org/10.1109/SP.2019.00025) — Matthew Joslin, Neng Li, Shuang Hao, Minhui Xue, Haojin Zhu

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published in May 2019.

### Core contribution

Attackers poison misspellings that are valid words in another language, thereby
evading search-engine autocorrection. The work generates these linguistic
collisions and measures malicious first-page results across Google and Baidu.

### Prior art

Typosquatting and poisoning misspelled search queries were known. The distinct
contribution is using cross-language lexical validity as an autocorrection bypass
and systematising candidate generation.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 62 | 25% | 15.50 | Adds a cross-language autocorrection-evasion mechanism. |
| Transferability | 74 | 20% | 14.80 | Applies across languages and search engines. |
| Lasting value | 65 | 20% | 13.00 | Useful but tied to changing ranking and correction systems. |
| Technical soundness | 89 | 15% | 13.35 | Large candidate and search-result analysis supports it. |
| Practical usability | 70 | 10% | 7.00 | Generation procedure is usable though promotion remains external. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Collision model and measurement are explicit. |

**Final score: 72.0/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It supplies a specific reusable evasion mechanism beyond
ordinary misspelling-based search poisoning.

## 74.1 — [Telerik Revisited](https://code-white.com/blog/2019-02-telerik-revisited/)

**KEPT** · Meaningful combination or adaptation · confidence High

### Candidate

Markus Wulftange, Code White, 7 February 2019 (originally posted to the Code
White blogspot the same month). Surfaced by the 2026-08-12 pass over the ysonet
.NET-deserialization reference set.

### Core contribution

A general answer to the dead end that follows most arbitrary-file-write bugs in
an IIS-hosted .NET application: the worker process identity usually cannot write
to the web root, and the web root is often unknown, so an uploaded web shell is
unreachable. The post removes that precondition. Upload a mixed-mode assembly
DLL to any writable location, then use a second, unrelated deserialization sink
with the AssemblyInstaller gadget — whose Path setter loads the assembly and so
calls its DllMain entry point — to execute it inside the IIS worker process. The
Telerik CVE-2017-11317 upload is only the delivery mechanism; the reusable part
is "write anywhere plus a type-controlled deserialization sink equals RCE
without knowing the web root".

### Prior art

The three Telerik issues are from 2017 and were public: CVE-2017-9248 with the
PatchAdvisor oracle analysis, CVE-2017-11317 with the straight_blast writeup
that preceded the vendor fix, and CVE-2017-11357. The AssemblyInstaller gadget
comes from Munoz and Mirosh's "Friday the 13th: JSON Attacks" (Black Hat USA
2017), already archived for the 2016-17 list. What is not prior art is the
combination: using the gadget purely as a loader for a previously uploaded
mixed-mode assembly, which is what defeats the unknown-web-root problem. The
2019 list already nominates Bishop Fox's Telerik entry, but that is
CVE-2019-18935, a different bug reached through RadAsyncUpload JSON
deserialization, so this is not a renamed duplicate of an existing nomination.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 66 | 25% | 16.50 | The upload-plus-AssemblyInstaller loader chain and the mixed-mode DllMain observation are new; the constituent bugs and the gadget are not. |
| Transferability | 74 | 20% | 14.80 | Applies to any .NET or IIS application offering a file write plus a type-controlled deserialization sink, well beyond Telerik. |
| Lasting value | 72 | 20% | 14.40 | Became the standard Telerik RCE recipe and a routine post-file-write escalation in later .NET work. |
| Technical soundness | 84 | 15% | 12.60 | Each step is traced through the affected code and demonstrated end to end against a real product with a vendor fix. |
| Practical usability | 78 | 10% | 7.80 | Directly usable; needs a writable path and a reachable deserialization sink. |
| Clarity and reproducibility | 80 | 10% | 8.00 | The chain and its preconditions are laid out plainly, though no tooling is released. |

**Final score: 74.1/100.** Archive decision: include as a core technique.

### Verdict

Meaningful combination or adaptation. Revisiting patched 2017 bugs produced a
reusable escalation path that removes the usual precondition on file-write
primitives in .NET web applications.

### Reverification

- **Candidate facts rechecked against:** the archived post and the Code White
  byline, which give the 7 February 2019 date and author.
- **Independent prior-art check:** searched for the mechanism rather than the
  product — mixed-mode assembly loading via AssemblyInstaller, and
  arbitrary-write-to-RCE in IIS — and checked the 2017 and 2018 lists and the
  local archive for an earlier statement of it. The gadget is 2017; its use as a
  loader for an uploaded mixed-mode DLL is not attested earlier.
- **Strongest challenge to the result:** every ingredient is public, so this can
  be read as an application rather than a contribution.
- **Benefit-of-doubt check:** the combination changes what an attacker can do
  with a whole class of primitive, which the rubric explicitly declines to
  dismiss.
- **Changes after reverification:** original contribution was lowered from a
  draft 72 to 66 once the AssemblyInstaller gadget was confirmed as 2017 prior
  art; the final score fell from 76.6 to 74.1.

## 73.1 — [Re-Animating ActivitySurrogateSelector](https://www.netspi.com/blog/technical-blog/red-teaming/re-animating-activitysurrogateselector/)

**KEPT** · Meaningful extension · confidence High

### Candidate

Nick Landers, NetSPI, 4 June 2019. Surfaced by the 2026-08-12 pass over the
ysonet .NET-deserialization reference set.

### Core contribution

A two-stage pattern for defeating a runtime mitigation with the very sink the
mitigation protects. .NET Framework 4.8 killed the ActivitySurrogateSelector
gadget by adding a type check to ObjectSurrogate.GetObjectData, but left that
check behind an undocumented AppSettings switch. Landers shows the switch is
reachable at run time from a still-working gadget: a XAML payload wires two
ObjectDataProvider elements so that ConfigurationManager.AppSettings is fetched
and then Set is called on it, flipping
microsoft:WorkflowComponentModel:DisableActivitySurrogateSelectorTypeCheck for
the life of the process. Send that first, and the original gadget works again.
The general shape — use a weak gadget to mutate process configuration, then use
the strong gadget that configuration was blocking — is what transfers.

### Prior art

The ActivitySurrogateSelector gadget is Forshaw's, published by Project Zero in
April 2017; the .NET 4.8 fix is Microsoft's. ObjectDataProvider abuse through
XamlReader was established by "Friday the 13th: JSON Attacks" (2017) and by
Mirosh's TextFormattingRunProperties gadget. The unattested step is targeting a
security kill switch rather than a shell as the gadget's payload. The 2019
list's ViewState entry uses ActivitySurrogateSelector but predates and does not
describe the type-check bypass; the 2020 MDSec entry already in the archive uses
the resulting ActivitySurrogateDisableTypeCheck gadget by name without citing
where it came from, which is the gap this closes.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 68 | 25% | 17.00 | New: a gadget used to disable the framework's own mitigation. The gadget being re-enabled, and the XAML technique used to do it, are prior work. |
| Transferability | 70 | 20% | 14.00 | The AppSettings write is a general primitive against other undocumented .NET switches, and the disable-then-exploit shape is stack-independent. |
| Lasting value | 72 | 20% | 14.40 | Shipped as ysoserial.net's ActivitySurrogateDisableTypeCheck and still the standard prelude on .NET 4.8 and later. |
| Technical soundness | 78 | 15% | 11.70 | The patched assembly is decompiled, the flag traced to ConfigurationManager.AppSettings, and a working payload given; persistence across app-domain recycles is asserted rather than measured. |
| Practical usability | 82 | 10% | 8.20 | A two-payload recipe usable as-is, and now packaged in standard tooling. |
| Clarity and reproducibility | 78 | 10% | 7.80 | Short but complete, with the decompiled code and both XAML payloads inline. |

**Final score: 73.1/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It converts a vendor mitigation into a configuration
problem and supplies the reusable disable-then-exploit pattern, not just one
restored gadget.

### Reverification

- **Candidate facts rechecked against:** the archived post, which carries the
  4 June 2019 date, the NetSPI byline and the decompiled patch.
- **Independent prior-art check:** searched for runtime AppSettings manipulation
  through deserialization gadgets and for other .NET kill-switch bypasses, and
  checked the local archive for an earlier description. The 2020 MDSec reference
  uses the resulting gadget but postdates this post.
- **Strongest challenge to the result:** the payload reuses a known XAML
  ObjectDataProvider technique, so the novelty is the choice of target method
  rather than a new mechanism.
- **Benefit-of-doubt check:** choosing a security switch as the target is the
  insight, and it generalises to any process-wide setting reachable from a
  gadget.
- **Changes after reverification:** none.
