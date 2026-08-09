# 2009 candidate judgements

These scorecards apply the repository's weighted judge rubric. `KEPT` means
the candidate met the 60-or-above gate plus the calendar-year,
originality-verdict and original-nomination exclusions. `REMOVED` entries are
preserved so later audits do not rediscover and rescore them without context.

## 87.3 — [New Tricks for Defeating SSL in Practice](https://blackhat.com/presentations/bh-dc-09/Marlinspike/BlackHat-DC-09-Marlinspike-Defeating-SSL.pdf) — Moxie Marlinspike

**KEPT** · Original technique · confidence High

### Candidate

Primary Black Hat DC paper and presentation, February 2009. This is a fresh
reassessment of an existing missed-list entry.

### Core contribution

`sslstrip` intercepts an HTTP navigation before the browser enters TLS,
rewrites HTTPS links and forms to HTTP for the victim, and maintains HTTPS to
the real server. The same work demonstrates null-prefix certificate names that
exploit inconsistent X.509 name parsing.

### Prior art

TLS interception, active network attackers, HTTPS downgrade concerns and the
2008 ForceHTTPS proposal predate the work. The qualifying contribution is the
transparent, deployable pre-TLS stripping workflow and its concrete tool; the
null-prefix construction is a second independently demonstrated parser bypass.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 88 | 25% | 22.00 | Distinct operational downgrade and certificate-parser techniques. |
| Transferability | 88 | 20% | 17.60 | Applies broadly to mixed HTTP/HTTPS navigation and PKI clients. |
| Lasting value | 86 | 20% | 17.20 | Canonical reason for strict transport and parser consistency. |
| Technical soundness | 90 | 15% | 13.50 | Complete mechanisms and working tools/demonstrations. |
| Practical usability | 86 | 10% | 8.60 | Directly usable by an active network attacker. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Paper gives attack flow, constraints and implementation. |

**Final score: 87.3/100.** Archive decision: include as a core technique.

### Verdict

Original technique. Earlier downgrade concerns do not disclose the same
transparent rewriting workflow, and the certificate-name bypass is separately
novel and evidenced.

## 84.4 — [TLS Renegotiation Authentication Gap](https://www.kb.cert.org/vuls/id/120541/) — Marsh Ray, Steve Dispensa and the TLS community

**KEPT** · Original technique · confidence High

### Candidate

CERT VU#120541 records the November 2009 public disclosure and affected TLS
implementations. This is a fresh reassessment of an existing missed-list entry.

### Core contribution

An active attacker establishes a TLS connection, sends an attacker-controlled
request prefix, then splices the victim's newly authenticated renegotiated
session into the same connection. Servers treat the concatenated bytes as one
authenticated application stream.

### Prior art

TLS renegotiation itself and ordinary MITM attacks were known. The previously
unrecognized contribution is the protocol composition/authentication gap: the
renegotiated handshake does not cryptographically bind to the existing TLS
channel, allowing prefix injection without breaking TLS encryption.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 84 | 25% | 21.00 | New channel-splicing attack against a protocol feature. |
| Transferability | 83 | 20% | 16.60 | Cross-protocol-library and broadly server-relevant. |
| Lasting value | 86 | 20% | 17.20 | Drove the secure-renegotiation protocol fix. |
| Technical soundness | 90 | 15% | 13.50 | Reproduced across implementations with exact mechanics. |
| Practical usability | 81 | 10% | 8.10 | Requires active network position but is operational. |
| Clarity and reproducibility | 80 | 10% | 8.00 | Advisory clearly states conditions, impact and remedy. |

**Final score: 84.4/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It exploits a newly identified missing binding between TLS
handshakes, not a generic replay or already-known certificate failure.

## 84.4 — [Pretty-Bad-Proxy: An Overlooked Adversary in Browsers' HTTPS Deployments](https://www.microsoft.com/en-us/research/publication/pretty-bad-proxy-an-overlooked-adversary-in-browsers-https-deployments/) — Shuo Chen, Ziqing Mao, Yi-Min Wang and Ming Zhang

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper, May 2009. Although
the authors completed parts of the investigation earlier and coordinated fixes,
this paper is the first public primary publication.

### Core contribution

A malicious configured HTTP proxy attacks browser behavior above TLS without
decrypting TLS: crafted `CONNECT` error bodies can execute in the requested
HTTPS origin; redirects of imported scripts can execute attacker content with
victim-origin privilege; and HTTP/HTTPS rendering, mixed-content, cookie and
certificate-cache behavior yield further HTTPS compromises.

### Prior art

Ordinary MITM, SSL stripping, mixed-content attacks, ForceHTTPS and earlier
browser-domain bugs were known. The nominated active MITM item modifies normal
HTTP traffic. This work instead identifies proxy-specific browser state and
origin-assignment errors that remain exploitable despite an intact TLS channel.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | New proxy/browser interaction attacks above uncompromised TLS. |
| Transferability | 84 | 20% | 16.80 | Affected several major browsers and generic proxy deployments. |
| Lasting value | 87 | 20% | 17.40 | Durable lesson for origin assignment and HTTPS proxy handling. |
| Technical soundness | 91 | 15% | 13.65 | Multiple vendor-confirmed attacks with precise traces. |
| Practical usability | 78 | 10% | 7.80 | Practical wherever the attacker controls the configured proxy. |
| Clarity and reproducibility | 83 | 10% | 8.30 | Paper documents mechanisms, implementations and fixes. |

**Final score: 84.4/100.** Archive decision: include as a core technique.

### Verdict

Original technique. The proxy is not merely another MITM location; the attacks
abuse browser processing and security-origin decisions made around `CONNECT`
and redirected HTTPS subresources.

## 82.4 — [Cross-Origin JavaScript Capability Leaks](https://www.usenix.org/conference/usenixsecurity09/technical-sessions/presentation/cross-origin-javascript-capability-leaks) — Adam Barth, Joel Weinberger and Dawn Song

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed USENIX Security paper, August 2009, with an author project page,
paper and browser implementation findings.

### Core contribution

The work defines cross-origin JavaScript capability leaks as a systemic browser
implementation class caused by mismatch between DOM access control and the
JavaScript heap. It builds a points-to/heap-graph detector and demonstrates
prototype-chain, `__proto__`, setter and gadget paths that expose privileged
objects across origins.

### Prior art

Earlier browser-domain bugs and script-isolation systems treated individual
failures or new architectures. This paper provides a general object-capability
model, an automated detector and previously unknown WebKit exploitation paths.
It is also distinct from the same-year explicit mashup-API confused deputies.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78 | 25% | 19.50 | New systemic bug class plus automated detection method. |
| Transferability | 80 | 20% | 16.00 | General to browser JavaScript/DOM bindings. |
| Lasting value | 87 | 20% | 17.40 | Object-capability reasoning remains useful for origin isolation. |
| Technical soundness | 92 | 15% | 13.80 | Formal model, implementation and concrete new browser flaws. |
| Practical usability | 75 | 10% | 7.50 | Detector and exploit patterns are actionable for browser auditors. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Algorithms and demonstrations are well specified. |

**Final score: 82.4/100.** Archive decision: include as a core technique.

### Verdict

Original technique. Individual same-origin failures existed,
but the capability-leak abstraction and whole-heap detection workflow are a
distinct contribution.

## 80.4 — [OAuth Security Advisory 2009.1](https://oauth.net/advisories/2009-1/) — OAuth community

**KEPT** · Meaningful extension · confidence High

### Candidate

Primary OAuth security advisory published 23 April 2009. It documents a flaw
in the then-current OAuth Core 1.0 three-legged authorization protocol.

### Core contribution

An attacker obtains a request token and approval URL, lures a victim into
authorizing that token, then redeems the now victim-authorized token. OAuth 1.0
did not bind authorization completion to the consumer instance/callback that
started the flow, so ordinary consumer-side CSRF protection was insufficient.

### Prior art

Classic web session fixation was published by Acros in 2002 and CSRF was well
known. The extension is protocol-specific: the attacker fixes a pre-authorized
OAuth capability across the consumer, service provider and victim, yielding a
general flaw in compliant implementations. The nominated clickjacking/OAuth
item uses UI redressing and is a separate mechanism.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 62 | 25% | 15.50 | Applies known fixation to a new multi-party token protocol. |
| Transferability | 83 | 20% | 16.60 | Affected compliant OAuth 1.0 three-legged flows. |
| Lasting value | 86 | 20% | 17.20 | Led directly to OAuth 1.0a callback/verifier binding. |
| Technical soundness | 92 | 15% | 13.80 | Protocol-wide mechanism and remediation are exact. |
| Practical usability | 84 | 10% | 8.40 | Simple attacker workflow with broad provider impact. |
| Clarity and reproducibility | 89 | 10% | 8.90 | Advisory gives explicit attack and upgrade steps. |

**Final score: 80.4/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. Session fixation is prior art, but transferring it to an
unbound, multi-party OAuth request-token flow is a distinct and consequential
web authorization attack.

## 79.7 — [Secure Content Sniffing for Web Browsers](https://webblaze.cs.berkeley.edu/contentsniff.html) — Adam Barth, Juan Caballero and Dawn Song

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper, May 2009, supported
by the authors' primary project page and paper.

### Core contribution

The authors model browser MIME inference, extract high-fidelity algorithms for
four major browsers using source inspection and string-enhanced exploration,
and construct content-sniffing XSS attacks on HotCRP and Wikipedia. They derive
a prefix-disjoint, avoid-privilege-escalation sniffing rule.

### Prior art

JPEG/HTML chameleons appeared in 2004, content-sniffing XSS was disclosed in
2006, and other polyglot uploads were known. The contribution is not the first
sniffing exploit; it is the systematic cross-browser extraction method,
general attack construction and principled algorithm derived from it.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 79 | 25% | 19.75 | New systematic model extraction and general attack construction. |
| Transferability | 82 | 20% | 16.40 | Applies to upload filters and multiple browsers/content types. |
| Lasting value | 78 | 20% | 15.60 | Durable basis for safer sniffing and `nosniff` reasoning. |
| Technical soundness | 84 | 15% | 12.60 | Browser models and real application exploits validate the method. |
| Practical usability | 76 | 10% | 7.60 | Useful to both attackers and filter/browser auditors. |
| Clarity and reproducibility | 78 | 10% | 7.80 | Method, generated strings and cases are documented. |

**Final score: 79.7/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. The primitive predates 2009, but the reusable discovery
method and cross-browser attack model are separately novel.

## 78.8 — [Cross-Channel Scripting](https://www.blackhat.com/presentations/bh-usa-09/BOJINOV/BHUSA09-Bojinov-EmbeddedMgmt-PAPER.pdf) — Hristo Bojinov, Elie Bursztein, Eric Lovett and Dan Boneh

**KEPT** · Original technique · confidence High

### Candidate

Primary Black Hat USA paper, July 2009, reporting a study of 21 embedded
products from 16 vendors across eight device classes.

### Core contribution

Cross-channel scripting injects active content through a non-web protocol or
data channel—such as FTP filenames, SMB values, SIP caller names or logs—then
executes it when an administrator views the stored value in the device's web
management interface. Reverse XCS sends web input into another device service.

### Prior art

Stored XSS and inter-protocol exploitation were known. The nominated
cross-protocol XSS entry makes a browser speak to a service on a nonstandard
port. XCS instead crosses from a separate service/data channel into a web UI,
with repeatable source/sink auditing and broad product evidence.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 77 | 25% | 19.25 | New cross-channel source/sink attack model and reverse form. |
| Transferability | 76 | 20% | 15.20 | Demonstrated across protocols, vendors and device classes. |
| Lasting value | 77 | 20% | 15.40 | Durable embedded/management-plane testing pattern. |
| Technical soundness | 88 | 15% | 13.20 | Large audit with concrete, reproduced examples. |
| Practical usability | 75 | 10% | 7.50 | Direct payload and interface-testing workflow. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Paper clearly identifies channels, sinks and products. |

**Final score: 78.8/100.** Archive decision: include as a core technique.

### Verdict

Original technique. Its direction, trust-boundary model and embedded-interface
audit method are distinct from conventional stored XSS and the already
nominated browser-to-non-web-port attack.

## 75.2 — [Attacks on JavaScript Mashup Communication](https://www.ieee-security.org/TC/W2SP/2009/papers/s1p3.pdf) — Adam Barth, Collin Jackson and William Li

**KEPT** · Meaningful extension · confidence High

### Candidate

Primary W2SP paper published 21 May 2009.

### Core contribution

The paper analyzes lexical versus dynamic authorization and value versus
reference capabilities in mashup communication systems. It demonstrates
overwritable-built-in, caller-chain, dereference, invocation and prototype
confused-deputy attacks, then shows why primitive-only typed `postMessage`
reduces the exposed authority.

### Prior art

Subspace, MashupOS, SMash, OMash, Caja, ADsafe, FBJS and frame-communication
research all predate the paper. The qualifying advance is the comparative
attack taxonomy and concrete privilege-escalation analysis across explicit
mashup APIs, not the invention of mashups or cross-frame messaging.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 69 | 25% | 17.25 | New taxonomy and concrete confused-deputy attack set. |
| Transferability | 79 | 20% | 15.80 | Applies across several communication-system designs. |
| Lasting value | 79 | 20% | 15.80 | Capability typing remains important to API review. |
| Technical soundness | 82 | 15% | 12.30 | Attacks are traced through real systems and designs. |
| Practical usability | 67 | 10% | 6.70 | Most useful to framework and API auditors. |
| Clarity and reproducibility | 74 | 10% | 7.40 | Comparative model and examples are clear. |

**Final score: 75.2/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It turns known mashup mechanisms into a reusable method
for finding confused deputies and authority leaks in communication interfaces.

## 72.9 — [Code-Injection Attacks in Browsers Supporting Policies](https://www.ieee-security.org/TC/W2SP/2009/papers/s3p1.pdf) — Elias Athanasopoulos, Vasilis Pappas and Evangelos P. Markatos

**KEPT** · Original technique · confidence Medium

### Candidate

Primary W2SP paper published 21 May 2009.

### Core contribution

The authors bypass BEEP's whitelist without injecting new script. An attacker
moves or invokes already authorized JavaScript in a different event/location,
reusing trusted code to log out users, redirect, delete data or take over AJAX
actions. They frame this as return-to-JavaScript, analogous to code reuse.

### Prior art

XSS, DOM injection, BEEP's 2007 script whitelist and return-to-libc/ROP were
known. Injection of attacker data into trusted scripts was also recognized.
The distinct contribution is rearranging and invoking existing whitelisted web
code as attack gadgets to defeat a structural browser policy.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 71 | 25% | 17.75 | Early explicit trusted-JavaScript code-reuse attack. |
| Transferability | 74 | 20% | 14.80 | General to whitelist/policy systems with reusable page code. |
| Lasting value | 81 | 20% | 16.20 | Anticipates modern script-gadget and code-reuse analysis. |
| Technical soundness | 69 | 15% | 10.35 | Concrete examples, though evaluation is brief. |
| Practical usability | 66 | 10% | 6.60 | Requires suitable trusted gadgets and injection placement. |
| Clarity and reproducibility | 72 | 10% | 7.20 | Short paper clearly explains the transformation. |

**Final score: 72.9/100.** Archive decision: include as a core technique.

### Verdict

Original technique, confidence Medium because obscure pre-2009 practice cannot
be exhaustively excluded. The primary record nevertheless presents a distinct,
reproducible browser-policy bypass not found in the original nominations.

## 70.8 — [Unraveling Unicode: A Bag of Tricks for Bug Hunting](https://www.blackhat.com/presentations/bh-usa-09/WEBER/BHUSA09-Weber-UnicodeSecurityPreview-SLIDES.pdf) — Chris Weber

**KEPT** · Tooling or methodology contribution · confidence Medium

### Candidate

Primary Black Hat USA presentation, July 2009.

### Core contribution

The deck assembles a repeatable bug-hunting matrix across best-fit mappings,
normalization after validation, overlong and malformed UTF-8, sequence
overconsumption/deletion, case expansion, syntax whitespace and character-set
conversion. It connects those transformations to XSS and filter/WAF/NIDS
bypasses with platform-specific tests.

### Prior art

Unicode TR36, homographs, overlong UTF-8 and many individual encoding bypasses
were known. The original nominations also include particular Unicode quotation
and UTF-7 cases. The qualifying value is the cross-layer testing method and
organized set of transformation oracles, not any single encoding trick.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 48 | 25% | 12.00 | Most primitives are prior art; the systematic method is new value. |
| Transferability | 84 | 20% | 16.80 | Applies across filters, platforms, encodings and web stacks. |
| Lasting value | 76 | 20% | 15.20 | Canonical transformation-differential testing remains relevant. |
| Technical soundness | 76 | 15% | 11.40 | Numerous concrete mappings and API behaviors support the method. |
| Practical usability | 78 | 10% | 7.80 | Directly usable as a filter-bypass test checklist. |
| Clarity and reproducibility | 76 | 10% | 7.60 | Slides contain specific bytes, APIs and transformations. |

**Final score: 70.8/100.** Archive decision: include as qualifying material.

### Verdict

Tooling or methodology contribution. It is not the invention of Unicode
evasion, but it packages dispersed primitives into a transferable, technically
supported web bug-hunting workflow.

## 63.5 — [A Wolf in Sheep's Clothing](https://blackhat.com/presentations/bh-dc-09/Sutton/blackhat-dc-09-Sutton-persistent-storage.pdf) — Michael Sutton

**KEPT** · Meaningful extension · confidence Medium

### Candidate

Primary Black Hat DC presentation, February 2009.

### Core contribution

The work maps cookies, Flash Local Shared Objects, Google Gears and emerging
HTML5 databases as persistent browser attack surfaces. It demonstrates XSS-led
storage compromise and client-side SQL injection against an offline-capable
application, then turns those observations into an audit workflow.

### Prior art

Cookies, Flash storage, XSS and SQL injection were known. Alberto Trivero's
2008 *Abusing HTML 5* already describes client-side SQL injection, so that
primitive is not credited as original. The qualifying extension is the broad
persistent-storage threat model and worked validation across storage systems
and a real application.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 45 | 25% | 11.25 | Extends prior client-side SQLi/storage ideas rather than inventing them. |
| Transferability | 73 | 20% | 14.60 | Relevant across several browser persistence mechanisms. |
| Lasting value | 67 | 20% | 13.40 | Durable client-side storage threat-model lesson. |
| Technical soundness | 70 | 15% | 10.50 | Concrete mechanism comparison and application demonstration. |
| Practical usability | 66 | 10% | 6.60 | Provides a usable audit direction, with platform dependencies. |
| Clarity and reproducibility | 72 | 10% | 7.20 | Deck explains storage APIs and test cases clearly. |

**Final score: 63.5/100.** Archive decision: include as qualifying material.

### Verdict

Meaningful extension. Its score reflects substantial prior art, but the
cross-technology browser-storage audit and real offline-application case are a
distinct 2009 contribution above the inclusion gate.

## 53.8 — [Cross Site Scripting Anonymous Browser](https://www.blackhat.com/presentations/bh-dc-09/Flick/BlackHat-DC-09-Flick-XAB-wp.pdf) — Matthew Flick

**REMOVED** · Meaningful combination or adaptation · confidence Medium

### Candidate

Primary Black Hat DC whitepaper, February 2009.

### Core contribution

XAB uses browsers compromised by stored XSS as relays for attacker requests,
with a server-side XABProxy component and optional rebinding/cross-origin
techniques intended to obscure the attacker's source.

### Prior art

XSS-Proxy (2005), XSS Shell (2008), conventional server-side proxying and DNS
rebinding already supplied the major components. In the documented design, the
server proxy often fetches the ultimate target, weakening the claim that the
victim browser is a distinct anonymous transport primitive.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 35 | 25% | 8.75 | Mostly combines established XSS relay and proxy components. |
| Transferability | 61 | 20% | 12.20 | Applicable where durable XSS victims can be recruited. |
| Lasting value | 53 | 20% | 10.60 | Concept overlaps established browser botnet techniques. |
| Technical soundness | 64 | 15% | 9.60 | Working architecture, but anonymity claims are limited. |
| Practical usability | 58 | 10% | 5.80 | Requires stored XSS and supporting infrastructure. |
| Clarity and reproducibility | 68 | 10% | 6.80 | Components and flows are described adequately. |

**Final score: 53.8/100.** Archive decision: include as a supporting reference,
but do not add it to the year list.

### Verdict

Meaningful combination or adaptation, but below 60. The implementation is a
credible lead; its independent contribution is not strong enough for the list.

## 54.0 — [Weaponizing the Web / MonkeyFist](https://www.blackhat.com/presentations/bh-usa-09/HAMIEL/BHUSA09-Hamiel-WeaponizingWeb-SLIDES.pdf) — Nathan Hamiel and Shawn Moyer

**REMOVED** · Tooling or methodology contribution · confidence Medium

### Candidate

Primary Black Hat USA presentation, July 2009.

### Core contribution

MonkeyFist automates stateful and dynamic CSRF sequences: obtaining pages,
extracting tokens or session-dependent values, constructing POST bodies and
chaining redirects rather than relying on a single static request.

### Prior art

CSRF, multistep web requests, token extraction and XSS worms were known. The
deck itself describes dynamic CSRF as understood and cites earlier work. The
distinct value is implementation convenience rather than a new attack class.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 26 | 25% | 6.50 | Automation of known dynamic CSRF mechanics. |
| Transferability | 66 | 20% | 13.20 | Can model varied stateful request flows. |
| Lasting value | 58 | 20% | 11.60 | Useful automation, but superseded by broader tooling. |
| Technical soundness | 63 | 15% | 9.45 | Concrete workflow and tool examples. |
| Practical usability | 63 | 10% | 6.30 | Helpful for constructing dynamic payload chains. |
| Clarity and reproducibility | 70 | 10% | 7.00 | Slides explain the sequence and tool purpose. |

**Final score: 54.0/100.** Archive decision: include as a supporting reference,
but do not add it to the year list.

### Verdict

Tooling or methodology contribution, but below 60. It is preserved as a real
lead rather than promoted as an independent core technique.

## 59.3 — [Breaking the Security Myths of Extended Validation SSL](https://www.blackhat.com/presentations/bh-usa-09/SOTIROV/BHUSA09-Sotirov-AttackExtSSL-SLIDES.pdf) — Alexander Sotirov and Mike Zusman

**REMOVED** · Useful application or case study · confidence High

### Candidate

Primary Black Hat USA presentation dated 6 August 2009.

### Core contribution

The work demonstrates how a rogue non-EV certificate can undermine the user
meaning of EV through mixed content, same-origin behavior, SSL rebinding and
cache poisoning, including concrete browser-visible outcomes.

### Prior art

The rogue-CA construction, mixed-content threats and Jackson/Barth same-origin
analysis were already public and are explicitly part of the presentation's
foundation. EV-specific cache and rebinding demonstrations refine the impact,
but do not establish a sufficiently independent technique.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 20 | 25% | 5.00 | Primarily applies already-published mechanisms to EV UI claims. |
| Transferability | 68 | 20% | 13.60 | Relevant across EV-enabled browsers and sites. |
| Lasting value | 68 | 20% | 13.60 | Durable PKI/UI lesson, but represented by stronger primitives. |
| Technical soundness | 82 | 15% | 12.30 | Detailed and credible demonstrations. |
| Practical usability | 70 | 10% | 7.00 | Operational after obtaining a rogue trusted certificate. |
| Clarity and reproducibility | 78 | 10% | 7.80 | Clear attack chains and browser outcomes. |

**Final score: 59.3/100.** Archive decision: include as a supporting reference,
but do not add it to the year list.

### Verdict

Useful application or case study, below 60. The work is preserved in the audit
record but is conceptually represented by the rogue-CA, TLS and browser-origin
techniques already listed.
