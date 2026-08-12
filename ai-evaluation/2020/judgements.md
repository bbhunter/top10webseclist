# 2020 candidate judgements

These scorecards apply the repository's weighted judge rubric. `KEPT` means the
candidate met the historical 60-or-above inclusion rule as well as the
first-publication, originality-verdict and original-nomination exclusions.

## 86.7 — [Timeless Timing Attacks: Exploiting Concurrency to Leak Secrets over Remote Connections](https://www.usenix.org/conference/usenixsecurity20/presentation/van-goethem) — Tom Van Goethem, Christina Pöpper, Wouter Joosen, Mathy Vanhoef

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2020 and already
present in the missed section.

### Core contribution

The attacker sends two HTTP/2 or Tor requests concurrently over one connection
and compares their response ordering. Removing network jitter makes sub-
millisecond server-side timing differences remotely observable and turns
otherwise impractical timing flaws into reliable secret-recovery attacks.

### Prior art

Remote timing attacks and statistical jitter reduction were established. The
same-connection concurrent request pair, response-order oracle and protocol-
level techniques for making the requests arrive together were not.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 90 | 25% | 22.50 | Introduces jitter-free remote timing through concurrency. |
| Transferability | 90 | 20% | 18.00 | Applies to many server-side comparisons and multiplexed protocols. |
| Lasting value | 88 | 20% | 17.60 | Changed how remote timing attacks are designed and tested. |
| Technical soundness | 90 | 15% | 13.50 | Protocol analysis and end-to-end attacks validate the oracle. |
| Practical usability | 70 | 10% | 7.00 | Strong but depends on concurrency and response-order control. |
| Clarity and reproducibility | 81 | 10% | 8.10 | Preconditions, synchronization and demonstrations are explicit. |

**Final score: 86.7/100.** Archive decision: include as a core technique.

### Verdict

Original technique. Concurrency removes the dominant noise source rather than
merely applying a familiar timing test to a new target.

## 84.7 — [Composition Kills: 18 Attacks on Email Sender Authentication](https://www.usenix.org/conference/usenixsecurity20/presentation/chen-jianjun) [Tool](https://github.com/chenjj/espoofer) — Jianjun Chen, Vern Paxson, Jian Jiang

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2020 and already
present in the missed section.

### Core contribution

Different SMTP, sender-authentication and mail-client parsers disagree over
which identity a message asserts. The work composes those discrepancies into
18 spoofing attacks that pass SPF, DKIM or DMARC yet display an attacker-chosen
sender, and supplies the ESpoofer evaluation tool.

### Prior art

Email spoofing, parser differentials and weaknesses in individual sender-
authentication mechanisms were known. The systematic cross-layer composition
model and its authenticated-spoofing families were not.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 88 | 25% | 22.00 | Defines a broad parser-composition spoofing class. |
| Transferability | 88 | 20% | 17.60 | Crosses servers, authentication schemes and mail clients. |
| Lasting value | 86 | 20% | 17.20 | Durable lesson for identity checks across layered parsers. |
| Technical soundness | 88 | 15% | 13.20 | Taxonomy, experiments and provider testing align. |
| Practical usability | 72 | 10% | 7.20 | ESpoofer makes the families testable, with provider caveats. |
| Clarity and reproducibility | 75 | 10% | 7.50 | Attack syntax and evaluation method are documented. |

**Final score: 84.7/100.** Archive decision: include as a core technique.

### Verdict

Original technique. It establishes parser composition as the common cause of a
previously unorganized set of authenticated sender-spoofing attacks.

## 82.2 — [Prototype Pollution and bypassing client-side HTML sanitizers](https://www.securitum.com/prototype-pollution-and-bypassing-client-side-html-sanitizers.html) — Michał Bentkowski

**KEPT** · Original technique · confidence High

### Candidate

Researcher-authored 2020 publication associated with Black Hat USA 2020 and
already present in the missed section.

### Core contribution

Client-side prototype pollution plants inherited configuration properties that
HTML sanitizers read as trusted options. This turns a pollution source into
reusable sanitizer-specific gadgets that admit dangerous markup and produce
XSS even where the sanitizer itself is otherwise functioning as designed.

### Prior art

Prototype pollution, client-side XSS gadgets and sanitizer bypasses were known
separately. Using inherited configuration state to alter a sanitizer's security
policy was a new, transferable sink class.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 84 | 25% | 21.00 | Establishes sanitizer configuration as a pollution sink. |
| Transferability | 85 | 20% | 17.00 | Generalizes across libraries that trust inherited options. |
| Lasting value | 84 | 20% | 16.80 | Seeded durable client-side gadget-hunting methodology. |
| Technical soundness | 84 | 15% | 12.60 | Concrete bypasses support the causal model. |
| Practical usability | 72 | 10% | 7.20 | Requires a pollution source and compatible sanitizer gadget. |
| Clarity and reproducibility | 76 | 10% | 7.60 | Payloads and affected property behavior are shown. |

**Final score: 82.2/100.** Archive decision: include as a core technique.

### Verdict

Original technique. The work turns prototype inheritance into a sanitizer-
policy override, not simply another vulnerable package demonstration.

## 81.5 — [PMForce: Systematically Analyzing PostMessage Handlers at Scale](https://publications.cispa.saarland/3164/) — Marius Steffens, Ben Stock

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

The author repository deposited the paper on 29 July 2020 before ACM CCS 2020.
Its primary URL was absent from the 63-link exclusion set.

### Core contribution

PMForce analyzes handlers inside a browser using selective forced execution,
lightweight taint tracking and extracted path constraints, then combines exploit
templates with Z3 to generate messages that prove code execution, state changes
or data leaks. It automatically exploited 111 handlers in the top 100,000 sites.

### Prior art

Unsafe `postMessage` handlers, missing origin checks and manual or static
analyses were established, including the 2013 Postman methodology. PMForce's
browser-internal forced execution and constraint-guided exploit generation make
previously manual validation work at Web scale.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 72 | 25% | 18.00 | New forced-execution and exploit-synthesis combination. |
| Transferability | 82 | 20% | 16.40 | Handles diverse sites, message schemas and client-side sinks. |
| Lasting value | 82 | 20% | 16.40 | Advances scalable validation of browser message handlers. |
| Technical soundness | 90 | 15% | 13.50 | Large-scale evaluation distinguishes traces from exploits. |
| Practical usability | 88 | 10% | 8.80 | Automatically produces concrete triggering messages. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Architecture, constraints and evaluation are explicit. |

**Final score: 81.5/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. The underlying bugs are known; automated
forced execution plus solver-backed exploit generation is the qualifying gain.

## 80.2 — [Carnus: Exploring the Privacy Threats of Browser Extension Fingerprinting](https://www.ndss-symposium.org/ndss-paper/carnus-exploring-the-privacy-threats-of-browser-extension-fingerprinting/) — Soroush Karami, Panagiotis Ilia, Konstantinos Solomos, Jason Polakis

**KEPT** · Meaningful extension · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2020. Its primary URL and
mechanism were absent from the original 2020 nominations.

### Core contribution

Carnus automatically derives behavior-based extension fingerprints and adds
two observation channels: extension-generated HTTP requests and intra-browser
message exchanges. It identifies 29,428 extensions and remains effective
against the contemporary state-of-the-art countermeasure.

### Prior art

Browser fingerprinting and extension detection through web-accessible resources
were established. Automated behavioral fingerprint generation and the two
communication channels materially expand the technique beyond exposed files or
DOM artifacts.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78 | 25% | 19.50 | Adds automated behavioral and communication fingerprints. |
| Transferability | 80 | 20% | 16.00 | Applies across thousands of extensions and user populations. |
| Lasting value | 78 | 20% | 15.60 | Broadens extension privacy threat models beyond resources. |
| Technical soundness | 89 | 15% | 13.35 | Large corpus and countermeasure testing support the claims. |
| Practical usability | 76 | 10% | 7.60 | Automated analysis lowers the cost of generating probes. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Channels, pipeline and evaluation are detailed. |

**Final score: 80.2/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It moves extension fingerprinting from exposed static
resources to automatically inferred behavior and browser communications.

## 78.9 — [CDN Judo: Breaking the CDN DoS Protection with Itself](https://www.ndss-symposium.org/ndss-paper/cdn-judo-breaking-the-cdn-dos-protection-with-itself/) — Run Guo et al.

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2020. The primary URL survived
exact and semantic exclusion against the year list.

### Core contribution

Crafted but legal requests exploit CDN-to-origin forwarding behavior: HTTP/2
conversion and pre-POST behavior amplify bandwidth or connection consumption,
while low-churn forwarding IP sets let an attacker selectively sever the CDN's
origin paths. The protection layer becomes the mechanism for origin denial.

### Prior art

Application-layer DoS, CDN origin exposure and amplification were known. Abuse
of CDN request conversion, pre-forwarding and concentrated origin connections
as three systematic CDN-to-origin attack primitives was not found earlier.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 78 | 25% | 19.50 | Defines three CDN forwarding abuse mechanisms. |
| Transferability | 78 | 20% | 15.60 | Observed across six major CDN vendors. |
| Lasting value | 76 | 20% | 15.20 | Durable warning about intermediary-to-origin asymmetry. |
| Technical soundness | 88 | 15% | 13.20 | Cross-vendor tests and disclosures validate the threats. |
| Practical usability | 72 | 10% | 7.20 | Legal requests are usable, though vendor behavior varies. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Request behaviors, constraints and outcomes are specified. |

**Final score: 78.9/100.** Archive decision: include as a core technique.

### Verdict

Original technique. The work makes CDN forwarding semantics, rather than raw
attacker bandwidth, the reusable DoS primitive.

## 78.8 — [FUSE: Finding File Upload Bugs via Penetration Testing](https://www.ndss-symposium.org/ndss-paper/fuse-finding-file-upload-bugs-via-penetration-testing/) — Taekjin Lee, Seongil Wi, Suyoung Lee, Sooel Son

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2020. It was neither linked nor
semantically represented in the original 2020 nominations.

### Core contribution

FUSE mutates multipart upload requests so they bypass server-side content
filters while preserving executable semantics, then triggers uploaded files to
confirm exploitability. It found 30 previously unreported executable-upload
bugs, including 15 CVEs, across 33 PHP applications.

### Prior art

Unrestricted file uploads, polyglots and many filter bypasses were long known.
FUSE contributes the first penetration-testing workflow that systematically
generates semantics-preserving bypass payloads and verifies uploaded execution.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 72 | 25% | 18.00 | Systematizes semantics-preserving upload mutation. |
| Transferability | 76 | 20% | 15.20 | Works across varied PHP applications and filter stacks. |
| Lasting value | 78 | 20% | 15.60 | Provides a reusable model for executable-upload testing. |
| Technical soundness | 88 | 15% | 13.20 | Confirmed bugs and CVEs substantiate the method. |
| Practical usability | 86 | 10% | 8.60 | Generates and validates exploit payloads automatically. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Mutations, preservation requirement and tests are detailed. |

**Final score: 78.8/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. File-upload exploitation is old; reliable,
semantics-preserving generation and confirmation across applications is new.

## 77.2 — [The Cookie Hunter: Automated Black-box Auditing for Web Authentication and Authorization Flaws](https://www.cs.uic.edu/~polakis/classes/CS568/fall-2020/cookiehijacker-ccs20.pdf) [Tool](https://gitlab.com/kostasdrk/xdriver3-open) — Kostas Drakonakis, Sotiris Ioannidis, Jason Polakis

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

The ACM CCS paper records publication in November 2020. Its primary paper URL
and tool were absent from the exclusion set.

### Core contribution

The framework automates account creation, infers authentication-cookie roles,
tests multiple hijacking threat models, and uses differential oracles to
determine resulting account access and exposed personal data. It completed
black-box audits of roughly 25,000 domains.

### Prior art

Cookie theft, missing flags, active HTTPS hijacking and automated scanners were
well established, including CookieMonster in 2008. Fully automated account
lifecycle handling, privilege inference and impact validation across arbitrary
web applications provide the qualifying methodology advance.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 58 | 25% | 14.50 | Automates a known class with new state and impact oracles. |
| Transferability | 82 | 20% | 16.40 | Black-box operation spans diverse application designs. |
| Lasting value | 78 | 20% | 15.60 | Reusable model for end-to-end authentication auditing. |
| Technical soundness | 90 | 15% | 13.50 | Large-scale completed audits and validation support it. |
| Practical usability | 88 | 10% | 8.80 | Account handling and differential analysis reduce manual work. |
| Clarity and reproducibility | 84 | 10% | 8.40 | Components, threat models and released automation are clear. |

**Final score: 77.2/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. It does not reinvent cookie hijacking; it
makes complete black-box authentication and authorization audits scalable.

## 75.0 — [A Tale of Two Headers: A Formal Analysis of Inconsistent Click-Jacking Protection on the Web](https://www.usenix.org/conference/usenixsecurity20/presentation/calzavara) — Stefano Calzavara, Sebastian Roth, Alvise Rabitti, Michael Backes, Ben Stock

**KEPT** · Tooling or methodology contribution · confidence High

### Candidate

Peer-reviewed USENIX Security paper published in August 2020. Its primary URL
and formal cross-browser policy mechanism were absent from the year list.

### Core contribution

The work formalizes how browsers combine CSP `frame-ancestors` and the
underspecified X-Frame-Options header, builds an analyzer for browser-specific
policy outcomes, finds that 10% of distinct deployed policies are inconsistent,
and supplies a server-side retrofit proxy.

### Prior art

Clickjacking, XFO, CSP and browser compatibility differences were well known.
The formal consistency criterion and automated differential policy analyzer
turn ad-hoc compatibility advice into a reproducible security test.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 56 | 25% | 14.00 | Formalizes and automates a known browser mismatch problem. |
| Transferability | 76 | 20% | 15.20 | Covers deployed policy combinations and multiple browsers. |
| Lasting value | 76 | 20% | 15.20 | Durable differential-testing lesson for security headers. |
| Technical soundness | 92 | 15% | 13.80 | Formal model, analyzer and Web measurement agree. |
| Practical usability | 80 | 10% | 8.00 | Analyzer and retrofit design translate directly to audits. |
| Clarity and reproducibility | 88 | 10% | 8.80 | Semantics, inconsistency cases and evaluation are explicit. |

**Final score: 75.0/100.** Archive decision: include as a core technique.

### Verdict

Tooling or methodology contribution. The attack class is old, but systematic
cross-browser enforcement analysis is a meaningful offensive testing method.

## 73.5 — [Melting Pot of Origins: Compromising the Intermediary Web Services that Rehost Websites](https://www.ndss-symposium.org/ndss-paper/melting-pot-of-origins-compromising-the-intermediary-web-services-that-rehost-websites/) — Takuya Watanabe, Eitaro Shioji, Mitsuaki Akiyama, Tatsuya Mori

**KEPT** · Original technique · confidence High

### Candidate

Peer-reviewed NDSS paper published in February 2020 and already present in the
missed section.

### Core contribution

Intermediary services fetch and rehost unrelated sites beneath their own origin.
That architecture collapses the browser's origin boundary: one rehosted site's
content can act with the service origin's authority against other rehosted
content or service functionality. The study systematizes the vulnerable service
patterns and demonstrates compromises.

### Prior art

Same-origin policy, hosting-provider same-origin risks and content-proxy bugs
were known. Treating rehosting intermediaries as systematic origin-flattening
services and mapping the resulting cross-customer attacks was distinct.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 75 | 25% | 18.75 | Identifies rehosting as an origin-flattening attack class. |
| Transferability | 78 | 20% | 15.60 | Applies to multiple intermediary service designs. |
| Lasting value | 74 | 20% | 14.80 | Durable isolation lesson for fetch-and-rehost products. |
| Technical soundness | 82 | 15% | 12.30 | Systematic study and exploits support the model. |
| Practical usability | 55 | 10% | 5.50 | Exploitation depends on a vulnerable rehosting workflow. |
| Clarity and reproducibility | 65 | 10% | 6.50 | Patterns are clear though service-specific details vary. |

**Final score: 73.5/100.** Archive decision: include as a core technique.

### Verdict

Original technique. The security boundary failure is architectural SOP
flattening by intermediaries, not a single service's isolated XSS.

## 72.0 — [DOM Clobbering strikes back](https://portswigger.net/research/dom-clobbering-strikes-back) — Gareth Heyes

**KEPT** · Meaningful extension · confidence High

### Candidate

Researcher-authored PortSwigger Research post published in 2020 and already
present in the missed section.

### Core contribution

The work expands markup-only DOM clobbering with multi-level property chains,
form collections and URL-string behavior, then shows how the primitives reach
useful JavaScript gadgets even when script injection is blocked by sanitization
or CSP.

### Prior art

DOM clobbering dates back years and the same author documented the class in
2013. The new browser-object constructions and sanitizer-compatible exploit
chains materially extend, but do not replace, that original primitive.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 66 | 25% | 16.50 | Adds useful multi-level and sanitizer-compatible primitives. |
| Transferability | 80 | 20% | 16.00 | Targets common DOM name resolution across applications. |
| Lasting value | 75 | 20% | 15.00 | Expanded modern DOM-clobbering gadget methodology. |
| Technical soundness | 80 | 15% | 12.00 | Browser-tested constructions support the claims. |
| Practical usability | 65 | 10% | 6.50 | Requires a markup injection and compatible gadget. |
| Clarity and reproducibility | 60 | 10% | 6.00 | Payloads are concrete but the treatment is compact. |

**Final score: 72.0/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. It adds reusable constructions to the established DOM-
clobbering class rather than rediscovering the original technique.

## 71.7 — [Deceptive Previews: A Study of the Link Preview Trustworthiness in Social Platforms](https://www.ndss-symposium.org/ndss-paper/deceptive-previews-a-study-of-the-link-preview-trustworthiness-in-social-platforms/) — Giada Stivala, Giancarlo Pellegrino

**KEPT** · Meaningful extension · confidence Medium

### Candidate

Peer-reviewed NDSS paper published in February 2020. Its primary URL and link-
preview mechanism were absent from the year list.

### Core contribution

An attacker controls preview metadata, redirect behavior or the difference
between the platform fetcher's view and the user's landing target to display a
benign-looking preview for a malicious link. The study derives reproducible
crafting strategies across 20 platforms and bypasses URL checks with client-
and server-side redirections.

### Prior art

Phishing, misleading metadata, URL redirection and platform-specific preview
spoofing were known. The cross-platform preview-generation model and systematic
separation of preview identity from landing identity form the extension.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 64 | 25% | 16.00 | Systematizes preview/landing identity mismatches. |
| Transferability | 74 | 20% | 14.80 | Demonstrated across 20 social and messaging platforms. |
| Lasting value | 66 | 20% | 13.20 | Useful model for link unfurlers and phishing reviews. |
| Technical soundness | 83 | 15% | 12.45 | Controlled platform experiments support the taxonomy. |
| Practical usability | 70 | 10% | 7.00 | Attacker-controlled pages and redirects suffice. |
| Clarity and reproducibility | 82 | 10% | 8.20 | Preview fields, platform behavior and bypasses are detailed. |

**Final score: 71.7/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. Familiar deception components are organized into a
transferable attack model for platform-generated link previews.

## 56.7 — [SharePoint and Pwn: Remote Code Execution Against SharePoint Server Abusing DataSet](https://srcincite.io/blog/2020/07/20/sharepoint-and-pwn-remote-code-execution-against-sharepoint-server-abusing-dataset.html) — Steven Seeley, Source Incite

**REMOVED** · Useful application or case study · confidence High

### Candidate

Published 20 July 2020. Judged in the 2026-08-12 pass over the ysonet
.NET-deserialization reference set.

### Core contribution

A breakdown of CVE-2020-1147 and a path from it to RCE as a low-privileged
SharePoint user: the DataSet XML schema lets the payload declare a column's
msdata:DataType, and an existing column definition is temporarily added to the
type allow-list, so an attacker-chosen type such as ObjectDataProvider is
constructed during XML deserialization.

### Prior art

The post opens by crediting the bug to Oleksandr Mirosh, Markus Wulftange and
Jonathan Birch. Their own presentation of the underlying work, "Room for Escape:
Scribbling Outside the Lines of Template Security" (Black Hat USA 2020), is
already a 2020 nomination on this list, and Microsoft published the DataSet
security guidance the post quotes. What is added is the SharePoint reachability
analysis, not the DataSet primitive.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 38 | 25% | 9.50 | Analysis of a bug whose discoverers and their own writeup are already represented on this list. |
| Transferability | 48 | 20% | 9.60 | The DataSet schema trick transfers, but it is the credited researchers' contribution rather than this post's. |
| Lasting value | 52 | 20% | 10.40 | Widely read as the readable explanation of the DataSet gadget; the knowledge itself is nominated elsewhere. |
| Technical soundness | 84 | 15% | 12.60 | Schema, code and constraints are demonstrated precisely and honestly, including the deliberate omission of a full exploit. |
| Practical usability | 66 | 10% | 6.60 | Enough to reproduce the primitive, deliberately not enough to weaponise. |
| Clarity and reproducibility | 80 | 10% | 8.00 | Clear, sequential and well evidenced. |

**Final score: 56.7/100.** Archive decision: do not include.

### Verdict

Useful application or case study — below the gate, and the underlying technique
is already nominated for 2020 through its discoverers' own publication.

### Reverification

- **Candidate facts rechecked against:** the archived post, which states the
  date and credits the three discoverers by name.
- **Independent prior-art check:** confirmed "Room for Escape" is present in
  2020.md, and checked whether this post adds a primitive beyond it; the addition
  is the SharePoint reach, not the DataSet mechanism.
- **Strongest challenge to the result:** this is the version most practitioners
  actually learned the DataSet gadget from.
- **Benefit-of-doubt check:** popularisation is credited separately from
  discovery under the neutrality rules and does not raise the novelty score.
- **Changes after reverification:** none.

## 51.8 — [CVE-2020-0688: Losing the keys to your kingdom](https://securitylab.github.com/research/exchange-rce-CVE-2020-0688/) — Alvaro Munoz, GitHub Security Lab

**REMOVED** · Useful application or case study · confidence High

### Candidate

Published 4 March 2020. Judged in the 2026-08-12 pass over the ysonet
.NET-deserialization reference set.

### Core contribution

A short commentary on Exchange shipping a fixed ASP.NET validation key, so any
authenticated mailbox user can sign a ViewState payload and reach RCE, together
with a useful enumeration of the ways machine keys leak in general — local file
inclusion and XXE against web.config, padding oracles, error pages, public
repositories, and one-click installers with hardcoded keys.

### Prior art

The post states its own position in the chain: it opens from Microsoft's
advisory and says ZDI's analysis, published the week before, "confirmed my
guess". The leak taxonomy is drawn from the author's own LocoMocoSec 2018
presentation, which it links. ViewState RCE with a known machine key was already
established by 2019, including the entry already on the 2019 list.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 30 | 25% | 7.50 | Commentary on a vulnerability analysed publicly a week earlier, restating a taxonomy from the author's 2018 talk. |
| Transferability | 55 | 20% | 11.00 | The machine-key leak taxonomy is genuinely reusable when testing any ASP.NET application. |
| Lasting value | 50 | 20% | 10.00 | The static-key lesson endured; this specific write-up is not the citation others use. |
| Technical soundness | 72 | 15% | 10.80 | Accurate, but it defers the mechanics to the ZDI advisory rather than demonstrating them. |
| Practical usability | 55 | 10% | 5.50 | The leak checklist is usable; there is no exploitation detail. |
| Clarity and reproducibility | 70 | 10% | 7.00 | Clearly written and short; nothing to reproduce. |

**Final score: 51.8/100.** Archive decision: do not include.

### Verdict

Useful application or case study. It is secondary analysis, and the original
disclosure it discusses is neither this post nor this URL.

### Reverification

- **Candidate facts rechecked against:** the archived post, which carries the
  4 March 2020 date and its own acknowledgement of the earlier ZDI analysis.
- **Independent prior-art check:** traced the disclosure order — MSRC February
  2020, ZDI 24 February 2020, this post 4 March 2020 — and checked the 2019 list
  for existing ViewState-with-known-key coverage.
- **Strongest challenge to the result:** the machine-key leak taxonomy is a
  genuinely useful contribution in its own right.
- **Benefit-of-doubt check:** that taxonomy is why transferability is scored at
  55 rather than lower; it does not make the post a first disclosure.
- **Changes after reverification:** none.
