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
