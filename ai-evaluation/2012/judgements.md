# 2012 candidate judgements

These scorecards apply the repository's weighted judge rubric. `KEPT` means the
candidate met the historical 60-or-above inclusion rule as well as the
first-publication, originality-verdict and original-nomination exclusions.

## 86.2 — [Signing Me onto Your Accounts through Facebook and Google](https://www.ieee-security.org/TC/SP2012/papers/4681a365.pdf) — Rui Wang, Shuo Chen, XiaoFeng Wang

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

IEEE S&P paper published in May 2012. The conference paper provides the primary
artifact, authorship, tested services and disclosure chronology.

### Core contribution

The work recovers the semantics of deployed single-sign-on traffic, derives
security invariants from the recovered protocol flows and tests major identity
providers and relying parties. It finds eight serious logic flaws, including
account compromise, by identifying fields whose intended ownership and binding
were lost across browser, provider and site.

### Prior art

Formal SSO analysis and individual OAuth flaws predate 2012. The new contribution
is traffic-guided semantic recovery and systematic field testing of commercially
deployed SSO implementations rather than another isolated protocol bug.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | New empirical workflow for recovering and testing hidden SSO semantics. |
| Transferability | 88 | 20% | 17.60 | Applies across IdPs, relying parties and other multi-party authentication flows. |
| Lasting value | 88 | 20% | 17.60 | Field and ownership confusion remain central OAuth/OIDC failure modes. |
| Technical soundness | 90 | 15% | 13.50 | Protocol reconstruction and validated real-service exploits support the claims. |
| Practical usability | 84 | 10% | 8.40 | The flow, ownership and binding checks translate directly into testing. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Traces, invariants and exploit conditions are explicit. |

**Final score: 86.2/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It systematizes discovery of deployed SSO
logic flaws without claiming that SSO or protocol confusion itself began in 2012.

## 86.0 — [Fuzzing with Code Fragments](https://www.usenix.org/conference/usenixsecurity12/technical-sessions/presentation/holler) — Christian Holler, Kim Herzig, Andreas Zeller

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

USENIX Security paper and presentation published in August 2012; the official
record identifies the artifact commonly known as LangFuzz.

### Core contribution

LangFuzz parses valid programs and known failure-inducing tests into reusable
fragments, recombines them under a language grammar and mutates the result. This
preserves enough syntax and semantic structure to reach deep interpreter paths,
finding 105 JavaScript and 18 PHP defects in major engines.

### Prior art

Grammar fuzzing, mutation fuzzing and jsfunfuzz predate the paper. Reusing
context-compatible fragments from real programs and previous bug tests as a
generic language-fuzzing strategy is the distinct methodology.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78 | 25% | 19.50 | Distinct fragment-recombination method grounded in grammars and bug corpora. |
| Transferability | 86 | 20% | 17.20 | General to parsers and interpreters with grammars and seed programs. |
| Lasting value | 90 | 20% | 18.00 | Corpus-guided structured fuzzing remains foundational. |
| Technical soundness | 90 | 15% | 13.50 | Large defect yield and multiple language engines validate the approach. |
| Practical usability | 88 | 10% | 8.80 | Converts existing tests and grammars into high-value test generation. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Algorithms, inputs and evaluation are thoroughly specified. |

**Final score: 86.0/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. Known fuzzing components are combined into
a materially new and demonstrably effective structured testing workflow.

## 85.9 — [Pixel Perfect: Fingerprinting Canvas in HTML5](https://hovav.net/ucsd/papers/ms12.html) [paper](https://www.ieee-security.org/TC/W2SP/2012/papers/w2sp12-final4.pdf) — Keaton Mowery, Hovav Shacham

**KEPT** · Original technique · confidence High

### Candidate

Author publication record and W2SP paper place the first publication in May
2012 and provide the complete primary artifact.

### Core contribution

The paper renders text, images and WebGL scenes into HTML5 canvas, reads back the
pixels and uses rendering differences as a browser/device fingerprint. It shows
that graphics stacks expose stable entropy without cookies or special plugins.

### Prior art

Panopticlick and earlier JavaScript configuration fingerprinting were public by
2010–2011. They did not use deterministic canvas and graphics-pipeline output as
the remote fingerprinting oracle introduced here.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 84 | 25% | 21.00 | Introduces the canvas-rendering fingerprint primitive. |
| Transferability | 88 | 20% | 17.60 | Works across browsers, operating systems, fonts and graphics stacks. |
| Lasting value | 90 | 20% | 18.00 | Canvas fingerprinting became a durable tracking technique. |
| Technical soundness | 82 | 15% | 12.30 | Multiple rendering paths and measured distinctness support the mechanism. |
| Practical usability | 86 | 10% | 8.60 | Requires only client-side drawing and pixel extraction. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Rendering tests and comparison procedure are concrete. |

**Final score: 85.9/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It adds a new browser-exposed measurement primitive, not
merely another selection of attributes in an existing fingerprint.

## 85.2 — [On Breaking SAML: Be Whoever You Want to Be](https://www.usenix.org/conference/usenixsecurity12/technical-sessions/presentation/somorovsky) — Juraj Somorovsky, Andreas Mayer, Jörg Schwenk, Marco Kampmann, Meiko Jensen

**KEPT** · Meaningful extension · confidence High

### Candidate

USENIX Security paper and official conference record published in August 2012.

### Core contribution

The authors build an automated XML Signature Wrapping test framework, analyze
14 SAML frameworks and find 11 vulnerable. They introduce a new wrapping variant
and an information-flow-based model that determines whether security-critical
XML data is actually bound to the validated signature.

### Prior art

XML Signature Wrapping was documented in 2005 and applied to cloud APIs before
2012. The new variant, broad SAML framework evaluation and automated
information-flow methodology materially extend that established primitive.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78 | 25% | 19.50 | New variant plus a generalized binding-analysis method. |
| Transferability | 86 | 20% | 17.20 | Applies across SAML stacks and signed XML protocols. |
| Lasting value | 88 | 20% | 17.60 | Signature-validation and application-data mismatch remains fundamental. |
| Technical soundness | 90 | 15% | 13.50 | Fourteen implementations and concrete exploits support the analysis. |
| Practical usability | 86 | 10% | 8.60 | Automated mutations and flow checks are directly useful to assessors. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Variants, framework behavior and success conditions are explicit. |

**Final score: 85.2/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. The primitive is older, but the new variant and reusable
automated SAML analysis substantially advance its capability.

## 85.1 — [Enemy of the State: A State-Aware Black-Box Web Vulnerability Scanner](https://www.usenix.org/conference/usenixsecurity12/technical-sessions/presentation/doupe) — Adam Doupé, Ludovico Cavedon, Christopher Kruegel, Giovanni Vigna

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

USENIX Security paper and presentation published in August 2012.

### Core contribution

The scanner infers an application's state machine from observed pages and
transitions, then uses that state model to revisit actions and inject tests in
the correct workflow context. It addresses the inability of stateless crawlers
to reach or reliably replay deep application behavior.

### Prior art

Black-box scanners, crawling and model inference were established. The distinct
contribution is external web-state inference integrated with vulnerability
testing and evaluated against real applications and scanner benchmarks.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78 | 25% | 19.50 | Integrates inferred application state into black-box security testing. |
| Transferability | 90 | 20% | 18.00 | General to workflow-heavy and session-dependent web applications. |
| Lasting value | 88 | 20% | 17.60 | State and workflow awareness remain core scanner challenges. |
| Technical soundness | 88 | 15% | 13.20 | Formal state handling and empirical comparisons support the approach. |
| Practical usability | 82 | 10% | 8.20 | Operates from the outside without application source. |
| Clarity and reproducibility | 86 | 10% | 8.60 | State construction and scanning workflow are well specified. |

**Final score: 85.1/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It contributes a reusable state-aware
scanner architecture rather than a new vulnerability class.

## 84.9 — [The Most Dangerous Code in the World](https://www.cs.utexas.edu/~shmat/shmat_ccs12.pdf) — Martin Georgiev, Subodh Iyengar, Suman Jana, Rishita Anubhai, Dan Boneh, Vitaly Shmatikov

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Author-hosted ACM CCS paper published in October 2012.

### Core contribution

The paper systematically examines how non-browser software uses TLS certificate
validation APIs. It shows that misleading interfaces, absent hostname checks
and insecure callbacks make many applications and libraries accept
man-in-the-middle certificates, and supplies platform-specific test patterns.

### Prior art

Individual certificate-validation mistakes and TLS man-in-the-middle attacks
were known. The cross-platform API analysis, failure taxonomy and reproducible
assessment of deployed clients form the new methodology.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 70 | 25% | 17.50 | Systematizes a previously scattered TLS API misuse class. |
| Transferability | 92 | 20% | 18.40 | Applies across languages, libraries, apps and API clients. |
| Lasting value | 92 | 20% | 18.40 | Hostname and trust validation remain perennial client failures. |
| Technical soundness | 88 | 15% | 13.20 | Source review and working MITM tests substantiate the findings. |
| Practical usability | 88 | 10% | 8.80 | Failure patterns translate directly into client testing. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Platform examples and validation conditions are explicit. |

**Final score: 84.9/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It turns known isolated validation bugs
into a transferable assessment model for TLS-using software.

## 84.4 — [Self-Exfiltration: The Dangers of Browser-Enforced Information Flow Control](https://www.ieee-security.org/TC/W2SP/2012/papers/w2sp12-final11.pdf) — Eric Y. Chen, Sergey Gorbaty, Astha Singhal, Collin Jackson

**KEPT** · Original technique · confidence High

### Candidate

W2SP paper published in May 2012 and hosted by the official workshop archive.

### Core contribution

The attack writes stolen data into an origin or service that a browser policy
allows, then retrieves the encoded data through a separate channel. The paper
demonstrates that destination whitelists and browser-enforced information-flow
policies cannot prevent exfiltration when an approved destination is also a
readable storage or communication medium.

### Prior art

Same-origin policy, information-flow control and covert channels were known.
The reusable self-exfiltration construction and its demonstrations across eight
browser mechanisms are the distinct contribution.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | New two-stage exfiltration construction against destination policies. |
| Transferability | 92 | 20% | 18.40 | Applies to any allowed endpoint that can encode and later expose data. |
| Lasting value | 86 | 20% | 17.20 | Durable limitation of destination-based browser controls. |
| Technical soundness | 82 | 15% | 12.30 | Multiple browser mechanisms and real destinations demonstrate the claim. |
| Practical usability | 76 | 10% | 7.60 | Requires a suitable allowed carrier but the pattern is straightforward. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Threat model, carriers and attack stages are clear. |

**Final score: 84.4/100.** Archive decision: include as a core technique.

### Verdict

Original technique. The two-stage carrier construction exposes a general flaw
in a class of browser security designs.

## 83.9 — [Off-Path Attacking the Web](https://www.usenix.org/conference/woot12/workshop-program/presentation/gilad) — Yossi Gilad, Amir Herzberg

**KEPT** · Meaningful combination or adaptation · confidence High

### Candidate

WOOT paper and official workshop record published in August 2012.

### Core contribution

An attacker uses a browser puppet to create a connection, a global IP-ID side
channel to infer the server's TCP sequence state and spoofed packets to inject
or corrupt web traffic while remaining off path. This yields page spoofing,
cross-site scripting and request forgery without compromising browser or server.

### Prior art

IP-ID side channels, blind TCP spoofing and browser puppets existed separately.
The reliable sequence-exposure and web exploitation chain is the new capability.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 84 | 25% | 21.00 | New practical chain from global IP-ID leakage to web injection. |
| Transferability | 86 | 20% | 17.20 | General to vulnerable TCP/IP stacks and attacker-triggered connections. |
| Lasting value | 84 | 20% | 16.80 | Durable example of web attacks crossing browser/network layers. |
| Technical soundness | 86 | 15% | 12.90 | Sequence inference and injection are analytically and experimentally validated. |
| Practical usability | 78 | 10% | 7.80 | Network conditions matter, but the attack does not require path control. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Side channel, puppet and packet sequence are explained concretely. |

**Final score: 83.9/100.** Archive decision: include as a core technique.

### Verdict

Meaningful combination or adaptation. Established network primitives are joined
into a distinct remotely triggered web exploitation technique.

## 83.6 — [Detecting and Defending Against Third-Party Tracking on the Web](https://www.usenix.org/conference/nsdi12/technical-sessions/presentation/roesner) — Franziska Roesner, Tadayoshi Kohno, David Wetherall

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

NSDI paper and official presentation record published in April 2012.

### Core contribution

The work instruments browsing to identify third-party tracking relationships,
classifies tracker behavior and measures it at scale. It then validates the model
through TrackingObserver and the ShareMeNot defense, showing how requests can be
rewritten while retaining intentional site interactions.

### Prior art

Cookies, web bugs, fingerprinting and tracker blocking were known. The complete
behavioral classification, measurement method and policy-grounded defense are
the distinct contribution.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 70 | 25% | 17.50 | New systematic method and taxonomy for observing tracker relationships. |
| Transferability | 88 | 20% | 17.60 | General to sites, trackers and evolving third-party request patterns. |
| Lasting value | 90 | 20% | 18.00 | Foundational for modern web privacy measurement. |
| Technical soundness | 90 | 15% | 13.50 | Large crawl, explicit classification and implemented defenses validate it. |
| Practical usability | 82 | 10% | 8.20 | Instrumentation and policy translate into usable tools. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Measurement logic, categories and limitations are documented. |

**Final score: 83.6/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It adds a reusable way to expose and
classify tracking rather than claiming discovery of cookies or third parties.

## 80.6 — [You Are What You Include: Large-scale Evaluation of Remote JavaScript Inclusions](https://www.securitee.org/files/jsinclusions_ccs2012.pdf) — Nick Nikiforakis, Luca Invernizzi, Alexandros Kapravelos, Steven Van Acker, Wouter Joosen, Christopher Kruegel, Frank Piessens, Giovanni Vigna

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Author-hosted ACM CCS paper published in October 2012.

### Core contribution

The authors crawl remote JavaScript inclusions, map dependency chains and study
how websites delegate origin-level authority to third parties. They identify
stale, vulnerable and unexpectedly transitive dependencies at web scale and
provide a repeatable way to measure this attack surface.

### Prior art

The trust risk of third-party scripts was already understood. Large-scale
dependency discovery, transitive-chain analysis and empirical risk measurement
are the new methodology.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 66 | 25% | 16.50 | Systematizes remote-script dependency risk rather than inventing inclusion. |
| Transferability | 88 | 20% | 17.60 | Applies to any site delegating execution to remote JavaScript. |
| Lasting value | 84 | 20% | 16.80 | Third-party supply-chain visibility remains important. |
| Technical soundness | 90 | 15% | 13.50 | Large-scale collection and dependency analysis support the conclusions. |
| Practical usability | 76 | 10% | 7.60 | Crawl and graph method is usable but requires measurement infrastructure. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Inclusion model, dataset and findings are clearly described. |

**Final score: 80.6/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It provides a new, scalable way to find
and reason about inherited remote-script trust.

## 80.3 — [Scriptless Attacks: Stealing the Pie Without Touching the Sill](https://www.nds.rub.de/media/emma/veroeffentlichungen/2012/08/16/scriptlessAttacks-ccs2012.pdf) — Mario Heiderich, Marcus Niemietz, Felix Schuster, Thorsten Holz, Jörg Schwenk

**KEPT** · Original technique · confidence High

### Candidate

Author-hosted ACM CCS paper published in October 2012. This reassesses the
existing missed-list entry under the current rubric.

### Core contribution

The paper composes HTML and CSS features into script-free data-exfiltration
channels, including conditional selectors, resource loads and user-interface
behavior. It demonstrates that disabling JavaScript or relying on script-focused
sanitization does not eliminate active browser attacks.

### Prior art

CSS history leaks, HTML injection and resource-load side channels predate 2012.
The systematic scriptless attack language and new exfiltration constructions are
the distinct contribution.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | Introduces a coherent family of script-free exfiltration techniques. |
| Transferability | 80 | 20% | 16.00 | Applies across HTML/CSS sanitizers and restrictive script policies. |
| Lasting value | 82 | 20% | 16.40 | Scriptless injection remains a durable browser-security category. |
| Technical soundness | 84 | 15% | 12.60 | Multiple primitives and browser demonstrations substantiate the model. |
| Practical usability | 70 | 10% | 7.00 | Payloads depend on parser, CSS and markup capabilities. |
| Clarity and reproducibility | 78 | 10% | 7.80 | The constructions are concrete, though browser support varies. |

**Final score: 80.3/100.** Archive decision: retain as a core technique.

### Verdict

Original technique. It generalizes scattered non-script browser behaviors into
a distinct offensive capability.

## 80.1 — [The Devil is in the (Implementation) Details: An Empirical Analysis of OAuth SSO Systems](https://css.csail.mit.edu/6.858/2012/readings/oauth-sso.pdf) — San-Tsai Sun, Konstantin Beznosov

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

ACM CCS paper published in October 2012; the surviving primary paper records the
three identity providers and 96 relying-party implementations studied.

### Core contribution

The work derives OAuth SSO security properties, observes real browser flows and
systematically tests how relying parties implement tokens, redirects, state and
identity bindings. It exposes recurring implementation tradeoffs and exploitable
departures from provider guidance across deployed sites.

### Prior art

OAuth session fixation, login CSRF and protocol-analysis work predate 2012. The
large empirical relying-party study and implementation-property framework are
the new methodology and are distinct from the S&P traffic-recovery workflow.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 68 | 25% | 17.00 | Adds systematic implementation analysis to known OAuth flaw classes. |
| Transferability | 86 | 20% | 17.20 | Properties apply across OAuth providers and relying parties. |
| Lasting value | 84 | 20% | 16.80 | Redirect, token and state mistakes remain common. |
| Technical soundness | 86 | 15% | 12.90 | Ninety-six relying parties support the empirical conclusions. |
| Practical usability | 80 | 10% | 8.00 | Property checks are directly useful in SSO reviews. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Threats, observations and implementation cases are clearly separated. |

**Final score: 80.1/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. The novelty lies in broad, property-driven
testing of OAuth SSO implementations, not in OAuth or login CSRF alone.

## 79.3 — [WAFFle: Fingerprinting Filter Rules of Web Application Firewalls](https://www.usenix.org/conference/woot12/workshop-program/presentation/schmitt) — Isabell Schmitt, Sebastian Schinzel

**KEPT** · Original technique · confidence High

### Candidate

WOOT paper and official workshop record published in August 2012.

### Core contribution

WAFFle sends paired requests and measures response timing to infer whether a WAF
rule was evaluated or matched, even when visible responses are normalized. It
works directly and through cross-site requests and reports high classification
accuracy against tested filters.

### Prior art

WAF bypasses and general timing side channels were known. Inferring hidden WAF
filter rules from their timing behavior is the distinct attack primitive.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 76 | 25% | 19.00 | New timing oracle for remote WAF rule fingerprinting. |
| Transferability | 80 | 20% | 16.00 | Applies to rule-based filters with measurable processing differences. |
| Lasting value | 76 | 20% | 15.20 | Durable lesson about hidden security-control side channels. |
| Technical soundness | 82 | 15% | 12.30 | Controlled experiments and classification results support the oracle. |
| Practical usability | 84 | 10% | 8.40 | Uses ordinary requests and simple timing measurements. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Probe construction and classifier are concrete. |

**Final score: 79.3/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It turns WAF processing time into a new rule-discovery
channel rather than another syntactic bypass list.

## 79.2 — [Touching from a Distance: Website Fingerprinting Attacks and Defenses](https://www.freehaven.net/anonbib/cache/ccs2012-fingerprinting.pdf) — Xiang Cai, Xin Cheng Zhang, Brijesh Joshi, Rob Johnson

**KEPT** · Meaningful extension · confidence High

### Candidate

ACM CCS paper published in October 2012; the preserved author-distributed paper
contains the full evaluation.

### Core contribution

The attack models ordered packet directions and sizes to identify websites over
encrypted tunnels, then evaluates defenses including randomized pipelining and
HTTPOS. It shows that active page structure remains recognizable under stronger
traffic transformations and Tor-like conditions than earlier attacks handled.

### Prior art

Website fingerprinting dates back at least to the early 2000s. The new feature
representation, evaluation and demonstrated defeat of contemporary defenses are
a material extension, not a claim to the original class.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 70 | 25% | 17.50 | Materially advances features and defense-resistant fingerprinting. |
| Transferability | 82 | 20% | 16.40 | Applies to encrypted web traffic across multiple tunnels and sites. |
| Lasting value | 84 | 20% | 16.80 | Traffic-analysis resistance remains an open anonymity problem. |
| Technical soundness | 86 | 15% | 12.90 | Comparative experiments against sites and defenses substantiate it. |
| Practical usability | 72 | 10% | 7.20 | Requires traffic observation and training traces. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Feature extraction, classifier and experiments are detailed. |

**Final score: 79.2/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It strengthens an older attack family enough to defeat
then-current countermeasures and expands its operational scope.

## 77.5 — [FlashOver: Automated Discovery of Cross-site Scripting Vulnerabilities in Rich Internet Applications](https://www.securitee.org/files/flashover_asiaccs2012.pdf) — Steven Van Acker, Nick Nikiforakis, Lieven Desmet, Wouter Joosen, Frank Piessens

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Author-hosted AsiaCCS paper published in May 2012.

### Core contribution

FlashOver decompiles SWF files, statically locates security-sensitive input-to-
sink patterns and then drives the containing browser to validate exploitability.
The hybrid analysis reports 286 XSS and 523 URL-injection findings in a large
collection of deployed Flash applications.

### Prior art

Flash decompilation, DOM XSS and static taint analysis were known. The automated
SWF-to-browser validation pipeline and its targeted patterns form the distinct
web-testing methodology.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 68 | 25% | 17.00 | New hybrid pipeline tailored to deployed rich web applications. |
| Transferability | 78 | 20% | 15.60 | General across ActionScript applications and browser integrations. |
| Lasting value | 76 | 20% | 15.20 | Flash faded, but hybrid static/dynamic validation remains relevant. |
| Technical soundness | 86 | 15% | 12.90 | Large-scale findings and browser confirmation support precision. |
| Practical usability | 84 | 10% | 8.40 | Automates candidate extraction and exploit validation. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Patterns and analysis stages are well described. |

**Final score: 77.5/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It contributes an effective automated
discovery workflow for Flash-based web injection rather than a new XSS class.

## 76.8 — [Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security](https://teamusec.de/publications/conf-ccs-fahlhmsbf12/) — Sascha Fahl, Marian Harbach, Thomas Muders, Matthew Smith, Lars Baumgärtner, Bernd Freisleben

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Author publication record and linked ACM CCS paper place publication in October
2012.

### Core contribution

MalloDroid statically identifies suspicious TLS-validation code in Android apps
and feeds likely cases into dynamic man-in-the-middle confirmation. A study of
13,500 apps exposes widespread hostname, certificate and trust-manager failures
and connects source patterns to exploitable network behavior.

### Prior art

Individual mobile TLS mistakes and insecure certificate callbacks were known.
The large-scale Android-specific static-to-dynamic testing workflow is the new
methodology; it complements rather than duplicates the broader TLS API study.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 58 | 25% | 14.50 | Strong new assessment pipeline, though the flaw classes were established. |
| Transferability | 78 | 20% | 15.60 | Adaptable to mobile clients and other certificate-validation APIs. |
| Lasting value | 84 | 20% | 16.80 | Mobile TLS validation remains a persistent assessment target. |
| Technical soundness | 86 | 15% | 12.90 | Large corpus plus dynamic confirmation supports the results. |
| Practical usability | 88 | 10% | 8.80 | Static triage sharply focuses reproducible MITM testing. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Detection patterns and confirmation procedure are clear. |

**Final score: 76.8/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It operationalizes TLS validation review at
Android-app scale without claiming a new cryptographic attack.

## 76.4 — [Host Fingerprinting and Tracking on the Web: Privacy and Security Implications](https://www.ndss-symposium.org/ndss2012/ndss-2012-programme/host-fingerprinting-and-tracking-web-privacy-and-security-implications/) — Ting-Fang Yen, Yinglian Xie, Fang Yu, Roger Peng Yu, Martin Abadi

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

NDSS paper and official programme record published in February 2012.

### Core contribution

Using large Hotmail and Bing traces, the work combines network, browser and
behavioral attributes to recognize hosts after cookies are cleared or private
browsing is used. It quantifies stability and false matches at deployment scale
and evaluates both tracking and account-security uses.

### Prior art

Cookie respawning, IP tracking and Panopticlick-style attribute fingerprints
predate 2012. The large-scale multi-signal host-linking methodology is the new
contribution.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 60 | 25% | 15.00 | Extends known fingerprints into measured host linking at service scale. |
| Transferability | 82 | 20% | 16.40 | Signals generalize across large login, search and fraud datasets. |
| Lasting value | 80 | 20% | 16.00 | Multi-signal tracking and device recognition remain important. |
| Technical soundness | 88 | 15% | 13.20 | Large real-world datasets and error analysis support the findings. |
| Practical usability | 74 | 10% | 7.40 | Requires service-side data but supplies a concrete matching method. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Features, thresholds and evaluation are explicit. |

**Final score: 76.4/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It systematizes durable host recognition
from multiple web signals rather than introducing fingerprinting itself.

## 70.7 — [XSS-FP: Browser Fingerprinting using HTML Parser Quirks](https://arxiv.org/abs/1211.4812) — Erwan Abgrall, Yves Le Traon, Martin Monperrus, Sylvain Gombault, Mario Heiderich, Alain Ribault

**KEPT** · Original technique · confidence Medium

### Candidate

Primary technical report submitted on 20 November 2012. Its dated manuscript,
authors and experiments establish first public availability in the target year.

### Core contribution

XSS-FP feeds malformed markup and XSS-derived parser tests to the browser, then
observes the resulting DOM or execution behavior. Differences in error recovery
fingerprint browser family and version, often with a small test subset.

### Prior art

User-agent, JavaScript-capability, network and rendering fingerprints predate the
report. Using security-relevant HTML parser differentials as the fingerprinting
oracle is the distinct primitive.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 62 | 25% | 15.50 | New use of malformed-markup parsing behavior as a fingerprint. |
| Transferability | 78 | 20% | 15.60 | Parser differentials exist across browser families and versions. |
| Lasting value | 68 | 20% | 13.60 | The concept endures, though exact signatures age quickly. |
| Technical soundness | 72 | 15% | 10.80 | Experiments support the idea but are smaller than top-tier studies. |
| Practical usability | 76 | 10% | 7.60 | A compact set of markup probes is easy to deploy. |
| Clarity and reproducibility | 76 | 10% | 7.60 | Tests and classification results are sufficiently documented. |

**Final score: 70.7/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It contributes a browser-measurement channel based on HTML
parser error recovery, distinct from earlier fingerprints.

## 65.1 — [Web-based Attacks on Host-Proof Encrypted Storage](https://www.usenix.org/conference/woot12/workshop-program/presentation/bhargavan) — Karthikeyan Bhargavan, Antoine Delignat-Lavaud

**KEPT** · Meaningful combination or adaptation · confidence Medium

### Candidate

WOOT paper and official workshop record published in August 2012.

### Core contribution

The paper shows how web delivery, origin trust, code updates and password-manager
integration can defeat the promises of host-proof encrypted storage even when
the cryptography itself is sound. It builds concrete attacks around malicious or
compromised application code and unsafe browser workflows.

### Prior art

XSS, malicious JavaScript and client-side encryption were established. Applying
those mechanisms as a systematic attack model against the host-proof trust claim
is a useful new combination, but not a wholly new primitive.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 54 | 25% | 13.50 | Mostly known web capabilities organized against a new trust model. |
| Transferability | 68 | 20% | 13.60 | Applies to browser-delivered encrypted stores and password managers. |
| Lasting value | 64 | 20% | 12.80 | Durable warning, though modern packaging can change assumptions. |
| Technical soundness | 76 | 15% | 11.40 | Concrete system analysis and attacks substantiate the claim. |
| Practical usability | 62 | 10% | 6.20 | Useful review model but often depends on broader compromise. |
| Clarity and reproducibility | 76 | 10% | 7.60 | Trust boundaries and attack paths are explicit. |

**Final score: 65.1/100.** Archive decision: include as supporting technique.

### Verdict

Meaningful combination or adaptation. It qualifies by exposing a reusable web
trust failure in client-side encrypted storage, not by numeric score alone.

## 60.9 — [Cruel Intentions: Violating Browser Security and Privacy Through Web Intents](https://www.ieee-security.org/TC/W2SP/2012/papers/w2sp12-final10.pdf) — Jenna Kallaher, Amal Krishnan, Paul Makowski, Eric Chen, Collin Jackson

**KEPT** · Meaningful extension · confidence Medium

### Candidate

W2SP paper published in May 2012 against the then-current Web Intents prototype.

### Core contribution

The work analyzes the browser's proposed service-dispatch mechanism and
demonstrates tracking, denial of service, intent overwrite and login-CSRF attack
paths created by its handler selection and invocation semantics.

### Prior art

Confused-deputy behavior, login CSRF and mobile intent security were known. The
paper carries those ideas into a browser-native inter-application dispatch model
and identifies concrete web-specific failure modes before deployment.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 54 | 25% | 13.50 | Extends established mechanisms to a new browser service primitive. |
| Transferability | 64 | 20% | 12.80 | Lessons apply to browser and app handler-dispatch systems. |
| Lasting value | 50 | 20% | 10.00 | Web Intents itself was short-lived, limiting direct longevity. |
| Technical soundness | 72 | 15% | 10.80 | Prototype attacks establish the claimed failure modes. |
| Practical usability | 62 | 10% | 6.20 | Useful design-testing cases, but tied to an emerging API. |
| Clarity and reproducibility | 76 | 10% | 7.60 | Each attack and required behavior is clearly described. |

**Final score: 60.9/100.** Archive decision: include as supporting technique.

### Verdict

Meaningful extension. The browser dispatch context creates a defensible new
application of known security failures, narrowly clearing the historical gate.

## 84.2 — [Are You My Type? Breaking .NET Through Serialization](https://media.blackhat.com/bh-us-12/Briefings/Forshaw/BH_US_12_Forshaw_Are_You_My_Type_WP.pdf)

**KEPT** · Original technique · confidence High

### Candidate

James Forshaw, Context Information Security, Black Hat USA 2012 (July 2012);
whitepaper, slides and conference video. Surfaced by the 2026-08-12 pass over
the ysonet .NET-deserialization reference set.

### Core contribution

The first systematic demonstration that .NET's own serializers are an attack
surface rather than a data format. Stripped of its 2012 targets, the
contribution is a method: enumerate the framework for types whose
deserialization callbacks, property setters or finalizers have side effects,
then reach one of them through any sink that deserializes untrusted input. It
adds three concrete primitives — type aliasing through
`SerializationInfo.SetType` so an object is reconstructed as an unrelated type,
delegate multicasting across incompatible signatures to produce CLR type
confusion, and the `Hashtable` comparer callback that hands attacker keys back
to attacker code during rebuild. The type-survey table (how many
`[Serializable]`, `ISerializable`, callback and finalizable types each core
assembly holds) is the origin of gadget hunting in .NET.

### Prior art

Deserialization abuse was known in other stacks — the Java `Calendar`
vulnerability CVE-2008-5353, the COM interoperability work presented at Black
Hat 2009, and long-standing misuse of PHP `unserialize()`; Forshaw cites all
three as motivation. No earlier public work demonstrated exploitation of .NET
`BinaryFormatter`/`SoapFormatter` or named framework gadget types. Later work
treats this talk as the origin: Birch's 2023 DEF CON 31 whitepaper opens with
"James Forshaw made an initial demonstration of the exploitability of
BinaryFormatter in his 2012 'Are You My Type' talk", and Muñoz and Mirosh's
2017 "Friday the 13th: JSON Attacks" builds directly on it.

Scope is borderline and stated plainly: the 2012 delivery vectors are XBAP
browser-hosted applications, Partial Trust sandboxes and .NET Remoting rather
than an HTTP request parameter. The transferable core is scored, not the
sandbox vectors — and that core is what ViewState, SharePoint, Exchange and
Telerik RCE all run on. The repository already treats this class as in scope
(2018 nominated PHP unserialization, 2019 .NET Remoting over HTTP, 2023 ranked
hardened .NET deserialization at #2).

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 88 | 25% | 22.00 | First public exploitation of .NET serialization, with three distinct new primitives and a gadget-survey method. |
| Transferability | 78 | 20% | 15.60 | The gadget-hunting residue transfers to every .NET deserialization sink; the specific XBAP and Partial Trust vectors do not. |
| Lasting value | 92 | 20% | 18.40 | Cited as the origin by essentially all later .NET deserialization research; ysoserial.net exists downstream of it. |
| Technical soundness | 88 | 15% | 13.20 | Vendor-confirmed as MS12-035 with CVE-2012-0160 and CVE-2012-0161, plus debugger evidence and live demonstrations. |
| Practical usability | 70 | 10% | 7.00 | The named sandbox escapes are patched; the method and the type-confusion primitives stay usable. |
| Clarity and reproducibility | 80 | 10% | 8.00 | Whitepaper plus slides give code for each primitive, though several slide diagrams did not survive extraction. |

**Final score: 84.2/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It established .NET deserialization as an attack class and
supplied the survey method and the type-confusion primitives that the following
decade of web-facing .NET RCE was built from.

### Reverification

- **Candidate facts rechecked against:** the archived whitepaper and slide deck,
  which carry the author, venue, MS12-035 and both CVE numbers.
- **Independent prior-art check:** searched by mechanism ("BinaryFormatter
  deserialization attack before 2012", type confusion via serialized delegates)
  rather than by title, and followed citations backward from the 2017 and 2023
  successor talks. Both name this work as the initial .NET demonstration; no
  earlier .NET result surfaced.
- **Strongest challenge to the result:** the 2012 attacker is often local
  (Partial Trust, ClickOnce) rather than remote-over-HTTP, so a strict reading
  puts the talk outside a web list.
- **Benefit-of-doubt check:** XBAP is browser-delivered, and the whitepaper's
  .NET Remoting section is a network-service attack; the primitives are the ones
  later used over HTTP.
- **Changes after reverification:** none. Transferability was held at 78 rather
  than raised, so the borderline scope is reflected in the score.
