# 2023 research judgements

These scorecards apply the six-category rubric to calendar-year 2023 candidates
that survived the exclusion, scope and plausibility screens. Publication date is
an independent list gate, so the wrong-year reassessment remains recorded.

## 90.2 — [The Leaky Web: Automated Discovery of Cross-Site Information Leaks in Browsers and the Web](https://trouge.net/papers/xsleaks_sp2023.pdf) — Jannis Rautenstrauch, Giancarlo Pellegrino, Ben Stock

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed IEEE S&P paper first posted on 6 January 2023.

### Core contribution

The framework systematically mutates cross-origin responses and observes browser
APIs to discover XS-Leak observation channels without a priori leak templates.
It characterizes 280 channels across three engines and drives a real-site pipeline
that measures visit, cookie-acceptance and login-state inference.

### Prior art

Individual XS-Leaks date to the 2000s; Basta-COSI (2020), XSinator (2021) and the
2022 XS-Leaks SoK already modeled and tested known classes. This work adds broad,
mechanism-agnostic channel discovery and an empirical Web exploitation pipeline.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | New systematic observation-channel discovery. |
| Transferability | 94 | 20% | 18.80 | Spans browser engines, APIs and site states. |
| Lasting value | 92 | 20% | 18.40 | Durable framework for the XS-Leak attack surface. |
| Technical soundness | 95 | 15% | 14.25 | Large browser and Web evaluations support it. |
| Practical usability | 90 | 10% | 9.00 | Open tooling converts channels into site tests. |
| Clarity and reproducibility | 93 | 10% | 9.30 | Method, code and evaluation are detailed. |

**Final score: 90.2/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It changes XS-Leak research from manual
instance hunting into systematic browser-surface discovery.

## 89.3 — [DiffCSP: Finding Browser Bugs in Content Security Policy Enforcement through Differential Testing](https://www.ndss-symposium.org/ndss-paper/diffcsp-finding-browser-bugs-in-content-security-policy-enforcement-through-differential-testing/) — Seongil Wi, Trung Tin Nguyen, Jihwan Kim, Ben Stock, Sooel Son

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2023.

### Core contribution

DiffCSP generates policies and HTML instances covering JavaScript execution paths,
runs them across browser engines, and uses decision trees to explain divergent CSP
enforcement. It found 29 security bugs, including specification ambiguities, and
contributed to twelve browser fixes.

### Prior art

Cross-browser differential testing and CSP bypass research were established.
DiffCSP's distinct contribution is a CSP-semantic generator and analysis pipeline
that systematically maps enforcement divergence back to common root causes.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | First CSP-specific differential framework of this breadth. |
| Transferability | 92 | 20% | 18.40 | Applies across directives, HTML paths and engines. |
| Lasting value | 90 | 20% | 18.00 | CSP evolution makes conformance testing durable. |
| Technical soundness | 94 | 15% | 14.10 | Findings, classifications and patches validate it. |
| Practical usability | 91 | 10% | 9.10 | Automated generation substantially lowers testing effort. |
| Clarity and reproducibility | 92 | 10% | 9.20 | Algorithms and experimental results are explicit. |

**Final score: 89.3/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It systematizes discovery of specification
and implementation bugs in a core browser security control.

## 87.4 — [Isolated and Exhausted: Attacking Operating Systems via Site Isolation in the Browser](https://www.usenix.org/conference/usenixsecurity23/presentation/gierlings) — Matthias Gierlings, Marcus Brinkmann, Jörg Schwenk

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2023.

### Core contribution

A malicious site turns per-site browser processes and related features into OS
resource-exhaustion primitives: a process fork bomb, exhaustion of UDP sockets,
and a resulting DNS-cache-poisoning chain. The work exposes an architectural
inversion in which Site Isolation gives Web origins leverage over host resources.

### Prior art

Browser denial of service, resource exhaustion and DNS poisoning were known.
The new mechanism is using Site Isolation's Web-to-process mapping and sandboxed
browser APIs to exhaust host-global resources and enable a cross-layer attack.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 88 | 25% | 22.00 | New Site-Isolation-to-host resource attack model. |
| Transferability | 86 | 20% | 17.20 | Recurs where browser abstractions consume host-global pools. |
| Lasting value | 87 | 20% | 17.40 | Important browser/OS boundary insight. |
| Technical soundness | 92 | 15% | 13.80 | Three escalating demonstrations validate the model. |
| Practical usability | 80 | 10% | 8.00 | Web delivery is direct, though advanced chains are demanding. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Threat model and attacks are well documented. |

**Final score: 87.4/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It derives new host-level capabilities from a browser
isolation defense rather than merely applying a known denial-of-service payload.

## 86.7 — [Scaling JavaScript Abstract Interpretation to Detect and Exploit Node.js Taint-style Vulnerability](https://www.yinzhicao.org/FAST/ODGen-FAST.pdf) — Mingqing Kang, Yichao Xu, Song Li, Rigel Gjomemo, Jianwei Hou, V. N. Venkatakrishnan, Yinzhi Cao

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed IEEE S&P paper published in May 2023.

### Core contribution

FAST combines bottom-up scope-based abstract interpretation with top-down,
sink-directed path pruning and exploitability constraints. It scales dynamic
JavaScript data-flow analysis to large Node.js packages and reports 242 new
vulnerabilities, including results in full applications and frameworks.

### Prior art

Node.js taint analysis, ODGen and syntax-directed static tools predate FAST. Its
advance is a two-direction abstract interpretation that preserves dynamic call
resolution while avoiding the state explosion that blocked application scale.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 72 | 25% | 18.00 | New scalable composition of abstract analyses. |
| Transferability | 90 | 20% | 18.00 | Covers packages, frameworks and Node applications. |
| Lasting value | 91 | 20% | 18.20 | Durable method for dynamic-language security analysis. |
| Technical soundness | 94 | 15% | 14.10 | Comparative evaluation and confirmed flaws support it. |
| Practical usability | 94 | 10% | 9.40 | Scales vulnerability and exploit-path detection. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Analysis stages and evaluation are explicit. |

**Final score: 86.7/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It makes precise JavaScript analysis usable
on code sizes that defeated earlier abstract interpreters.

## 86.1 — [RøB: Ransomware over Modern Web Browsers](https://www.usenix.org/conference/usenixsecurity23/presentation/oz) — Harun Oz, Ahmet Aris, Abbas Acar, Güliz Seray Tuncay, Leonardo Babun, Selcuk Uluagac

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2023.

### Core contribution

RøB combines the File System Access API and WebAssembly into browser-delivered
ransomware that encrypts files in user-approved directories, including external,
network and cloud-integrated storage. The evaluation shows why native antivirus
and existing ransomware defenses miss malicious activity performed by a browser.

### Prior art

Ransomware and the browser File System Access API were established, and the API's
risk was discussed conceptually. This is the first systematic end-to-end browser
ransomware construction and defense evaluation using the granted Web capability.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 84 | 25% | 21.00 | New end-to-end browser-native ransomware technique. |
| Transferability | 88 | 20% | 17.60 | Applies wherever powerful file APIs are granted to Web apps. |
| Lasting value | 84 | 20% | 16.80 | Durable warning about capability-rich browser APIs. |
| Technical soundness | 91 | 15% | 13.65 | Cross-platform and defense evaluations support it. |
| Practical usability | 82 | 10% | 8.20 | Requires user-granted access but no native installation. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Attack, experiments and mitigations are documented. |

**Final score: 86.1/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It turns a legitimate browser file capability into a complete
malware workflow that existing endpoint assumptions do not capture.

## 85.8 — [It's (DOM) Clobbering Time: Attack Techniques, Prevalence, and Defenses](https://trouge.net/publication/domclob-sp-2023/) — Soheil Khodayari, Giancarlo Pellegrino

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed IEEE S&P paper first posted in January 2023.

### Core contribution

The work systematizes DOM-clobbering sources, gadget patterns and exploit chains,
builds automated discovery, measures real-site prevalence, and demonstrates how
markup-only injection can redirect trusted JavaScript data flow into dangerous
sinks. It also evaluates defenses against the resulting gadget space.

### Prior art

DOM clobbering was public by 2010 and named attack payloads appeared by 2013;
script-gadget and sanitizer work followed. The contribution is a comprehensive
attack methodology, automated gadget analysis and prevalence evidence, not the
original collision behavior.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 70 | 25% | 17.50 | Materially expands a known primitive. |
| Transferability | 92 | 20% | 18.40 | Gadget patterns recur across client-side applications. |
| Lasting value | 88 | 20% | 17.60 | Established a durable audit methodology. |
| Technical soundness | 94 | 15% | 14.10 | Tooling and Web measurement support the taxonomy. |
| Practical usability | 90 | 10% | 9.00 | Patterns and automation are directly actionable. |
| Clarity and reproducibility | 92 | 10% | 9.20 | Attack classes and defenses are precisely presented. |

**Final score: 85.8/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It turns a long-known DOM quirk into a systematic offensive
testing discipline with new gadget classes and evidence.

## 85.0 — [Finding All Cross-Site Needles in the DOM Stack](https://casa.rub.de/en/research/publications/detail/finding-all-cross-site-needles-in-the-dom-stack-a-comprehensive-methodology-for-the-automatic-xs-leak-detection-in-web-browsers) — Dominik Trevor Noß, Lukas Knittel, Christian Mainka, Marcus Niemietz, Jörg Schwenk

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed ACM CCS paper published in November 2023.

### Core contribution

AutoLeak serializes browser DOM object graphs under two victim states and diffs
the graphs to enumerate observable cross-origin differences. Across 151,776 tests
it found thousands of leak techniques, five new XS-Leak classes and practical
leaks in twenty of twenty-four evaluated high-ranking sites.

### Prior art

XS-Leak automation included Basta-COSI, XSinator and the earlier-2023 Leaky Web
framework. AutoLeak's distinct contribution is exhaustive runtime DOM graph
differencing for a chosen resource and inclusion method, rather than response/API
mutation and decision-tree characterization.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 72 | 25% | 18.00 | New DOM-graph differencing methodology. |
| Transferability | 90 | 20% | 18.00 | Works across engines, objects, headers and sites. |
| Lasting value | 86 | 20% | 17.20 | Durable complement to other XS-Leak frameworks. |
| Technical soundness | 93 | 15% | 13.95 | Large test matrix and site validation support it. |
| Practical usability | 88 | 10% | 8.80 | Automated enumeration lowers manual leak hunting. |
| Clarity and reproducibility | 91 | 10% | 9.10 | Tool, graph method and cases are documented. |

**Final score: 85.0/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It adds a distinct exhaustive DOM-observation
strategy alongside the year's broader XS-Leak discovery work.

## 84.8 — [SynthDB: Synthesizing Database via Program Analysis for Security Testing of Web Applications](https://www.ndss-symposium.org/ndss-paper/synthdb-synthesizing-database-via-program-analysis-for-security-testing-of-web-applications/) — An Chen, Jiho Lee, Basanta Chaulagain, Yonghwi Kwon, Kyu Hyung Lee

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2023.

### Core contribution

SynthDB uses concolic analysis of PHP and SQL interactions to construct a database
that satisfies integrity constraints while unlocking unexplored Web-application
paths. Feeding the synthesized state to Burp Suite, Wfuzz and webFuzz raises
coverage and reveals 33 previously unknown vulnerabilities.

### Prior art

Concolic execution, database test-data generation and Web fuzzers were known. The
advance is purpose-built reconstruction of relational state from application
constraints so existing dynamic security tools can reach database-dependent paths.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 68 | 25% | 17.00 | New security-oriented database synthesis pipeline. |
| Transferability | 90 | 20% | 18.00 | Benefits many database-backed PHP applications and tools. |
| Lasting value | 88 | 20% | 17.60 | State preparation is a durable Web-testing bottleneck. |
| Technical soundness | 93 | 15% | 13.95 | Seventeen-app comparisons and findings validate it. |
| Practical usability | 92 | 10% | 9.20 | Directly augments established testing tools. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Constraints and evaluation are well specified. |

**Final score: 84.8/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It automates the hidden database-state setup
that otherwise limits dynamic Web security coverage.

## 84.5 — [Fashion Faux Pas: Implicit Stylistic Fingerprints for Bypassing Browsers' Anti-Fingerprinting Defenses](https://www.cs.uic.edu/~polakis/papers/lin-sp23.pdf) — Xu Lin, Frederico Araujo, Teryl Taylor, Jiyong Jang, Jason Polakis

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed IEEE S&P paper published in May 2023.

### Core contribution

StylisticFP infers browser, OS and installed-font attributes using only CSS and
carefully arranged HTML elements. It avoids JavaScript APIs—the choke point used
by major anti-fingerprinting defenses—and remains effective against privacy-focused
browsers and extensions.

### Prior art

CSS-only fingerprinting, font probing and implicit layout measurements predate
2023. The meaningful advance is a complete optimized fingerprint that extracts
advanced attributes without JavaScript and is evaluated against deployed defenses.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78 | 25% | 19.50 | Strong CSS-only construction over known signals. |
| Transferability | 88 | 20% | 17.60 | Works across major privacy-oriented browsers. |
| Lasting value | 83 | 20% | 16.60 | Broadens defensive models beyond API blocking. |
| Technical soundness | 90 | 15% | 13.50 | Comparative and pilot evaluations support it. |
| Practical usability | 84 | 10% | 8.40 | Web-only deployment is directly actionable. |
| Clarity and reproducibility | 89 | 10% | 8.90 | Construction and measurements are detailed. |

**Final score: 84.5/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It makes earlier CSS fingerprinting a practical replacement
for JavaScript-heavy fingerprints under modern defenses.

## 84.5 — [Navigating Murky Waters: Automated Browser Feature Testing for Uncovering Tracking Vectors](https://www.ndss-symposium.org/ndss-paper/navigating-murky-waters-automated-browser-feature-testing-for-uncovering-tracking-vectors/) — Mir Masood Ali, Binoy Chitale, Mohammad Ghasemisharif, Chris Kanich, Nick Nikiforakis, Jason Polakis

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2023.

### Core contribution

CanITrack accepts read/write operations for an arbitrary browser mechanism and
tests its state across browsing contexts to discover tracking behavior without a
feature-specific oracle. Testing 21 mechanisms uncovered thirteen third-party
tracking vectors and two private-mode isolation bypasses.

### Prior art

Researchers had manually found storage, cache and browser-feature tracking
vectors. This work contributes a mechanism-agnostic state-transition harness that
vendors can reuse as new browser APIs and privacy-sandbox features appear.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 68 | 25% | 17.00 | New generic harness over a known tracking goal. |
| Transferability | 92 | 20% | 18.40 | Accepts heterogeneous present and future mechanisms. |
| Lasting value | 87 | 20% | 17.40 | Fits continuing browser feature deployment. |
| Technical soundness | 92 | 15% | 13.80 | Multi-browser disclosures validate the method. |
| Practical usability | 89 | 10% | 8.90 | Simple read/write adapters make it reusable. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Framework and contexts are well described. |

**Final score: 84.5/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It generalizes tracking-vector discovery
across browser features instead of adding one isolated state leak.

## 84.5 — [CoCo: Efficient Browser Extension Vulnerability Detection via Coverage-guided, Concurrent Abstract Interpretation](https://yinzhicao.org/CoCo/CoCo.pdf) — Jianjia Yu, Song Li, Junmin Zhu, Yinzhi Cao

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed ACM CCS paper published in November 2023.

### Core contribution

CoCo parallelizes abstract interpretation and taint propagation across branches,
message channels, and extension content/background scripts, prioritizing paths
that increase code coverage. It found 43 manually verified vulnerabilities missed
by previous extension analyzers.

### Prior art

EmPoWeb and DoubleX already used static dependency and data-flow analysis for
extension privilege escalation. CoCo adds coverage-guided concurrent abstract
interpretation to handle dynamic JavaScript without client-side state explosion.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 70 | 25% | 17.50 | New scalable extension-analysis composition. |
| Transferability | 88 | 20% | 17.60 | Covers common extension components and message flows. |
| Lasting value | 87 | 20% | 17.40 | Dynamic extension analysis remains a durable need. |
| Technical soundness | 93 | 15% | 13.95 | Verified unique findings support the analysis. |
| Practical usability | 91 | 10% | 9.10 | Automates difficult privileged-flow discovery. |
| Clarity and reproducibility | 89 | 10% | 8.90 | Algorithm and evaluation are documented. |

**Final score: 84.5/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It materially scales discovery of known
extension privilege-boundary failures.

## 82.9 — [QUICforge: Client-side Request Forgery in QUIC](https://www.ndss-symposium.org/ndss-paper/quicforge-client-side-request-forgery-in-quic/) — Yuri Gbur, Florian Tschorsch

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2023.

### Core contribution

QUIC clients are induced to emit attacker-shaped protocol messages toward a
third party, enabling UDP protocol impersonation—including DNS—and traffic
amplification. The paper derives the capability from QUIC's protocol design and
tests anti-amplification behavior across thirteen server implementations.

### Prior art

Cross-protocol request forgery, UDP amplification and QUIC implementation flaws
were known. The new contribution is the controllable client-side request-forgery
space inherent in QUIC messages and its concrete cross-protocol construction.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | New protocol-derived QUIC request-forgery primitive. |
| Transferability | 82 | 20% | 16.40 | Relevant across QUIC deployments and UDP targets. |
| Lasting value | 80 | 20% | 16.00 | Important as HTTP/3 and QUIC adoption expands. |
| Technical soundness | 90 | 15% | 13.50 | Protocol analysis and implementation study support it. |
| Practical usability | 77 | 10% | 7.70 | Exploitation needs controllable QUIC interactions. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Modalities and evaluation are documented. |

**Final score: 82.9/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It identifies request forgery emerging from QUIC semantics,
not merely a missing rate limit in one implementation.

## 82.3 — [Uncovering and Exploiting Hidden APIs in Mobile Super Apps](https://arxiv.org/abs/2306.08134) — Chao Wang, Yue Zhang, Zhiqiang Lin

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Complete preprint published on 13 June 2023; later peer-reviewed at ACM CCS.

### Core contribution

APIScope combines cross-language static recognition and dynamic invocation to
identify undocumented super-app APIs that third-party mini-apps can call without
the intended checks. Across five platforms it demonstrates access to privileged
resources, arbitrary Web content, downloads and sensitive information.

### Prior art

Hidden mobile APIs, mini-app privilege flaws and broken access control were known.
The advance is a systematic multi-language method for recognizing the host's
private JavaScript-facing API surface and validating third-party reachability.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 72 | 25% | 18.00 | New hidden mini-app API discovery pipeline. |
| Transferability | 82 | 20% | 16.40 | Demonstrated across five major super-app runtimes. |
| Lasting value | 84 | 20% | 16.80 | App-in-app APIs remain a growing Web-like boundary. |
| Technical soundness | 91 | 15% | 13.65 | Cross-platform findings and case studies support it. |
| Practical usability | 85 | 10% | 8.50 | Automates recognition and exploitability checks. |
| Clarity and reproducibility | 89 | 10% | 8.90 | Architecture, scope and findings are explicit. |

**Final score: 82.3/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It systematizes discovery of an undocumented
Web-like API trust boundary inside super apps.

## 80.7 — [Checking Passwords on Leaky Computers: A Side Channel Analysis of Chrome's Password Leak Detect Protocol](https://www.usenix.org/conference/usenixsecurity23/presentation/kwong) — Andrew Kwong, Walter Wang, Jason Kim, Jonathan Berger, Daniel Genkin, Eyal Ronen, Hovav Shacham, Riad Wahby, Yuval Yarom

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2023.

### Core contribution

The work builds practical cache attacks against Chrome's scrypt and hash-to-curve
processing and a new single-trace cryptanalysis of its variable-time modular
inversion. A local attacker or malicious service can reduce password guessing or
recover a credential digest despite the private-set-intersection design.

### Prior art

Browser cache attacks and theoretical scrypt leakage were known. The contribution
is making the scrypt attack practical under noise and showing three concrete
leakage points in a default browser credential-protection protocol.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78 | 25% | 19.50 | New practical attacks and BEEA trace recovery. |
| Transferability | 75 | 20% | 15.00 | Ideas transfer, though the protocol target is specific. |
| Lasting value | 82 | 20% | 16.40 | Durable warning for client-side privacy protocols. |
| Technical soundness | 94 | 15% | 14.10 | End-to-end experiments and cryptanalysis are rigorous. |
| Practical usability | 66 | 10% | 6.60 | Requires side-channel access or a malicious server. |
| Clarity and reproducibility | 91 | 10% | 9.10 | Attacks and limitations are carefully documented. |

**Final score: 80.7/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It turns anticipated timing concerns into practical attacks
against a widely deployed browser authentication-protection workflow.

## 80.5 — [A Security Study about Electron Applications and a Programming Methodology to Tame DOM Functionalities](https://www.ndss-symposium.org/ndss-paper/a-security-study-about-electron-applications-and-a-programming-methodology-to-tame-dom-functionalities/) — Zihao Jin, Shuo Chen, Yang Chen, Haixin Duan, Jianjun Chen, Jianping Wu

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2023.

### Core contribution

The authors model an application's intended markup as a DOM-tree type and enforce
that type in Electron, rejecting attacker-created trees rather than enumerating
every dangerous input. The approach follows a multi-app vulnerability study and
blocks the discovered HTML-to-local-privilege exploit paths.

### Prior art

Electron XSS-to-RCE chains, sanitizers, Trusted Types and typed DOM construction
were known. DOM-tree types add an intention-oriented structural policy integrated
into the Electron platform and validated against real applications.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 65 | 25% | 16.25 | New structural typing policy for Electron DOMs. |
| Transferability | 85 | 20% | 17.00 | Relevant to Electron and other privileged Web runtimes. |
| Lasting value | 84 | 20% | 16.80 | Useful intention-over-blocklist methodology. |
| Technical soundness | 90 | 15% | 13.50 | Vulnerability study and platform evaluation support it. |
| Practical usability | 82 | 10% | 8.20 | Requires platform integration but protects existing apps. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Type model and evaluation are clear. |

**Final score: 80.5/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It supplies a transferable structural
defense and audit model for Web content operating with desktop privilege.

## 81.7 — [Silent Spring: Prototype Pollution Leads to Remote Code Execution in Node.js](https://arxiv.org/abs/2207.11171) — Mikhail Shcherbakov, Musard Balliu, Cristian-Alexandru Staicu

**REMOVED** · Original technique · confidence High

### Candidate

Complete public preprint published on 22 July 2022; presented at USENIX Security
in August 2023. This reassesses the pre-existing 2023 missed-list entry.

### Core contribution

The paper combines prototype-pollution detection with hybrid universal-gadget
analysis, finds eleven Node.js core gadgets, and demonstrates eight end-to-end RCE
chains in full applications. The technical contribution remains substantial.

### Prior art

Prototype pollution, Node.js RCE gadgets and individual application chains were
known. Silent Spring systematizes application-to-universal-gadget discovery, but
all of that contribution was already public in calendar year 2022.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 70 | 25% | 17.50 | Strong systematic gadget methodology. |
| Transferability | 85 | 20% | 17.00 | Applies across Node.js applications and core APIs. |
| Lasting value | 84 | 20% | 16.80 | Influenced later prototype-gadget research. |
| Technical soundness | 92 | 15% | 13.80 | Tools and end-to-end exploits validate it. |
| Practical usability | 76 | 10% | 7.60 | Analysis is usable but requires expert triage. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Paper and artifacts document the method. |

**Final score: 81.7/100.** Archive decision: include as a core technique, but not in the 2023 list.

### Verdict

Original technique. Rejected from this year's missed section solely because the
first complete public disclosure is 2022; venue year cannot override that date.

## 79.2 — [Extending a Hand to Attackers: Browser Privilege Escalation Attacks via Extensions](https://www.usenix.org/conference/usenixsecurity23/presentation/kim-young-min) — Young Min Kim, Byoungyoung Lee

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2023.

### Core contribution

The work derives security requirements at the extension content-script/background
boundary, finds 59 violations in 40 extensions enabling UXSS and secret theft,
and proposes FistBump, an architecture that isolates Web pages from content scripts
so developers need not manually uphold those requirements.

### Prior art

Extension message-passing vulnerabilities, privilege escalation and analysis tools
were established. The contribution is a requirement-level study plus an isolation
architecture that removes the recurring confused-deputy pattern by construction.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 60 | 25% | 15.00 | New architecture over a known extension flaw family. |
| Transferability | 86 | 20% | 17.20 | Applies across common extension components and engines. |
| Lasting value | 82 | 20% | 16.40 | Durable least-privilege design lesson. |
| Technical soundness | 91 | 15% | 13.65 | Broad findings and prototype evaluation support it. |
| Practical usability | 83 | 10% | 8.30 | Architecture reduces developer-side security burden. |
| Clarity and reproducibility | 87 | 10% | 8.70 | Requirements and design are clearly reported. |

**Final score: 79.2/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It replaces fragile extension coding rules
with a privilege boundary enforced by architecture.

## 47.4 — [Hijacking OAuth Code via Reverse Proxy for Account Takeover](https://blog.voorivex.team/hijacking-oauth-code-via-reverse-proxy-for-account-takeover) — Omid Rezaei, Voorivex

**REMOVED** · Meaningful combination or adaptation · confidence Medium

### Candidate

Published 17 November 2023. Judged in the 10 August 2026 single-publisher sweep of
`blog.voorivex.team`; not part of the original 2023 nomination round.

### Core contribution

The application validates `state` with a regex that is strict about the prefix but
tolerant of anything appended, so path segments can be added to it. Those segments
traverse into an internal `/imageProxy` endpoint, which will fetch an arbitrary
URL, and the OAuth authorization code rides the resulting request out to the
attacker. The reusable shape is that a strict-looking validator which permits
appending turns any same-origin fetching endpoint into an exfiltration channel for
whatever the flow carries.

### Prior art

Every constituent is established: `state` and `redirect_uri` manipulation in OAuth,
path traversal past a prefix check, and reverse proxies or image proxies as SSRF
and exfiltration gadgets. The dirty-dancing family of OAuth redirect-chain attacks
(2022, in archive) covers moving an authorization code to an attacker-observable
location. No prior work is cited in the post for this combination.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 34 | 25% | 8.50 | A combination of three well-known primitives on one target. |
| Transferability | 48 | 20% | 9.60 | The prefix-validator-plus-fetching-endpoint pattern recurs across applications. |
| Lasting value | 40 | 20% | 8.00 | Useful as an example rather than as a technique. |
| Technical soundness | 66 | 15% | 9.90 | The chain is coherent; the target is anonymised so the regex behaviour rests on the author's account. |
| Practical usability | 50 | 10% | 5.00 | Worth testing wherever a validated parameter allows appending. |
| Clarity and reproducibility | 64 | 10% | 6.40 | Readable; no reproducible artifact. |

**Final score: 47.4/100.** Archive decision: do not include.

### Reverification

- **Candidate facts rechecked against:** the post's description of the validator and
  the proxy endpoint.
- **Independent prior-art check:** searched by outcome (authorization code delivered
  to an attacker via a same-origin fetching endpoint) rather than by "reverse proxy",
  which lands in the established OAuth redirect-chain literature.
- **Strongest challenge to the result:** the combination is genuinely a chain rather
  than a single known bug, which argues for a slightly higher Original score.
- **Benefit-of-doubt check:** credited as a combination rather than an application
  for exactly that reason; it still sits well below the gate because each link and
  the overall goal were already documented.
- **Changes after reverification:** None. Confidence held at Medium because the
  target is anonymised and the validator behaviour cannot be checked independently.

### Verdict

Meaningful combination or adaptation. Below the 60 gate for the 2023 list.

- **Archive decision:** Do not include
- **Confidence:** Medium
- **Evidence gaps:** Anonymised target; the regex and proxy behaviour are author
  claims that cannot be verified.

## 32.9 — [Uncovering a Command Injection, $2400 Bounty](https://blog.voorivex.team/uncovering-a-command-injection-2400-bounty) — Omid Rezaei, Voorivex

**REMOVED** · Useful application or case study · confidence High

### Candidate

Published 14 October 2023. Judged in the 10 August 2026 single-publisher sweep.

### Core contribution

An ASN-driven reconnaissance chain — whois to `mapcidr` to `httpx`, then directory
fuzzing — reaches an exposed admin panel behind default credentials, where a
`changelogo.php` upload passes its filename into a shell. A filename of
`test || sleep 30 ||.gif` satisfies the extension check and executes, confirmed by
the delay.

### Prior art

Shell metacharacters in a filename reaching a command interpreter is one of the
oldest documented injection patterns, and time-based confirmation via `sleep` is
standard practice. The reconnaissance methodology is conventional and tool-driven.
The post cites tools rather than research and makes no novelty claim.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 15 | 25% | 3.75 | Textbook command injection found by conventional recon. |
| Transferability | 30 | 20% | 6.00 | Nothing beyond the standard practice it demonstrates. |
| Lasting value | 20 | 20% | 4.00 | No durable contribution. |
| Technical soundness | 62 | 15% | 9.30 | The finding is confirmed by observable timing and is plainly correct. |
| Practical usability | 38 | 10% | 3.80 | Reinforces a familiar workflow. |
| Clarity and reproducibility | 60 | 10% | 6.00 | Clear account of the steps taken. |

**Final score: 32.9/100.** Archive decision: do not include.

### Reverification

- **Candidate facts rechecked against:** the post.
- **Independent prior-art check:** searched by sink (filename concatenated into a
  shell command during upload handling), which is documented across decades of
  injection literature.
- **Strongest challenge to the result:** none; no novelty is claimed.
- **Benefit-of-doubt check:** competent bug hunting and a clear writeup — neither is
  what this rubric measures.
- **Changes after reverification:** None.

### Verdict

Useful application or case study.

- **Archive decision:** Do not include
- **Confidence:** High
- **Evidence gaps:** None material.

## 80.7 — [Second Breakfast: Implicit and Mutation-Based Serialization Vulnerabilities in .NET](https://media.defcon.org/DEF%20CON%2031/DEF%20CON%2031%20presentations/Jonathan%20Birch%20-%20Second%20Breakfast%20Implicit%20and%20Mutation-Based%20Serialization%20Vulnerabilities%20in%20.NET-whitepaper.pdf)

**KEPT** · Original technique · confidence High

### Candidate

Jonathan Birch, Microsoft, DEF CON 31 (August 2023); whitepaper, slide deck and
conference video. Surfaced by the 2026-08-12 pass over the ysonet
.NET-deserialization reference set.

### Core contribution

A serialization attack that does not require the attacker to supply or tamper
with the serialized stream. Polymorphic JSON and BSON serializers encode a type
specifier as an ordinary key ("__type", "$type"), and they also encode key-value
collections by using the keys directly. Nothing separates the two encodings, so
an attacker who can only influence a dictionary key inside an object the
application serializes can make the round trip reconstruct that object as a type
of their choosing. The whitepaper demonstrates it on JavaScriptSerializer with a
SimpleTypeResolver and on Json.NET with TypeNameHandling, reaching RCE through
AssemblyInstaller, and tabulates which of four serializers need the key first
and which check assignability.

The consequence is the part that matters: the sinks previously treated as safe —
serialization to a database, to an in-memory cache, or between back-end servers —
become reachable, and signing the serialized data with an HMAC does not help,
because the attacker never touches the signed bytes.

### Prior art

Forshaw's 2012 "Are You My Type?" and Munoz and Mirosh's 2017 "Friday the 13th:
JSON Attacks" are the whitepaper's own cited antecedents and are the closest
work; both assume an attacker-supplied stream, and the tamper-proofing advice
that followed them is exactly what this defeats. Type-confusion through a type
specifier is old; producing that specifier through the collection encoding, from
data the application itself serializes, is not attested earlier. A mechanism
search on the collision between type-specifier keys and dictionary keys returned
this whitepaper as the earliest statement.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 86 | 25% | 21.50 | A vulnerability class with a different threat model from all prior deserialization work, and one that invalidates the standard mitigation. |
| Transferability | 82 | 20% | 16.40 | The collision is a property of the encoding, not of .NET; four libraries are shown and the reasoning applies to any polymorphic key-value serializer. |
| Lasting value | 80 | 20% | 16.00 | Reframes "sign your serialized data" as insufficient and opens internal serialization paths as a durable audit target. |
| Technical soundness | 80 | 15% | 12.00 | Minimal working proofs per serializer and a coherent assignability analysis; no field survey and no measurement of how often the required data flow exists. |
| Practical usability | 70 | 10% | 7.00 | Needs a specific flow — attacker-controlled keys reaching an unsafe serializer — which is real but not ubiquitous. |
| Clarity and reproducibility | 78 | 10% | 7.80 | Short and precise with runnable snippets; the affected-serializer table renders poorly in extraction. |

**Final score: 80.7/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It defines a serialization attack that works without stream
tampering and shows the standard integrity defence does not address it.

### Reverification

- **Candidate facts rechecked against:** the archived DEF CON 31 whitepaper,
  which carries the author, affiliation and its own bibliography.
- **Independent prior-art check:** searched by mechanism for dictionary-key
  injection of a type specifier and for mutation during a serialization round
  trip, rather than by talk title, and followed the whitepaper's citations
  backward. Nothing earlier than 2023 states it.
- **Strongest challenge to the result:** the exploitation payloads are the
  familiar AssemblyInstaller and ObjectDataProvider gadgets, so only the reach
  is new, not the code execution.
- **Benefit-of-doubt check:** reach is precisely the contribution — it converts
  sinks that were correctly considered out of scope into exploitable ones.
- **Changes after reverification:** none.

## 79.5 — [Exploiting ASP.NET TemplateParser — Part I](https://code-white.com/blog/exploiting-asp.net-templateparser-part-1/)

**KEPT** · Original technique · confidence High

### Candidate

Markus Wulftange, Code White; Part I published 25 September 2023 and Part II
("SharePoint (CVE-2023-33160)") 29 September 2023. Judged as one piece of work.
Surfaced by the 2026-08-12 pass over the ysonet .NET-deserialization reference
set.

### Core contribution

Setter-based gadgets reached through the ASP.NET page parser itself rather than
through a serializer. Any application that parses attacker-influenced markup
lets an @ Register directive name an assembly, namespace and type; the parser
then instantiates that type and assigns its properties, and property types are
resolved by reflection. Two observations make that exploitable in general. A
generic type can be used to control what type a property has — declaring
ExpandedWrapper&lt;T&gt; makes the ExpandedElement property take type T, so
assigning a string routes through T's TypeConverter — which turns the parser
into a general "call an arbitrary TypeConverter on an attacker string" gadget.
Part II then defeats SharePoint's SafeControls allow-list, which validates the
control type during tokenisation, and reaches RCE as CVE-2023-33160.

### Prior art

Soroush Dalili's "A Security Review of SharePoint Site Pages" and Munoz and
Mirosh's "Room for Escape: Scribbling Outside the Lines of Template Security" are
both from 2020 and both already nominated on the 2020 list; the post cites them
as required reading. They analyse SPPageParserFilter and template security in
SharePoint. What is new here is moving down a layer to the framework's own
TemplateParser, so the gadget class exists for any ASP.NET application that
parses user-supplied markup, and the ExpandedWrapper generic-type trick for
controlling a property's declared type. Independent evidence of the gain:
Viettel's 2025 SharePoint ToolShell chain for CVE-2025-53770, already archived,
names Part I as the source of the technique it used, and Mirosh's 2026 Black Hat
type-conversion paper cites Part II.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78 | 25% | 19.50 | A gadget class in the page parser rather than a serializer, plus the generic-type route to controlling property types. |
| Transferability | 76 | 20% | 15.20 | Applies to any ASP.NET application that parses attacker-influenced markup; the TypeConverter reach is a general primitive. |
| Lasting value | 80 | 20% | 16.00 | Demonstrably reused by later work, including the 2025 SharePoint ToolShell chain and 2026 type-conversion research. |
| Technical soundness | 88 | 15% | 13.20 | Traced through framework reference source with a vendor-confirmed CVE at the end. |
| Practical usability | 74 | 10% | 7.40 | Usable where markup parsing is exposed, which is a real but not universal precondition; no tool released. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Two-part writeup with the parser policy stated explicitly and payloads given. |

**Final score: 79.5/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It establishes the ASP.NET TemplateParser as a gadget
surface in its own right and supplies the generic-type primitive that makes it
general rather than SharePoint-specific.

### Reverification

- **Candidate facts rechecked against:** both Code White posts, whose bylines
  give 25 and 29 September 2023 and the author, and MSRC for CVE-2023-33160.
- **Independent prior-art check:** searched for setter-based gadgets in ASP.NET
  page parsing and for TypeConverter abuse through generic wrappers, and checked
  the 2020 list entries the post itself cites. The 2020 work is SharePoint-level;
  the parser-level generalisation is not attested before 2023.
- **Strongest challenge to the result:** with two 2020 nominations already
  covering SharePoint template security, this could be read as a third pass over
  the same ground.
- **Benefit-of-doubt check:** the layer is different and the reuse by later,
  unrelated researchers is documented in the archive rather than asserted here.
- **Changes after reverification:** none.

## 57.4 — [Generating deserialization payloads for MessagePack C#'s Typeless mode](https://www.netwrix.com/en/resources/blog/generating-deserialization-payloads-for-messagepack-cs-typeless-mode/) — Netwrix

**REMOVED** · Useful application or case study · confidence High

### Candidate

Published 10 April 2023. Judged in the 2026-08-12 pass over the ysonet
.NET-deserialization reference set.

### Core contribution

Shows that MessagePack-CSharp's Typeless mode is an unbounded polymorphic
serializer like any other — it embeds assembly-qualified type names and
restores private fields — and walks through building working payloads for it
with the established gadgets, including under MessagePack's hardened security
options. Useful as a warning for teams migrating off BinaryFormatter.

### Prior art

The gadget chains used are the standard ObjectDataProvider and XXE ones from
2017 onward, and the library's own documentation already advises against
Typeless with untrusted data. The contribution is coverage of one more
serializer, which the rubric explicitly declines to count as a new technique.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 45 | 25% | 11.25 | Applies known gadgets to a serializer already documented as unsafe for untrusted input. |
| Transferability | 50 | 20% | 10.00 | Confined to MessagePack Typeless; the general "polymorphic serializer is a sink" lesson predates it. |
| Lasting value | 46 | 20% | 9.20 | Relevant while BinaryFormatter migrations continue, with no broader consequence. |
| Technical soundness | 78 | 15% | 11.70 | Payload construction is demonstrated concretely, including behaviour with hardened options enabled. |
| Practical usability | 72 | 10% | 7.20 | Directly usable against this library. |
| Clarity and reproducibility | 80 | 10% | 8.00 | Step-by-step with runnable code. |

**Final score: 57.4/100.** Archive decision: do not include.

### Verdict

Useful application or case study. Extending an established sink taxonomy to one
more library is coverage, not discovery.

### Reverification

- **Candidate facts rechecked against:** the archived post, which carries the
  10 April 2023 date and the payload code.
- **Independent prior-art check:** searched for earlier MessagePack Typeless
  exploitation and for the general polymorphic-serializer taxonomy; the library
  documentation and the 2017 gadget work both predate it.
- **Strongest challenge to the result:** the demonstration that MessagePack's
  hardened options do not help is a concrete, non-obvious result.
- **Benefit-of-doubt check:** that result lifts technical soundness, but it
  confirms an expectation rather than changing the model.
- **Changes after reverification:** none.
## 75.3 — [Cracking the Odd Case of Randomness in Java](https://www.elttam.com/blog/cracking-randomness-in-java) — Joseph, elttam

**KEPT** · Meaningful extension · confidence Medium

### Candidate

Published 9 February 2023. Attacks `java.util.Random` seed recovery where the
bound passed to `nextInt(bound)` is odd, and applies it to
`RandomStringUtils.randomAlphanumeric` as used for password-reset tokens.

### Core contribution

A meet-in-the-middle attack that splits the 48-bit LCG state into upper and
lower halves and solves them separately, cutting the work for three observed
outputs from roughly 2^41.5 to about 2^32.5 and recovering seeds in under a
minute. The reported web consequence is direct: request a reset for an
attacker-held account, recover the state from the issued token, then predict
the victim's token.

### Prior art

Recovering `java.util.Random` state is long established, and lattice and
brute-force approaches handle the even-bound case where `nextInt` leaks state
bits directly. The odd-bound case was the known-harder gap because the modulo
rejection loop destroys that direct leak; closing it practically is the
contribution.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 75 | 25% | 18.75 | Genuine algorithmic advance on the acknowledged hard case, not a re-run of even-bound work. |
| Transferability | 70 | 20% | 14.00 | Any Java application using `Random` for security tokens; the split-state idea generalises to other truncated LCGs. |
| Lasting value | 70 | 20% | 14.00 | `RandomStringUtils` remains widespread, so the finding stays actionable in review work. |
| Technical soundness | 85 | 15% | 12.75 | Complexity claims are argued and backed by a released tool with measured runtimes. |
| Practical usability | 80 | 10% | 8.00 | Sub-minute recovery makes it usable inside a real assessment. |
| Clarity and reproducibility | 78 | 10% | 7.80 | Method explained with a public implementation; some derivation is compressed. |

**Final score: 75.3/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. Seed recovery was known; making the odd-bound case
practical, and tying it to a concrete account-takeover path, is the addition.

## 57.2 — [PwnAssistant - Controlling /home's via a Home Assistant RCE](https://www.elttam.com/blog/pwnassistant) — elttam

**REMOVED** · Useful application or case study · confidence Medium

### Candidate

Published 9 May 2023 as CVE-2023-27482: an authentication bypass in Home
Assistant's Supervisor integration reaching unauthenticated remote code
execution.

### Core contribution

Endpoints opting out of authentication were enumerated by searching for
`requires_auth = False`, and the Supervisor proxy's filtering was bypassed by
inserting characters such as a tab into the request path so the middleware and
the backend disagreed about the route.

### Prior art

Proxy-versus-backend path disagreement is a well-covered class, including
Orange Tsai's 2018 parser-logic work already held in the archive, and the
"authentication opt-out endpoint" review pattern is standard practice. The
finding is a competent application of both to one product.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 48 | 25% | 12.00 | Known middleware-bypass class applied to a new target. |
| Transferability | 55 | 20% | 11.00 | The review methodology transfers; the specific bypass does not. |
| Lasting value | 45 | 20% | 9.00 | Patched product-specific bug; little new to build on. |
| Technical soundness | 78 | 15% | 11.70 | Chain to RCE is demonstrated and credible. |
| Practical usability | 60 | 10% | 6.00 | Useful as a review pattern rather than a reusable primitive. |
| Clarity and reproducibility | 75 | 10% | 7.50 | Clear write-up with the request shapes shown. |

**Final score: 57.2/100.** Archive decision: do not include.

### Verdict

Useful application or case study. Below the 60 threshold: real impact, but the
underlying technique was already documented.
