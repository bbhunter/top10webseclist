# 2026 candidate scoring

Every candidate collected for [`2026-ai.md`](../../2026-ai.md) was evaluated with the
[`webseclist-judge-reference`](../../.claude/skills/webseclist-judge-reference/SKILL.md) skill.
This folder is the record: what was scored, what survived, and why.

- **[judgements.md](judgements.md)** — the per-entry detail: score, verdict, what is
  genuinely new, what was already known, and the closest prior art with links. This is
  where the removed entries' links are preserved.
- **[history.jsonl](history.jsonl)** — the append-only machine-readable audit trail.
  Its first 160 events are labelled `baseline-import`: they capture the scorecards that
  existed when history tracking was introduced, without inventing earlier timestamps.
- The index below is the same data sorted by score.

## Method

For full-evidence judgements, candidates were read in full, then prior-art searched two ways — by *mechanism* against
the local `archived-references/` corpus using several phrasings, and against the open web
for the earliest and the closest work, following citations backward. The six weighted
categories were then scored and totalled with
[`score.py`](../../.claude/skills/webseclist-judge-reference/scripts/score.py).

| Category | Weight |
|---|---:|
| Original contribution | 25% |
| Transferability | 20% |
| Lasting value | 20% |
| Technical soundness | 15% |
| Practical usability | 10% |
| Clarity and reproducibility | 10% |

The scoring rule that shapes these results more than any other: **impact is not research
value.** A CVSS 10.0 on a famous target can teach nothing new, and an obscure parser quirk
can introduce a primitive that reshapes a class. What is scored is the *marginal*
contribution over the closest prior art — so a competent writeup applying a known class to
a new target lands in the 30s–50s no matter how serious the bug.

## Results

The current display threshold is **55**, following the requested September threshold review. A qualifying score also needs a verified publication year and an Original, Extension, Combination, or Tooling/Methodology verdict. Case studies, duplicates and insufficient-evidence records do not become eligible just by crossing 55. This display rule is distinct from the judge's general supporting-reference threshold of 50.

Current totals, reconciled on **10 September 2026**, are **240 grouped evaluation records: 103 kept and 137 removed**. Of these records, **44 contain full six-category scorecards**; the remainder are compact historical assessments or explicitly unresolved records. They must not all be described as full-evidence judgements. Unscored watchlist leads are outside these totals.

| Band | Records | Current outcome |
|---|---:|---|
| 70–100 | 29 | 29 kept; 0 removed |
| 60–69.9 | 76 | 72 kept; 4 removed |
| 55–59.9 | 5 | 2 kept; 3 removed |
| 50–54.9 | 47 | 0 kept; 47 removed |
| Below 50 | 83 | 0 kept; 83 removed |

The preceding September sweep contained 76 retained entries. This threshold reconciliation adds **27 grouped entries**, after full original-source and prior-art review where an old compact assessment needed upgrading. Numerical changes are explicit fresh judgements, not invented reconstructions of the old category scores. Nys retains its existing 58.0 full scorecard and is promoted by the threshold change alone.

Four qualifying studies are excluded from 2026 because their technical disclosure belongs in 2025: Bullseye (64.6), TranSPArent (69.1), One Email, Many Faces / OriginMail (61.3), and Network-Level Prompt and Trait Leakage (69.5). Each has a full original-source evaluation and a grouped 2025 listing. The latter was completed in the parallel historical review. [The 2025 record](../2025/judgements.md) also supersedes old cross-year suggestions for RebirthDay (56.8) and Jakarta EL (56.3): both remain excluded as useful applications/case studies after earlier primary exploitation evidence was established.

VulGenie and Fratric's browser-agent talk remain **Insufficient evidence**. VulGenie's full paper is now readable, but its December 2025 artifact cannot be read to establish the first technical version. Fratric's complete technical presentation remains unavailable. Their retained historical totals (59.1 and 57.5) are provenance, not newly validated six-category scores. Other threshold exclusions are h2 WAF bypass (49.7), the Wiz GitHub case study (59.9), Shaking the MCP Tree (54.5), Speculation Rules token leakage (47.5), and VaultRaider (54.2). Detailed evidence and narrower claims appear in [judgements.md](judgements.md).

### Threshold reconciliation inventory

All 38 previously removed records scoring 55–59.9 were reconciled. This is a bounded review of existing candidates, not a new exhaustive internet sweep. Original-source access, frozen publication-time evidence, independent mechanism searches and skeptical reverification were required for fresh additions. Experiments were not rerun. The five moved DEF CON URLs remain grouped with their historical card identifiers through current-slide links; they are not additional candidates.

| Historical score | Current score | Outcome | Candidate |
|---:|---:|---|---|
| 59.8 | 68.6 | Retained | [Almost Impossible: Java Deserialization Through Broken Crypto in OpenText Directory Services](https://slcyber.io/research-center/almost-impossible-java-deserialization-through-broken-crypto-in-opentext-directory-services/) |
| 59.5 | 67.9 | Retained | [Avoiding the paradox: A native full-read SSRF and one-shot DoS in SvelteKit](https://zhero-web-sec.github.io/research-and-things/avoiding-the-paradox-a-native-full-read-ssrf-and-oneshot-dos-in-sveltekit) |
| 59.3 | 67.6 | Retained | [The Usual Suspect: Type Confusion in Twelve Bytes](https://blog.voorivex.team/usual-suspect-type-confusion-in-twelve-bytes) |
| 59.2 | 49.7 | Excluded; see full record | [HTTP/2 WAF Bypass: A Black-Box Methodology (h2 framing)](https://lab.ctbb.show/research/h2-WAF-Bypasses) |
| 59.2 | 66.1 | Retained | [Claude in Chrome: from alert(1) to full account takeover](https://labs.zenity.io/post/claude-in-chrome-from-alert-to-full-account-takeover) |
| 59.1 | 64.0 | Retained | [Grand Theft Atlas](https://labs.zenity.io/post/grand-theft-atlas) |
| 59.1 | 59.8 | Retained | [Computer-Use and TOCTOU: What You Click Is Not What You Get!](https://embracethered.com/blog/posts/2026/toctou-agent-what-you-click-is-not-what-you-get/) |
| 59.1 | 59.1 | Pending evidence | [Patch-Guided Vulnerability Detection: Extracting Java API Security Rules via Attack–Defense Cross-Analysis (VulGenie)](https://www.usenix.org/conference/usenixsecurity26/presentation/chen-bofei) |
| 59.0 | 71.5 | Retained | [Cruising for Shells in Flowise](https://www.elttam.com/blog/cruising-for-shells-in-flowise) |
| 59.0 | 61.7 | Retained | [Security Considerations on Istio’s CRDs with Namespace-based Multi-Tenancy](https://istio.io/latest/blog/2026/security-considerations-on-namespace-based-multi-tenancy/) |
| 59.0 | 64.1 | Retained | [The Memory Heist](https://www.ayush.digital/blog/the-memory-heist) |
| 59.0 | 66.8 | Retained | [Web Cache Overflow: Exploiting Imprecise Keys for Cache Degradation and Beyond](https://arxiv.org/abs/2608.04744) |
| 57.8 | 64.6 | Excluded; see full record | [Bullseye: Detecting Prototype Pollution in NPM Packages with Proof of Concept Exploits](https://www.ndss-symposium.org/ndss-paper/bullseye-detecting-prototype-pollution-in-npm-packages-with-proof-of-concept-exploits/) |
| 57.8 | 60.4 | Retained | [The Dot-Dot-Slash That Frameworks Hand You: CSPT Across Every Major Frontend Framework](https://lab.ctbb.show/research/the-dot-dot-slash-that-frameworks-hand-you) |
| 57.7 | 63.2 | Retained | [Three 0-Day Vulnerabilities in Adminer](https://blog.voorivex.team/three-0-day-vulnerabilities-in-adminer) |
| 57.5 | 57.5 | Pending evidence | [Beyond the Limits of Site Isolation](https://www.youtube.com/watch?v=d3nfJL86jrc) |
| 57.2 | 65.5 | Retained | [AgentForger: ChatGPT Cross-Site Agent Forgery](https://labs.zenity.io/post/agentforger-part-1-chatgpt-cross-site-agent-forgery) |
| 56.8 | 66.0 | Retained | [KindaRails2Shell: how a MATLAB file reads your secrets and pops a shell on Rails](https://ethiack.com/info-hub/research/kindarails2shell-how-a-matlab-file-reads-your-secrets-and-pops-a-shell-on-ruby-on-rails) |
| 56.8 | 59.9 | Excluded; see full record | [GitHub RCE Vulnerability: CVE-2026-3854](https://www.wiz.io/blog/github-rce-vulnerability-cve-2026-3854) |
| 56.5 | 73.0 | Retained | [DOMPurify XSS via `<selectedcontent>` re-clone](https://github.com/cure53/DOMPurify/security/advisories/GHSA-87xg-pxx2-7hvx) |
| 56.2 | 66.2 | Retained | [SearchLeak: Parameter-to-Prompt injection in Microsoft Copilot](https://www.varonis.com/blog/searchleak) |
| 56.2 | 68.6 | Retained | [Breaking the Boundaries: Analyzing QUIC Frame-Packet Interactions With QUIC-Attacker](https://www.usenix.org/conference/usenixsecurity26/presentation/erinola) |
| 56.0 | 64.8 | Retained | [Caught in the Octopus Trap: Unauthenticated RCE in Argo CD](https://www.synacktiv.com/en/publications/caught-in-the-octopus-trap-unauthenticated-rce-in-argo-cd-with-codeql) |
| 56.0 | 64.3 | Retained | [The sorry state of skill distribution](https://blog.trailofbits.com/2026/06/03/the-sorry-state-of-skill-distribution/) |
| 55.9 | 61.1 | Retained | [Zero-Click RCE in Figma Desktop](https://lab.ctbb.show/research/figma-desktop-zero-click-rce/) |
| 55.7 | 62.8 | Retained | [ELF in the Pixels: Building Shared Object–Image Polyglots](https://blog.babelo.xyz/posts/elf-in-the-pixels/) |
| 55.5 | 63.2 | Retained | [Race Against The Patch: Four Exploit Chains in LiteLLM](https://starlabs.sg/blog/2026/05-race-against-the-patch-the-evolution-of-four-exploit-chains-in-litellm/) |
| 55.3 | 54.5 | Excluded; see full record | [Shaking the MCP Tree: A Security Deep Dive](https://blog.voorivex.team/shaking-the-mcp-tree) |
| 55.2 | 66.3 | Retained | [Living Off The Pipeline: Defensive Research, Weaponized (SmokedMeat / Brisket)](https://labs.boostsecurity.io/articles/introducing-smokedmeat/) |
| 55.2 | 66.5 | Retained | [Scanning the Scanners: Turning Security Vendors into Supply-Chain Weapons](https://i.blackhat.com/BH-USA-26/Presentations/US-26-Karger-Scanning-The-Scanners-Thursday.pdf) |
| 68.0 | 69.5 | Excluded; see full record | [Network-Level Prompt and Trait Leakage in Local Research Agents](https://www.usenix.org/conference/usenixsecurity26/presentation/jeong) |
| 59.6 | 69.1 | Excluded; see full record | [TranSPArent: Taint-style Vulnerability Detection in Generic Single Page Applications through Automated Framework Abstraction](https://www.ndss-symposium.org/wp-content/uploads/2026-f1721-paper.pdf) |
| 59.4 | 62.8 | Retained | [When Authorization Loses Its Meaning: Breaking and Fixing Third-Party Online Payments](https://www.usenix.org/conference/usenixsecurity26/presentation/xiao) |
| 57.2 | 65.1 | Retained | [XSS2Shell: WordPress Preauth XSS to RCE Chain (CVE-2026-64638)](https://pwn.ai/blog/xss2shell) |
| 55.8 | 61.3 | Excluded; see full record | [One Email, Many Faces: A Deep Dive into Identity Confusion in Email Aliases](https://www.ndss-symposium.org/wp-content/uploads/2026-s148-paper.pdf) |
| 55.5 | 47.5 | Excluded; see full record | [The Script Tag That Isn't: Speculation Rules Injection](https://labs.trace37.com/blog/specfetch-speculation-rules-injection/) |
| 55.4 | 54.2 | Excluded; see full record | [Vault Raider: Stealthy UI-based Attacks Against Password Managers in Desktop Environments](https://www.ndss-symposium.org/wp-content/uploads/2026-s1067-paper.pdf) |
| 58.0 | 58.0 | Retained | [This Message Was Sent by Microsoft: Turning Microsoft Apps into our Phishing Platform](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Keanu%20Nys%20-%20This%20Message%20Was%20Sent%20by%20Microsoft%20Turning%20Microsoft%20Apps%20into%20our%20Phishing%20Platform%20-%20DEF%20CON%2034%20Red%20Byte%20Messag.pdf) |

The rounds below preserve their historical decisions and counts; this current reconciliation and the regenerated index supersede their display outcomes.

## Re-check round

Several Watchlist items were confirmed to exist but had no published artifact when first
collected. Searching for them again by title turned up three that had since been published,
and each was judged on the new material:

| Score | Entry | Outcome |
|---:|---|---|
| 70.0 | Write Once, Shell Everywhere (Ethiack, published 2026-08-07) | **Added.** Clears the bar on the errno-as-path-oracle methodology and two new file-write destinations; the catalogue around them is coverage. |
| 66.5 | AutoFail (TU Wien, code artifact released 2026-07-22) | Not added. The USENIX paper is still embargoed, so the argument and related-work positioning could not be read; **re-judge after 2026-08-12**, when it may well clear. |
| 48.7 | PleaseFix (Zenity Labs, published 2026-08-05) | Not added. The umbrella scores *below* its own constituent posts, which were already judged at 59.1 and 59.2 — aggregating them plus a class name adds little, and the name itself relabels indirect prompt injection. |

Two Watchlist entries turned out not to belong there at all, and were dropped rather than
deferred: **Remote Server, Local Root. Welcome to MCP.** is 2025 work (its primary artifact
is a September 2025 blog post and all five CVEs are 2025-numbered; Black Hat Asia 2026 was a
later presentation of it), and **Writing to Shadow Stacks** is Linux kernel and CPU
mitigation research — `/proc/self/mem` with `FOLL_FORCE`, `userfaultfd` on the shadow-stack
VMA, and the `WRSSQ` instruction — with no web, HTTP or browser bearing.

## Second re-check round (8 August 2026)

During the Black Hat USA / DEF CON 34 week the `bh_files` arrays and the media server filled
in with decks that had been empty at first collection. A focused sweep — the Black Hat US-26
and Asia-26 schedule JSON, the DEF CON 34 media server, the four DEF CON villages, and the
week's researcher blogs — surfaced twelve un-judged artifacts (everything the sweep found had
either already been judged in the initial round, e.g. CRLF-Powered Desync at 67.5 and Cast
Attack at 64.2, or was one of these twelve). Each was read in full and judged. Under the
≥ 60 keep-cut, **four** are kept (Cache Me, One Char, CoreBreak, ChatMate); the rest fall
below 60 or are prior-year:

| Score | Entry | Outcome |
|---:|---|---|
| 76.8 | RebirthDay Attack (Nankai / Tsinghua, Black Hat Asia 2026) | **Not added — prior year.** Genuinely strong, but the disclosure is ACM CCS 2025 (Oct 2025, ~50 CVEs, IETF fix draft); the deck states "Based on ACM CCS Research." Belongs to 2025 and is **not** in `2025.md` — flagged to the maintainer for the 2025 missed-nominee review path. |
| 75.6 | Cache Me, Catch You (Wu et al., Black Hat Asia 2026 / NDSS 2026) | **Added.** Establishes the LLM inference cache layer (prefix-KV, semantic, multimodal) as a distinct attack surface; the prefix-cache non-crypto-hash KV collision and multimodal image-byte collision are primitives absent from concurrent semantic-only work. |
| 73.8 | One Char to Rule Them All / SHAR (Tsinghua, Black Hat Asia 2026 / S&P 2026) | **Added.** First exhaustive measurement of special-character handling across 31 DNS implementations, isolating a silent-drop primitive that widens the spoofing window; in-scope via DNS cache-poisoning's web-trust impact. Downstream impacts partly re-derive Disablance (CCS 2023). |
| 70.0 | The CoreBreak Attack (Ingber & Ivgi, Black Hat USA 2026) | **Added — borderline.** Direct tool invocation: the agent-SDK harness (Strands, Google ADK, Vercel AI SDK) runs a tool-call block with no model turn in between, so the infra never verifies a model authorized it — the antithesis of prompt injection, validated by AWS+Google CVEs. Held to exactly 70 by prior art: the IMDS-theft half is by-design, and Anthropic's Mythos "Project Glasswing" had flagged the Vercel direct-invocation instance. Medium confidence. |
| 67.5 | ChatMate (Rubrik Zero Labs, Black Hat USA 2026) | **Added** (≥ 60). First escape of a *managed* AI-assistant sandbox (Copilot → root on the host node) is a real 0-day, but every primitive is a classic container-escape building block and "Remote Prompt Execution" is impact framing, not a new mechanism — so it lands in the 60–69.9 supporting band, not the ≥ 70 core tier. |
| 58.3 | Breaking Multi-Tenancy Over and Over (ERNW, Black Hat USA 2026) | Not added. Overlaps the already-judged Istio namespace item (59.0); the marginal material is useful systematization of over-permissive-RBAC / trusted-reference config, no new primitive. |
| 52.6 | Handle With Care: Azure Automation cross-tenant (Microsoft, Black Hat USA 2026) | Not added — and prior year. CVE-2025-29827, patched server-side 8 May 2025; substring path-check pollution + case-sensitivity router differential on one cloud target. |
| 52.0 | Pre-auth RCE in Enterprise Java (Novee, Black Hat USA 2026) | Not added. Clean Bonita / OFBiz chains, but every primitive is prior art (Orange Tsai `..;` normalization 2018, FoxGloveSecurity XStream/CommonsCollections 2015). |
| 51.6 | Bad Vibes — Pwning Coding Agents 70 Times (CyberArk, Black Hat Asia 2026) | Not added. 81+ findings / 18 CVEs across ~20 coding agents, but breadth of known classes (allowlist bypass, path-equivalence, symlink TOCTOU) is coverage, not discovery. |
| 44.6 | LLM Heist: Hijacking LiteLLM (Rehberger, 2026-08-03) | Not added. Presupposes the attacker already holds the master key; the "routing config is a MITM primitive" residue is a consequence of admin control, below the already-judged LiteLLM auth-bypass/RCE items (55.5, 53.0). |
| 34.5 | The Stream Is Dead (MadeYouReset, DEF CON 34) | Not added — prior year. CVE-2025-8671, fully disclosed August 2025; the 2026 deck re-presents it. Already in `2025.md`. |
| 79.0 | Discovering React2Shell (Carapace, Black Hat Asia 2026) | Not added — prior year. CVE-2025-55182, disclosed 3 December 2025; strong on merits but 2025, and already in `2025.md`. |

The four DEF CON 34 village decks still on the Watchlist (Cache Key Injection, This Message
Was Sent by Microsoft, New Hope for SSRF, ROP for the Web) were re-checked the same day and
still have no primary artifact published.

## Third re-check round — single-publisher sweep (10 August 2026)

A sweep of one publisher rather than one venue: every post on `blog.voorivex.team`, taken
from its sitemap so pagination could not hide any, checked against the year lists and this
folder. Twenty-eight posts exist; two are already in [`2024.md`](../../2024.md) and one
(Content-Type Override, 50.0) was judged in the initial round, leaving **ten** in the 2026
window. Each was read in full and judged; **two** clear the ≥ 60 keep-cut. The six posts
from 2023–2025 went to their own years' folders.

| Score | Entry | Outcome |
|---:|---|---|
| 71.2 | We Need to Talk About CSRF Again | **Added.** Chromium safelists a fourth content type the Fetch standard does not list, so a cross-origin POST carrying it took no preflight — defeating the content-type-check family of CSRF defences generally, then amplified into a GraphQL-APQ XS-Leak. Since patched. Medium confidence on first discovery: no earlier public source found, which is not proof. |
| 66.3 | JavaScript Functions Overload Confusion | **Added** (≥ 60). The census is the contribution — 2,228 Blink IDL files walked to find which type-resolved overloads reach a sink, landing on ~30 sinks, 4 security-decision forks and ~22 Trusted Types sinks that fork on type. The underlying array/structured-clone primitive is community-known and the challenge was joaxcar's; scored down for an LLM-assisted enumeration with no published artifact. |
| 59.3 | The Usual Suspect: Type Confusion in Twelve Bytes | Not added — just under. The reusable half is that `file-type` never validates the ISO-BMFF box-size field, so a sniffer keyed on a suffix of the header hands over free bytes *before* the magic. Polyglot uploads and comment-wrapped headers are old. |
| 57.7 | Three 0-Day Vulnerabilities in Adminer | Not added. Real pre-auth RCE and a CSP-nonce-signed XSS from a rogue MySQL version banner, but ODBC `TraceFile` writes, `VACUUM INTO` file writes and rogue-DB-server attacks are all established. |
| 55.3 | Shaking the MCP Tree | Not added. Early field survey of open Dynamic Client Registration on MCP servers; the author states the techniques are not new, and 2026 already carries MCP entries that go further into mechanism. |
| 54.9 | When Two Parsers Disagree | Not added. A neat 20-line reproducible `qs`-versus-`URLSearchParams` challenge, but parser differentials run from HPP (2009) through the syntax-confusion entry already in `2025.md`. |
| 52.1 | uXSS on Samsung Browser (CVE-2025-58485) | Not added. Guarded launcher activity beside an unguarded exported sibling that accepts `javascript:` — a long-standing Android browser class. Judged as 2026: first public disclosure Feb 2026, though reported Sept 2025. |
| 50.1 | Story of Abusing a Fully Secured redirect_uri | Not added. Clean worked example of decode-count asymmetry (`%2523%40`) past strict validation; the primitive is foundational URL-confusion material. |
| 44.5 | My First RCE by Reverse Engineering an EXE With AI | Not added. Cross-site WebSocket hijacking of an unauthenticated localhost service; the author cites Ormandy's 2018 Electrum finding as the same shape. |
| 42.0 | Two cPanel Zero Day Vulnerabilities | Not added. `json.dumps()` not escaping `/` so `</script>` breaks out, plus one unescaped `From:` header — textbook XSS on a widely deployed product. |

## Fourth re-check round — the 8–14 August window (14 August 2026)

The window the initial collection stopped short of: the last two days of DEF CON 34, and the
opening of USENIX Security '26 on 12 August. Twelve candidates were judged, sourced from a
weekly research scan and checked first against `2026-ai.md` and this folder — three of the
scan's items (H3Act at 54.2, ROP for the Web at 22.5, HTTP Terminator at 74.2) were **already
judged** and are not re-judged here. Under the ≥ 60 keep-cut, **two** are kept:

| Score | Entry | Outcome |
|---:|---|---|
| 71.1 | The State of Passkeys (RUB / Heilbronn / Wuppertal, USENIX Security '26) | **Added.** The first RP-side passkey evaluation at scale under a plain web-attacker model — 15 attack types and 28 detection methods against 103 live sites, all 103 failing something — carried by a released tool that emulates client *and* authenticator. Credential Overwrite (attacker's public key registered under the victim's public credential ID) is the one genuinely new attack type; most of the rest systematise checks WebAuthn already mandates, which is what holds it to 61 on originality. |
| 64.7 | When HTTP 402 Meets the Blockchain / x402 (Zhejiang / EPFL, USENIX Security '26) | **Added.** Eight checkable rules over the x402 facilitator, of which the durable one is that *verified* and *paid* are different facts; the sponsored-settlement Gas Abuse class has no analogue in earlier payment-logic work. Scored down because [Five Attacks on x402](https://arxiv.org/abs/2605.11781) published overlapping authorization and replay attacks on 12 May 2026 and is not cited, and because the method descends directly from How to Shop for Free Online (S&P 2011, in the archive). |
| 59.1 | VulGenie (Fudan / EPFL, USENIX Security '26) | Not added — just under, and judged without the full text. Patch denoising via a modification-behaviour dependency graph is a real increment over SEADER-style diff mining; web bearing is indirect. |
| 53.0 | Salesforce Apex Predator (Reco, DEF CON 34 workshop) | Not added. The LWR/GraphQL surface and Apex-from-LWC-bundle enumeration are genuine increments with labs and the LWRed tool behind them, but the Aura half is Aaron Costello's 2020 work and everything sits on one SaaS product. |
| 52.5 | PANGOLIN (USENIX Security '26) | Not added. Cross-language dispatch analysis is the new part; recovering hidden IoT web interfaces from the router rather than the frontend is EAGLEYE (NDSS 2025). |
| 39.8 | Zero-click RCE in Uptrain (GitHub Security Lab) | Not added. Default API key + credentialed CORS + `eval()` — the composition is the lesson, every element is textbook. Reported September 2024, published 8 August 2026. |
| 37.0 | Slop Spotting (Paxton-Fear & vonBlankenburg) | Not added — insufficient evidence. Sensible triage gate (AI claim → SAST rule → does the pattern exist), nothing published. |
| 36.5 | New Hope for SSRF (Cloud Village) | Not added — insufficient evidence. Delivered 8 August, still no deck; **stays on the Watchlist**. |
| 32.0 | Pattern, Graph, Prompt (Airbnb) | Not added — insufficient evidence. The per-paradigm unique-find numbers are the contribution and are unpublished. |
| 31.8 | The API Made Me Do It | Not added — insufficient evidence. Well-designed A/B on secure-by-default scaffolding versus prompting; no results published. |
| 30.5 | CVE-2026-62899 .NET `HttpListener` smuggling | Not added — insufficient evidence. Vendor advisory with no public mechanism; a patch, not a technique. |
| 29.8 | Testing API Business Logic With AI Agents | Not added — insufficient evidence. "Build the ownership graph before hunting BOLA" is standing methodology; no benchmark published. |

Seven of the twelve are village or vendor material with no published artifact, which is the
shape of this window: the conference weeks generate abstracts far faster than decks. Village
decks are still not mirrored on the DEF CON media server, so those seven are placeholders to
re-judge rather than settled scores.

## Fifth re-check round — the 14–18 August window and a year-wide catch-up (18 August 2026)

Six beats were swept in parallel: researcher blogs, vendor labs and bug-bounty platforms,
academic venues, non-English research, a mechanism-led sweep, and the conference circuit.
**Five returned; the conference beat did not**, so DEF CON 34 and Black Hat deck re-checks are
carried forward unresolved and anything published there since 14 August is still missing. That
gap is recorded in the Watchlist rather than left silent.

Forty-nine candidates were judged, plus one existing entry amended. **Eighteen are kept.** The
round's character is different from the fourth: because the beats swept the whole year rather
than only the new window, most of the finds are things earlier rounds missed — *Pwning Claude
Code* published on 12 January, the Internet Explorer clickjacking chain on 5 June, zkLogin on
13 February — rather than newly published work.

| Score | Entry | Outcome |
|---:|---|---|
| 75.5 | Regular Expression Denial of Service Induced by Backreferences | **Added.** The first ReDoS theory covering backreferences, deriving super-linear runtime in exactly the regime every deployed detector certifies as safe, and turning it into an IDS *alert bypass* rather than just a slowdown. |
| 73.7 | Recovering Encrypted LLM Reasoning Traces | **Added.** Route an opaque reasoning blob to the weakest-guarded sibling model and ask it to transcribe: the strong model is never jailbroken, its guardrails are routed around. Cited to the paper, not the reproduction blog. |
| 73.2 | DNS Cache Poisoning Like it's 2006 | **Added.** RRset shuffle order and the security-critical port and transaction ID come from one non-cryptographic PRNG, so a cosmetic output becomes a client-side state-disclosure oracle needing no attacker-controlled nameserver. |
| 72.5 | BUIzz | **Added**, resolving a fourth-round Watchlist item. Drives browser-*chrome* interactions at OS level with a within-one-browser metamorphic oracle, and finds that 67.6% of the security bugs live in vendor-added interface features. |
| 71.8 | Analyzing the WebRTC Ecosystem and Breaking Authentication in DTLS-SRTP | **Added.** First systematic authentication audit of WebRTC's media plane; 19 of 33 media-server implementations fail DTLS-layer authentication. |
| 70.5 | Melting the Flesh of PHP's Memory Hardening | **Added.** A write primitive using only built-in objects that never touches freelist pointers, plus a shadow key a respawned worker inherits before re-seeding. |
| 68.1 | HijackKV | **Added.** Cache-*integrity* attack on position-independent KV reuse, by design rather than by hash collision, hijacking a victim who supplies no attacker text at all. |
| 68.0 | Network-Level Prompt and Trait Leakage in Local Research Agents | **Not added — out of window.** arXiv v1 is 27 August 2025 with the full attack in the abstract. 2025 work at a 2026 venue; flagged for the 2025 missed-item path. |
| 67.7 | MUZZLE | **Added.** Discovers the injection surface from the agent's own trajectory instead of guessing it, and demonstrates cross-*application* compromise using stored credentials. |
| 67.3 | Solving an ORB mystery | **Added.** A pass-through service worker rewrites a request's destination, selecting the branch where Opaque Response Blocking returns a blank response instead of an error, restoring the status oracle ORB exists to close. |
| 66.5 | zkLogin: when ZKP is not enough | **Added.** A ZK proof attests to the circuit's parsing of a document, not its meaning, so a parser differential is laundered rather than eliminated. |
| 64.8 | DOMPurify bypass via SMIL animateTransform on Safari | **Added.** WebKit checks only that an animated attribute is animatable, and an unknown transform type suppresses the function prefix — turning a transform animator into a generic attribute writer under the default config. |
| 64.5 | Pwning Claude Code in 8 Different Ways | **Added.** Eight allowlist escapes whose common core is a parse differential between the gate and the executed program — git's abbreviated long options and an xargs flag-arity mismatch are the sharpest. |
| 63.4 | The Click that shouldn't have worked | **Added.** Mark-of-the-Web is origin-dependent on the download path, and an embedded shell folder view is a clickjack target with execution semantics. The linchpin bug was patched in 2024, so the durable parts are the provenance and ordering insights. |
| 63.2 | Overcoming the Retrieval Barrier | **Added.** Shows that unoptimised injected text is essentially never retrieved under natural queries, which reframes what prior indirect-injection evaluations were measuring. |
| 61.8 | The Masks We (Think We) Wear | **Added.** Wallet extensions inject their provider into cross-origin iframes, so an ordinary third-party tracker reads the address with no dApp and no interaction. |
| 61.1 | Site Isolation is Dead | **Added, marginally** (+1.1). The IPC channel authenticates by message shape, so a renderer compromise inherits delegated agent authority — but the attacker needs a renderer 0-day to reach what a plain prompt-injecting page largely achieves for free. |
| 60.9 | LeakyLinks | **Added.** The new knowledge is not that URL scanners leak but that the leak is actively consumed — canary tokens fired, including from a URL encoded only in a QR image. |
| 60.5 | Semantic Cache Poisoning | **Added, marginally.** A hit is served without inference, so prompt-level defences are bypassed by construction; confirmed on three production cloud gateways. |
| 59.6 | TranSPArent | Not added — 0.4 under. Derives framework taint sinks instead of enumerating them; false-discovery rate is barely better than the stock tool. |
| 59.4 | Breaking and Fixing Third-Party Online Payments | Not added — 0.6 under, deliberately not rounded up. The design-level invariant is real; the empirical half rests on a known mobile IPC weakness. |
| 57.2 | XSS2Shell | Not added. The `strip_tags`-versus-KSES resurrection is a genuine new primitive; the entire exploitation half is the same site's own 2022 work, already in this archive and cited by `2022.md`. |

Below 57 the round produced a long tail of competent applications of known classes; all are in
the index. Four are worth calling out because of *why* they failed rather than how far.

**A single-publisher cluster, verified before judging.** Five candidates came from
`labs.trace37.com`, which openly runs an AI-assisted hunting platform. Given the standing
caution about a source where eight of eight candidates once turned out to be reproductions, the
cluster was put through a dedicated verification pass against independent records before any of
it was scored. The result is mixed and worth recording precisely: the publisher is real — two
findings landed genuine upstream commits, and the DOMPurify prototype-pollution advisory is
credited to them by name in the 3.4.0 release notes — but every one of the five failed the
keep-cut, and the failures share a shape. The JSON escaped-solidus post (24.7) rediscovers a
2018 technique whose closest relative is **already in this archive and already cited on
`2023.md`**, with no prior-art section at all. The email CSS census (54.6) rests on one
verifiable claim, and upstream credits that fix to a different reporter. The speculation-rules
post (55.5) has no independent record of any kind, and two apparent corroborations found while
searching turned out to be the publisher's own text quoted back. The DOMPurify post (52.4) is
real and correctly credited, but its flagship version history does not survive checking — the
vulnerable idiom is present from 2.5.0 onward, so the advertised affected range understates it
by the whole still-deployed 2.5.x line. **Standing rule for this source: cite it only where an
independent artefact exists, and never on its own authority.**

**Two candidates resolved to URLs already inside judged entries** — the Brave indirect-prompt-
injection post is the companion of *Attacking and Defending AI Browsers* (51.6), and the
Nextcloud Mail sanitizer reports are the entry already scored at 43.0. The latter was
**amended rather than duplicated**: its three sibling reports and the author's own two blog
posts are now cited on it, which also makes its long-standing title claim accurate and records
that the real first publication was February and March 2026, not the April platform disclosure.

**Two corrections to the existing record** came out of prior-art checking. `Cache Me, Catch You`
(75.6) is described here as a confidentiality result; it also contains explicit system-integrity
poisoning attacks including a block-collision cache hijack, which is why HijackKV's originality
was scored down. And the index was missing its row for the Ruby 4.0 gadget chain, which has been
in `2026-ai.md` since the initial collection.

## Sixth re-check round — missed-item sweep through 9 September 2026

This bounded refresh searched the 2026 window with emphasis on **18 August–9 September**,
and revisited older missed papers, talks and pending artifacts. **Eight new grouped
candidates received complete, reverified scorecards; six clear the ≥60 display cut.**
Unscored screens and unresolved leads below are separate from those eight. Full reasoning,
prior art and evidence limits are in [judgements.md](judgements.md).

| Score | Candidate | Outcome |
|---:|---|---|
| 70.1 | [What's in a tag name? JavaScript, apparently](https://portswigger.net/research/whats-in-a-tag-name-javascript-apparently) — Gareth Heyes | **Added**, core combination after rubric rejudgement. August 25. Tag-name retrieval and transformation provide a reusable payload-source technique; retained executable handlers remain necessary, and universal browser/WAF success is not established. |
| 67.8 | [Out of Bounds, Out of Sandbox: RCE in Go JavaScript Engine](https://www.slcyber.io/research/out-of-bounds-out-of-sandbox-rce-goja) — Dylan Pindur and Adam Kues | **Added**, supporting adaptation. September 7 article; June technical fix/PoC timing is recorded separately in the card. Reuses native heap/Go-runtime exploitation through an embedded JavaScript boundary. |
| 66.5 | [What's in Your Agent's Context?](https://arxiv.org/abs/2609.01222) — Zichuan Li et al.; [project](https://zichuan.li/LLMAgentCPE/) | **Added**, supporting methodology. September 1 v1. CoRA operationalizes context-source discovery and role/scope propagation testing; the August 27 *When Context Gets Root* paper narrows its originality. |
| 65.4 | [Chat-template backdoors: systematic evaluation and agentic impact](https://arxiv.org/abs/2602.04653), grouped with [BadTemplate](https://arxiv.org/abs/2602.05401) | **Added**, supporting methodology. February 4–5 papers extend the [July 9, 2025 original disclosure](https://www.pillar.security/blog/llm-backdoors-at-the-inference-level-the-threat-of-poisoned-templates); they do not establish a 2026 first discovery. May 24 agent results are later evidence. The inspected public repository did not expose the claimed agent artifact paths. |
| 64.4 | [Hacking AI customer service agents / Hacking Human-in-the-Loop Systems](https://www.intigriti.com/researchers/blog/hacking-tools/hacking-ai-customer-service-agents) — Inti De Ceukelaire; [slides](https://drive.google.com/file/d/1e7deupIiaOVN_DPPz4YAs68wRi0QpqUC/view) | **Added**, supporting combination. August 7 talk is the cutoff; companion article displays September 2 while its CMS publication is September 3. Victim-signed email delivery composes with action-taking support agents and review workflows. |
| 62.2 | [A Formal Analysis of Agent Payment Protocols](https://arxiv.org/abs/2609.00060) | **Added**, supporting methodology. Formalizes payment authorization invariants and protocol failure cases; full evaluation is preserved in the scorecard. |
| 58.0 | [This Message Was Sent by Microsoft](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Keanu%20Nys%20-%20This%20Message%20Was%20Sent%20by%20Microsoft%20Turning%20Microsoft%20Apps%20into%20our%20Phishing%20Platform%20-%20DEF%20CON%2034%20Red%20Byte%20Messag.pdf) — Keanu Nys | **Below cut.** August 9 talk, deck generated August 13 and available at this recheck. Resolves the missing-artifact watchlist item; useful recipient/card combinations build on established trusted-service phishing. |
| 54.2 | [Drive-By Agent Hijacking](https://www.cyera.com/research/nemoclaw-one-website-visit-to-hijack-your-ai-agent) — Elad Luz and Ofek Itach | **Below cut.** August 25. DNS rebinding reaches Ollama management and persistent template rewriting, with substantial earlier art for both components. |

The same-day rubric audit deliberately rejudged Heyes **56.0 → 70.1** and Nys
**57.0 → 58.0**, preserving both earlier cards in append-only history. Heyes's change
separates old DOM components from the age of their security use and credits a reusable
research construction without demanding a deployed WAF bypass or immediate adoption.
It does not assert newly verified browser/WAF results. These are two rejudgement events,
not two additional candidates; the round remains eight new cards, six retained and two below cut.

### Pending technical leads — no inclusion decision

| Date | Lead | Evidence and next step |
|---|---|---|
| August 26 | [Breaking Claude Code Opus 5 Auto Mode](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/) | Full original read. HTTP 415 and a ZIP lead the agent to replace a rejected supplied decoder with its own code, which imports attacker `struct.py`. Judge the fallback-workflow contribution against established Python module shadowing. |
| August 27 | [When Context Gets Root: Privilege Escalation in LLM Harnesses](https://arxiv.org/abs/2608.27299) | Primary mechanism/threat-model sections read and used as CPE prior art; not fully judged. Delegation can relabel tool-derived content as user instructions, including for permission review; persistent/custom-agent paths also require assessment. |
| September 3 | [HookPry](https://arxiv.org/abs/2609.03884) | Abstract lead only; acquire full original, establish mechanism and prior art before judging. |
| September 5 | [HAE-GEO](https://arxiv.org/abs/2609.06027) | Abstract lead only; no claim that it meets the web-technique or novelty threshold. |
| August 25 | [WebMCP-Phalanx](https://arxiv.org/abs/2608.24017) | Abstract lead only; full technical comparison remains pending. |
| August 6 | [MCP-2026-008: public cacheScope](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/3207) | Original issue read. Claimed cross-user cache poisoning does not yet establish the server/cache-key identity confusion; inspect linked PoC before accepting the boundary claim. |
| July 27 / August 12 | [JFrog advisory index](https://docs.jfrog.com/releases/docs/jfrog-security-advisories), [CVE-2026-65922 record](https://github.com/advisories/ghsa-cqxf-f7w8-7gff) | Artifactory metadata/cache-poisoning advisory leads; detailed Oligo original attributed in later coverage was not located. Do not conflate 65922 with 69105/69106 or the older 2024-6915. |
| August 31 | [Xianzhi 92754 — FreeMarker/Aviator sandbox bridge](https://xz.aliyun.com/news/92754) | Abstract only; original body blocked. Explicit extension of 2023 work, CVE-2026-51086/51087; judge the added bridge after obtaining full text. |
| August 19 | [Xianzhi 92692 — CFITSIO EFS filename attack surface](https://xz.aliyun.com/news/92692) | Abstract only; body blocked. Filename-driven I/O, validation ordering and copy/SSRF/exfiltration composition may overlap the already-scored CFITSIO work. |
| August 26 | [Xianzhi 92743 — Agentic RAG in-band smuggling](https://xz.aliyun.com/news/92743) | Abstract only; retrieval-to-tool chain appears related to known injection, but unavailable body prevents a negative judgement. |
| August 20 | [Xianzhi 92724 — FastGPT 4.14.8 Python sandbox escape](https://xz.aliyun.com/news/92724) | Abstract only; frame/global introspection appears familiar, full source needed. |
| September 9 | [Xianzhi 92789 — JimuReport 2.5.1 signing key/Aviator chain](https://xz.aliyun.com/news/92789) | Abstract labels reproduction/analysis; full body unavailable. |
| August 17 | [Xianzhi 92715 — JDBC/MySQL file-descriptor path](https://xz.aliyun.com/news/92715) | Abstract-only possible earlier gap just before the incremental window; claimed route avoids outbound network. |

### Screens without numeric judgements

These are triage outcomes, not completed scorecards or proof that a source contains no
useful research. Full-read and index-only evidence are distinguished explicitly.

| Source | Screen and evidence level |
|---|---|
| [Valid, But Never Issued: Session Spoofing and SSRF in Grafana MCP](https://www.pillar.security/blog/valid-but-never-issued-session-spoofing-and-ssrf-in-grafana-mcp), September 2 | Full original read. Format-valid session IDs accepted without authentication plus caller-selected SSRF destination/method/headers; no distinct mechanism established beyond the case study. Canary metadata is not proof of theft from real IMDS. |
| [PostGREShell](https://www.cyera.com/research/postgreshell-the-database-powering-much-of-the-internet-had-an-open-door-for-12-years), September 1 | Full original read. Replication-slot plugin path bypasses SQL LOAD restrictions; source identifies plugin-loading precedents. Article date must not replace the earlier advisory/release timeline without checking. |
| [ASCII smuggling crosses over from AI prompt injection to phishing evasion](https://www.microsoft.com/en-us/security/blog/2026/09/03/ascii-smuggling-crosses-over-from-ai-prompt-injection-to-phishing-evasion/), September 3 | Index/search-level screen: telemetry application of established Unicode obfuscation, no new technique established. |
| [Loom Chrome extension silent webcam activation](https://bugcrowd.com/disclosures/6c751112-6cd1-4a9a-90f1-d502c164ea94/unauthorized-silent-webcam-activation-via-loom-chrome-extension-web-accessible-resources), disclosed September 3 | Full primary report read. Framing a web-accessible extension resource reuses an existing camera grant; same-origin policy prevents the parent from reading pixels. Familiar privileged-resource confused-deputy class; extra capture chains are conjecture. |
| [Silent patches](https://www.yeswehack.com/lab/cve-2023-54391-silent-patches), September 9 | Full original read. Proxmox patch-attribution/CVE-lag retrospective; no sufficiently distinct attack contribution established. This is a 2026 article despite its CVE year. |
| [YesWeHack LLM series: Codex](https://www.yeswehack.com/learn-bug-bounty/llm-series-codex), September 3 | Educational lab walkthrough with earlier WordPress research; no new original technique established. |

### Conference artifacts and remaining watchlist

The [DEF CON 34 presentation directory](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/)
was fully enumerated and six newly or previously unrecorded decks were downloaded and
triaged. Its working path has one `DEF CON 34 presentations` directory; the previously
used double nesting is obsolete. These additional full decks did not produce new scores:

- [Taming the Swarm](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Albert%20Corzo%20-%20Taming%20the%20Swarm%20Hard%20Architectural%20Lessons%20from%20Building%20a%20Deterministic%20Agentic%20Web%20Pentesting%20System%20-%20v1.pdf): 131-slide BugTraceAI retrospective: architecture and deterministic validation, but no distinct exploit or convincing new benchmark contribution established.
- [Your OTP Never Arrived](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Kyprianos%20Vasilopoulos%2C%20Nikos%20Vourdas%20-%20Your%20OTP%20Never%20Arrived%20Attacking%20the%20Trust%20Boundary%20Where%20SMS%20Meets%20the%20Internet%20-%20v1.pdf): 65-slide Kannel field study: NUL/log parsing differences, message-ID mismatch, backoff reset and familiar injection classes. Exact first-disclosure date remains unverified.
- [1.1 Million Cameras, One Wildcard](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Sammy%20Azdoufal%20-%201.1%20Million%20Cameras%2C%20One%20Wildcard%20Architectural%20Surveillance%20in%20an%20IoT%20Cloud%20-%20nobody%20puts%20baby.pdf): 69-slide IoT-cloud chain: MQTT ACL absence, exposed secrets and ordinary API authorization failures.
- [No Prompt Required](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Elad%20Meged%20-%20No%20Prompt%20Required%20Pre-Task%20RCE%20in%20Google%20Gemini%20CLI%20-%20RCEin.pdf): Additional artifact for the already-scored Novee 52.5 group: Gemini pre-task shell injection and CI trust handling; no new judgement.
- [The Sandbox Is a Suggestion](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Elad%20Meged%20-%20The%20Sandbox%20is%20a%20Suggestion%20Deconstructing%20AI%20Agent%20Sandboxes%20-%20ASuggestion%20AIA.pdf): Additional artifact for the existing Novee group: permission precedence, exfiltration, environment reads, Landlock and symlink cases; no deliberate rejudgement.

Five existing citation moves were verified as HTTP 200 PDF responses and repaired in this refresh; these are link repairs, not new candidates:

- [Get Set, Exploit: Python Class Pollution](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Gavin%20Zhong%2C%20Zhengyu%20Liu%2C%20Jianjia%20Yu%20-%20Get%20Set%2C%20Exploit%20Unveiling%20Python%20Class%20Pollution%20In-the-Wild%20-%20P.pdf): Removed duplicate directory nesting.
- [One Chain to Own Them All](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Ji%27an%20Zhou%2C%20Lei%20Lu%20-%20One%20Chain%20to%20Own%20Them%20All%20-%20Breaking%20AI%20Infrastructures%20-%20azraelxuemo%20v3.pdf): Removed duplicate directory nesting.
- [Your WAF Blocked Us, That Was the Exploit](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Barak%20Sternberg%2C%20Nevo%20Poran%2C%20Ron%20Bobrov%20-%20Your%20WAF%20Blocked%20Us%2C%20That%20Was%20The%20Exploit%20-%20Remote%20Agent%20Takeover%20via%20Cloudflare%2C%20Sentry%20and%20C.pdf): Removed duplicate directory nesting.
- [Hacking Your Life with AI Can Get You Hacked](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Peyton%20Kennedy%20-%20Hacking%20Your%20Life%20with%20AI%20Can%20Get%20You%20Hacked%20How%20AI%20Orchestration%20Platforms%20Ship%20RCE%20by%20Design%20-%20V1.pdf): Removed duplicate directory nesting.
- [LGTM: Bypassing an LLM Build Gate](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Aviv%20Donenfeld%20-%20LGTM%20Bypassing%20an%20LLM%20Build%20Gate%20When%20Prompt%20Injection%20Fails.pdf): Removed duplicate directory nesting and replaced the retired v2 filename with the current unversioned PDF.

Still unresolved: [Cache Key Injection](https://www.bugbountydefcon.com/agenda-2026)
remains agenda/abstract-only after the presentations page returned 404 and the researcher's
blog exposed no new artifact; [ROP for the Web](https://appsecvillage.com/events/dc-2026/rop-for-the-web-smuggling-xss-sqli-and-web-shells-past-every-waf-using-compression-dictionaries-1250560)
still has no verified full deck or gadget-scanner publication; [New Hope for SSRF](https://www.cloud-village.org/dc34)
still has only an abstract. Nys's Microsoft talk is resolved above. Four AI-assessment village
items remain incompletely rechecked: [A Billion-User Blast Radius](https://appsecvillage.com/events/dc-2026/a-billion-user-blast-radius-owning-chatgpt-s-secure-sandbox-1248604),
[Pattern, Graph, Prompt](https://appsecvillage.com/events/dc-2026/pattern-graph-prompt-what-happens-when-you-layer-three-analysis-paradigms-on-the-same-codebase-1223399),
[The API Made Me Do It](https://appsecvillage.com/events/dc-2026/the-api-made-me-do-it-do-bad-apis-lead-ai-to-generate-vulnerable-code-1248780),
and [Testing API Business Logic With AI Agents](https://www.bugbountydefcon.com/agenda-2026).

Black Hat USA/Asia schedule JSON returned 403, and the rendered schedule exposed a JavaScript
shell rather than a reliable session listing. Artifact fields for *Lost in Normalization*
and *PleaseFix* could not be reverified; this is not evidence that no artifacts exist.
Spotit's blog also returned 403. No completeness claim is
made for other conferences.

### Coverage and gaps at 9 September

- **Researcher blogs and mechanisms:** Original indexes/feeds fetched for Searchlight,
  watchTowr, CTBB, Doyensec, Trail of Bits, Slonser, Arkark, Mizu, Embrace the Red, Cyera,
  Include Security, Flomb, W4ke, Lyra and Zhero. PortSwigger's full RSS had six 2026 items:
  four research posts and two 2025 competition posts; Heyes was the only new technical
  article since August 18. Mechanism searches covered desync, parser differentials,
  caching/CDNs, OAuth/SAML, CSP/Trusted Types, MCP/AI, Go sandboxing and local services.
  Generic date-qualified searches were noisy. This was not a deep refresh of every
  source-map publisher: identity specialists, Quarkslab, Synacktiv, Guardio, Zenity,
  Datadog, PT SWARM and browser vendors remain under-covered. Doyensec's CFITSIO/ELBaph
  cases already have below-cut judgements; Include Security's August 31 storage guidance
  and August 10 AI-pentesting material were educational screens rather than new techniques.
- **Academic:** Fetched the full [August cs.CR index](https://arxiv.org/list/cs.CR/2026-08)
  and September 2–9 cs.CR index entries, plus [IEEE S&P 2026's accepted-paper list](https://sp2026.ieee-security.org/accepted-papers.html).
  [USENIX Security 2026](https://www.usenix.org/conference/usenixsecurity26/technical-sessions)
  returned 403. Selected originals were read for the completed cards and prior-art checks;
  this does not constitute a complete academic-venue or all-category arXiv sweep.
- **Non-English:** Xianzhi list API pages 1–3 yielded 45 titles/abstracts spanning August
  16–September 9. HTML and article-detail API bodies still hit the JavaScript challenge;
  those abstracts do not close the earlier 675-item full-text gap. Flatt's Japanese and
  Arkark's indexes, Theori's Korean index, Hackyboiz, leavesongs and Tencent XLab were
  checked; tutorials, recaps, already-scored items or non-web kernel research predominated.
  Habr infosecurity API pages 1–3 were fetched, but only part of the title inventory was
  screened and bodies were not systematically read. Russian coverage is partial.
  Weixin enumeration and Butian access remain unresolved.
- **Disclosures and CTFs:** Bugcrowd's first public Crowdstream JSON page enumerated 20
  disclosures from July 31 through September 9, covering the incremental date range.
  Except Loom, these were title/index screens, not complete technical assessments; the
  URLs are retained below for follow-up. Fresh HackerOne Hacktivity enumeration was not
  completed; the previous January/February gap remains. Google Bug Hunters' report index
  returned an error. Intigriti's August 20 fuzzing tutorial and earlier DOM-clobber/CSP
  and postMessage CTF cases were educational screens. A September 6 third-party BlackHat
  MEA *Lumen* writeup suggested PHP `max_input_vars` header-dropping/filter splitting, but
  the original author/challenge artifact was not verified; it remains an unendorsed
  source-discovery lead. Existing L3ak/Sekai cases were already rejected in history.
- **Fetch limits:** `blog.calif.io/feed` and `adnanthekhan.com/index.xml` returned 403;
  guessed elttam Atom and Boost feed URLs returned 404, leaving those sources under-covered.
  Direct HTTP retrieval recovered CTBB XML after the web reader rejected it. `kibty.town`
  returned an expired-domain sale page: a live-source availability observation, not a
  finding of a faulty archived capture. No absent source is treated as a negative novelty result.

### Bugcrowd index-only follow-up inventory

The titles below are disclosure-platform labels, not independently verified impact claims.
Loom has the full-read screen above; all other reports remain index-level triage.

- 9 Sep 2026: [Unauthenticated Access to Internal Files via Direct Object Reference (UUID-based) Leading to Sensitive Data Exposure](https://bugcrowd.com/disclosures/085b5b66-83fb-4580-beb2-5b592c260418/unauthenticated-access-to-internal-files-via-direct-object-reference-uuid-based-leading-to-sensitive-data-exposure)
- 9 Sep 2026: [Broken Link Hijacking (Impersonation) on ntrs.nasa.gov via abandoned Facebook URL](https://bugcrowd.com/disclosures/cd65bae3-c385-4964-af8f-a902da35051b/broken-link-hijacking-impersonation-on-ntrs-nasa-gov-via-abandoned-facebook-url)
- 3 Sep 2026: [Unauthorized Silent Webcam Activation via Loom Chrome Extension Web Accessible Resources](https://bugcrowd.com/disclosures/6c751112-6cd1-4a9a-90f1-d502c164ea94/unauthorized-silent-webcam-activation-via-loom-chrome-extension-web-accessible-resources)
- 2 Sep 2026: [Command injection in Harmony trajectory-subsetter (subset.shape GeoJSON) gives any Earthdata user remote code execution (RCE) as root on harmony.earthdata.nasa.gov](https://bugcrowd.com/disclosures/31ad3b26-beae-4a91-879d-c6640cfe41dc/command-injection-in-harmony-trajectory-subsetter-subset-shape-geojson-gives-any-earthdata-user-remote-code-execution-rce-as-root-on-harmony-earthdata-nasa-gov)
- 1 Sep 2026: [Unauthenticated Create, Read, and Delete of Any User's Data + Email Relay on JPL Hurricane Watch](https://bugcrowd.com/disclosures/eb823c31-5e78-4bf9-9b2a-4c339918e879/unauthenticated-create-read-and-delete-of-any-user-s-data-email-relay-on-jpl-hurricane-watch)
- 1 Sep 2026: [Unauthenticated OS Command Injection (RCE) in NASA International Mass Loading Service CGI (massloading.smce.nasa.gov /cgi-bin/eop_series.py)](https://bugcrowd.com/disclosures/9fd428e5-c863-49d4-aea7-e91d2ba9199b/unauthenticated-os-command-injection-rce-in-nasa-international-mass-loading-service-cgi-massloading-smce-nasa-gov-cgi-bin-eop_series-py)
- 1 Sep 2026: [DOM-based cross-site scripting through the publicly exposed Cesium Sandcastle shared-code feature](https://bugcrowd.com/disclosures/6765826c-df24-47cd-afa4-c158bde0e4b6/dom-based-cross-site-scripting-through-the-publicly-exposed-cesium-sandcastle-shared-code-feature)
- 1 Sep 2026: [Publicly Accessible Administrative Configuration File Exposes Authentication Hashes and Internal Configuration](https://bugcrowd.com/disclosures/e2794469-0dec-4c81-a5ca-916a663f35c5/publicly-accessible-administrative-configuration-file-exposes-authentication-hashes-and-internal-configuration)
- 1 Sep 2026: [Impersonation via Broken Link Hijacking on NASA Earth Matters Blog Page](https://bugcrowd.com/disclosures/081a696d-d1d2-4d7d-acb7-29b313c9aa9b/impersonation-via-broken-link-hijacking-on-nasa-earth-matters-blog-page)
- 27 Aug 2026: [Unauthenticated Disclosure of Unpublished / Embargoed](https://bugcrowd.com/disclosures/c25fa845-a833-4df7-b706-ece0eab5bda0/unauthenticated-disclosure-of-unpublished-embargoed)
- 20 Aug 2026: [Unauthenticated Error-Based SQL Injection via POST Parameter Name in /api/experiment/answer/new/](https://bugcrowd.com/disclosures/2b1df6dc-0ea2-42ee-a16a-9bbfc33e151a/unauthenticated-error-based-sql-injection-via-post-parameter-name-in-api-experiment-answer-new)
- 20 Aug 2026: [Unauthenticated Remote Code Execution in NASA AMMOS AIT-GUI 2.5.0 via /tlm/query file write chained to /script/run code execution](https://bugcrowd.com/disclosures/e7ef226d-895b-4cfa-859a-59f83475ee60/unauthenticated-remote-code-execution-in-nasa-ammos-ait-gui-2-5-0-via-tlm-query-file-write-chained-to-script-run-code-execution)
- 20 Aug 2026: [Unauthenticated SSRF in NASA Trek addManifest allows internal network access from the Trek server](https://bugcrowd.com/disclosures/652ddcf8-f52a-44f5-8a72-2e4a61f7c9ce/unauthenticated-ssrf-in-nasa-trek-addmanifest-allows-internal-network-access-from-the-trek-server)
- 20 Aug 2026: [Unauthorized Access to CI/CD Infrastructure and Project Secrets via Compromised GitLab Runner Token](https://bugcrowd.com/disclosures/cc46ad29-f297-4847-abcd-9f5da5a85621/unauthorized-access-to-ci-cd-infrastructure-and-project-secrets-via-compromised-gitlab-runner-token)
- 19 Aug 2026: [URGENT: CRITICAL DATA BREACH - Cross-User PHI/PII Leakage via Prompt Injection - Non-malicious discovery](https://bugcrowd.com/disclosures/5d10a6d3-734e-401d-8871-b141de740a46/urgent-critical-data-breach-cross-user-phi-pii-leakage-via-prompt-injection-non-malicious-discovery)
- 13 Aug 2026: [Reflected XSS on itims.bia.gov](https://bugcrowd.com/disclosures/51f047c6-6cd6-4c96-b064-d74104868d2e/reflected-xss-on-itims-bia-gov)
- 13 Aug 2026: [Host Header Injection ](https://bugcrowd.com/disclosures/4abc50f7-2400-475f-b126-822b9c19cea3/host-header-injection)
- 13 Aug 2026: [Server Side Errors](https://bugcrowd.com/disclosures/e6f7bf2e-9ac3-4f40-8f54-679cb8706c4b/server-side-errors)
- 11 Aug 2026: [Unauthenticated MQTT Wildcard (board/#) Leaks All Pinboard UUIDs to Unauthorized Users](https://bugcrowd.com/disclosures/585d9b4e-c301-4b68-8e55-1e21139d97bc/unauthenticated-mqtt-wildcard-board-leaks-all-pinboard-uuids-to-unauthorized-users)
- 31 Jul 2026: [Data Integrity Risk & PII Exposure: Publicly Editable OPAG Collaboration Document (Google Sheets) via science.nasa.gov](https://bugcrowd.com/disclosures/18f49357-f70c-4f60-b2d1-e43a0dcddf2f/data-integrity-risk-pii-exposure-publicly-editable-opag-collaboration-document-google-sheets-via-science-nasa-gov)


## Confidence

Scores are one judgement, not a verdict. Where the primary source could not be read in full
— an embargoed paper, an image-only deck, a 403 — the entry was scored *Insufficient
evidence* with low confidence rather than guessed at, and says so in `judgements.md`. Those
should be revisited rather than treated as settled.

Prior-art searching also degraded partway through: the session's web-search budget ran out
and later batches fell back to fetching index pages and known sources directly. A failed
search lowers confidence in a novelty claim; it is not evidence of originality.

**Historical coverage gaps as of the fifth round (superseded where the sixth round resolves them).** The conference beat did not complete
on 18 August, so no DEF CON 34 or Black Hat deck published after 14 August has been looked at
and every conference Watchlist item is carried forward unverified. Chinese-language original
research remains the largest standing hole in this collection and has never been read in full:
`forum.butian.net` is geo-blocked from outside China, `mp.weixin.qq.com` cannot be enumerated
externally at all, and `xz.aliyun.com` article *bodies* sit behind a JavaScript challenge that
defeated scripted fetching, reader proxies and the Wayback snapshots alike — 675 of its 2026
articles were listed by title and abstract, and not one could be verified against its full text,
so none was cited. Two Chinese leads that look genuinely interesting on their abstracts, on
object-storage policy injection and on virtual-thread context crosstalk, are recorded in the
Watchlist as unverifiable rather than scored. Smaller gaps: `bughunters.google.com` has no
usable feed and went unswept, HackerOne coverage reached back only to roughly March 2026, and
several bug-bounty disclosures cited here have no researcher-authored body at all.

## Index

Current grouped records, sorted by score. Historical compact totals are retained for provenance; consult the full record for evidence quality and publication-year exclusions.

| Score | Verdict | Outcome | Reference |
|---:|---|---|---|
| 79.3 | Original technique | kept | [Time for ACKrobatics: Abusing TCP Timestamps to Improve Remote Timing Attacks](https://i.blackhat.com/BH-USA-26/Presentations/USA-26-Vanderlinden-Time-for-ACKrobatics.pdf) |
| 79.3 | Meaningful extension | kept | [Ruby 4.0 Universal RCE Deserialization Gadget Chain](https://www.elttam.com/blog/ruby-4-0-universal-rce-deserialization-gadget-chain) |
| 77.0 | Original technique | kept | [CSS: the bomb inside your inbox](https://portswigger.net/research/css-the-bomb-inside-your-inbox) [Related 1](https://i.blackhat.com/BH-USA-26/Presentations/BHUS26-Heyes-CSS-WP.pdf) [Related 2](https://i.blackhat.com/BH-USA-26/Presentations/BHUS26-Heyes-CSS-Slides.pdf) [Related 3](https://github.com/portswigger/css-the-bomb-inside-your-inbox) |
| 75.6 | Original technique | kept | [Cache Me, Catch You: Exploiting LLM Caching Layers in vLLM, GPTCache & Friends](https://i.blackhat.com/Asia-26/Presentations/BHAS26-Wu-Cache-Me-Catch-You.pdf) [Related 1](https://www.ndss-symposium.org/ndss-paper/cache-me-catch-you-cache-related-security-threats-in-llm-serving-frameworks/) [Related 2](https://github.com/XingTuLab/Cache_Me_Catch_You) |
| 75.5 | Original technique | kept | [Regular Expression Denial of Service Induced by Backreferences](https://www.usenix.org/conference/usenixsecurity26/presentation/liu-yichen) [Related 1](https://www.usenix.org/system/files/usenixsecurity26-liu-yichen.pdf) [Related 2](https://arxiv.org/abs/2602.21459) [Related 3](https://zenodo.org/records/20762298) |
| 75.2 | Meaningful extension | kept | [Transformers: Dark Side of the Type — Weaponizing the Conversion Layer](https://i.blackhat.com/BH-USA-26/Presentations/BHUS26-Mirosh-Transformers-Dark-Side-WP.pdf) [Related 1](https://i.blackhat.com/BH-USA-26/Presentations/BHUS26-Mirosh-Transformers-Dark-Side-Slides.pdf) |
| 74.5 | Meaningful extension | kept | [Get Set, Exploit! Unveiling Python Class Pollution In-the-Wild](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Gavin%20Zhong%2C%20Zhengyu%20Liu%2C%20Jianjia%20Yu%20-%20Get%20Set%2C%20Exploit%20Unveiling%20Python%20Class%20Pollution%20In-the-Wild%20-%20P.pdf) [Related 1](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Gavin%20Zhong%2C%20Zhengyu%20Liu%2C%20Jianjia%20Yu%20-%20Get%20Set%2C%20Exploit%20Unveiling%20Python%20Class%20Pollution%20In-the-Wild%20-%20P.pdf) |
| 74.2 | Original technique | kept | [Can AI do novel security research? Meet the HTTP Terminator](https://portswigger.net/research/can-ai-do-novel-security-research) [Related 1](https://portswigger.net/kb/papers/gkaicuremal/http-terminator.pdf) [Related 2](https://github.com/portswigger/http-terminator) |
| 74.0 | Original technique | kept | [No Tools Required: Post-Injection Exploitation Across AI Agent Frameworks](https://i.blackhat.com/BH-USA-26/Presentations/BHUSA26-Porat-No-Tools-Required-REV01.pdf) |
| 74.0 | Original technique | kept | [One Chain to Own Them All: Breaking AI Infrastructures](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Ji%27an%20Zhou%2C%20Lei%20Lu%20-%20One%20Chain%20to%20Own%20Them%20All%20-%20Breaking%20AI%20Infrastructures%20-%20azraelxuemo%20v3.pdf) [Related 1](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Ji%27an%20Zhou%2C%20Lei%20Lu%20-%20One%20Chain%20to%20Own%20Them%20All%20-%20Breaking%20AI%20Infrastructures%20-%20azraelxuemo%20v3.pdf) |
| 73.8 | Meaningful combination | kept | [One Char to Rule Them All: DNS Silent Vulnerabilities in Domain Name Resolution](https://i.blackhat.com/Asia-26/Presentations/BHAS26-Miao-One-Char-to-Rule-The.pdf) |
| 73.7 | Meaningful extension | kept | [Recovering Encrypted LLM Reasoning Traces](https://arxiv.org/abs/2608.09867) [Related 1](https://embracethered.com/blog/posts/2026/recovering-encrypted-llm-thoughts/) |
| 73.2 | Meaningful extension | kept | [DNS Cache Poisoning Like it's 2006](https://www.usenix.org/conference/usenixsecurity26/presentation/ben-simhon) [Related 1](https://www.usenix.org/system/files/usenixsecurity26-ben-simhon.pdf) [Related 2](https://kb.isc.org/docs/cve-2025-40780) |
| 73.0 | Meaningful extension | kept | [Pass-the-Passkey Family of Attacks](https://www.dsinternals.com/en/black-hat-usa-26-pass-the-passkey/) [Related 1](https://i.blackhat.com/BH-USA-26/Presentations/BHUS26-Grafnetter-Pass-the-Passkey-WP.pdf) [Related 2](https://i.blackhat.com/BH-USA-26/Presentations/BHUS26-Grafnetter-Pass-the-Passkey-Slides.pdf) |
| 73.0 | Meaningful extension | kept | [DOMPurify XSS via `<selectedcontent>` re-clone](https://github.com/cure53/DOMPurify/security/advisories/GHSA-87xg-pxx2-7hvx) |
| 72.7 | Original technique | kept | [When Agentic Glue Melts: Exploiting Cloudflare Code Mode and Workers](https://research.checkpoint.com/2026/when-agentic-glue-melts/) [Related 1](https://i.blackhat.com/BH-USA-26/Presentations/BUHUS26-Porat-When-Agentic-Glue-Melts-REV01.pdf) [Related 2](https://github.com/yardenporat353/WhenAgenticGlueMeltsPOCs) |
| 72.5 | Tooling / methodology | kept | [BUIzz: Finding Policy Enforcement Bugs via Interaction Simulation on the Browser User Interface](https://www.usenix.org/conference/usenixsecurity26/presentation/jung) [Related 1](https://www.usenix.org/system/files/usenixsecurity26-jung.pdf) [Related 2](https://github.com/WebSec-Lab/BUIzz) |
| 71.8 | Meaningful extension | kept | [Angular compromise through dev infra: GitHub Actions cache poisoning as a vulnerability class](https://adnanthekhan.com/posts/angular-compromise-through-dev-infra) [Related 1](https://adnanthekhan.com/posts/clinejection/) [Related 2](https://adnanthekhan.com/posts/copilot-or-co-conspirator/) [Related 3](https://github.com/AdnaneKhan/Cacheract) |
| 71.8 | Meaningful extension | kept | [Prompt Injection as Role Confusion (CoT Forgery)](https://role-confusion.github.io/) [Related 1](https://arxiv.org/abs/2603.12277) |
| 71.8 | Meaningful combination | kept | [Analyzing the WebRTC Ecosystem and Breaking Authentication in DTLS-SRTP](https://www.usenix.org/conference/usenixsecurity26/presentation/bach) [Related 1](https://www.usenix.org/system/files/usenixsecurity26-bach.pdf) |
| 71.5 | Meaningful combination | kept | [Cruising for Shells in Flowise](https://www.elttam.com/blog/cruising-for-shells-in-flowise) |
| 71.2 | Meaningful extension | kept | [We Need to Talk About CSRF Again](https://blog.voorivex.team/we-need-to-talk-about-csrf-again) |
| 71.1 | Tooling / methodology | kept | [The State of Passkeys: Studying the Adoption and Security of Passkeys on the Web](https://www.usenix.org/conference/usenixsecurity26/presentation/jannett) [Related 1](https://github.com/RUB-NDS/state-of-passkeys-artifacts/blob/main/paper.pdf) [Related 2](https://github.com/RUB-NDS/state-of-passkeys-artifacts) [Related 3](https://passkeys.tools) |
| 71.0 | Meaningful combination | kept | [Sub:jugation — Hijacking Cloud Identities by Recycling Namespaces in Global OIDC Issuers](https://astrix.security/learn/blog/subjugation-hijacking-cloud-identities-by-recycling-namespaces-in-global-oidc-issuers/) [Related 1](https://labs.boostsecurity.io/articles/sleeper-squats-github-oidc-immutable-subject-claim) |
| 70.5 | Original technique | kept | [Hack the Source, Of the Source](https://i.blackhat.com/Asia-26/Presentations/BHAS26-Ng-Hack-the-Source-of-the-Source.pdf) [Related 1](https://i.blackhat.com/BH-USA-26/Presentations/US-26-SplitlineNg-BornCorrupted-Thursday.pdf) |
| 70.5 | Meaningful extension | kept | [Melting the Flesh of PHP's Memory Hardening](https://www.usenix.org/conference/usenixsecurity26/presentation/wu-yifan) [Related 1](https://www.usenix.org/system/files/usenixsecurity26-wu-yifan.pdf) |
| 70.1 | Meaningful combination or adaptation | kept | [What's in a tag name? JavaScript, apparently](https://portswigger.net/research/whats-in-a-tag-name-javascript-apparently) |
| 70.0 | Meaningful combination | kept | [Write Once, Shell Everywhere: Turning Arbitrary File Writes into RCE](https://ethiack.com/info-hub/research/write-once-shell-everywhere-arbitrary-file-writes-into-rce) |
| 70.0 | Meaningful combination | kept | [The CoreBreak Attack: Turning AI Agents into Credentials Exfiltration Vectors](https://i.blackhat.com/BH-USA-26/Presentations/CoreBreak_BlackHat2026_FINAL.pdf) |
| 69.8 | Meaningful combination | kept | [Poisoning Claude Code: One GitHub Issue to Break the Supply Chain](https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/) |
| 69.5 | Original technique | kept | [Two Bypasses for Chrome's Sanitizer API](https://slcyber.io/research-center/two-bypasses-for-chromes-sanitizer-api/) |
| 69.5 | Meaningful extension | removed | [Network-Level Prompt and Trait Leakage in Local Research Agents](https://www.usenix.org/conference/usenixsecurity26/presentation/jeong) |
| 69.2 | Meaningful extension | kept | [HashDoS in V8's array-index string hash, and a seeded but invertible permutation as the fix](https://hackerone.com/reports/3511792) [Related 1](https://nodejs.org/en/blog/vulnerability/march-2026-hashdos) |
| 69.1 | Tooling or methodology contribution | removed | [TranSPArent: Taint-style Vulnerability Detection in Generic Single Page Applications through Automated Framework Abstraction](https://www.ndss-symposium.org/wp-content/uploads/2026-f1721-paper.pdf) [Related 1](https://zenodo.org/records/17822391) |
| 68.8 | Tooling / methodology | kept | [Are your Sites Truly Isolated? Automatically Detecting Logic Bugs in Site Isolation Implementations](https://www.ndss-symposium.org/wp-content/uploads/2026-f902-paper.pdf) [Related 1](https://www.ndss-symposium.org/wp-content/uploads/f0902-drescher-slides.pdf) |
| 68.8 | Tooling / methodology | kept | [Finding Gadgets Like it's 2026](https://www.atredis.com/blog/2026/3/12/findings-gadgets-like-its-2026) [Related 1](https://github.com/atredispartners/llmchainhunter) |
| 68.6 | Meaningful combination | kept | [Almost Impossible: Java Deserialization Through Broken Crypto in OpenText Directory Services](https://slcyber.io/research-center/almost-impossible-java-deserialization-through-broken-crypto-in-opentext-directory-services/) |
| 68.6 | Tooling or methodology contribution | kept | [Breaking the Boundaries: Analyzing QUIC Frame-Packet Interactions With QUIC-Attacker](https://www.usenix.org/conference/usenixsecurity26/presentation/erinola) [Related 1](https://www.usenix.org/system/files/usenixsecurity26-erinola.pdf) [Related 2](https://zenodo.org/records/20280317) |
| 68.1 | Meaningful extension | kept | [HijackKV: New Threat in Position-Independent KV Cache Reuse](https://www.usenix.org/conference/usenixsecurity26/presentation/zhang-yichi) [Related 1](https://www.usenix.org/system/files/usenixsecurity26-zhang-yichi.pdf) [Related 2](https://arxiv.org/abs/2607.19957) [Related 3](https://github.com/YichiCS/KV-Cache-Hijack) |
| 67.9 | Meaningful extension | kept | [Avoiding the paradox: A native full-read SSRF and one-shot DoS in SvelteKit](https://zhero-web-sec.github.io/research-and-things/avoiding-the-paradox-a-native-full-read-ssrf-and-oneshot-dos-in-sveltekit) |
| 67.8 | Meaningful extension | kept | [Alias Equals Zone? Large-Scale and Stealthy Takeover of Domain Hosting Service via CNAME-Following Cross-Domain Verification](https://www.usenix.org/conference/usenixsecurity26/presentation/li-ruixuan) |
| 67.8 | Meaningful combination or adaptation | kept | [Out of Bounds, Out of Sandbox: RCE in Go JavaScript Engine](https://www.slcyber.io/research/out-of-bounds-out-of-sandbox-rce-goja) |
| 67.7 | Tooling / methodology | kept | [MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection](https://www.usenix.org/conference/usenixsecurity26/presentation/syros) [Related 1](https://www.usenix.org/system/files/usenixsecurity26-syros.pdf) [Related 2](https://arxiv.org/abs/2602.09222) |
| 67.6 | Meaningful extension | kept | [The Usual Suspect: Type Confusion in Twelve Bytes](https://blog.voorivex.team/usual-suspect-type-confusion-in-twelve-bytes) |
| 67.5 | Meaningful combination | kept | [CRLF-Powered Desync Attacks: Beheading HTTP Streams](https://portswigger.net/research/crlf-powered-desync-attacks) [Related 1](https://thomas.stacey.se/posts/CRLF-Powered-Desync-Attacks/) [Related 2](https://i.blackhat.com/BH-USA-26/Presentations/US-26-Stacey-CRLF-Powered-Desync-Attacks-Wed.pdf) [Related 3](https://github.com/t0xodile/crlf-powered-desync-scanner) |
| 67.5 | Meaningful combination | kept | [ChatMate: Remote Prompt Execution on AI Assistants through Sandbox Escaping](https://i.blackhat.com/BH-USA-26/Presentations/BHUS26-Lahav-ChatMate-Slides.pdf) |
| 67.3 | Meaningful combination | kept | [Solving an ORB mystery](https://lab.ctbb.show/research/solving-an-orb-mystery) |
| 67.2 | Meaningful extension | kept | [Path traversal in signed URLs — present even in the official AWS SDKs](https://blog.flatt.tech/entry/signed_url_path_traversal) |
| 67.0 | Meaningful extension | kept | [Borrowing Windows Hello Keys for Authentication and Persistence](https://dirkjanm.io/borrowing-windows-hello-keys/) |
| 66.8 | Meaningful combination | kept | [Remote Command Execution in Google Cloud with Single Directory Deletion](https://flatt.tech/research/posts/remote-command-execution-in-google-cloud-with-single-directory-deletion/) |
| 66.8 | Meaningful extension | kept | [Web Cache Overflow: Exploiting Imprecise Keys for Cache Degradation and Beyond](https://arxiv.org/abs/2608.04744) [Related 1](https://github.com/Golim/web-cache-overflow) |
| 66.5 | Meaningful combination | kept | [AutoFail: Breaking Web Boundaries using Android's Autofill Framework](https://github.com/SecPriv/autofail) |
| 66.5 | Tooling or methodology contribution | kept | [Scanning the Scanners: Turning Security Vendors into Supply-Chain Weapons](https://i.blackhat.com/BH-USA-26/Presentations/US-26-Karger-Scanning-The-Scanners-Thursday.pdf) [Related 1](https://github.com/rek7/build-canaries) [Related 2](https://github.com/rek7/DVASP) |
| 66.5 | Meaningful combination | kept | [zkLogin: when ZKP is not enough](https://brave.com/blog/zklogin/) [Related 1](https://eprint.iacr.org/2026/227) |
| 66.5 | Tooling or methodology contribution | kept | [What's in Your Agent's Context? Context Privilege Escalation Attacks against AI Agent Harness](https://arxiv.org/abs/2609.01222) |
| 66.3 | Tooling / methodology | kept | [JavaScript Functions Overload Confusion](https://blog.voorivex.team/javascript-functions-overload-confusion) |
| 66.3 | Meaningful methodology extension | kept | [Living Off The Pipeline: Defensive Research, Weaponized (SmokedMeat / Brisket)](https://labs.boostsecurity.io/articles/introducing-smokedmeat/) [Related 1](https://github.com/boostsecurityio/smokedmeat) |
| 66.2 | Meaningful combination | kept | [SearchLeak: Parameter-to-Prompt injection in Microsoft Copilot](https://www.varonis.com/blog/searchleak) |
| 66.1 | Meaningful combination | kept | [Claude in Chrome: from alert(1) to full account takeover](https://labs.zenity.io/post/claude-in-chrome-from-alert-to-full-account-takeover) [Related 1](https://labs.zenity.io/post/claude-in-chrome-breaking-down-the-injection) [Related 2](https://labs.zenity.io/post/account-takeover-via-claude-in-chrome-a-technical-deep-dive) |
| 66.0 | Tooling / methodology | kept | [Agentic Browsers and the Same-Origin Policy](https://agent-security.cs.washington.edu/agentic_browsers_sop.html) [Related 1](https://www.franziroesner.com/pdf/roesner_kohlbrenner_2026_agentic_sop.pdf) [Related 2](https://github.com/UWCSESecurityLab/agentic-browser-sop) |
| 66.0 | Meaningful combination | kept | [KindaRails2Shell: how a MATLAB file reads your secrets and pops a shell on Rails](https://ethiack.com/info-hub/research/kindarails2shell-how-a-matlab-file-reads-your-secrets-and-pops-a-shell-on-ruby-on-rails) [Related 1](https://abdelmounaim.xyz/posts/leaky-avatar/) [Related 2](https://github.com/rails/rails-forensics-CVE-2026-66066) |
| 65.6 | Meaningful combination | kept | [Your WAF Blocked Us, That Was The Exploit — Remote Agent Takeover via Cloudflare, Sentry and Claude Zero-Day](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Barak%20Sternberg%2C%20Nevo%20Poran%2C%20Ron%20Bobrov%20-%20Your%20WAF%20Blocked%20Us%2C%20That%20Was%20The%20Exploit%20-%20Remote%20Agent%20Takeover%20via%20Cloudflare%2C%20Sentry%20and%20C.pdf) [Related 1](https://tenetsecurity.ai/blog/agentjacking-coding-agents-with-fake-sentry-errors/) [Related 2](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Barak%20Sternberg%2C%20Nevo%20Poran%2C%20Ron%20Bobrov%20-%20Your%20WAF%20Blocked%20Us%2C%20That%20Was%20The%20Exploit%20-%20Remote%20Agent%20Takeover%20via%20Cloudflare%2C%20Sentry%20and%20C.pdf) |
| 65.5 | Meaningful combination | kept | [Hacking Your Life with AI Can Get You Hacked: How AI Orchestration Platforms Ship RCE by Design](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Peyton%20Kennedy%20-%20Hacking%20Your%20Life%20with%20AI%20Can%20Get%20You%20Hacked%20How%20AI%20Orchestration%20Platforms%20Ship%20RCE%20by%20Design%20-%20V1.pdf) [Related 1](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Peyton%20Kennedy%20-%20Hacking%20Your%20Life%20with%20AI%20Can%20Get%20You%20Hacked%20How%20AI%20Orchestration%20Platforms%20Ship%20RCE%20by%20Design%20-%20V1.pdf) |
| 65.5 | Meaningful extension | kept | [Stealing GitHub tokens via VS Code webview keyboard event bubbling](https://blog.ammaraskar.com/github-token-stealing/) |
| 65.5 | Meaningful combination | kept | [AgentForger: ChatGPT Cross-Site Agent Forgery](https://labs.zenity.io/post/agentforger-part-1-chatgpt-cross-site-agent-forgery) [Related 1](https://labs.zenity.io/post/agentforger-part-2-the-autonomous-insider) |
| 65.4 | Tooling or methodology contribution | kept | [Chat-template backdoors: systematic evaluation and agentic impact](https://arxiv.org/abs/2602.04653) [Related 1](https://arxiv.org/abs/2602.05401) |
| 65.1 | Meaningful combination | kept | [XSS2Shell: WordPress Preauth XSS to RCE Chain (CVE-2026-64638)](https://pwn.ai/blog/xss2shell) |
| 64.8 | Meaningful combination | kept | [One trigram at a time: XSLeak via Universal CSS Injection and DoS in Opera (GX)](https://zhero-web-sec.github.io/research-and-things/one-trigram-at-a-time-xsleak-via-universal-css-injection-and-dos-in-opera-(gx)) |
| 64.8 | Meaningful extension | kept | [Zero Knowledge (About) Encryption: A Comparative Security Analysis of Three Cloud-based Password Managers](https://eprint.iacr.org/2026/058) |
| 64.8 | Meaningful extension | kept | [Caught in the Octopus Trap: Unauthenticated RCE in Argo CD](https://www.synacktiv.com/en/publications/caught-in-the-octopus-trap-unauthenticated-rce-in-argo-cd-with-codeql) |
| 64.8 | Meaningful extension | kept | [DOMPurify bypass via SMIL animateTransform on Safari](https://mizu.re/post/dompurify-bypass-smil-animatetransform-safari) |
| 64.7 | Meaningful extension | kept | [When HTTP 402 Meets the Blockchain: Risks on Emerging x402 Payments](https://www.usenix.org/conference/usenixsecurity26/presentation/wang-qinying) [Related 1](https://arxiv.org/abs/2607.19545) [Related 2](https://github.com/HexHive/x402scope) |
| 64.6 | Tooling or methodology contribution | removed | [Bullseye: Detecting Prototype Pollution in NPM Packages with Proof of Concept Exploits](https://www.ndss-symposium.org/ndss-paper/bullseye-detecting-prototype-pollution-in-npm-packages-with-proof-of-concept-exploits/) [Related 1](https://spectrum.library.concordia.ca/id/eprint/996198/2/Houis_MASc_F2025.pdf) |
| 64.5 | Meaningful extension | kept | [Pwning Claude Code in 8 Different Ways](https://flatt.tech/research/posts/pwning-claude-code-in-8-different-ways/) |
| 64.4 | Meaningful combination or adaptation | kept | [Hacking AI customer service agents](https://www.intigriti.com/researchers/blog/hacking-tools/hacking-ai-customer-service-agents) |
| 64.3 | Tooling or methodology contribution | kept | [The sorry state of skill distribution](https://blog.trailofbits.com/2026/06/03/the-sorry-state-of-skill-distribution/) [Related 1](https://github.com/trailofbits/overtly-malicious-skills) [Related 2](https://github.com/cisco-ai-defense/skill-scanner/pull/25) |
| 64.2 | Meaningful extension | kept | [Cast Attack: A New Threat Posed by Ghost Bits in Java](https://i.blackhat.com/Asia-26/Presentations/Asia-26-Bai-Cast-Attack-Ghost-Bits-4.23.pdf) |
| 64.1 | Meaningful extension | kept | [The Memory Heist](https://www.ayush.digital/blog/the-memory-heist) |
| 64.0 | Meaningful extension | kept | [Grand Theft Atlas](https://labs.zenity.io/post/grand-theft-atlas) |
| 63.4 | Meaningful combination | kept | [The Click that shouldn't have worked: RCE via clickjacking in Internet Explorer](https://swarm.ptsecurity.com/the-click-that-shouldnt-have-worked-rce-via-clickjacking-in-internet-explorer/) |
| 63.2 | Meaningful combination | kept | [Three 0-Day Vulnerabilities in Adminer](https://blog.voorivex.team/three-0-day-vulnerabilities-in-adminer) |
| 63.2 | Meaningful combination | kept | [Race Against The Patch: Four Exploit Chains in LiteLLM](https://starlabs.sg/blog/2026/05-race-against-the-patch-the-evolution-of-four-exploit-chains-in-litellm/) |
| 63.2 | Meaningful extension | kept | [Overcoming the Retrieval Barrier: Indirect Prompt Injection in the Wild for LLM Systems](https://www.usenix.org/conference/usenixsecurity26/presentation/chang-hongyan) [Related 1](https://www.usenix.org/system/files/usenixsecurity26-chang-hongyan.pdf) [Related 2](https://arxiv.org/abs/2601.07072) |
| 62.8 | Meaningful extension | kept | [Privacy risks of agentic oversharing on the Web (SPILLAGE)](https://brave.com/blog/agentic-oversharing/) |
| 62.8 | Meaningful combination | kept | [ELF in the Pixels: Building Shared Object–Image Polyglots](https://blog.babelo.xyz/posts/elf-in-the-pixels/) |
| 62.8 | Tooling or methodology contribution | kept | [When Authorization Loses Its Meaning: Breaking and Fixing Third-Party Online Payments](https://www.usenix.org/conference/usenixsecurity26/presentation/xiao) [Related 1](https://www.usenix.org/system/files/usenixsecurity26-xiao.pdf) |
| 62.6 | Meaningful combination | kept | [Codex Discovered a Hidden HTTP/2 Bomb](https://blog.calif.io/p/codex-discovered-a-hidden-http2-bomb) |
| 62.5 | Meaningful combination | kept | [LGTM: Bypassing an LLM Build Gate When Prompt Injection Fails](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Aviv%20Donenfeld%20-%20LGTM%20Bypassing%20an%20LLM%20Build%20Gate%20When%20Prompt%20Injection%20Fails%20-%20LGMT%20v2.pdf) [Related 1](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Aviv%20Donenfeld%20-%20LGTM%20Bypassing%20an%20LLM%20Build%20Gate%20When%20Prompt%20Injection%20Fails.pdf) |
| 62.5 | Meaningful extension | kept | [Parse and Parse: MIME Validation Bypass to XSS via Parser Differential](https://lab.ctbb.show/research/parse-and-parse-mime-validation-bypass-to-xss-via-parser-differential) |
| 62.2 | Meaningful combination | kept | [FCSC 2026 writeups: Firefox `execCommand` ICU-vs-JS case-folding differential, Gunicorn `HEAd` smuggling, libmagic polyglots](https://web.archive.org/web/20260418230027/https://mizu.re/post/fcsc-2026-writeups) |
| 62.2 | Tooling or methodology contribution | kept | [A Formal Analysis of Agent Payment Protocols](https://arxiv.org/abs/2609.00060) |
| 62.0 | Meaningful combination | kept | [wp2shell: Pre-Authentication RCE in WordPress Core](https://slcyber.io/research-center/wp2shell-pre-authentication-rce-in-wordpress-core/) [Related 1](https://slcyber.io/research-center/exploit-brokers-pay-500000-for-a-wordpress-rce-i-found-one-with-gpt5-6/) [Related 2](https://blog.calif.io/p/the-wordpress-chain-massacre) |
| 61.8 | Meaningful extension | kept | [The Masks We (Think We) Wear: Privacy Threats of Browser-Extension Wallets in the Web3 Ecosystem](https://petsymposium.org/popets/2026/popets-2026-0094.pdf) [Related 1](https://arxiv.org/abs/2607.06141) [Related 2](https://github.com/podiumdesu/wallet-privacy-threats) |
| 61.7 | Meaningful extension | kept | [Security Considerations on Istio’s CRDs with Namespace-based Multi-Tenancy](https://istio.io/latest/blog/2026/security-considerations-on-namespace-based-multi-tenancy/) |
| 61.5 | Meaningful extension | kept | [Deployment Poisoning: A(nother) Novel Attack Vector for GitHub Actions](https://labs.boostsecurity.io/articles/deployment_poisoning) |
| 61.3 | Tooling or methodology contribution | removed | [One Email, Many Faces: A Deep Dive into Identity Confusion in Email Aliases](https://www.ndss-symposium.org/wp-content/uploads/2026-s148-paper.pdf) [Related 1](https://github.com/lab-rynth/OriginMail) |
| 61.2 | Tooling / methodology | kept | [Token Time Bomb: Evaluating JWT Implementations for Vulnerability Discovery](https://www.ndss-symposium.org/wp-content/uploads/2026-f697-paper.pdf) [Related 1](https://www.ndss-symposium.org/wp-content/uploads/f0697-yang-slides.pdf) |
| 61.1 | Meaningful combination | kept | [Zero-Click RCE in Figma Desktop](https://lab.ctbb.show/research/figma-desktop-zero-click-rce/) |
| 61.1 | Useful application or case study | kept | [Site Isolation is Dead: How Site Isolation is Broken in Agentic Browsers and Extensions](https://wsp-lab.github.io/papers/lee-sp26.pdf) [Related 1](https://github.com/WSP-LAB/Site-Isolation-Is-Dead) |
| 60.9 | Tooling / methodology | kept | [LeakyLinks: Measuring the Security and Privacy Risks of URL Scanning Services](https://swag.cispa.saarland/papers/mustafa2026leakylinks.pdf) [Related 1](https://github.com/cispa/leakylinks) |
| 60.8 | Meaningful extension | kept | [Smashing the ServiceNow Sandbox – Pre-Authentication RCE](https://slcyber.io/research-center/smashing-the-servicenow-sandbox-pre-authentication-rce/) |
| 60.5 | Meaningful extension | kept | [Your House Has an FFmpeg Problem](https://www.elttam.com/blog/your-house-has-an-ffmpeg-problem) |
| 60.5 | Tooling / methodology | kept | [A First Measurement Study on Authentication Security in Real-World Remote MCP Servers](https://arxiv.org/abs/2605.22333) |
| 60.5 | Meaningful combination | kept | [When Cache Poisoning Meets LLM Systems: Semantic Cache Poisoning](https://www.ndss-symposium.org/ndss-paper/when-cache-poisoning-meets-llm-systems-semantic-cache-poisoning-and-its-countermeasures/) [Related 1](https://www.ndss-symposium.org/wp-content/uploads/2026-f200-paper.pdf) [Related 2](https://github.com/dequeueing/SemanticCache_Poisoning) |
| 60.4 | Useful synthesis | kept | [The Dot-Dot-Slash That Frameworks Hand You: CSPT Across Every Major Frontend Framework](https://lab.ctbb.show/research/the-dot-dot-slash-that-frameworks-hand-you) [Related 1](https://github.com/xssdoctor/cspt_research) |
| 59.9 | Useful application/case study | removed | [GitHub RCE Vulnerability: CVE-2026-3854](https://www.wiz.io/blog/github-rce-vulnerability-cve-2026-3854) |
| 59.8 | Meaningful extension | kept | [Computer-Use and TOCTOU: What You Click Is Not What You Get!](https://embracethered.com/blog/posts/2026/toctou-agent-what-you-click-is-not-what-you-get/) |
| 59.1 | Insufficient evidence | removed | [Patch-Guided Vulnerability Detection: Extracting Java API Security Rules via Attack–Defense Cross-Analysis (VulGenie)](https://www.usenix.org/conference/usenixsecurity26/presentation/chen-bofei) [Related 1](https://zenodo.org/records/18039660) |
| 58.0 | Meaningful combination or adaptation | kept | [This Message Was Sent by Microsoft: Turning Microsoft Apps into our Phishing Platform](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Keanu%20Nys%20-%20This%20Message%20Was%20Sent%20by%20Microsoft%20Turning%20Microsoft%20Apps%20into%20our%20Phishing%20Platform%20-%20DEF%20CON%2034%20Red%20Byte%20Messag.pdf) |
| 57.5 | Insufficient evidence | removed | [Beyond the Limits of Site Isolation](https://www.youtube.com/watch?v=d3nfJL86jrc) |
| 54.9 | Useful application | removed | [When Two Parsers Disagree: Exploiting Query String Differentials for XSS](https://blog.voorivex.team/when-two-parsers-disagree-exploiting-query-string-differentials-for-xss) |
| 54.6 | Useful application or case study | removed | [Trust Transitions in Email: When Sanitizers and CSS Engines Disagree](https://labs.trace37.com/blog/css-email-trust-transitions/) |
| 54.5 | Useful application/case study | removed | [Shaking the MCP Tree: A Security Deep Dive](https://blog.voorivex.team/shaking-the-mcp-tree) |
| 54.5 | Meaningful combination | removed | [HermeticReader: turning Adobe's 300M-install extension into a WhatsApp takeover](https://guard.io/labs/hermeticreader---the-vulnerability-that-turned-adobe-300m-install-extension-into-a-full-whatsapp-takeover) |
| 54.5 | Meaningful extension | removed | [Pass the Passkey: A Novel Attack Surface in Passwordless Authentication](https://unit42.paloaltonetworks.com/passwordless-authentication-security-risks/) |
| 54.5 | Meaningful extension | removed | [Re:CACHE — Excessive reflection, type confusion, and 0-click SXSS on Next.js](https://zhero-web-sec.github.io/research-and-things/re-cache-excessive-reflection-type-confusion-and-0-click-sxss-on-nextjs) |
| 54.2 | Meaningful extension | removed | [H3Act: Automated Measuring Semantic Conversion Anomalies of HTTP/3-to-HTTP/1.1 Translation in CDNs](https://www.usenix.org/conference/usenixsecurity26/presentation/peng-qihang) |
| 54.2 | Tooling / methodology | removed | [Identifying Logical Vulnerabilities in QUIC Implementations](https://www.ndss-symposium.org/wp-content/uploads/2026-s1777-paper.pdf) |
| 54.2 | Useful application or case study | removed | [Vault Raider: Stealthy UI-based Attacks Against Password Managers in Desktop Environments](https://www.ndss-symposium.org/wp-content/uploads/2026-s1067-paper.pdf) [Related 1](https://zenodo.org/records/16996391) |
| 54.2 | Useful application or case study | removed | [Drive-By Agent Hijacking: One Website Visit, Persistent Model Poisoning](https://www.cyera.com/research/nemoclaw-one-website-visit-to-hijack-your-ai-agent) |
| 53.8 | Tooling / methodology | removed | [AI Server-Side Browser Security Whitepaper](https://xlab.tencent.com/cn/2026/02/02/ai-browser-crawler-whitepaper/) |
| 53.5 | Useful application | removed | [Exploiting Auth0 Defaults in XSS Attacks](https://www.elttam.com/blog/exploiting-auth0-defaults-in-xss-attacks/) |
| 53.2 | Meaningful combination | removed | [L3akCTF 2026 "Squid": racing `/proc/self/fd` symlinks against Flask `send_file`'s stat/open TOCTOU to read zero-length files](https://jorianwoltjer.com/blog/p/ctf/l3akctf-2026-squid) |
| 53.2 | Meaningful combination | removed | [Burp Suite Professional: browser-powered crawl writes attacker-controlled files](https://hackerone.com/reports/3712279) |
| 53.0 | Meaningful combination | removed | [SekaiCTF 2026 "Filtered Reality": invalid Signed HTTP Exchange fallback navigation as a redirect and CSP-nonce escape primitive](https://github.com/project-sekai-ctf/sekaictf-2026/blob/main/web/filtered-reality/solution/writeup.md) |
| 53.0 | Useful application | removed | [OffGuard: Breaking the Most Popular AI Gateway (LiteLLM) from Auth Bypass to Cloud Compromise](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Yaara%20Shriki%20-%20OffGuard%20Breaking%20the%20Most%20Popular%20AI%20Gateway%20from%20Auth%20Bypass%20to%20Cloud%20Compromise.pdf) |
| 53.0 | Meaningful extension | removed | [Salesforce Apex Predator: Breaking Salesforce Sites](https://dcworkshop.reco.ai/) [Related 1](https://www.reco.ai/blog/salesforce-experience-site-pentest-apex-predator) [Related 2](https://github.com/nitay-bachrach/lwred) |
| 52.9 | Meaningful extension | removed | [Never Trust the Output: Data Pollution in AI Agents and MCP](https://blog.slonser.info/posts/smugglle-ai-ouputs/) |
| 52.8 | Meaningful extension | removed | [Node.js TLS hostname-normalisation differentials: Unicode dot separators defeat wildcard depth](https://hackerone.com/reports/3688064) [Related 1](https://hackerone.com/reports/3656716) [Related 2](https://hackerone.com/reports/3649802) [Related 3](https://github.com/nodejs/node/commit/1efb4ff51a) |
| 52.7 | Tooling / methodology | removed | [Poisoned by the Host: Large-Scale Measurement of Host Name Poisoning in Web Applications](https://www.iamruiyang.me/papers/sp26-HNP.pdf) |
| 52.5 | Tooling / methodology | removed | [PANGOLIN: Fuzzing Multilingual IoT Firmware with LLM-Driven Code Analysis](https://www.usenix.org/conference/usenixsecurity26/presentation/jia-zhipeng) |
| 52.5 | Meaningful combination | removed | [Critical Flaws in Anthropic, Google and OpenAI's Coding Agents: the trust-handoff primitive](https://novee.security/blog/critical-flaws-in-anthropic-google-and-openais-coding-agents/) [Related 1](https://novee.security/blog/gemini-cli-cvss-10-rce-novee-security/) |
| 52.4 | Meaningful extension | removed | [CVE-2026-41238: How Prototype Pollution Turns DOMPurify Into an XSS Gadget](https://labs.trace37.com/blog/dompurify-pp-ceh-bypass/) [Related 1](https://github.com/advisories/GHSA-v9jr-rg53-9pgp) |
| 52.2 | Meaningful extension | removed | [FirefUXSS: universal XSS in Firefox Focus/Klar for iOS](https://github.com/v12-security/pocs/tree/main/firefox) |
| 52.2 | Meaningful extension | removed | [XSS via i18n translation-template injection in NodeBB](https://www.aikido.dev/blog/eight-high-severity-vulnerabilities-nodebb) |
| 52.2 | Useful application | removed | [Drupal PostgreSQL SQL Injection: From SELECT-Only to RCE](https://blog.lexfo.fr/drupal-postgresql-sqli-to-rce.html) |
| 52.1 | Useful application | removed | [uXSS on Samsung Browser (CVE-2025-58485 · SVE-2025-1879)](https://blog.voorivex.team/uxss-on-samsung-browser-cve-2025-58485-sve-2025-1879) |
| 52.1 | Meaningful combination | removed | [iframe sandbox bypass, cross-origin drag-and-drop, unvalidated postMessage origin, cookie bomb to account takeover](https://medium.com/@renwa/iframe-sandbox-bypass-cross-origin-drag-drop-unvalidated-postmessage-origin-cookie-bomb-to-21357a4d94f5) |
| 51.9 | Useful application or case study | removed | [API Keys Leaking in PNG Metadata of AI Images](https://trufflesecurity.com/blog/api-keys-leaking-in-png-metadata-of-ai-images) |
| 51.8 | Meaningful combination | removed | [New Age of Collisions: Pre-Auth Arbitrary File Read as root in cPanel](https://slcyber.io/research-center/new-age-of-collisions-reading-arbitrary-files-pre-auth-as-root-in-cpanel-cve-2026-29205/) |
| 51.6 | Tooling / methodology | removed | [Attacking and Defending AI Browsers](https://i.blackhat.com/BH-USA-26/Presentations/US-26-Chaikin-Attacking-Defending-AI-Browsers.pdf) [Related 1](https://brave.com/blog/indirect-prompt-injection/) |
| 51.5 | Meaningful combination | removed | [Finding XSS on Shazzer (literally)](https://jorianwoltjer.com/blog/p/stories/finding-xss-on-shazzer) |
| 51.0 | Useful application | removed | [Sandcastles, Not Sandboxes: `ctypes.CDLL(None)` reaches Emscripten exports to escape Pyodide into the host JS runtime](https://www.cyera.com/research/sandcastles-not-sandboxes-how-one-architectural-flaw-exposed-seven-products) [Related 1](https://www.cyera.com/research/cellbreak-grists-pyodide-sandbox-escape-and-the-data-at-risk-blast-radius) |
| 50.6 | Meaningful extension | removed | [Apache httpd HTTP/2 Memory Exhaustion (CVE-2025-53020)](https://galbarnahum.com/posts/apache-httpd-cve-2025-53020) |
| 50.6 | Independent rediscovery | removed | [From Length to Content: Token-Length Side-Channel Attacks on LLM API Merged Outputs](https://www.usenix.org/conference/usenixsecurity26/presentation/li-sijia) [Related 1](https://www.usenix.org/system/files/usenixsecurity26-li-sijia.pdf) |
| 50.5 | Meaningful extension | removed | [Blind enumeration of unreadable records via a sort oracle in Trello](https://bugcrowd.com/disclosures/0ecb51a3-2064-4f9d-aa19-aa7b6ae21812/blind-enumeration-of-private-card-names-via-sort-oracle-and-id-discovery) |
| 50.5 | Tooling / methodology | removed | [Golang code review notes II](https://www.elttam.com/blog/golang-code-review-notes-ii) |
| 50.5 | Useful application | removed | [Fooling AI Agents: Web-Based Indirect Prompt Injection Observed in the Wild](https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/) |
| 50.5 | Useful application | removed | [Proto6: The Schema Was Not Supposed to Run](https://www.cyera.com/research/proto6-the-schema-was-not-supposed-to-run) |
| 50.4 | Useful application | removed | [Breaking the Control Plane: Exploiting MCP Servers in AI Workflows](https://troopers.de/downloads/troopers26/TR26_Breaking_the_Control_Plane_F3XCER.pdf) [Related 1](https://youtu.be/DAbyi6MZR9w) |
| 50.2 | Useful application | removed | [Trusted Publishing, Untrusted Branch: Inside the Red Hat npm Compromise](https://labs.boostsecurity.io/articles/trusted-publishing-untrusted-branch-red-hat-npm) |
| 50.1 | Useful application | removed | [Story of Abusing a Fully Secured redirect_uri in an OAuth Flow](https://blog.voorivex.team/story-of-abusing-a-fully-secured-redirect-uri-in-an-oauth-flow) |
| 50.1 | Useful application or case study | removed | [SvelteSpill: A Cache Deception Bug in SvelteKit + Vercel](https://www.aikido.dev/blog/sveltespill-cache-deception-sveltekit-vercel) |
| 50.0 | Independent rediscovery | removed | [The SQL Server Unicode problem: Best-Fit mapping as a universal filter bypass](https://www.synacktiv.com/en/publications/the-sql-server-unicode-problem-why-your-data-might-not-be-what-you-think-it-is) |
| 50.0 | Meaningful combination | removed | [Content-Type Override to Stored XSS on public objects](https://blog.voorivex.team/content-type-override-to-stored-xss-on-public-objects) |
| 50.0 | Meaningful extension | removed | [Hack the Elephant One Bite at a Time: NUL byte SQL Injection in pdo\_firebird](https://swarm.ptsecurity.com/hack-the-elephant-one-bite-at-a-time-nul-byte-sql-injection-in-pdo_firebird-and-null-pointer-dereference-in-pdo-pgsql/) [Related 1](https://swarm.ptsecurity.com/hack-the-elephant-one-bite-at-a-time-jpeg-related-memory-safety-bugs-in-php/) |
| 50.0 | Useful application | removed | [When Filenames Become Attack Surfaces: Weaponizing NASA's CFITSIO Extended Filename Syntax](https://blog.doyensec.com/2026/05/19/cfitsio-weaponized-filenames.html) |
| 49.7 | Useful synthesis | removed | [HTTP/2 WAF Bypass: A Black-Box Methodology (h2 framing)](https://lab.ctbb.show/research/h2-WAF-Bypasses) |
| 49.6 | Useful application | removed | [The CSRF-token leak both Claude Code and Codex Security missed (SAML IdP form helpers)](https://gmo-cybersecurity.com/blog/claude-codex-missed-csrf-token-leak/) |
| 49.6 | Tooling / methodology | removed | [Phantom Squatting: AI-Hallucinated Domains as a Software Supply Chain Vector](https://unit42.paloaltonetworks.com/phantom-squatting-hallucinated-web-domains/) |
| 49.5 | Useful application | removed | [Charting your way in: Helm template injection](https://www.synacktiv.com/en/publications/charting-your-way-in-helm-template-injection) |
| 49.5 | Useful application | removed | [My Road to Black-Box RCE in LLM Products: `postinstall` in AI preview builders, weakest-model-wins guardrail bypass, and DLP evasion by channel choice](https://mp.weixin.qq.com/s/whv4LzJTiJt-i2zHzdG8Eg) |
| 49.2 | Tooling / methodology | removed | [Gotta Phish 'Em All! Novel Attack Techniques via Persistent Browser-in-the-Middle](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Giacomo%20Lenzini%20-%20Gotta%20Phish%20%27Em%20All%20Novel%20Attack%20Techniques%20via%20Persistent%20Browser-in-the-Middle%20-%20v2.pdf) |
| 49.0 | Useful application | removed | [BodySnatcher: agentic hijacking in ServiceNow](https://appomni.com/ao-labs/bodysnatcher-agentic-ai-security-vulnerability-in-servicenow/) |
| 48.8 | Tooling / methodology | removed | [No Socket, No Privs, No Problem: Weaponizing OCI Registries for SSRF, Credential Theft, and Container Escapes](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20David%20Rochester%2C%20Nicholas%20Gould%20-%20No%20Socket%2C%20No%20Privs%2C%20No%20Problem%20Weaponizing%20OCI%20Registries%20for%20SSRF%2C%20Credential%20Theft%2C%20and%20Container%20E.pdf) |
| 48.8 | Useful application | removed | [Beyond Normalization: The Expanding Unicode Attack Surface](https://i.blackhat.com/BH-USA-26/Presentations/BHUSA26-Barnett-Beyond-Normalization-Slides.pdf) |
| 48.7 | Useful application | removed | [Pwning Agentic Browsers with PleaseFix](https://zenity.io/research/pleasefix-vulnerabilities) |
| 48.0 | Meaningful extension | removed | [CVE-2026-21876: bypassing OWASP CRS by overwriting the multipart charset in a later segment](https://habr.com/ru/articles/984632/) |
| 48.0 | Tooling / methodology | removed | [Beyond the Ceremony: The 2026 Passkey Attack Surface](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Matteo%20Giordano%20-%20Beyond%20the%20Ceremony%20The%202026%20Passkey%20Attack%20Surface%20-%20v2.pdf) |
| 47.7 | Meaningful combination | removed | [LLM Heist: Hijacking LiteLLM for Traffic Interception, Key Theft, and Tool-Call Injection](https://embracethered.com/blog/posts/2026/hijacking-litellm-for-fun-and-profit/) |
| 47.6 | Useful application or case study | removed | [KYC: Bypass age verification using generative video models](https://www.synacktiv.com/en/publications/kyc-bypass-age-verification-using-generative-video-models) |
| 47.5 | Useful application/case study | removed | [The Script Tag That Isn't: Speculation Rules Injection](https://labs.trace37.com/blog/specfetch-speculation-rules-injection/) |
| 47.2 | Useful application | removed | [Breaking SameSite=Strict in Chrome](https://lab.ctbb.show/writeups/breaking-samesite-strict-in-chrome) |
| 47.2 | Useful application | removed | [Keys to the Kingdom: Anonymous SQL Injection in Drupal Core (CVE-2026-9082)](https://slcyber.io/research-center/keys-to-the-kingdom-anonymous-sql-injection-in-drupal-core-cve-2026-9082/) |
| 46.9 | Useful application | removed | [Hidden security risks in Jupyter notebooks](https://www.sonarsource.com/blog/hidden-security-risks-in-jupyter-notebooks/) |
| 46.9 | Useful application or case study | removed | [Roundcube XSS chained with cookie tossing for full inbox access](https://www.aikido.dev/blog/roundcube-xss-cookie-tossing) [Related 1](https://hackerone.com/reports/3594137) |
| 46.8 | Useful application | removed | [CosmosEscape: Taking Over Every Database in Azure Cosmos DB](https://www.wiz.io/blog/cosmosescape-taking-over-every-database-in-azure-cosmos-db) |
| 46.7 | Useful application or case study | removed | [Astro Full-Read SSRF via Host Header Injection](https://www.aikido.dev/blog/astro-full-read-ssrf-via-host-header-injection) |
| 46.7 | Useful application or case study | removed | [Authorization Bypass in Quarkus via matrix parameters](https://securitylab.github.com/advisories/GHSL-2026-099_Quarkus/) |
| 46.5 | Meaningful extension | removed | [CDN Tsunami: Exploiting HTTP/3-HTTP/1.1 Conversion for DoS Attacks](https://arxiv.org/abs/2607.26589) |
| 45.8 | Independent rediscovery | removed | [Before the first prompt: Code execution paths in trusted coding-agent projects](https://securitylabs.datadoghq.com/articles/coding-agent-project-trust-code-execution-before-first-prompt/) |
| 45.5 | Useful application | removed | [Jupyter Enterprise Gateway: SSTI and YAML break-out to cluster takeover](https://www.elttam.com/blog/jupyter-enterprise-gateway) |
| 45.2 | Useful application | removed | [Same-site DOM XSS using cookie injection via the TikTok analytics pixel](https://medium.com/@renwa/site-dom-xss-using-cookie-injection-the-ai-hackers-are-coming-faster-than-you-think-3ef82f2a991d) |
| 44.8 | Useful application | removed | [Securing the Supply Chain: Cache Vulnerability in RubyGems](https://trufflesecurity.com/blog/rubygems-cache-vulnerability) |
| 44.5 | Useful application | removed | [My First RCE by Reverse Engineering an EXE File With the Help of AI](https://blog.voorivex.team/first-rce-via-reverse-engineering-with-ai) |
| 44.5 | Useful application | removed | [HTTP Request Smuggling via `Connection: close<TAB>` in Node.js llhttp](https://hackerone.com/reports/3723248) |
| 44.3 | Useful application or case study | removed | [LiteLLM Security: SSTI RCE and Unicode Sandbox Bypass](https://fortbridge.co.uk/research/litellm-critical-vulnerabilities-ssti-unicode-bypass/) |
| 44.2 | Independent rediscovery | removed | [Wrestling with a Python: Escaping Copilot Studio's AI-Guarded Sandbox](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Ryan%20Hausknecht%2C%20Simon%20Maxwell-Stewart%20-%20Wrestling%20with%20a%20Python%20Escaping%20Copilot%20Studio%27s%20AI-Guarded%20Sandbox%20-%20DEFCON2026%20embargo.pptx) |
| 44.2 | Useful application | removed | [UI consent bypass via comma injection in Burp's MCP `addAutoApproveTarget`](https://hackerone.com/reports/3717354) |
| 44.0 | Tooling / methodology | removed | [Navigating Lax Load Balancers: When an Intersection Gets You Inside](https://blog.doyensec.com/2026/05/25/cloudsectidbits-elbaph-alb.html) |
| 43.8 | Meaningful extension | removed | [Chaos by Design: The Death of Stochastic Race Conditions in HTTP/3](https://i.blackhat.com/BH-USA-26/Presentations/BHUS26-Chatzoglou-Chaos-by-Design-Slides.pdf) [Related 1](https://github.com/efchatz/timeorch) |
| 43.8 | Useful application | removed | [8 Out of 10 Banks in Belgium HATE This One Weird eID RCE](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20James%20Arnott%20-%208%20Out%20of%2010%20Banks%20in%20Belgium%20HATE%20This%20One%20Weird%20eID%20RCE%20-%20MEDIA%20SERVER%20Belgi.pdf) |
| 43.5 | Meaningful extension | removed | [The Forgotten Bug: How a Node.js Core Design Flaw Enables HTTP Request Splitting](https://r3verii.github.io/cve/2026/02/27/nodejs-toctou.html) |
| 43.2 | Meaningful combination | removed | [AgenticBlabbering: how AI browsers' verbose reasoning fuels the ultimate scamming machine](https://guard.io/labs/agenticblabbering---how-ai-browsers-verbose-reasoning-fuels-the-ultimate-scamming-machine) |
| 43.2 | Useful application | removed | [Ghosts of Encryption Past: Salesforce Marketing Cloud / ExactTarget](https://slcyber.io/research-center/ghosts-of-encryption-past-salesforce-exacttarget/) |
| 43.0 | Useful application | removed | [CargoWise WebTracker — The Keys Were in the Cargo](https://slcyber.io/research-center/cargowise-webtracker-the-keys-were-in-the-cargo/) |
| 43.0 | Useful application | removed | [Remote-content-blocking and CSS-sanitizer bypasses in Roundcube's washtml via SVG `feImage` and SMIL animation attributes](https://hackerone.com/reports/3486747) [Related 1](https://hackerone.com/reports/3590576) [Related 2](https://hackerone.com/reports/3590583) [Related 3](https://hackerone.com/reports/3590586) [Related 4](https://nullcathedral.com/posts/2026-02-08-roundcube-webmail-svg-feimage/) [Related 5](https://nullcathedral.com/posts/2026-03-18-roundcube-round-two-three-more-sanitizer-bypasses/) |
| 43.0 | Useful application | removed | [SECCON CTF 14 Finals: Shadow CSS and friends](https://blog.arkark.dev/2026/03/08/seccon-finals/) [Related 1](https://nanimokangaeteinai.hateblo.jp/entry/2026/03/02/235931) |
| 42.8 | Useful application | removed | [FCSC 2026 "Aquarium": escaping the Node.js Permission Model via `data:` URL import and `SIGUSR1` inspector activation](https://worty.fr/post/writeups/fcsc2026/fcsc_aquarium/) |
| 42.5 | Useful application | removed | [Can a Predicted `window.open` Target Really Be That Impactful?](https://lab.ctbb.show/research/can-a-predicted-window-open-target-really-be-that-impactful) |
| 42.0 | Useful application | removed | [Two cPanel Zero Day Vulnerabilities](https://blog.voorivex.team/two-cpanel-zero-day-vulnerabilities) |
| 41.5 | Independent rediscovery | removed | [Ghost Dependency: version ghosts and name ghosts as supply-chain primitives under agentic coding](https://xlab.tencent.com/cn/2026/02/28/ghost-dependency-agentic-coding-supply-chain-threat/) |
| 40.5 | Duplicate / already known | removed | [postMessage targetOrigin bypass via IP normalization](https://lab.ctbb.show/research/postmessage-targetorigin-bypass-via-ip-normalization) |
| 39.8 | Useful application | removed | [GHSL-2024-198 / GHSL-2024-199: Zero-click RCE in Uptrain](https://securitylab.github.com/advisories/GHSL-2024-198_GHSL-2024-199_Uptrain/) |
| 39.2 | Duplicate / already known | removed | [Mini Shai-Hulud Returns: 42 Malicious npm Packages Fake Sigstore Badges](https://www.endorlabs.com/learn/mini-shai-hulud-returns-42-malicious-npm-packages-fake-sigstore-badges-in-antv-ecosystem-attack) |
| 39.0 | Useful application or case study | removed | [Privilege escalation via authorization bypass in graphql-ruby](https://securitylab.github.com/advisories/GHSL-2026-152_graphql-ruby/) |
| 38.8 | Useful application or case study | removed | [Roundcube: IMAP Command Injection and SSRF via CSS Proxying](https://blog.ostorlab.co/roundcube-imap-injection-ssrf-ove-2026.html) |
| 38.5 | Useful application | removed | [Elasticsearch Painless execution via a pass-through `sort_query` GraphQL argument](https://hackerone.com/reports/3694007) |
| 38.5 | Useful application | removed | [OAuth Client ID Spoofing: Why Fake Client IDs Are Gaining Traction for Stealthy Enumeration](https://www.proofpoint.com/us/blog/threat-insight/oauth-client-id-spoofing-why-fake-client-ids-are-gaining-traction-stealthy) |
| 38.2 | Duplicate / already known | removed | [Unauthenticated RCE in Taskcluster via a GraphQL filter reaching sift's `$where`](https://hackerone.com/reports/3782701) |
| 37.5 | Duplicate / already known | removed | [Domain Decoupling Attack: Exploiting the Validation Gap Between Protective DNS and Shared Edge Routing](https://arxiv.org/abs/2608.00643) |
| 37.0 | Insufficient evidence | removed | [Slop Spotting: Using Rules to Detect AI Slop for Bug Bounty](https://semgrep.dev/events/hsc-26-defcon-34/) [Related 1](https://www.bugbountydefcon.com/agenda-2026) |
| 36.5 | Insufficient evidence | removed | [New Hope for SSRF: Exploiting Credential Relay from APIM to AI Foundry](https://www.cloud-village.org/dc34) |
| 36.5 | Useful application or case study | removed | [An Analysis of Modern Web Security Vulnerabilities Inside WebAssembly Applications](https://arxiv.org/abs/2603.09426) |
| 36.2 | Independent rediscovery | removed | [Install Me Maybe: Turning Claimable VS Code Extension IDs into Supply-Chain Attacks](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Raphael%20Silva%20-%20Install%20Me%20Maybe%20Turning%20Claimable%20VS%20Code%20Extension%20IDs%20into%20Supply-Chain%20Attacks%20-%20v1.pdf) |
| 35.6 | Tooling / methodology | removed | [npx confusion and npxconfuse](https://lab.ctbb.show/research/from-defcon-research-to-automated-supply-chain-defense-with-npxconfuse) [Related 1](https://github.com/cybershaykh/npxconfuse) |
| 35.1 | Independent rediscovery | removed | [Bandwidth amplification with a factor of x783 caused by HTTP/2 → HTTP/1.1 translation in Cloudflare](https://habr.com/ru/articles/1063428/) |
| 34.8 | Insufficient evidence | removed | [A Billion-User Blast Radius: Owning ChatGPT's Secure Sandbox](https://appsecvillage.com/events/dc-2026/a-billion-user-blast-radius-owning-chatgpt-s-secure-sandbox-1248604) |
| 34.7 | Duplicate / already known | removed | [Cline Kanban WebSocket Hijack](https://www.oasis.security/blog/cline-kanban-websocket-hijack) [Related 1](https://www.oasis.security/blog/paperclip-agent-vulnerabilities) |
| 34.2 | Independent rediscovery | removed | [Ticket Tricking OpenSSL.org with Google Groups](https://spaceraccoon.dev/ticket-trick-openssl-google-groups/) |
| 34.0 | Useful application | removed | [Trailing-dot hostname normalisation in curl: IP-literal guard bypass to wildcard SAN match, and multi-dot HSTS bypass](https://hackerone.com/reports/3734921) [Related 1](https://hackerone.com/reports/3733984) |
| 33.0 | Duplicate / already known | removed | [DOMPurify mXSS via Re-Contextualization (CVE-2026-0540)](https://fluidattacks.com/advisories/daft) |
| 32.0 | Duplicate / already known | removed | [BioShocking AI: "Gaming" the AI Browser and Escaping its Guardrails](https://layerxsecurity.com/blog/bioshocking-ai-gaming-the-ai-browser-and-escaping-its-guardrails/) |
| 32.0 | Duplicate / already known | removed | [Dollar-Quote Bypass: Blind SQLi Against Regex-Sanitized Dynamic PL/pgSQL](https://jrbusiness.github.io/Dollar-Quote-Desync/) |
| 32.0 | Insufficient evidence | removed | [Pattern, Graph, Prompt: What Happens When You Layer Three Analysis Paradigms on the Same Codebase](https://appsecvillage.com/events/dc-2026/pattern-graph-prompt-what-happens-when-you-layer-three-analysis-paradigms-on-the-same-codebase-1223399) |
| 31.8 | Useful application | removed | [Duplicate chunked `Transfer-Encoding` smuggles a response across reused proxy connections in curl](https://hackerone.com/reports/3795615) [Related 1](https://hackerone.com/reports/3785919) |
| 31.8 | Insufficient evidence | removed | [The API Made Me Do It: Do Bad APIs Lead AI to Generate Vulnerable Code?](https://appsecvillage.com/events/dc-2026/the-api-made-me-do-it-do-bad-apis-lead-ai-to-generate-vulnerable-code-1248780) |
| 31.2 | Duplicate / already known | removed | [SSRF filter bypass via the RFC 8215 local-use NAT64 prefix `64:ff9b:1::/48`](https://hackerone.com/reports/3634400) |
| 30.5 | Insufficient evidence | removed | [CVE-2026-62899: .NET `System.Net.HttpListener` security-feature bypass via HTTP request/response smuggling](https://github.com/dotnet/announcements/issues/427) [Related 1](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62899) |
| 30.2 | Insufficient evidence | removed | [Nested APP Authentication — Undocumented Risk and Conditional Access Bypass](https://troopers.de/troopers26/talks/ezcteq/) |
| 30.2 | Duplicate or already known | removed | [Indirect Prompt Injection remains a fundamental security challenge for AI](https://brave.com/blog/indirect-prompt-injection/) |
| 30.0 | Insufficient evidence | removed | [Reflections on Disregarding Trust: Weaponizing CDP and MHTML for Header-Agnostic Session Hijacking](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Gregory%20Disney-Leugers%20-%20Reflections%20on%20Disregarding%20Trust%20%28Weaponizing%20CDP%20and%20MHTML%20for%20Header-Agnostic%20Session%20Hijacking%29%20-%201umberhac.pdf) |
| 29.8 | Insufficient evidence | removed | [Testing API Business Logic With AI Agents: What We Got Wrong First](https://www.bugbountydefcon.com/agenda-2026) |
| 27.5 | Insufficient evidence | removed | [GitHub scoped user-to-server tokens can escape their installation](https://hackerone.com/reports/3638909) [Related 1](https://hackerone.com/reports/3641229) |
| 26.8 | Duplicate / already known | removed | [curl HTTP/2 server push accepts a non-authoritative `:scheme=https` over cleartext h2c](https://hackerone.com/reports/3630310) [Related 1](https://hackerone.com/reports/3674275) |
| 24.7 | Duplicate or already known | removed | [Your WAF Doesn't Speak JSON: How the escaped solidus bypasses major WAFs](https://labs.trace37.com/blog/json-escape-waf-bypass/) |
| 24.7 | Independent rediscovery | removed | [HTTP Response Queue Poisoning via TOCTOU race in the Node.js HTTP agent](https://hackerone.com/reports/3582376) [Related 1](https://nodejs.org/en/blog/vulnerability/june-2026-security-releases) [Related 2](https://adventures.nodeland.dev/archive/cve-2026-48931-shouldnt-have-been-a-cve/) |
| 22.5 | Insufficient evidence | removed | [ROP for the Web: Smuggling XSS, SQLi and Web Shells Past Every WAF Using Compression Dictionaries](https://appsecvillage.com/events/dc-2026/rop-for-the-web-smuggling-xss-sqli-and-web-shells-past-every-waf-using-compression-dictionaries-1250560) |
| 15.5 | Insufficient evidence | removed | [The Hidden Cost of Sanitization: How Secure Parsing Can Introduce New XSS Attack Surfaces](https://nullcon.net/talk/the-hidden-cost-of-sanitization-how-secure-parsing-can-introduce-new-xss-attack-surfaces/) [Related 1](https://www.youtube.com/watch?v=BJCgSLGq308) |
| 14.8 | Insufficient evidence | removed | [Demystifying the (In)Security of OAuth-based Account Linking in Connector Ecosystems](https://sp2026.ieee-security.org/accepted-papers.html) |

## Archive publication follow-up — 9 September 2026

Eight original sources were preserved for six retained additions: eight Markdown documents and eight PDFs (five publisher originals and three rendered webpages). The pending Goja, Intigriti and Heyes PDFs were completed using Windows Docker Desktop after restarting its idle, unresponsive backend. Rendering used the pinned toolbox image with networking disabled and only a temporary working directory mounted; WSL paths were translated for the Windows Docker CLI. Rendering checks: containerized extraction confirms 19 pages for Goja, 12 for Intigriti and 3 for Heyes, with readable text through each document’s end. First-page previews were visually checked. The 43.6 MB Inti deck uses an exact GitHub Pages fallback registered in `website/hosting.json`. Independent capture/layout review is recorded in [review-gaps.md](../../archived-references/review-gaps.md).

The final list link check found 138 successful responses, no likely broken links, two unreachable hosts (PT SWARM and Zenodo), and one GitHub rate limit. It did not establish that the unreachable sources were dead; their captures were not replaced.

Validation: the judgement history verifies (245 events for 240 current 2026 candidates); all eight new archive titles/bylines/body-presence checks and five original-PDF hash comparisons pass. The five DEF CON migrations preserve their prior content/raw hashes and research bodies. Website refresh and smoke checks pass with 76 preliminary leads; Cloudflare and GitHub staging passed before the three pending PDFs were completed; the final website refresh passes with those additional copies, and all 76 preliminary entries now have PDF links. The smoke check exposed a pre-existing interface asset-version mismatch, corrected by aligning the HTML version tags. The repeated archive-wide `refs.py verify` reports the same 219 missing-store-object failures and one unreferenced-object warning; every missing hash was already recorded at HEAD, and none belongs to a new reference. Store-integrity gaps remain in the generated [store-gaps.md](../../archived-references/store-gaps.md), separately from document gaps. No deployment was published.

## Threshold and archive follow-up — 10 September 2026

The subsequent 55-point reconciliation supersedes the preceding sweep's 76-entry total: the current collection has 103 retained grouped entries. The 2021–2025 review also added five historical entries. See the [threshold review](../archive-reviews/2026-09-10-threshold-review.md), [store recovery evidence](../archive-reviews/2026-09-10-store-recovery.md), and [Top 10 PDF transcription review](../archive-reviews/2026-09-10-top10-pdf-review.md) for current results and remaining limitations. The older dated reports above remain as historical records.
