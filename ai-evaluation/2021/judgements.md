# 2021 candidate judgements

These scorecards apply the repository's weighted judge rubric. `KEPT` means the
candidate met the historical 60-or-above inclusion rule as well as the
first-publication, originality-verdict and original-nomination exclusions.

## 85.5 — [Spook.js: Attacking Chrome Strict Site Isolation via Speculative Execution](https://www.spookjs.com/)

**KEPT** · Meaningful extension · confidence High

### Candidate

The researchers publicly disclosed the work, paper and proof of concept in
September 2021; its eventual IEEE S&P publication was in 2022.

### Core contribution

Spook.js combines same-eTLD+1 renderer co-location with speculative type
confusion that recovers 64-bit pointers from Chrome's 32-bit renderer sandbox.
A malicious same-site page can read co-located pages, while a malicious
extension can read data from other extensions sharing its process.

### Prior art

Spectre was a 2018 Top 10 technique, and browser/site-isolation weaknesses were
already studied. This work's distinct gain is a concrete attack that defeats
Chrome's strict isolation assumptions and renderer sandbox in the deployed Web
process model; it does not claim speculative execution itself as new.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 84 | 25% | 21.00 | Composes co-location and speculative type confusion into a new isolation bypass. |
| Transferability | 82 | 20% | 16.40 | Applies to same-site pages and extension process sharing. |
| Lasting value | 90 | 20% | 18.00 | Exposes a durable boundary between origin grouping and process isolation. |
| Technical soundness | 90 | 15% | 13.50 | End-to-end data recovery and vendor response substantiate the model. |
| Practical usability | 78 | 10% | 7.80 | The exploit is concrete but hardware and co-location conditions matter. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Paper, website, code and demonstrations disclose the chain. |

**Final score: 85.5/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It turns established Spectre primitives into a distinct
and demonstrated bypass of Chrome's strict Site Isolation deployment.

## 84.4 — [Prime+Probe 1, JavaScript 0: Overcoming Browser-based Side-Channel Defenses](https://arxiv.org/abs/2103.04952)

**KEPT** · Meaningful extension · confidence High

### Candidate

The primary preprint was public on 8 March 2021 and the work appeared at USENIX
Security 2021.

### Core contribution

The attack implements a browser cache Prime+Probe side channel entirely with
CSS and HTML. It remains viable when JavaScript is disabled, crosses Intel,
AMD, Exynos and Apple M1 systems, and bypasses defenses whose assumptions focus
on JavaScript timers or script execution.

### Prior art

Prime+Probe, browser cache attacks and scriptless CSS information leaks were
known. Replacing the complete cache-probing and timing path with declarative Web
features, across architectures and hardened browsers, is the qualifying gain.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | Establishes a complete scriptless cache-probing construction. |
| Transferability | 88 | 20% | 17.60 | Works across major CPU families and browser configurations. |
| Lasting value | 85 | 20% | 17.00 | Invalidates a durable class of JavaScript-centered mitigations. |
| Technical soundness | 90 | 15% | 13.50 | Cross-platform experiments support the claimed channel. |
| Practical usability | 76 | 10% | 7.60 | Requires careful cache and rendering measurement but no script. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Construction, targets and evaluations are documented. |

**Final score: 84.4/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. The underlying cache channel is known, but moving its
entire operation outside JavaScript materially changes the attack surface.

## 83.7 — [Tales of Favicons and Caches: Persistent Tracking in Modern Browsers](https://www.ndss-symposium.org/ndss-paper/tales-of-favicons-and-caches-persistent-tracking-in-modern-browsers/)

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed NDSS work first published in early 2021; neither its primary URL
nor mechanism appeared in the 41-link exclusion set.

### Core contribution

The tracker encodes identifier bits as favicon-cache entries on attacker
subdomains, then redirects through those hosts and observes which icons the
browser fetches. The identifier survives ordinary data clearing and private-
browsing boundaries in affected browsers without overwriting existing state.

### Prior art

Browser-cache history sniffing, cache identifiers and supercookies were known.
The separately managed favicon cache and its redirect-addressable bit store form
a new persistent state channel with unusual clearing and isolation behavior.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 86 | 25% | 21.50 | Introduces the favicon cache as an addressable persistent identifier store. |
| Transferability | 84 | 20% | 16.80 | The technique spans sites, sessions and affected browser modes. |
| Lasting value | 82 | 20% | 16.40 | Reveals a durable risk in secondary browser caches. |
| Technical soundness | 88 | 15% | 13.20 | Browser experiments and a working construction validate it. |
| Practical usability | 76 | 10% | 7.60 | Redirect cost exists, but the tracker is practical and non-destructive. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Encoding, decoding and browser differences are explained. |

**Final score: 83.7/100.** Archive decision: include as a core technique.

### Verdict

Original technique. The favicon cache is not merely another target application;
its independently persistent entries create the attack's state primitive.

## 83.5 — [JAW: Studying Client-side CSRF with Hybrid Property Graphs and Declarative Traversals](https://www.usenix.org/conference/usenixsecurity21/presentation/khodayari)

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed USENIX Security research published in 2021, with its primary URL
and client-side request-forgery mechanism absent from the original list.

### Core contribution

Client-side CSRF occurs when attacker-controlled JavaScript inputs, such as a
URL fragment, flow through trusted client code that constructs a state-changing
request. JAW models pages as hybrid property graphs and uses declarative graph
traversals to find forgeable requests and generate concrete exploits at scale.

### Prior art

Classical CSRF makes the browser submit an attacker-shaped request, while DOM
taint analysis and request mining were known. Here the victim application's own
client logic becomes the confused deputy that shapes and sends the request.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 80 | 25% | 20.00 | Defines and operationalizes a distinct client-side CSRF class. |
| Transferability | 85 | 20% | 17.00 | Applies across input sources, client frameworks and request sinks. |
| Lasting value | 82 | 20% | 16.40 | Captures a durable confused-deputy pattern in rich Web clients. |
| Technical soundness | 90 | 15% | 13.50 | Large-scale analysis and validated exploits support the model. |
| Practical usability | 84 | 10% | 8.40 | The graph queries and generated requests make findings actionable. |
| Clarity and reproducibility | 82 | 10% | 8.20 | The property graph, query model and results are explicit. |

**Final score: 83.5/100.** Archive decision: include as a core technique.

### Verdict

Original technique. Its defining primitive is attacker control over the trusted
client request builder, not a new wrapper around conventional CSRF.

## 82.3 — [Abusing Hidden Properties to Attack the Node.js Ecosystem](https://www.usenix.org/conference/usenixsecurity21/presentation/xiao)

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in 2021. Semantic comparison was
performed against the original list's Prototype Pollution nomination.

### Core contribution

Hidden Property Abuse follows attacker-supplied properties as application
objects are shared, copied and passed between Node.js components, then finds
where an undocumented or security-sensitive property changes control flow.
Lynx combines analysis and exploit synthesis and exposed previously unknown
vulnerabilities.

### Prior art

Prototype pollution, mass assignment and unsafe JavaScript object merging were
known. HPA does not require mutating the global prototype: its primitive is the
propagation of attacker-owned properties into a component that assigns special
meaning to the same property name.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | Isolates cross-component hidden-property collisions as an attack primitive. |
| Transferability | 82 | 20% | 16.40 | Object sharing is common across Node.js packages and applications. |
| Lasting value | 80 | 20% | 16.00 | Remains relevant to dynamic object-centric ecosystems. |
| Technical soundness | 88 | 15% | 13.20 | Analysis, synthesis and newly validated vulnerabilities align. |
| Practical usability | 80 | 10% | 8.00 | Lynx turns the model into testable exploit paths. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Sources, propagation and trigger conditions are defined. |

**Final score: 82.3/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It is semantically distinct from the listed prototype-
pollution work because no inherited global prototype mutation is required.

## 81.8 — [DNS Cache Poisoning Attack: Resurrections with Side Channels](https://www.cs.ucr.edu/~zhiyunq/pub/ccs21_dns_poisoning.pdf)

**KEPT** · Meaningful extension · confidence High

### Candidate

The author-hosted ACM CCS 2021 paper was first published in 2021 and was absent
from the original nomination links.

### Core contribution

New Linux ICMP side channels reveal the ephemeral UDP source port used for a
DNS query, reducing the remaining search to transaction identifiers and making
off-path cache poisoning practical again. The analysis spans ICMP, UDP and DNS
and demonstrates impact across BIND, Unbound and dnsmasq deployments.

### Prior art

Kaminsky poisoning, port randomization bypasses and the 2020 SADDNS ICMP side
channel are explicit prior art. The qualifying contribution is a new set of
kernel feedback paths that restores the off-path oracle after prior fixes.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 76 | 25% | 19.00 | Finds new cross-layer side channels after earlier oracle closure. |
| Transferability | 82 | 20% | 16.40 | Affects multiple resolvers on widely deployed Linux systems. |
| Lasting value | 84 | 20% | 16.80 | Demonstrates the recurring danger of shared network-stack state. |
| Technical soundness | 92 | 15% | 13.80 | Kernel analysis and resolver/internet validation are extensive. |
| Practical usability | 72 | 10% | 7.20 | Off-path timing and packet guessing remain operational constraints. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Side channels, attack sequence and affected systems are detailed. |

**Final score: 81.8/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. DNS poisoning is established, but the new ICMP/kernel
oracles materially resurrect it after contemporary randomization defenses.

## 80.4 — [Processing Dangerous Paths: On Security and Privacy of the Portable Document Format](https://www.ndss-symposium.org/ndss-paper/processing-dangerous-paths-on-security-and-privacy-of-the-portable-document-format/)

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2021. Its mechanism is distinct
from 2020 browser-oriented PDF data-exfiltration work.

### Core contribution

The study systematically follows standard PDF object, action and file-
specification paths through native and server-side processors. Crafted files
use legitimate features for denial of service, local-file and NTLM leakage,
form-data extraction or modification, local writes and embedded execution; 26
of 28 tested applications were affected.

### Prior art

Malicious PDFs, JavaScript actions and launch behavior were known. The distinct
gain is the specification-driven dangerous-path model and its new combinations
of standard actions, local resources and processing contexts.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 74 | 25% | 18.50 | Systematizes and extends attacks through standards-defined PDF paths. |
| Transferability | 84 | 20% | 16.80 | Affects diverse desktop, browser-backed and server processors. |
| Lasting value | 80 | 20% | 16.00 | The specification-path method survives individual implementation fixes. |
| Technical soundness | 88 | 15% | 13.20 | Broad product testing and disclosures substantiate the families. |
| Practical usability | 75 | 10% | 7.50 | Crafted PDFs are usable, though effects vary by product. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Object paths, actions and tested outcomes are explicit. |

**Final score: 80.4/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It derives reusable attack families from a systematic PDF
processing graph rather than reporting another isolated malicious-document bug.

## 80.0 — [ALPACA: Application Layer Protocol Confusion — Analyzing and Mitigating Cracks in TLS Authentication](https://alpaca-attack.com/)

**KEPT** · Original technique · confidence High

### Candidate

The researchers publicly disclosed ALPACA on 9 June 2021; it appeared at USENIX
Security 2021 and was already present in this year's missed section.

### Core contribution

An attacker redirects HTTPS traffic to a TLS service such as SMTP, IMAP, POP3
or FTP that presents a certificate acceptable for the intended Web host. TLS
authentication succeeds, but application-protocol confusion lets the attacker
reflect or store HTTP-shaped content and build cookie theft or XSS variants.

### Prior art

Cross-protocol HTTP attacks existed by 2001, and a TLS-secured instance was
demonstrated in 2014. ALPACA's distinct contribution is the generalized TLS-
content-confusion model, systematic client/server study and Internet-wide
evidence across multiple application protocols.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | Generalizes TLS-authenticated cross-protocol content confusion. |
| Transferability | 84 | 20% | 16.80 | Crosses browsers, servers and several text-based TLS protocols. |
| Lasting value | 82 | 20% | 16.40 | Exposes a durable gap between certificate identity and protocol intent. |
| Technical soundness | 88 | 15% | 13.20 | Systematic experiments and Internet measurements support the class. |
| Practical usability | 58 | 10% | 5.80 | Requires traffic redirection, certificate compatibility and server behavior. |
| Clarity and reproducibility | 73 | 10% | 7.30 | Attack variants and mitigations are documented. |

**Final score: 80.0/100.** Archive decision: include as a core technique.

### Verdict

Original technique. Earlier examples establish ancestry, but the reusable
multi-protocol TLS authentication-confusion class was not previously organized.

## 78.7 — [SerialDetector: Principled and Practical Exploration of Object Injection Vulnerabilities for the Web](https://www.ndss-symposium.org/ndss-paper/serialdetector-principled-and-practical-exploration-of-object-injection-vulnerabilities-for-the-web/)

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2021. Its URL was new, while its
underlying object-injection family was checked against older serialization and
gadget-chain entries.

### Core contribution

SerialDetector models data flow from HTTP entry points through arbitrary-type
instantiation to trigger methods, searches .NET applications for viable gadget
paths and validates exploitability. It recovers public gadgets and found new
remote-code-execution vulnerabilities, including Azure DevOps findings.

### Prior art

Unsafe deserialization, object injection and gadget chains were long
established. The new value lies in principled whole-application exploration and
validation rather than the underlying vulnerability class.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 64 | 25% | 16.00 | Adds a systematic dataflow model for known object-injection mechanics. |
| Transferability | 78 | 20% | 15.60 | Generalizes across .NET Web applications and gadget libraries. |
| Lasting value | 82 | 20% | 16.40 | Principled gadget exploration remains useful beyond found bugs. |
| Technical soundness | 90 | 15% | 13.50 | Known-gadget recovery and new RCE validation support the method. |
| Practical usability | 88 | 10% | 8.80 | Produces concrete, exploitable paths rather than warnings alone. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Model, implementation and evaluation are explicit. |

**Final score: 78.7/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It materially improves discovery and
validation of established object-injection and gadget-chain attacks.

## 78.4 — [Fingerprinting in Style: Detecting Browser Extensions via Injected Style Sheets](https://www.usenix.org/conference/usenixsecurity21/presentation/laperdrix)

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in 2021. Earlier extension-
fingerprinting mechanisms and 2020 Carnus were part of the prior-art check.

### Core contribution

A Web page creates elements targeted by an installed extension's injected CSS
and reads the resulting computed styles. Large-scale analysis found usable
style triggers for thousands of extensions, including many not detectable via
web-accessible resources, DOM changes or message/request behavior.

### Prior art

Extension detection through exposed resources and observable behavior was
known. Treating extension style sheets as externally triggerable and readable
fingerprints adds a separate observation channel.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 72 | 25% | 18.00 | Establishes injected computed style as a distinct detection channel. |
| Transferability | 80 | 20% | 16.00 | Applies to many extensions that inject content styles. |
| Lasting value | 76 | 20% | 15.20 | Highlights a persistent privacy cost of page-visible extension effects. |
| Technical soundness | 88 | 15% | 13.20 | Large corpus analysis and validation support the channel. |
| Practical usability | 78 | 10% | 7.80 | Generated triggers can be deployed by ordinary pages. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Detection construction and coverage are documented. |

**Final score: 78.4/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. The privacy goal is established, but computed-style
probing reaches extensions invisible to earlier resource and behavior probes.

## 78.1 — [Revealer: Detecting and Exploiting Regular Expression Denial-of-Service Vulnerabilities](https://research.cuhk.edu.hk/en/publications/revealer-detecting-and-exploiting-regular-expression-denial-of-se-2/)

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed IEEE S&P work published in May 2021. ReDoS and the 2018 `Freezing
the Web` tooling entry were treated as explicit prior art.

### Core contribution

Revealer combines static and dynamic analysis to locate vulnerable regex
subexpressions and generate attack strings that trigger recursive backtracking,
including extended regex features poorly handled by earlier analyzers. Its
large-scale evaluation found real-world vulnerable expressions missed by prior
tools.

### Prior art

Catastrophic backtracking, ReDoS and automated evil-input generation were
known. Broader language-feature support plus subexpression localization and
working exploit-string generation is the qualifying methodological advance.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 58 | 25% | 14.50 | Improves analysis of an established vulnerability class. |
| Transferability | 80 | 20% | 16.00 | Covers varied regex features and application corpora. |
| Lasting value | 82 | 20% | 16.40 | Better handling of real engines remains useful for testing. |
| Technical soundness | 92 | 15% | 13.80 | Comparative evaluation and validated cases are strong. |
| Practical usability | 90 | 10% | 9.00 | Produces localized findings and concrete denial inputs. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Analysis stages and datasets are well specified. |

**Final score: 78.1/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. The score reflects materially stronger
detection and exploit generation, not a claim that ReDoS itself is new.

## 71.8 — [Gummy Browsers: Targeted Browser Spoofing against State-of-the-Art Fingerprinting Techniques](https://arxiv.org/abs/2110.10129)

**KEPT** · Meaningful extension · confidence Medium

### Candidate

The primary preprint was public on 19 October 2021. Its URL and targeted full-
fingerprint spoofing mechanism were absent from the original nominations.

### Core contribution

An attacker first captures a victim's browser fingerprint, then configures or
instruments another browser to reproduce the collected attributes to a relying
site. The paper demonstrates three spoofing strategies and evaluates the cloned
profiles against contemporary fingerprinting and tracking systems.

### Prior art

Browser fingerprint collection, user-agent spoofing and anti-fingerprinting
tools were known. The distinct step is targeted, coordinated reproduction of a
specific victim's high-dimensional profile for impersonation rather than
generic uniqueness reduction.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 65 | 25% | 16.25 | Reframes spoofing as targeted full-profile cloning. |
| Transferability | 74 | 20% | 14.80 | Applies where fingerprint signals influence identity or tracking. |
| Lasting value | 70 | 20% | 14.00 | The threat persists, though signal sets change over time. |
| Technical soundness | 82 | 15% | 12.30 | Multiple strategies and system evaluations support feasibility. |
| Practical usability | 66 | 10% | 6.60 | Requires prior victim fingerprint collection and ongoing synchronization. |
| Clarity and reproducibility | 78 | 10% | 7.80 | Threat model and spoofing approaches are described. |

**Final score: 71.8/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. Targeted fingerprint cloning adds an impersonation goal
and orchestration method beyond generic browser-attribute spoofing.

## 69.4 — [To Err.Is Human: Characterizing the Threat of Unintended URLs in Social Media](https://www.ndss-symposium.org/ndss-paper/to-err-is-human-characterizing-the-threat-of-unintended-urls-in-social-media/)

**KEPT** · Meaningful extension · confidence Medium

### Candidate

Peer-reviewed NDSS paper published in February 2021. Its automatic-linkification
mechanism was absent from the original list and backward mechanism search.

### Core contribution

Permissive social-media parsers can interpret prose with a missing space after
a period as a domain name. An attacker registers that unintended generated
domain and captures clicks from the original post's audience; the study built a
classifier, found thousands of such URLs and validated the risk by registering
selected domains.

### Prior art

Typosquatting, parser ambiguity and malicious linkification were known themes.
The contribution isolates a reproducible mismatch between human sentence
boundaries and automatic URL recognition, then turns it into domain takeover of
otherwise benign text.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 60 | 25% | 15.00 | Defines a specific parser-to-domain-capture mechanism. |
| Transferability | 70 | 20% | 14.00 | Applies across permissive social and messaging linkifiers. |
| Lasting value | 64 | 20% | 12.80 | Parser fixes are possible, but auto-linkification remains widespread. |
| Technical soundness | 84 | 15% | 12.60 | Corpus analysis and registered-domain experiments substantiate it. |
| Practical usability | 70 | 10% | 7.00 | Exploitation is simple when an eligible generated domain is available. |
| Clarity and reproducibility | 80 | 10% | 8.00 | Parsing pattern, classifier and validation are clear. |

**Final score: 69.4/100.** Archive decision: include under the historical
60-or-above qualifying-technique rule.

### Verdict

Meaningful extension. It is narrower than the higher-scoring candidates but is
not merely ordinary typosquatting: the platform parser manufactures the link.
