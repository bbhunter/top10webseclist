# 2010 candidate judgements

These scorecards apply the repository's weighted judge rubric. `KEPT` means the
candidate met the historical 60-or-above inclusion rule as well as the
first-publication, originality-verdict and original-nomination exclusions.

## 85.8 — [How Unique Is Your Web Browser?](https://coveryourtracks.eff.org/static/browser-uniqueness.pdf) [EFF 2010 announcement](https://www.eff.org/press/archives/2010/05/13) — Peter Eckersley

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

EFF's Panopticlick study was publicly announced in May 2010 and presented at
PETS 2010. The authorized paper, deployment and contemporary announcement fix
the publication date and provide primary evidence.

### Core contribution

The work implemented a concrete multi-attribute browser fingerprint, measured
470,161 browsers, quantified its entropy and uniqueness, and demonstrated a
high-precision heuristic for linking a changed fingerprint to its predecessor.
It turned a collection of exposed browser properties into a measurable,
operational tracking method.

### Prior art

User-Agent strings, font/plugin enumeration and commercial device identifiers
predated Panopticlick. The credited advance is the large empirical methodology,
combined fingerprint and longitudinal linking result, not invention of every
individual input signal.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 74 | 25% | 18.50 | Strong empirical synthesis of known and new fingerprint signals. |
| Transferability | 90 | 20% | 18.00 | Applies to browsers, tracking systems and anti-fingerprinting design. |
| Lasting value | 94 | 20% | 18.80 | Established the modern browser-fingerprinting measurement model. |
| Technical soundness | 86 | 15% | 12.90 | Large study with bias and stability limitations stated. |
| Practical usability | 86 | 10% | 8.60 | Live test and explicit algorithm made the method immediately usable. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Inputs, collection and linking heuristic are documented. |

**Final score: 85.8/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. Earlier components existed, but the
combined measurement and linking methodology is distinct and historically
foundational.

## 85.3 — [A Symbolic Execution Framework for JavaScript](https://webblaze.cs.berkeley.edu/papers/kudzu.pdf) [project page](https://webblaze.cs.berkeley.edu/kudzu.html) — Prateek Saxena, Devdatta Akhawe, Steve Hanna, Feng Mao, Stephen McCamant, Dawn Song

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

IEEE S&P 2010 paper and Berkeley project release, published in May 2010.

### Core contribution

Kudzu is the first end-to-end symbolic-execution framework for client-side
JavaScript. It separates GUI-event exploration from symbolic value exploration,
adds the Kaluza solver for real JavaScript string constraints, and automatically
generates inputs that expose client-side code-injection bugs.

### Prior art

Symbolic execution, server-side web analysis and FLAX's taint-enhanced fuzzing
predate Kudzu. The new contribution is automatic JavaScript path exploration,
event-space coverage and a string theory expressive enough for deployed code.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 85 | 25% | 21.25 | First complete symbolic execution system for client-side JavaScript. |
| Transferability | 82 | 20% | 16.40 | General analysis substrate beyond its code-injection case study. |
| Lasting value | 88 | 20% | 17.60 | String solving and event/value exploration shaped later analysis. |
| Technical soundness | 90 | 15% | 13.50 | 18 live applications, concrete findings and solver analysis. |
| Practical usability | 78 | 10% | 7.80 | Automated end-to-end prototype with released solver artifacts. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Architecture, constraints, experiments and benchmarks are detailed. |

**Final score: 85.3/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. The vulnerabilities are established
classes; the qualifying advance is a new automatic way to reach and prove them.

## 84.5 — [A Practical Attack to De-Anonymize Social Network Users](https://iseclab.org/publications/wondracek2010a_practical/) [paper](https://seclab.nu/static/publications/ssp2010osn.pdf) — Gilbert Wondracek, Thorsten Holz, Engin Kirda, Christopher Kruegel

**KEPT** · Meaningful combination or adaptation · confidence High

### Candidate

Primary iSecLab publication record and IEEE S&P paper, public by February 2010
and presented in May 2010.

### Core contribution

The attack turns history-stealing yes/no probes into real-identity recovery by
matching a visitor's sparse social-network group memberships against public
membership data. The authors give scalable probing methods and validate the
attack on Xing, Facebook and LinkedIn.

### Prior art

CSS history stealing and statistical dataset de-anonymization were known. No
earlier source found combined live browser-history probes with public group
membership fingerprints to identify an arbitrary site visitor.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | Non-obvious synthesis creates identity recovery, not mere tracking. |
| Transferability | 88 | 20% | 17.60 | General to sites exposing sparse user-associated URL sets. |
| Lasting value | 84 | 20% | 16.80 | Durable model for web-assisted de-anonymization. |
| Technical soundness | 88 | 15% | 13.20 | Formal treatment plus real-world collection and experiments. |
| Practical usability | 78 | 10% | 7.80 | Low-interaction attack, subject to history protections and data access. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Algorithm, assumptions, crawling and evaluation are explicit. |

**Final score: 84.5/100.** Archive decision: include as a core technique.

### Verdict

Meaningful combination or adaptation. Known primitives are assembled into a
new, practical ability to map a browser visitor to a named person.

## 82.9 — [FLAX: Systematic Discovery of Client-side Validation Vulnerabilities in Rich Web Applications](https://www.ndss-symposium.org/ndss2010/flax-systematic-discovery-client-side-validation-vulnerabilities-rich-web-applications/) [paper](https://www.ndss-symposium.org/wp-content/uploads/2017/09/saxe.pdf) — Prateek Saxena, Steve Hanna, Pongsin Poosankam, Dawn Song

**KEPT** · Original technique · confidence High

### Candidate

NDSS paper and conference record dated 1 March 2010.

### Core contribution

FLAX defines client-side validation vulnerabilities as unsafe use of untrusted
data entirely within JavaScript and introduces taint-enhanced, sink-aware
black-box fuzzing. Its hybrid analysis generated concrete exploits with no
reported false positives and found 11 previously unknown bugs in 40 programs.

### Prior art

DOM XSS, taint tracking and fuzzing existed. The paper distinguishes broader
client-side validation sinks, handles reflected server flows and uses precise
taint to reduce a concrete fuzzing space rather than merely reporting flows.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 82 | 25% | 20.50 | Defines a broader client-side class and a novel hybrid detector. |
| Transferability | 82 | 20% | 16.40 | Applies across JavaScript-rich sites, gadgets and sink types. |
| Lasting value | 82 | 20% | 16.40 | Strong precursor to later client-side vulnerability analysis. |
| Technical soundness | 88 | 15% | 13.20 | Explicit model, algorithms and field evaluation. |
| Practical usability | 78 | 10% | 7.80 | Automated concrete findings on live applications. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Method, architecture and results are fully described. |

**Final score: 82.9/100.** Archive decision: include as a core technique.

### Verdict

Original technique. Existing pieces do not supply FLAX's client-side validation
model plus taint-guided, exploit-confirming fuzzing workflow.

## 81.7 — [Protecting Browsers from Extension Vulnerabilities](https://www.ndss-symposium.org/ndss2010/protecting-browsers-extension-vulnerabilities/) [paper](https://www.ndss-symposium.org/wp-content/uploads/2017/09/barth.pdf) — Adam Barth, Adrienne Porter Felt, Prateek Saxena, Aaron Boodman

**KEPT** · Meaningful extension · confidence High

### Candidate

NDSS publication dated 1 March 2010; the primary paper states that its design
was adopted for the Chrome extension system.

### Core contribution

The paper systematizes extension exploitation as untrusted web input reaching
over-privileged browser code, measures the privilege gap in 25 Firefox
extensions, analyzes API escalation paths, and develops the content-script,
extension-core and optional-native-binary separation model.

### Prior art

Individual extension XSS, DOM replacement and capability-leak attacks were
known. The qualifying advance is the reusable privilege-analysis methodology
and least-privilege architecture backed by empirical evidence.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 68 | 25% | 17.00 | Systematic extension threat and privilege model over known bug classes. |
| Transferability | 86 | 20% | 17.20 | General to browser extension APIs and third-party privileged code. |
| Lasting value | 90 | 20% | 18.00 | Model became the basis of a major deployed extension platform. |
| Technical soundness | 90 | 15% | 13.50 | Manual study, API lattice and concrete architecture support the claims. |
| Practical usability | 72 | 10% | 7.20 | Directly useful to platform designers and extension auditors. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Threats, measurements and design boundaries are explicit. |

**Final score: 81.7/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It does not invent extension bugs, but turns them into a
general privilege-analysis method and deployable containment model.

## 81.1 — [Regular Expressions Considered Harmful in Client-Side XSS Filters](https://www.adambarth.com/papers/2010/bates-barth-jackson.pdf) [WWW copy](https://archives.iw3c2.org/www2010/research/xssauditor.pdf) — Daniel Bates, Adam Barth, Collin Jackson

**KEPT** · Meaningful extension · confidence High

### Candidate

WWW 2010 paper, published April 2010, with matching author and conference copies.

### Core contribution

The work demonstrates a general mismatch between pre-parse regex filters and
the browser's actual decoding/parsing pipeline, including filter bypass and
attacker-induced false positives that create vulnerabilities. It then derives
the post-parse, pre-execution XSS Auditor design deployed in Chrome.

### Prior art

XSS and specific IE8 filter attacks were already known and the original 2010
list contains one. This score credits the cross-filter architectural analysis,
induced-false-positive class and parser-integrated method, not the nominated
IE8 exploit alone.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 70 | 25% | 17.50 | Generalizes isolated bypasses into a filter-architecture failure mode. |
| Transferability | 82 | 20% | 16.40 | Applies wherever security simulation diverges from real parsing. |
| Lasting value | 86 | 20% | 17.20 | Influenced deployed browser filtering and parser-aware testing. |
| Technical soundness | 88 | 15% | 13.20 | Multiple filters, 145 XSS cases and an implementation evaluation. |
| Practical usability | 82 | 10% | 8.20 | Concrete bypass reasoning and a deployed design. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Examples and pipeline placement are precise. |

**Final score: 81.1/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. The distinct contribution is the reusable parser/filter
differential model, beyond the already nominated IE8 instance.

## 81.0 — [Busting Frame Busting: a Study of Clickjacking Vulnerabilities on Popular Sites](https://seclab.stanford.edu/websec/framebusting/framebust.pdf) — Gustav Rydstedt, Elie Bursztein, Dan Boneh, Collin Jackson

**KEPT** · Meaningful extension · confidence High

### Candidate

W2SP 2010 paper already present in the missed section, re-recorded so the 2010
judgement trail and current threshold are complete.

### Core contribution

The paper systematically breaks deployed frame-busting scripts using double
framing, `onBeforeUnload`, no-content flushing, restricted-zone and related
techniques, measures real sites, and develops a robust browser-enforced remedy.

### Prior art

Clickjacking and basic frame busting predate 2010. The reusable catalogue of
bypasses, deployment evidence and systematic evaluation are the advance.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 75 | 25% | 18.75 | Multiple new and generalized frame-busting bypass mechanisms. |
| Transferability | 80 | 20% | 16.00 | Applies across scripted framing defenses and browsers. |
| Lasting value | 90 | 20% | 18.00 | Drove durable browser-level anti-framing guidance. |
| Technical soundness | 85 | 15% | 12.75 | Broad measurements and concrete demonstrations. |
| Practical usability | 75 | 10% | 7.50 | Directly usable in clickjacking tests. |
| Clarity and reproducibility | 80 | 10% | 8.00 | Bypasses and mitigations are clearly specified. |

**Final score: 81.0/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. Clickjacking was known; the systematic defeat of common
script defenses is a distinct, durable contribution.

## 78.9 — [Fear the EAR: Execution After Redirect](https://bryceboe.com/2010/12/09/ucsbs-international-capture-the-flag-competition-2010-challenge-6-fear-the-ear/) — Bryce Boe

**KEPT** · Meaningful combination or adaptation · confidence High

### Candidate

The author's complete UCSB iCTF challenge writeup is dated 9 December 2010. It
defines Execution After Redirect, publishes the vulnerable source path and
records how competition teams found and exploited it. The later CCS paper is
not used to move the first-publication date into 2011.

### Core contribution

The writeup shows that an authorization branch can send an HTTP redirect yet
continue executing privileged code and returning a sensitive response body.
Because browsers and common command-line clients automatically follow the
redirect, the security-relevant body and continued server-side execution are
hidden unless the tester disables redirect following or inspects the raw first
response. The challenge turns that observation into an authorization bypass and
then uses the exposed privileged command path to reach a further injection.

### Prior art

The underlying control-flow behavior was public: the PHP manual's redirect
example calls `exit`, and an April 2010 [public discussion](https://stackoverflow.com/questions/2747791/why-i-have-to-call-exit-after-redirection-through-headerlocation-in-php)
explicitly says that a `Location` header does not halt PHP execution. The
qualifying advance is therefore not “redirects do not terminate programs.” It
is the explicit security construction that combines missing termination,
authorization control flow, an automatically hidden 3xx response body and a
raw-response testing procedure into the reusable EAR vulnerability class.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 60 | 25% | 15.00 | Names and demonstrates a security class from behavior previously known mainly as a coding hazard. |
| Transferability | 90 | 20% | 18.00 | Applies across frameworks whenever redirect helpers do not terminate privileged control flow. |
| Lasting value | 86 | 20% | 17.20 | Missing-return authorization failures and redirect-masking remain durable review targets. |
| Technical soundness | 74 | 15% | 11.10 | Complete code and a working challenge validate the mechanism, though it is a constructed single case. |
| Practical usability | 90 | 10% | 9.00 | Disabling redirects and inspecting the first response are immediate, low-cost tests. |
| Clarity and reproducibility | 86 | 10% | 8.60 | The vulnerable line, response behavior, exploitation path and team results are explicit. |

**Final score: 78.9/100.** Archive decision: include as a core technique.

### Verdict

Meaningful combination or adaptation. Redirect continuation itself predates the
writeup; EAR's contribution is the reusable authorization-bypass construction
and raw-response discovery method built from it.

## 78.7 — [NoTamper: Automatic Blackbox Detection of Parameter Tampering Opportunities in Web Applications](https://www.cs.uic.edu/~venkat/research/papers/NoTamper-ccs2010.pdf) — Prithvi Bisht, Timothy Hinrichs, Nazari Skrupsky, Radoslaw Bobrowicz, V. N. Venkatakrishnan

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Primary author-hosted CCS 2010 paper, published October 2010.

### Core contribution

NoTamper analyzes client-side JavaScript validation, negates inferred
constraints, generates prioritized violating inputs and observes black-box
server responses to find validation assumptions the server failed to repeat.
It produced concrete exploits including unauthorized transfers and discounts.

### Prior art

Manual parameter tampering, generic scanners and framework-level integrity
systems predate the paper. The contribution is the first systematic black-box
method that mines client validation to construct targeted tampering tests.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 68 | 25% | 17.00 | New automatic input-generation method for an old class. |
| Transferability | 80 | 20% | 16.00 | General to forms with client/server validation asymmetry. |
| Lasting value | 80 | 20% | 16.00 | Durable model for business-logic and parameter testing. |
| Technical soundness | 86 | 15% | 12.90 | Algorithms plus open-source and live-site evaluation. |
| Practical usability | 82 | 10% | 8.20 | Produces actionable parameters and exploit starting points. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Design, heuristics and findings are detailed. |

**Final score: 78.7/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It systematizes and scales parameter
tampering rather than claiming to invent the underlying vulnerability.

## 78.4 — [On the Incoherencies in Web Browser Access Control Policies](https://www.microsoft.com/en-us/research/publication/incoherencies-web-browser-access-control-policies/) [paper](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/12/incoherencyAndWebAnalyzer.pdf) — Kapil Singh, Alexander Moshchuk, Helen J. Wang, Wenke Lee

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Microsoft Research record and IEEE S&P 2010 paper, published May 2010.

### Core contribution

The paper derives principal-consistency invariants for browser resources,
systematically finds conflicts across DOM, network, cookies, display and user
resources, and builds WebAnalyzer to measure the compatibility cost of removing
unsafe policies across roughly 100,000 sites.

### Prior art

Individual same-origin exceptions, clickjacking and history/privacy flaws were
known. The new value is a single principal-driven discovery framework and the
large-scale measurement method; already nominated individual mechanisms are not
claimed again.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 68 | 25% | 17.00 | New systematic invariants and compatibility-measurement framework. |
| Transferability | 82 | 20% | 16.40 | General across browser resource types and evolving APIs. |
| Lasting value | 80 | 20% | 16.00 | Durable way to reason about piecemeal browser policies. |
| Technical soundness | 88 | 15% | 13.20 | Explicit principles and large executed-web measurement. |
| Practical usability | 72 | 10% | 7.20 | Useful to browser security review and feature deprecation. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Policies, crawler instrumentation and results are documented. |

**Final score: 78.4/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It does not re-credit the individual
clickjacking/history findings; the qualifying advance is systematic discovery
and compatibility measurement of browser-policy incoherence.

## 78.1 — [Protecting Browsers from Cross-Origin CSS Attacks](https://www.linshunghuang.com/papers/css.pdf) — Lin-Shung Huang, Zack Weinberg, Chris Evans, Collin Jackson

**KEPT** · Meaningful extension · confidence High

### Candidate

Author-hosted ACM CCS 2010 paper, published October 2010.

### Core contribution

The work generalizes cross-origin stylesheet data theft to every major browser,
including a no-JavaScript exfiltration path. Attacker-controlled CSS delimiters
make authenticated HTML parse as a rule and leak secrets through computed style
or resource loads; a cross-origin content-type check blocks the class.

### Prior art

The paper identifies CSS data theft as dating to 2002 and explicitly limits its
claim. The 2010 advance is the cross-browser, JavaScript-independent form, real
site demonstrations and the general content-type enforcement insight.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 62 | 25% | 15.50 | Strong generalization of an acknowledged older attack. |
| Transferability | 82 | 20% | 16.40 | Applies across browsers and authenticated HTML endpoints. |
| Lasting value | 82 | 20% | 16.40 | Led to multi-browser content-type enforcement. |
| Technical soundness | 88 | 15% | 13.20 | Detailed parsing mechanics, site attacks and compatibility study. |
| Practical usability | 78 | 10% | 7.80 | Clear injection and extraction patterns. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Preconditions, variants and limitations are explicit. |

**Final score: 78.1/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. The paper is not credited with the 2002 primitive; its
portable, scriptless exploitation and content-type model are the advance.

## 77.6 — [An Analysis of Private Browsing Modes in Modern Browsers](https://www.usenix.org/conference/usenixsecurity10/analysis-private-browsing-modes-modern-browsers) [paper](https://www.usenix.org/event/sec10/tech/full_papers/Aggarwal.pdf) — Gaurav Aggarwal, Elie Bursztein, Collin Jackson, Dan Boneh

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

USENIX Security 2010 paper and conference record dated August 2010.

### Core contribution

The paper separates local- and web-attacker goals for private browsing,
introduces automated state-differential testing across public/private sessions,
finds implementation failures, and demonstrates that extensions and plugins can
preserve or reveal supposedly private activity.

### Prior art

The 2009 list already includes detecting private mode, and individual residue
channels were known. The credited contribution is the systematic threat model,
automated testing method and extension/plugin composition analysis.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 64 | 25% | 16.00 | New systematic definition and automated differential method. |
| Transferability | 82 | 20% | 16.40 | Applies across browser modes, state types and add-ons. |
| Lasting value | 82 | 20% | 16.40 | Remains the canonical model for private-mode evaluation. |
| Technical soundness | 88 | 15% | 13.20 | Four-browser analysis, measurement and concrete failures. |
| Practical usability | 72 | 10% | 7.20 | Actionable test method, though implementation tooling is specialized. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Goals, state tests and findings are clear. |

**Final score: 77.6/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It extends isolated private-mode probes
into a reusable security-testing framework.

## 77.1 — [Residue Objects: A Challenge to Web Browser Security](https://www.microsoft.com/en-us/research/publication/residue-objects-a-challenge-to-web-browser-security/) [paper](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/euro054-chen.pdf) — Shuo Chen, Hong Chen, Manuel Caballero

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Microsoft Research record and EuroSys 2010 paper, published April 2010.

### Core contribution

The paper identifies browser objects that remain active after navigation as a
coherent vulnerability class. It derives security consequences for visual and
document integrity and memory safety, then uses an enumerative lifetime/guard
analysis to find five previously unknown Internet Explorer vulnerabilities.

### Prior art

Individual stale-window and browser lifetime bugs had appeared before. The
research contribution is the residue-object abstraction and a systematic
method for enumerating object/guard combinations rather than another isolated
browser bug.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 76 | 25% | 19.00 | First coherent class and systematic lifetime analysis. |
| Transferability | 74 | 20% | 14.80 | General idea, with evaluation concentrated on IE's object model. |
| Lasting value | 78 | 20% | 15.60 | Durable browser-lifecycle security insight. |
| Technical soundness | 86 | 15% | 12.90 | Concrete object analysis and five new findings. |
| Practical usability | 66 | 10% | 6.60 | Useful to browser auditors but implementation-intensive. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Conditions and enumeration procedure are well explained. |

**Final score: 77.1/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. The paper elevates scattered bugs into a
reusable discovery model for security-sensitive object lifetimes.

## 76.3 — [Preventing Capability Leaks in Secure JavaScript Subsets](https://webblaze.cs.berkeley.edu/blancura.html) [paper](https://webblaze.cs.berkeley.edu/papers/finifter-weinberger-barth.pdf) — Matthew Finifter, Joel Weinberger, Adam Barth

**KEPT** · Meaningful extension · confidence High

### Candidate

NDSS publication dated 1 March 2010 with an author project page, paper and
source-code release.

### Core contribution

The authors show that blacklist-based safe JavaScript subsets let an approved
advertisement reach host-added prototype methods, making one third of the Alexa
US Top 100 exploitable under ADsafe. Blancura replaces property blacklisting
with guest namespaces and a whitelist, while preserving static verification.

### Prior art

JavaScript capability leaks and safe subsets predate 2010, including a 2009
cross-origin browser-leak paper. This work finds a different host/guest
prototype interaction in verifier-based ad sandboxes and measures its prevalence.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 68 | 25% | 17.00 | New prototype-augmentation escape in static subset sandboxes. |
| Transferability | 76 | 20% | 15.20 | General to blacklist verifiers and shared JavaScript prototypes. |
| Lasting value | 78 | 20% | 15.60 | Durable warning against blacklist-based language sandboxes. |
| Technical soundness | 86 | 15% | 12.90 | Detection algorithm, top-site study and working defense. |
| Practical usability | 72 | 10% | 7.20 | Released verifier/compiler and concrete exploitation condition. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Attack, measurements and namespace design are explicit. |

**Final score: 76.3/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It adapts capability-leak reasoning to a distinct and
widely deployed class of verifier-based JavaScript sandboxes.

## 75.2 — [An Empirical Study of Privacy-Violating Information Flows in JavaScript Web Applications](https://www.cs.cornell.edu/~lerner/papers/ccs10-jsc.pdf) — Dongseok Jang, Ranjit Jhala, Sorin Lerner, Hovav Shacham

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Author-hosted ACM CCS 2010 paper, published October 2010.

### Core contribution

The work builds a fine-grained policy language and rewriting-based information-
flow engine in Chrome, then executes the Alexa top 50,000 to measure cookie
stealing, geolocation hijacking, history sniffing and behavior tracking. It
connects otherwise separate privacy attacks through observable JavaScript flows.

### Prior art

Each measured attack family and dynamic information-flow tracking had prior
work. The qualification is the browser-integrated, policy-driven large-scale
measurement methodology, not rediscovery of those individual attacks.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 60 | 25% | 15.00 | Novel synthesis and engine over known privacy-flow classes. |
| Transferability | 82 | 20% | 16.40 | Policy method generalizes to varied JavaScript sources and sinks. |
| Lasting value | 78 | 20% | 15.60 | Strong foundation for empirical web privacy analysis. |
| Technical soundness | 88 | 15% | 13.20 | Browser implementation and very large executed-site study. |
| Practical usability | 68 | 10% | 6.80 | Useful research platform, with substantial instrumentation cost. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Policies, engine and measurements are detailed. |

**Final score: 75.2/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It is retained for the general measurement
method, while the known component attacks remain credited to their prior art.

## 74.0 — [State of the Art: Automated Black-Box Web Application Vulnerability Testing](https://web.stanford.edu/~jcm/papers/pci_oakland10.pdf) [project record](https://seclab.stanford.edu/websec/) — Jason Bau, Elie Bursztein, Divij Gupta, John Mitchell

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Stanford-hosted IEEE S&P 2010 paper, published May 2010.

### Core contribution

The authors construct common vulnerable applications and an evaluation protocol
for eight leading black-box scanners, then compare scanner coverage against
real vulnerability populations. The study exposes systematic blind spots,
including stored XSS and SQL injection, and supplies a durable scanner benchmark.

### Prior art

Web scanners and individual scanner evaluations predate 2010. The new value is
the first comprehensive multi-tool, common-target methodology tied to wild
vulnerability prevalence rather than a new vulnerability primitive.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 55 | 25% | 13.75 | New comprehensive benchmark for existing tools and classes. |
| Transferability | 76 | 20% | 15.20 | Evaluation design generalizes to scanners and vulnerability sets. |
| Lasting value | 78 | 20% | 15.60 | Became a reference point for scanner effectiveness research. |
| Technical soundness | 90 | 15% | 13.50 | Controlled targets, eight tools and careful anonymized reporting. |
| Practical usability | 72 | 10% | 7.20 | Directly informs scanner validation and test-suite construction. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Questions, targets, metrics and limitations are explicit. |

**Final score: 74.0/100.** Archive decision: include as a supporting reference;
the historical 60-or-above gate qualifies it for the missed list.

### Verdict

Tooling or methodology contribution. The benchmark advances how black-box web
testing is evaluated, without claiming the scanners' underlying attacks.

## 73.0 — [The Emperor's New APIs: On the (In)Secure Usage of New Client-side Primitives](https://www.comp.nus.edu.sg/~prateeks/papers/w2sp10-primitives.pdf) — Steve Hanna, Richard Shin, Devdatta Akhawe, Prateek Saxena, Arman Boehm, Dawn Song

**KEPT** · Meaningful combination or adaptation · confidence High

### Candidate

W2SP 2010 paper already present in the missed section, re-recorded so the
judgement trail is complete.

### Core contribution

The paper audits deployed uses of `postMessage`, CORS and related new browser
primitives, with the distinct attack contribution being real applications that
accept cross-window messages without authenticating `event.origin`, enabling
cross-origin command and data abuse.

### Prior art

The APIs and the need for origin binding were specified earlier. The advance is
demonstrating the recurring missing-origin-check class in deployed applications
and turning specification advice into a practical auditing rule.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 60 | 25% | 15.00 | First substantial deployed evidence of this API misuse pattern. |
| Transferability | 80 | 20% | 16.00 | General to cross-origin message consumers and emerging APIs. |
| Lasting value | 75 | 20% | 15.00 | Origin validation remains a standard review requirement. |
| Technical soundness | 80 | 15% | 12.00 | Concrete sites and API-level causal analysis. |
| Practical usability | 70 | 10% | 7.00 | Immediately actionable audit check. |
| Clarity and reproducibility | 80 | 10% | 8.00 | Misuse and fixes are clearly shown. |

**Final score: 73.0/100.** Archive decision: include as a supporting reference;
the historical 60-or-above gate qualifies it for the missed list.

### Verdict

Meaningful combination or adaptation. It applies established trust-boundary
reasoning to new browser APIs and validates the resulting class in the wild.

## 72.3 — [Sidebuster: Automated Detection and Quantification of Side-Channel Leaks in Web Application Development](https://www.microsoft.com/en-us/research/publication/sidebuster-automated-detection-and-quantification-of-side-channel-leaks-in-web-application-development/) — Kehuan Zhang, Zhou Li, Rui Wang, XiaoFeng Wang, Shuo Chen

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Microsoft Research record for the ACM CCS 2010 paper, published October 2010.

### Core contribution

Sidebuster analyzes event-driven web-application source to find program states
that produce distinguishable encrypted traffic, then reruns cases to quantify
entropy loss. Its GWT prototype handles AJAX widgets and converts a manual
side-channel concern into a development-time detector.

### Prior art

The authors' May 2010 web-application side-channel paper and the original list's
related nominations already establish the attack. This score credits only the
later automatic detection and quantification workflow.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 66 | 25% | 16.50 | New automated source/rerun analysis over a known leak class. |
| Transferability | 68 | 20% | 13.60 | General approach, initially evaluated on GWT applications. |
| Lasting value | 72 | 20% | 14.40 | Durable model for development-time side-channel testing. |
| Technical soundness | 84 | 15% | 12.60 | Formal quantification and evaluated prototype. |
| Practical usability | 72 | 10% | 7.20 | Actionable for instrumentable event-driven applications. |
| Clarity and reproducibility | 80 | 10% | 8.00 | Analysis stages and experiments are documented. |

**Final score: 72.3/100.** Archive decision: include as a supporting reference;
the historical 60-or-above gate qualifies it for the missed list.

### Verdict

Tooling or methodology contribution. The original side-channel attack is not
re-added; Sidebuster qualifies for automating its discovery and measurement.

## 68.2 — [DNS Prefetching and Its Privacy Implications: When Good Things Go Bad](https://www.usenix.org/conference/leet-10/dns-prefetching-and-its-privacy-implications-when-good-things-go-bad) [paper](https://www.usenix.org/legacy/event/leet10/tech/full_papers/Krishnan.pdf) — Srinivas Krishnan, Fabian Monrose

**KEPT** · Meaningful extension · confidence High

### Candidate

USENIX LEET 2010 paper and conference record dated April 2010.

### Core contribution

The work shows that browser/search DNS prefetching loads a resolver cache with
context-rich names before a user follows any result. An observer who probes
that shared cache can infer likely client search terms much more precisely than
with ordinary cache snooping.

### Prior art

DNS cache snooping and privacy concerns around prefetching existed. The distinct
2010 contribution is the prefetch-amplified search inference mechanism and its
experimental analysis, not the base cache-timing primitive.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 60 | 25% | 15.00 | New privacy inference from combining two known behaviors. |
| Transferability | 74 | 20% | 14.80 | Applies to shared resolvers and context-rich prefetch schemes. |
| Lasting value | 62 | 20% | 12.40 | Important design warning, moderated by deployment changes. |
| Technical soundness | 80 | 15% | 12.00 | Mechanism and experiments support scoped claims. |
| Practical usability | 62 | 10% | 6.20 | Feasible under shared-cache and probing preconditions. |
| Clarity and reproducibility | 78 | 10% | 7.80 | Attack model, queries and limitations are clear. |

**Final score: 68.2/100.** Archive decision: include as a supporting reference;
the historical 60-or-above gate qualifies it for the missed list.

### Verdict

Meaningful extension. Prefetching materially amplifies old DNS cache snooping
into a search-query inference technique.
