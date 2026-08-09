# 2016 candidate judgements

These scorecards apply the repository's weighted judge rubric. `KEPT` means the
candidate met the historical 60-or-above inclusion rule as well as the
first-publication, originality-verdict and original-nomination exclusions.

## 93.2 — [A Journey from JNDI/LDAP Manipulation to Remote Code Execution Dream Land](https://www.blackhat.com/docs/us-16/materials/us-16-Munoz-A-Journey-From-JNDI-LDAP-Manipulation-To-RCE-wp.pdf) — Alvaro Muñoz, Oleksandr Mirosh

**KEPT** · Original technique · confidence High

### Candidate

Black Hat USA whitepaper published in August 2016. The paper and conference
record establish the public date and distinguish the earlier 2015 applet sample
that motivated the broader research.

### Core contribution

The paper defines JNDI injection and LDAP entry poisoning as server-side attack
classes. Attacker-controlled RMI, CORBA or LDAP names and directory entries can
make Java resolve a reference, fetch a remote factory and instantiate code. It
turns obscure naming behavior into concrete Web-application tests and exploit
flows across enterprise frameworks.

### Prior art

Java deserialization, RMI remote loading and the 2015 CVE-2015-4902 applet chain
were public. They did not systematize untrusted JNDI lookup names or poisoned
object-returning LDAP searches as reusable server-side injection sinks. The
paper explicitly derives and demonstrates those two new classes.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 94 | 25% | 23.50 | Defines two new naming/directory injection classes. |
| Transferability | 94 | 20% | 18.80 | Applies across JNDI providers and Java enterprise stacks. |
| Lasting value | 98 | 20% | 19.60 | Became foundational to later JNDI testing and exploitation. |
| Technical soundness | 88 | 15% | 13.20 | Detailed internals, attack paths and affected APIs support the claims. |
| Practical usability | 90 | 10% | 9.00 | Gives concrete payload families and penetration-test guidance. |
| Clarity and reproducibility | 91 | 10% | 9.10 | Code, diagrams and stepwise flows are unusually complete. |

**Final score: 93.2/100.** Archive decision: include as a core technique.

### Verdict

Original technique. Earlier ingredients do not supply the generic untrusted-name
and poisoned-directory abstractions that remained reusable after the named
products were patched.

## 92.4 — [DROWN: Breaking TLS Using SSLv2](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/aviram) — Nimrod Aviram et al.

**KEPT** · Original technique · confidence High

### Candidate

The public DROWN disclosure appeared in March 2016; the complete paper was
published at USENIX Security in August 2016.

### Core contribution

DROWN uses a server that still accepts SSLv2 as a cross-protocol padding oracle
to decrypt modern TLS sessions, even when the victim client never speaks SSLv2.
Certificate and key reuse lets an oracle on one service endanger HTTPS on
another; a newly found OpenSSL flaw provides an accelerated practical variant.

### Prior art

Bleichenbacher RSA oracles date to 1998, and SSLv2's protocol flaws were known.
No earlier work located composed SSLv2's export behavior, modern RSA TLS
ciphertexts and cross-service key reuse into this oracle or supplied its new
query algorithms.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 93 | 25% | 23.25 | New cross-protocol RSA-decryption attack. |
| Transferability | 91 | 20% | 18.20 | Key reuse carries risk across protocols, hosts and services. |
| Lasting value | 95 | 20% | 19.00 | Canonical lesson in legacy-protocol composition. |
| Technical soundness | 96 | 15% | 14.40 | Algorithms, implementations and Internet measurements agree. |
| Practical usability | 82 | 10% | 8.20 | Accelerated attack is directly operational, general form is costly. |
| Clarity and reproducibility | 94 | 10% | 9.40 | Full paper, tooling, scans and parameters are public. |

**Final score: 92.4/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It is not another instance of Bleichenbacher but a new
protocol-composition oracle that makes an obsolete service break current TLS.

## 90.4 — [All Your DNS Records Point to Us](https://scholarworks.wm.edu/aspubs/823/) — Daiping Liu, Shuai Hao, Haining Wang

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed ACM CCS paper published in October 2016; the institutional record
links the proceedings DOI and complete work.

### Core contribution

The paper defines exploitable dangling DNS records and three takeover vectors:
re-registering a referenced domain, reclaiming a released IP, or acquiring an
abandoned cloud resource. It shows that control of the target resource can yield
the still-live subdomain and a valid CA certificate, then measures the problem
and proposes authenticity checks.

### Prior art

Stale delegations, expired-domain takeovers and isolated subdomain-takeover
reports predate 2016. The new contribution is the unified DNS-resource lifecycle
model, multiple resource-reclamation vectors and systematic method for finding
and exploiting the records at scale.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 87 | 25% | 21.75 | Defines and operationalizes the general dangling-resource class. |
| Transferability | 94 | 20% | 18.80 | Applies to domains, IPs and cloud resource mappings. |
| Lasting value | 93 | 20% | 18.60 | Foundation for modern subdomain-takeover research and tools. |
| Technical soundness | 91 | 15% | 13.65 | Three vectors and a large, manually validated measurement. |
| Practical usability | 86 | 10% | 8.60 | Preconditions translate directly into DNS audits. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Taxonomy, acquisition flow and validation are explicit. |

**Final score: 90.4/100.** Archive decision: include as a core technique.

### Verdict

Original technique. Earlier cases supply antecedents, but not this general model
of reclaimable DNS targets or its transferable discovery procedure.

## 89.4 — [Forwarding-Loop Attacks in Content Delivery Networks](https://www.ndss-symposium.org/wp-content/uploads/2017/09/forwarding-loop-attacks-content-delivery-networks.pdf) — Jianjun Chen et al.

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2016.

### Core contribution

A malicious CDN customer composes origin configuration, DNS control and header
filtering to make requests circulate within one CDN or across several. The loop
amplifies a small request into repeated processing and traffic, and cross-CDN
features can strip the headers intended to detect recurrence.

### Prior art

Routing loops, HTTP redirect loops and amplification attacks were established.
They did not exploit customer-controlled CDN forwarding as a multi-provider
application-layer loop or show that one provider's header features defeat
another provider's loop checks.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 90 | 25% | 22.50 | New CDN forwarding and amplification primitive. |
| Transferability | 91 | 20% | 18.20 | Works within and between heterogeneous CDNs. |
| Lasting value | 87 | 20% | 17.40 | Durable warning about user-controlled forwarding graphs. |
| Technical soundness | 92 | 15% | 13.80 | All 16 tested providers exposed some form of the flaw. |
| Practical usability | 85 | 10% | 8.50 | Clear configurations and bypass conditions support testing. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Mechanism, variants and mitigations are fully specified. |

**Final score: 89.4/100.** Archive decision: include as a core technique.

### Verdict

Original technique. The reusable idea is adversarial construction of a cyclic
HTTP forwarding graph across administrative boundaries.

## 87.3 — [Transcript Collision Attacks](https://www.ndss-symposium.org/wp-content/uploads/2017/09/transcript-collision-attacks-breaking-authentication-tls-ike-ssh.pdf) — Karthikeyan Bhargavan, Gaëtan Leurent

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2016. The practical TLS attacks
were disclosed as SLOTH.

### Core contribution

The work defines transcript collisions in authenticated key exchange: a
man-in-the-middle crafts two different handshake transcripts with the same weak
hash and forwards valid credentials between them. It demonstrates client or
server impersonation, channel-binding breaks and downgrade paths in TLS, IKE and
SSH.

### Prior art

MD5/SHA-1 collision attacks and rogue certificates were known, as were generic
unknown-key-share concerns. The paper is the first located to use chosen-prefix
collisions inside live key-exchange transcripts to break protocol
authentication rather than third-party signed documents.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 90 | 25% | 22.50 | New class of collision attack on handshake authentication. |
| Transferability | 82 | 20% | 16.40 | Demonstrated across TLS, IKE, SSH and channel bindings. |
| Lasting value | 91 | 20% | 18.20 | Influenced hash removal and protocol design. |
| Technical soundness | 94 | 15% | 14.10 | Generic model, concrete protocols and proofs of concept align. |
| Practical usability | 70 | 10% | 7.00 | Some variants are practical; others remain costly. |
| Clarity and reproducibility | 91 | 10% | 9.10 | Collision construction and transcripts are explicit. |

**Final score: 87.3/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It establishes collision resistance as a live protocol
authentication requirement, contrary to the then-common second-preimage claim.

## 87.3 — [Exploiting CORS Misconfigurations for Bitcoins and Bounties](https://portswigger.net/research/exploiting-cors-misconfigurations-for-bitcoins-and-bounties) — James Kettle

**KEPT** · Meaningful extension · confidence High

### Candidate

Researcher post dated 14 October 2016, based on the author's OWASP AppSec USA
talk and live-target research.

### Core contribution

The work turns CORS policy review into a reusable attack methodology: detect
reflected origins, exploit credentialed trust, use `null` origins, pivot through
trusted subdomains or insecure schemes, and assess cache behavior. Real API
examples show cross-origin extraction of account data and tokens.

### Prior art

Unsafe CORS configurations and cross-origin credential risks were already
public, including early implementation bugs and a prior post that inspired this
research. The distinct contribution is the systematic offensive workflow plus
new `null`-origin, trust-chain, redirect and caching adaptations validated on
real targets.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 72 | 25% | 18.00 | Materially extends known CORS risk with several attack paths. |
| Transferability | 95 | 20% | 19.00 | Applies to Web APIs and origin allowlists broadly. |
| Lasting value | 94 | 20% | 18.80 | Became the durable practical CORS-testing model. |
| Technical soundness | 86 | 15% | 12.90 | Browser behavior and multiple live findings substantiate it. |
| Practical usability | 96 | 10% | 9.60 | Direct request/response tests and payloads are immediately usable. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Each configuration and exploit is demonstrated clearly. |

**Final score: 87.3/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It does not invent CORS abuse; it supplies the enduring
offensive taxonomy and techniques that earlier warnings lacked.

## 87.0 — [Back in Black: Towards Formal, Black Box Analysis of Sanitizers and Filters](https://www.ieee-security.org/TC/SP2016/papers/0824a091.pdf) — George Argyros, Ioannis Stais, Angelos Keromytis, Aggelos Kiayias

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published in May
2016; the later Black Hat Europe LightBulb talk applies the same core work.

### Core contribution

The method learns symbolic automata for remote regular-expression filters and
transducers for sanitizers using only queries and outputs. Attack grammars serve
as an efficient equivalence oracle, exposing XSS/SQL-injection WAF bypasses and
permitting black-box equivalence checks among proprietary encoders.

### Prior art

Automata learning, WAF fuzzing and filter-bypass payload collections predate
2016. Existing learners required impractical query volumes and could not express
real sanitizers. The paper's symbolic inference and grammar-guided oracle are
the qualifying advances.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78 | 25% | 19.50 | New symbolic learners and security-specific equivalence oracle. |
| Transferability | 92 | 20% | 18.40 | General to WAFs, validators, encoders and sanitizers. |
| Lasting value | 88 | 20% | 17.60 | Durable approach to inferring hidden parser policies. |
| Technical soundness | 94 | 15% | 14.10 | Formal algorithms and real-system evaluation support it. |
| Practical usability | 83 | 10% | 8.30 | Finds bypasses remotely and powers a released framework. |
| Clarity and reproducibility | 91 | 10% | 9.10 | Algorithms, grammars and evaluations are detailed. |

**Final score: 87.0/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It turns known filter evasion into a
general, model-learning black-box audit technique.

## 86.8 — [Trusted Browsers for Uncertain Times](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/kohlbrenner) — David Kohlbrenner, Hovav Shacham

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2016.

### Core contribution

Attacker JavaScript amplifies degraded reference clocks by two orders of
magnitude and constructs multiple implicit clocks without querying a timer at
all. These mechanisms defeat browser defenses that merely coarsen explicit
timers; Fuzzyfox demonstrates whole-browser fuzzy time as a feasible defense.

### Prior art

Cross-origin timing attacks and reducing JavaScript timer resolution were well
known. Earlier work did not provide these implicit clocks or show a generic way
to recover high effective resolution from intentionally degraded clocks.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 83 | 25% | 20.75 | New implicit clocks and clock-amplification techniques. |
| Transferability | 89 | 20% | 17.80 | Applies to many browser timing channels and mitigations. |
| Lasting value | 92 | 20% | 18.40 | Anticipated recurring timer-reduction bypasses. |
| Technical soundness | 92 | 15% | 13.80 | Multiple clocks and a browser prototype are evaluated. |
| Practical usability | 70 | 10% | 7.00 | Attacks are reusable but require side-channel adaptation. |
| Clarity and reproducibility | 91 | 10% | 9.10 | Techniques, experiments and code design are explained. |

**Final score: 86.8/100.** Archive decision: include as a core technique.

### Verdict

Original technique. The offensive contribution is the family of timer-free and
timer-amplifying measurements, not the defensive browser fork.

## 85.7 — [A Comprehensive Formal Security Analysis of OAuth 2.0](https://arxiv.org/abs/1601.01229) — Daniel Fett, Ralf Küsters, Guido Schmitz

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

The complete preprint was first submitted 6 January 2016 and the peer-reviewed
version appeared at ACM CCS in October 2016.

### Core contribution

The authors model all four OAuth grants running concurrently with malicious
participants and realistic browser behavior. Formal proof attempts expose four
practical protocol attacks, including HTTP 307 credential forwarding and
authorization-server mix-up, then yield fixes and the first proof of the
repaired system's authorization, authentication and session integrity.

### Prior art

OAuth implementation bugs, IdP mix-up discussions and smaller formal models
predate 2016. None covered the full standard in this expressive Web model or
proved the corrected protocol across all modes and adversarial roles.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 75 | 25% | 18.75 | New full-protocol model, attacks and repaired proof. |
| Transferability | 96 | 20% | 19.20 | OAuth and its analysis pattern span the Web ecosystem. |
| Lasting value | 94 | 20% | 18.80 | Findings informed standards and later SSO analysis. |
| Technical soundness | 97 | 15% | 14.55 | Formal definitions, proofs and working attacks agree. |
| Practical usability | 55 | 10% | 5.50 | Expert-intensive, though fixes are directly actionable. |
| Clarity and reproducibility | 89 | 10% | 8.90 | Model, assumptions, attacks and proofs are documented. |

**Final score: 85.7/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. Individual OAuth flaws have antecedents;
the complete expressive analysis and proof-driven discovery process are new.

## 85.6 — [Attack Patterns for Black-Box Security Testing of Multi-Party Web Applications](https://www.ndss-symposium.org/wp-content/uploads/2017/09/attack-patterns-black-box-security-testing-multi-party-web-applications.pdf) — Avinash Sudhodanan, Alessandro Armando, Roberto Carbone, Luca Compagna

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2016.

### Core contribution

Security experts encode known multi-party attacks as application-agnostic
patterns; a ZAP-based engine maps observed protocol messages to those patterns
and generates black-box tests for replay, login CSRF and persistent XSS across
SSO, payment and other workflows. Seven patterns found 21 unknown flaws.

### Prior art

Multi-party payment and SSO logic attacks, model-based tests and black-box logic
testing were established. The distinct advance is extracting reusable attack
patterns from known attacks and automatically instantiating them without source
or a protocol-specific formal model.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 72 | 25% | 18.00 | New pattern abstraction and automatic instantiation method. |
| Transferability | 94 | 20% | 18.80 | Spans SSO, payments and other multi-party protocols. |
| Lasting value | 88 | 20% | 17.60 | Durable way to operationalize logic-attack knowledge. |
| Technical soundness | 92 | 15% | 13.80 | Framework and 21 new findings validate the approach. |
| Practical usability | 85 | 10% | 8.50 | ZAP integration makes expert patterns usable in testing. |
| Clarity and reproducibility | 89 | 10% | 8.90 | Pattern language, mappings and evaluation are explicit. |

**Final score: 85.6/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. The constituent attacks are known; the
general black-box pattern-transfer process is the qualifying contribution.

## 85.4 — [Towards Automated Dynamic Analysis for Linux-based Embedded Firmware](https://www.ndss-symposium.org/wp-content/uploads/2017/09/towards-automated-dynamic-analysis-linux-based-embedded-firmware.pdf) — Daming D. Chen, Manuel Egele, Maverick Woo, David Brumley

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2016.

### Core contribution

FIRMADYNE automatically extracts, emulates and dynamically analyzes Linux-based
embedded firmware using an instrumented kernel. At a scale of 23,035 images, it
identified 14 previously unknown vulnerabilities while addressing architecture,
network and boot differences that had blocked bulk whole-system analysis.

### Prior art

Static firmware extraction and manual or product-specific emulation predate
2016. The automated full-system pipeline and its demonstrated scale are the
qualifying methodological advance.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 76 | 25% | 19.00 | New scalable full-system firmware-emulation pipeline. |
| Transferability | 86 | 20% | 17.20 | Applies across large families of Linux embedded devices. |
| Lasting value | 90 | 20% | 18.00 | Established a durable basis for automated firmware analysis. |
| Technical soundness | 94 | 15% | 14.10 | Large evaluation and new findings support the method. |
| Practical usability | 80 | 10% | 8.00 | Automated workflow is useful despite emulation edge cases. |
| Clarity and reproducibility | 91 | 10% | 9.10 | Architecture, instrumentation and evaluation are explicit. |

**Final score: 85.4/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. Earlier work supplied components, while
FIRMADYNE made whole-system dynamic analysis broadly automatable.

## 84.9 — [AUTOFORGE: Automatic Forgery of Cryptographically Consistent Messages to Identify Security Vulnerabilities in Mobile Services](https://www.ndss-symposium.org/wp-content/uploads/2017/09/automatic-forgery-cryptographically-consistent-messages-identify-security-vulnerabilities.pdf) — Chaoshun Zuo, Wubing Wang, Rui Wang, Zhiqiang Lin

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2016.

### Core contribution

AUTOFORGE hooks client cryptographic APIs, infers protected message fields by
differential execution, and re-executes the application's own crypto to forge
valid mobile API requests. It thereby tests whether servers enforce security
properties that ordinary proxies cannot reach through signed or encrypted data.

### Prior art

Mobile API reverse engineering and traffic interception were established.
Automating cryptographically consistent mutation through lightweight runtime
observation and reuse of the target's crypto was not.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 75 | 25% | 18.75 | New automatic crypto-consistent request-forgery workflow. |
| Transferability | 92 | 20% | 18.40 | Generalizes across protected mobile-backed Web APIs. |
| Lasting value | 83 | 20% | 16.60 | Runtime semantic mutation remains a useful testing pattern. |
| Technical soundness | 91 | 15% | 13.65 | Design and vulnerability findings validate the approach. |
| Practical usability | 86 | 10% | 8.60 | Automates a previously labor-intensive testing step. |
| Clarity and reproducibility | 89 | 10% | 8.90 | Hooking, inference and mutation stages are documented. |

**Final score: 84.9/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It turns established mobile traffic
analysis into a materially new automated forgery method.

## 84.8 — [SWEET32: Birthday Attacks on 64-bit Block Ciphers in TLS and OpenVPN](https://sweet32.info/) — Karthikeyan Bhargavan, Gaëtan Leurent

**KEPT** · Meaningful extension · confidence High

### Candidate

The research and coordinated disclosure were published in August 2016.

### Core contribution

The authors make the birthday bound practical against long-lived TLS and
OpenVPN connections that use 64-bit CBC ciphers. Browser JavaScript generates
enough chosen traffic for ciphertext collisions to reveal recurring plaintext
such as cookies.

### Prior art

The birthday limit for small block ciphers and collision risks had long been
known, while browser-driven chosen traffic had BEAST-era precedent. The new
work supplies an end-to-end practical recovery attack against deployed suites.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 73 | 25% | 18.25 | Converts known theory into a practical deployed attack. |
| Transferability | 89 | 20% | 17.80 | Affects any long session using vulnerable 64-bit CBC suites. |
| Lasting value | 91 | 20% | 18.20 | Drove retirement of legacy ciphers and remains instructive. |
| Technical soundness | 92 | 15% | 13.80 | Analysis and demonstrations support plaintext recovery. |
| Practical usability | 78 | 10% | 7.80 | Requires heavy traffic but is operationally concrete. |
| Clarity and reproducibility | 89 | 10% | 8.90 | Attack conditions and demonstrations are clearly presented. |

**Final score: 84.8/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. The cryptographic limit was known, but its practical
Web-driven exploitation against real protocols was a substantial advance.

## 84.7 — [Request and Conquer: Exposing Cross-Origin Resource Size](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/vangoethem) — Tom Van Goethem, Mathy Vanhoef, Frank Piessens, Wouter Joosen

**KEPT** · Original contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2016.

### Core contribution

The work shows that browser storage mechanisms and request behavior expose the
exact size of cross-origin resources within seconds, enabling sensitive state
inference. A complementary Wi-Fi method extracts sizes from encrypted traffic.

### Prior art

Timing attacks and traffic-size leakage predate 2016, but generally offered
approximate or network-observer measurements. The reliable browser-side exact
resource-size primitive is the distinct contribution.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 75 | 25% | 18.75 | New exact cross-origin size-disclosure primitive. |
| Transferability | 91 | 20% | 18.20 | Applies to many state-dependent cross-origin resources. |
| Lasting value | 84 | 20% | 16.80 | Important foundation for later browser side channels. |
| Technical soundness | 92 | 15% | 13.80 | Multiple techniques and evaluations support the claims. |
| Practical usability | 81 | 10% | 8.10 | Fast browser-based inference is directly exploitable. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Measurement mechanisms and experiments are well specified. |

**Final score: 84.7/100.** Archive decision: include as a core technique.

### Verdict

Original contribution. It exposes a new exact cross-origin measurement
primitive rather than merely refining a known timing attack.

## 84.5 — [Timing Attacks Have Never Been So Practical: Advanced Cross-Site Search Attacks](https://www.blackhat.com/docs/us-16/materials/us-16-Gelernter-Timing-Attacks-Have-Never-Been-So-Practical-Advanced-Cross-Site-Search-Attacks.pdf) — Nethanel Gelernter

**KEPT** · Meaningful extension · confidence High

### Candidate

Presented at Black Hat USA in August 2016.

### Core contribution

The research develops browser-based response-size cross-site search that no
longer depends on strong server-side response inflation, plus a second-order
variant that plants records to amplify later private-search distinctions.

### Prior art

Cross-site search and response-inflation attacks were publicly demonstrated in
2015. These variants significantly broaden the conditions under which the
technique works but do not originate the family.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78 | 25% | 19.50 | New low-inflation and second-order variants. |
| Transferability | 90 | 20% | 18.00 | Applies across private search and stateful applications. |
| Lasting value | 86 | 20% | 17.20 | Expanded the practical XS-search design space. |
| Technical soundness | 86 | 15% | 12.90 | Demonstrations substantiate the attack mechanisms. |
| Practical usability | 85 | 10% | 8.50 | Browser-only exploitation is operationally accessible. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Variants and constraints are described with examples. |

**Final score: 84.5/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It materially relaxes and extends the earlier XS-search
attack rather than claiming the original response-inflation technique.

## 84.0 — [CSP Is Dead, Long Live CSP! On the Insecurity of Whitelists and the Future of Content Security Policy](https://research.google/pubs/csp-is-dead-long-live-csp-on-the-insecurity-of-whitelists-and-the-future-of-content-security-policy/) — Lukas Weichselbaum, Michele Spagnuolo, Sebastian Lekies, Artur Janc

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed ACM CCS paper published in October 2016.

### Core contribution

A large-scale study finds 94.72% of distinct real-world CSP policies
ineffective against XSS, systematizes three common whitelist bypass classes,
and proposes the nonce-based `strict-dynamic` model that avoids brittle host
allowlists.

### Prior art

JSONP, AngularJS and plugin-based CSP bypasses were already public, including
earlier community challenges. The systematic measurement, taxonomy and new
deployment model are the meaningful advances.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 55 | 25% | 13.75 | Known bypasses are synthesized into a new empirical case. |
| Transferability | 96 | 20% | 19.20 | Directly relevant to CSP deployments across the Web. |
| Lasting value | 94 | 20% | 18.80 | `strict-dynamic` became a durable defensive design. |
| Technical soundness | 95 | 15% | 14.25 | Large measurement and attack validation support conclusions. |
| Practical usability | 88 | 10% | 8.80 | Provides a deployable replacement policy pattern. |
| Clarity and reproducibility | 92 | 10% | 9.20 | Dataset, bypass classes and recommendation are clear. |

**Final score: 84.0/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. Public bypass ideas predate the paper; its systematic
evidence and robust policy model justify inclusion.

## 82.9 — [New gTLD Name Collisions and the WPAD Attack](https://www.ieee-security.org/TC/SP2016/papers/0824a675.pdf) — Qi Alfred Chen, Eric Osterweil, Matthew Thomas, Z. Morley Mao

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published in May
2016.

### Core contribution

Leaked internal WPAD names combined with newly delegated top-level domains let
an attacker register a matching domain and automatically route victims' Web
traffic through an attacker-controlled proxy. The work systematically measures
the exposure and demonstrates end-to-end interception.

### Prior art

WPAD query leakage and proxy auto-discovery abuse were known. The new-gTLD
ownership transition turns that leakage into a newly practical, measurable
cross-boundary attack.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 69 | 25% | 17.25 | New exploitation of delegated-domain name collisions. |
| Transferability | 91 | 20% | 18.20 | Affects organizations leaking internal WPAD names. |
| Lasting value | 86 | 20% | 17.20 | General lesson persists across namespace transitions. |
| Technical soundness | 91 | 15% | 13.65 | Measurement and demonstrations substantiate exposure. |
| Practical usability | 76 | 10% | 7.60 | Requires registrable collisions but enables automatic MITM. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Threat model, measurement and experiments are explicit. |

**Final score: 82.9/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It joins known WPAD leakage with a new domain-delegation
condition and demonstrates the resulting attack at scale.

## 82.8 — [CrossFire: An Analysis of Firefox Extension-Reuse Vulnerabilities](https://www.ndss-symposium.org/wp-content/uploads/2017/09/crossfire-analysis-firefox-extension-reuse-vulnerabilities.pdf) — Ahmet Salih Buyukkayhan, Kaan Onarlioglu, William Robertson, Engin Kirda

**KEPT** · Original contribution · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2016.

### Core contribution

CrossFire shows that a malicious extension can reuse capabilities accidentally
exposed by benign extensions, avoiding sensitive APIs and evading permission-
based review. Its analyzer detects vulnerable extension interactions and
generates proof-of-concept exploits.

### Prior art

Malicious browser extensions and overprivileged add-ons were well known. The
cross-extension capability-reuse channel and automatic exploit construction
form a distinct attack and analysis technique.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 85 | 25% | 21.25 | New cross-extension capability-reuse attack class. |
| Transferability | 80 | 20% | 16.00 | Broad within the affected extension architecture. |
| Lasting value | 78 | 20% | 15.60 | Durable composition lesson despite platform evolution. |
| Technical soundness | 91 | 15% | 13.65 | Analyzer and generated exploits validate the class. |
| Practical usability | 75 | 10% | 7.50 | Automated analysis helps, though ecosystem-specific. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Threat model and detection process are well documented. |

**Final score: 82.8/100.** Archive decision: include as a core technique.

### Verdict

Original contribution. The vulnerability emerges from extension composition,
not merely from another overprivileged or malicious add-on.

## 82.0 — [Tracking Mobile Web Users Through Motion Sensors: Attacks and Defenses](https://www.ndss-symposium.org/wp-content/uploads/2017/09/tracking-mobile-web-users-through-motion-sensors-attacks-defenses.pdf) — Anupam Das, Nikita Borisov, Matthew Caesar

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2016.

### Core contribution

Browser-accessible accelerometer and gyroscope readings reveal manufacturing
anomalies that fingerprint mobile devices. The authors improve stability using
inaudible sound stimulation and combine sensors for cross-site and cross-app
tracking, then evaluate defenses.

### Prior art

Application-side sensor fingerprinting had been proposed. This work adapts and
strengthens it under Web API constraints, supplying the practical browser
collection and multi-sensor tracking method.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78 | 25% | 19.50 | New practical Web and stimulated-sensor realization. |
| Transferability | 86 | 20% | 17.20 | Applies across mobile sites and applications with sensor access. |
| Lasting value | 80 | 20% | 16.00 | Important precedent for permissionless sensor privacy. |
| Technical soundness | 90 | 15% | 13.50 | Device experiments and defenses support the findings. |
| Practical usability | 70 | 10% | 7.00 | Collection is easy, while stability needs careful setup. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Features, stimulation and experiments are described. |

**Final score: 82.0/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It moves sensor fingerprinting from native-app prior art
to a stronger, usable Web tracking primitive.

## 80.9 — [Crippling HTTPS with Unholy PAC](https://blackhat.com/us-16/briefings.html#crippling-https-with-unholy-pac) — Itzik Kotler, Amit Klein

**KEPT** · Original contribution · confidence High

### Candidate

Presented at Black Hat USA in August 2016.

### Core contribution

A malicious proxy auto-configuration file can observe HTTPS destination URLs
without installing a TLS certificate and use PAC decisions as a bidirectional
channel. The work builds contextual phishing, denial-of-service, credential
and session attacks across browsers and platforms.

### Prior art

WPAD poisoning and malicious proxy configuration were known. The PAC-only
malware capabilities, especially HTTPS URL leakage and the two-way command
channel, are the new attack construction.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 80 | 25% | 20.00 | New PAC-only HTTPS observation and command techniques. |
| Transferability | 86 | 20% | 17.20 | Demonstrated across common browsers and platforms. |
| Lasting value | 82 | 20% | 16.40 | Durable warning about configuration-code privilege. |
| Technical soundness | 78 | 15% | 11.70 | Cross-platform demonstrations substantiate the claims. |
| Practical usability | 81 | 10% | 8.10 | Practical after PAC delivery or WPAD compromise. |
| Clarity and reproducibility | 75 | 10% | 7.50 | Briefing materials explain techniques but less fully than a paper. |

**Final score: 80.9/100.** Archive decision: include as a core technique.

### Verdict

Original contribution. It extracts a surprising attack platform from PAC
execution rather than merely repeating proxy interception.

## 73.1 — [HEIST: HTTP Encrypted Information Can Be Stolen Through TCP-Windows](https://www.blackhat.com/docs/us-16/materials/us-16-VanGoethem-HEIST-HTTP-Encrypted-Information-Can-Be-Stolen-Through-TCP-Windows-wp.pdf) — Mathy Vanhoef, Tom Van Goethem

**KEPT** · Meaningful extension · confidence High

### Candidate

Presented at Black Hat USA in August 2016. This is the previously retained 2016
missed reference; the current sweep preserves its established score.

### Core contribution

Attacker-controlled JavaScript manipulates and measures TCP receive windows to
infer exact encrypted response sizes, turning compression and size-oracle
attacks that previously assumed a network observer into browser-only attacks.

### Prior art

BREACH, TIME and Request and Conquer supplied compression, timing and size-
measurement foundations. HEIST's contribution is moving the observation point
into an ordinary victim browser through TCP flow-control behavior.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 56 | 25% | 14.00 | Recombines known families through a new TCP-window oracle. |
| Transferability | 82 | 20% | 16.40 | Applies to many authenticated cross-origin responses. |
| Lasting value | 78 | 20% | 15.60 | Durable browser/network side-channel lesson. |
| Technical soundness | 82 | 15% | 12.30 | Analysis and demonstrations support the oracle. |
| Practical usability | 72 | 10% | 7.20 | Browser-only model helps, though attack setup is demanding. |
| Clarity and reproducibility | 76 | 10% | 7.60 | Paper documents the mechanism and attack pipeline. |

**Final score: 73.1/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It composes prior compression and size work into a new
browser-visible transport oracle rather than originating those attack families.

## 69.3 — [Practical New Developments in the BREACH Attack](https://www.blackhat.com/docs/asia-16/materials/asia-16-Karakostas-Practical-New-Developments-In-The-BREACH-Attack-wp.pdf) — Dionysios Zindros, Dimitris Karakostas

**KEPT** · Meaningful extension · confidence High

### Candidate

Presented at Black Hat Asia in March 2016.

### Core contribution

The work makes BREACH more operational through a persistent HTTP command
channel, statistical handling of block-cipher and application noise,
parallelization, and the Rupture implementation.

### Prior art

BREACH was publicly disclosed in 2013 and already established the compression
oracle. These developments improve reliability and usability but do not create
a new attack family.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 35 | 25% | 8.75 | Practical refinements to a known attack. |
| Transferability | 83 | 20% | 16.60 | Refinements apply across noisy BREACH targets. |
| Lasting value | 77 | 20% | 15.40 | Useful operational treatment of compression oracles. |
| Technical soundness | 82 | 15% | 12.30 | Statistical methods and implementation support the claims. |
| Practical usability | 85 | 10% | 8.50 | Tooling and parallelization materially lower attack friction. |
| Clarity and reproducibility | 78 | 10% | 7.80 | Whitepaper and implementation describe the workflow. |

**Final score: 69.3/100.** Archive decision: include as a supplementary technique.

### Verdict

Meaningful extension. It is retained in the 60–69 band for practical advances,
with the 2013 BREACH disclosure credited as the origin.

## 69.1 — [A Simple Generic Attack on Text CAPTCHAs](https://www.ndss-symposium.org/wp-content/uploads/2017/09/simple-generic-attack-text-captchas.pdf) — Haichang Gao, Jeff Yan, Fang Cao, Zhilei Zhang, Lei Lei, Mengyun Tang, Ping Zhang, Xin Zhou, Xuejia Liu, Jiawei Li

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2016.

### Core contribution

A generic pipeline based on Log-Gabor filters segments and recognizes diverse
text CAPTCHAs without a scheme-specific attack. Across substantially different
designs it achieves 5–77% success in under 15 seconds.

### Prior art

CAPTCHA segmentation, OCR and numerous scheme-specific breaks were mature.
The contribution is a low-cost, generic filter-based attack that transfers
across designs rather than a new CAPTCHA weakness.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 45 | 25% | 11.25 | New generic use of Log-Gabor filtering in a mature field. |
| Transferability | 72 | 20% | 14.40 | Demonstrated across several distinct text CAPTCHA designs. |
| Lasting value | 68 | 20% | 13.60 | Generalization lesson remains useful as CAPTCHAs evolve. |
| Technical soundness | 89 | 15% | 13.35 | Broad experiments quantify accuracy and runtime. |
| Practical usability | 78 | 10% | 7.80 | Low cost and short runtime aid deployment. |
| Clarity and reproducibility | 87 | 10% | 8.70 | Pipeline, features and results are explicit. |

**Final score: 69.1/100.** Archive decision: include as a supplementary technique.

### Verdict

Tooling or methodology contribution. The score reflects a transferable attack
method, not originality of CAPTCHA recognition as a research area.

## 69.1 — [Killed by Proxy: Analyzing Client-end TLS Interception Software](https://www.ndss-symposium.org/wp-content/uploads/2017/09/killed-proxy-analyzing-client-end-tls-interception-software.pdf) — Xavier de Carné de Carnavalet, Mohammad Mannan

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2016.

### Core contribution

An integrated framework evaluates certificate generation, trust-store changes,
validation and proxy behavior in client-side TLS interception products. Tests
of eight antivirus and four parental-control products uncover proxy-specific
attack vectors and systemic failures.

### Prior art

TLS validation failures and earlier interception-proxy studies predate 2016.
The contribution is the client-end testing framework, product breadth and
proxy-specific synthesis rather than first discovery of broken validation.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 37 | 25% | 9.25 | New integrated framework over established failure modes. |
| Transferability | 77 | 20% | 15.40 | Applicable to many local TLS interception products. |
| Lasting value | 75 | 20% | 15.00 | Durable guidance for auditing endpoint middleboxes. |
| Technical soundness | 91 | 15% | 13.65 | Systematic multi-product experiments support findings. |
| Practical usability | 70 | 10% | 7.00 | Framework is useful but needs product-specific setup. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Test dimensions and results are thoroughly documented. |

**Final score: 69.1/100.** Archive decision: include as a supplementary technique.

### Verdict

Tooling or methodology contribution. It retains credit for a systematic audit
method while recognizing extensive prior TLS-validation work.

## 69.0 — [The Cracked Cookie Jar: HTTP Cookie Hijacking and the Exposure of Private Information](https://www.ieee-security.org/TC/SP2016/papers/0824a724.pdf) — Suphannee Sivakorn, Iasonas Polakis, Angelos Keromytis

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published in May
2016.

### Core contribution

The study shows that non-session HTTP cookies can retain privileged or
personalized functionality even when login cookies use HTTPS. It systematically
maps cookie dependencies and demonstrates private-data exposure, browser-app
abuse and Tor deanonymization.

### Prior art

Cookie sniffing, Firesheep-style hijacking and a 2013 Google-search leakage case
were known. The large cross-service dependency analysis and expansion beyond
session cookies are the meaningful additions.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 30 | 25% | 7.50 | Broadens and systematizes a known cookie problem. |
| Transferability | 86 | 20% | 17.20 | Applies across services with mixed cookie protections. |
| Lasting value | 72 | 20% | 14.40 | Useful lesson on cookie dependency and transport scope. |
| Technical soundness | 91 | 15% | 13.65 | Systematic service analysis supports the conclusions. |
| Practical usability | 75 | 10% | 7.50 | Attacks are concrete where plaintext cookies remain. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Cookie roles and experiments are clearly detailed. |

**Final score: 69.0/100.** Archive decision: include as a supplementary technique.

### Verdict

Meaningful extension. The score preserves prior cookie-hijacking credit while
recognizing the new dependency-driven exposure analysis.

## 68.3 — [Domain-Z: 28 Registrations Later; Measuring the Exploitation of Residual Trust in Domains](https://coeus.ece.gatech.edu/articles/domain-z-ieee.pdf) — Chaz Lever, Robert Walls, Yacin Nadji, David Dagon, Patrick Traynor

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published in May
2016.

### Core contribution

Domain-Z systematizes residual trust after domain ownership changes, measures
how malicious re-registration inherits traffic and authority, and introduces
Alembic, a passive-DNS method for detecting ownership transitions.

### Prior art

Expired-domain takeover, password-reset abuse, email inheritance and dangling
name-server cases were known. This work unifies those risks and adds broad
measurement and automated ownership-change detection.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 30 | 25% | 7.50 | Synthesizes known cases with a new detector and measurement. |
| Transferability | 83 | 20% | 16.60 | Residual trust affects many expired or transferred domains. |
| Lasting value | 78 | 20% | 15.60 | Domain lifecycle trust remains a recurring security issue. |
| Technical soundness | 90 | 15% | 13.50 | Registrations and passive-DNS analysis validate the model. |
| Practical usability | 65 | 10% | 6.50 | Detection needs historical infrastructure and careful attribution. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Taxonomy, detector and empirical method are explained. |

**Final score: 68.3/100.** Archive decision: include as a supplementary technique.

### Verdict

Meaningful extension. The study and detector advance a known expired-domain
risk enough to retain in the expanded 60-point record.

## 68.0 — [Website Fingerprinting at Internet Scale](https://www.ndss-symposium.org/wp-content/uploads/2017/09/website-fingerprinting-internet-scale.pdf) — Andriy Panchenko, Fabian Lanze, Andreas Zinnen, Martin Henze, Jan Pennekamp, Klaus Wehrle, Thomas Engel

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2016.

### Core contribution

A cumulative traffic representation improves encrypted website-fingerprinting
accuracy and speed, enabling experiments on 300,000 realistic pages. Results
separate poorly scaling page fingerprinting from still-feasible site-level
fingerprinting.

### Prior art

Website fingerprinting was a mature field and appeared in earlier annual lists.
The contribution is its Internet-scale representation, evaluation and sharper
statement of operational limits.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 47 | 25% | 11.75 | New representation and unprecedented realistic scale. |
| Transferability | 70 | 20% | 14.00 | Relevant across encrypted browsing traffic, with deployment limits. |
| Lasting value | 72 | 20% | 14.40 | Scale-aware conclusions remain useful to later evaluations. |
| Technical soundness | 90 | 15% | 13.50 | Large experiments rigorously test accuracy and limits. |
| Practical usability | 55 | 10% | 5.50 | Site-level use is possible; page-level scale remains difficult. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Features, dataset construction and results are explicit. |

**Final score: 68.0/100.** Archive decision: include as a supplementary technique.

### Verdict

Meaningful extension. It advances the scale and evaluation of an established
attack family, warranting retention below the former 70-point threshold.

## 66.2 — [Beauty and the Beast: Diverting Modern Web Browsers to Build Unique Browser Fingerprints](https://www.ieee-security.org/TC/SP2016/papers/0824a878.pdf) — Pierre Laperdrix, Walter Rudametkin, Benoit Baudry

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published in May
2016.

### Core contribution

The authors measure 17 modern attributes across 118,934 fingerprints, quantify
HTML5 and canvas features, and analyze differences and constraints on mobile
browsers to update the practical browser-fingerprinting model.

### Prior art

Panopticlick established large-scale browser fingerprinting in 2010 and canvas
fingerprinting was public by 2012. This is a modernized measurement and feature
extension, not the origin of fingerprinting.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 35 | 25% | 8.75 | Extends established fingerprinting with modern attributes. |
| Transferability | 75 | 20% | 15.00 | Findings apply across desktop and mobile browsers. |
| Lasting value | 73 | 20% | 14.60 | Useful snapshot and method for evolving browser surfaces. |
| Technical soundness | 88 | 15% | 13.20 | Large dataset supports the empirical conclusions. |
| Practical usability | 62 | 10% | 6.20 | Features are easy to collect but uniqueness varies. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Attribute definitions and evaluation are clear. |

**Final score: 66.2/100.** Archive decision: include as a supplementary technique.

### Verdict

Meaningful extension. It earns retention as a substantial modern measurement,
with explicit credit to earlier browser and canvas fingerprinting work.

## 65.5 — [I Know What You Saw Last Minute: Encrypted HTTP Adaptive Video Streaming Title Classification](https://arxiv.org/abs/1602.00490) — Ran Dubin, Amit Dvir, Ofir Pele, Ofer Hadar

**KEPT** · Meaningful extension · confidence High

### Candidate

The complete preprint was first submitted 1 February 2016.

### Core contribution

Machine learning identifies encrypted HTTP adaptive-streaming video titles
despite changing segment sizes and quality levels. Experiments on 10,000 streams
and 100 titles exceed 95% accuracy and include an unknown-title class.

### Prior art

Traffic classification of encrypted and non-adaptive video existed. The advance
is handling adaptive bitrate behavior at a materially larger title scale, not
originating encrypted-media inference.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 55 | 25% | 13.75 | Extends known classification to adaptive streaming. |
| Transferability | 72 | 20% | 14.40 | Relevant across common encrypted adaptive-video services. |
| Lasting value | 62 | 20% | 12.40 | Important privacy result, though traffic patterns evolve. |
| Technical soundness | 82 | 15% | 12.30 | Large controlled experiment supports reported accuracy. |
| Practical usability | 45 | 10% | 4.50 | Needs trained title sets and network observation. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Features, training and evaluation are documented. |

**Final score: 65.5/100.** Archive decision: include as a supplementary technique.

### Verdict

Meaningful extension. Adaptive streaming and unknown-title handling advance a
known traffic-analysis family enough to retain above the 60-point threshold.
