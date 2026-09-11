# 2014 candidate judgements

These scorecards apply the repository's weighted judge rubric. `KEPT` means the
candidate met the historical 60-or-above inclusion rule as well as the
first-publication, originality-verdict and original-nomination exclusions.

## 89.0 — [Virtual Host Confusion: Weaknesses and Exploits](https://www.blackhat.com/docs/us-14/materials/us-14-Delignat-The-BEAST-Wins-Again-Why-TLS-Keeps-Failing-To-Protect-HTTP-wp.pdf) — Antoine Delignat-Lavaud, Karthikeyan Bhargavan

**KEPT** · Original technique · confidence High

### Candidate

Primary Black Hat USA whitepaper published and presented in August 2014. The
paper, conference archive and contemporaneous nginx advisory establish the date
and attribution.

### Core contribution

The work separates network, TLS-session and HTTP `Host` identities and shows
that HTTPS multiplexers often route on unauthenticated or inconsistent values.
It turns port forwarding, certificate overlap, default virtual hosts and shared
TLS session caches/ticket keys into cross-origin routing, cookie theft, XSS and
full server impersonation on nginx, Apache, IIS, CDNs and major web services.

### Prior art

Host-header attacks, DNS rebinding, TLS interception and the 2009
Pretty-Bad-Proxy attacks predate 2014. They do not define or systematically
exploit the mismatch among the identities used by HTTPS multiplexers; the paper
also explicitly distinguishes earlier fallback-server folklore.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 87 | 25% | 21.75 | Defines and demonstrates a new HTTPS routing-confusion class. |
| Transferability | 92 | 20% | 18.40 | Recurs across servers, terminators, reverse proxies and CDNs. |
| Lasting value | 91 | 20% | 18.20 | Durable model for authenticated routing across protocol layers. |
| Technical soundness | 91 | 15% | 13.65 | Precise model, multiple implementations, live exploits and fixes. |
| Practical usability | 82 | 10% | 8.20 | Direct tests and configurations are usable by HTTPS auditors. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Attack paths, assumptions and server behaviors are explicit. |

**Final score: 89.0/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It exposes a previously unsystematized authentication and
routing boundary, not merely another Host-header or TLS implementation bug.

## 88.0 — [Triple Handshakes and Cookie Cutters: Breaking and Fixing Authentication over TLS](https://www.ieee-security.org/TC/SP2014/papers/TripleHandshakesandCookieCutters_c_BreakingandFixingAuthenticationoverTLS.pdf) — Karthikeyan Bhargavan, Antoine Delignat-Lavaud, Cédric Fournet, Alfredo Pironti, Pierre-Yves Strub

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published in May
2014.

### Core contribution

The paper composes RSA/DHE handshakes, resumption and renegotiation so a
malicious TLS proxy synchronizes keys across separate connections. That breaks
channel bindings and enables client impersonation in renegotiation, tunneled
authentication and channel-bound cookies. It also develops HTTPS “cookie
cutter” truncation attacks caused by treating authenticated TLS fragments as
complete application messages.

### Prior art

The 2009 renegotiation prefix-injection flaw, TLS unknown-key shares and HTTP
truncation behavior were known separately. The triple-handshake composition,
its defeat of the secure-renegotiation fix and the resulting application-level
authentication attacks were new.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 88 | 25% | 22.00 | New multi-handshake key-synchronization and authentication attacks. |
| Transferability | 84 | 20% | 16.80 | Applies to several TLS authentication and channel-binding uses. |
| Lasting value | 91 | 20% | 18.20 | Influenced TLS extended-master-secret and channel-binding design. |
| Technical soundness | 94 | 15% | 14.10 | Formal analysis, implementations and practical attacks agree. |
| Practical usability | 78 | 10% | 7.80 | Requires an active network position but provides concrete procedures. |
| Clarity and reproducibility | 91 | 10% | 9.10 | Handshake transcripts, variants and mitigations are detailed. |

**Final score: 88.0/100.** Archive decision: include as a core technique.

### Verdict

Original technique. Earlier TLS attacks supply ingredients, but not this
three-handshake synchronization capability or its cross-protocol consequences.

## 86.8 — [Using Frankencerts for Automated Adversarial Testing of Certificate Validation in SSL/TLS Implementations](https://www.ieee-security.org/TC/SP2014/papers/UsingFrankencertsforAutomatedAdversarialTestingofCertificateValidationinSSL_s_TLSImplementations.pdf) — Chad Brubaker, Suman Jana, Baishakhi Ray, Sarfraz Khurshid, Vitaly Shmatikov

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published in May
2014.

### Core contribution

Frankencerts recombines and mutates parts of real X.509 certificates into
syntactically valid but semantically adversarial inputs, then uses disagreement
among independent validators as an oracle. More than eight million generated
certificates exposed 208 discrepancies and exploitable trust, key-usage,
constraint and browser-warning failures across major TLS libraries.

### Prior art

Certificate-validation bugs, general mutation fuzzing, differential testing
and the 2012 “Most Dangerous Code” study were established. The new contribution
is a structure-aware X.509 generator plus cross-validator oracle that makes
deep semantic certificate testing automatic and scalable.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78 | 25% | 19.50 | Novel certificate-specific adversarial generation and oracle. |
| Transferability | 88 | 20% | 17.60 | Applies to TLS libraries, browsers and other X.509 consumers. |
| Lasting value | 89 | 20% | 17.80 | Canonical example of structured differential security testing. |
| Technical soundness | 96 | 15% | 14.40 | Millions of tests, manual triage and vendor-confirmed flaws. |
| Practical usability | 82 | 10% | 8.20 | Automates a previously expensive validation audit. |
| Clarity and reproducibility | 93 | 10% | 9.30 | Generator, oracle, corpus and findings are fully explained. |

**Final score: 86.8/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It does not invent certificate-validation
failure, but introduces a powerful reusable way to find it.

## 86.7 — [Relative Path Overwrite](http://www.thespanner.co.uk/2014/03/21/rpo/) — Gareth Heyes

**KEPT** · Original technique · confidence High

### Candidate

Researcher post dated 21 March 2014. Later academic work explicitly identifies
this post as the first RPO disclosure. The technique appeared in the following
year's nominations, but was absent from the original 2014 round.

### Core contribution

RPO exploits a semantic mismatch: a server accepts added path segments while a
browser resolves relative stylesheet URLs from the attacker-modified base URL.
The page can therefore load its own HTML response as same-origin CSS; quirks-mode
CSS parsing and reflected content then enable scriptless injection and data
exfiltration without a conventional stylesheet-upload sink.

### Prior art

CSS injection, content sniffing, path-info quirks and relative URLs were known.
No earlier source located combined tolerant server routing and browser-relative
resource resolution into this same-origin self-inclusion primitive.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 84 | 25% | 21.00 | New browser/server path-confusion exploitation primitive. |
| Transferability | 88 | 20% | 17.60 | General to many stacks with flexible paths and relative CSS. |
| Lasting value | 91 | 20% | 18.20 | Seeded a durable path-confusion research and testing family. |
| Technical soundness | 82 | 15% | 12.30 | Mechanism and examples are correct, though the post is compact. |
| Practical usability | 92 | 10% | 9.20 | Simple URL mutations and response checks make it highly actionable. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Payload construction and browser preconditions are demonstrated. |

**Final score: 86.7/100.** Archive decision: include as a core technique.

### Verdict

Original technique. The reusable contribution is the two-parser path mismatch
that creates an attacker-controlled same-origin stylesheet load.

## 85.8 — [Breaking and Fixing Origin-Based Access Control in Hybrid Web/Mobile Application Frameworks](https://www.ndss-symposium.org/ndss2014/ndss-2014-programme/breaking-and-fixing-origin-based-access-control-hybrid-webmobile-application-frameworks/) — Martin Georgiev, Suman Jana, Vitaly Shmatikov

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed NDSS paper published on 22 February 2014.

### Core contribution

The paper shows that hybrid frameworks fail to compose browser-origin policy
with operating-system permissions. Foreign Web content, such as an ad iframe,
can invoke privileged native bridges and “frack” through the layers to contacts,
files, camera and other device resources. The attack is demonstrated across
frameworks, bridge designs and platforms, with prevalence analysis and a
capability-based defense.

### Prior art

WebView bridge bugs, same-origin violations and confused deputies existed.
Earlier work did not identify the generic policy-composition failure spanning
foreign Web frames, hybrid bridges and whole-application native permissions.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 84 | 25% | 21.00 | New generic “fracking” attack class across hybrid stacks. |
| Transferability | 88 | 20% | 17.60 | Applies across frameworks, embedded browsers and mobile OSes. |
| Lasting value | 84 | 20% | 16.80 | Durable warning about composing Web and native authority. |
| Technical soundness | 92 | 15% | 13.80 | Mechanism, cross-platform tests and population study align. |
| Practical usability | 78 | 10% | 7.80 | Clear malicious-content tests, with app-specific bridge details. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Threat model, examples and defense are explicit. |

**Final score: 85.8/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It turns a systemic cross-layer authorization mismatch into
a reusable attack rather than cataloguing isolated WebView bugs.

## 85.2 — [Static Detection of Second-Order Vulnerabilities in Web Applications](https://www.usenix.org/conference/usenixsecurity14/technical-sessions/presentation/dahse) — Johannes Dahse, Thorsten Holz

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2014.

### Core contribution

The analysis connects attacker-controlled writes to later reads from databases,
sessions and other persistent stores, then follows the retrieved value to a
security-sensitive sink. This makes multi-request, second-order XSS, SQL
injection and command-execution flows statically visible. Evaluation found 159
previously unknown vulnerabilities across six applications, including flaws
missed by earlier analyzers.

### Prior art

Stored/second-order injection and static taint analysis were known. Prior tools
usually treated persistent-store reads as either trusted or indiscriminately
tainted; they did not pair writes and reads at storage locations to reconstruct
multi-step exploit flows at this scale.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 75 | 25% | 18.75 | New storage-aware static analysis for second-order flows. |
| Transferability | 88 | 20% | 17.60 | Covers multiple stores, sinks and vulnerability classes. |
| Lasting value | 89 | 20% | 17.80 | Durable model for persistent taint and multi-step exploits. |
| Technical soundness | 94 | 15% | 14.10 | Large real-code evaluation and confirmed findings. |
| Practical usability | 80 | 10% | 8.00 | Produces actionable flows and scales to substantial PHP apps. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Analysis, assumptions, evaluation and limitations are detailed. |

**Final score: 85.2/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. The bug family predates the paper; its
precise persistent-store connection method is the qualifying advance.

## 85.1 — [All Your Screens Are Belong to Us: Attacks Exploiting the HTML5 Screen Sharing API](https://www.ieee-security.org/TC/SP2014/papers/AllYourScreensareBelongtoUs_c_AttacksExploitingtheHTML5ScreenSharingAPI.pdf) — Yuan Tian, Ying-Chuan Liu, Amar Bhosale, Lin-Shung Huang, Patrick Tague, Collin Jackson

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published in May
2014.

### Core contribution

HTML5 screen sharing creates a visual cross-origin feedback channel. A sharing
site can force authenticated cross-origin pages onscreen, flash or blend them
below human perception, then capture secrets, CSRF tokens, history and autofill
content from pixels. The work shows why SOP, frame busting, third-party-cookie
controls and conventional CSRF defenses do not close this channel.

### Prior art

Shoulder surfing, clickjacking, pixel stealing and history sniffing were known.
They did not use the screen-sharing stream as a programmable cross-origin read
oracle combined with attacker-controlled navigation and human visual limits.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 88 | 25% | 22.00 | New visual feedback primitive that bypasses origin isolation. |
| Transferability | 86 | 20% | 17.20 | General to screen-sharing APIs and sensitive visual content. |
| Lasting value | 81 | 20% | 16.20 | Influential lesson for capture APIs and permission UX. |
| Technical soundness | 90 | 15% | 13.50 | Multiple attacks, sites, browsers and defense analysis. |
| Practical usability | 74 | 10% | 7.40 | Requires sharing permission but attacks then need little interaction. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Timings, layouts, attack flows and limits are clear. |

**Final score: 85.1/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It identifies screen capture itself as a cross-origin
feedback oracle, beyond ordinary clickjacking or pixel-history attacks.

## 81.7 — [Password Managers: Attacks and Defenses](https://www.usenix.org/conference/usenixsecurity14/technical-sessions/presentation/silver) — David Silver, Suman Jana, Dan Boneh, Eric Chen, Collin Jackson

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2014.

### Core contribution

The paper models password-manager autofill policies and shows that origin,
frame and interaction choices can let a remote network attacker silently
extract multiple stored passwords. It evaluates built-in, mobile and third-party
managers, demonstrates attacks, and proposes deployable policy changes.

### Prior art

Autofill and autocomplete theft had been demonstrated, including browser
attacks nominated in 2010. This work extends them into a systematic policy model
covering password managers, frames and remote network manipulation, and shows
multi-credential extraction without user interaction.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 72 | 25% | 18.00 | Materially deepens known autofill abuse into a policy attack family. |
| Transferability | 85 | 20% | 17.00 | Applies across built-in, mobile and third-party managers. |
| Lasting value | 82 | 20% | 16.40 | Durable guidance for password-manager origin and interaction policy. |
| Technical soundness | 90 | 15% | 13.50 | Comparative experiments and demonstrated attacks support claims. |
| Practical usability | 80 | 10% | 8.00 | Policies and attack conditions translate directly into tests. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Threat model, manager behavior and defenses are explicit. |

**Final score: 81.7/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It does not invent autofill theft, but produces a broader,
reusable and remotely exploitable password-manager policy model.

## 80.9 — [An Expressive Model for the Web Infrastructure: Definition and Application to the BrowserID SSO System](https://www.ieee-security.org/TC/SP2014/papers/AnExpressiveModelfortheWebInfrastructure_c_DefinitionandApplicationtotheBrowserIDSSOSystem.pdf) — Daniel Fett, Ralf Küsters, Guido Schmitz

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published in May
2014.

### Core contribution

The work defines a comprehensive Dolev–Yao-style model spanning DNS, HTTP,
cookies, origins, storage, AJAX and cross-document messaging, then uses it to
analyze Mozilla BrowserID. It discovers critical SSO flaws outside prior models,
states precise security properties and proves the repaired protocol for a
defined deployment setting.

### Prior art

Formal WebSpi-style models and symbolic protocol analysis predate 2014. The
qualifying contribution is the substantially more faithful browser/Web model
and its ability to expose real multi-component SSO attacks missed by earlier
abstractions.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 70 | 25% | 17.50 | Materially more expressive web-security model with new findings. |
| Transferability | 90 | 20% | 18.00 | Models standards and mechanisms shared by many Web protocols. |
| Lasting value | 88 | 20% | 17.60 | Became a foundation for rigorous analysis of web systems. |
| Technical soundness | 96 | 15% | 14.40 | Formal definitions, proofs and vendor-fixed flaws. |
| Practical usability | 52 | 10% | 5.20 | Expert-intensive and not automated, but usable for protocol review. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Model and BrowserID reasoning are thoroughly specified. |

**Final score: 80.9/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It advances rigorous offensive protocol
analysis even though the artifact is a formal model rather than a scanner.

## 79.6 — [S3: A Symbolic String Solver for Vulnerability Detection in Web Applications](https://trinhmt.github.io/home/S3/ccs14-trinh.pdf) — Minh-Thai Trinh, Duc-Hiep Chu, Joxan Jaffar

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed ACM CCS paper published in November 2014; the linked author copy
matches the official program and proceedings record.

### Core contribution

S3 provides a symbolic string constraint language covering widespread
JavaScript-style operations. It converts regular-expression membership into
string equations and uses bounded instance generation to solve constraints
needed by dynamic symbolic execution. On practical Web-analysis benchmarks it
returns more definitive answers and is roughly twenty times faster than the
evaluated state of the art.

### Prior art

Hampi, Kaluza, Kudzu, Z3-str and other string solvers already supported Web
vulnerability analysis. S3 contributes a different symbolic encoding and
instance-generation algorithm with broader operation coverage and materially
better robustness and performance, not a new injection class.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 66 | 25% | 16.50 | New solver algorithm and expressive operation coverage. |
| Transferability | 84 | 20% | 16.80 | Useful across symbolic Web analyses and multiple bug classes. |
| Lasting value | 81 | 20% | 16.20 | Advances reusable string reasoning for exploit generation. |
| Technical soundness | 91 | 15% | 13.65 | Formal algorithm and benchmark comparison support the claims. |
| Practical usability | 75 | 10% | 7.50 | Integrates with analysis pipelines but requires specialist setup. |
| Clarity and reproducibility | 89 | 10% | 8.90 | Language, algorithm and benchmark methodology are detailed. |

**Final score: 79.6/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. Its novelty lies in making known symbolic
vulnerability-analysis ideas substantially more expressive and tractable.

## 77.4 — [MACE: Detecting Privilege Escalation Vulnerabilities in Web Applications](https://research.ibm.com/publications/mace-detecting-privilege-escalation-vulnerabilities-in-web-applications) — Maliheh Monshizadeh, Prasad Naldurg, V. N. Venkatakrishnan

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed ACM CCS paper published on 3 November 2014. The IBM publication
record and author paper agree on date, authorship and content.

### Core contribution

MACE infers an application's implicit authorization policy from code and checks
authorization-context consistency around sensitive resources. It identifies
missing or inconsistent checks that enable horizontal privilege escalation and
finds serious unknown flaws in five of seven large Web applications.

### Prior art

Broken object-level authorization, role inconsistencies and static access-control
analysis were established, including a 2011 static detector. MACE adds a
resource- and context-consistency abstraction specifically capable of finding
same-role, cross-user horizontal escalation without a supplied policy.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 65 | 25% | 16.25 | New context-consistency method for horizontal escalation. |
| Transferability | 82 | 20% | 16.40 | General to applications with repeated authorization patterns. |
| Lasting value | 80 | 20% | 16.00 | Durable model for policy-free authorization analysis. |
| Technical soundness | 88 | 15% | 13.20 | Program analysis and real-code findings substantiate the method. |
| Practical usability | 70 | 10% | 7.00 | Automates weeks of review but requires source and modeling. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Definitions, algorithm and evaluation are well documented. |

**Final score: 77.4/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. The vulnerability class is known; the
policy-free horizontal-consistency analysis is the distinct advance.

## 76.7 — [Revisiting SSL/TLS Implementations: New Bleichenbacher Side Channels and Attacks](https://www.usenix.org/conference/usenixsecurity14/technical-sessions/presentation/meyer) — Christopher Meyer, Juraj Somorovsky, Eugen Weiss, Jörg Schwenk, Sebastian Schinzel, Erik Tews

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2014.

### Core contribution

The paper finds four new PKCS#1 conformance oracles in JSSE, OpenSSL and
hardware TLS accelerators. Three support practical recovery of TLS premaster
secrets, including the first reported timing-based Bleichenbacher attacks on TLS
and a modified algorithm for an unusual `0x??02` oracle.

### Prior art

Bleichenbacher's adaptive chosen-ciphertext attack dates to 1998, and TLS had
long prescribed indistinguishable error handling. The 2014 contribution is a
new set of subtle error/timing oracles, evidence that prescribed fixes still
leak, and an algorithmic adaptation that makes one nonstandard oracle usable.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 64 | 25% | 16.00 | New practical oracles and algorithm variant for a known attack. |
| Transferability | 75 | 20% | 15.00 | Relevant across software and hardware TLS implementations. |
| Lasting value | 79 | 20% | 15.80 | Reinforced oracle testing and informed later ROBOT-style work. |
| Technical soundness | 93 | 15% | 13.95 | Realistic measurements and successful key recovery. |
| Practical usability | 70 | 10% | 7.00 | Query-intensive but operational over real networks. |
| Clarity and reproducibility | 89 | 10% | 8.90 | Oracles, algorithms, query counts and timing are explicit. |

**Final score: 76.7/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It does not rediscover Bleichenbacher; it exposes and
operationalizes new TLS side channels despite standard countermeasures.

## 76.2 — [A Web Traffic Analysis Attack Using Only Timing Information](https://arxiv.org/abs/1410.2087) — Saman Feghhi, Douglas J. Leith

**KEPT** · Original technique · confidence Medium

### Candidate

Primary author preprint submitted on 8 October 2014. The dated version contains
the complete attack and evaluation; no earlier public version was located.

### Core contribution

The attacker fingerprints encrypted Web activity using only uplink packet
timings. It does not require packet sizes, fetch boundaries or a single isolated
page load and therefore survives padding defenses aimed at length features.
Experiments on wired and wireless streams report mean success above 90 percent.

### Prior art

Website fingerprinting using packet size, sequence and sometimes timing was
well established. The distinct primitive is discarding size and explicit
start/end boundaries and classifying continuous traffic from uplink timings
alone, changing which defenses and collection assumptions matter.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 70 | 25% | 17.50 | New timing-only, boundary-free encrypted-Web fingerprint. |
| Transferability | 79 | 20% | 15.80 | Applies across encrypted wired, wireless and VPN-like traffic. |
| Lasting value | 75 | 20% | 15.00 | Durable lesson that padding size alone leaves timing leakage. |
| Technical soundness | 82 | 15% | 12.30 | Coherent method and experiments, though preprint evidence is narrower. |
| Practical usability | 72 | 10% | 7.20 | Passive collection is realistic but training is required. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Features, stream handling and evaluation are sufficiently detailed. |

**Final score: 76.2/100.** Archive decision: include as a core technique.

### Verdict

Original technique. Earlier fingerprinting used richer traces or discrete page
loads; the timing-only continuous-stream oracle is a distinct capability.

## 75.9 — [Toward Black-Box Detection of Logic Flaws in Web Applications](https://www.ndss-symposium.org/ndss2014/ndss-2014-programme/toward-black-box-detection-logic-flaws-web-applications/) — Giancarlo Pellegrino, Davide Balzarotti

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed NDSS paper published on 22 February 2014.

### Core contribution

The method learns behavioral patterns from a small number of normal user
network traces, creates an application model, and generates targeted deviations
for common logic-attack scenarios without source code. Testing seven commerce
applications found ten previously unknown severe logic flaws.

### Prior art

Black-box scanners, model-based testing, BLOCK and NoTamper predate this work.
Those approaches target parameters or state invariants differently; this paper
learns functionality-specific behavioral patterns from example interactions to
drive attack generation against otherwise application-specific logic.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 62 | 25% | 15.50 | Distinct trace-learned model for black-box logic testing. |
| Transferability | 78 | 20% | 15.60 | Applicable to many workflow-heavy applications without source. |
| Lasting value | 78 | 20% | 15.60 | Useful bridge from examples to targeted business-logic tests. |
| Technical soundness | 88 | 15% | 13.20 | Concrete algorithm and ten new real-world findings. |
| Practical usability | 74 | 10% | 7.40 | Requires representative traces but avoids source instrumentation. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Learning, mutations and evaluation are clearly described. |

**Final score: 75.9/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It extends prior black-box analysis with a
new way to learn and perturb application-specific behavior.

## 75.1 — [SSOScan: Automated Testing of Web Applications for Single Sign-On Vulnerabilities](https://www.usenix.org/conference/usenixsecurity14/technical-sessions/presentation/zhou) — Yuchen Zhou, David Evans

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2014.

### Core contribution

SSOScan automatically probes black-box sites that integrate Facebook SSO for
five serious authentication and authorization failures. It identifies SSO use,
constructs protocol manipulations, and scales the checks to the top 20,000
sites, finding at least one serious flaw in more than 20 percent of the 1,660
Facebook-SSO sites observed.

### Prior art

OAuth/SSO logic flaws and traffic-guided analysis were established by 2012,
and the five tested bug patterns were not all new. The qualifying contribution
is reliable black-box automation and Internet-scale application of protocol
misuse tests that had previously required expert manual work.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 55 | 25% | 13.75 | Automates known and emerging SSO misuse patterns. |
| Transferability | 82 | 20% | 16.40 | Method generalizes to many relying-party integrations. |
| Lasting value | 76 | 20% | 15.20 | Established scalable black-box SSO conformance testing. |
| Technical soundness | 86 | 15% | 12.90 | Large crawl, validation and prevalence evidence. |
| Practical usability | 82 | 10% | 8.20 | Removes source access and much manual protocol work. |
| Clarity and reproducibility | 87 | 10% | 8.70 | Checks, architecture and study population are explicit. |

**Final score: 75.1/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It is not a new SSO flaw class, but it
makes serious relying-party logic failures automatically testable at scale.

## 73.0 — [Detecting Logic Vulnerabilities in E-Commerce Applications](https://www.ndss-symposium.org/ndss2014/ndss-2014-programme/detecting-logic-vulnerabilities-e-commerce-applications/) — Fangqi Sun, Liang Xu, Zhendong Su

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed NDSS paper published on 22 February 2014.

### Core contribution

The paper formulates a general checkout invariant: order ID, total, merchant ID
and currency must retain integrity and authenticity across merchant and cashier
flows. A PHP symbolic-execution and taint-analysis framework checks that
invariant across modules and finds eleven previously unknown exploitable payment
logic flaws.

### Prior art

The 2011 “How to Shop for Free Online” work systematized multi-party payment
binding attacks, and symbolic/taint analysis was established. This paper's
advance is turning those payment-state lessons into a source-level invariant and
automated static detector; it is not a new payment attack family.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 59 | 25% | 14.75 | First static invariant checker for checkout-state bindings. |
| Transferability | 72 | 20% | 14.40 | General across payment modules sharing the four critical fields. |
| Lasting value | 77 | 20% | 15.40 | Durable translation of business invariants into security analysis. |
| Technical soundness | 90 | 15% | 13.50 | Symbolic implementation and eleven new validated flaws. |
| Practical usability | 65 | 10% | 6.50 | Requires PHP source and framework support, but automates review. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Invariant, flow tracking and evaluation are clearly presented. |

**Final score: 73.0/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. The attacks have prior art; the reusable
payment-invariant detector is new.

## 72.6 — [Same Origin Method Execution (SOME)](http://www.benhayak.com/2015/06/same-origin-method-execution-some.html) [Whitepaper](https://www.blackhat.com/docs/eu-14/materials/eu-14-Hayak-Same-Origin-Method-Execution-Exploiting-A-Callback-For-Same-Origin-Policy-Bypass-wp.pdf) — Ben Hayak

**KEPT** · Original technique · confidence High

### Candidate

Primary Black Hat Europe whitepaper and presentation published in October 2014;
the linked researcher retrospective was posted in 2015. This is a fresh
reassessment of the existing missed-list entry.

### Core contribution

SOME turns a permissive JSONP callback into execution of attacker-chosen
same-origin DOM methods. Timed windows and frames let an attacker invoke a
sequence of authenticated application actions without clicks, frameability or
script injection on the target page, expanding one callback weakness to the
whole origin's exposed method surface.

### Prior art

JSONP callback injection, CSRF, clickjacking and frame choreography were known.
The new primitive is treating callback-controlled property paths and calls as a
general method-execution capability, then composing it into interaction-free
same-origin workflows.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 68 | 25% | 17.00 | New general method-execution framing of unsafe JSONP callbacks. |
| Transferability | 78 | 20% | 15.60 | Applies wherever callback names resolve through callable object paths. |
| Lasting value | 72 | 20% | 14.40 | Continues to inform JSONP and callback validation testing. |
| Technical soundness | 82 | 15% | 12.30 | Multiple demonstrations support the browser mechanics. |
| Practical usability | 66 | 10% | 6.60 | Requires a suitable callback and careful window sequencing. |
| Clarity and reproducibility | 67 | 10% | 6.70 | The mechanism is reproducible, though presentation is less systematic. |

**Final score: 72.6/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It creates a generalized same-origin method-call primitive,
not merely another CSRF payload or ordinary JSONP data leak.

## 71.9 — [Effective Attacks and Provable Defenses for Website Fingerprinting](https://www.usenix.org/conference/usenixsecurity14/technical-sessions/presentation/wang_tao) — Tao Wang, Xiang Cai, Rishab Nithyanand, Rob Johnson, Ian Goldberg

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2014.

### Core contribution

The attack uses a weighted large-feature k-nearest-neighbor classifier to
identify Web pages through Tor. It operates in a large open world, cuts the
false-positive rate from 6 percent to 0.6 percent at comparable true-positive
rates, trains far faster, and remains effective against several defenses.

### Prior art

Website fingerprinting, packet-sequence classifiers and open-world evaluation
all predate 2014. This contribution materially improves the classifier,
feature weighting, scale and low-base-rate reliability but remains within the
established traffic-fingerprinting mechanism.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 55 | 25% | 13.75 | Strong classifier and evaluation advance within a known family. |
| Transferability | 70 | 20% | 14.00 | Applies across Tor and other encrypted proxy traffic. |
| Lasting value | 72 | 20% | 14.40 | Influential baseline for realistic website-fingerprinting work. |
| Technical soundness | 93 | 15% | 13.95 | Careful open-world experiments and defense comparisons. |
| Practical usability | 68 | 10% | 6.80 | Passive and efficient, though it needs representative training traces. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Features, classifier, data and limitations are detailed. |

**Final score: 71.9/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. The attack family is old, but the low-false-positive,
large-open-world capability is a substantial practical step.

## 71.0 — [The Emperor's New Password Manager: Security Analysis of Web-based Password Managers](https://www.usenix.org/conference/usenixsecurity14/technical-sessions/presentation/li_zhiwei) — Zhiwei Li, Warren He, Devdatta Akhawe, Dawn Song

**KEPT** · Meaningful combination or adaptation · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2014.

### Core contribution

The study maps four attack surfaces—bookmarklets, conventional Web flaws, logic
failures and UI errors—across five Web-based password managers. It chains origin
and authorization mistakes in one-time passwords, credential sharing,
bookmarklets and vault applications to recover credentials for arbitrary sites
from four products, then derives architectural anti-patterns.

### Prior art

XSS, CSRF, password-manager abuse, weak client-side crypto and bookmarklet
origin hazards were individually known. The work's value is the systematic
cross-feature threat model and the demonstrated combinations that turn those
primitives into whole-vault compromise; it does not establish one wholly new
attack class.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 58 | 25% | 14.50 | New systematic attack surface and several non-obvious chains. |
| Transferability | 74 | 20% | 14.80 | Anti-patterns recur across Web-based manager architectures. |
| Lasting value | 71 | 20% | 14.20 | Durable defense-in-depth and vault-boundary lessons. |
| Technical soundness | 83 | 15% | 12.45 | Attacks were verified and responsibly disclosed across products. |
| Practical usability | 68 | 10% | 6.80 | Useful review framework, though exploits vary by implementation. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Threat model, product behaviors and attack categories are clear. |

**Final score: 71.0/100.** Archive decision: include as a core technique.

### Verdict

Meaningful combination or adaptation. Known Web primitives are assembled into
a reusable security model and severe password-manager compromise paths.

## 65.4 — [Bypassing HTTP Strict Transport Security](https://blackhat.com/docs/eu-14/materials/eu-14-Selvi-Bypassing-HTTP-Strict-Transport-Security-wp.pdf) — Jose Selvi

**KEPT** · Meaningful extension · confidence High

### Candidate

Primary Black Hat Europe whitepaper and presentation published in October 2014.

### Core contribution

An active network attacker forges unauthenticated NTP responses to push a
victim's clock beyond stored HSTS expiry, then applies SSL stripping. The
Delorean proof-of-concept advances time in increments that operating systems
accept and the browser study shows that most tested preloaded entries were
finite and could also expire; Safari's static treatment was the exception.

### Prior art

SSL stripping dates to 2009, HSTS/ForceHTTPS are older, and the 2012 HSTS draft
explicitly warns that a manipulated clock can make policy less effective. The
new work operationalizes that warning through NTP, tooling, OS behavior and the
unexpected finite-preload finding. Novelty is therefore deliberately modest.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 42 | 25% | 10.50 | Operational extension of a risk already named by the specification. |
| Transferability | 73 | 20% | 14.60 | Applies across several OS/browser combinations and HSTS sites. |
| Lasting value | 63 | 20% | 12.60 | Useful clock/trust-composition lesson, though implementations evolved. |
| Technical soundness | 78 | 15% | 11.70 | Demonstrations and browser comparison support bounded claims. |
| Practical usability | 76 | 10% | 7.60 | Delorean makes the network-time manipulation directly testable. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Packet fields, stepping logic, browser behavior and limits are shown. |

**Final score: 65.4/100.** Archive decision: include as qualifying supporting material.

### Verdict

Meaningful extension. The clock-expiry idea has explicit prior art, but the NTP
workflow, tool and preload analysis create a materially more actionable attack.

## 66.8 — [Do not trust me: Using malicious IdPs for analyzing and attacking Single Sign-On](https://arxiv.org/pdf/1412.1623v1) — Christian Mainka, Vladislav Mladenov, Jörg Schwenk

**KEPT** · Meaningful extension · confidence Medium

Evaluated 2026-09-10.

### Candidate

Full original v1 read, including evaluation, availability statement and appendix. [Version metadata](https://arxiv.org/abs/1412.1623) establishes 4 December 2014. Component fixes appeared during 2014, including Drupal's January advisory; that advisory does not disclose the complete session-overwrite procedure. The judgement uses the 2014 technical boundary, excludes the later expanded paper and credits no later uptake. Exact first disclosure of every component within 2014 is uncertain. URL and semantic checks against `2014.md` passed.

### Core Contribution

A hostile OpenID provider exercises discovery, association and token validation. The substantive extensions are (1) delaying a token while a second login overwrites session identity/provider state, bypassing rediscovery while retaining the attacker's key handle, and (2) supplying victim local identity through attacker-controlled discovery despite successful verification of the attacker's token. The paper supplies concrete Drupal, Sourceforge and ownCloud flows plus configurable testing profiles. These are web authentication attacks; they require the relevant inconsistent trust bindings, not a cryptographic break.

### Prior Art

Local searches covered OpenID association poisoning, discovery identity, concurrent login and SSO testing in the pre-2014 archive. The following comparisons restrict novelty:

- [Arnott, 8 March 2009](https://blog.nerdbank.net/2009/03/08/openid-association-poisoning/) already gives the malicious-provider association-handle overwrite attack. KC strategy 1 and the purported new attacker model receive no originality credit. The 2010 van Delft/Oostdijk survey repeats it with an unnecessarily stronger interception assumption.
- [Drupal's February 2011 discovery discussion](https://www.drupal.org/project/drupal/issues/575810) already identifies forged local-identity mapping after intercepted discovery. The residual 2014 adaptation serves the attacker's own metadata and needs no interception of the victim's discovery.
- The archived 2012 traffic-guided SSO paper and [2014 SSOScan](https://www.usenix.org/conference/usenixsecurity14/technical-sessions/presentation/zhou), especially its §3.3 replay tests, establish active SSO testing. A [January 2010 OpenID framework proposal](https://lists.openid.net/pipermail/openid-general/2010-January/019887.html) even explicitly requests automated association-poisoning tests and names existing security tests. Generic hostile-provider testing is therefore not new; the particular concurrent-state bypass and reproducible expanded profiles are the increment.

### Scorecard

| Category | Score | Weight | Weighted score | Publication-time reason |
|---|---:|---:|---:|---|
| Original contribution | 53 | 25% | 13.25 | Major novelty claims have exact prior art; concurrent-state and discovery adaptations remain substantive. |
| Transferability | 68 | 20% | 13.60 | Correlated issuer/key/identity checks and session state recur across SSO implementations. |
| Lasting value | 70 | 20% | 14.00 | Detailed adversarial flows and reusable profiles support subsequent audits without relying on later adoption. |
| Technical soundness | 81 | 15% | 12.15 | White-box analysis and black-box account-access checks support the bounded mechanisms across 11 of 16 tested implementations. |
| Practical usability | 61 | 10% | 6.10 | Reconstructible procedure, but provider setup and no verified public tool release at v1 impose effort. |
| Clarity and reproducibility | 77 | 10% | 7.70 | Message sequences and state transitions are explicit; the suite is promised on acceptance despite the abstract's availability claim. |

**Final score: 66.8/100.** Computed with `score.py 53 68 70 81 61 77`.

### Reverification

Fresh backward searches for concurrent OpenID login/key attacks and OpenID testing found the 2010 framework proposal, further narrowing methodology credit. Reopened the candidate's §7.2 session overwrite and §8 availability descriptions, and the earlier SSOScan replay procedure. Strongest objection: the paper packages known trust-binding failures and overclaims four new classes. Strongest favorable case: its concrete concurrent-state bypass defeats an otherwise effective rediscovery check, and the attacker-owned discovery route removes a prior network prerequisite. No claim of first-ever malicious IdP or all-new tooling survives this check. The procedure, rather than vulnerable-site counts, clears the 55-point gate.

### Verdict

Meaningful extension. Keep the distinct validation-bypass compositions, with explicit deduction for the already published poisoning primitive and earlier testing work.

---

## 62.3 — [EL 3.0/Lambda Injection: Hacker Friendly Java](https://sectooladdict.blogspot.com/2014/12/el-30-injection-java-is-getting-hacker.html) — Shay Chen

**KEPT** · Meaningful extension · confidence Medium

Reviewed 2026-09-11; [TECAPI source audit](2026-09-11-tecapi.md).


### Candidate

- **Title:** EL 3.0/Lambda Injection: Hacker Friendly Java
- **Author or organisation:** Shay Chen
- **Publication date:** 17 December 2014
- **Reference:** [Original post](https://sectooladdict.blogspot.com/2014/12/el-30-injection-java-is-getting-hacker.html)

### Core Contribution

An expression evaluator's default capabilities determine the consequences of injecting into it. Chen demonstrates Java EL3 access to useful static classes without application-specific EL imports, and uses its sequence operator to append execution to an existing expression. The reusable addition is a simpler exploitation route in the standard EL3 evaluator. Generic expression injection and command execution were already known. The source distinguishes unsafe application code from a Java vulnerability; its unnamed production findings remain author claims.

### Prior Art

- **Novelty cutoff:** 17 December 2014, the dated original technical post. No earlier candidate-side disclosure was located. Its later comments are excluded.
- **Earliest credible pre-cutoff related work:** Di Paola and Dabirsiaghi's [Expression Language Injection announcement](https://blog.mindedsecurity.com/2011/09/expression-language-injection.html), 12 September 2011, and the complete [paper preserved locally](../../archived-references/md/2011/expression-language-injection.md). It describes double evaluation, scope disclosure and blind inference, while identifying static access as a limitation of that environment.
- **Closest pre-cutoff equivalent work:** Brandon Perry's [Theoretical vulnerabilities using the Spring Expression Language](https://volatile-minds.blogspot.com/2012/09/theoritical-vulnerabilities-using.html), 12 September 2012, already demonstrates direct Runtime execution and escaping a surrounding string with expression operators. It uses SpEL, not standard EL3. Dan Amodio's December 2012 [Remote Code with Expression Language Injection](http://danamodio.com/application-security/discoveries/spring-remote-code-with-expression-language-injection/) demonstrates EL2.2 method invocation and remote class loading; its seven-page original text was read in a [preserved copy](https://www.slideshare.net/slideshow/remote-codewithexpressionlanguageinjection/24272376). The exact December day is uncertain from the available copies, but its pre-2014 existence is additionally corroborated by Arteau's November 2014 citation.
- **Evidence boundary:** Only the technical body of the dated candidate was scored. Amodio's original text is a mirror of the author publication, not the platform's generated summary. Current Oracle API pages were consulted as retrieval/context leads but carry 2015 copyrights and were not used to establish pre-cutoff novelty. Local mechanism searches covered expression language, ScriptEngine and related Java exploitation in 2006–2014. Later Minded Security articles and modern JNDI payloads were excluded.
- **Candidate's distinct contribution as of the cutoff:** An incremental standard-EL3 route that removes the older EL2.2 class-loader construction and uses native sequencing. It does not originate Java expression RCE, quote breakouts or blind injection. Existing API functionality is background; the security application is the contribution being compared.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 52/100 | 25% | 13.00/25 | Real simplification and adaptation to EL3; comparable execution and breakout capabilities existed in other expression environments. |
| Transferability | 62/100 | 20% | 12.40/20 | Applies across applications using the standard evaluator with attacker-controlled expressions. |
| Lasting value | 65/100 | 20% | 13.00/20 | Default imports and expression composition provide reusable review and testing questions. |
| Technical soundness | 70/100 | 15% | 10.50/15 | Concrete narrow mechanism; broad security-intent framing and unnamed application claims do not establish wider prevalence. |
| Practical usability | 68/100 | 10% | 6.80/10 | Straightforward probes and API sinks, conditional on input reaching EL evaluation. |
| Clarity and reproducibility | 66/100 | 10% | 6.60/10 | Payloads and servlet examples explain the method, but two concatenation examples contain quote/parenthesis transcription errors. |

**Final score: 62.3/100**

### Reverification

- **Candidate facts rechecked against:** The entire original post, fetched again directly and compared with the web rendering; its byline, date, examples, limitations and comments were checked separately.
- **Cutoff audit:** The 2011 announcement establishes the paper's public date; Perry's page displays 12 September 2012. Amodio's precise day is unnecessary to the ordering and is not asserted. Arteau's 17 November 2014 post also predates the candidate. Later comments and newer payload collections supply no credit.
- **Independent prior-art check:** Searching for SpEL Runtime execution and quoted-input breakouts, rather than EL3 by name, found Perry's complete original demonstration. This is stronger prior art than the 2011 paper alone.
- **Strongest challenge to the result:** The overall attack is old, and SpEL already offered a short execution payload plus operators for partial-expression injection. EL3 is a platform extension, not a new attack class.
- **Benefit-of-doubt check:** Standard EL3 supplies a distinct, usable execution route under its own evaluator constraints; earlier standard EL2.2 exploitation used more elaborate class-loader setup. This is enough for a modest extension verdict.
- **Changes after reverification:** Narrowed the contribution to the EL3 route, excluded any claim of originating RCE or expression breakout, and retained the reproduction deduction for malformed example wrappers. No hindsight or adoption bonus was used.

### Verdict

Meaningful extension

- **Archive decision:** Include as a supporting reference
- **Confidence:** Medium
- **Reasoning:** The standard-EL3 adaptation is distinct enough to meet the historical missed-technique gate of 55 with a qualifying verdict. Its merit is an incremental testing capability, not the size of an affected deployment.
- **Evidence gaps:** No runnable project or named production example was supplied; historical execution was not replayed. The live post lacks immutable revision history. No exact pre-cutoff EL3 exploit was found, which is uncertainty rather than proof of first invention.

---


---

## 55.0 — [SpoofedMe — Social Login Impersonation Attack](https://www.slideshare.net/slideshow/spoofed-me-socialloginattack/42313457) — Or Peles and Roee Hay

**REMOVED** · Useful application or case study · confidence Medium

Reviewed 2026-09-11; [TECAPI source audit](2026-09-11-tecapi.md).


### Candidate

- **Title:** SpoofedMe — Intruding Accounts using Social Login Providers
- **Author or organisation:** Or Peles and Roee Hay, IBM Security Systems
- **Publication date:** Paper dated 3 December 2014; public author disclosure verified on 4 December 2014
- **Reference:** [Author disclosure](https://seclists.org/fulldisclosure/2014/Dec/22); [eight-page paper uploaded by IBM Security](https://www.slideshare.net/slideshow/spoofed-me-socialloginattack/42313457)

### Core Contribution

A relying application mistakes an identity provider's unverified email claim for proof of ownership, then selects or links a victim's local account. The attacker registers an identity with the victim's unused email address at a permissive provider and completes ordinary login. The paper documents controlled end-to-end cases and separates provider verification from account linking. It expressly acknowledges the relying-party problem as known; its remaining value is empirical explanation across provider configurations, not a new identity-trust primitive.

### Prior Art

- **Novelty cutoff:** 3–4 December 2014. The paper's internal date is 3 December; the dated Full Disclosure message on 4 December verifies public availability. Private vendor reports are not publication dates.
- **Earliest credible pre-cutoff related work:** Eran Hammer's [account-linking architecture answer](https://stackoverflow.com/questions/6666267/architecture-for-merging-multiple-user-accounts-together), 2 August 2011, requires an existing authenticated session for linking. Brad J's answer on the same page, 25 November 2012, explicitly identifies account takeover through unsafe automatic merging and requires authentication to an existing identity first. These are firsthand design contributions, not secondary reporting.
- **Closest pre-cutoff equivalent work:** The firsthand [LinkedIn unverified-email OAuth report](https://stackoverflow.com/questions/19278201/oauth-request-verified-email-address-from-linkedin), 9 October 2013, already identifies the very provider behavior later tested by SpoofedMe. Its November 2013 answer distinguishes OAuth versions. The candidate cites this thread itself. [Wang, Chen and Wang's 2012 paper](../../archived-references/md/2012/signing-me-onto-your-accounts-through-facebook-google.md), §§4.1 and 4.5, supplies demonstrated email-identity confusion through unsigned attributes or datatype substitution. [Nat Sakimura's response](https://nat.sakimura.org/2012/04/27/comments-on-wang-chen-wang-paper/), 27 April 2012 with a 1 May author response, explains the identifier-selection issue. Those protocol-manipulation routes differ from simply registering an unverified address.
- **Evidence boundary:** All eight original paper pages and their references were read; generated SlideShare summaries were ignored. The local 2012 OAuth and 2014 SSOScan papers were checked by mechanism. [SSOScan](https://www.usenix.org/conference/usenixsecurity14/technical-sessions/presentation/zhou), August 2014, tests credential misuse/leakage and signature handling; it is related but not a direct duplicate of this email-registration route. Undated Stack Overflow comments and the June 2016 answer were excluded. No later account-prehijacking work was scored.
- **Candidate's distinct contribution as of the cutoff:** A useful systematic case study, explicit preconditions and mitigation comparison for an already exposed provider behavior combined with known unsafe linking. The Amazon email-change discussion is a plausible variant, not evidence of a separate demonstrated new primitive.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 30/100 | 25% | 7.50/25 | The provider flaw and unsafe-linking consequence were already public; the added contribution is empirical treatment. |
| Transferability | 50/100 | 20% | 10.00/20 | Cross-provider cases clarify shared preconditions, but the trust rule itself is older. |
| Lasting value | 50/100 | 20% | 10.00/20 | A useful concrete reference for testing two-sided identity assumptions; no new general model or automation. |
| Technical soundness | 80/100 | 15% | 12.00/15 | Clear causal sequence, controlled victim accounts, provider distinctions and sensible limits. |
| Practical usability | 70/100 | 10% | 7.00/10 | An actionable test and mitigation checklist for integrations with the specified conditions. |
| Clarity and reproducibility | 85/100 | 10% | 8.50/10 | Eight-page treatment states prerequisites, stages, affected pairings and mitigations. |

**Final score: 55.0/100**

### Reverification

- **Candidate facts rechecked against:** The complete IBM-uploaded paper and its dated author mailing-list message; claims of successful controlled-account tests remain attributed to the authors rather than independently reproduced results.
- **Cutoff audit:** The 2011 and 2012 answers expose explicit dates; the provider question is October 2013. The original 2012 papers' content and local copies were checked. No uncertain comment timestamp was treated as pre-cutoff evidence.
- **Independent prior-art check:** Followed the candidate's citations backward to account-merging advice and provider verification, rather than searching for SpoofedMe or general OAuth failures. This exposed closer prior art than SSOScan.
- **Strongest challenge to the result:** Both the provider behavior and unsafe-merge attack were public before 2014; protocol independence alone does not establish a new mechanism.
- **Benefit-of-doubt check:** The original paper does more than reprint the earlier warning: it presents useful end-to-end validation, precise constraints and differentiated provider behavior. That supports a case-study verdict rather than dismissing all value as duplication.
- **Changes after reverification:** Rejected the initial new-technique interpretation after checking the 2013 LinkedIn report. Retained supporting research value without upgrading the verdict to clear the historical gate. Score arithmetic was recomputed exactly.

### Verdict

Useful application or case study

- **Archive decision:** Include as a supporting reference
- **Confidence:** Medium
- **Reasoning:** Strong explanatory evidence adds value, but this is not a qualifying novelty verdict. Therefore there is no new 2014 missed-list entry. The standalone supporting recommendation is recorded here and does not result in a year-list citation or reference-archive mutation in this workflow.
- **Evidence gaps:** No independent historical execution. The 2013 version-specific answer does not document its own tests in detail, and the later comment dates could not be verified; those comments were not used. The exact paper upload day within 3–4 December is unresolved.

---


---

## 46.9 — [Remote Code Execution .. by design](https://blog.h3xstream.com/2014/11/remote-code-execution-by-design.html) — Philippe Arteau

**REMOVED** · Useful application or case study · confidence Medium

Reviewed 2026-09-11; [TECAPI source audit](2026-09-11-tecapi.md).


### Candidate

- **Title:** Remote Code Execution .. by design
- **Author or organisation:** Philippe Arteau
- **Publication date:** 17 November 2014
- **Reference:** [Original post](https://blog.h3xstream.com/2014/11/remote-code-execution-by-design.html)

### Core Contribution

Application-exposed expression and scripting engines inherit Java capabilities unless their evaluation contexts restrict them. Arteau provides SpEL execution and output-reading examples, plus a Rhino/ScriptEngine example and sandbox pointers. The anonymous real-world situations are author claims; the article uses illustrative application code. Its contribution is a concise practitioner case study and payload reference.

### Prior Art

- **Novelty cutoff:** 17 November 2014, the original dated post; no earlier candidate-side public disclosure located.
- **Earliest credible pre-cutoff related work:** Jani Hartikainen's [Sandboxing Rhino in Java](https://codeutopia.net/blog/2009/01/02/sandboxing-rhino-in-java/), 2 January 2009, explains untrusted-script Java access and reflection paths around ClassShutter. Arteau cites it. The later “newer versions” note on that page is excluded.
- **Closest pre-cutoff equivalent work:** Brandon Perry's [SpEL post](https://volatile-minds.blogspot.com/2012/09/theoritical-vulnerabilities-using.html), 12 September 2012, already provides direct Runtime execution and quote-breakout code. The [2011 EL paper](../../archived-references/md/2011/expression-language-injection.md) and Dan Amodio's [December 2012 original text preserved in seven pages](https://www.slideshare.net/slideshow/remote-codewithexpressionlanguageinjection/24272376) provide additional EL exploitation context. SpEL and standard JSP EL are kept distinct.
- **Evidence boundary:** Read the entire candidate twice, once by direct fetch; read Perry's entire source and Hartikainen's technical sections. Local searches found the 2011 EL paper and 2013 Struts research. Later Rhino API notes, later comments and post-2014 payload collections were excluded. Amodio's exact December publication day is not necessary to establish pre-November-2014 ordering.
- **Candidate's distinct contribution as of the cutoff:** Practical packaging and a compact output-reading idiom. The paper neither establishes a new execution primitive nor demonstrates defeating a configured sandbox. The different script-engine example is not itself enough to turn an already explained Java-access risk into a new attack class.

### Scorecard

| Category | Score | Weight | Weighted score | Reason |
|---|---:|---:|---:|---|
| Original contribution | 28/100 | 25% | 7.00/25 | Mostly known evaluator-to-Java execution, with a useful output-reading example. |
| Transferability | 42/100 | 20% | 8.40/20 | Two engine families are covered, but the marginal insight beyond prior sources is limited. |
| Lasting value | 40/100 | 20% | 8.00/20 | Convenient reference material, without a new reusable testing method or boundary-bypass result. |
| Technical soundness | 64/100 | 15% | 9.60/15 | Main execution routes are explained; claims about expression restrictions are too broad and the HTTP exfiltration example is incomplete. |
| Practical usability | 65/100 | 10% | 6.50/10 | Useful short examples when an application exposes an unrestricted evaluator. |
| Clarity and reproducibility | 74/100 | 10% | 7.40/10 | API snippets and payloads are readable, with some placeholders and no complete application. |

**Final score: 46.9/100**

### Reverification

- **Candidate facts rechecked against:** The original dated byline and all technical sections, including the stated illustrative scope and citations.
- **Cutoff audit:** Perry's date is visible on the original page. Hartikainen's dated URL and its citation by the candidate establish pre-cutoff availability; its newer-version note was omitted from comparison. The 2011 disclosure has a dated author announcement. No later publication supplies novelty credit or discredit.
- **Independent prior-art check:** Searching for the direct Runtime call plus partial-expression injection found Perry's 2012 example, independently of Arteau's references. Following the Rhino citation supplied earlier explicit analysis of untrusted script reaching Java.
- **Strongest challenge to the result:** The Scanner output idiom and juxtaposition of engines could be credited as a practical extension. They improve convenience but do not establish a new capability under a previously unmet constraint.
- **Benefit-of-doubt check:** The compact examples are usable research aids and justify retaining the lead as an evaluated case study, rather than labeling it a verbatim duplicate.
- **Changes after reverification:** Narrowed the verdict to a case study and scored its incremental utility. Anonymous deployments were not treated as novel merely because they were real. The final total was recomputed.

### Verdict

Useful application or case study

- **Archive decision:** Do not include
- **Confidence:** Medium
- **Reasoning:** Clear enough to be useful as a short tutorial, but its marginal contribution scores below 50 and does not qualify for a missed-technique addition. No separate archive acquisition is requested.
- **Evidence gaps:** No runnable complete project or named target; no independent replay of historical environments. The precise revision histories of the live blogs are unavailable.
