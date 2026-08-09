# 2011 candidate judgements

These scorecards apply the repository's weighted judge rubric. `KEPT` means the
candidate met the historical 60-or-above inclusion rule as well as the
first-publication, originality-verdict and original-nomination exclusions.

## 92.6 — [How to Shop for Free Online](https://www.ieee-security.org/TC/SP2011/PAPERS/2011/paper029.pdf) — Rui Wang, Shuo Chen, XiaoFeng Wang, Shaz Qadeer

**KEPT** · Original technique · confidence High

### Candidate

IEEE S&P paper published in May 2011. The paper, conference imprint and tested
systems establish the date, authorship and primary evidence.

### Core contribution

The work models third-party checkout as a three-party state-coordination
problem. By tracking which party controls each API argument and which identities,
orders, prices and payments must remain bound, it derives concrete attacks that
make a merchant accept a payment to the wrong seller, reuse one payment, accept
an attacker-selected price or fulfil an unpaid order. It validates the method on
merchant software, live shops and major payment providers.

### Prior art

Parameter tampering, payment-protocol verification and general web logic flaws
predate 2011; the paper cites, among others, the 2010 automated logic-analysis
and NoTamper work. None supplied its API-oriented multi-party binding model or
the systematic Cashier-as-a-Service attack family.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 92 | 25% | 23.00 | First systematic attack model for multi-party checkout state and identity bindings. |
| Transferability | 94 | 20% | 18.80 | The same confused bindings recur across payment and other service integrations. |
| Lasting value | 92 | 20% | 18.40 | Durable foundation for web business-logic and API workflow testing. |
| Technical soundness | 96 | 15% | 14.40 | Formalized invariants, source analysis and carefully validated real attacks. |
| Practical usability | 88 | 10% | 8.80 | The API-argument and state-binding method translates directly into tests. |
| Clarity and reproducibility | 92 | 10% | 9.20 | Workflows, assumptions, traces and findings are exceptionally explicit. |

**Final score: 92.6/100.** Archive decision: include as a core technique.

### Verdict

Original technique. Earlier work addressed pieces of payment or logic security;
this paper exposes and systematizes the distinct multi-party binding failure.

## 85.7 — [Server-Side JavaScript Injection](https://media.blackhat.com/bh-us-11/Sullivan/BH_US_11_Sullivan_Server_Side_WP.pdf) [Black Hat archive](https://blackhat.com/html/bh-us-11/bh-us-11-archives.html) — Bryan Sullivan

**KEPT** · Meaningful combination or adaptation · confidence High

### Candidate

Author whitepaper dated July 2011 and presented at Black Hat USA on 3 August
2011.

### Core contribution

The paper transfers code-injection reasoning to the then-new server-side
JavaScript stack. It demonstrates direct Node.js `eval` injection, one-request
denial of service, file read/write and process execution, plus Boolean and blind
JavaScript injection against MongoDB queries that can enumerate schema-less
documents.

### Prior art

Server-side `eval`, SQL injection, blind extraction and client-side JavaScript
injection were established. The distinct contribution is a concrete exploitation
model spanning Node.js and JavaScript-executing NoSQL engines, including payloads
and data-extraction procedures appropriate to those runtimes.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 76 | 25% | 19.00 | Adapts known injection ideas into a materially new server-side JS capability. |
| Transferability | 92 | 20% | 18.40 | Applies broadly to dynamic server runtimes, NoSQL queries and unsafe evaluators. |
| Lasting value | 90 | 20% | 18.00 | Established a durable NoSQL/SSJS testing category. |
| Technical soundness | 82 | 15% | 12.30 | Concrete, technically coherent payloads, though not a broad empirical study. |
| Practical usability | 92 | 10% | 9.20 | Direct probes, exploit payloads and mitigations are immediately usable. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Examples cover the full path from injection to extraction or code execution. |

**Final score: 85.7/100.** Archive decision: include as a core technique.

### Verdict

Meaningful combination or adaptation. It does not invent code injection, but it
creates and documents a reusable offensive capability for emerging SSJS systems.

## 85.5 — [“You Might Also Like:” Privacy Risks of Collaborative Filtering](https://www.ieee-security.org/TC/SP2011/PAPERS/2011/paper015.pdf) — Joseph A. Calandrino, Ann Kilzer, Arvind Narayanan, Edward W. Felten, Vitaly Shmatikov

**KEPT** · Original technique · confidence High

### Candidate

IEEE S&P paper published in May 2011, with evaluations against Hunch, Last.fm,
LibraryThing and Amazon.

### Core contribution

A passive attacker watches temporal changes in public item-to-item
recommendations and combines them with moderate auxiliary knowledge to infer a
target user's private transactions or ratings. The key is treating changes in a
high-dimensional aggregate as a side channel for individual inputs.

### Prior art

Recommender privacy, statistical-database disclosure and the 2008 Netflix
dataset deanonymization attack predate this work. Those attacks assumed access
to released records or different query models; they did not extract individual
events from the time-varying public output of a live recommender.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 84 | 25% | 21.00 | New temporal aggregate-output inference oracle. |
| Transferability | 88 | 20% | 17.60 | General to public, dynamic aggregates influenced by private user events. |
| Lasting value | 86 | 20% | 17.20 | Presaged later inference and aggregate-data privacy attacks. |
| Technical soundness | 90 | 15% | 13.50 | Algorithms and multiple real-system evaluations support the claim. |
| Practical usability | 74 | 10% | 7.40 | Requires observation and auxiliary data, but only public black-box access. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Threat model, algorithms, accuracy and limitations are documented. |

**Final score: 85.5/100.** Archive decision: include as a core technique.

### Verdict

Original technique. The temporal side channel is distinct from record-release
deanonymization and from older privacy-preserving recommender designs.

## 83.4 — [Fast and Precise Sanitizer Analysis with BEK](https://www.usenix.org/conference/usenix-security-11/presentation/fast-and-precise-sanitizer-analysis-bek) [paper](https://www.usenix.org/legacy/events/sec11/tech/full_papers/Hooimeijer.pdf) — Pieter Hooimeijer, Benjamin Livshits, David Molnar, Prateek Saxena, Margus Veanes

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

USENIX Security paper and presentation published on 10 August 2011.

### Core contribution

BEK expresses real sanitizers as symbolic finite transducers, then checks
equivalence, idempotence, commutativity and whether a dangerous target can be an
output. When it can, the system synthesizes a concrete triggering input. The
authors encode ASP.NET, Internet Explorer, Google AutoEscape and other
sanitizers, retain Unicode precision and compile analyzed definitions to
deployable code.

### Prior art

SANER, string solvers, finite-state analysis and parser/filter differentials
were established. BEK's precise sanitizer language, symbolic representation,
fast algebraic analyses and counterexample synthesis form the new methodology.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 76 | 25% | 19.00 | New exact, executable sanitizer-analysis abstraction and analyses. |
| Transferability | 86 | 20% | 17.20 | Applies across sanitizer families, output contexts and implementation languages. |
| Lasting value | 86 | 20% | 17.20 | Durable model for reasoning about composed transformations. |
| Technical soundness | 92 | 15% | 13.80 | Formal algorithms, real encodings and performance evidence. |
| Practical usability | 72 | 10% | 7.20 | Requires modeling, but produces concrete counterexamples and deployable code. |
| Clarity and reproducibility | 90 | 10% | 9.00 | Semantics, algorithms, test subjects and timings are explicit. |

**Final score: 83.4/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. The vulnerability classes are known; BEK
adds a substantially more precise and reusable way to find sanitizer failures.

## 82.3 — [All Your Clouds Are Belong to Us](https://www.nds.rub.de/media/nds/veroeffentlichungen/2011/10/22/AmazonSignatureWrapping.pdf) [publication record](https://www.nds.rub.de/research/publications/amazon-hacking/) — Juraj Somorovsky, Mario Heiderich, Meiko Jensen, Jörg Schwenk, Nils Gruschka, Luigi Lo Iacono

**KEPT** · Meaningful extension · confidence High

### Candidate

ACM CCSW paper presented on 21 October 2011; the Ruhr publication record and
author-hosted paper agree on provenance.

### Core contribution

The work black-boxes Amazon EC2 and Eucalyptus control interfaces and develops
new XML Signature Wrapping variants. It bypasses message freshness and, in one
case, needs only a public certificate to invoke arbitrary control operations. It
also connects web-console XSS to cloud-account compromise and formalizes a
black-box interface-analysis method.

### Prior art

McIntosh and Austel introduced XML Signature Wrapping in 2005, and Gruschka and
Lo Iacono attacked Amazon EC2 with a five-minute signed-message constraint in
2009. The 2011 work explicitly builds on both, removes important constraints,
adds variants and applies a broader control-plane methodology.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 74 | 25% | 18.50 | New variants, constraint removal and black-box control-interface analysis. |
| Transferability | 86 | 20% | 17.20 | General to signed SOAP APIs and privileged management planes. |
| Lasting value | 84 | 20% | 16.80 | Durable warning about control-plane parsers and signed/processed node mismatch. |
| Technical soundness | 88 | 15% | 13.20 | Concrete messages, verified operations and responsible disclosure. |
| Practical usability | 80 | 10% | 8.00 | Mutation and fault-response methodology is directly useful to testers. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Variants, assumptions and prior constraints are carefully laid out. |

**Final score: 82.3/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. The primitive predates 2011, but the new variants and
control-interface analysis materially expand its capability and testability.

## 81.2 — [Static Detection of Access Control Vulnerabilities in Web Applications](https://www.usenix.org/conference/usenix-security-11/static-detection-access-control-vulnerabilities-web-applications) [paper](http://www.usenix.org/events/sec11/tech/full_papers/Sun.pdf) — Fangqi Sun, Liang Xu, Zhendong Su

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

USENIX Security paper and conference record published on 11 August 2011.

### Core contribution

The analysis infers role-specific intended access from source, builds a sitemap
for each role, compares them to identify privileged endpoints, then checks
whether forced browsing reaches those pages without the expected enforcement.
It avoids a hand-written policy and reports known and new flaws with few false
positives on real applications.

### Prior art

Forced browsing, authorization testing and dynamic/probabilistic policy
inference were known. The candidate's first static role-sitemap construction and
implicit-policy enforcement check are the distinct contribution.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 74 | 25% | 18.50 | New source-derived, role-sensitive authorization inference method. |
| Transferability | 84 | 20% | 16.80 | General to role-based web applications and forced-browsing checks. |
| Lasting value | 84 | 20% | 16.80 | Durable approach to application-specific authorization analysis. |
| Technical soundness | 86 | 15% | 12.90 | Static model and real-application evaluation support the claims. |
| Practical usability | 76 | 10% | 7.60 | Requires source but minimizes manually supplied policy. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Inference, sitemap comparison and validation are well specified. |

**Final score: 81.2/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It systematizes authorization testing with
a distinct inferred-policy technique rather than claiming a new access-control bug.

## 81.1 — [Bit-squatting: DNS Hijacking Without Exploitation](https://dinaburg.org/data/DC19_Dinaburg_Presentation.pdf) [Black Hat archive](https://blackhat.com/html/bh-us-11/bh-us-11-archives.html) — Artem Dinaburg

**KEPT** · Original technique · confidence High

### Candidate

Primary author slides and the Black Hat USA/DEF CON 19 records place the public
release in August 2011.

### Core contribution

The attacker registers domains one bit away from frequently requested names and
waits for spontaneous hardware or transmission errors to transform valid DNS
lookups into attacker-controlled names. Controlled registrations and months of
traffic showed background requests, cookies and even update traffic reaching
these domains without a typo or software exploit.

### Prior art

Typosquatting and soft-error reliability research predate 2011. No earlier
primary source located in the mechanism search turned random single-bit memory
faults in machine-generated hostnames into a passive domain-hijacking primitive.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 86 | 25% | 21.50 | Distinct exploitation of physical bit errors through DNS ownership. |
| Transferability | 84 | 20% | 16.80 | Applies to popular domains and machine-generated subresource traffic. |
| Lasting value | 76 | 20% | 15.20 | Enduring conceptual link between fault models and naming security. |
| Technical soundness | 80 | 15% | 12.00 | Real registrations and traffic evidence, with limits on attributing each flip. |
| Practical usability | 74 | 10% | 7.40 | Registration and monitoring are simple, but yield is stochastic. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Domain generation, filtering and observed traffic are described. |

**Final score: 81.1/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It is not merely a spelling variant of typosquatting; the
machine fault is a different trigger with different target selection and traffic.

## 79.3 — [How to Break XML Encryption](https://www.nds.rub.de/media/nds/veroeffentlichungen/2011/10/22/HowToBreakXMLenc.pdf) — Tibor Jager, Juraj Somorovsky

**KEPT** · Original technique · confidence High

### Candidate

Author-hosted ACM CCS paper published in October 2011. This entry was already in
the missed section and is reassessed here so the current audit has a complete
judgement trail.

### Core contribution

The paper constructs adaptive chosen-ciphertext attacks against standards-based
XML Encryption deployments. It turns error and validity behavior around CBC
processing into practical plaintext recovery despite the surrounding XML
structure and tests real libraries and web-service stacks.

### Prior art

Vaudenay's CBC padding oracle and later web padding-oracle exploitation predate
2011. The distinct contribution is the XML Encryption-specific oracle and
recovery construction, including how standards processing exposes the feedback
needed against deployed implementations.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 84 | 25% | 21.00 | New practical break tailored to XML Encryption processing. |
| Transferability | 75 | 20% | 15.00 | Applies across conforming XML-encryption stacks, but not all encryption uses. |
| Lasting value | 82 | 20% | 16.40 | Durable example of format/protocol behavior defeating sound primitives. |
| Technical soundness | 82 | 15% | 12.30 | Formal attack reasoning and tested implementations. |
| Practical usability | 72 | 10% | 7.20 | Practical where an observable XML validity oracle exists. |
| Clarity and reproducibility | 74 | 10% | 7.40 | Complete, though cryptographic details demand specialist knowledge. |

**Final score: 79.3/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It derives a distinct XML Encryption attack rather than
merely demonstrating an unchanged generic padding oracle on a named product.

## 79.3 — [Dark Clouds on the Horizon](https://www.usenix.org/conference/usenix-security-11/presentation/dark-clouds-horizon-using-cloud-storage-attack-vector-and) [paper](https://www.usenix.org/legacy/events/sec11/tech/full_papers/Mulazzani6-24-11.pdf) — Martin Mulazzani, Sebastian Schrittwieser, Manuel Leithner, Markus Huber, Edgar Weippl

**KEPT** · Meaningful combination or adaptation · confidence High

### Candidate

USENIX Security paper and conference record published on 10 August 2011.

### Core contribution

The authors reverse-engineer Dropbox's chunked, hash-based deduplication and
client authentication, then show how knowledge of content hashes can claim
server-resident files without uploading them and turn shared deduplicated
storage into an oracle and effectively unbounded “online slack space.” They also
analyze credential transplantation and practical abuse of the storage service.

### Prior art

Content-addressed storage, client-side deduplication, cloud credential theft and
proofs of possession existed. The contribution combines those properties into
concrete cross-user acquisition and storage-abuse procedures against an
Internet service, then derives the missing-possession-check problem.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 74 | 25% | 18.50 | New practical abuse of global deduplication and weak client trust. |
| Transferability | 82 | 20% | 16.40 | General to client-side deduplicating storage services. |
| Lasting value | 78 | 20% | 15.60 | Durable basis for ownership-proof and deduplication privacy work. |
| Technical soundness | 84 | 15% | 12.60 | Protocol reverse engineering and concrete experiments support the findings. |
| Practical usability | 78 | 10% | 7.80 | Hash-driven tests and credential analysis are actionable. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Protocol, attacks, evaluation and countermeasures are documented. |

**Final score: 79.3/100.** Archive decision: include as a core technique.

### Verdict

Meaningful combination or adaptation. Known storage components are joined into
new cross-account and forensic capabilities that the individual primitives did
not imply operationally.

## 78.8 — [WAPTEC: Whitebox Analysis of Web Applications for Parameter Tampering Exploit Construction](https://www.cs.uic.edu/~hinrichs/papers/bisht2011waptec.pdf) [CCS record](https://www.sigsac.org/ccs/CCS2011/paper_list.shtml) — Prithvi Bisht, Timothy Hinrichs, Nazari Skrupsky, V. N. Venkatakrishnan

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Author-hosted ACM CCS paper published in October 2011.

### Core contribution

WAPTEC extracts constraints from client HTML/JavaScript, models PHP and
database-side acceptance, and solves for inputs the client rejects but the
server accepts. Unlike an opportunity report, it follows candidate executions
to successful sinks and automatically constructs concrete parameter-tampering
exploits. It found previously unknown flaws in every one of six tested apps.

### Prior art

Manual parameter tampering and the same group's 2010 NoTamper system predate
WAPTEC. NoTamper was black-box and left human work between an opportunity and a
confirmed exploit. WAPTEC's cross-tier white-box reasoning and automatic exploit
construction are the marginal contribution.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 68 | 25% | 17.00 | Significant automation advance over NoTamper, not a new flaw class. |
| Transferability | 84 | 20% | 16.80 | General to multi-tier applications with client/server validation asymmetry. |
| Lasting value | 76 | 20% | 15.20 | Durable exploit-confirmation and cross-tier-analysis model. |
| Technical soundness | 88 | 15% | 13.20 | Formalization, implementation and concrete findings on six apps. |
| Practical usability | 80 | 10% | 8.00 | Produces usable exploits automatically when source is available. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Constraints, refinement loop and evaluation are explicit. |

**Final score: 78.8/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It meaningfully advances the 2010
black-box approach from suspected tampering opportunities to constructed proof.

## 78.2 — [Automated Discovery of Parameter Pollution Vulnerabilities in Web Applications](https://www.ndss-symposium.org/ndss2011/automated-discovery-of-parameter-pollution-vulnerabilities-in-web-applications/) [paper](https://www.ndss-symposium.org/wp-content/uploads/2017/09/Bald.pdf) — Marco Balduzzi, Carmen Torrano Gimenez, Davide Balzarotti, Engin Kirda

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

NDSS publication dated 7 February 2011, with the official paper and slides.

### Core contribution

PAPAS fingerprints how back-end technologies resolve duplicate parameters,
discovers candidate injection points and automatically tests both server- and
client-side HTTP Parameter Pollution behavior. Its crawl of more than 5,000
sites showed that vulnerable parameters were widespread and produced confirmed
findings on prominent applications.

### Prior art

HTTP Parameter Pollution was publicly introduced in 2009 and is present in that
year's list; 2010 work also combined it with CSRF. The candidate does not reclaim
the class. Its first automated detection workflow, back-end precedence model and
large-scale measurement are distinct.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 62 | 25% | 15.50 | Strong automation of a technique already public in 2009. |
| Transferability | 86 | 20% | 17.20 | Covers varied frameworks, parameter channels and client/server outcomes. |
| Lasting value | 78 | 20% | 15.60 | Parameter-precedence fingerprinting remains a useful testing model. |
| Technical soundness | 86 | 15% | 12.90 | Explicit phases and a large real-site evaluation. |
| Practical usability | 82 | 10% | 8.20 | Automated black-box workflow produces actionable findings. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Architecture, probes and empirical results are detailed. |

**Final score: 78.2/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. The novelty lies in automated, scalable
discovery and technology-aware interpretation, not in HPP itself.

## 77.4 — [Sour Pickles](https://media.blackhat.com/bh-us-11/Slaviero/BH_US_11_Slaviero_Sour_Pickles_WP.pdf) [Black Hat archive](https://blackhat.com/html/bh-us-11/bh-us-11-archives.html) — Marco Slaviero

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Black Hat USA whitepaper and presentation published on 4 August 2011.

### Core contribution

The work treats Python Pickle as a shellcoding virtual machine. It specifies
stack- and type-preserving ways to prepend or splice opcodes into an existing
object, constructs reliable call and method templates, explores output channels
and constrained unpicklers, and releases Anapickle plus an exploit library for
generic, Django and App Engine targets.

### Prior art

Python's documentation had long warned that unpickling attacker data can execute
functions, and simple exploits—including a March 2011 post—already existed. The
paper openly credits that fact. Its contribution is the first systematic,
reliable exploitation methodology and supporting transformation tools.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 56 | 25% | 14.00 | Known RCE primitive, but substantial new exploit engineering. |
| Transferability | 86 | 20% | 17.20 | General across Pickle-using Python services and frameworks. |
| Lasting value | 84 | 20% | 16.80 | Durable foundation for serialized-object exploitation. |
| Technical soundness | 80 | 15% | 12.00 | Internals, templates and working tools substantiate the method. |
| Practical usability | 88 | 10% | 8.80 | Designed explicitly for converting a found bug into a reliable exploit. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Opcodes, constraints, examples and tools are extensively documented. |

**Final score: 77.4/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It does not claim the dangerous
deserialization behavior as new; it turns toy demonstrations into a reusable
exploitation discipline.

## 76.9 — [BLOCK: A Black-Box Approach for Detection of State Violation Attacks Towards Web Applications](https://ptolemy.berkeley.edu/projects/truststc/pubs/883.html) [ACM record](https://doi.org/10.1145/2076732.2076767) — Xiaowei Li, Yuan Xue

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Institutional publication record and ACSAC paper published in December 2011.

### Core contribution

BLOCK learns stateful behavior from observed request/response sequences and
session variables, derives likely invariants, then generates and evaluates
sequence mutations that reach functions or information in inappropriate states.
It brings state-violation testing to a black-box setting without source
instrumentation or a manually written workflow specification.

### Prior art

Workflow bypass, state-machine inference and 2010 source-assisted logic-flaw
analysis were known. The paper's own closest comparison required source or
instrumentation; black-box invariant learning and attack generation are the
qualifying methodological extension.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 70 | 25% | 17.50 | Distinct black-box state-invariant and violation-detection approach. |
| Transferability | 82 | 20% | 16.40 | General to stateful web workflows and session-backed applications. |
| Lasting value | 76 | 20% | 15.20 | Workflow/state testing remains a durable application-security problem. |
| Technical soundness | 84 | 15% | 12.60 | Formal model, implementation and evaluation support the method. |
| Practical usability | 70 | 10% | 7.00 | No source required, though learned models depend on crawl coverage. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Inputs, inference and testing stages are specified. |

**Final score: 76.9/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It systematizes black-box discovery of
state violations rather than re-labelling a single workflow bypass.

## 74.4 — [I Still Know What You Visited Last Summer](https://research.owlfolio.org/pubs/2011-i-still-know.pdf) — Zachary Weinberg, Eric Y. Chen, Pavithra Ramesh Jayaraman, Collin Jackson

**KEPT** · Meaningful extension · confidence High

### Candidate

IEEE S&P paper published in May 2011. The author-hosted copy gives a complete
paper and date-stamped conference imprint.

### Core contribution

After browsers blocked scripted inspection of visited-link styles, the authors
show that sites can encode the remaining visible color difference into disguised
human tasks—text, image and game-like challenges—and infer history from the
answers. They also demonstrate an optical side channel that lets a permitted
webcam measure screen-light color correlated with visited links.

### Prior art

CSS history sniffing dates to 2002, and the original 2011 nominations include
cache-timing history extraction and CSS timing attacks. This paper's human
interaction channel and screen-reflection measurement bypass the new defense by
different mechanisms, but inherit the older visited-link oracle and have lower
throughput.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 68 | 25% | 17.00 | Two distinct post-defense extraction channels over a known privacy leak. |
| Transferability | 80 | 20% | 16.00 | General human-oracle and physical-output side-channel ideas. |
| Lasting value | 72 | 20% | 14.40 | Durable lesson about UI-visible secrets, though exact visited styling changed. |
| Technical soundness | 84 | 15% | 12.60 | 307-person user study plus a working optical experiment. |
| Practical usability | 58 | 10% | 5.80 | Interactive probing is slow; webcam permission makes the optical path narrow. |
| Clarity and reproducibility | 86 | 10% | 8.60 | Tasks, threat model, study and limitations are explicit. |

**Final score: 74.4/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It is not the already nominated cache or shader timing
method; it introduces user-mediated and physical side channels around the same
browser defense.

## 71.2 — [Crouching Tiger Hidden Payload](https://www.nds.ruhr-uni-bochum.de/media/hgi/veroeffentlichungen/2011/10/19/svgSecurity-ccs11.pdf) — Mario Heiderich, Tilman Frosch, Meiko Jensen, Thorsten Holz

**KEPT** · Meaningful extension · confidence High

### Candidate

Author-hosted ACM CCS paper published in October 2011. It was already in the
missed section and is reassessed for the current history record.

### Core contribution

The paper maps SVG's active features, context-dependent browser handling and
sanitization hazards, then demonstrates payloads that survive common image
workflows or become active when the same content is embedded differently. It
adds a systematic attack surface and test corpus for “image” uploads that are
actually script-capable XML applications.

### Prior art

SVG scripting, XML/XSS and active-file upload risks were known. The contribution
is a deeper, cross-browser systematization of SVG-specific execution contexts,
obfuscation and sanitizer failures rather than invention of active SVG itself.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 64 | 25% | 16.00 | New payload/context catalogue over known active-content foundations. |
| Transferability | 74 | 20% | 14.80 | Applies to SVG upload, embedding, sanitization and browser testing. |
| Lasting value | 68 | 20% | 13.60 | Important file/content lesson, with browser behavior evolving over time. |
| Technical soundness | 78 | 15% | 11.70 | Concrete browser and sanitizer experiments support the findings. |
| Practical usability | 72 | 10% | 7.20 | Payloads and contextual tests are directly useful. |
| Clarity and reproducibility | 79 | 10% | 7.90 | Features, contexts and examples are substantially documented. |

**Final score: 71.2/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It turns scattered knowledge about active SVG into a
reusable attack and sanitizer-testing methodology.

## 68.3 — [Automated Black-Box Detection of Side-Channel Vulnerabilities in Web Applications](https://www.cs.virginia.edu/~evans/pubs/ccs2011/) [paper](https://www.cs.virginia.edu/~evans/pubs/ccs2011/sca-packaged.pdf) — Peter Chapman, David Evans

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Author publication page and ACM CCS paper dated 17–21 October 2011.

### Core contribution

The tool repeatedly crawls a web application under controlled secret states,
captures encrypted network behavior and treats the observable dimensions as a
classification problem. It quantifies distinguishability with multiple metrics
and introduces a Fisher-criterion measure that finds leaks missed or
mischaracterized by entropy-only analysis.

### Prior art

Encrypted web-traffic side channels were established, and 2010's Sidebuster
already automated detection and quantification using application-guided
analysis. The candidate's marginal contribution is black-box repeated crawling,
multi-dimensional classification and the more robust metric—not invention of
the leak class or automated analysis generally.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 52 | 25% | 13.00 | Useful black-box and metric advance over closely related 2010 work. |
| Transferability | 74 | 20% | 14.80 | Applies to varied state-dependent encrypted web interactions. |
| Lasting value | 68 | 20% | 13.60 | Classification remains relevant, though later traffic models advanced. |
| Technical soundness | 82 | 15% | 12.30 | Clear method and evaluation on deployed applications and defenses. |
| Practical usability | 64 | 10% | 6.40 | Black-box access helps, but controlled repeated states and traffic are required. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Metrics, crawl procedure and comparisons are well described. |

**Final score: 68.3/100.** Archive decision: include as a supporting reference
under the general judge mapping and as qualifying historical-list material under
this audit's explicit 60-point rule.

### Verdict

Tooling or methodology contribution. The overlap with Sidebuster keeps the
score below 70; the black-box classifier and Fisher metric remain distinct and
strong enough for the historical gate.
