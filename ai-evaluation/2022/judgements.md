# 2022 candidate judgements

These scorecards apply the repository's weighted judge rubric. `KEPT` means the
candidate met the historical 60-or-above inclusion rule as well as the
first-publication, originality-verdict and original-nomination exclusions.

## 88.8 — [Hertzbleed: Turning Power Side-Channel Attacks Into Remote Timing Attacks on x86](https://www.usenix.org/conference/usenixsecurity22/presentation/wang-yingchen) — Yingchen Wang et al.

**KEPT** · Original technique · confidence High

### Candidate

The coordinated public disclosure occurred on 14 June 2022; the peer-reviewed
paper appeared at USENIX Security in August 2022.

### Core contribution

Hertzbleed shows that data-dependent power consumption changes dynamic CPU
frequency and therefore remotely observable wall time. It extracts a
cryptographic key over a network even from software written to be constant-time.

### Prior art

Power analysis, remote timing attacks and DVFS effects were known separately.
No earlier public work turned power variation into this remote frequency/timing
channel against constant-time code on mainstream processors.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 94 | 25% | 23.50 | Defines a new remote channel through power-sensitive DVFS. |
| Transferability | 85 | 20% | 17.00 | The hardware effect spans processors and remotely invoked code. |
| Lasting value | 93 | 20% | 18.60 | Changes assumptions behind constant-time engineering. |
| Technical soundness | 94 | 15% | 14.10 | Reverse engineering and full key recovery substantiate it. |
| Practical usability | 65 | 10% | 6.50 | Exploitation needs amplification and many measurements. |
| Clarity and reproducibility | 91 | 10% | 9.10 | Channel, attack and limits are carefully documented. |

**Final score: 88.8/100.** Archive decision: include as a core technique.

### Verdict

Original technique. The web relevance is the remotely measurable timing channel;
the underlying cause materially broadens the server-side threat model.

## 88.0 — [FuzzOrigin: Detecting UXSS vulnerabilities in Browsers through Origin Fuzzing](https://www.usenix.org/conference/usenixsecurity22/presentation/kim) — Sunwoo Kim, Young Min Kim, Jaewon Hur, Suhwan Song, Gwangmu Lee, Byoungyoung Lee

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2022.

### Core contribution

FuzzOrigin tags origins, detects semantic cross-origin violations and prioritises
chained navigation and origin-update operations, allowing a browser fuzzer to
find UXSS bugs that ordinary crash or single-document fuzzing misses.

### Prior art

Browser fuzzers and origin-policy testing existed. The distinct contribution is
an origin-aware oracle and interaction generator designed for semantic UXSS.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | Adds an origin-aware UXSS oracle and navigation strategy. |
| Transferability | 90 | 20% | 18.00 | Works across major browser engines and origin transitions. |
| Lasting value | 88 | 20% | 17.60 | Durable model for semantic browser-security fuzzing. |
| Technical soundness | 94 | 15% | 14.10 | Multiple confirmed browser bugs validate the design. |
| Practical usability | 88 | 10% | 8.80 | Implemented fuzzer directly supports browser testing. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Oracle and generation logic are explicit. |

**Final score: 88.0/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It makes a difficult semantic vulnerability
class systematically fuzzable.

## 87.6 — [Rendering Contention Channel Made Practical in Web Browsers](https://www.usenix.org/conference/usenixsecurity22/presentation/wu-shujiang) — Shujiang Wu, Jianjia Yu, Min Yang, Yinzhi Cao

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2022.

### Core contribution

SIDER applies stable, self-adjusting rendering pressure and times frame sequences
to infer co-rendering activity. The channel enables cross-browser cookie syncing,
history sniffing, website fingerprinting and keystroke inference.

### Prior art

Single-frame rendering timing and browser CPU/cache channels were known. Sustained
rendering contention across CPU, GPU and screen buffers is a distinct channel.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 88 | 25% | 22.00 | Establishes rendering contention as a browser side channel. |
| Transferability | 88 | 20% | 17.60 | Supports several attacks across browser boundaries. |
| Lasting value | 86 | 20% | 17.20 | Expands browser isolation beyond cache-focused models. |
| Technical soundness | 92 | 15% | 13.80 | Causal tests and four demonstrated attacks support it. |
| Practical usability | 82 | 10% | 8.20 | Open framework and browser delivery make it usable. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Pressure control and measurements are documented. |

**Final score: 87.6/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It exposes a shared rendering resource rather than another
variant of a cache oracle.

## 87.0 — [Targeted Deanonymization via the Cache Side Channel](https://www.usenix.org/conference/usenixsecurity22/presentation/zaheri) — Mojtaba Zaheri, Yossi Oren, Reza Curtmola

**KEPT** · Meaningful combination or adaptation · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2022.

### Core contribution

A malicious site induces identity-dependent work in another browser context and
uses a JavaScript CPU-cache channel to determine whether the visitor owns a chosen
identifier. This bypasses CORP, COOP, SameSite and third-party-cookie defenses.

### Prior art

Targeted deanonymization and browser cache channels existed separately. Their
combination removes embedding and cookie assumptions that constrained XS-Leaks.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | Creates a defense-bypassing targeted identity oracle. |
| Transferability | 90 | 20% | 18.00 | Demonstrated across sites, CPUs, OSes and browsers. |
| Lasting value | 88 | 20% | 17.60 | Durable warning that process policy does not stop hardware leakage. |
| Technical soundness | 93 | 15% | 13.95 | Broad evaluation and fast attacks substantiate it. |
| Practical usability | 82 | 10% | 8.20 | A hostile page can deploy it, though profiling is needed. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Threat model, classifier and limitations are explicit. |

**Final score: 87.0/100.** Archive decision: include as a core technique.

### Verdict

Meaningful combination or adaptation. It materially changes the assumptions and
reach of targeted web deanonymization.

## 86.7 — [DRAWN APART: A Device Identification Technique based on Remote GPU Fingerprinting](https://orenlab.cis.bgu.ac.il/p/DrawnApart) — Tomer Laor et al.

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed NDSS paper published in 2022; the primary project page and
artifacts identify the NDSS 2022 publication.

### Core contribution

WebGL workloads expose manufacturing-level performance variation among execution
units of nominally identical GPUs, yielding a device-specific fingerprint that
substantially lengthens tracking when combined with ordinary browser attributes.

### Prior art

Canvas/WebGL fingerprinting identified models, drivers and rendered outputs.
DrawnApart's distinct contribution is remotely measuring within-model physical
variation to distinguish otherwise identical devices.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 84 | 25% | 21.00 | Adds manufacturing-variation GPU fingerprints. |
| Transferability | 88 | 20% | 17.60 | Integrates with broad browser fingerprinting systems. |
| Lasting value | 85 | 20% | 17.00 | Durable risk for hardware-exposing browser APIs. |
| Technical soundness | 94 | 15% | 14.10 | Controlled and crowdsourced longitudinal studies support it. |
| Practical usability | 80 | 10% | 8.00 | Deployable through unprivileged browser JavaScript. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Artifacts and workload design are available. |

**Final score: 86.7/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It crosses from configuration fingerprinting to physical
device discrimination using a browser-accessible GPU.

## 86.3 — [Phish in Sheep's Clothing](https://www.usenix.org/conference/usenixsecurity22/presentation/lin-xu) — Xu Lin, Panagiotis Ilia, Saumya Solanki, Jason Polakis

**KEPT** · Meaningful combination or adaptation · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2022.

### Core contribution

The method reconstructs each service's browser fingerprint vector, phishes those
attributes from a victim, then reproduces the vector on another device to defeat
risk-based authentication and suppress additional verification.

### Prior art

Browser fingerprinting, phishing and device impersonation were known. The
distinct contribution is exact service-specific fingerprint replication as an
authentication-bypass workflow.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 80 | 25% | 20.00 | Turns fingerprint collection into a concrete RBA bypass. |
| Transferability | 90 | 20% | 18.00 | Applies to many services and fingerprint constructions. |
| Lasting value | 87 | 20% | 17.40 | Durable warning against treating spoofable attributes as identity. |
| Technical soundness | 93 | 15% | 13.95 | Automated vectors and service tests validate it. |
| Practical usability | 82 | 10% | 8.20 | Attackers can add collection to realistic phishing. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Workflow and service observations are explicit. |

**Final score: 86.3/100.** Archive decision: include as a core technique.

### Verdict

Meaningful combination or adaptation. It makes browser fingerprinting an active
authentication-bypass component rather than merely a tracking signal.

## 86.0 — [Port Contention Goes Portable](https://thomasrokicki.github.io/publications/wpc.pdf) — Thomas Rokicki, Clémentine Maurice, Marina Botvinnik, Yossi Oren

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed AsiaCCS paper published in May 2022.

### Core contribution

WebAssembly workloads measure contention on CPU execution ports entirely inside
a browser. The framework maps instructions to port pressure and creates a fast
cross-browser covert channel resistant to cache- and timer-focused mitigations.

### Prior art

Native port-contention attacks and browser cache/event-loop channels were known.
The new contribution is a portable browser-only port channel and instruction
evaluation framework.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 86 | 25% | 21.50 | First practical browser-only CPU-port contention channel. |
| Transferability | 85 | 20% | 17.00 | Framework maps many WebAssembly instructions and contexts. |
| Lasting value | 86 | 20% | 17.20 | Broadens browser microarchitectural threat models. |
| Technical soundness | 91 | 15% | 13.65 | Covert-channel and resolution measurements validate it. |
| Practical usability | 78 | 10% | 7.80 | Browser delivery is easy but hardware mapping is specialised. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Method, artifacts and benchmarks are described. |

**Final score: 86.0/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It moves a distinct native microarchitectural channel into
the web platform rather than retuning an existing cache attack.

## 85.8 — [Identity Confusion in WebView-based Mobile App-in-app Ecosystems](https://www.usenix.org/conference/usenixsecurity22/presentation/zhang-lei) — Lei Zhang et al.

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2022.

### Core contribution

Super-apps inconsistently bind privileged WebView APIs to web domains, sub-app
IDs and capabilities. Confusing these identities grants a broader principal than
intended, enabling financial actions, data access and malware installation.

### Prior art

WebView bridges, origin confusion and mobile confused-deputy bugs were known.
The distinct contribution is the three-identity app-in-app authorization model
and systematic attack class across super-app ecosystems.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 86 | 25% | 21.50 | Defines identity confusion across three app-in-app principals. |
| Transferability | 85 | 20% | 17.00 | Appears across 47 super-app ecosystems and API types. |
| Lasting value | 85 | 20% | 17.00 | Durable model for embedded mini-app authorization. |
| Technical soundness | 92 | 15% | 13.80 | Systematic study and proof attacks substantiate it. |
| Practical usability | 78 | 10% | 7.80 | Provides concrete identity checks for audits. |
| Clarity and reproducibility | 87 | 10% | 8.70 | Identities and failure modes are clearly separated. |

**Final score: 85.8/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It identifies an authorization boundary specific to hybrid
app-in-app platforms, not just another unsafe WebView method.

## 85.3 — [HTTP/3 connection contamination: an upcoming threat?](https://portswigger.net/research/http-3-connection-contamination) — James Kettle

**KEPT** · Meaningful combination or adaptation · confidence Medium

### Candidate

PortSwigger Research published the work on 19 October 2022.

### Core contribution

Browser HTTP/2+ connection coalescing combines with a reverse proxy's
first-request routing to send a sibling origin's request to the wrong backend,
letting content from a weak sibling execute under a stronger origin. HTTP/3 can
broaden the condition by relaxing address matching.

### Prior art

Connection coalescing, first-request routing and host-header attacks were known.
Their browser-driven combination creates a distinct cross-origin capability.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 84 | 25% | 21.00 | Combines connection reuse and routing state into origin confusion. |
| Transferability | 88 | 20% | 17.60 | Applies to shared frontends, certificates and sibling hosts. |
| Lasting value | 88 | 20% | 17.60 | Important as HTTP/2 and HTTP/3 coalescing expands. |
| Technical soundness | 82 | 15% | 12.30 | Clear proof, though prevalence was not measured. |
| Practical usability | 78 | 10% | 7.80 | Testable with browser fetches and connection reuse. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Preconditions and proof sequence are explicit. |

**Final score: 85.3/100.** Archive decision: include as a core technique.

### Verdict

Meaningful combination or adaptation. This is connection-state origin confusion,
not another HTTP message-boundary desync.

## 84.4 — [Timing-Based Browsing Privacy Vulnerabilities Via Site Isolation](https://www.microsoft.com/en-us/research/publication/timing-based-browsing-privacy-vulnerabilities-via-site-isolation/) — Zihao Jin, Ziqiao Kong, Shuo Chen, Haixin Duan

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published in May 2022.

### Core contribution

Process allocation and contention introduced by site isolation become timing
oracles for which sites are loaded and which one the user is interacting with.
The attack works without privileged code or classic shared-cache assumptions.

### Prior art

Browser timing and process-contention channels were known. The distinct
contribution is exploiting site isolation's finite process allocation itself.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 83 | 25% | 20.75 | Derives privacy oracles from site-isolation process state. |
| Transferability | 86 | 20% | 17.20 | Applies broadly to isolated cross-site frames and tabs. |
| Lasting value | 84 | 20% | 16.80 | Exposes a durable security-versus-resource tension. |
| Technical soundness | 90 | 15% | 13.50 | Broad site evaluation supports the attack. |
| Practical usability | 76 | 10% | 7.60 | Remote and robust, though timing classification is needed. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Metrics and attack conditions are documented. |

**Final score: 84.4/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It turns a modern defensive architecture into a new
browsing-state timing surface.

## 83.6 — [The Dangers of Human Touch](https://www.usenix.org/conference/usenixsecurity22/presentation/solomos) — Konstantinos Solomos, Panagiotis Ilia, Soroush Karami, Nick Nikiforakis, Jason Polakis

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2022.

### Core contribution

Pages simulate mouse and keyboard actions to trigger otherwise dormant extension
behaviour, then fingerprint DOM effects. Action templates reveal thousands of
extensions, including many missed by prior passive techniques.

### Prior art

Extension fingerprinting through resources, styles and injected DOM was known.
The new contribution is systematic user-action activation of hidden behaviour.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 76 | 25% | 19.00 | Adds action-triggered extension revelation. |
| Transferability | 88 | 20% | 17.60 | Templates cover many extensions and user interactions. |
| Lasting value | 82 | 20% | 16.40 | Durable warning about trusting synthetic browser events. |
| Technical soundness | 92 | 15% | 13.80 | Large extension analysis and evaluation support it. |
| Practical usability | 80 | 10% | 8.00 | A web page can exercise the attack directly. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Templates and results are explicit. |

**Final score: 83.6/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It expands extension fingerprinting into interaction-gated
functionality rather than repeating passive probing.

## 83.2 — [Probe the Proto](https://www.ndss-symposium.org/ndss-paper/auto-draft-207/) — Zifeng Kang, Song Li, Yinzhi Cao

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed NDSS paper published in April 2022.

### Core contribution

ProbeTheProto combines dynamic joint-taint tracking with exploit-input generation
to connect client-side prototype-pollution sources to concrete sinks such as XSS,
cookie manipulation and URL manipulation at Internet scale.

### Prior art

Prototype pollution and manual client-side gadgets were public by 2020–2021. The
distinct contribution is scalable source-to-consequence analysis and generation.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 70 | 25% | 17.50 | Advances analysis rather than inventing prototype pollution. |
| Transferability | 91 | 20% | 18.20 | Covers diverse sites, inputs and consequence sinks. |
| Lasting value | 83 | 20% | 16.60 | Durable model for source/gadget exploitability analysis. |
| Technical soundness | 93 | 15% | 13.95 | Million-site run and verified outcomes support it. |
| Practical usability | 82 | 10% | 8.20 | Automated generation produces actionable exploits. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Taint and generation stages are documented. |

**Final score: 83.2/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It is distinct from the original list's
server-side prototype-poisoning guidance and earlier manual browser gadgets.

## 83.0 — [Wobfuscator](https://doi.org/10.1109/SP46214.2022.00064) — Alan Romano, Daniel Lehmann, Michael Pradel, Weihang Wang

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed IEEE Symposium on Security and Privacy paper published in May 2022.

### Core contribution

Wobfuscator selectively translates behaviour from malicious JavaScript into
WebAssembly while preserving integration with the page, evading detectors that
assume JavaScript is the sole executable representation.

### Prior art

JavaScript obfuscation, WebAssembly and malware evasion existed. Opportunistic
cross-language translation specifically to defeat JS malware analysis is distinct.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 80 | 25% | 20.00 | Introduces selective JS-to-Wasm detector evasion. |
| Transferability | 85 | 20% | 17.00 | Applies to many scripts and static detectors. |
| Lasting value | 80 | 20% | 16.00 | Durable mixed-language analysis lesson. |
| Technical soundness | 90 | 15% | 13.50 | Transformations and detector tests substantiate it. |
| Practical usability | 78 | 10% | 7.80 | Automated but constrained by translatable code. |
| Clarity and reproducibility | 87 | 10% | 8.70 | Rules and evaluation are explicit. |

**Final score: 83.0/100.** Archive decision: include as a core technique.

### Verdict

Original technique. Its offensive contribution is a new cross-language malware
evasion path, not generic code minification.

## 83.0 — [GET /out: Automated Discovery of Application-Layer Censorship Evasion Strategies](https://www.usenix.org/conference/usenixsecurity22/presentation/harrity) — Michael Harrity, Kevin Bock, Frederick Sell, Dave Levin

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2022.

### Core contribution

The system mutates HTTP and DNS application messages, measures censor behaviour
from affected networks and automatically discovers deployable evasion strategies
without privileged TCP/IP-header manipulation.

### Prior art

Manual HTTP censorship bypasses and automated transport-header mutation existed.
The distinct contribution is automated search in structured application messages.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 76 | 25% | 19.00 | Moves automated evasion discovery to HTTP and DNS messages. |
| Transferability | 88 | 20% | 17.60 | Generalises across censors and application protocols. |
| Lasting value | 80 | 20% | 16.00 | Durable differential-testing method for middleboxes. |
| Technical soundness | 91 | 15% | 13.65 | Multi-country live measurements validate it. |
| Practical usability | 82 | 10% | 8.20 | Findings can be deployed without privileged packet access. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Mutation and measurement strategy are specified. |

**Final score: 83.0/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It systematises application-layer HTTP
evasion rather than contributing another manually found parser quirk.

## 82.9 — [Counting in Regexes Considered Harmful](https://www.usenix.org/conference/usenixsecurity22/presentation/turonova) — Lenka Turoňová et al.

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2022.

### Core contribution

Bounded repetition forces expensive deterministic-automaton simulations in
nonbacktracking regex engines. The generator creates ReDoS inputs against engines
previously treated as safe from catastrophic backtracking.

### Prior art

Classic ReDoS targets backtracking engines. This work exposes a different
complexity mechanism in nonbacktracking matchers and automates its exploitation.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 74 | 25% | 18.50 | Extends ReDoS to bounded repetition in DFA simulation. |
| Transferability | 85 | 20% | 17.00 | Applies across nonbacktracking matchers and applications. |
| Lasting value | 83 | 20% | 16.60 | Corrects a durable assumption about safe regex engines. |
| Technical soundness | 92 | 15% | 13.80 | Broad engine and real-application tests support it. |
| Practical usability | 82 | 10% | 8.20 | Generator yields concrete denial-of-service inputs. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Complexity trigger and evaluation are clear. |

**Final score: 82.9/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. The outcome is ReDoS, but the vulnerable engine model and
complexity trigger are materially different from backtracking attacks.

## 82.2 — [Mining Node.js Vulnerabilities via Object Dependence Graph and Query](https://www.usenix.org/conference/usenixsecurity22/presentation/li-song) — Song Li, Mingqing Kang, Jianwei Hou, Yinzhi Cao

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2022.

### Core contribution

ODGEN models dynamic JavaScript object definitions, lookups and dependencies with
flow-, context- and branch-sensitive analysis, then expresses multiple Node.js
vulnerability classes as graph queries instead of building one analyser per class.

### Prior art

Code-property graphs and single-class Node.js analysers existed. The distinct
contribution is an object-dependence representation suited to JavaScript dynamics.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 70 | 25% | 17.50 | Adds a JavaScript-specific object-dependence graph. |
| Transferability | 88 | 20% | 17.60 | Queries model many packages and vulnerability classes. |
| Lasting value | 83 | 20% | 16.60 | Durable basis for extensible Node.js analysis. |
| Technical soundness | 93 | 15% | 13.95 | Broad class coverage and confirmed findings support it. |
| Practical usability | 80 | 10% | 8.00 | Open prototype and graph queries support audits. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Abstraction and evaluation are documented. |

**Final score: 82.2/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It systematises vulnerability mining rather
than claiming its detected injection and pollution classes as new.

## 81.7 — [Silent Spring: Prototype Pollution Leads to Remote Code Execution in Node.js](https://arxiv.org/abs/2207.11171) — Mikhail Shcherbakov, Musard Balliu, Cristian-Alexandru Staicu

**KEPT** · Original technique · confidence High

### Candidate

The complete public preprint was published on 22 July 2022; the paper was later
presented at USENIX Security in August 2023. Neither its URL nor its contribution
appears in the original 2022 nomination set.

### Core contribution

The paper combines prototype-pollution detection with hybrid universal-gadget
analysis, finds eleven Node.js core gadgets, and demonstrates eight end-to-end RCE
chains in full applications.

### Prior art

Prototype pollution, Node.js RCE gadgets and individual application chains were
known. The original nomination's prototype-poisoning explainer does not provide
this app-to-universal-gadget discovery method, while Probe the Proto performs
client-side source-to-sink analysis rather than Node.js core-gadget discovery.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 70 | 25% | 17.50 | Strong systematic gadget methodology. |
| Transferability | 85 | 20% | 17.00 | Applies across Node.js applications and core APIs. |
| Lasting value | 84 | 20% | 16.80 | Influenced later prototype-gadget research. |
| Technical soundness | 92 | 15% | 13.80 | Tools and end-to-end exploits validate it. |
| Practical usability | 76 | 10% | 7.60 | Analysis is usable but requires expert triage. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Paper and artifacts document the method. |

**Final score: 81.7/100.** Archive decision: include as a core technique.

### Verdict

Original technique. Its server-side universal-gadget analysis is a separate
mechanism from the original explainer and Probe the Proto's client-side tooling.

## 80.3 — [Pre-hijacked Accounts](https://arxiv.org/abs/2205.10174) — Avinash Sudhodanan, Andrew Paverd

**KEPT** · Meaningful extension · confidence High

### Candidate

The primary preprint was published on 20 May 2022. This entry existed in the
retrospective section before the current audit and is retained once.

### Core contribution

Five attacks let an adversary act before a victim creates an account, then retain
or regain access after conventional or federated registration, recovery or email
change merges the attacker's state into the victim's account.

### Prior art

Preemptive account hijacking and SSO account confusion were known. The paper
generalises these into a class, adds four mechanisms and derives requirements.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | Defines and expands a coherent pre-hijacking class. |
| Transferability | 80 | 20% | 16.00 | Applies across conventional and federated account flows. |
| Lasting value | 79 | 20% | 15.80 | Durable guidance for account-state lifecycle design. |
| Technical soundness | 88 | 15% | 13.20 | Service study and attack taxonomy support it. |
| Practical usability | 73 | 10% | 7.30 | Requires service-specific lifecycle behaviour. |
| Clarity and reproducibility | 75 | 10% | 7.50 | Mechanisms are clear, though reproduction details vary. |

**Final score: 80.3/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It turns a prior isolated account-merging idea into a
reusable taxonomy of pre-registration attack states.

## 80.2 — [Testability Tarpits](https://www.ndss-symposium.org/ndss-paper/auto-draft-206/) — Feras Al Kassar, Giulia Clerici, Luca Compagna, Davide Balzarotti, Fabian Yamaguchi

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed NDSS paper published in April 2022.

### Core contribution

The work catalogues more than 270 PHP and JavaScript code patterns that prevent
SAST tools from building usable models, detects these blind spots in projects and
shows that refactoring them reveals previously missed vulnerabilities.

### Prior art

SAST false negatives and a small number of coding-style cases were known. The
distinct contribution is a broad testability taxonomy, rules and validation.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 60 | 25% | 15.00 | Systematises analysis blind spots rather than a new bug class. |
| Transferability | 90 | 20% | 18.00 | Covers languages, applications and several scanners. |
| Lasting value | 82 | 20% | 16.40 | Durable concept for interpreting negative scanner results. |
| Technical soundness | 92 | 15% | 13.80 | Cross-tool experiments and newly exposed bugs support it. |
| Practical usability | 82 | 10% | 8.20 | Detection rules and refactoring guidance are actionable. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Pattern catalogue and experiments are detailed. |

**Final score: 80.2/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It adds a reusable way to detect when web
code is untestable by common analysis tools.

## 79.8 — [Experimental Security Analysis of the App Model in Business Collaboration Platforms](https://www.usenix.org/conference/usenixsecurity22/presentation/chen-yunang-experimental) — Yunang Chen et al.

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2022.

### Core contribution

Slack- and Teams-style apps can exploit missing mediation and provenance across
user delegation, bot interactions, commands and linked resources to impersonate
users, trigger other apps and read data beyond granted scopes.

### Prior art

OAuth scope failures and third-party app privilege escalation were known. The
distinct contribution is the multi-app delegation/provenance attack model for
business collaboration platforms.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 72 | 25% | 18.00 | Adds platform-specific delegation and provenance attacks. |
| Transferability | 84 | 20% | 16.80 | Applies across apps, resources and collaboration platforms. |
| Lasting value | 78 | 20% | 15.60 | Durable access-control lesson for integrated app ecosystems. |
| Technical soundness | 91 | 15% | 13.65 | Systematic interaction analysis and proofs support it. |
| Practical usability | 72 | 10% | 7.20 | Testing requires platform apps and permissions. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Roles and attack paths are clearly defined. |

**Final score: 79.8/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It identifies attack composition across delegated web apps,
not just another overly broad OAuth scope.

## 79.2 — [The Security Lottery](https://www.usenix.org/conference/usenixsecurity22/presentation/roth) — Sebastian Roth, Stefano Calzavara, Moritz Wilhelm, Alvise Rabitti, Ben Stock

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2022.

### Core contribution

The method formalises semantic consistency for browser security headers and
compares responses across user agents, networks and languages, revealing client
characteristics that deterministically receive weaker CSP, HSTS or related policy.

### Prior art

Missing and misconfigured headers were known. The distinct contribution is
cross-client semantic differential analysis of delivered security guarantees.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 62 | 25% | 15.50 | Adds semantic differential policy analysis. |
| Transferability | 88 | 20% | 17.60 | Applies to policies, sites and client dimensions. |
| Lasting value | 80 | 20% | 16.00 | Durable warning against testing only one response variant. |
| Technical soundness | 92 | 15% | 13.80 | Formalisation and large response dataset support it. |
| Practical usability | 76 | 10% | 7.60 | Requires multi-vantage collection but yields testable weaknesses. |
| Clarity and reproducibility | 87 | 10% | 8.70 | Guarantees and dimensions are explicit. |

**Final score: 79.2/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It moves header auditing from presence checks
to adversarial comparison of effective policy across clients.

## 76.9 — [Characterizing the Security of GitHub CI Workflows](https://www.usenix.org/conference/usenixsecurity22/presentation/koishybayev) — Igibek Koishybayev et al.

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2022.

### Core contribution

The work defines admittance, execution, code and secret-access properties for CI,
checks hundreds of thousands of GitHub workflows and implements GWChecker to flag
overprivileged, attacker-triggerable and untrusted-action patterns.

### Prior art

CI secret theft and supply-chain workflow attacks were established, including in
earlier year lists. The contribution is a reusable property model and checker.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 54 | 25% | 13.50 | Systematises known CI risks rather than inventing them. |
| Transferability | 87 | 20% | 17.40 | Properties generalise across CI/CD platforms. |
| Lasting value | 78 | 20% | 15.60 | Useful baseline for workflow security review. |
| Technical soundness | 92 | 15% | 13.80 | Large workflow study and comparisons support it. |
| Practical usability | 80 | 10% | 8.00 | GWChecker produces actionable warnings. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Properties and risky patterns are explicit. |

**Final score: 76.9/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It qualifies for systematic CI analysis,
not for rediscovering arbitrary-code or secret-exposure outcomes.

## 75.3 — [Leaky Forms](https://www.usenix.org/conference/usenixsecurity22/presentation/senol) — Asuman Senol, Gunes Acar, Mathias Humbert, Frederik Zuiderveen Borgesius

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2022.

### Core contribution

A crawler fills but does not submit email and password fields, intercepts script
access and network traffic, and identifies third-party exfiltration that occurs
before consent or an explicit form submission.

### Prior art

Third-party trackers, session replay and reading form inputs from JavaScript were
known. The distinct contribution is a controlled non-submission test methodology
and systematic attribution of the resulting leaks.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 52 | 25% | 13.00 | The mechanism is known; the controlled measurement is new. |
| Transferability | 88 | 20% | 17.60 | Applies to sites, fields, scripts and jurisdictions. |
| Lasting value | 76 | 20% | 15.20 | Useful audit model for pre-consent collection. |
| Technical soundness | 91 | 15% | 13.65 | Multi-vantage crawl and script/network checks support it. |
| Practical usability | 72 | 10% | 7.20 | Reuse requires crawler instrumentation. |
| Clarity and reproducibility | 87 | 10% | 8.70 | Collection conditions and findings are detailed. |

**Final score: 75.3/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It qualifies as a reusable way to expose
silent pre-submission collection, not as a novel JavaScript read primitive.

## 72.6 — [.NET Remoting Revisited](https://code-white.com/blog/2022-01-dotnet-remoting-revisited/)

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Markus Wulftange, Code White, 27 January 2022 (also posted to the Code White
blogspot). Surfaced by the 2026-08-12 pass over the ysonet .NET-deserialization
reference set.

### Core contribution

The reference treatment of .NET Remoting as an attack surface: how the channel
sink chains are assembled, what each security feature actually enforces, and
where each one fails. It works through the TypeFilterLevel low/full split, shows
that the restriction is applied to the message body but not to every path that
reaches a formatter, and demonstrates that a service can be attacked without any
MarshalByRefObject interface. It ships the results as reusable tooling — major
additions to ExploitRemotingService, a new ObjRef gadget for ysoserial.net, and
RogueRemotingServer as the attacker-side counterpart — so the findings are
executable rather than descriptive. The web-relevant part is the HTTP channel,
which IIS and ASP.NET expose by default through the .rem and .soap handler
mappings.

### Prior art

Forshaw's 2012 Black Hat talk introduced .NET Remoting as a serialization target
and produced ExploitRemotingService; his 2014 and 2019 posts covered the low
type-filter level. NCC Group's "Finding and Exploiting .NET Remoting over HTTP
using Deserialisation" is already in the 2019 list and establishes the HTTP
vector. This post's distinct gain is the systematic security-feature-by-bypass
mapping and the ObjRef gadget, neither of which existed as a single reusable
body of work. It is not a duplicate of the 2022 list's "Bypassing .NET
Serialization Binders", which is a different Code White post about binder
implementations rather than the Remoting channel.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 66 | 25% | 16.50 | The ObjRef gadget and several feature bypasses are new; the protocol's exploitability and the base tooling were already established by Forshaw and NCC. |
| Transferability | 60 | 20% | 12.00 | The HTTP channel and the ObjRef gadget carry into web work; the TCP and IPC material, which is most of the post, does not. |
| Lasting value | 74 | 20% | 14.80 | Became the citation of record for .NET Remoting exploitation, and the 2024 follow-up already on the 2024 list builds directly on it. |
| Technical soundness | 86 | 15% | 12.90 | Each claim is traced through reference source and demonstrated with released code. |
| Practical usability | 80 | 10% | 8.00 | Three pieces of working tooling accompany the analysis. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Long, well-structured, and specific about preconditions. |

**Final score: 72.6/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It systematises an under-documented remote
invocation surface and ships the gadget and servers that make the analysis
reusable.

### Reverification

- **Candidate facts rechecked against:** the Code White byline, which gives
  27 January 2022 and the author, and the archived text for the tooling claims.
- **Independent prior-art check:** searched backward by mechanism (TypeFilterLevel
  bypass, ObjRef as a deserialization gadget, .NET Remoting over HTTP) and
  checked the 2012, 2019 and 2022 lists. Forshaw's and NCC's work is earlier and
  narrower; no earlier source states the ObjRef gadget.
- **Strongest challenge to the result:** .NET Remoting is a deprecated RPC
  protocol whose common transports are TCP and IPC, which is not web.
- **Benefit-of-doubt check:** the HTTP channel is enabled by default under IIS,
  the repository already nominated the 2019 HTTP-Remoting work and the 2024
  successor from the same team, and the ObjRef gadget is transport-independent.
- **Changes after reverification:** transferability was cut from a draft 72 to 60
  to reflect how much of the post is non-web transport; the final score fell
  from 75.0 to 72.6.

## 57.0 — [The Perils of Expired Domains - We're Reading Your Email](https://labs.watchtowr.com/the-perils-of-expired-domains-were-reading-your-email/) — Benjamin Harris, watchTowr

**REMOVED** · Useful application or case study · confidence High

### Candidate

Benjamin Harris, watchTowr Labs, 23 August 2022. Judged in the 2026-08-12
publisher sweep, as the earliest entry in this team's abandoned-infrastructure
line and therefore as prior art for their 2024 and 2025 work.

### Core contribution

Organisations retire a mail host, let the hostname's domain lapse, and leave the
MX record pointing at it while real delivery falls through to a surviving server.
Registering the lapsed name makes the attacker a valid mail exchanger for the
affected domain, and mail arrives. The post's own contribution is the observation
that this is prolific on subdomains, where nobody audits the records.

### Prior art

Dangling DNS records and hostile subdomain takeover were established well before
2022 - Frans Rosén's subdomain takeover work dates from 2014, and the
NS/MX/CNAME variants were public throughout the intervening years. Applying the
known class to MX specifically, on a corpus of subdomains, is coverage of that
class rather than a distinct primitive.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 40 | 25% | 10.00 | An MX-shaped instance of dangling-record takeover, a class public since 2014. |
| Transferability | 58 | 20% | 11.60 | The audit-your-lapsed-MX lesson is broadly applicable but is the known class restated. |
| Lasting value | 48 | 20% | 9.60 | Useful as evidence of prevalence; the same team's later work is what changed the model. |
| Technical soundness | 76 | 15% | 11.40 | The mechanism is correct and demonstrated, with prevalence asserted rather than quantified. |
| Practical usability | 66 | 10% | 6.60 | Directly actionable for both attack and audit. |
| Clarity and reproducibility | 78 | 10% | 7.80 | Clear and stepwise. |

**Final score: 57.0/100.** Archive decision: do not include.

### Verdict

Useful application or case study. It is the first of this team's
abandoned-infrastructure posts and is recorded here as prior art for the 2024
.MOBI and 2025 abandoned-bucket entries, but on its own it restates a class that
was already eight years old.

### Reverification

- **Candidate facts rechecked against:** the post, which carries the 23 August
  2022 date and author.
- **Independent prior-art check:** searched dangling MX and subdomain-takeover
  history back through 2014 rather than searching the post's own title.
- **Strongest challenge to the result:** it is the seed of a line of research
  that later produced two qualifying entries.
- **Benefit-of-doubt check:** being the seed is credited where it belongs - in
  the prior-art sections of the 2024 and 2025 cards, which lowered .MOBI's
  originality score - not by inflating this one.
- **Changes after reverification:** none.
