# 2025 candidate judgements

These scorecards apply the repository's weighted judge rubric. `KEPT` means the
candidate met the historical 55-or-above inclusion rule as well as the
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

## 76.4 — [Styled to Steal: The Overlooked Attack Surface in Email Clients](https://doi.org/10.1145/3719027.3765189) [Artifact](https://github.com/cispa/stylemail) — Leon Trampert, Daniel Weber, Christian Rossow, Michael Schwarz, CISPA

**KEPT** · Meaningful extension · confidence High

### Candidate

ACM CCS '25, Taipei, October 2025 — in the 2025 window and absent from the
nomination round. Found in the 2026-08-11 CCS sweep. Read in full from the
authors' open figshare copy (`stylemail_ccs25.pdf`), since the ACM landing page
is walled.

### Core contribution

A scriptless attack that recovers **arbitrary plaintext out of an end-to-end
encrypted email** using CSS alone. Three benign features compose into the
primitive: container queries decide, lazy-loaded web fonts fire the request, and
contextual ligatures map each character of the decrypted text to a distinct font
glyph — so every character becomes a unique network request to the attacker.
The recovery completes in a **single rendering pass**, with no JavaScript, no
visual artifact, and depending on client configuration no user interaction at
all. Demonstrated end to end against PGP mail in Thunderbird and KMail, with a
proof of concept against Meta's Code Verify (Accountable JavaScript) and a
finding that DOMPurify's default configuration does not stop it.

### Prior art

Dense, and partly in this same year's list. Efail (2018) established
content exfiltration from encrypted mail through crafted HTML, and the isolation
mitigations this paper defeats were the response to it. **Fontleak** (already in
`2025.md`) exfiltrates text with CSS and ligatures, and **Cascading Spy Sheets**
(in this missed list, same first author) covers CSS-based email and browser
fingerprinting. Blind CSS exfiltration (2023, in archive), the Firefox
single-injection-point work (2020, in archive) and Bench Press (2024, in archive)
carry the wider lineage.

### Candidate's distinct contribution

Not the ligature oracle — that is Fontleak's, in the same year. What is new is
the **threat model it reaches**: plaintext out of an E2EE mailbox rather than
text off a web page, defeating the specific isolation that email clients adopted
after Efail. Plus the single-pass, zero-interaction construction, and two
results that transfer past email: Code Verify does not stop it, and DOMPurify's
defaults do not either.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 66 | 25% | 16.50 | The ligature primitive is Fontleak's, published the same year; the new threat model and single-pass construction are the increment. |
| Transferability | 78 | 20% | 15.60 | Applies across three mail clients and reaches Code Verify and DOMPurify; the primitive works in any CSS-injection context. |
| Lasting value | 74 | 20% | 14.80 | Post-Efail isolation is a standing design problem, and practitioner work in 2026 already cites this as the CCS result for scriptless CSS on mail clients. |
| Technical soundness | 88 | 15% | 13.20 | Peer-reviewed, end-to-end exploits, responsible disclosure to GPGSuite, Thunderbird and KMail. |
| Practical usability | 78 | 10% | 7.80 | Artifact released at github.com/cispa/stylemail. |
| Clarity and reproducibility | 85 | 10% | 8.50 | Full paper plus a public artifact. |

**Final score: 76.4/100.** Archive decision: include as a core technique.

### Reverification

- **Candidate facts rechecked against:** the paper itself (title page, contribution
  list, threat model), the figshare record for authorship and affiliation, and the
  CCS '25 proceedings reference in the paper's own ACM citation block.
- **Independent prior-art check:** searched the year lists and the archive by
  mechanism — ligature oracle, CSS exfiltration, scriptless attack, Efail — rather
  than by title. That surfaced Fontleak in this very list, which the abstract does
  not mention and which materially reduces the originality claim.
- **Strongest challenge to the result:** with Fontleak already listed for 2025,
  a reader could call this the same technique with a different target, which would
  make it a duplicate rather than an extension.
- **Benefit-of-doubt check:** it survives that challenge because the target is the
  contribution here — recovering plaintext from inside an E2EE mailbox is a
  different security property from reading a rendered page, and the isolation it
  defeats was purpose-built against exactly this class after Efail.
- **Changes after reverification:** Original contribution cut from 72 to 66 and the
  total from 78.7 to 76.4 once Fontleak was found in the same year's list.

### Verdict

Meaningful extension. New is the E2EE-mail threat model, the single-pass
zero-interaction construction, and the Code Verify and DOMPurify results.
Already known is the ligature oracle, CSS exfiltration generally, and that
crafted markup can exfiltrate decrypted mail.

- **Archive decision:** Include as a core technique
- **Confidence:** High
- **Evidence gaps:** None material; the paper and its artifact were both read.

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

## 61.1 — [Cloudflare Image Proxy as a CSPT Gadget: A Cross-Origin CSPT Exploit](https://blog.voorivex.team/cloudflare-image-proxy-as-a-cspt-gadget-a-cross-origin-cspt-exploit) — Amirmohammad Safari, Voorivex

**KEPT** · Meaningful extension · confidence Medium

### Candidate

Published 19 October 2025 on the Voorivex team blog; not in the original 2025
nomination round and absent from the exclusion set. Found in the 10 August 2026
single-publisher sweep of `blog.voorivex.team`.

### Core contribution

Client-Side Path Traversal is normally reasoned about as a same-origin primitive:
the injected `../` rewrites the path of a request the page was already going to
make, so the request stays on the origin. This chains it with a redirect gadget
that returns 307 or 308, which preserve method and body, so the rewritten request
lands on a *different* origin still carrying its verb and payload. That converts
CSPT2CSRF from a same-origin write into a cross-origin one wherever the target
accepts cookie-borne credentials and permissive CORS. The gadget named is
Cloudflare's Image Transformation endpoint, which redirects to an arbitrary path
on another subdomain and is therefore available on a large share of the web
rather than only on a bespoke target. The accompanying constraint is precise and
reusable: browsers strip `Authorization` across a cross-origin redirect, so the
technique reaches cookie-authenticated targets and not bearer-token ones.

### Prior art

Doyensec's CSPT2CSRF (July 2024, in archive) established turning CSPT into a
state-changing request and framed the sink as same-origin. Renwa's CSPT roundup
(January 2025, in archive and cited in `2025.md`) already chains open redirects
with CSPT — but for *response* control, spoofing a JSON body to reach XSS, which
is the read direction. Matan Ber's encoding-levels work (2024, in archive) and
Nadir's account-takeover writeup (2023, in archive) cover reach and exploitation
depth rather than origin crossing. That 307/308 preserve method and body is
specified behaviour and long used in SSRF and CORS work.

### Candidate's distinct contribution

The method-and-body-preserving variant of redirect chaining, which changes what
CSPT can do rather than what it can read, plus the identification of a ubiquitous
third-party 307 gadget and the `Authorization`-header limit. This is a composition
of known parts; the score reflects that it is a real capability change on a narrow
base, not a new primitive.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 52 | 25% | 13.00 | Redirect chaining with CSPT was published nine months earlier; the method-preserving cross-origin variant is the increment. |
| Transferability | 65 | 20% | 13.00 | The gadget is third-party and widely deployed, so the pattern applies well beyond the reported target. |
| Lasting value | 56 | 20% | 11.20 | Likely to persist as a checklist item — "can this CSPT leave the origin?" — rather than to seed a research line. |
| Technical soundness | 70 | 15% | 10.50 | Mechanism, preconditions and the Authorization-header limit are stated correctly and consistently. |
| Practical usability | 68 | 10% | 6.80 | Directly actionable against real applications with no tooling required. |
| Clarity and reproducibility | 66 | 10% | 6.60 | Clear writeup, single target, no released playground or PoC repository. |

**Final score: 61.1/100.** Archive decision: include as a supporting reference.

### Reverification

- **Candidate facts rechecked against:** the post itself, and the archived copies of
  Doyensec's CSPT2CSRF, Renwa's CSPT roundup and Matan Ber's encoding-levels post.
- **Independent prior-art check:** searched by outcome ("cross-origin CSPT", "307
  gadget preserves body") rather than by name, and re-read Renwa's roundup for
  redirect usage. It uses open redirects throughout — but to control the *response*,
  never to move a state-changing request to another origin.
- **Strongest challenge to the result:** redirect-gadget chaining with CSPT was
  already in `2025.md` via Renwa, nine months earlier. If one treats "chain a
  redirect onto a CSPT" as the unit of contribution, this is a duplicate.
- **Benefit-of-doubt check:** read the other way, read and write are different
  capabilities: Renwa's chain spoofs data the page consumes, this one performs an
  authenticated write against an origin the page never intended to contact. The
  status-code choice is load-bearing, not incidental.
- **Changes after reverification:** Original contribution cut from 58 to 52 and the
  total from 64.8 to 61.1 after finding the Renwa overlap, and confidence set to
  Medium. It stays above the 60 gate, but marginally — a re-judge is reasonable if
  earlier method-preserving CSPT work surfaces.

### Verdict

Meaningful extension. What is new is that CSPT's blast radius is not bounded by the
origin when a method-preserving redirect is available, together with a named gadget
that makes the precondition common rather than exotic. What was already known is
CSPT itself, CSPT2CSRF, redirect chaining for response control, and 307/308
semantics.

- **Archive decision:** Include as a supporting reference
- **Confidence:** Medium
- **Evidence gaps:** No public record establishes whether anyone had previously
  documented CSPT crossing origins by 307; a negative search result is not proof.

## 54.2 — [CSS Data Exfiltration to Steal OAuth Token](https://blog.voorivex.team/css-data-exfiltration-to-steal-oauth-token) — Amirmohammad Safari & Yashar Shahinzadeh, Voorivex

**REMOVED** · Meaningful combination or adaptation · confidence High

### Candidate

Published 15 February 2025. Judged in the 10 August 2026 single-publisher sweep.

### Core contribution

A chain: DOMPurify's default configuration permits `<style>`, so HTML injection
that cannot reach script can still reach CSS; sequential import chaining leaks the
page character by character; and an OAuth flow that accepts an attacker-supplied
`redirect_uri` puts the token in a URL that a third-party ads script reflects into
a `src` attribute where the selectors can see it. The one piece of genuine
mechanism is a specificity fix: later-loaded import rounds lose to earlier rules,
so the authors nest `:is(div)` selectors in successive rounds to keep priority and
sustain multi-round extraction.

### Prior art

Dense, and the authors credit it themselves: Gareth Heyes on CSS exfiltration and
blind CSS exfiltration (2023, in archive), d0nut's sequential import chaining,
Securitum's single-injection-point Firefox work (2020, in archive), and Frans
Rosén's dirty-dancing OAuth (2022, in archive). Reflecting query parameters into a
`src` attribute is a known sink pattern.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 42 | 25% | 10.50 | Every component is cited prior art; the `:is()` specificity workaround is a small genuine addition. |
| Transferability | 55 | 20% | 11.00 | The specificity fix helps any multi-round import chain; the rest depends on a specific ads script and OAuth misconfiguration. |
| Lasting value | 48 | 20% | 9.60 | A useful worked chain, unlikely to redirect later research. |
| Technical soundness | 70 | 15% | 10.50 | The obstacle is diagnosed correctly and the fix is explained. |
| Practical usability | 58 | 10% | 5.80 | Reusable where the same preconditions line up. |
| Clarity and reproducibility | 68 | 10% | 6.80 | Clear narrative with payloads; no released tooling. |

**Final score: 54.2/100.** Archive decision: include as a supporting reference; below the 2025 list gate.

### Reverification

- **Candidate facts rechecked against:** the post, plus archived copies of the
  PortSwigger blind CSS exfiltration and Securitum posts.
- **Independent prior-art check:** searched by mechanism for CSS import chaining and
  specificity handling rather than by the OAuth outcome; found the chaining lineage
  well established and no earlier statement of the specificity problem in these terms.
- **Strongest challenge to the result:** the authors state plainly that this combines
  existing techniques, which argues for a lower Original score still.
- **Benefit-of-doubt check:** the specificity obstacle is real and would stop a
  reimplementation, so documenting it has value beyond the case study.
- **Changes after reverification:** None. The score is a fair reading of a
  well-executed chain built almost entirely from cited prior art.

### Verdict

Meaningful combination or adaptation. Below the 60 gate for the 2025 list.

- **Archive decision:** Include as a supporting reference
- **Confidence:** High
- **Evidence gaps:** None material.

## 53.0 — [DOM XSS to Account Takeover: not-so-dirty dancing in a GIS SDK](https://blog.voorivex.team/not-so-dirty-dancing-in-gis-sdk) — HamidSj, Voorivex

**REMOVED** · Useful application or case study · confidence High

### Candidate

Published 7 December 2025. Judged in the 10 August 2026 single-publisher sweep.

### Core contribution

Two layered controls create the gap that defeats them: a WAF blocks `javascript:`
and a replace function strips characters, so interleaving dots
(`ja.va.sc.ri.pt.:`) satisfies neither filter's assumptions. The XSS then drives
the Google Identity Services SDK with `auto_select: true` and a hooked
`window.open` injecting `prompt=none` and `authuser=0`, so authentication
completes with no user interaction; stealing the non-`HttpOnly` browser-identity
cookie alongside the JWT defeats the 2FA exemption that trusts that cookie.

### Prior art

The author credits Omid Rezaei's `prompt=none` OAuth work (2024, in `2024.md`).
Silent re-authentication via `prompt=none` is specified OIDC behaviour that has
been abused since the dirty-dancing lineage (2022, in archive). Filter-stripping
bypasses that exploit a sanitiser's own rewriting are long established. The
transferable observation — that a "remember this device" cookie readable by script
is a second factor in name only — is real but not new.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 45 | 25% | 11.25 | Applies the team's own prior `prompt=none` technique to a specific SDK's auto-select feature. |
| Transferability | 50 | 20% | 10.00 | The GIS auto-select angle applies wherever that SDK is embedded; the filter bypass is target-specific. |
| Lasting value | 45 | 20% | 9.00 | Useful case study; unlikely to seed further work. |
| Technical soundness | 70 | 15% | 10.50 | The chain is coherent and each step is evidenced. |
| Practical usability | 55 | 10% | 5.50 | Reusable against other GIS integrations with the same settings. |
| Clarity and reproducibility | 68 | 10% | 6.80 | Well told, with the payloads shown. |

**Final score: 53.0/100.** Archive decision: include as a supporting reference; below the 2025 list gate.

### Reverification

- **Candidate facts rechecked against:** the post and the cited 2024 OAuth entry
  already listed in `2024.md`.
- **Independent prior-art check:** searched by the silent-authentication mechanism
  (`prompt=none`, `auto_select`) rather than by the XSS, confirming it as
  specified behaviour with an established abuse history.
- **Strongest challenge to the result:** the chain leans on the same team's earlier
  published technique, so the marginal contribution is the SDK-specific packaging.
- **Benefit-of-doubt check:** the script-readable device cookie as a 2FA bypass is a
  design lesson that generalises past this target.
- **Changes after reverification:** None.

### Verdict

Useful application or case study. Below the 60 gate for the 2025 list.

- **Archive decision:** Include as a supporting reference
- **Confidence:** High
- **Evidence gaps:** None material.

## 50.6 — [Puny-Code, 0-Click Account Takeover](https://blog.voorivex.team/puny-code-0-click-account-takeover) — Yashar Shahinzadeh & Amirmohammad Safari, Voorivex

**REMOVED** · Independent rediscovery · confidence High

### Candidate

Published 1 June 2025, presented at NahamCon 2025. Judged in the 10 August 2026
single-publisher sweep.

### Core contribution

A lookup-versus-delivery split: MySQL's default collation treats certain Unicode
characters as equal to their ASCII counterparts, so a puny-coded variant of a
victim's address matches the victim's row, while SMTP treats the same string as a
distinct mailbox and delivers the reset token to the attacker. The reusable rule is
that a password reset must send to the address the *database* holds, never to the
one the request supplied. The authors extend the same idea to OAuth provider email
callbacks and redirect URLs.

### Prior art

Substantial and acknowledged — the authors write that it "had been discovered
before us; we just put it into action." ReCollapse (2022, in archive) is the
canonical statement of normalisation producing a value that still matches;
HostSplit's Unicode-normalisation anti-patterns (2019, in archive) and Gareth
Heyes's Splitting the Email Atom (2024, in archive) cover email parser divergence
in depth. Unicode-collation account confusion has been reported publicly since the
late 2010s.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 34 | 25% | 8.50 | Self-described as prior discovery applied at scale rather than a new finding. |
| Transferability | 55 | 20% | 11.00 | The lookup-versus-delivery rule applies to any stack with a collating store and a byte-exact mailer. |
| Lasting value | 45 | 20% | 9.00 | A durable testing habit, already documented elsewhere. |
| Technical soundness | 66 | 15% | 9.90 | Mechanism correct; the breadth claim rests on unverifiable bounty reports. |
| Practical usability | 60 | 10% | 6.00 | Immediately testable on any reset flow. |
| Clarity and reproducibility | 62 | 10% | 6.20 | Clear, though specific collations and payloads are lightly covered. |

**Final score: 50.6/100.** Archive decision: include as a supporting reference; below the 2025 list gate.

### Reverification

- **Candidate facts rechecked against:** the post, plus archived ReCollapse and
  HostSplit references for the normalisation lineage.
- **Independent prior-art check:** searched by precondition (collation equality in
  the store, byte-exact delivery in the mailer) rather than by "punycode", which
  surfaces the same class under normalisation and homograph names going back years.
- **Strongest challenge to the result:** the authors concede prior discovery, which
  makes *Duplicate* arguable; the score is kept above 50 because the demonstrated
  extension to OAuth email callbacks is more than a restatement.
- **Benefit-of-doubt check:** independent arrival is credited, and breadth of
  affected programs is real evidence that the class was under-tested.
- **Changes after reverification:** None. Verdict set to Independent rediscovery
  rather than Duplicate on the strength of the OAuth-callback extension.

### Verdict

Independent rediscovery. Below the 60 gate for the 2025 list.

- **Archive decision:** Include as a supporting reference
- **Confidence:** High
- **Evidence gaps:** No first-publication date is offered for the earlier discovery
  the authors refer to.

## 50.5 — [Stealing oAuth Token via Referrer Policy Override](https://blog.voorivex.team/leaking-oauth-token-via-referrer-leakage) — Omid Rezaei, Voorivex

**REMOVED** · Meaningful combination or adaptation · confidence High

### Candidate

Published 6 May 2025. Judged in the 10 August 2026 single-publisher sweep.

### Core contribution

Chrome applies the referrer policy carried by a `Link` header to sub-resource
preload requests, so a page that can only inject an `<img>` — everything else
sanitised away — can still force `unsafe-url` and leak a full referrer containing
an OAuth authorization code to an attacker endpoint. Combined with a
`redirect_uri` that lands the victim on the injectable path, that is account
takeover from a markup-only injection.

### Prior art

The browser behaviour is not the author's: the post credits `@slonser_`'s
disclosure of Chrome's `Link`-header handling (May 2025) and calls it a Chrome
0-day rather than claiming it. Referrer leakage of OAuth codes and the
dirty-dancing family of redirect-chain attacks are established (2022, in archive).

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 36 | 25% | 9.00 | The load-bearing browser primitive is explicitly credited to another researcher. |
| Transferability | 52 | 20% | 10.40 | The combination applies wherever limited HTML injection meets a redirect-controlled flow. |
| Lasting value | 44 | 20% | 8.80 | Tied to a browser behaviour that was expected to be fixed. |
| Technical soundness | 68 | 15% | 10.20 | The chain is coherent and the browser dependency stated. |
| Practical usability | 55 | 10% | 5.50 | Usable while the behaviour persists. |
| Clarity and reproducibility | 66 | 10% | 6.60 | Clear, with the attribution made explicit. |

**Final score: 50.5/100.** Archive decision: include as a supporting reference; below the 2025 list gate.

### Reverification

- **Candidate facts rechecked against:** the post and its attribution link.
- **Independent prior-art check:** searched by the observable outcome (full referrer
  from a preload despite a restrictive policy) rather than by `Link` header, which
  confirms the primitive belongs to the credited disclosure.
- **Strongest challenge to the result:** with the primitive credited elsewhere, the
  contribution is the OAuth application, which is a familiar shape.
- **Benefit-of-doubt check:** turning an `<img>`-only injection into token theft is a
  real escalation and the attribution is handled honestly.
- **Changes after reverification:** None. Attribution recorded separately, per the
  rule that first publication and application are credited apart.

### Verdict

Meaningful combination or adaptation. Below the 60 gate for the 2025 list; the
browser primitive is credited to `@slonser_`.

- **Archive decision:** Include as a supporting reference
- **Confidence:** High
- **Evidence gaps:** None material.

## 45.0 — [Hacking Veeam: Several CVEs and $30k Bounties](https://blog.voorivex.team/hacking-veeam-several-cves-and-30k-bounties) — Yashar Shahinzadeh, Voorivex

**REMOVED** · Useful application or case study · confidence High

### Candidate

Published 9 August 2025, but every finding carries a 2024 CVE
(CVE-2024-29849, -42024, -29850, -29853, -29852) and was fixed in 2024, so the
research window is 2024 and only the writeup is 2025. Judged in the 10 August 2026
single-publisher sweep and recorded here because that is where the writeup falls.

### Core contribution

Five findings in Veeam products reached by decompiling .NET assemblies: a SAML
validation branch that hands out a session cookie for an arbitrary username, a
deserialization allowlist bypassed by keeping a valid `assemblyName` while
changing `typeName`, an NTLM relay enabled by missing Extended Protection, a DLL
path built from user-controlled arguments, and a set of missing authorization
checks. The one broadly reusable note is the allowlist bypass shape: a check that
validates one half of a type reference while the other half decides what is
constructed.

### Prior art

Each class is long established — SAML validation bypasses, .NET deserialization
allowlist bypasses via partial type matching, NTLM relay (the post cites Compass
Security's writeup and impacket), path traversal into DLL loading, and IDORs. The
work is competent enterprise vulnerability research rather than a contribution to
web technique.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 30 | 25% | 7.50 | Known classes located in one product; the type-name allowlist bypass is the only reusable twist. |
| Transferability | 42 | 20% | 8.40 | The allowlist-bypass shape generalises; the rest is product-specific. |
| Lasting value | 35 | 20% | 7.00 | Unlikely to influence later research. |
| Technical soundness | 72 | 15% | 10.80 | Decompiled evidence, CVEs and vendor fixes support each finding. |
| Practical usability | 48 | 10% | 4.80 | Useful to .NET auditors, little beyond. |
| Clarity and reproducibility | 65 | 10% | 6.50 | Clear per-bug walkthroughs with code excerpts. |

**Final score: 45.0/100.** Archive decision: do not include.

### Reverification

- **Candidate facts rechecked against:** the post and the CVE identifiers it cites.
- **Independent prior-art check:** searched by the deserialization allowlist-bypass
  mechanism rather than by product, confirming partial-type-match bypasses as an
  established .NET technique.
- **Strongest challenge to the result:** five CVEs and $30,000 argue for impact — but
  impact is explicitly not scored, and none of the five introduce a primitive.
- **Benefit-of-doubt check:** the "web skills transfer to thick-client appsec"
  methodology point is genuine and honestly made.
- **Changes after reverification:** None. Also flagged: the findings belong to the
  2024 disclosure window, so this would not be a 2025 candidate at any score.

### Verdict

Useful application or case study.

- **Archive decision:** Do not include
- **Confidence:** High
- **Evidence gaps:** None material.

## 63.0 — [More Than DoS: Progress Telerik UI for ASP.NET AJAX Unsafe Reflection (CVE-2025-3600)](https://labs.watchtowr.com/more-than-dos-progress-telerik-ui-for-asp-net-ajax-unsafe-reflection-cve-2025-3600/) — Piotr Bazydlo, watchTowr

**REMOVED** · Useful application or case study · confidence High

### Candidate

Published 10 October 2025; disclosed to Progress in April 2025. Judged in the
2026-08-12 pass over the ysonet .NET-deserialization reference set.

### Core contribution

Shows that a Telerik UI issue published as a denial of service is in fact unsafe
reflection whose reachable property setters can produce remote code execution
depending on what else is loaded in the target process, and makes the library
argument: a flaw in a component shipped inside thousands of products outlives
and outreaches a flaw in any one product, because nobody patches the component.

### Prior art

The unsafe-reflection-to-RCE mechanism in this exact library is the
CVE-2019-18935 lineage already on the 2019 list, and setter-driven gadget reach
is established from 2017 onward. The severity-reassessment observation — that a
vendor-assigned DoS can hide an RCE — is a good testing habit rather than a new
primitive.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 46 | 25% | 11.50 | A new CVE in a known sink class; the reflection-to-setter-to-RCE mechanism is prior work. |
| Transferability | 60 | 20% | 12.00 | The "re-examine DoS-classified reflection bugs" heuristic and the library-versus-product argument generalise. |
| Lasting value | 55 | 20% | 11.00 | Consequential while the library remains unpatched in the field; not a lasting model change. |
| Technical soundness | 85 | 15% | 12.75 | Reachability is demonstrated, including a chained pre-auth RCE against a real CMS. |
| Practical usability | 74 | 10% | 7.40 | Directly usable against a very large installed base. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Detailed and specific about preconditions and environment dependence. |

**Final score: 63.0/100.** Archive decision: do not include.

### Verdict

Useful application or case study. High impact on a widely deployed library, but
the underlying primitive is already represented and the contribution is a new
instance of it.

### Reverification

- **Candidate facts rechecked against:** the archived post, which carries the
  10 October 2025 date, the author and the CVE.
- **Independent prior-art check:** compared against the CVE-2019-18935 Telerik
  entry on the 2019 list and against 2017 setter-gadget work.
- **Strongest challenge to the result:** ~185,000 exposed hosts is a large
  practical result.
- **Benefit-of-doubt check:** exposure counts are explicitly excluded from
  novelty by the neutrality rules; the transferable heuristic is credited in the
  transferability score.
- **Changes after reverification:** none.

## 62.7 — [Bypassing Authentication Like It's The '90s: Pre-Auth RCE Chain(s) in Kentico Xperience CMS](https://labs.watchtowr.com/bypassing-authentication-like-its-the-90s-pre-auth-rce-chain-s-in-kentico-xperience-cms/) — Piotr Bazydlo, watchTowr

**REMOVED** · Useful application or case study · confidence Medium

### Candidate

Published 17 March 2025; WT-2025-0006, WT-2025-0007 and WT-2025-0011, tracked as
CVE-2025-2746 and CVE-2025-2747. Judged in the 2026-08-12 pass over the ysonet
.NET-deserialization reference set.

### Core contribution

The staging web service authenticates with a WS-Security UsernameToken through
the obsolete WSE3 library. Kentico's token manager returns an empty string when
the supplied username is unknown, and WSE3 lets the request itself choose how
the password is verified by setting the Password Type attribute. Switching from
PasswordText to PasswordDigest sidesteps the empty-password rejection, because a
digest over an empty secret is computable, and authentication passes. A second
variant uses the SendNone option, which performs no verification at all. Behind
that door sits a SoapFormatter deserialization sink.

### Prior art

The shape is not new. Apache CXF's CVE-2012-0803 is the same failure —
UsernameToken policy not enforced, so the client selects a weaker or absent
password mode — with CVE-2013-0239 in the same family. The general lesson that a
WS-Security implementation must not let the message pick its own verification
mode has been public since 2012. What is new here is the WSE3 and Kentico
incarnation, including the empty-string sentinel that makes the digest
computable.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 48 | 25% | 12.00 | An independent instance of a WS-Security UsernameToken failure class public since 2012, in a different stack. |
| Transferability | 58 | 20% | 11.60 | Worth testing against any WSE3 or WS-Security endpoint, though the exact sentinel is Kentico's. |
| Lasting value | 52 | 20% | 10.40 | Reinforces an existing lesson about attacker-selected verification modes. |
| Technical soundness | 86 | 15% | 12.90 | Every step is traced through decompiled framework and product code with working requests. |
| Practical usability | 72 | 10% | 7.20 | Immediately usable where the staging service is enabled with password authentication. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Complete requests, code and configuration preconditions. |

**Final score: 62.7/100.** Archive decision: do not include.

### Verdict

Useful application or case study. Excellent product research, but the
attacker-chooses-the-verification-mode weakness in WS-Security UsernameToken was
public prior art, so this is a rediscovery in a new stack rather than a new
technique.

### Reverification

- **Candidate facts rechecked against:** the archived post, which carries the
  17 March 2025 date, the author and the WT identifiers.
- **Independent prior-art check:** searched the WS-Security UsernameToken
  mechanism rather than the product name, which surfaced Apache CXF
  CVE-2012-0803 and CVE-2013-0239 as the same class from 2012 to 2013.
- **Strongest challenge to the result:** the empty-string-sentinel plus
  digest-mode combination is a specific insight the CXF cases do not contain.
- **Benefit-of-doubt check:** that combination is why originality is scored at 48
  rather than in the thirties; it is not enough to make the class new.
- **Changes after reverification:** original contribution was cut from a draft 66
  to 48 after the CXF prior art surfaced; the final score fell from 67.2 to 62.7,
  and the verdict changed from meaningful combination to useful application.

## 61.5 — [Cache Me If You Can: Sitecore Experience Platform Cache Poisoning to RCE](https://labs.watchtowr.com/cache-me-if-you-can-sitecore-experience-platform-cache-poisoning-to-rce/) — Piotr Bazydlo, watchTowr

**REMOVED** · Useful application or case study · confidence High

### Candidate

Published 29 August 2025; part two of the team's Sitecore research, covering
CVE-2025-53693, CVE-2025-53691 and CVE-2025-53694. Judged in the 2026-08-12 pass
over the ysonet .NET-deserialization reference set.

### Core contribution

Chains a pre-auth HTML cache poisoning primitive, reached through unsafe
reflection in a XAML page handler that is exposed without authentication, with a
post-auth insecure deserialization sink, so a fully patched instance can be
compromised without credentials. The reusable observation is that an internal
server-side render cache is an attack surface in its own right: poison it
pre-auth and an authenticated user executes the result.

### Prior art

Web cache poisoning is a 2018 Top 10 technique and has been extended repeatedly
on later lists; unsafe reflection and .NET deserialization sinks are long
established. Applying cache poisoning to a CMS-internal render cache rather than
an HTTP cache is a good re-targeting, but the chain is assembled from primitives
that are all already represented.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 50 | 25% | 12.50 | Re-targets cache poisoning at an internal render cache; each constituent primitive is prior work. |
| Transferability | 55 | 20% | 11.00 | The internal-cache-as-surface idea travels; the specific handler and sinks do not. |
| Lasting value | 50 | 20% | 10.00 | A strong worked example rather than a change in how the class is understood. |
| Technical soundness | 84 | 15% | 12.60 | Handler resolution and the full chain are traced through product code with vendor patches. |
| Practical usability | 70 | 10% | 7.00 | Usable against a specific product and version range. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Detailed, with the chain and its preconditions set out in order. |

**Final score: 61.5/100.** Archive decision: do not include.

### Verdict

Useful application or case study. Clears the numeric gate on execution quality,
but a product-specific chain of already-represented primitives is not a missed
technique.

### Reverification

- **Candidate facts rechecked against:** the archived post, which carries the
  29 August 2025 date, the author and the three CVEs.
- **Independent prior-art check:** checked the cache-poisoning lineage across the
  2018 to 2022 lists and searched for earlier server-side render-cache poisoning.
- **Strongest challenge to the result:** poisoning an application-internal cache
  to cross a privilege boundary is a distinct enough framing to argue for it.
- **Benefit-of-doubt check:** that framing is credited in the transferability
  score; it is one worked instance, not a demonstrated general method.
- **Changes after reverification:** none.

## 56.1 — [By Executive Order, We Are Banning Blacklists: Domain-Level RCE in Veeam Backup and Replication (CVE-2025-23120)](https://labs.watchtowr.com/by-executive-order-we-are-banning-blacklists-domain-level-rce-in-veeam-backup-replication-cve-2025-23120/) — Piotr Bazydlo, watchTowr

**REMOVED** · Useful application or case study · confidence High

### Candidate

Published 20 March 2025. Judged in the 2026-08-12 pass over the ysonet
.NET-deserialization reference set.

### Core contribution

Veeam patched earlier deserialization bugs by adding a blocklist of forbidden
classes; the post finds product-internal classes that are not on it and reaches
domain-level RCE again. The argument is that blocklist-based deserialization
defence fails because a product's own codebase and its third-party libraries
supply gadgets the vendor never enumerated.

### Prior art

The author says so himself in the post: his own Hexacon 2023 whitepaper
"Exploiting Hardened .NET Deserialization" — which is the number two entry on
the 2023 list — is the general result, and this is a further instance of it.
Frycos and Code White's earlier Veeam work (CVE-2024-40711) is the immediate
predecessor on the same product.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 38 | 25% | 9.50 | A further instance of the author's own already-nominated 2023 result. |
| Transferability | 48 | 20% | 9.60 | The blocklist critique is general but already established by the 2023 entry. |
| Lasting value | 45 | 20% | 9.00 | Evidence that vendors have not learned, rather than new knowledge. |
| Technical soundness | 84 | 15% | 12.60 | Gadget discovery and the chain are demonstrated concretely against the patched product. |
| Practical usability | 70 | 10% | 7.00 | Usable against the affected versions. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Clear and well evidenced. |

**Final score: 56.1/100.** Archive decision: do not include.

### Verdict

Useful application or case study. The general lesson is already the 2023 list's
number two entry, by the same author.

### Reverification

- **Candidate facts rechecked against:** the archived post, which carries the
  20 March 2025 date and the author's own citation of his Hexacon whitepaper.
- **Independent prior-art check:** confirmed "Exploiting Hardened .NET
  Deserialization" is nominated at number two on 2023.md.
- **Strongest challenge to the result:** finding fresh product-internal gadgets
  after a vendor blocklist is real work.
- **Benefit-of-doubt check:** it is scored as a case study rather than a
  duplicate, which is why it lands in the mid-fifties.
- **Changes after reverification:** none.

## 68.8 — [8 Million Requests Later, We Made The SolarWinds Supply Chain Attack Look Amateur](https://labs.watchtowr.com/8-million-requests-later-we-made-the-solarwinds-supply-chain-attack-look-amateur/) — Benjamin Harris, Aliz Hammond and Pinaki Mondal, watchTowr

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Benjamin Harris, Aliz Hammond and Pinaki Mondal, watchTowr Labs, 4 February 2025.
Found by the 2026-08-12 publisher sweep.

### Core contribution

A method for measuring how long abandoned infrastructure keeps being trusted, and
the finding that the answer is years. The researchers re-registered roughly 150
abandoned S3 buckets previously used by governments, militaries, Fortune 500
companies, security vendors and open-source projects, then logged - and only
logged - what arrived. Over two months the buckets received more than eight
million HTTP requests, and the request types are the point: software updates,
precompiled binaries for three operating systems, virtual machine images,
JavaScript files, CloudFormation templates and SSLVPN configuration. One bucket
had been removed from a project's documentation in 2015 and was still being
fetched nine years later.

The transferable part is the method rather than the bucket: enumerate a global
namespace for entries an owner has released, reclaim them, and measure the
residual trust. It applies to package names, container tags, storage namespaces
and domains alike.

### Prior art

S3 bucket squatting and dangling storage references were public well before this;
the post does not claim the primitive. Supply-chain compromise through update
channels is established by SolarWinds, XZ/liblzma, npm takeovers and HandBrake,
all of which the post cites as the comparison it is drawing. The gain is
empirical and structural: nobody had shown at this scale that a reclaimed bucket
is a live, unauthenticated code-delivery channel into named government and
enterprise networks, nor that the exposure persists for the better part of a
decade after the reference is removed from a repository.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 55 | 25% | 13.75 | The squatting primitive is old; what is new is the measurement design and the demonstration that abandoned buckets remain trusted update channels for years. |
| Transferability | 70 | 20% | 14.00 | The reclaim-and-measure method generalises to any global namespace with reusable names. |
| Lasting value | 72 | 20% | 14.40 | Changed how abandoned cloud storage is treated in supply-chain threat models and prompted provider-side change. |
| Technical soundness | 80 | 15% | 12.00 | Real, quantified observation over two months with named request classes, and an ethically bounded design that served nothing. |
| Practical usability | 62 | 10% | 6.20 | Reproducible in principle, but opportunistic and narrowed by subsequent provider changes to name reuse. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Specific about scale, sources and method, with the restraint stated plainly. |

**Final score: 68.8/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. The primitive was known; the reclaim-and-
measure methodology and the scale of residual trust it exposed are the
contribution, and both remain usable.

### Reverification

- **Candidate facts rechecked against:** the post, which carries the 4 February
  2025 date, all three authors, the bucket count, the two-month window and the
  eight-million-request figure.
- **Independent prior-art check:** searched for earlier abandoned-S3-bucket
  takeover and for supply-chain measurement studies of dangling storage, and read
  the same team's 2024 .MOBI work to separate the two contributions. The earlier
  work is a different namespace and a different consumer.
- **Strongest challenge to the result:** breadth of a known bug is coverage, not
  discovery, and the neutrality rules say so explicitly - this could be scored as
  a case study in the fifties.
- **Benefit-of-doubt check:** the measurement is the artifact, not the bug count;
  originality is held at 55 to reflect the borrowed primitive while the method is
  credited under transferability and lasting value.
- **Changes after reverification:** none.
## 72.8 — [New Method to Leverage Unsafe Reflection and Deserialisation to RCE on Rails](https://www.elttam.com/blog/rails-sqlite-gadget-rce) — Alex Brown, elttam

**KEPT** · Meaningful combination or adaptation · confidence Medium

### Candidate

Published 4 March 2025. Restores remote code execution on Rails after the
long-used `Logger`/`Kernel#open` route was closed.

### Core contribution

A gadget that abuses SQLite's supported extension-loading: instantiating
`SQLite3::Database` with an `extensions` argument loads an attacker-supplied
compiled library. Reached through
`ActiveRecord::ConnectionAdapters::SQLite3Adapter` and chained from the 2013
`DeprecatedInstanceVariableProxy` gadget, it needs only gems Rails ships by
default. Uploaded temporary files are addressed through `/proc/self/fd/x`,
avoiding any need for a known path.

### Prior art

Rails deserialization chains date to 2013, and the `Kernel#open` pipe trick was
the standard sink until it was replaced with `File.open` in 2017. Using a
library's legitimate, still-supported extension mechanism as the execution sink
is the new element, and it is not patchable in the way the previous sink was.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 70 | 25% | 17.50 | New sink of a kind that cannot simply be removed, rather than a new payload. |
| Transferability | 68 | 20% | 13.60 | Rails-bounded, but relies only on default gems; the `/proc/self/fd` step generalises. |
| Lasting value | 68 | 20% | 13.60 | Extension loading is a documented feature, so the sink should persist. |
| Technical soundness | 82 | 15% | 12.30 | Full chain shown from entry gadget to loaded shared object. |
| Practical usability | 80 | 10% | 8.00 | Works against default installations without extra dependencies. |
| Clarity and reproducibility | 78 | 10% | 7.80 | Gadgets and preconditions are named; some setup is assumed. |

**Final score: 72.8/100.** Archive decision: include as a core technique.

### Verdict

Meaningful combination or adaptation. The chain is assembled from known parts,
but the execution sink is new and durable by design.

## 56.3 — [Gotchas in Email Parsing - Lessons From Jakarta Mail](https://www.elttam.com/blog/jakarta-mail-primitives) — Jia Hao Poh, elttam

**REMOVED** · Useful application or case study · confidence High

### Candidate

Full rejudgement on 9 September 2026 of the original 17 November 2025 article,
read in full live and in the intact local archive. The article expands the
author's BSides Canberra and Perth 2025 talks; the
[Canberra programme history](https://pretalx.com/bsides-canberra-2025/schedule/changelog/)
establishes the earlier presentation. All load-bearing prior art below predates
2025, so the precise talk cutoff does not affect the comparison. The score
replaces 60.1 on new evidence, not because the threshold changed. The old event
remains in `history.jsonl`.

### Core contribution

An audit catalogue maps Java mail constructors, encoded personal names, group
addresses and downstream Spring/Hibernate validation to application trust
decisions. `InternetAddress(String)` parses, whereas the personal-name overloads
assign the address directly. An application can validate one interpretation and
send to another, or display a decoded name as trusted identity. The article
adds concrete review prompts and linked Semgrep audit rules. It does not show
a distinct new exploit beyond these established parsing and display confusions;
several proposed consequences are explicitly hypothetical.

### Prior art

Local list/archive checks found the nominated 2024
[Splitting the email atom](https://portswigger.net/research/splitting-the-email-atom),
which turns parser disagreement and encoded email syntax into identity bypasses.
The article itself credits Nathan Davison's earlier
[AWS SES research](https://nathandavison.com/blog/exploiting-email-address-parsing-with-aws-ses):
the angle-address plus trailing address payload, privilege check, and different
delivery destination are the same security use, not merely shared old APIs.
An independent search for constructor validation found
[Commons Email EMAIL-49, 7 September 2005](https://issues.apache.org/jira/browse/email-49),
which explicitly compares the validating one-argument constructor with the
non-validating personal-name overloads and explains the required validation.
That issue alone is API background, not a prior security attack; combined with
the earlier demonstrated parser-to-identity attack, it removes the claimed
new capability. Mapping these behaviours to Jakarta and adding call-site audit
patterns is useful engineering, but no new search or exploit-generation method
is demonstrated.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 40 | 25% | 10.00 | Useful systematic audit mapping; the exploit and constructor distinction both predate the article. |
| Transferability | 55 | 20% | 11.00 | Applies across Jakarta Mail consumers, with Spring and Hibernate examples. |
| Lasting value | 55 | 20% | 11.00 | Concrete review checklist remains useful, but mainly repackages an established identity-parsing test. |
| Technical soundness | 72 | 15% | 10.80 | Source-level behaviours and payloads are shown; hypothetical chains and a reversed accessor claim limit confidence in the checklist. |
| Practical usability | 65 | 10% | 6.50 | Audit rules locate call sites, but do not establish attacker control or an exploitable identity decision. |
| Clarity and reproducibility | 70 | 10% | 7.00 | Clear code examples; the final checklist needs correction before direct use. |

**Final score: 56.3/100.** Computed with `score.py 40 55 55 72 65 70`.
Archive decision: exclude from the missed-technique list; nonqualifying verdict.

### Reverification

- Reopened the full article, its linked Semgrep rules and the two closest original
  attack accounts; separately searched pre-2025 constructor validation history.
- Checked the strongest tooling interpretation: the rules identify named API
  uses for manual review, without a new analysis or discovery algorithm. That
  helps usability but does not make every audit checklist a new methodology.
- The article's final checklist reverses `getSender()` and `getFrom()` return
  shapes. The published API has a single `Address` sender and `Address[]` from
  and reply-to values. This is an error in the original source, not a faulty
  archive capture. The earlier card also misstated the angle-address payload's
  naive split result; this card avoids that unsupported example.
- Benefit of doubt was given to the broader review mapping, not withheld because
  the components are old. No live exploit was run. Later adoption and fixes do
  not enter any category.

### Verdict

Useful application or case study. Remove the previously grandfathered entry
after mechanism-level review. A score over 55 does not satisfy the separate
novelty-verdict gate.

## 69.5 — [Network-Level Prompt and Trait Leakage in Local Research Agents](https://arxiv.org/abs/2508.20282v1) — Hyejun Jeong, Mohammadreza Teymoorianfard, Abhinav Kumar, Amir Houmansadr and Eugene Bagdasarian

**KEPT** · Meaningful extension · confidence Medium

### Candidate

Original arXiv v1, submitted 27 August 2025 at 21:24 UTC, verified against the
[version history](https://arxiv.org/abs/2508.20282). Read the complete
[v1 paper](https://arxiv.org/html/2508.20282v1), including appendices and inference
templates. The January 2026 revision and later USENIX appearance do not determine
eligibility or scores. This explicit six-category rejudgement replaces the
compact 68.0 assessment in the 2026 audit; its original arithmetic is unknown
and is not reconstructed. Absent from the 2025 original nominations.

### Core contribution

Local research agents amplify a private request into a dense sequence of visits
to semantically related web domains. A passive observer who sees those domains
can use a few labelled examples and an LLM to infer the originating task; repeated
sessions support trait inference. The added capability is reconstruction of
free-form agent intent from its browser actions, rather than a classifier for a
preselected website or search keyword. The observer needs domain visibility and
separable local sessions, but not page content, the user prompt or model access.

The original evaluates GPT Researcher, Browser Use and AutoGen traces; two agents
are instructed to visit at least five sites. Prompt evaluation uses TREC queries,
while traits use generated personas whose queries intentionally expose selected
traits. The reported 0.77 functional and 0.735 domain-equivalence results are
LLM-judged similarity dimensions, not percentages of exactly recovered prompts.
The 19-of-32 trait result likewise uses similarity thresholds on synthetic data.

### Prior art

Local backward searches found the already-listed 2019
[search-autocomplete keylogging attack](https://www.usenix.org/conference/usenixsecurity19/presentation/monaco),
which recovers typed search text from timing and protocol-dependent lengths.
[Oh, Li and Hopper's 2017 keyword fingerprinting](https://petsymposium.org/popets/2017/popets-2017-0048.php)
classifies monitored search keywords using Tor traffic features.
[Weiss, Ayzenshteyn and Mirsky, March 2024](https://arxiv.org/abs/2403.09751)
infer AI-assistant responses from streamed-token lengths. These establish that
encrypted traffic can disclose user intent; the 2025 contribution is the
agent-created sequence of domain semantics as an additional observation channel,
with open-ended inference and a multi-session extension. It is not the first
traffic inference or demographic profiling attack.

An independent web search for pre-cutoff research-agent domain privacy and
prompt inference did not locate the same demonstrated method. Later related
agent-query papers were excluded from all six scores. Comparison against 2025
prompt-injection nominations found a different trust boundary: passive exposure
through actions, rather than attacker instructions changing those actions.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 66 | 25% | 16.50 | Meaningful new observation and inference method within established traffic privacy attacks. |
| Transferability | 76 | 20% | 15.20 | Several browsing-agent architectures share task-driven domain expansion, subject to visibility. |
| Lasting value | 74 | 20% | 14.80 | Provides a reusable test for privacy leakage through delegated web actions and session composition. |
| Technical soundness | 64 | 15% | 9.60 | Ablations and multiple agents support the narrower leakage claim; synthetic traits and lenient model judging constrain recovery claims. |
| Practical usability | 60 | 10% | 6.00 | Domain-log inference is feasible, but encrypted DNS/ECH, tunnel placement and session mixing affect observation. |
| Clarity and reproducibility | 74 | 10% | 7.40 | Detailed datasets, settings and templates; no credit for code availability added after v1. |

**Final score: 69.5/100.** Computed with `score.py 66 76 74 64 60 74`.
Archive decision: include as a supporting reference in 2025.

### Reverification

- Rechecked arXiv chronology independently of the 2026 conference label and
  compared the original nomination set by mechanism as well as URL.
- Read the appendix scoring prompts: OBELS uses abstracted intent/source/entity
  matches and encourages partial agreement. It is not an independent execution
  test demonstrating that a recovered prompt completes the same task.
- The strongest objection is that domains have always revealed interests.
  The measured amplification through agent task decomposition and reusable
  inference experiment add enough beyond that observation for an extension,
  with originality below a new-class claim.
- Trait experiments are deliberately revealing synthetic personas; logged
  agent visits often stand in for network capture. A user's ISP cannot directly
  observe a remote hosted agent's browsing, so those traces do not establish that
  threat model. The 70–140-domain figure is not universal across agents.
- Full primary evidence supports a 2025 technique despite these limitations;
  no live interception was performed and no later replication was credited.

### Verdict

Meaningful extension. Add one grouped 2025 entry for v1 and its PDF. The older
2026 exclusion remains correct on year, while its historical omission is fixed.

## 56.8 — [RebirthDay Attack: Reviving DNS Cache Poisoning with the Birthday Paradox](https://doi.org/10.1145/3719027.3744832) — Xiang Li, Mingming Zhang, Zuyao Xu, Fasheng Miao, Yuqi Qiu, Baojun Liu, Jia Zhang, Xiaofeng Zheng, Haixin Duan, Zheli Liu, Yunhai Zhang and Dunqiu Fan

**REMOVED** · Useful application or case study · confidence High

### Candidate

Full original CCS 2025 paper, read in the intact archived author document.
The [author's publication page](https://zhangmm.net/publication/ccs25-rebirthday/)
labels it July 2025; the
[institution's September 2025 announcement](https://dissec.nankai.edu.cn/2025/0922/c34486a578225/page.htm)
and October 2025 proceedings independently establish the year. Exact earliest
public day is unresolved, so no 2025 prior work is used against it. The 2026
Black Hat presentation is a later presentation. This new full judgement replaces
the compact 76.8 claim preserved in the 2026 README; no original six-score table
exists to reconstruct. It was not nominated in 2025.

### Core contribution

Different ECS subnets separate otherwise identical in-flight DNS queries.
Accepting replies without ECS removes that distinction, so many outstanding
queries can match an attacker's forged response attempts. The paper implements
this birthday-poisoning attack against current resolvers and measures aggregation
and randomness weaknesses across software, routers and public services.
Its strongest remaining contribution is empirical validation and a reproducible
deployment-testing procedure, not the first description of the ECS mechanism.

The paper's 18-of-22 software headline combines six ECS-related implementations
with eleven lacking aggregation and one with weak randomness. Three controlled
poisoning demonstrations succeed, while Technitium yields denial of service
without establishing poisoning. Internet measurements test prerequisites rather
than actually poisoning the surveyed resolvers.

### Prior art

Local DNS-poisoning searches and the original paper's references led to
[CERT VU#457875, November 2002](https://www.kb.cert.org/vuls/id/457875):
concurrent same-record queries increase spoofed-answer collision probability.
More decisively, an independent pre-2025 ECS/birthday search found
[RFC 7871 §11.2, May 2016](https://www.rfc-editor.org/rfc/rfc7871#section-11.2).
It explicitly describes varying ECS to create concurrent same-name queries,
the need to match ECS response fields, and bypassing that match by flooding
responses with no ECS because compatibility rules accept their absence. This is
the exact relevant security use, not simply documentation of old components.
The paper cites RFC 7871 but does not identify a new step that escapes this
earlier threat description. Its current implementations and larger census do
not by themselves establish a new technique. Other port side-channel and
bailiwick attacks are less close prior art than this explicit ECS account.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 30 | 25% | 7.50 | Substantial empirical follow-through on an explicitly described attack, with no distinct new offensive mechanism established. |
| Transferability | 74 | 20% | 14.80 | ECS aggregation and response matching span independent resolver implementations. |
| Lasting value | 62 | 20% | 12.40 | Concrete deployment checks and experimental data give the older warning useful testing value. |
| Technical soundness | 66 | 15% | 9.90 | Packet model and controlled results are detailed; broad vulnerability totals are weaker than demonstrated exploitation. |
| Practical usability | 48 | 10% | 4.80 | Requires spoofing and favorable timing; experiments change resolver limits and delay legitimate replies. |
| Clarity and reproducibility | 74 | 10% | 7.40 | Packet layouts, settings and test procedure are provided, though the headline conflates different failure classes. |

**Final score: 56.8/100.** Computed with `score.py 30 74 62 66 48 74`.
Archive decision: exclude from the missed-technique list; nonqualifying verdict.

### Reverification

- Re-read RFC 7871 §11.2 separately from the paper's novelty claim. Its missing-ECS
  attack is explicit and public nine years before the candidate.
- Considered the strongest alternative, a tooling or methodology contribution.
  The measurement sends repeated queries to owned authoritative infrastructure
  and counts aggregation/forwarding outcomes. This is a useful application of
  the specified threat predicates, not a distinct demonstrated discovery method.
- Publication-time experiments impose 0.5–1-second legitimate-answer delays;
  Unbound's per-thread query limit is raised, and PowerDNS near-miss protection
  is disabled. Source spoofing, ECS configuration and DNSSEC/0x20 constraints
  remain. These settings limit practical claims but do not invalidate the
  controlled mechanism.
- The Internet census establishes vulnerable-looking prerequisites rather than
  successful attacks on 365,000 resolvers. CVE counts and later vendor response
  are not novelty or lasting-value evidence. No attack was run during this review.
- Benefit of doubt preserves strong cross-implementation and empirical value;
  it cannot convert an explicit prior attack into an original extension.

### Verdict

Useful application or case study. Remove the earlier compact-score addition.
The year is correctly 2025, but the exact attack predates it and the remaining
empirical contribution does not pass the qualifying novelty-verdict gate.

## 64.6 — [Bullseye: Detecting Prototype Pollution in NPM Packages with Proof of Concept Exploits](https://spectrum.library.concordia.ca/id/eprint/996198/) [Thesis](https://spectrum.library.concordia.ca/id/eprint/996198/2/Houis_MASc_F2025.pdf) — Tariq Houis; related conference paper with Shaoqi Jiang, Mohammad Mannan and Amr Youssef

**KEPT** · Tooling or methodology contribution · confidence Medium

### Candidate

- **Title:** Detecting Prototype Pollution in NPM Packages with Proof of Concept Exploits (Bullseye)
- **Author:** Tariq Houis, Concordia University; the related NDSS paper credits Tariq Houis, Shaoqi Jiang, Mohammad Mannan and Amr Youssef.
- **Publication date / novelty cutoff:** 4 November 2025, 16:48, verified repository deposit and unchanged modification timestamp. The cover's May 2025 and catalogue's 13 August thesis dates do not establish public availability.
- **Reference:** [Full thesis](https://spectrum.library.concordia.ca/id/eprint/996198/2/Houis_MASc_F2025.pdf); [deposit record](https://spectrum.library.concordia.ca/id/eprint/996198/).

Fresh full review on 9 September 2026, replacing the 57.8 compact assessment that incorrectly treated the conference appearance as a 2026 contribution. Checked the 2025 curated nominations and original PortSwigger nomination page for title, authors and mechanism overlap; this tool is absent.

### Core Contribution

Combine package-specific valid arguments extracted from developer tests with typed attack fragments, enumerate less obvious exported entry points, and validate each attempt through recursive and differential prototype observations. This creates a practical discovery method for previously unknown pollution sources, including functions that need a valid options argument alongside the attack input. It does not establish application-level attacker reachability or downstream RCE. The full thesis already includes the dual oracles, proxy-based sink locator, ablations and the same package study as the later conference paper.

### Prior Art

- [Arteau's NorthSec 2018 release](https://github.com/HoLyVieR/prototype-pollution-nsec18) supplies the underlying dynamic reflection/fixed-exploit approach. The local 2018 archive and original release were checked. Bullseye explicitly inherits these inputs rather than introducing prototype pollution.
- [JSGo, CCS 2024](https://netsec.ccert.edu.cn/files/papers/ccs24-testsuite.pdf), especially sections 3–4, already converts test-suite knowledge into vulnerability-triggering inputs, including prototype pollution. It uses trace alignment to construct HTTP requests for a known target location. Bullseye instead discovers sources across package entry points through simpler typed argument combinations.
- [PoCGen v1](https://arxiv.org/html/2506.04962v1) ([5 June 2025 submission record](https://arxiv.org/abs/2506.04962v1)) already dynamically enumerates package exports, statically extracts test usage snippets, combines them with exploit examples, and validates prototype pollution at runtime. It starts from a vulnerability report and uses iterative LLM generation, whereas Bullseye is a deterministic discovery pipeline without a known vulnerability report.
- The incremental contribution is the integrated source-discovery method and its demonstrated complementary coverage. Testsuite guidance or automatic PoC generation alone cannot be claimed as new. Only the 2025 thesis and pre-cutoff sources affect these scores; the 2026 paper is used to verify duplication, not to supply later benefits.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 52/100 | 25% | 13.00/25 | Known testing ideas are combined into a distinct discovery pipeline with improved entry coverage and richer pollution observations. |
| Transferability | 71/100 | 20% | 14.20/20 | Package tests can supply otherwise missing argument constraints across JavaScript libraries; the method remains language and oracle dependent. |
| Lasting value | 70/100 | 20% | 14.00/20 | Combining valid usage with attack fragments and measuring observation blind spots provides durable testing guidance. |
| Technical soundness | 66/100 | 15% | 9.90/15 | Baselines and ablations support the incremental method, with denominator inconsistencies and disputed reachability classifications limiting broad claims. |
| Practical usability | 61/100 | 10% | 6.10/10 | Detailed construction is usable by researchers; the cutoff document promises a future code release and cannot show real application exploitability. |
| Clarity and reproducibility | 74/100 | 10% | 7.40/10 | Full algorithms, seed tables, timings, experimental settings and limitations allow substantial reconstruction without counting later artifacts. |

**Final score: 64.6/100.** Computed with `score.py 52 71 70 66 61 74`.

### Reverification

Read the complete 72-page original thesis, including references and appendices, then reopened the deposit metadata and compared the conference paper's contribution, algorithms, experiment sizes and appendices. A second prior-art search for test-guided exploit generation found PoCGen's June 2025 version, which materially narrows the novelty beyond the thesis's own related-work discussion. JSGo's original methodological sections were also reopened. Both are pre-cutoff original sources.

The strongest objection is that existing test-guided validation already provides the general idea. The favorable, supported reading is a complementary discovery design, with ablations attributing gains to input pairing and richer observations; this justifies a methodology verdict rather than an original attack label. The 0.51-second headline is amortized parallel throughput, excluding download and installation, while individual packages average 32.38 seconds. “No false positives” concerns observed pollution under package-level input control, not confirmed remote attack paths. The thesis reports 807 entry points in its main result but 818 in ablations, and sometimes labels baseline-only results unknown rather than proved false positives. Its exclusion of `constructor.prototype` assumes equivalence that need not hold when filters distinguish keys. Its 100-ms timeout and partial AST handling can miss valid cases. These are publication-time limitations. No tool was executed, and no later CVEs, patches, adoption or code release increased any score.

### Verdict

**Tooling or methodology contribution; include as a supporting reference in 2025.** The combined discovery workflow clears 55 and is distinct from report-driven PoC synthesis and known-sink HTTP validation. It is excluded from the 2026 display because the full contribution was public in 2025. Confidence is medium: first public code availability and any earlier full disclosure remain uncertain, and the original artifact was promised rather than verified at the cutoff.

---

## 69.1 — [TranSPArent: Taint-style Vulnerability Detection in Generic Single Page Applications through Automated Framework Abstraction](https://zenodo.org/records/17822391) [Source code](https://github.com/diwangs/transparent-ae/tree/v1.0.0) — Senapati Diwangkara and Yinzhi Cao

**KEPT** · Tooling or methodology contribution · confidence Medium

### Candidate

- **Title:** TranSPArent: Taint-style Vulnerability Detection in Generic Single Page Applications through Automated Framework Abstraction
- **Author or organisation:** Senapati Diwangkara and Yinzhi Cao
- **Publication date / novelty cutoff:** 4 December 2025: public Zenodo v1.0.0 artifact, created the same day. The NDSS conference publication is February 2026 and is not the original technique year.
- **Reference:** [TranSPArent: Taint-style Vulnerability Detection in Generic Single Page Applications through Automated Framework Abstraction](https://www.ndss-symposium.org/wp-content/uploads/2026-f1721-paper.pdf)

Fresh full evaluation on 9 September 2026 under the publication-time rubric; supersedes the compact 59.6-point record. The old total is preserved in history, not reverse-engineered into category scores.

### Core Contribution

Automates framework-specific taint-sink models by working backward from dangerous DOM operations through SPA runtimes. Framework tests supply dynamic stack traces to repair missing static call edges; value/key analysis identifies exposed JavaScript parameters; transpiler test pairs recover the corresponding HTML/JSX/template attributes. These generated abstractions feed ordinary application taint analysis. The public 2025 artifact already implements the central combination; the later paper explains the same method.

### Prior Art

- **First public evidence:** [Zenodo v1.0.0, 4 December 2025](https://zenodo.org/records/17822391), links an immutable [GitHub v1.0.0 tree](https://github.com/diwangs/transparent-ae/tree/v1.0.0). The full release README, autostitch implementation, template-mapping implementations and evaluation driver were read. This is working technical source, not an empty repository or acceptance notice.
- **Local and closest prior:** [ReactAppScan, CCS October 2024](https://yinzhicao.org/reactappscan/reactappscan.pdf), also preserved locally, models React lifecycles and cross-component data flow but uses a curated sink list (§5/Table 2). It already covers JSX attributes, refs and DOM writes: those underlying exploits are not new.
- **Earlier analysis foundations:** [Madsen, Livshits and Fanning, Microsoft technical report, November 2012](https://www.microsoft.com/en-us/research/publication/practical-static-analysis-of-javascript-applications-in-the-presence-of-frameworks-and-libraries/) combines use and pointer analysis to avoid handwritten library stubs. [Chakraborty et al., ECOOP 2022](https://manu.sridharan.net/files/ECOOP22-RootCause.pdf), public preprint 13 May 2022, compares dynamic and static flows to diagnose missing JavaScript call edges. This precedes the use of runtime evidence to improve framework analysis.
- **Distinct increment:** Amortized sink abstraction across multiple SPA runtimes and template syntaxes, rather than a new XSS primitive or the first hybrid JavaScript analysis. The 2026 paper was read in full to verify mechanism identity; later conference recognition, patch outcomes and unsupported later additions do not increase any score.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 58/100 | 25% | 14.50/25 | A meaningful automation combination beyond curated React sinks and earlier dynamic/static graph comparison; the constituent analyses and underlying DOM exploits are established. |
| Transferability | 75/100 | 20% | 15.00/20 | The abstraction applies to Vue, React and Angular, with reusable separation between framework and application; typed sources and runnable framework tests remain prerequisites. |
| Lasting value | 76/100 | 20% | 15.20/20 | Learning sink models from runtime/compiler tests can reduce recurring model maintenance and support future framework versions without relying on a particular vulnerability remaining open. |
| Technical soundness | 68/100 | 15% | 10.20/15 | Historical implementation supplies concrete stitching and mapping logic plus evaluation drivers, with explicit framework-specific heuristics; it is not a soundness proof or independently rerun result. |
| Practical usability | 69/100 | 10% | 6.90/10 | Versioned code, datasets and installation workflow support reuse, though Nix, Git LFS, CodeQL and framework-specific setup impose material cost. |
| Clarity and reproducibility | 73/100 | 10% | 7.30/10 | The immutable README, implementation and test fixtures expose the process clearly; the later paper clarifies the same process, but its reported aggregate results are not treated as independently verified. |

**Final score: 69.1/100.** Calculated with `score.py`; all six scores use evidence available at the disclosure cutoff.

### Reverification

Reopened the immutable release, the full conference paper, ReactAppScan’s actual source/sink table and the ECOOP 2022 dynamic/static comparison. A second mechanism search for library summaries and missing-call-edge recovery found the 2012 report, reducing any claim of foundational novelty. Corrected ReactAppScan’s venue from the candidate bibliography’s S&P attribution to CCS 2024. ReactAppScan already lists DOM attribute sinks, so the candidate’s broad “none considered” statement is not accepted literally. Its 14 additional CodeQL sink categories are not 14 newly invented exploits. The historical autostitch code contains a React workLoop special case, and template mapping uses heuristics, so “generic” is conditional. The paper reports 24/57 false discoveries; package-level flows can require an external sanitizer and need not be exploitable end-to-end in every embedding. Its appendix says 24 baseline alerts while Table IV uses 34, an unresolved reproducibility inconsistency. Tests and source were inspected but not executed. The nomination page and complete local 2025 list were checked by title, authors, URLs and mechanism; this contribution is absent. The score evaluates the public December 2025 artifact, without rewarding later adoption or asserting every conference result was already documented in December.

### Verdict

**Tooling or methodology contribution; supporting archive inclusion in 2025.** The 2025 artifact clears the 55-point historical gate and is not an existing 2025 nomination. Include the artifact once in 2025; exclude this later conference copy from the 2026 display.

---

## 61.3 — [One Email, Many Faces: A Deep Dive into Identity Confusion in Email Aliases](https://funeoka-yumee.github.io/assets/files/ndss26_alias.pdf) [OriginMail](https://github.com/lab-rynth/OriginMail) — Mengying Wu, Geng Hong, Jiatao Chen, Baojun Liu, Mingxuan Liu and Min Yang

**KEPT** · Tooling or methodology contribution · confidence Medium

### Candidate

- **Title:** One Email, Many Faces: A Deep Dive into Identity Confusion in Email Aliases
- **Author or organisation:** Mengying Wu, Geng Hong, Jiatao Chen, Baojun Liu, Mingxuan Liu and Min Yang
- **Publication date / novelty cutoff:** 23 April 2025 for the substantive OriginMail normalization implementation; 29 July 2025 for the complete public preprint in the author’s Git history. September 2025 camera-ready and February 2026 conference publication are later copies.
- **Reference:** [One Email, Many Faces: A Deep Dive into Identity Confusion in Email Aliases](https://funeoka-yumee.github.io/assets/files/ndss26_alias.pdf)

Fresh full evaluation during the September 2026 threshold reconciliation; migrated from a compact 2026 record after verifying the original 2025 disclosure.

### Core Contribution

Systematically probes provider-specific email alias rules and compares them with account-registration checks, then supplies a normalization implementation and a study of human alias classification. The reusable increment is a cross-provider test matrix covering prefix, infix, suffix, case and domain transformations, including unusual provider rules. It extends known email canonicalization and identity-confusion analysis rather than inventing alias-based account multiplication or phishing.

### Prior Art

- **Candidate-side disclosure:** [OriginMail implementation, 23 April 2025](https://github.com/lab-rynth/OriginMail/blob/71e8d6e38130d739bf73acd88072eaa555607a9a/src/OriginMail.py) already contains the provider-specific transformation rules. The [complete preprint, 29 July 2025](https://raw.githubusercontent.com/funeoka-yumee/funeoka-yumee.github.io/0c6460ebb20ec38b4acff180d455b7959e6f39a6/assets/files/ndss26_alias.pdf) contains the comparative measurement and user study. Immutable Git timestamps are the available evidence; independent first-live snapshots were not found.
- **Earlier foundations and tooling:** [RFC 5233, January 2008, §4](https://www.rfc-editor.org/rfc/rfc5233) explicitly describes implementation-specific subaddress splitting, including prefixes, and warns that applying local rules to foreign addresses can misidentify them. [normalize-email, July 2015 release](https://github.com/johno/normalize-email/blob/de0dc4f1d79f2d1875aacd5ea75a00f9e6a4e22c/index.js) already normalizes provider-specific dots/plus tags/domain aliases; [August 2017 code](https://github.com/johno/normalize-email/blob/5c959f44294913628b270872e172029ae3b6e59d/index.js) explicitly adds Outlook-specific rules. Both historical implementations were read.
- **Earlier exploitation:** [James Fisher, 7 April 2018](https://jameshfisher.com/2018/04/07/the-dots-do-matter-how-to-scam-a-gmail-user/) describes Gmail/Netflix identity disagreement and a concrete payment phishing scenario. [Castle, 9 July 2025](https://blog.castle.io/detecting-gmail-based-fake-accounts-what-emailnator-teaches-us/) measured 46,000 Gmail variants collapsing to 291 roots and discussed free-tier abuse plus normalization. Castle predates the full July paper but postdates OriginMail’s April implementation, so it cannot diminish the April tool contribution.
- **Local check and distinction:** Mechanism searches found email-parsing and account-abuse material but no earlier preserved equivalent of this five-transformation, 28-provider/18-platform matrix. This is a useful measurement/tooling extension; the older account-abuse campaign and normalization concept are not new attacks. The full July preprint was compared against the fully read conference paper, with every changed earlier sentence read separately; later revised wording, artifact badges and recognition do not affect any score.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 48/100 | 25% | 12.00/25 | Broadens an established canonicalization/identity-confusion method into a comparative probe matrix and more unusual rules; core normalization and alias abuse precede it. |
| Transferability | 72/100 | 20% | 14.40/20 | Provider/consumer interpretation mismatches recur in registration, abuse detection and account correlation beyond any one service. |
| Lasting value | 70/100 | 20% | 14.00/20 | The test dimensions and separation of provider truth from relying-party interpretation support future testing; a static rule table still requires maintenance. |
| Technical soundness | 52/100 | 15% | 7.80/15 | Actual delivery probes and registration observations support implementation findings, but survey classification is not observed phishing compromise and several internal table/assertion inconsistencies limit stronger conclusions. |
| Practical usability | 65/100 | 10% | 6.50/10 | The original Python implementation and explicit transformations are usable in testing; ambiguous 2925 prefixes yield candidate roots rather than a uniquely safe normalization oracle. |
| Clarity and reproducibility | 66/100 | 10% | 6.60/10 | The immutable source and detailed preprint expose procedures and limitations, although aggregate documentation judgments and survey arithmetic contain unresolved errors. |

**Final score: 61.3/100.** Calculated with `score.py`; all six scores use evidence available at the disclosure cutoff.

### Reverification

Reopened the historical implementation, complete July preprint and its differences from the conference copy; independently searched disposable-account abuse and provider-specific normalization history. The April code already includes Eclipso separators, Proton punctuation and 2925 prefix candidates; these are not 2026 inventions. RFC 5233 expressly anticipates implementation-specific prefix/suffix conventions. The 2015/2017 library verifies prior provider-specific normalization, while Castle is used only against the later paper measurement claim. The study enrolled 304 people but analyzes 174 passing attention; its 31.65% concerns alias-classification errors, not measured phishing clicks or account compromise. Table VI says 151/174 equals 65.52%, which is arithmetically inconsistent. Its Eclipso plus example conflicts with the detailed separator set and historical code. Registration-check acceptance does not prove unlimited activated accounts or resource theft; only two actual accounts per tested platform were created. Provider-local case folding is not by itself an SMTP violation. The 139-account npm campaign is evidence reused from the authors’ earlier corpus, not a freshly invented attack. No experiment or supplied code was executed. The complete 2025 list and previously fetched nomination set were checked by title, authors, URLs and mechanism; this grouped contribution was absent. Earlier publication evidence changes placement, not research credit.

### Verdict

**Tooling or methodology contribution; supporting archive inclusion in 2025.** The 61.3-point methodology contribution passes the historical 55-point gate. Include it once under 2025, grouping the preprint with OriginMail, and exclude the later NDSS copy from the 2026 display.

---

---

## 67.8 — [Be Aware of What You Let Pass: Demystifying URL-based Authentication Bypass Vulnerability in Java Web Applications](https://racerz-fighting.github.io/paper/uabscan-ccs25.pdf) — Qiyi Zhang, Fengyu Liu, Zihan Lin and Yuan Zhang

**KEPT** · Tooling or methodology contribution · confidence Medium · reviewed 2026-09-10

### Candidate

- **Title:** Be Aware of What You Let Pass: Demystifying URL-based Authentication Bypass Vulnerability in Java Web Applications.
- **Authors:** Qiyi Zhang, Fengyu Liu, Zihan Lin and Yuan Zhang, Fudan University.
- **Publication date:** 2025; CCS proceedings dated 13–17 October. [Artifact metadata](https://zenodo.org/records/16990216) records 29 August 2025.
- **Reference:** Original author-hosted 15-page proceedings paper linked above.

### Core Contribution

UABScan maps framework versions and configuration to routing transformations, extracts authentication-related URL code slices, and compares risky checks with sanitization patterns. It turns known normalization bypasses into a targeted static audit method. It reports candidate inconsistencies; exploitation still needs manual validation.

### Prior Art

- **Novelty cutoff:** 2025, no later than the October proceedings; August artifact publication is an earlier candidate-side release. Exact first release of the full paper and prototype contents is unresolved. Only safely pre-2025 work is asserted as prior art.
- **Closest attack work:** Orange Tsai's [Breaking Parser Logic](https://i.blackhat.com/us-18/Wed-August-8/us-18-Orange-Tsai-Breaking-Parser-Logic-Take-Your-Path-Normalization-Off-And-Pop-0days-Out-2.pdf), Black Hat USA 2018, slides 44–49, already demonstrates path-parameter normalization disagreement bypassing ACLs and context mapping. The underlying bypass is not new.
- **Closest verified tool:** [BypassPro at its 21 June 2024 revision](https://github.com/0x727/BypassPro/tree/34a1d23f1fcf17e2c28f071bcfe0f3a0e5dda1be). Original README describes active/passive Burp fuzzing, `/public/..;`, status-code and response-similarity signals. It does not perform the candidate's routing/configuration-aware static slicing.
- **Local comparison:** Searched normalization, authentication bypass, UABScan and the candidate title across the lists and archive. The nominated 2018 slides are related prior art; the 2025 list contains no equivalent tool.
- **Distinct contribution:** A framework-feature model joined to path-specific data/control-flow and sanitization patterns, with measured ablations. Not a first claim to path traversal or authentication bypass.
- **Evidence boundary:** Proceedings body and its original evaluation only. Later lab publication pages were retrieval leads, not evidence of subsequent success; CVE counts, popularity and subsequent uptake do not affect scores.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 58 | 25% | 14.50 | Useful specialized static method built from established bypasses and analysis components. |
| Transferability | 71 | 20% | 14.20 | Routing-feature/check consistency generalizes; implementation models Spring and Jersey manually. |
| Lasting value | 76 | 20% | 15.20 | Configuration-aware comparison supplies a durable audit strategy for distributed enforcement. |
| Technical soundness | 68 | 15% | 10.20 | Concrete validations and ablations, but selected ground truth and inconsistent ablation prose limit confidence in aggregate claims. |
| Practical usability | 65 | 10% | 6.50 | Prototype and manageable reported runtime; compilation, framework models and manual PoCs constrain deployment. |
| Clarity and reproducibility | 72 | 10% | 7.20 | Algorithm, tuple design, examples and artifact are given; heuristic patterns and reporting discrepancies need care. |

**Final score: 67.8/100**

### Reverification

- **Candidate facts rechecked:** Read the full 15-page paper including algorithm, validation, limitations, references and example appendix; revisited §4–5 and the primary prior-art artifacts.
- **Cutoff audit:** Zenodo API confirms an unchanged 29 August 2025 metadata record. Exact first technical release remains a 2025 precision gap; 2018 and the pinned 2024 README are safely earlier.
- **Independent prior-art check:** Repeated searches using Java routing/authentication code slicing and static normalization detection; traced the paper's own BypassPro and Orange Tsai citations to their original contents.
- **Strongest challenge:** Most attack features are already known, and the 53 cases used to derive patterns overlap the historical ground-truth source population.
- **Benefit-of-doubt check:** Feature extraction and sanitization modeling reduce false positives in the reported ablations; this is a substantive method, even without new payloads.
- **Changes after reverification:** Score the method only. The paper verifies 56 findings among 70 tested reports, not all 94 reports; 87.5% recall concerns 24 historical vulnerabilities. Table 5 and its prose swap 24/28 false positives; the broader recall table uses a different denominator. These original reporting limitations affect technical/clarity scores, not an unsupported rejection of the whole method.

### Verdict

Tooling or methodology contribution.

- **Archive decision:** Include as a supporting reference.
- **Confidence:** Medium.
- **Reasoning:** Qualifies under the 55 gate for a reusable, evaluated audit method, with no credit for inventing normalization bypasses.
- **Evidence gaps:** Exact first technical release date; prototype was not executed; no independent validation of all reported findings.

---

## 69.5 — [The Power to Never Be Wrong: Evasions and Anachronistic Attacks Against Web Archives](https://www.securitee.org/files/kirchner_power_ccs2025.pdf) — Robin Kirchner, Chris Tsoukaladelis, Martin Johns and Nick Nikiforakis

**KEPT** · Meaningful extension · confidence Medium · reviewed 2026-09-10

### Candidate

- **Authors:** Robin Kirchner, Chris Tsoukaladelis, Martin Johns and Nick Nikiforakis.
- **Publication date:** 2025, CCS proceedings 13–17 October; April disclosure to services was private. Public patches in April are possible earlier partial disclosures, not proof the entire study was public.
- **Reference:** Original author-hosted 15-page paper linked above.

### Core Contribution

An archive observatory maps crawler characteristics, while deliberate policy-dependent page behavior and archive-specific bypasses allow publishers to evade faithful capture or change replayed content. The separable extension includes activating otherwise blocked code when CSP is stripped and combining measured crawler detection with replay manipulation across services.

### Prior Art

- **Novelty cutoff:** 2025, by the October proceedings; exact first public technical release remains unresolved. All asserted prior art is safely pre-2025.
- **Closest predecessor:** Lerner, Kohno and Roesner, [Rewriting History](https://adalerner.com/lerner-rewritingHistory-CCS17.pdf), CCS October–November 2017, §§3.2–3.3 and 5.1–5.4. It explicitly includes an unchanged first-party owner deliberately altering its own past, foresight, script URL obfuscation, same-origin archive escapes and nearest-neighbor anachronisms. These are not new 2025 threat models.
- **Additional earlier comparison:** Watanabe et al., *Melting Pot of Origins*, NDSS 2020, already evaluates rehosting attacks; its actual paper describes feasible demonstrations, so the candidate's characterization as purely theoretical is not adopted. Local archived prose has dropped ligatures, filed separately for repair.
- **Local exclusion:** Both earlier works are represented; the 2025 observatory and CSP-stripping evasion are absent from the curated year and previous completed cards.
- **Distinct contribution:** Systematic cross-service analysis, policy-removal activation and concrete routes around modern archive defenses. Ordinary cloaking and deliberate own-history modification receive no novelty credit.
- **Evidence boundary:** Original proceedings experiments and safely earlier work only. Later archive patches, uptake and policy responses do not influence any category.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 55 | 25% | 13.75 | Narrower evasion and measurement extension; much of the claimed threat model and replay manipulation is explicit prior art. |
| Transferability | 73 | 20% | 14.60 | Policy-dependent transformations and crawler observatories apply across rehosting services. |
| Lasting value | 75 | 20% | 15.00 | Reusable tests of capture/replay integrity and policy removal, not dependent on current crawler addresses. |
| Technical soundness | 76 | 15% | 11.40 | Concrete payloads, service-specific conditions and experiments; crawler attribution and detection false positives remain limitations. |
| Practical usability | 70 | 10% | 7.00 | Examples and observatory implementation support testing; some routes require several service-specific steps. |
| Clarity and reproducibility | 77 | 10% | 7.70 | Explicit attack requirements, tables and demos; full crawler dataset is restricted and broad novelty claims overstate the delta. |

**Final score: 69.5/100**

### Reverification

- **Candidate facts rechecked:** Full paper, references and appendix read; reopened primary paper and original 2017 predecessor, especially §§3 and 5.
- **Cutoff audit:** Private April exchanges are not the public cutoff; scored original 2025 publication against safely earlier 2017/2020 evidence.
- **Independent prior-art check:** Searched archive CSP-removal activation and deliberately planted future resources, then followed the candidate's own antecedent to its complete threat model.
- **Strongest challenge:** The paper calls intentional first-party history changes new, but the 2017 source states and illustrates them explicitly.
- **Benefit-of-doubt check:** That overstatement does not erase the separately demonstrated CSP-stripping evasion or systematic observatory method.
- **Changes after reverification:** Removed first-party threat-model novelty and reduced the verdict to an extension. Resource deletion remains theoretical; not every service permits every attack, and post-patch Megalodon needs its snapshot-only mode.

### Verdict

Meaningful extension.

- **Archive decision:** Include as a supporting reference.
- **Confidence:** Medium.
- **Reasoning:** Useful incremental methods survive a substantially narrower novelty comparison.
- **Evidence gaps:** Exact earliest public release of each partial mechanism; no independent demo replay; crawler dataset not publicly available in full.

---

## 60.7 — [In the DOM We Trust: Exploring the Hidden Dangers of Reading from the DOM on the Web](https://trouge.net/papers/in_the_dom_we_trust_ccs25.pdf) — Jan Drescher, Sepehr Mirzaei, Soheil Khodayari, David Klein, Thomas Barber, Martin Johns and Giancarlo Pellegrino

**KEPT** · Tooling or methodology contribution · confidence Medium

Reviewed 2026-09-10.

### Candidate

- **Title:** In the DOM We Trust: Exploring the Hidden Dangers of Reading from the DOM on the Web
- **Author or organisation:** Jan Drescher, Sepehr Mirzaei, Soheil Khodayari, David Klein, Thomas Barber, Martin Johns and Giancarlo Pellegrino
- **Publication date / novelty cutoff:** By 29 August 2025 substantive artifact documentation; exact earlier first release remains unresolved, with CCS paper in October2025.
- **Reference:** [Original source](https://trouge.net/papers/in_the_dom_we_trust_ccs25.pdf). Full-source reading, local exclusion checks and source-specific evidence are recorded in the [dated sweep](2026-09-10-sweep.md).

### Core Contribution

Extend DOM-source analysis and combine gadget discovery with separately verified markup injection, measuring their intersection and validation patterns. Two limited table/frameset selection adaptations may add capability. The defensible contribution is incremental methodology and measurement, not a new gadget class or four new ordering attacks.

### Prior Art

The full [2017 script-gadgets paper](https://raw.githubusercontent.com/google/security-research-pocs/master/script-gadgets/ccs_gadgets.pdf) already automates DOM taint, benign-markup generation and gadget validation. [Heyes, November–December2022](https://portswigger.net/research/hijacking-service-workers-via-dom-clobbering) directly demonstrates later html/body injection changing getElementById and querySelector selection: two claimed2025 ordering attacks are already exploitation knowledge. [Sheriff’s 2023 graph code](https://github.com/SoheilKhodayari/JAW/blob/c74fcfe6b62a6d93901f65ffd4d7483c2aab2b89/engine/lib/jaw/graphbuilder.js) and [Great Request Robbery, 2024](https://trouge.net/papers/sp24_request_hijacking.pdf) supply hybrid graph/taint machinery and non-XSS request sinks. [Parse Me Baby, 2024](https://www.ias.tu-bs.de/publications/parsing_differentials.pdf) already explains foster parenting; its selector-order adaptation is not automatically duplicate merely because the parser rule is old. Detailed comparison is in the [DOM follow-up](2026-09-10-dom-followup.md).

**Evidence boundary:** All six categories assess the original technical disclosure and demonstrably earlier knowledge. Later copies are retrieval evidence only; uptake, subsequent patches and present-day exploitability receive no credit or penalty. The dated sweep records the local mechanism search and nomination comparison.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 45 | 25% | 11.25 | Modest systematization; major ingredients and two exact ordering attacks are prior. |
| Transferability | 72 | 20% | 14.40 | Explicit DOM reads and sensitive sinks recur, subject to injection/selector/parser constraints. |
| Lasting value | 68 | 20% | 13.60 | DOM-source semantics and paired-prerequisite analysis offer reusable testing research. |
| Technical soundness | 62 | 15% | 9.30 | Substantial evidence and error analysis, but influence/impact and ordering claims require narrowing. |
| Practical usability | 58 | 10% | 5.80 | Useful tools with substantial setup and manual conditional-exploit investigation. |
| Clarity and reproducibility | 64 | 10% | 6.40 | Full method and dated artifact; ordering and live impact reproduction need gap filling. |

**Final score: 60.7/100**

### Reverification

- **Facts rechecked:** Full candidate,2017 paper and2024 Robbery paper read in the sweep/follow-up; main read candidate earlier and reopened Heyes’s complete relevant ordering examples after the new prior was found.
- **Cutoff audit:** [AE-v2 August29 record](https://zenodo.org/records/16994554) supplies a substantive public bound; all decisive prior is2024 or earlier, so exact2025 day uncertainty does not affect this comparison.
- **Independent check:** Search by later injection, first-match selectors and parser ordering found exact2022 attacks, overturning the stronger initial novelty draft.
- **Strongest challenge:** Mechanism, automation, sink taxonomy, hybrid machinery and two attacks already exist. **Benefit-of-doubt check:** DOM-source/injection-pair integration and constrained table/frameset adaptations retain useful incremental value.
- **Changes:** Reduced initial73.2 draft to60.7. The657 pairs are coexisting prerequisites,357,982 checks are marker influence, and34% is an ordering obstacle, not completed harmful attacks or successful new bypasses. Detailed cases lack a current injection.

### Verdict

Tooling or methodology contribution.

- **Archive decision:** Include as a supporting reference.
- **Confidence:** Medium.
- **Reasoning:** The bounded contribution described above clears the 55-point historical-addition gate; component age and familiar impact are excluded from its novelty credit.
- **Evidence gaps:** Exact earliest artifact visibility unresolved; conditional case studies,28.6% static false positives and8/13 benchmark detection limit impact/coverage. No live exploit execution.
