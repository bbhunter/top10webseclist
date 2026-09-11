# 2013 candidate judgements

These scorecards apply the repository's weighted judge rubric. `KEPT` means
the candidate met the 60-or-above gate plus the calendar-year, qualifying
verdict and original-nomination exclusions. Screened leads that failed one of
those gates remain indexed in the companion README.

## 85.2 — [Practical HTTP Host Header Attacks](https://www.skeletonscribe.net/2013/05/practical-http-host-header-attacks.html) — James Kettle

**KEPT** · Original technique · confidence High

### Candidate

Primary researcher article published 16 May 2013. This is a fresh reassessment
of the sole existing missed-list entry.

### Core contribution

The work turns server trust in the HTTP `Host` header into reusable password-
reset poisoning, cache-poisoning and virtual-host routing attacks, and gives a
practical method for finding ambiguous host sources and forwarding overrides.

### Prior Art

HTTP virtual hosting, proxy host rewriting and cache poisoning were established
before 2013. The distinct contribution is the systematic application-level
attack surface—especially attacker-selected absolute reset links—and a coherent
test workflow across frameworks and intermediaries. The [primary article](https://www.skeletonscribe.net/2013/05/practical-http-host-header-attacks.html)
documents the preconditions, demonstrations and earlier host-spoofing context.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78/100 | 25% | 19.50/25 | Establishes a general host-derived-link attack class rather than one target bug. |
| Transferability | 88/100 | 20% | 17.60/20 | Applies across proxies, frameworks, caches and applications generating absolute URLs. |
| Lasting value | 88/100 | 20% | 17.60/20 | Host-header testing remains a standard application and infrastructure review task. |
| Technical soundness | 90/100 | 15% | 13.50/15 | Multiple mechanisms and real implementations validate the claims. |
| Practical usability | 84/100 | 10% | 8.40/10 | The probes and exploitation paths are directly actionable. |
| Clarity and reproducibility | 86/100 | 10% | 8.60/10 | Concrete requests, responses and attack flows are supplied. |

**Final score: 85.2/100.** Archive decision: include as a core technique.

### Verdict

Original technique. Earlier host manipulation did not provide this systematic
web-application attack model or password-reset poisoning workflow.

## 82.5 — [One Bad Apple: Backwards Compatibility Attacks on State-of-the-Art Cryptography](https://www.ndss-symposium.org/ndss2013/ndss-2013-programme/one-bad-apple-backwards-compatibility-attacks-state-art-cryptography/) — Tibor Jager, Kenneth G. Paterson and Juraj Somorovsky

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed NDSS paper published 24 April 2013. Private notifications in 2012
do not displace the 2013 public-paper date; the W3C first published the new
backwards-compatibility warning in its [24 January 2013 draft](https://www.w3.org/TR/2013/PR-xmlenc-core1-20130124/).

### Core contribution

An attacker changes an algorithm identifier so a strong AES-GCM or RSA-OAEP
ciphertext is processed by a weaker legacy algorithm under the same key. The
legacy CBC or PKCS#1 v1.5 oracle then compromises the modern ciphertext or a
reused signing key, demonstrated against XML Encryption and Web Services.

### Prior Art

Protocol downgrade attacks, CBC padding oracles and Bleichenbacher's RSA oracle
were known. The paper's distinct mechanism is a cross-algorithm oracle created
by backwards-compatible processing and key reuse; no interactive negotiation is
needed. The [W3C security section](https://www.w3.org/TR/2013/PR-xmlenc-core1-20130124/Overview_diff.html)
records the new class and mitigations.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 72/100 | 25% | 18.00/25 | New cross-algorithm use of established decryption oracles. |
| Transferability | 86/100 | 20% | 17.20/20 | General wherever legacy and modern algorithms share keys and dispatch formats. |
| Lasting value | 88/100 | 20% | 17.60/20 | Durable lesson for algorithm agility, policy enforcement and key separation. |
| Technical soundness | 94/100 | 15% | 14.10/15 | Formal analysis and practical XML/JWE cases support the result. |
| Practical usability | 70/100 | 10% | 7.00/10 | Requires a compatible legacy endpoint but gives a concrete attack recipe. |
| Clarity and reproducibility | 86/100 | 10% | 8.60/10 | Algorithms, conditions and implementations are precisely documented. |

**Final score: 82.5/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It is not ordinary version rollback: the attacker repurposes
a legacy primitive as an oracle against ciphertext from a stronger algorithm.

## 81.9 — [The Postman Always Rings Twice: Attacking and Defending postMessage in HTML5 Websites](https://www.ndss-symposium.org/ndss2013/ndss-2013-programme/postman-always-rings-twice-attacking-and-defending-postmessage-html5-websites/) — Sooel Son and Vitaly Shmatikov

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed NDSS paper published 23 April 2013.

### Core contribution

The authors systematically discover `postMessage` receivers, model their origin
checks and data use, and demonstrate how weak validation enables cross-origin
script injection and persistent manipulation through browser storage. The work
also extracts safe receiver patterns.

### Prior Art

`postMessage` and individual origin-check mistakes existed, and 2009 mashup work
studied explicit communication APIs. The [NDSS source](https://www.ndss-symposium.org/ndss2013/ndss-2013-programme/postman-always-rings-twice-attacking-and-defending-postmessage-html5-websites/)
adds a large-scale receiver-discovery and validation methodology with new real
vulnerabilities, rather than another isolated message bug.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 68/100 | 25% | 17.00/25 | Systematises a young bug class and adds new validation patterns. |
| Transferability | 88/100 | 20% | 17.60/20 | Applies to any cross-origin messaging integration. |
| Lasting value | 86/100 | 20% | 17.20/20 | Origin/source validation remains central to message-event testing. |
| Technical soundness | 91/100 | 15% | 13.65/15 | Large-scale analysis and confirmed exploits support the conclusions. |
| Practical usability | 80/100 | 10% | 8.00/10 | The receiver tests and exploit conditions translate directly to audits. |
| Clarity and reproducibility | 84/100 | 10% | 8.40/10 | Patterns, examples and measurements are well specified. |

**Final score: 81.9/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. The primitive predates the paper, but the
systematic discovery, classification and exploitation workflow is distinct.

## 81.0 — [Unauthorized Origin Crossing on Mobile Platforms: Threats and Mitigation](https://www.microsoft.com/en-us/research/publication/unauthorized-origin-crossing-on-mobile-platforms-threats-and-mitigation/) — Rui Wang, Luyi Xing, XiaoFeng Wang and Shuo Chen

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed ACM CCS paper published in November 2013.

### Core contribution

The paper identifies missing origin provenance across app intents, custom URL
schemes and web-access utilities on Android and iOS. Malicious web or app origins
can cross these channels to trigger mobile XSS/request forgery, steal OAuth-style
credentials and capture input in high-profile services.

### Prior Art

Android capability leaks and individual WebView flaws were known. This work's
distinct contribution is a systematic origin-crossing model across app-to-app and
web-to-app channels, with five new issue families and an origin-labelled defense.
The [author paper](https://homes.luddy.indiana.edu/luyixing/bib/ccs13-origin.pdf)
states the earlier capability-leak work and channel-specific differences.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 72/100 | 25% | 18.00/25 | Defines a new cross-channel origin-confusion class. |
| Transferability | 84/100 | 20% | 16.80/20 | Covers generic intents, schemes, utilities and web-service apps. |
| Lasting value | 82/100 | 20% | 16.40/20 | Origin provenance remains a core hybrid/mobile design problem. |
| Technical soundness | 91/100 | 15% | 13.65/15 | Systematic platform study and vendor-confirmed cases support the model. |
| Practical usability | 78/100 | 10% | 7.80/10 | The channels and attack flows are directly testable. |
| Clarity and reproducibility | 84/100 | 10% | 8.40/10 | The paper gives concrete traces, conditions and examples. |

**Final score: 81.0/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It generalises several mobile integration bugs into an origin-
provenance failure not captured by ordinary browser SOP or OS permissions.

## 80.6 — [Explicating SDKs: Uncovering Assumptions Underlying Secure Authentication and Authorization](https://www.cs.virginia.edu/~evans/pubs/usenix2013/) — Rui Wang, Yuchen Zhou, Shuo Chen, Shaz Qadeer, David Evans and Yuri Gurevich

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published 14–16 August 2013.

### Core contribution

The method builds semantic models of an SDK plus its runtime, explicitly states
the hidden assumptions needed for security, and formally checks all applications
constructible through the SDK. It found exploitable authentication/authorization
patterns in three SDKs and supplied a prototype detector.

### Prior Art

Formal protocol analysis and manual OAuth/SSO audits predate the work, including
the 2012 implementation studies already represented in the archive. The distinct
contribution is reasoning about SDK semantics and runtime assumptions across all
client applications, not one protocol trace. Models and publication evidence are
available from the [author project](https://www.cs.virginia.edu/~evans/pubs/usenix2013/).

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 70/100 | 25% | 17.50/25 | New SDK/runtime assumption-explication method. |
| Transferability | 82/100 | 20% | 16.40/20 | General to security-sensitive SDKs and app integrations. |
| Lasting value | 85/100 | 20% | 17.00/20 | Durable model for auditing abstraction boundaries and safe-use contracts. |
| Technical soundness | 94/100 | 15% | 14.10/15 | Formal models, broad reasoning and real findings corroborate the approach. |
| Practical usability | 72/100 | 10% | 7.20/10 | Model construction is specialised, but the detector and patterns are usable. |
| Clarity and reproducibility | 84/100 | 10% | 8.40/10 | Paper, models and prototype details are available. |

**Final score: 80.6/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It materially extends protocol auditing by
extracting and checking hidden SDK usage assumptions.

## 79.7 — [AUTHSCAN: Automatic Extraction of Web Authentication Protocols from Implementations](https://www.ndss-symposium.org/ndss2013/ndss-2013-programme/authscan-automatic-extraction-web-authentication-protocols-implementations/) — Guangdong Bai, Jike Lei, Guozhu Meng, Sai Sathyanarayan Venkatraman, Prateek Saxena, Jun Sun, Yang Liu and Jin Song Dong

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed NDSS paper published 23 April 2013.

### Core contribution

AUTHSCAN observes real browser/server implementations, extracts a protocol model
from executions, and sends that model to formal verification. It found seven
authentication flaws in deployed SSO and custom-login systems.

### Prior Art

Formal analysis of hand-written protocols and dynamic web scanning were known.
The [NDSS paper](https://www.ndss-symposium.org/ndss2013/ndss-2013-programme/authscan-automatic-extraction-web-authentication-protocols-implementations/)
connects them through automatic implementation-to-protocol extraction, avoiding
the frequent mismatch between specifications and deployed code. This differs from
Explicating SDKs, which models the SDK/runtime contract for all possible clients.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 69/100 | 25% | 17.25/25 | New implementation-to-formal-model extraction workflow. |
| Transferability | 82/100 | 20% | 16.40/20 | Applies across custom and federated web authentication protocols. |
| Lasting value | 84/100 | 20% | 16.80/20 | Bridges concrete implementations and formal verification. |
| Technical soundness | 92/100 | 15% | 13.80/15 | Formal checks and seven deployed findings validate the system. |
| Practical usability | 72/100 | 10% | 7.20/10 | Automated extraction lowers effort though setup remains specialised. |
| Clarity and reproducibility | 82/100 | 10% | 8.20/10 | Architecture, extraction and case studies are documented. |

**Final score: 79.7/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It scales formal authentication analysis to
the behavior of real implementations rather than idealised specifications.

## 78.1 — [Automated Password Extraction Attack on Modern Password Managers](https://arxiv.org/abs/1309.1416) — Raul Gonzalez, Eric Y. Chen and Collin Jackson

**KEPT** · Meaningful combination or adaptation · confidence High

### Candidate

Primary public paper submitted 5 September 2013.

### Core contribution

Lupin injects hidden frames into any intercepted HTTP response, supplies forged
same-origin login pages, and lets Chrome or Firefox autofill stored credentials.
It can steal credentials for sites the victim is not visiting, including passwords
whose form action is HTTPS, and automates the process across 1,000 sites.

### Prior Art

Network response injection, iframe loading, autofill risks and same-origin attacks
were known; 2012 Self-Exfiltration also showed form-action checks were insufficient.
The [paper](https://arxiv.org/abs/1309.1416) explicitly distinguishes those pieces.
Its new capability is scalable extraction of unrelated saved credentials through
the composition of a network foothold and password-manager origin matching.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 64/100 | 25% | 16.00/25 | Non-obvious combination creates bulk off-path credential extraction. |
| Transferability | 80/100 | 20% | 16.00/20 | Applies broadly to automatic origin-based password filling on HTTP pages. |
| Lasting value | 82/100 | 20% | 16.40/20 | Durable lesson for credential-manager binding and secure transport. |
| Technical soundness | 86/100 | 15% | 12.90/15 | Working tool and 45,000-site measurement substantiate the attack. |
| Practical usability | 86/100 | 10% | 8.60/10 | Automated, stealth-conscious implementation lowers the attack cost. |
| Clarity and reproducibility | 82/100 | 10% | 8.20/10 | Four-step workflow, browser conditions and measurements are explicit. |

**Final score: 78.1/100.** Archive decision: include as a core technique.

### Verdict

Meaningful combination or adaptation. Familiar primitives are assembled into a
new, scalable password-manager extraction capability.

## 76.7 — [Truncating TLS Connections to Violate Beliefs in Web Applications](https://www.usenix.org/conference/woot13/workshop-program/presentation/smyth) — Ben Smyth and Alfredo Pironti

**KEPT** · Meaningful extension · confidence High

### Candidate

Black Hat USA and peer-reviewed WOOT paper, August 2013.

### Core contribution

An active attacker drops selected concurrent TLS connections so the browser shows
success before the server commits a state change. This desynchronises user and
server beliefs and enables blocked logout, vote manipulation and account takeover
without breaking TLS confidentiality or integrity.

### Prior Art

TLS truncation and partial-response concerns predate 2013. The [WOOT paper](https://www.usenix.org/system/files/conference/woot13/woot13-smyth.pdf)
adds application-state exploitation across parallel requests, selected request
truncation and concrete authentication failures rather than incomplete documents.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 62/100 | 25% | 15.50/25 | Extends truncation into a reusable application-state attack. |
| Transferability | 82/100 | 20% | 16.40/20 | General to optimistic UI feedback and concurrent state-changing requests. |
| Lasting value | 80/100 | 20% | 16.00/20 | Durable lesson about transport guarantees versus distributed application state. |
| Technical soundness | 88/100 | 15% | 13.20/15 | Formalised model and real voting/authentication demonstrations. |
| Practical usability | 74/100 | 10% | 7.40/10 | Requires an active network position but uses deployable traffic control. |
| Clarity and reproducibility | 82/100 | 10% | 8.20/10 | Attack traces, targets and assumptions are clear. |

**Final score: 76.7/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It transforms an older transport edge case into a general
web-application state and authentication attack.

## 75.5 — [DOM Clobbering](https://thespanner.co.uk/2013/05/16/dom-clobbering) — Gareth Heyes

**KEPT** · Meaningful extension · confidence High

### Candidate

Primary researcher article published 16 May 2013.

### Core contribution

Attacker-controlled, non-script HTML with chosen `id` and `name` values creates
global named properties and nested collections that shadow variables and APIs.
This lets markup injection alter trusted JavaScript control flow and can escalate
to script execution even where direct script injection is blocked.

### Prior Art

Named DOM properties were old browser behavior, and the 2010 [frame-busting study](https://seclab.stanford.edu/websec/framebusting/)
used a `self`-named element to defeat framebusters. The 2013 article generalises
that quirk into nested property clobbering, collection construction and code-
execution patterns; later PortSwigger research identifies it as the technique's
[first introduction](https://portswigger.net/research/dom-clobbering-strikes-back).

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 58/100 | 25% | 14.50/25 | Generalises an older quirk into a broader exploit primitive. |
| Transferability | 86/100 | 20% | 17.20/20 | Any script relying on clobberable named properties can be affected. |
| Lasting value | 86/100 | 20% | 17.20/20 | Remains relevant to sanitizers, CSP and framework gadgets. |
| Technical soundness | 76/100 | 15% | 11.40/15 | Working cross-browser examples establish the behavior; coverage is informal. |
| Practical usability | 84/100 | 10% | 8.40/10 | Payloads are compact and immediately testable. |
| Clarity and reproducibility | 68/100 | 10% | 6.80/10 | Clear examples, but limited formal scoping and browser matrix. |

**Final score: 75.5/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. Prior framebuster clobbering existed, but the named-property
and collection attack model materially broadens it into a reusable code primitive.

## 75.4 — [When Tolerance Causes Weakness: The Case of Injection-Friendly Browsers](https://archives.iw3c2.org/www2013/proceedings/p435.pdf) — Yossi Gilad and Amir Herzberg

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed WWW paper published 13–17 May 2013.

### Core contribution

A browser puppet, spoofed packets and browsers' tolerance of malformed HTTP let
an off-path attacker infer a connection's client port and sequence number, inject
responses and persist malicious objects in shared caches without predictable IP-ID
or malware on the client.

### Prior Art

Blind TCP injection is old, and the authors' 2012 Off-Path Attacking the Web work
required Windows/global counters and predictable allocation. The [2013 paper](https://archives.iw3c2.org/www2013/proceedings/p435.pdf)
explicitly removes those assumptions through browser invalid-response behavior,
hash-port derandomisation and a modular cache-poisoning exploit.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 62/100 | 25% | 15.50/25 | New modules remove major prerequisites from the authors' earlier attack. |
| Transferability | 80/100 | 20% | 16.00/20 | Browser/HTTP behavior and Linux-derived port selection are broadly shared. |
| Lasting value | 78/100 | 20% | 15.60/20 | Useful model for composing browser puppets with transport side channels. |
| Technical soundness | 87/100 | 15% | 13.05/15 | Detailed modular analysis and current-browser evaluation. |
| Practical usability | 70/100 | 10% | 7.00/10 | Requires spoofing capability but no on-path position or client malware. |
| Clarity and reproducibility | 82/100 | 10% | 8.20/10 | Modules, requirements and prior comparisons are explicit. |

**Final score: 75.4/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It is not a repeat of the 2012 attack: it replaces platform-
specific counters with new browser and transport mechanisms and adds persistent
cache poisoning.

## 74.5 — [Cookieless Monster: Exploring the Ecosystem of Web-Based Device Fingerprinting](https://seclab.cs.ucsb.edu/publications/nikiforakis2013cookieless_monster/) — Nick Nikiforakis, Alexandros Kapravelos, Wouter Joosen, Christopher Kruegel, Frank Piessens and Giovanni Vigna

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper, May 2013.

### Core contribution

The work reverse-engineers commercial fingerprinting libraries, measures their
deployment and adds fast implementation-divergence tests that identify browser
families and minor versions despite user-agent spoofing. It also exposes proxy
bypass and plugin-installation practices used by commercial trackers.

### Prior Art

Panopticlick (2010), JavaScript-engine fingerprinting (2011) and canvas
fingerprinting (2012) already established stateless identification. The [paper](https://www.ieee-security.org/TC/SP2013/papers/4977a541.pdf)
acknowledges those works and adds new browser-version probes, commercial ecosystem
analysis and evidence that spoofing extensions can increase uniqueness.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 55/100 | 25% | 13.75/25 | Extends known fingerprinting with new implementation probes and ecosystem evidence. |
| Transferability | 78/100 | 20% | 15.60/20 | Methods span browsers, versions and commercial libraries. |
| Lasting value | 80/100 | 20% | 16.00/20 | Established a durable measurement and anti-spoofing baseline. |
| Technical soundness | 90/100 | 15% | 13.50/15 | Code analysis, measurement and controlled tests corroborate claims. |
| Practical usability | 74/100 | 10% | 7.40/10 | Probes and taxonomy are readily useful for tracking audits. |
| Clarity and reproducibility | 82/100 | 10% | 8.20/10 | Features, providers and experiments are documented. |

**Final score: 74.5/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It does not originate browser fingerprinting, but adds
transferable new probes and the first detailed view of operational providers.

## 74.0 — [Language-based Defenses Against Untrusted Browser Origins](https://www.usenix.org/conference/usenixsecurity13/technical-sessions/presentation/bhargavan) — Karthikeyan Bhargavan, Antoine Delignat-Lavaud and Sergio Maffeis

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2013.

### Core contribution

The authors demonstrate that a hosting page or peer component can tamper with
security-sensitive SSO and client-cryptography code through the shared JavaScript
global environment. They define defensive JavaScript patterns, a type system and
a model-extraction workflow that finds and repairs behavior-integrity failures.

### Prior Art

Prototype poisoning, hostile same-origin scripts and component-isolation proposals
predate 2013. The [USENIX source](https://www.usenix.org/conference/usenixsecurity13/technical-sessions/presentation/bhargavan)
adds original attacks against real security components and a reusable method for
proving library behavior in an adversarial shared realm.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 55/100 | 25% | 13.75/25 | Extends shared-realm interference into systematic component attacks and analysis. |
| Transferability | 80/100 | 20% | 16.00/20 | Applies to embedded SSO, cryptography and encoding libraries on hostile pages. |
| Lasting value | 78/100 | 20% | 15.60/20 | Durable insight for JavaScript supply chains and component integrity. |
| Technical soundness | 92/100 | 15% | 13.80/15 | Sound type system, formal verifier and implemented cases support the claims. |
| Practical usability | 66/100 | 10% | 6.60/10 | Patterns are useful though full formal modelling is specialised. |
| Clarity and reproducibility | 82/100 | 10% | 8.20/10 | Attacks, language subset and examples are clearly supplied. |

**Final score: 74.0/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. Known JavaScript interference is developed
into a rigorous attack-and-verification method for security-sensitive components.

## 73.0 — [Take This Personally: Pollution Attacks on Personalized Services](https://www.usenix.org/conference/usenixsecurity13/technical-sessions/paper/xing) — Xinyu Xing, Wei Meng, Dan Doozan, Alex C. Snoeren, Nick Feamster and Wenke Lee

**KEPT** · Meaningful combination or adaptation · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2013.

### Core contribution

An attacker induces actions or interests in one victim's profile so a service's
personalisation algorithm promotes attacker-chosen videos, products or search
results specifically to that victim. The manipulation is invisible to both the
victim and provider and is demonstrated across YouTube, Amazon and Google.

### Prior Art

Recommender shilling, search poisoning and profile injection existed, generally
using many fake users to alter global outputs. The [paper](https://www.usenix.org/conference/usenixsecurity13/technical-sessions/paper/xing)
adapts those ideas to targeted, cross-service pollution of an individual user's
implicit profile and provides general attack phases.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 58/100 | 25% | 14.50/25 | Non-obvious targeted adaptation of established poisoning ideas. |
| Transferability | 78/100 | 20% | 15.60/20 | Applies across services learning profiles from observable actions. |
| Lasting value | 75/100 | 20% | 15.00/20 | Anticipates adversarial manipulation of personalised systems. |
| Technical soundness | 86/100 | 15% | 12.90/15 | Three independent service demonstrations support generality. |
| Practical usability | 70/100 | 10% | 7.00/10 | Service details vary, but the attack workflow is actionable. |
| Clarity and reproducibility | 80/100 | 10% | 8.00/10 | Mechanisms, experiments and limitations are clear. |

**Final score: 73.0/100.** Archive decision: include as a core technique.

### Verdict

Meaningful combination or adaptation. It redirects known poisoning concepts into
a transferable, victim-specific web-personalisation attack.

## 71.9 — [Exploiting Innocuous Activity for Correlating Users Across Sites](https://archives.iw3c2.org/www2013/proceedings/p447.pdf) — Oana Goga, Howard Lei, Sree Hari Krishnan Parthasarathi, Gerald Friedland, Robin Sommer and Renata Teixeira

**KEPT** · Meaningful combination or adaptation · confidence High

### Candidate

Peer-reviewed WWW paper published 13–17 May 2013.

### Core contribution

The attack links pseudonymous accounts across Yelp, Flickr and Twitter using
implicit location, posting-time and writing-style signals rather than declared
profile fields. Combining the signals correlates more Yelp/Twitter accounts than
username matching alone.

### Prior Art

Graph de-anonymisation, username matching and large-scale stylometry predate the
paper. Its [primary paper](https://archives.iw3c2.org/www2013/proceedings/p447.pdf)
explicitly compares those methods and contributes the combination of innocuous
activity features for cross-site account linkage, including real ground truth.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 54/100 | 25% | 13.50/25 | New feature combination and threat model over known re-identification methods. |
| Transferability | 80/100 | 20% | 16.00/20 | Location, timing and language signals recur across social platforms. |
| Lasting value | 74/100 | 20% | 14.80/20 | Useful foundation for cross-platform identity-linkage research. |
| Technical soundness | 88/100 | 15% | 13.20/15 | Large ground-truth sets and baseline comparisons support the conclusions. |
| Practical usability | 64/100 | 10% | 6.40/10 | Requires substantial data collection but no privileged access. |
| Clarity and reproducibility | 80/100 | 10% | 8.00/10 | Features, classifiers and evaluation are described. |

**Final score: 71.9/100.** Archive decision: include as a core technique.

### Verdict

Meaningful combination or adaptation. Established inference methods are combined
into a distinct cross-site activity-correlation capability.

## 70.4 — [I Know the Shortened URLs You Clicked on Twitter](https://archives.iw3c2.org/www2013/proceedings/p1191.pdf) — Jonghyuk Song, Sangho Lee and Jong Kim

**KEPT** · Meaningful combination or adaptation · confidence High

### Candidate

Peer-reviewed WWW paper published 13–17 May 2013.

### Core contribution

The attack repeatedly polls public bit.ly and goo.gl aggregate click analytics,
observes changes in country, platform, browser and referrer, and correlates them
with public Twitter metadata to infer which known user clicked a particular link.

### Prior Art

Browser-history inference, traffic correlation and public aggregate statistics
were known. The [paper](https://archives.iw3c2.org/www2013/proceedings/p1191.pdf)
contributes a browser-independent public-analytics oracle and a practical temporal
correlation method that works without controlling the victim or short URL.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 58/100 | 25% | 14.50/25 | Novel combination of analytics deltas and social metadata. |
| Transferability | 72/100 | 20% | 14.40/20 | Applies where public per-link aggregates and user attributes overlap. |
| Lasting value | 70/100 | 20% | 14.00/20 | Durable warning about small-group leakage from aggregate telemetry. |
| Technical soundness | 86/100 | 15% | 12.90/15 | Controlled evaluations and accuracy results support the inference. |
| Practical usability | 66/100 | 10% | 6.60/10 | Requires carefully timed polling and distinguishable metadata. |
| Clarity and reproducibility | 80/100 | 10% | 8.00/10 | Data sources, algorithm and cases are clear. |

**Final score: 70.4/100.** Archive decision: include as a core technique.

### Verdict

Meaningful combination or adaptation. It creates a new privacy oracle from two
individually public data sources.

## 68.4 — [A View to a Kill: WebView Exploitation](https://www.usenix.org/conference/leet13/workshop-program/presentation/neugschwandtner) — Matthias Neugschwandtner, Martina Lindorfer and Christian Platzer

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed LEET paper published in August 2013.

### Core contribution

The work treats attacker-controlled WebView content—through a compromised server
or network injection—as a bridge into exposed native JavaScript APIs, validates
end-to-end cases and scales the review to more than 287,000 Android applications.

### Prior Art

WebView bridge risks, mobile web-to-native attacks and `addJavascriptInterface`
exploitation were public by 2011–2012. The [LEET source](https://www.usenix.org/conference/leet13/workshop-program/presentation/neugschwandtner)
adds a practical threat model, exploitable case studies and a reusable large-scale
analysis method; it is therefore not scored as the first bridge attack.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 48/100 | 25% | 12.00/25 | Meaningful analysis and exploitation over a known bridge primitive. |
| Transferability | 76/100 | 20% | 15.20/20 | Applies broadly to hybrid apps exposing native functions to web content. |
| Lasting value | 70/100 | 20% | 14.00/20 | Useful audit model for WebView trust boundaries. |
| Technical soundness | 80/100 | 15% | 12.00/15 | Case studies and a 287,000-app analysis support prevalence. |
| Practical usability | 76/100 | 10% | 7.60/10 | Threat conditions and exposed-interface tests are actionable. |
| Clarity and reproducibility | 76/100 | 10% | 7.60/10 | Method and examples are sufficiently documented. |

**Final score: 68.4/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. The bridge weakness is prior art, but the
end-to-end exploitation model and large-scale audit are distinct and reusable.

## 68.3 — [Cross-Site Scripting Attacks in Social Network APIs](https://www.ieee-security.org/TC/W2SP/2013/papers/s3p1.pdf) — Yuqing Zhang, Xiali Wang, Qihan Luo and Qixu Liu

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed W2SP paper published 24 May 2013.

### Core contribution

The paper systematises Cross-API Scripting: tainted or inconsistently encoded
REST API responses move attacker content through a social platform into third-
party applications, where a different rendering context executes it. A tool
tests eleven social networks and 143 web applications for the patterns.

### Prior Art

The paper itself records API XSS cases from 2009 and 2011 and cites 2009 reverse
cross-channel scripting. Its distinct contribution is not the first API-carried
XSS; it is the taxonomy, source-to-client context analysis and automated ecosystem
test method in the [primary W2SP paper](https://www.ieee-security.org/TC/W2SP/2013/papers/s3p1.pdf).

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 45/100 | 25% | 11.25/25 | Systematises and scales a mechanism with documented earlier instances. |
| Transferability | 78/100 | 20% | 15.60/20 | API-to-client context mismatches recur across platforms and consumers. |
| Lasting value | 72/100 | 20% | 14.40/20 | Useful framework for testing modern API ecosystems. |
| Technical soundness | 82/100 | 15% | 12.30/15 | Multi-platform tool results and root-cause analysis support the claims. |
| Practical usability | 72/100 | 10% | 7.20/10 | The test patterns are actionable though APIs require adapters. |
| Clarity and reproducibility | 76/100 | 10% | 7.60/10 | Examples, categories and experiment design are available. |

**Final score: 68.3/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. Earlier cases prevent an originality claim,
but the systematic multi-party API analysis is a qualifying contribution.

## 67.3 — [FireDrill: Interactive DNS Rebinding](https://www.usenix.org/conference/woot13/workshop-program/presentation/dai) — Yunxing Dai and Ryan Resig

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed WOOT paper published in August 2013.

### Core contribution

FireDrill floods the browser DNS cache to evict a pinned attacker hostname, then
rebinds it to an internal server and maintains an interactive session. The session
supports authentication, state changes and framing beyond one-shot requests.

### Prior Art

DNS rebinding and browser DNS pinning bypasses were established before 2013; the
original 2013 nominations even include a rebinding defense. The [WOOT paper](https://www.usenix.org/conference/woot13/workshop-program/presentation/dai)
adds cache-flood eviction against then-modern browsers and a concrete interactive
tool, rather than claiming the base attack.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 48/100 | 25% | 12.00/25 | New cache-flooding bypass and interactive implementation of old rebinding. |
| Transferability | 74/100 | 20% | 14.80/20 | Targets shared browser DNS-cache behavior and internal web services. |
| Lasting value | 68/100 | 20% | 13.60/20 | Useful extension in the evolution of rebinding bypasses. |
| Technical soundness | 78/100 | 15% | 11.70/15 | Working tool and browser experiments support the mechanism. |
| Practical usability | 76/100 | 10% | 7.60/10 | Automates an otherwise brittle attack sequence. |
| Clarity and reproducibility | 76/100 | 10% | 7.60/10 | Cache manipulation and session setup are documented. |

**Final score: 67.3/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It advances DNS rebinding through a new pin/cache bypass and
an interactive exploitation mode.

## 62.3 — [Analyzing Unique-Bid Auction Sites for Fun and Profit](https://www.ndss-symposium.org/ndss2013/ndss-2013-programme/analyzing-unique-bid-auction-sites-fun-and-profit/) — Ory Samorodnitzky, Eran Tromer and Avishai Wool

**KEPT** · Tooling or methodology contribution · confidence Medium

### Candidate

Peer-reviewed NDSS paper published 24 April 2013.

### Core contribution

The authors reconstruct hidden bidding behavior from a site's side signals,
validate an agent-based model and derive automated strategies that achieve a 91%
win rate and profit against a commercial unique-bid auction. The reusable core is
side-signal extraction plus simulation-guided abuse of web business logic.

### Prior Art

Auction game theory, bidding bots and automated strategies were known. The [NDSS
paper](https://www.ndss-symposium.org/wp-content/uploads/2017/09/11_5.pdf) adds a
specific back-propagation method for recovering temporal hidden bids, a validated
behavioral model and a demonstrated strategy. Transfer is narrower than the other
candidates, so it qualifies only in the new 60–69 band.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 48/100 | 25% | 12.00/25 | New side-signal/model workflow over established automated bidding ideas. |
| Transferability | 52/100 | 20% | 10.40/20 | Transfers to similar feedback-driven business logic, not ordinary auctions. |
| Lasting value | 56/100 | 20% | 11.20/20 | Useful case for adversarial simulation, but mechanism is specialised. |
| Technical soundness | 86/100 | 15% | 12.90/15 | Extracted data, validated model and live results substantiate the claims. |
| Practical usability | 80/100 | 10% | 8.00/10 | Automated strategy is directly operational where the same signals exist. |
| Clarity and reproducibility | 78/100 | 10% | 7.80/10 | Model, extraction and validation are explained. |

**Final score: 62.3/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It contributes a reusable method for turning
web-visible side signals into a simulation-guided business-logic exploit, although
its reach is narrower than the higher-scoring additions.

---

## 65.5 — [A Perfect CRIME? Only TIME Will Tell](https://media.blackhat.com/eu-13/briefings/Beery/bh-eu-13-a-perfect-crime-beery-wp.pdf) — Tal Be’ery and Amichai Shulman

**KEPT** · Meaningful extension · confidence Medium

Reviewed 2026-09-10.

### Candidate

- **Title:** A Perfect CRIME? Only TIME Will Tell
- **Author or organisation:** Tal Be’ery and Amichai Shulman
- **Publication date / novelty cutoff:** March 2013, Black Hat Europe technical disclosure; exact first public day not established.
- **Reference:** [Original source](https://media.blackhat.com/eu-13/briefings/Beery/bh-eu-13-a-perfect-crime-beery-wp.pdf). Full-source reading, local exclusion checks and source-specific evidence are recorded in the [dated sweep](2026-09-10-sweep.md).

### Core Contribution

Choose request lengths on either side of a TCP acknowledgement boundary so a one-byte difference changes browser-observed completion time. The demonstrated HTTP timing signal and separate compression-length recovery experiment are distinct. Their combination into network-observer-free secret extraction is explicitly future work, not a completed exploit.

### Prior Art

[Bortz, Boneh and Nandy, 2007](https://crypto.stanford.edu/~dabo/pubs/papers/webtiming.pdf) already supply browser timing and minimum-sample filtering, while excluding multi-packet requests in their experiment. [Ling et al., INFOCOM2012](https://citeseerx.ist.psu.edu/document?doi=31e7ff7312f34a08a995e5b2f08e948aae7e4995&repid=rep1&type=pdf) passively classify sites using captured SSH-tunnel RTTs; they do not supply the chosen-byte browser boundary. [Gilad and Herzberg, PETS2012](https://www.freehaven.net/anonbib/cache/tcp-tor-pets12.pdf) use spoofed active TCP probes for connection discovery. General compression-length attacks and response extraction are earlier; recovered [CRIME slides](https://docs.google.com/presentation/d/11eBmGiHbYcHR9gL5nDyZChu_-lCa2GizeuOfaLU2HOU/export/pdf) explicitly discuss response gzip, although the mutable export is not an authenticated 2012 snapshot.

**Evidence boundary:** All six categories assess the original technical disclosure and demonstrably earlier knowledge. Later copies are retrieval evidence only; uptake, subsequent patches and present-day exploitability receive no credit or penalty. The dated sweep records the local mechanism search and nomination comparison.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 65 | 25% | 16.25 | Concrete chosen-byte boundary measurement beyond passive RTT classification and active connection discovery. |
| Transferability | 65 | 20% | 13.00 | Protocol-level browser measurement, conditional on connection behavior and observable events. |
| Lasting value | 72 | 20% | 14.40 | Reusable investigation of whether restricted timing exposes length, assessed at disclosure. |
| Technical soundness | 68 | 15% | 10.20 | Code and measurements support narrow signal; separate experiments do not prove their combination. |
| Practical usability | 45 | 10% | 4.50 | Hard-coded boundaries and missing combined recovery leave substantial implementation work. |
| Clarity and reproducibility | 72 | 10% | 7.20 | Detailed explanation, logs and JavaScript support reconstruction within environment limits. |

**Final score: 65.5/100**

### Reverification

- **Facts rechecked:** The full TIME paper, full Ling paper and 43-slide CRIME deck were read during follow-up; main reviewed the source-specific comparison and reopened TIME’s AppendixB/future-work evidence.
- **Cutoff audit:** All securely dated related papers precede March2013; later BREACH/HEIST are excluded. Mutable CRIME provenance prevents a stronger priority claim.
- **Independent check:** A new TCP-boundary/acknowledgement path recovered Gilad’s active timing work and resolved Ling’s full-source comparison.
- **Strongest challenge:** Familiar timing and compression ideas, with no combined secret oracle. **Benefit-of-doubt check:** A demonstrated one-byte-to-RTT amplification remains a useful measurement primitive.
- **Changes:** Retained 65.5 only for that narrow extension; the CNN demo uses HTTP and hard-coded 2588/2589 parameters, not demonstrated HTTPS secret recovery.

### Verdict

Meaningful extension.

- **Archive decision:** Include as a supporting reference.
- **Confidence:** Medium.
- **Reasoning:** The bounded contribution described above clears the 55-point historical-addition gate; component age and familiar impact are excluded from its novelty credit.
- **Evidence gaps:** Exact cutoff day and immutable CRIME slide revision unresolved; no historical execution or independent figure-by-figure reproduction.

---

## 61.2 — [Invisibility Purge / .NET Havoc](https://media.blackhat.com/eu-13/briefings/Chen/bh-eu-13-invisibility-purge-chen-slides.pdf) — Shay Chen and Niv Sela

**KEPT** · Tooling or methodology contribution · confidence Medium

Reviewed 2026-09-11; [TECAPI source audit](2026-09-11-tecapi.md).


### Candidate

- **Title:** Invisibility Purge / .NET Havoc — Abusing ASP.net Mechanics and Overriding Properties of Server-Side Web Controls
- **Author or organisation:** Shay Chen; research with Niv Sela; SCIP implementation by Alex Mor; Hacktics ASC, Ernst & Young.
- **Publication date:** 14 March 2013 for Invisibility Purge; 12 September 2013 for the expanded .NET Havoc deck.
- **Reference:** [Invisibility Purge slides](https://media.blackhat.com/eu-13/briefings/Chen/bh-eu-13-invisibility-purge-chen-slides.pdf), [.NET Havoc original slides](https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/hasc-research/DotNetHavoc%20-%2044Con2013.pptx).

### Core Contribution

A structured testing method for server-side control events and properties that
are absent or disabled in the browser interface. The March disclosure organizes
control enumeration and event execution into a proxy extension; September adds
property-oriented testing and manipulation. The reusable contribution is the
testing coverage and explicit separation of control visibility, event validation,
state integrity, and authorization—not the discovery that client state can be
tampered with or replayed.

### Prior Art

- **Novelty cutoff:** The [Black Hat schedule](https://blackhat.com/eu-13/schedule/briefings-14.html)
  places the technical Invisibility Purge presentation on 14 March 2013; its
  original deck says March 2013. The .NET Havoc deck is dated 12 September 2013,
  corroborated by the [44CON programme](https://44con.com/44con/44con-2013/44con-2013-presentations/).
  The event-enumeration/replay work is assessed at March; the property-focused
  extension at September. They constitute one research line, not two additions.
- **Earliest credible pre-cutoff related work:** Michal Zalewski's
  [3 May 2005 original disclosure](https://marc.info/?l=bugtraq&m=111513127704270&w=2)
  already explains signed ViewState replay across compatible views and after
  state or access restrictions change. Reusing signed state is therefore not a
  new 2013 primitive.
- **Closest pre-cutoff equivalent work:** James Jardine's
  [6 February 2012 Part 1](https://www.jardinesoftware.net/2012/02/06/asp-net-tampering-with-event-validation-part-1/)
  and [10 February 2012 Part 2](https://www.jardinesoftware.net/2012/02/10/asp-net-tampering-with-event-validation-part-2/)
  show ViewState/EventValidation tampering with MAC disabled, unauthorized data
  selection, and invocation of a hidden button event. This directly anticipates
  the basic hidden-control attack, not merely its API building blocks.
- **Evidence boundary:** Read the original 65-slide March PDF and the complete
  text extracted from the September PPTX. Later VEHICLE documentation and
  mirrors were retrieval leads only. Local searches covered `eventvalidation`,
  dormant/hidden controls, ViewState, and related session mechanisms across
  the pre-cutoff archive. They supplied no closer local predecessor. LinkedIn
  project employment dates were not accepted as public technical disclosure.
- **Candidate's distinct contribution as of the cutoff:** An integrated
  control/event testing workflow with error-based enumeration, explicit control
  categories, and proxy tooling; the later deck develops control-property
  fingerprinting and injection. Property metadata and alternate event coverage
  extend Jardine's narrower parameter/hidden-button examples. The incremental
  scope warrants methodology credit, without claiming a new vulnerability class.

### Scorecard

Computed with `score.py --original 50 --transferability 55 --lasting 68 --technical 72 --practical 68 --clarity 65`.

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 50/100 | 25% | 12.50/25 | A real method/tooling extension over known tampering and replay, with more systematic control coverage. |
| Transferability | 55/100 | 20% | 11.00/20 | Useful across ASP.NET/Mono applications; control lifecycle and state-format assumptions limit cross-framework portability. |
| Lasting value | 68/100 | 20% | 13.60/20 | At publication, the explicit coverage model offers durable testing guidance beyond an individual vulnerable page. |
| Technical soundness | 72/100 | 15% | 10.80/15 | Mechanisms and configuration conditions are explained; broad bypass statements require application-specific authorization and state-binding conditions. |
| Practical usability | 68/100 | 10% | 6.80/10 | Proxy integration and enumeration make the method actionable; vulnerable handlers and compatible state are still required. |
| Clarity and reproducibility | 65/100 | 10% | 6.50/10 | Detailed attack steps and configuration examples; some demonstrations are visual and not complete standalone reproductions. |

**Final score: 61.2/100**

### Reverification

- **Earlier implementation provenance:** The [Google Code release inventory](https://storage.googleapis.com/google-code-archive/v2/code.google.com/ria-scip/downloads-page-1.json) records SCIP v1.0 artifacts on 17 February 2013, before the March presentation. The source archive was not read in this review, so this establishes earlier implementation availability, not the exact contents of the February technique. The March deck is the earliest complete technical document reviewed; none of the compared prior art falls between those dates. The year and score are unchanged.


- **Candidate facts rechecked against:** The original September deck, March
  technical PDF, and both conference programmes. Rechecked the distinction
  between current and upcoming SCIP features; cache scraping and automated
  control fingerprinting were not credited as shipped functionality.
- **Cutoff audit:** Jardine's dated 2012 posts and Zalewski's dated 2005 message
  precede both cutoffs. The March deck already contains cached signed replay
  and proposed blind enumeration; those are not counted again as September
  discoveries. No later adoption or patch history influenced any score.
- **Independent prior-art check:** After searching hidden controls and
  EventValidation, searched signed-state replay and stale privileges. This found
  Zalewski's primary disclosure and materially narrowed the originality claim.
- **Strongest challenge to the result:** Most individual exploitation primitives
  predate the talk. Treating them collectively as an original attack class would
  inflate the score. The defensible contribution is systematic testing coverage.
- **Benefit-of-doubt check:** The September property model targets server control
  metadata rather than merely changing another account ID; this is a useful
  extension even though unsigned-state tampering was already understood.
- **Changes after reverification:** Reframed the initial novelty hypothesis as a
  methodology contribution and selected supporting inclusion. Retained the
  computed 61.2 score after checking all six reasons. Historical demonstrations
  were not rerun. PDF screenshot retrieval failed; substantive conclusions rely
  on readable source text, not uninspected diagram details.

### Verdict

Tooling or methodology contribution

- **Archive decision:** Include as a supporting reference
- **Confidence:** Medium
- **Reasoning:** Systematic control/event and property testing adds useful
  coverage above known primitives and clears the historical 55-point gate.
  Preserve the March and September artifacts together, with no duplicate count.
- **Evidence gaps:** An earlier public SCIP release date has not been proved;
  both recovered technical conference disclosures are in 2013. Some property
  demonstrations require reconstructing a historical test application.


---

## 33.0 — [The Boomerang Effect](https://deepsec.net/docs/Slides/2013/DeepSec_2013_Shay_Chen_-_The_Boomerang_Effect_-_Using_Session_Puzzling_To_Attack_Apps_From_The_Backend.pdf) — Shay Chen

**REMOVED** · Duplicate or already known · confidence Medium

Reviewed 2026-09-11; [TECAPI source audit](2026-09-11-tecapi.md).


### Candidate

- **Title:** The Boomerang Effect — Using Session Puzzling to Attack Apps from the Backend
- **Author or organisation:** Shay Chen, Hacktics ASC, Ernst & Young.
- **Publication date:** 22 November 2013; the deck's title slide.
- **Reference:** [Original DeepSec slides](https://deepsec.net/docs/Slides/2013/DeepSec_2013_Shay_Chen_-_The_Boomerang_Effect_-_Using_Session_Puzzling_To_Attack_Apps_From_The_Backend.pdf).

### Core Contribution

A retrospective presentation of session-variable interference, controlled
latency for exploiting temporary state, and behavioral mapping of server state.
The question is whether this particular 2013 presentation supplies a new
contribution beyond the author's existing disclosures.

### Prior Art

- **Novelty cutoff:** Session Puzzling was technically presented on 17 May 2011,
  as the [original whitepaper](https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/puzzlemall/Session%20Puzzles%20-%20Indirect%20Application%20Attack%20Vectors%20-%20May%202011%20-%20Whitepaper.pdf)
  records; TSRC's [original presentation](https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/puzzlemall/Temporal%20Session%20Race%20Conditions%20%28TSRC%29%20-%20Sept%202011%20-%20Presentation.pptx)
  is dated 15 September 2011; Diviner's [technical author article](https://sectooladdict.blogspot.com/2012/07/the-diviner-clairvoyance-in-digital.html)
  is dated 30 July 2012. The later Boomerang artifact is dated 22 November 2013.
- **Earliest credible pre-cutoff related work:** The 2011 Session Puzzles paper,
  already preserved and cited by `2011.md`, includes authentication/flow bypass,
  indirect injection, delivery redirection, and black-box sequence testing.
- **Closest pre-cutoff equivalent work:** The original TSRC deck already supplies
  selective latency using RegEx DoS and connection-pool exhaustion. The 2012
  Diviner article already explains request-history/authentication/token scenario
  variation and conversion of observed behavior into probable code/state maps.
- **Evidence boundary:** Read all 67 slides using the original PDF and the
  independently extracted local text, the archived 2011 sources, and the original
  2012 article. No later session research or Diviner revisions were scored.
- **Candidate's distinct contribution as of the cutoff:** A consolidated
  presentation and illustrations; no demonstrated new primitive, materially new
  combination, or newly implemented method beyond those earlier disclosures.

### Scorecard

Computed with `score.py --original 10 --transferability 20 --lasting 25 --technical 70 --practical 45 --clarity 65`.

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 10/100 | 25% | 2.50/25 | Repackages the author's previously disclosed mechanisms. |
| Transferability | 20/100 | 20% | 4.00/20 | The presentation adds little transferable capability beyond its originals. |
| Lasting value | 25/100 | 20% | 5.00/20 | Modest value as a combined teaching artifact; no distinct research direction added. |
| Technical soundness | 70/100 | 15% | 10.50/15 | Coherent mechanisms; broad field examples and divination confidence figures are author claims, not independent measurements. |
| Practical usability | 45/100 | 10% | 4.50/10 | Useful survey and testing guide, with originals already offering the actionable methods. |
| Clarity and reproducibility | 65/100 | 10% | 6.50/10 | Clear sequence diagrams and examples; slide format omits some implementation details. |

**Final score: 33.0/100**

### Reverification

- **Candidate facts rechecked against:** DeepSec's original PDF title page and
  complete extracted text; the local 2011 source documents and 2012 author post.
- **Cutoff audit:** Read the actual September 2011 title-slide date, not only
  the archive directory name. The 2012 article precedes the November 2013 deck.
- **Independent prior-art check:** Specifically investigated whether Diviner was
  a new 2013 addition. Its 2012 article contains the same scenario factors,
  behavioral isolation, code inference, and beta tool disclosure.
- **Strongest challenge to the result:** Combining practical inference tooling
  with session puzzling could be a meaningful methodological advance if newly
  disclosed here. The 2012 source already explicitly connects these ideas.
- **Benefit-of-doubt check:** The deck is a useful teaching artifact; usefulness
  does not establish a new 2013 contribution or require another archive copy
  when the original technique documents are already preserved.
- **Changes after reverification:** Removed the possible Diviner-extension
  rationale after locating its earlier technical disclosure; final duplicate
  score and decision are consistent. No later uptake influenced the judgement.

### Verdict

Duplicate or already known

- **Archive decision:** Do not include
- **Confidence:** High
- **Reasoning:** The source's three technical strands were already disclosed in
  2011–2012. Preserve attribution to those original dates; do not add Boomerang
  as a new 2013 technique or as a required replacement for existing originals.
- **Evidence gaps:** No material gap for excluding this as a new 2013 technique.
  Diviner is a separate 2012 lead, not evaluated for novelty in this scorecard.
