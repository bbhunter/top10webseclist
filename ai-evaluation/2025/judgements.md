# 2025 candidate judgements

These scorecards apply the repository's weighted judge rubric. `KEPT` means the
candidate met the historical 60-or-above inclusion rule as well as the
first-publication, originality-verdict and original-nomination exclusions.

## 86.9 — [My ZIP isn't your ZIP: Identifying and Exploiting Semantic Gaps Between ZIP Parsers](https://www.usenix.org/conference/usenixsecurity25/presentation/you)

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed USENIX Security research published in August 2025; its primary
URL was absent from the 74-link exclusion set.

### Core contribution

ZipDiff differentially tests 50 parsers across 19 languages and organizes their
disagreements into 14 ambiguity types, ten newly reported. Crafted archives
bypass mail gateways, spoof office content or extensions, and preserve a nested
JAR signature while changing the interpreted payload.

### Prior art

ZIP confusion, Zip Slip and individual parser discrepancies were established,
including the year's nominated disguised-path traversal. The reusable gain is
the systematic ambiguity taxonomy and cross-parser exploit construction across
security boundaries, not archive parsing itself.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | Ten new ambiguity types extend known isolated parser gaps. |
| Transferability | 90 | 20% | 18.00 | Crosses languages, formats, gateways, documents and package systems. |
| Lasting value | 86 | 20% | 17.20 | The taxonomy remains useful for parser and signing design. |
| Technical soundness | 92 | 15% | 13.80 | Broad differential testing and five exploit settings validate it. |
| Practical usability | 86 | 10% | 8.60 | ZipDiff and concrete scenarios make the gaps testable. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Ambiguity classes and demonstrations are explicit. |

**Final score: 86.9/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It turns scattered ZIP parsing bugs into a transferable
cross-parser attack methodology with several newly demonstrated ambiguity types.

## 86.3 — [STEK Sharing is Not Caring: Bypassing TLS Authentication in Web Servers using Session Tickets](https://www.usenix.org/conference/usenixsecurity25/presentation/hebrok)

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed USENIX Security research published in August 2025.

### Core contribution

When virtual hosts share a Session Ticket Encryption Key, a ticket issued in
one host context can be resumed in another whose authentication policy differs.
The resulting ticket confusion bypasses client authentication in Apache, nginx,
LiteSpeed and Caddy and can also break server authentication in provider clusters.

### Prior art

TLS resumption, cross-host ticket sharing and virtual-host isolation risks were
known design concerns. The demonstrated cross-vhost session-context confusion
that bypasses both client and server authentication is a distinct attack class.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 88 | 25% | 22.00 | Establishes ticket-context confusion as an authentication bypass. |
| Transferability | 86 | 20% | 17.20 | Affects four major servers and shared-hosting architectures. |
| Lasting value | 88 | 20% | 17.60 | Captures a durable key-sharing and context-binding failure. |
| Technical soundness | 90 | 15% | 13.50 | Implementation analysis and provider scans substantiate it. |
| Practical usability | 76 | 10% | 7.60 | Requires compatible ticket/key sharing and host policy differences. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Resumption flow and affected configurations are documented. |

**Final score: 86.3/100.** Archive decision: include as a core technique.

### Verdict

Original technique. The ticket is accepted cryptographically but rebound to the
wrong virtual-host security context, creating the reusable primitive.

## 84.6 — [Cascading Spy Sheets: Exploiting the Complexity of Modern CSS for Email and Browser Fingerprinting](https://www.ndss-symposium.org/ndss-paper/cascading-spy-sheets-exploiting-the-complexity-of-modern-css-for-email-and-browser-fingerprinting/)

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed NDSS paper first published in 2025.

### Core contribution

Fuzzed CSS container queries, arithmetic functions and complex selectors build
scriptless probes for application, OS and hardware properties. The approach
distinguishes browser/OS combinations and operates in restrictive HTML email
clients where JavaScript is unavailable.

### Prior art

CSS data leakage, scriptless side channels and browser/extension fingerprinting
were established. Systematically composing modern dynamic CSS into high-
dimensional fingerprints, especially inside email, is the qualifying extension.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | Adds three modern CSS probe families and email applicability. |
| Transferability | 88 | 20% | 17.60 | Covers browsers, operating systems, hardware and mail clients. |
| Lasting value | 82 | 20% | 16.40 | Shows why script blocking alone cannot stop rich-CSS fingerprinting. |
| Technical soundness | 90 | 15% | 13.50 | Fuzzing and broad configuration testing support the claims. |
| Practical usability | 80 | 10% | 8.00 | Probes work in deployable HTML/CSS environments. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Techniques, results and defenses are detailed. |

**Final score: 84.6/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. The privacy goal is known, but modern CSS creates new,
scriptless fingerprint dimensions and reaches the stricter email environment.

## 84.0 — [Automatic Insecurity: Exploring Email Auto-configuration in the Wild](https://www.ndss-symposium.org/ndss-paper/automatic-insecurity-exploring-email-auto-configuration-in-the-wild/)

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed NDSS paper first published in 2025.

### Core contribution

Email clients retrieve connection settings from domain-controlled discovery
mechanisms before login. The work defines ten attack scenarios across protocol,
deployment and UI failures that silently steer victims to attacker servers or
insecure transport, exposing credentials across many domains and clients.

### Prior art

Exchange Autodiscover abuse, configuration mistakes and TLS downgrade were
known separately. A cross-client model of auto-configuration trust and UI
composition, with eight newly identified defects, was not represented earlier.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 84 | 25% | 21.00 | Defines a broad discovery-to-credential attack surface. |
| Transferability | 86 | 20% | 17.20 | Spans standards, domains and 29 clients. |
| Lasting value | 82 | 20% | 16.40 | Auto-discovery trust remains a durable bootstrap problem. |
| Technical soundness | 88 | 15% | 13.20 | Attack scenarios and large-scale measurements align. |
| Practical usability | 78 | 10% | 7.80 | Exploitation depends on discovery control or misconfiguration. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Defects, scenarios and client behavior are organized clearly. |

**Final score: 84.0/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It elevates email configuration bootstrap into a systematic
credential-redirection attack model rather than another Autodiscover case study.

## 83.0 — [Posthammer: Pervasive Browser-based Rowhammer Attacks with Postponed Refresh Commands](https://www.usenix.org/conference/usenixsecurity25/presentation/de-ridder)

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2025.

### Core contribution

JavaScript generates sustained hammering followed by delay windows that cause
the memory controller to batch refresh commands. A new lane abstraction creates
non-uniform access patterns, raising browser-triggered bit flips from limited
coverage to 86% of 28 tested DDR4 devices.

### Prior art

Rowhammer.js established browser-based fault attacks in 2015, and postponed-
refresh concepts existed natively. The distinct gain is making refresh
postponement and non-uniform patterns practical inside the browser sandbox.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 80 | 25% | 20.00 | Adds practical refresh postponement and lanes to browser Rowhammer. |
| Transferability | 80 | 20% | 16.00 | Generalizes across many tested DDR4 devices. |
| Lasting value | 86 | 20% | 17.20 | Changes assumptions about browser feasibility under in-DRAM defenses. |
| Technical soundness | 92 | 15% | 13.80 | Large device testing and bit-flip evidence are strong. |
| Practical usability | 74 | 10% | 7.40 | Hardware layout and browser constraints remain. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Patterns, lane model and evaluation are explicit. |

**Final score: 83.0/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It substantially expands the reach of the established
Rowhammer.js primitive rather than claiming browser Rowhammer as new.

## 80.5 — [EvoCrawl: Exploring Web Application Code and State using Evolutionary Search](https://www.ndss-symposium.org/ndss-paper/evocrawl-exploring-web-application-code-and-state-using-evolutionary-search/)

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed NDSS paper first published in 2025.

### Core contribution

EvoCrawl evolves sequences of browser interactions that satisfy relationships
between fields, events and server state. It submits valid forms more often,
raises code coverage, and exposes state-dependent IDOR and XSS paths missed by
contemporary crawlers.

### Prior art

State-aware scanners and dynamic Web crawlers date back at least to Enemy of
the State and jÄk. Evolutionary search over complete interaction sequences and
state-constrained form submission is the methodological advance.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 70 | 25% | 17.50 | Adds evolutionary sequence search to established state-aware crawling. |
| Transferability | 84 | 20% | 16.80 | Applies across forms, workflows and vulnerability engines. |
| Lasting value | 82 | 20% | 16.40 | State reachability remains a central scanner limitation. |
| Technical soundness | 88 | 15% | 13.20 | Comparative coverage and zero-day results support it. |
| Practical usability | 84 | 10% | 8.40 | Integrates with IDOR and XSS scanners. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Search representation and evaluation are detailed. |

**Final score: 80.5/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. The vulnerabilities are known; improved
state-sequence exploration is the qualifying contribution.

## 80.1 — [SAML roulette: the hacker always wins](https://portswigger.net/research/saml-roulette-the-hacker-always-wins)

**KEPT** · Original technique · confidence High

### Candidate

PortSwigger published the research on 18 March 2025; it was already present in
the missed section and is reassessed here without duplication.

### Core contribution

A signed SAML document is parsed and serialized with one XML implementation,
then reparsed with another for attribute access. Comments, CDATA and namespace
behavior mutate structure across the round trip, so the authenticated identity
differs from the identity consumed by the application.

### Prior art

XML signature wrapping, SAML parser differentials and XML round-trip mutation
were known. The work's reusable contribution is the concrete mutation chain
that converts parser/serializer disagreement into unauthenticated impersonation.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | Derives an identity swap from round-trip structural mutation. |
| Transferability | 82 | 20% | 16.40 | Applies to multi-parser SAML and signed-XML pipelines. |
| Lasting value | 82 | 20% | 16.40 | Reinforces a durable parse-once security invariant. |
| Technical soundness | 86 | 15% | 12.90 | A complete Ruby-SAML/GitLab chain substantiates it. |
| Practical usability | 70 | 10% | 7.00 | Requires a vulnerable parse-serialize-reparse pipeline. |
| Clarity and reproducibility | 69 | 10% | 6.90 | Mutation details are public, though target conditions are specific. |

**Final score: 80.1/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It is related to signature wrapping but the exploitable
primitive is identity-changing round-trip mutation between parser stages.

## 79.6 — [RaceDB: Detecting Request Race Vulnerabilities in Database-Backed Web Applications](https://doi.org/10.1109/SP61157.2025.00029)

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed IEEE S&P paper published on 12 May 2025.

### Core contribution

RaceDB models dependencies across application logic and database queries,
identifies feasible request interleavings, then uses replay-based execution to
separate true races from false positives and generate definitive exploits. It
recovered known races and discovered new vulnerabilities in PHP applications.

### Prior art

Web race conditions, single-packet synchronization and temporal session races
were established. Application-aware database dependency analysis plus automated
replay verification and exploit generation is the qualifying methodology.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 66 | 25% | 16.50 | Advances detection of an established vulnerability class. |
| Transferability | 82 | 20% | 16.40 | Model applies across database-backed request logic. |
| Lasting value | 82 | 20% | 16.40 | Connects code and query dependencies in a reusable way. |
| Technical soundness | 90 | 15% | 13.50 | Known/new vulnerability and false-positive results are strong. |
| Practical usability | 86 | 10% | 8.60 | Generates verified race exploits. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Detection and replay stages are specified. |

**Final score: 79.6/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It does not make request races new; it
makes subtle database-backed races verifiable and exploitable automatically.

## 78.8 — [NodeMedic-FINE: Automatic Detection and Exploit Synthesis for Node.js Vulnerabilities](https://www.ndss-symposium.org/ndss-paper/nodemedic-fine-automatic-detection-and-exploit-synthesis-for-node-js-vulnerabilities/)

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed NDSS paper first published in 2025.

### Core contribution

Type- and object-structure-aware fuzzing supplies valid package API inputs,
while dynamic taint results guide payload construction through transformations
to command/code-execution sinks. The system synthesized working exploits in
hundreds of npm packages rather than stopping at potential flows.

### Prior art

Node.js taint analysis, object-dependence graphs, command injection and exploit
synthesis were established. Feedback between inferred structured inputs and
payload synthesis materially improves automated exploit confirmation.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 62 | 25% | 15.50 | Improves an established dynamic-analysis and synthesis line. |
| Transferability | 82 | 20% | 16.40 | Handles varied npm APIs, types and object layouts. |
| Lasting value | 80 | 20% | 16.00 | Structured-input inference remains broadly useful. |
| Technical soundness | 90 | 15% | 13.50 | Large-scale flows and hundreds of working exploits validate it. |
| Practical usability | 90 | 10% | 9.00 | Produces proof exploits rather than unconfirmed sink reports. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Fuzzing, taint and synthesis interaction is explicit. |

**Final score: 78.8/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. Its value is stronger exploit synthesis for
known Node.js vulnerability classes, not a new injection primitive.

## 78.4 — [Cross-Origin Web Attacks via HTTP/2 Server Push and Signed HTTP Exchange](https://www.ndss-symposium.org/ndss-paper/cross-origin-web-attacks-via-http-2-server-push-and-signed-http-exchange/)

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed NDSS paper first published in 2025.

### Core contribution

CrossPUSH and CrossSXG exploit cases where HTTP/2 authority or signed-exchange
validation follows the certificate SAN set rather than the URI origin. An
off-path attacker controlling one shared-certificate domain can inject content,
cookies or downloads under sibling domains.

### Prior art

The 2022 nomination `A Magic Way of XSS in HTTP/2` already demonstrated shared-
certificate server-push XSS, so CrossPUSH is not scored as original. Systematic
browser/site validation, broader effects and the separate SXG route are the
2025 contribution.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 68 | 25% | 17.00 | CrossPUSH extends 2022 work; CrossSXG supplies a new route. |
| Transferability | 84 | 20% | 16.80 | Shared certificates and affected features cross many sites. |
| Lasting value | 78 | 20% | 15.60 | Durable warning about certificate authority versus Web origin. |
| Technical soundness | 88 | 15% | 13.20 | Browser, website and vendor evidence supports the attacks. |
| Practical usability | 76 | 10% | 7.60 | Requires feature support and a shared-certificate attacker domain. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Both attack paths and outcomes are documented. |

**Final score: 78.4/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. The record preserves the 2022 priority while recognizing
the new SXG vector and systematic expansion of the HTTP/2 push technique.

## 77.3 — [Do (Not) Follow the White Rabbit: Challenging the Myth of Harmless Open Redirection](https://www.ndss-symposium.org/ndss-paper/do-not-follow-the-white-rabbit-challenging-the-myth-of-harmless-open-redirection/)

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed NDSS paper first published in 2025.

### Core contribution

STORK extracts JavaScript redirect indicators with static and dynamic analysis,
mines live and historical pages for client-side open redirects, and tests
whether their surrounding context escalates them to XSS, CSRF or data leakage.

### Prior art

Open redirects and product-specific escalation chains were long known. The
qualifying gain is scalable indicator extraction and context-aware escalation
analysis, not a claim that redirection itself is new.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 62 | 25% | 15.50 | Systematizes detection and escalation of a known weakness. |
| Transferability | 82 | 20% | 16.40 | Covers varied JavaScript redirect forms and escalation contexts. |
| Lasting value | 78 | 20% | 15.60 | Reframes impact assessment for client-driven redirects. |
| Technical soundness | 88 | 15% | 13.20 | Large-scale findings and validated escalations support it. |
| Practical usability | 82 | 10% | 8.20 | Indicators and mining make the method operational. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Pipeline, catalog and escalation results are clear. |

**Final score: 77.3/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. STORK converts open-redirect triage from a
low-impact label into evidence-based discovery and escalation testing.

## 76.8 — [Phishing Attacks against Password Manager Browser Extensions](https://www.usenix.org/conference/usenixsecurity25/presentation/anliker)

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2025.

### Core contribution

A hostile site imitates a locked password-manager extension prompt because
extension UI is overlaid inside the same viewport and lacks a reliable trusted
visual boundary. Implementations for four managers and a large user study show
that victims disclose the high-value master password.

### Prior art

UI redressing, browser-dialog spoofing, phishing and password-manager attacks
were established. Targeting indistinguishable in-viewport extension chrome to
capture the master credential is a meaningful adaptation with measured effect.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 66 | 25% | 16.50 | Adapts UI spoofing to the extension/website boundary. |
| Transferability | 78 | 20% | 15.60 | Applies across several password-manager extension designs. |
| Lasting value | 76 | 20% | 15.20 | Trusted-path ambiguity persists for overlaid browser UI. |
| Technical soundness | 86 | 15% | 12.90 | Implementations and a large study support effectiveness. |
| Practical usability | 84 | 10% | 8.40 | A normal hostile page can present the imitation. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Threat model, variants and study are documented. |

**Final score: 76.8/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It is not generic phishing alone; the browser's failure to
distinguish extension UI from page content creates the reusable condition.

## 75.0 — [Universal Cross-app Attacks: Exploiting and Securing OAuth 2.0 in Integration Platforms](https://www.usenix.org/conference/usenixsecurity25/presentation/luo-kaixuan)

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2025 and already
present in the missed section.

### Core contribution

Integration platforms mediate OAuth account linking for many third-party apps
but fail to distinguish which app an authorization belongs to. A malicious app
can therefore cause Cross-app OAuth Account Takeover or Request Forgery against
other linked services; COVScan profiles platforms for both patterns.

### Prior art

OAuth mix-up, redirect confusion, CSRF and multi-tenant identity failures were
known. The platform-wide cross-app capability created by a shared integration
broker is the distinct extension.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 74 | 25% | 18.50 | Adds cross-app COAT/CORF patterns to known OAuth confusion. |
| Transferability | 78 | 20% | 15.60 | Applies across automation, assistant and smart-home platforms. |
| Lasting value | 76 | 20% | 15.20 | Shared brokers remain a durable authorization boundary. |
| Technical soundness | 82 | 15% | 12.30 | COVScan and multi-platform validation support the patterns. |
| Practical usability | 68 | 10% | 6.80 | Requires a malicious linked app or crafted authorization path. |
| Clarity and reproducibility | 66 | 10% | 6.60 | Attacks are clear, though platform details vary. |

**Final score: 75.0/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. Shared platform mediation turns familiar OAuth identity
confusion into universal attacks across otherwise unrelated integrated apps.
