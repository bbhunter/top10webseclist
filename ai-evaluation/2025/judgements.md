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
