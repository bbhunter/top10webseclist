# Per-entry judgements

One block per candidate, ordered by score. Every entry was read in full, prior-art searched
against `archived-references/` by mechanism and against the open web, then scored with
[`score.py`](../../.claude/skills/webseclist-judge-reference/scripts/score.py). See
[README.md](README.md) for the method, the weights and the caveats.

**Kept** entries appear in [`2026-ai.md`](../../2026-ai.md). **Removed** entries appear only
here — this file is where their links are preserved.

Read *What was already known* as the load-bearing half. A high score means the work adds
something over that prior art; a low one means it mostly restates it, which is a statement
about marginal novelty and not about whether the writeup is worth reading.

---

## 79.3 — [Time for ACKrobatics: Abusing TCP Timestamps to Improve Remote Timing Attacks](https://i.blackhat.com/BH-USA-26/Presentations/USA-26-Vanderlinden-Time-for-ACKrobatics.pdf) — Vanderlinden, Vanhoef, Van Goethem

**KEPT** · Original technique · confidence High

**What is new.** Server execution time is read out of the server's own TCP timestamps, comparing TSval on the ACK against TSval on the response, so the measurement is jitter-free without needing request coalescing; plus runtime multiplication to inflate sub-granularity differences and a formal argument that it parallelises across hosts.

**What was already known.** Jitter-free remote timing via Timeless Timing Attacks (USENIX 2020) and Date/Server-Timing headers (2023-24); TCP timestamps were long used for uptime fingerprinting but not as a server-side runtime oracle. The new preconditions make it apply where the prior technique does not, at 5-33x finer resolution.

---

## 77.0 — [CSS: the bomb inside your inbox](https://portswigger.net/research/css-the-bomb-inside-your-inbox) [Whitepaper](https://i.blackhat.com/BH-USA-26/Presentations/BHUS26-Heyes-CSS-WP.pdf) [Slides](https://i.blackhat.com/BH-USA-26/Presentations/BHUS26-Heyes-CSS-Slides.pdf) [Code](https://github.com/portswigger/css-the-bomb-inside-your-inbox) — Gareth Heyes, PortSwigger

**KEPT** · Original technique · confidence Medium

**What is new.** Turning CSS injection from a read primitive into a control primitive inside sanitised HTML: label hijacking, CSS hotwiring (full-viewport pseudo-element stacking so any click fires a chosen action), CSS gadgets where an allow-listed attribute makes a third-party library inject properties outside the allow list, and CSSOM mutation, which is mXSS transposed to CSS and which I could not find described before.

**What was already known.** The exfiltration half is a dense lineage: attribute-selector leaking, font and ligature oracles, blind CSS exfiltration, and a CCS 2025 paper had already established scriptless CSS attacks on email clients specifically.

---

## 75.6 — [Cache Me, Catch You: Exploiting LLM Caching Layers in vLLM, GPTCache & Friends](https://i.blackhat.com/Asia-26/Presentations/BHAS26-Wu-Cache-Me-Catch-You.pdf) [Paper (NDSS 2026)](https://www.ndss-symposium.org/ndss-paper/cache-me-catch-you-cache-related-security-threats-in-llm-serving-frameworks/) [Code](https://github.com/XingTuLab/Cache_Me_Catch_You) — Wu, Ying, Chen, Gu, Qu

**KEPT** · Original technique · confidence Medium-High

*(Second re-check round, 8 August 2026.)*

**What is new.** Establishes the LLM inference cache layer — prefix/KV cache, semantic cache, multimodal cache — as a distinct attack surface where the security question is not "can the model be wrong" but "why is the cache allowed to decide two different inputs are the same request." Systematised into a six-path taxonomy with vendor-confirmed fixes and three CVEs; the load-bearing primitives are the prefix-cache block-wise non-crypto-hash KV collision (the model never "sees" the malicious block) and the multimodal image-byte-hash collision for moderation bypass.

**What was already known.** General cache poisoning and hash-collision-forced-equality are decades-old web concepts, transplanted here to a new domain; the concurrent, independent [From Similarity to Vulnerability (arXiv 2601.23088, Jan 2026)](https://arxiv.org/abs/2601.23088) covers only the semantic-cache fuzzy-collision path, not the prefix/multimodal primitives.

---

## 75.2 — [Transformers: Dark Side of the Type — Weaponizing the Conversion Layer](https://i.blackhat.com/BH-USA-26/Presentations/BHUS26-Mirosh-Transformers-Dark-Side-WP.pdf) [Slides](https://i.blackhat.com/BH-USA-26/Presentations/BHUS26-Mirosh-Transformers-Dark-Side-Slides.pdf) — Oleksandr Mirosh, OpenText Fortify

**KEPT** · Meaningful extension · confidence High

**What is new.** The reframing and the systematic map: a four-condition definition separating Insecure String Transformation from deserialization, a walk of every .NET string-to-object mechanism deciding which can resolve an attacker-chosen type, RCE with no serializer at the entry point, framework-assembly converter gadgets, four new SharePoint CVEs and grep-level detection rules.

**What was already known.** The individual primitives were enumerated by the same authors in 2017 (Friday the 13th, in archive), a resource-file TypeConverter RCE gadget was published in 2018 (in archive), and CVE-2020-1460 was published in 2020.

---

## 74.5 — [Get Set, Exploit! Unveiling Python Class Pollution In-the-Wild](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Gavin%20Zhong%2C%20Zhengyu%20Liu%2C%20Jianjia%20Yu%20-%20Get%20Set%2C%20Exploit%20Unveiling%20Python%20Class%20Pollution%20In-the-Wild%20-%20P.pdf) — Zhong, Liu, Yu, Johns Hopkins

**KEPT** · Meaningful extension · confidence High

**What is new.** The first taxonomy of Python class-pollution primitives (six get-set combinations, five never described before), a universal stdlib RCE gadget via an environment variable reaching a subprocess call, a static operational-taint detector existing source-to-sink tools structurally cannot express, and a 671,475-program measurement yielding 47 verified zero-days.

**What was already known.** The class itself (Abdulrah33m, Jan 2023, in archive), that it reaches RCE end-to-end (chilaxan, CVE-2024-5452, 2024), the Ruby analogue (Doyensec 2024), and automated pollution-gadget hunting from the JavaScript world.

---

## 74.2 — [Can AI do novel security research? Meet the HTTP Terminator](https://portswigger.net/research/can-ai-do-novel-security-research) [Whitepaper](https://portswigger.net/kb/papers/gkaicuremal/http-terminator.pdf) [Tool](https://github.com/portswigger/http-terminator) — James Kettle, PortSwigger

**KEPT** · Original technique · confidence High

**What is new.** Shared-Parser Confusion (response-only parsing rules misapplied to requests because parsers share code paths) is a class-level lens nobody had named, and the dangling-byte primitive removes the race from response queue poisoning. The spec-fragment-to-hypothesis-to-blackbox-oracle discovery loop is itself reusable and open-sourced.

**What was already known.** Desync/RQP as a class and differential fuzzing for parser discrepancies (T-Reqs, CCS 2021) were established; the new desync triggers are incremental additions to a corpus Kettle has published since 2019.

---

## 74.0 — [No Tools Required: Post-Injection Exploitation Across AI Agent Frameworks](https://i.blackhat.com/BH-USA-26/Presentations/BHUSA26-Porat-No-Tools-Required-REV01.pdf) — Yarden Porat & Shahar Tal, Check Point

**KEPT** · Original technique · confidence Medium

**What is new.** The LLM itself is used as the gadget injector: attacker-shaped tool-call arguments to a completely benign tool flow into the framework's own serializer, giving arbitrary class instantiation with attacker keyword arguments, environment disclosure by name, and subprocess RCE through an unallowlisted checkpoint decoder; plus a document pipeline landing in a C parser and an artifact keyspace collision overwriting the system prompt.

**What was already known.** Deserialization gadget chains, SSRF, arbitrary file read, indirect prompt injection and RAG loaders as an ingestion surface; the contribution is the bridge that post-injection exploitation needs no dangerous tool, only the harness plumbing.

---

## 74.0 — [One Chain to Own Them All: Breaking AI Infrastructures](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Ji%27an%20Zhou%2C%20Lei%20Lu%20-%20One%20Chain%20to%20Own%20Them%20All%20-%20Breaking%20AI%20Infrastructures%20-%20azraelxuemo%20v3.pdf) — Ji'an Zhou & Lei Lu

**KEPT** · Original technique · confidence Medium

**What is new.** A memory-safety attack on the allowlisted path itself: after the framework replaced bypassable logic with a strict function whitelist, the whitelisted primitives reachable from pickle item-setting give attacker-controlled index and value, producing heap corruption turned into RCE, paired with an error-message address leak to survive PIE.

**What was already known.** The logic-level bypass of the same boundary was the author's own earlier CVE, that pickle model files are dangerous at all, and that several inference servers expose model loading over HTTP; the re-targeting across five products is coverage, but the primitive voids the vendor's published security guarantee.

---

## 73.8 — [One Char to Rule Them All: DNS Silent Vulnerabilities in Domain Name Resolution](https://i.blackhat.com/Asia-26/Presentations/BHAS26-Miao-One-Char-to-Rule-The.pdf) — Miao, Li, An, Xu, Wang, Tsinghua

**KEPT** · Meaningful combination · confidence Medium-High

*(Second re-check round, 8 August 2026. Black Hat Asia 2026 / IEEE S&P 2026.)*

**What is new.** The first exhaustive measurement of how the full ASCII set (0x00–0x7F) is handled across 31 DNS implementations spanning every role (stub, forwarder, recursive, authoritative, library), isolating a "silent vulnerability" primitive: a single special character makes a component silently drop a query with no downstream response. That silencing is then weaponised four ways — enhancing 10 of 13 classic off-path cache-poisoning attacks, reviving TxID/port brute-force by widening the spoofing window, and load-balancing disruption / persistent SERVFAIL DoS.

**What was already known.** The RFC 1035 vs RFC 2181 character-set inconsistency is long known; escaped-character cache poisoning is prior lab work from the same research lineage (2021/2023); [Disablance (CCS 2023)](https://dl.acm.org/doi/10.1145/3576915.3616647) already did the load-balancing-disruption impact via a different trigger; TuDoor (S&P 2024) supplied the "systematically explore logic vulnerabilities" framing. Above the bar on the exhaustive character-handling map and the reusable silent-drop primitive; the downstream impacts largely re-derive known attacks. In scope via DNS cache poisoning's web-trust impact (traffic, certificate, CDN and email misdirection).

---

## 73.0 — [Pass-the-Passkey Family of Attacks](https://www.dsinternals.com/en/black-hat-usa-26-pass-the-passkey/) [Whitepaper](https://i.blackhat.com/BH-USA-26/Presentations/BHUS26-Grafnetter-Pass-the-Passkey-WP.pdf) [Slides](https://i.blackhat.com/BH-USA-26/Presentations/BHUS26-Grafnetter-Pass-the-Passkey-Slides.pdf) — Michael Grafnetter, SpecterOps

**KEPT** · Meaningful extension · confidence Medium

**What is new.** Windows writes the complete credential including the signature into an undocumented event log readable by any local user, the identity provider replaces stored challenges with stateless JWTs and tracked no signature counters so a logged assertion is a replayable bearer token satisfying phishing-resistant conditional access, and a hook substitutes the operator challenge to defeat even session-bound challenges.

**What was already known.** The general malware-hijacks-the-WebAuthn-call idea (SquareX, DEF CON 33, 2025), assertion redirection via client-side compromise (Toth 2025, in archive), passkey pre-registration as persistence, and the flag-stripping silent assertion, which the paper credits to 2020 work rather than claiming.

---

## 72.7 — [When Agentic Glue Melts: Exploiting Cloudflare Code Mode and Workers](https://research.checkpoint.com/2026/when-agentic-glue-melts/) [Slides](https://i.blackhat.com/BH-USA-26/Presentations/BUHUS26-Porat-When-Agentic-Glue-Melts-REV01.pdf) [PoCs](https://github.com/yardenporat353/WhenAgenticGlueMeltsPOCs) — Yarden Porat & Shahar Tal, Check Point

**KEPT** · Original technique · confidence Medium

**What is new.** That the hand-written native binding layer between JS and host APIs in a multi-tenant isolate runtime is an unexamined memory-corruption surface sitting outside both the sandbox cage and memory protection keys, so the vendor's layered defenses do not cover it, demonstrated with five bugs including a capture-group count mismatch between the parser and the regex compiler, chained to cross-tenant secret theft and host escape.

**What was already known.** V8 exploitation itself, the sandbox and MPK defenses documented in the vendor's own 2025 hardening post, and parser-differential reasoning as a bug-hunting shape.

---

## 71.8 — [Angular compromise through dev infra: GitHub Actions cache poisoning as a vulnerability class](https://adnanthekhan.com/posts/angular-compromise-through-dev-infra) [Clinejection](https://adnanthekhan.com/posts/clinejection/) [Copilot or Co-conspirator](https://adnanthekhan.com/posts/copilot-or-co-conspirator/) [Cacheract](https://github.com/AdnaneKhan/Cacheract) — Adnan Khan

**KEPT** · Meaningful extension · confidence Medium

**What is new.** Restore-key partial-match poisoning, weaponising the platform's switch to immediate eviction so a cache can be evicted and replaced inside a single run, imposter commit SHAs planted in bot-authored dependency PRs that maintainers pre-approve, and a TOCTOU where an issue is edited after assignment to an agent and reverted so the agent itself commits an attacker-triggerable workflow.

**What was already known.** Cache poisoning as a vulnerability class is the same author's own 2024 work, script injection from unsanitized branch names is standard, and prompt injection into CI-hosted agents leading to supply-chain compromise was published in 2025 (in archive).

---

## 71.8 — [Prompt Injection as Role Confusion (CoT Forgery)](https://role-confusion.github.io/) [Paper](https://arxiv.org/abs/2603.12277) — Ye, Cui, Hadfield-Menell, MIT

**KEPT** · Meaningful extension · confidence Medium

**What is new.** The mechanistic account: role probes showing perceived speaker role tracks writing style rather than the role tag, that injected text lands in the same representational space as the role it mimics, and that this predicts attack success before generation, with a causal ablation dropping success from 61 to 10 percent.

**What was already known.** That faking conversation turns and forging assistant reasoning defeats alignment was known (many-shot jailbreaking, prefill jailbreaks, H-CoT) as was the instruction-data separation failure; this explains why those work rather than discovering that they do.

---

## 71.0 — [Sub:jugation — Hijacking Cloud Identities by Recycling Namespaces in Global OIDC Issuers](https://astrix.security/learn/blog/subjugation-hijacking-cloud-identities-by-recycling-namespaces-in-global-oidc-issuers/) [Sleeper squats follow-up](https://labs.boostsecurity.io/articles/sleeper-squats-github-oidc-immutable-subject-claim) — Tal Skverer, Astrix

**KEPT** · Meaningful combination · confidence Medium

**What is new.** The recognition that multi-tenant CI platforms run a single global OIDC issuer whose subject claim is assembled from mutable recyclable paths, so a deleted namespace leaves a phantom cloud identity any third party can reclaim across the tenant boundary, with a working recon pipeline and measurement of how many live trust policies point at unregistered namespaces.

**What was already known.** Dangling-identifier takeover generally, and namespace reuse specifically as repojacking; the adaptation moves that pattern from package resolution to a federated identity trust boundary. The vendor redesigned the subject-claim format platform-wide, and the fix spawned follow-on research.

---

## 70.5 — [Hack the Source, Of the Source](https://i.blackhat.com/Asia-26/Presentations/BHAS26-Ng-Hack-the-Source-of-the-Source.pdf) [Born Corrupted](https://i.blackhat.com/BH-USA-26/Presentations/US-26-SplitlineNg-BornCorrupted-Thursday.pdf) — Tsi-Lin Ng & Splitline Ng, DEVCORE

**KEPT** · Original technique · confidence Medium

**What is new.** Several distinct registry-infrastructure primitives: a global manifest generated as executable source so an injected package name rewrites the download-URL table, with a numeric parsing differential making server and client read different manifests; a validator-versus-catalog archive-path differential letting an unprivileged upload poison another package's registration blob; and path traversal chained into argument injection in a registration service.

**What was already known.** The ingredients in isolation: argument injection into version-control binaries, archive path handling, and cross-job CI metadata trust. The closest prior work covers the shape of one finding but not its mechanism or the blob-write escalation.

---

## 70.0 — [Write Once, Shell Everywhere: Turning Arbitrary File Writes into RCE](https://ethiack.com/info-hub/research/write-once-shell-everywhere-arbitrary-file-writes-into-rce) — André Baptista, Rafael Castilho & Bruno Mendes, Ethiack

**KEPT** · Meaningful combination · confidence Medium

**What is new.** Four things beyond the catalogue: that a failed write is a path-probe oracle, because POSIX resolution stops at the first bad component so the errno names which one, built into a calibrated fingerprinting tree that reads runtime versions out of directory names; /proc/1/fd/255 (bash) or /fd/10 (dash) as a guess-free RCE destination, since a shell reads its script lazily from a held descriptor so a container entrypoint can be rewritten with no knowledge of its path; worker-pool entrypoints (Piscina, thread-stream, Tinypool, jest-worker) as restart-free Node sinks whose paths are pinned by the dependency rather than the application, defeating the require cache; and a Rails schema_cache.yml deserialization sink reached through YAML.unsafe_load.

**What was already known.** The catalogue itself is coverage, not discovery: ld.so.preload, cron, .pth, .user.ini, Bootsnap, web.config and template caches are all in HackTricks, GTFOBins and Doyensec 2023 (in archive). The Rails item points a 2018-era universal gadget at a newly-named sink, and the bash lazy-read behaviour has been documented as an operational footgun since 2019. Notably the oracle answers the black-box version-guessing problem that the archived Conviso and siunam techniques both explicitly leave open.

---

## 70.0 — [The CoreBreak Attack: Turning AI Agents into Credentials Exfiltration Vectors](https://i.blackhat.com/BH-USA-26/Presentations/CoreBreak_BlackHat2026_FINAL.pdf) — Hedi Ingber & Aviyam Ivgi

**KEPT** · Meaningful combination · confidence Medium

*(Second re-check round, 8 August 2026. Borderline — exactly at the ≥ 70 core threshold; kept regardless under the ≥ 60 keep-cut.)*

**What is new.** Direct tool invocation: the agent-SDK harness (Strands, Google ADK, Vercel AI SDK) executes a tool-call block that is the most-recent input message with no model call in between — "one elif skips the model" — so the infrastructure never verifies that a model turn authorized the tool call. The attacker picks the tool and arguments outright, bypassing every model-level guardrail. This is the antithesis of indirect prompt injection ("don't inject the prompt"), validated by accepted CVEs from two major cloud vendors (CVE-2026-18830 AgentCore/Strands, CVE-2026-18236 Google ADK) and generalising across SDKs.

**What was already known.** The IMDS/MMDS credential-theft half is credited to Nigel Sood (Sonrai) and AWS rules it by-design (the microVM is the trust boundary); the Vercel direct-invocation instance had been flagged earlier by Anthropic's Mythos "Project Glasswing" internal pen-test. Nearest kept peer is [No Tools Required (74.0)](https://i.blackhat.com/BH-USA-26/Presentations/BHUSA26-Porat-No-Tools-Required-REV01.pdf) — same "the vuln is the SDK harness plumbing, not a dangerous tool" family, but a distinct mechanism (serializer gadgets *through* the model vs. CoreBreak *skipping* it). The multi-vendor accepted CVEs defuse the "just a relabel of confused-deputy" risk that sank Novee's trust-handoff writeup (52.5).

---

## 69.8 — [Poisoning Claude Code: One GitHub Issue to Break the Supply Chain](https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/) — RyotaK, GMO Flatt Security

**KEPT** · Meaningful combination · confidence Medium

**What is new.** The authorization insight: the permission check let any GitHub App through unconditionally, and because anyone can create an App and use its token to file issues on any public repo, actor-is-a-bot turns out to be an identity anyone can mint rather than a privilege signal, chained through injection to an OIDC exchange minting a write-capable token.

**What was already known.** Prompt injection into agents running in CI, reading secrets from the process environment, and Actions supply-chain propagation are all already in this archive, and the author notes misconfiguration variants were exploited in the wild before publication.

---

## 69.5 — [Two Bypasses for Chrome's Sanitizer API](https://slcyber.io/research-center/two-bypasses-for-chromes-sanitizer-api/) — Adam Kues, Searchlight Cyber

**KEPT** · Original technique · confidence Medium

**What is new.** The URL-reparsing differential: a URL the full parser rejects as invalid passes the sanitizer's cheap protocol check, and Chrome re-serialization on form submission mutates it into a valid executing javascript URL. The generalised lesson is reusable against a brand-new browser security boundary.

**What was already known.** SVG animate as an href-mutation XSS vector, javascript URLs with comment padding, and the sanitizer-bypass-by-parsing-differential genre; the first bypass is a string-comparison bug of modest depth.

---

## 69.2 — [HashDoS in V8's array-index string hash, and a seeded but invertible permutation as the fix](https://hackerone.com/reports/3511792) [Writeup](https://nodejs.org/en/blog/vulnerability/march-2026-hashdos) — Mate Marjanović; fix by Joyee Cheung

**KEPT** · Meaningful extension · confidence Medium

**What is new.** V8 deliberately exempted one hash path from seeding to keep it reversible, and at realistic table capacities the length bits are masked away so the hash equals the numeric value, making any JSON.parse endpoint a collision oracle. The fix contributes a reusable invertible seeded-permutation design.

**What was already known.** HashDoS since 2003, JS-engine hash flooding since 2011, and a same-codebase precursor eight months earlier (CVE-2025-27209, unseeded rapidhash constants) cited by the fix writeup itself.

---

## 68.8 — [Are your Sites Truly Isolated? Automatically Detecting Logic Bugs in Site Isolation Implementations](https://www.ndss-symposium.org/wp-content/uploads/2026-f902-paper.pdf) [Slides](https://www.ndss-symposium.org/wp-content/uploads/f0902-drescher-slides.pdf) — Drescher, Klein, Johns

**KEPT** · Tooling / methodology · confidence High

**What is new.** Two oracles for a bug class ASan cannot see, a leak sanitizer for victim-secret reachability and a process sanitizer for process-reuse bugs that leak nothing but stay Spectre-exploitable, plus the insight that renderer compromise can be simulated by mutating IPC. Fuzzer released, four vendor-confirmed bugs.

**What was already known.** Browser semantic-bug fuzzing with state-based oracles (FuzzOrigin, CorbFuzz) and browser IPC fuzzing for memory bugs; this extends a populated line into a new bug class rather than opening one.

---

## 68.8 — [Finding Gadgets Like it's 2026](https://www.atredis.com/blog/2026/3/12/findings-gadgets-like-its-2026) [Tool](https://github.com/atredispartners/llmchainhunter) — Stephen Breen, Atredis Partners

**KEPT** · Tooling / methodology · confidence Medium

**What is new.** A shaded copy of Xalan inside an application JAR sits outside the java.xml module, so JPMS no longer blocks bytecode-loading RCE on JDK 21, generalising to the idea that dependency shading erases a module boundary, plus a new toString trigger and CC4 entry points surviving CC 4.5.0.

**What was already known.** Automated gadget-chain discovery over a pruned call graph including LLM-driven variants (GadgetInspector 2018; GadgetHunter FSE 2026), shaded Xalan already on jackson-databind blocklists, and the authors found one new chain had been published by Synacktiv in 2022.

---

## 67.8 — [Alias Equals Zone? Large-Scale and Stealthy Takeover of Domain Hosting Service via CNAME-Following Cross-Domain Verification](https://www.usenix.org/conference/usenixsecurity26/presentation/li-ruixuan) — Ruixuan Li et al.

**KEPT** · Meaningful extension · confidence Medium

**What is new.** That hosting providers resolve ownership-challenge records through live CNAME chains, so a record placed at the chain's target validates an alias domain that never configured a token: takeover without any dangling resource, across eleven providers and two million domains.

**What was already known.** That DNS-based ownership proofs break when resolution is delegated is understood in the certificate-issuance context, and domain and subdomain takeover via DNS trust is well covered; the marginal contribution is showing hosting and email onboarding inherit that resolver behaviour at scale.

---

## 67.5 — [CRLF-Powered Desync Attacks: Beheading HTTP Streams](https://portswigger.net/research/crlf-powered-desync-attacks) [Author's post](https://thomas.stacey.se/posts/CRLF-Powered-Desync-Attacks/) [Slides](https://i.blackhat.com/BH-USA-26/Presentations/US-26-Stacey-CRLF-Powered-Desync-Attacks-Wed.pdf) [Scanner](https://github.com/t0xodile/crlf-powered-desync-scanner) — Tom Stacey & Tobia Righi

**KEPT** · Meaningful combination · confidence High

**What is new.** Using an upstream CRLF-injection point as the source of the malformation lets a victim's ordinary browser request produce a desync, lifting the IP- and connection-lock preconditions that normally block exploitation.

**What was already known.** Both halves were public: CRLF response splitting (Klein 2004), header injection escalated to response queue poisoning (Kettle 2022), browser-reachable desync (Kettle 2022), and nginx proxy_pass splitting with browser-delivered payloads (Bobrov, OFFZONE 2023, in the local archive).

---

## 67.5 — [ChatMate: Remote Prompt Execution on AI Assistants through Sandbox Escaping](https://i.blackhat.com/BH-USA-26/Presentations/BHUS26-Lahav-ChatMate-Slides.pdf) — Ori Lahav, Rubrik Zero Labs

**KEPT** · Meaningful combination · confidence Medium

*(Second re-check round, 8 August 2026. In the 60–69.9 supporting band — kept under the ≥ 60 keep-cut, below the ≥ 70 core tier.)*

**What is new.** The first demonstrated escape of a *managed* AI-assistant code sandbox — Microsoft Copilot on Azure Dynamic Sessions / Container Apps / AKS — up to root on the host node: a real 0-day chain of missing auth on an internal host-network containerd config service → path traversal → `hosts.toml` `.toml` injection → an `/etc/ld.so.preload` backdoor. CVE-2026-32193, $48k bounty.

**What was already known.** Each primitive is a classic container-escape building block applied to a new target, and the headline "Remote Prompt Execution" class is impact/demo framing (an interactive C2 into the victim's live session *after* full host compromise), not a new mechanism. Kept peers with genuinely novel escape primitives sit at 72–74 (One Chain to Own Them All's heap corruption on the allowlisted path; When Agentic Glue Melts' native-binding memory-corruption surface); ChatMate uses known primitives, so it lands a notch below them.

---

## 67.2 — [Path traversal in signed URLs — present even in the official AWS SDKs](https://blog.flatt.tech/entry/signed_url_path_traversal) — ryotaromosao & Eui Chul Chung, GMO Flatt Security

**KEPT** · Meaningful extension · confidence Medium

**What is new.** That the act of signing can itself defeat the authorization it provides: the signer normalises the path while the object store treats keys as opaque, so a traversal in user input yields a valid signature for a different object and prefix-based tenant isolation collapses, inside the official SDKs.

**What was already known.** The parent class, path-normalization differentials between two layers (Orange Tsai 2018, in archive), and that concatenating user input into an object key is dangerous; this relocates the class into the signing layer.

---

## 67.0 — [Borrowing Windows Hello Keys for Authentication and Persistence](https://dirkjanm.io/borrowing-windows-hello-keys/) — Dirk-jan Mollema

**KEPT** · Meaningful extension · confidence High

**What is new.** Treating the platform key as a FIDO2 passkey over WebAuthn, which drops the previously-required registered device and yields tokens with no device-ID claim, plus a reverse-engineered deterministic user-handle derivation and a fake-device-registration persistence chain, shipped in tooling.

**What was already known.** The author's own DEF CON 32 talk (Aug 2024) already covered invoking the keys from a user session with no PIN prompt, signing the assertion, requesting a refresh token, and proxying assertions to a compromised host.

---

## 66.8 — [Remote Command Execution in Google Cloud with Single Directory Deletion](https://flatt.tech/research/posts/remote-command-execution-in-google-cloud-with-single-directory-deletion/) — RyotaK, GMO Flatt Security

**KEPT** · Meaningful combination · confidence Medium

**What is new.** Treating a recursive delete as an exploitable temporal window: the walk is post-order and non-atomic, so the git directory can be gone while attacker-planted files remain, and the deletion order is steerable by choosing names that exploit deterministic filesystem ordering.

**What was already known.** The payload half is entirely known: a git config monitor hook as an arbitrary-command sink is well-worn across several 2026 CVEs, as is TOCTOU racing of cleanup routines.

---

## 66.5 — [AutoFail: Breaking Web Boundaries using Android's Autofill Framework](https://github.com/SecPriv/autofail) — Lamarca, Beer, Squarcina, TU Wien

**KEPT** · Meaningful combination · confidence Medium

**What is new.** Relocating the boundary to the per-browser DOM-to-ViewStructure translation, evidenced by an asymmetry only a multi-browser method could find: the embedder-harvests-credentials direction reproduces in Firefox and nowhere else. Plus a modern web-isolation corpus (sandboxed and COEP credentialless iframes, object and embed), a silent no-permission Cross-Context Account Oracle that enumerates which services a victim holds accounts on, and the first quantification of exposure at 59 percent of the top million embeddable.

**What was already known.** More than the abstract implies. ACSAC 2021 already published that Android autofill does not prevent cross-origin iframe fill, with a 14-manager table, but held the browser constant so it could not see the translation divergence. CCS 2018 established gameable app-to-domain trust, and AutoSpill (CODASPY 2023) covered origin confusion for web content inside native view structures. Two of the three headline outcomes are broadenings rather than discoveries.

---

## 66.0 — [Agentic Browsers and the Same-Origin Policy](https://agent-security.cs.washington.edu/agentic_browsers_sop.html) [PDF](https://www.franziroesner.com/pdf/roesner_kohlbrenner_2026_agentic_sop.pdf) [Code](https://github.com/UWCSESecurityLab/agentic-browser-sop) — Roesner & Kohlbrenner, UW

**KEPT** · Tooling / methodology · confidence High

**What is new.** A systematic released test suite and an 8-configuration capability matrix turning a hand-wavy worry into per-browser evidence, plus a working cross-origin theft PoC.

**What was already known.** The central claim, that a prompt-injectable agent with cross-origin reach reduces the same-origin policy to the model's injection robustness, was stated almost verbatim by Brave a year earlier; the paper's own related work concedes the issue has been identified at a high level.

---

## 65.6 — [Your WAF Blocked Us, That Was The Exploit — Remote Agent Takeover via Cloudflare, Sentry and Claude Zero-Day](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Barak%20Sternberg%2C%20Nevo%20Poran%2C%20Ron%20Bobrov%20-%20Your%20WAF%20Blocked%20Us%2C%20That%20Was%20The%20Exploit%20-%20Remote%20Agent%20Takeover%20via%20Cloudflare%2C%20Sentry%20and%20C.pdf) [Agentjacking](https://tenetsecurity.ai/blog/agentjacking-coding-agents-with-fake-sentry-errors/) — Sternberg, Poran, Bobrov, Tenet Security

**KEPT** · Meaningful combination · confidence High

**What is new.** Public write-only telemetry credentials and WAF block logs as unauthenticated zero-victim-contact injection channels, where being blocked is itself the delivery, plus laundering the injection through the vendor's own analysis agent so the coding agent never sees the raw payload.

**What was already known.** Indirect prompt injection (2023), untrusted-data-in-a-trusted-source reaching tool abuse and the read-plus-write same-session condition (Invariant 2025), log-field injection reaching AI SOC agents (Sep 2025), agent-to-agent propagation (Morris II 2024), and config poisoning.

---

## 65.5 — [Hacking Your Life with AI Can Get You Hacked: How AI Orchestration Platforms Ship RCE by Design](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Peyton%20Kennedy%20-%20Hacking%20Your%20Life%20with%20AI%20Can%20Get%20You%20Hacked%20How%20AI%20Orchestration%20Platforms%20Ship%20RCE%20by%20Design%20-%20V1.pdf) — Peyton Kennedy, Endor Labs

**KEPT** · Meaningful combination · confidence Medium

**What is new.** A four-stage taxonomy across seven platforms and thirteen findings, the observation that a real isolation primitive applied at a later phase is worthless when attacker code runs in bootstrap, and the demonstration that a regex import-blocklist cannot constrain an executor that pre-imports data libraries.

**What was already known.** Each individual bug is a classic class, LLM-output-equals-user-input is settled 2023-era doctrine, and the sandbox escape is precisely the endowment-leak obligation that the sandbox's own documentation and prior analyses already name as the primary risk.

---

## 65.5 — [Stealing GitHub tokens via VS Code webview keyboard event bubbling](https://blog.ammaraskar.com/github-token-stealing/) — Ammar Askar

**KEPT** · Meaningful extension · confidence High

**What is new.** The primitive that a sandbox boundary forwarding raw keydown events rather than explicit intents silently restores the privilege it was meant to remove, because event trust does not survive a postMessage relay, so any webview XSS becomes arbitrary command execution.

**What was already known.** Webview XSS in VS Code and escalation to RCE (STAR Labs 2025, Doyensec 2022), synthetic-event abuse generally, and the workspace-trust keybinding gap. The demonstrated chain works only on github.dev.

---

## 64.8 — [One trigram at a time: XSLeak via Universal CSS Injection and DoS in Opera (GX)](<https://zhero-web-sec.github.io/research-and-things/one-trigram-at-a-time-xsleak-via-universal-css-injection-and-dos-in-opera-(gx)>) — zhero; & inzo\_

**KEPT** · Meaningful combination · confidence Medium

**What is new.** Exfiltrating an arbitrary-length string from a single static stylesheet with no server feedback loop, via pre-generated trigram rules bound to distinct CSS variables and an overlap-based DFS reassembly.

**What was already known.** The Opera GX silent extension install (Renwa 2023), attribute-selector substring leaking, and the Heyes CSS-variable trick to avoid cascade collisions; the vulnerability half is a vendor bug on a previously-reported unfixed primitive.

---

## 64.8 — [Zero Knowledge (About) Encryption: A Comparative Security Analysis of Three Cloud-based Password Managers](https://eprint.iacr.org/2026/058) — Scarlata, Torrisi, Backendal, Paterson

**KEPT** · Meaningful extension · confidence Medium

**What is new.** The first rigorous comparative cryptanalysis of cloud password managers under a fully malicious server model, 25 attacks across three products, plus an extracted taxonomy of recurring end-to-end-encryption anti-patterns that transfers to any such web application.

**What was already known.** That vendor zero-knowledge marketing collapses against a malicious server is the established finding of this group's own prior line, and earlier analyses had surfaced concrete crypto weaknesses in these products under weaker threat models.

---

## 64.2 — [Cast Attack: A New Threat Posed by Ghost Bits in Java](https://i.blackhat.com/Asia-26/Presentations/Asia-26-Bai-Cast-Attack-Ghost-Bits-4.23.pdf) — Bai, Chen, Zheng

**KEPT** · Meaningful extension · confidence Medium

**What is new.** Systematising the Java 16-bit char to 8-bit byte collapse as a general parser-differential primitive with a sink inventory and a scanner, plus the separate observation that optimised hex decoders force non-hex characters into valid hex digits.

**What was already known.** The frame itself, a lossy character-to-byte transformation that validator and consumer disagree about, weaponised for filter bypass and traversal: WorstFit did exactly this for Windows ANSI a year earlier and is already on the 2024 list; Unicode-normalisation WAF bypass and SMTP injection via recipient address are also prior.

---

## 62.8 — [Privacy risks of agentic oversharing on the Web (SPILLAGE)](https://brave.com/blog/agentic-oversharing/) — Ali Shahin Shamsabadi, Brave

**KEPT** · Meaningful extension · confidence Medium

**What is new.** The second axis: prior agent-privacy work measured what the agent types, while this adds the behavioural channel, leakage inferable from clicks, scrolls and navigation path, reported dominating content leakage roughly fivefold, plus the counter-intuitive result that stripping task-irrelevant data raises task success.

**What was already known.** That web agents over-use sensitive data and that simple privacy prompting does not fix it were established by a data-minimisation benchmark a year earlier; live-site evaluation is a methodological improvement, not a new problem.

---

## 62.6 — [Codex Discovered a Hidden HTTP/2 Bomb](https://blog.calif.io/p/codex-discovered-a-hidden-http2-bomb) — Quang Luong, Jun Rong, Duc Phan, Calif

**KEPT** · Meaningful combination · confidence High

**What is new.** The principle that a compression amplifier is only a DoS when paired with a hold primitive, realised by pinning HPACK bookkeeping amplification with a zero-byte flow-control window, demonstrated across five implementations.

**What was already known.** Both halves: the HPACK bomb (Benfield, CVE-2016-6581, 2016), the per-entry-bookkeeping variant (entry 7, explicitly credited), and HTTP/2 slow-read stalling (CVE-2016-1546).

---

## 62.5 — [LGTM: Bypassing an LLM Build Gate When Prompt Injection Fails](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Aviv%20Donenfeld%20-%20LGTM%20Bypassing%20an%20LLM%20Build%20Gate%20When%20Prompt%20Injection%20Fails%20-%20LGMT%20v2.pdf) — Aviv Donenfeld

**KEPT** · Meaningful combination · confidence Medium

**What is new.** The failure mode demonstrated against a production LLM gate: after direct hiding and prompt injection were caught, the working bypass carried no attack in the diff at all, just one added dependency coordinate whose artifact contents the model cannot fetch, plus decision-boundary measurement showing the gate is probabilistic.

**What was already known.** Both halves separately: dependency confusion as a build-time execution vector, and that LLM reviewers are bypassable. The structural claim that scanning artifacts an analyzer cannot see is unsound was published two months earlier.

---

## 62.5 — [Parse and Parse: MIME Validation Bypass to XSS via Parser Differential](https://lab.ctbb.show/research/parse-and-parse-mime-validation-bypass-to-xss-via-parser-differential) — Tang Cheuk Hei (siunam)

**KEPT** · Meaningful extension · confidence High

**What is new.** An empirical taxonomy of 23 server-side Content-Type parsers sorted into four behaviour classes, with tailored payloads defeating the stricter ones including a Chromium comment trick.

**What was already known.** Cited by the author: BlackFan content-type-research already documents the multiple-Content-Type trick and flags Chrome and Firefox, so the load-bearing browser behaviour is not this work's discovery.

---

## 62.2 — [FCSC 2026 writeups: Firefox `execCommand` ICU-vs-JS case-folding differential, Gunicorn `HEAd` smuggling, libmagic polyglots](https://web.archive.org/web/20260418230027/https://mizu.re/post/fcsc-2026-writeups) — Kévin Mizu *(live host down; the post's own frontmatter date is a copy-paste error — FCSC 2026 ran April 2026)*

**KEPT** · Meaningful combination · confidence Medium

**What is new.** Several small reusable primitives: an execCommand denylist bypass via ICU versus JS case-folding of a dotted capital I, Angular matrix-param segments letting a CSPT survive a traversal-blocking proxy, a libmagic encoding-max parameter hiding a JSON header behind padding, and JSDOM attribute-serialization mXSS.

**What was already known.** The underlying classes are all known, including Unicode case-folding filter bypasses (the author calls the Kelvin-sign trick well-known), CSPT, magic-byte polyglots and mXSS on non-browser serializers; the Gunicorn half reuses publicly-known 21.2.0 bugs.

---

## 62.0 — [wp2shell: Pre-Authentication RCE in WordPress Core](https://slcyber.io/research-center/wp2shell-pre-authentication-rce-in-wordpress-core/) [Discovery methodology](https://slcyber.io/research-center/exploit-brokers-pay-500000-for-a-wordpress-rce-i-found-one-with-gpt5-6/) [Escalation to root](https://blog.calif.io/p/the-wordpress-chain-massacre) — Adam Kues, Searchlight Cyber

**KEPT** · Meaningful combination · confidence Medium

**What is new.** The batch-endpoint desync: validation and dispatch run over two parallel arrays, and an unparseable sub-request offsets them permanently so a later sub-request executes under a different request's verdict. An index-desync idea worth carrying to any multiplexed API.

**What was already known.** The second half is a textbook string-vs-array sanitization skip, the admin escalation is standard WordPress post-exploitation, and the cited primary source deliberately withholds all technical detail.

---

## 61.5 — [Deployment Poisoning: A(nother) Novel Attack Vector for GitHub Actions](https://labs.boostsecurity.io/articles/deployment_poisoning) — Sébastien Graveline, Boost Security Labs

**KEPT** · Meaningful extension · confidence Medium

**What is new.** A previously uncatalogued source of untrusted input: a fork PR naming a nonexistent environment causes the platform to auto-create it in the base repo, emitting an event that fires the base repo's workflow in default-branch context with secrets, with the attacker-chosen name as the injection sink.

**What was already known.** The surrounding class is thoroughly documented by vendor and third-party research, and the author concedes the auto-creation behaviour surfaced in a January 2024 community discussion.

---

## 61.2 — [Token Time Bomb: Evaluating JWT Implementations for Vulnerability Discovery](https://www.ndss-symposium.org/wp-content/uploads/2026-f697-paper.pdf) [Slides](https://www.ndss-symposium.org/wp-content/uploads/f0697-yang-slides.pdf) — Yang, Wang, Chen et al.

**KEPT** · Tooling / methodology · confidence High

**What is new.** A grammar for the whole JOSE space driving a differential analyzer with parsing-discrepancy and resource-exhaustion oracles, plus the first cross-language evaluation of 43 libraries in 10 languages and mitigations the IETF said it would fold into a new BCP.

**What was already known.** Four of the five attack categories are prior art, restating Tervoort's three 2023 attacks, algorithm confusion from 2015, and a long-flagged compression footgun; grammar-based differential fuzzing is an established playbook. The paper cites both.

---

## 60.8 — [Smashing the ServiceNow Sandbox – Pre-Authentication RCE](https://slcyber.io/research-center/smashing-the-servicenow-sandbox-pre-authentication-rce/) — Adam Kues, Searchlight Cyber

**KEPT** · Meaningful extension · confidence Medium

**What is new.** The escape primitive: because the inner sandbox and the unsandboxed loader share one mutable global scope, clobbering a property definer to swap a clone helper for Function makes a later include evaluate attacker source outside the sandbox. A reusable write-a-global-from-inside-the-jail pattern.

**What was already known.** Rhino and SaaS sandbox escapes generally, ServiceNow sandbox escapes specifically, and the underlying shape of polluting shared state so a privileged gadget executes it.

---

## 60.5 — [Your House Has an FFmpeg Problem](https://www.elttam.com/blog/your-house-has-an-ffmpeg-problem) — Jia Hao Poh, elttam

**KEPT** · Meaningful extension · confidence Medium

**What is new.** The header-synthesis trick: scan an arbitrary on-disk binary for byte sequences forming a valid container header, splice them as a chain of subfile slices, then append the target path, turning must-be-valid-audio from a blocker into a bypass.

**What was already known.** Arbitrary file read through the ffmpeg concat and subfile pseudo-protocols has been public since CVE-2016-1897, argument injection into an ffmpeg parameter is standard, and the Home Assistant pre-auth surface was the same team's earlier work.

---

## 60.5 — [A First Measurement Study on Authentication Security in Real-World Remote MCP Servers](https://arxiv.org/abs/2605.22333) — Zhou, Zhang, Zhang, Zhang, Zhang, Yang, Fudan

**KEPT** · Tooling / methodology · confidence Medium

**What is new.** The OAuth layer specifically: a nine-type taxonomy of authentication flaws with dynamic client registration flaws in 96.6 percent of tested OAuth-enabled servers, a semi-automated framework, and nine disclosed CVEs.

**What was already known.** The headline that a large share of exposed servers have no authentication at all was published a year earlier by a smaller scan, so that figure is confirmation at larger scale rather than discovery.

---

## 59.8 — [Almost Impossible Java Deserialization Through Broken Crypto in OpenText Directory Services](https://slcyber.io/research-center/almost-impossible-java-deserialization-through-broken-crypto-in-opentext-directory-services/) — Pindur, Kues, Williamson

**REMOVED** · Meaningful combination · confidence Medium

**What is new.** The delivery primitive: a hand-built Deflate stream whose canonical Huffman codes emit only ASCII bytes, keeping bit alignment and deliberately incompressible so zlib stores rather than compresses, letting a ysoserial payload survive a character-constrained channel.

**What was already known.** HMAC over content with attacker-controlled length prefixes excluded is a textbook canonicalisation flaw, alphabet-constrained Deflate has existed as a tool since 2014 (ascii-zip, behind Rosetta Flash, in archive and cited by the candidate), and the gadget chain is stock ysoserial.

---

## 59.5 — [Avoiding the paradox: A native full-read SSRF and one-shot DoS in SvelteKit](https://zhero-web-sec.github.io/research-and-things/avoiding-the-paradox-a-native-full-read-ssrf-and-oneshot-dos-in-sveltekit) — zhero; & inzo\_

**REMOVED** · Meaningful extension · confidence High

**What is new.** Escaping the execution paradox by routing through the internal remote endpoint so a private header rewrites the pathname, then URL-encoding one character so the decoded and raw paths diverge, reaching a server-side fetch against a Host-derived origin.

**What was already known.** The class, an SSR framework trusting its own internal headers plus a Host-derived origin, is established largely by these same authors (Next.js internal-header work 2024, in archive; CVE-2025-29927).

---

## 59.2 — [HTTP/2 WAF Bypass: A Black-Box Methodology (h2 framing)](https://lab.ctbb.show/research/h2-WAF-Bypasses) — Diyan Apostolov

**REMOVED** · Meaningful combination · confidence Medium

**What is new.** The architectural insight that where the WAF sits relative to frame assembly decides what it can see: an out-of-process hook fires on HEADERS and reads an empty body because the DATA frame has not arrived. Plus Extended CONNECT to GET conversion defeating method ACLs.

**What was already known.** H2-to-H1 translation as an attack surface (Kettle 2021, Frameshifter 2022, h2c smuggling 2020), body-size inspection limits, and HAProxy documented multiplexer behaviour. The writeup cites no prior art and re-presents some as findings.

---

## 59.2 — [Claude in Chrome: from alert(1) to full account takeover](https://labs.zenity.io/post/claude-in-chrome-from-alert-to-full-account-takeover) [Technical deep dive](https://labs.zenity.io/post/account-takeover-via-claude-in-chrome-a-technical-deep-dive) — Onitza-Klugman, Donato, Cohen, Zenity Labs

**REMOVED** · Useful application · confidence Medium

**What is new.** One evasion primitive: hiding the payload behind an import from an attacker-run lookalike CDN so the agent never reads the code it is about to execute, a reusable way to defeat model-level review of agent-executed code.

**What was already known.** The whole spine is known: email-delivered indirect injection, an agent script tool amounting to universal XSS in an authenticated session, and an unauthenticated feed as a token oracle. The vendor treated it as known-by-design and marked the report ineligible.

---

## 59.1 — [Grand Theft Atlas (PleaseFix + Intent Collision)](https://labs.zenity.io/post/grand-theft-atlas) [PerplexedBrowser](https://labs.zenity.io/p/perplexedbrowser-perplexity-s-agent-browser-can-leak-your-personal-pc-local-files) [Class hub](https://zenity.io/research/pleasefix-vulnerabilities) — Stav Cohen, Michael Bargury et al., Zenity Labs

**REMOVED** · Meaningful combination · confidence Medium

**What is new.** The intent-collision framing plus concrete evasions against intent-based gates, and above all delegating a code-blocked action to a second agent to route around a deterministic boundary that held. Agent-to-agent delegation as a boundary bypass is the durable idea.

**What was already known.** Indirect prompt injection in agentic browsers with cross-origin reach and hidden-instruction obfuscation, including the same team's own earlier post which already named intent collision, and Brave's series from August 2025.

---

## 59.1 — [Computer-Use and TOCTOU: What You Click Is Not What You Get!](https://embracethered.com/blog/posts/2026/toctou-agent-what-you-click-is-not-what-you-get/) — Johann Rehberger

**REMOVED** · Meaningful extension · confidence High

**What is new.** Turning a flaky screenshot-versus-action race into a reliable one by deliberately widening the window with an injected stalling task, plus an end-to-end sink using a deeplink to pre-draft a message so one click at a known coordinate sends it.

**What was already known.** The core mechanism, that a screenshot-then-click agent can be made to click something other than what it saw, was publicly disclosed against a major agent a year earlier and is cited by the author; UI redressing and TOCTOU are decades old.

---

## 59.0 — [Cruising for Shells in Flowise](https://www.elttam.com/blog/cruising-for-shells-in-flowise) — Brown, Jahnke, Poh, elttam

**REMOVED** · Meaningful combination · confidence High

**What is new.** Two primitives look genuinely new: choosing a 13-byte table name so the SQLite record header serialises as a quote byte, smuggling a quote past an alphanumeric-only regex, which generalises to other length-prefixed formats; and a config-sourcing behaviour as an exec sink for an arbitrary file write.

**What was already known.** The other four chains are competent re-application: a vm2 escape via an allowlisted dependency, pandas pickle reading past a denylist, TypeORM as a code loader, and the authors' own 2020 environment-variable trick.

---

## 59.0 — [Security Considerations on Namespace-Based Multi-Tenancy (Istio VirtualService MITM)](https://istio.io/latest/blog/2026/security-considerations-on-namespace-based-multi-tenancy/) [Weaponized against Kubeflow](https://insinuator.net/2026/05/cve-2026-47237-overly-permissive-istio-permissions-allow-kubeflow-authorization-token-stealing/) — Lehawany & Nobis, ERNW

**REMOVED** · Meaningful extension · confidence Medium

**What is new.** A real transferable idea: the networking CRDs predate namespace RBAC, so a route with mesh-wide blast radius is guarded by namespace-scoped RBAC, letting a tenant claim arbitrary hostnames and MITM other namespaces despite mTLS, proven end-to-end by stealing bearer tokens.

**What was already known.** The underlying class, namespace-scoped RBAC guarding cluster-wide-effect config, is established from ingress-controller research; the cross-namespace behaviour was filed upstream in 2022 and a mitigation setting already existed.

---

## 59.0 — [The Memory Heist](https://www.ayush.digital/blog/the-memory-heist) [Independent Tencent Zhuque analysis](https://security.tencent.com/index.php/blog/msg/225) — Ayush Paul; Tencent Zhuque Lab

**REMOVED** · Meaningful extension · confidence Medium

**What is new.** The channel: where the defence was that the agent may only follow links it found and never construct URLs, the attacker page supplies a pre-built alphabetic link tree so each navigation choice encodes one character, showing that no-URL-construction does not reduce channel capacity.

**What was already known.** Agent memory extraction via indirect injection, fake-verification social engineering of agents, user-agent cloaking, and symbol-at-a-time encoding of secrets into a network destination, whose DNS form was published a year earlier.

---

## 59.0 — [Web Cache Overflow: Exploiting Imprecise Keys for Cache Degradation and Beyond](https://arxiv.org/abs/2608.04744) — Golinelli, Onarlioglu, Crispo

**REMOVED** · Meaningful extension · confidence High

**What is new.** Turning developer cache-busting into sustained eviction needing no knowledge of the replacement algorithm, the corollary that forced eviction opens a poisoning window, and a Tranco-10k measurement of the precondition.

**What was already known.** Cache busting via unnecessarily-keyed query strings is decades-old practice (the paper says so), cache pollution has a large literature, Random Query String DoS was described in 2011, and CPDoS (2019) and Cache Key Normalization DoS (2020, in archive) cover cache-key availability attacks.

---

## 57.8 — [Bullseye: Detecting Prototype Pollution in NPM Packages with Proof-of-Concept Exploits](https://www.ndss-symposium.org/ndss-paper/bullseye-detecting-prototype-pollution-in-npm-packages-with-proof-of-concept-exploits/) — Houis, Jiang, Mannan, Youssef, Concordia

**REMOVED** · Tooling / methodology · confidence High

**What is new.** Solving the reachability problem in dynamic prototype-pollution detection by harvesting entry points and real argument shapes from each package's own test suite, then combining context-aware exploit generation with dual runtime oracles for PoC-validated results with no false positives, at 50,392 packages in under eight hours.

**What was already known.** The detection idea is explicitly built on Arteau's reflection-based dynamic checking and a later extended exploit-input study, and prototype pollution discovery at registry scale has been attacked repeatedly by static and dynamic tools; this scales and validates known knowledge.

---

## 57.8 — [The Dot-Dot-Slash That Frameworks Hand You: CSPT Across Every Major Frontend Framework](https://lab.ctbb.show/research/the-dot-dot-slash-that-frameworks-hand-you) [Repo](https://github.com/xssdoctor/cspt_research) — Jonathan Dunn

**REMOVED** · Tooling / methodology · confidence High

**What is new.** A per-framework map of URL-decoding pipelines across eight frameworks with concrete new gadgets, including a React Router case-sensitive double-decode and a Next.js page-vs-route-handler split, plus published labs.

**What was already known.** CSPT itself, its exploitation to CSRF and XSS, and the decode-level reasoning were established by Doyensec CSPT2CSRF (2024) and Berson WAF decode-level work; this systematises an established primitive.

---

## 57.5 — [Beyond the Limits of Site Isolation](https://www.youtube.com/watch?v=d3nfJL86jrc) — Ivan Fratric, Google Project Zero

**REMOVED** · Meaningful extension · confidence Low

**What is new.** Per the official abstract: systematic enumeration of alternate channels by which a compromised renderer leaks cross-site URLs, why one Chromium bug has resisted fixing for six years, and the reframing that sensitive URLs carry auth tokens.

**What was already known.** The Chromium compromised-renderers documentation states the full-URL protection goal and the open bug, and compromised-renderer attacks on Site Isolation were surveyed publicly in 2019. The only artifact is a conference video with no transcript or slides.

---

## 57.2 — [AgentForger: ChatGPT Cross-Site Agent Forgery](https://labs.zenity.io/post/agentforger-part-1-chatgpt-cross-site-agent-forgery) [Part 2](https://labs.zenity.io/post/agentforger-part-2-the-autonomous-insider) — Mike Takahashi, Zenity Labs

**REMOVED** · Meaningful combination · confidence Medium

**What is new.** The escalation target: a URL-seeded prompt against an agent builder yields not a single forged response but a persistent scheduled connector-authorized agent, forging a backdoor rather than a request.

**What was already known.** The underlying primitive, an unguarded URL parameter that auto-submits a prompt for a logged-in user, was published by Tenable a year earlier and is not acknowledged by the post.

---

## 56.8 — [KindaRails2Shell: how a MATLAB file reads your secrets and pops a shell on Rails](https://ethiack.com/info-hub/research/kindarails2shell-how-a-matlab-file-reads-your-secrets-and-pops-a-shell-on-ruby-on-rails) — Baptista, Mendes, Castilho, Ethiack

**REMOVED** · Meaningful combination · confidence Medium

**What is new.** The Rails-side chain around the file-read primitive: trusting the client-declared content type on direct upload, a variation key that signs only the transform and not the blob so a harvested key can be replayed against an attacker-uploaded blob, and single-pixel transforms for byte-exact exfiltration.

**What was already known.** The headline primitive was not first here: the libvips and libmatio header disagreement reaching HDF5 external file lists was published independently two weeks earlier, another researcher reached a similar chain, HDF5 external storage as a file-read primitive had surfaced in ML model loaders, and the escalation CVE was pre-existing.

---

## 56.8 — [GitHub RCE Vulnerability: CVE-2026-3854](https://www.wiz.io/blog/github-rce-vulnerability-cve-2026-3854) — Wiz Research

**REMOVED** · Useful application · confidence Medium

**What is new.** The specific attack surface: push options copied unsanitised into an internal semicolon-delimited header parsed last-write-wins, so a user can override security-policy fields downstream services treat as authoritative, then chain them into execution.

**What was already known.** The class is textbook: injecting the delimiter of an internal trusted-metadata channel built by string concatenation, with last-write-wins parsing turning that into a policy override (Intruder 2021, in archive; Orange Tsai 2018). The AI-assisted reverse engineering is asserted with no method shown.

---

## 56.5 — [DOMPurify XSS via `<selectedcontent>` re-clone](https://github.com/cure53/DOMPurify/security/advisories/GHSA-87xg-pxx2-7hvx) — Cure53 / KabirAcharya

**REMOVED** · Meaningful extension · confidence High

**What is new.** An engine-maintained live mirror is refreshed after a one-pass sanitizer has already cleared that subtree, yielding the invariant that sanitizers must re-walk or ban engine-managed clones.

**What was already known.** mXSS via post-sanitization DOM mutation is a decade-old family (Heiderich 2013; Securitum 2019 and 2020; mizu.re 2024), and the fix is a one-line allowlist removal on one new element.

---

## 56.2 — [SearchLeak: Parameter-to-Prompt injection in Microsoft Copilot](https://www.varonis.com/blog/searchleak) [Reprompt](https://www.varonis.com/blog/reprompt) [Data Tomb Raider slides](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Dolev%20Taler%2C%20Mark%20Vaitsman%20-%20Data%20Tomb%20Raider%20Raiding%20Modern%20AI%20Vaults%20with%20Legacy%20Flaws%20for%20Treasure%20Stealing%20-%20v1.pdf) — Dolev Taler & Mark Vaitsman, Varonis Threat Labs

**REMOVED** · Meaningful combination · confidence Medium

**What is new.** The HTML rendering race, where the image tag renders before the sanitizer wraps it, defeating the standard wrap-outbound-URLs mitigation in a streaming LLM interface: a reusable client-side primitive to test against any AI chat frontend.

**What was already known.** Everything else is built from known parts: URL-parameter auto-submit (Tenable 2025), zero-click assistant exfiltration (EchoLeak 2025), markdown-image exfiltration, and abusing an allowlisted endpoint as the fetching proxy. The label is the team's own from a companion post the same month.

---

## 56.2 — [Breaking the Boundaries: Analyzing QUIC Frame-Packet Interactions With QUIC-Attacker](https://www.usenix.org/conference/usenixsecurity26/presentation/erinola) — Niklas Erinola et al.

**REMOVED** · Tooling / methodology · confidence Medium

**What is new.** A sending-side-unconstrained framework plus a probe suite systematically enumerating valid and invalid coalescence and fragmentation combinations, an encoding-equivalence oracle earlier tools could not express, yielding eight DoS bugs across fifteen libraries.

**What was already known.** The underlying idea that multiple encodings of the same information produce divergence is standard parser-differential reasoning, and the same authors already applied this probing methodology to DTLS fragmentation in 2023.

---

## 56.0 — [Caught in the Octopus Trap: Unauthenticated RCE in Argo CD](https://www.synacktiv.com/en/publications/caught-in-the-octopus-trap-unauthenticated-rce-in-argo-cd-with-codeql) — Hugo Vincent, Synacktiv

**REMOVED** · Meaningful combination · confidence Medium

**What is new.** The concrete demonstration that a caller-supplied field on an internal-only gRPC API reaches exec argv, chained through unauthenticated cache poisoning to cluster-wide manifest injection, plus a reusable CodeQL recipe for modelling Go gRPC methods as remote flow sources.

**What was already known.** Argument injection into subprocess flags is textbook, the repo-server and cache being unauthenticated-by-design is documented in the project's own hardening guidance, and CodeQL model packs are a standard documented feature.

---

## 56.0 — [The sorry state of skill distribution](https://blog.trailofbits.com/2026/06/03/the-sorry-state-of-skill-distribution/) — Judson & Hess, Trail of Bits

**REMOVED** · Useful application · confidence Medium

**What is new.** The head-to-head result that three real scanners all pass four deliberately malicious skills, plus a public PoC corpus and upstreamed hardening patches: a concrete checkable datapoint that scanning cannot be the control.

**What was already known.** Every evasion used is long-standing tradecraft: source-versus-bytecode divergence, archive obfuscation, padding past a truncation window, and prompt injection against an LLM analyzer, the last already shown academically in 2025.

---

## 55.9 — [Zero-Click RCE in Figma Desktop](https://lab.ctbb.show/research/figma-desktop-zero-click-rce/) — Benjamin Mamoud

**REMOVED** · Meaningful combination · confidence Medium

**What is new.** Two reusable escalation ideas: racing prototype pollution against initialisation to forge a feature flag and unlock a normally-unreachable API, and recognising that a partial expression evaluator resolving unbound identifiers against an empty object is a pollution sink reaching Function.

**What was already known.** Prototype-pollution gadget hunting, the webpack require-leak, and unvalidated Electron IPC file-write as XSS-to-RCE (ElectroVolt, BH USA 2022, in archive); the chain composition is the contribution and it is bound to one product patched within hours.

---

## 55.7 — [ELF in the Pixels: Building Shared Object–Image Polyglots](https://blog.babelo.xyz/posts/elf-in-the-pixels/) — Salvatore Abello

**REMOVED** · Meaningful extension · confidence High

**What is new.** That the Pillow PCD plugin sniffs its marker at offset 2048 rather than byte 0, so an ELF header can occupy offset 0 and the file passes verify() while remaining loadable as a shared object, plus a standalone builder.

**What was already known.** Polyglot upload-validation bypass as a class (GIFAR 2008, PHP-in-PNG, ImageTragick, mitra) and the author's own HITCON 2025 precursor; ELF shared-object polyglots appeared independently in the Atril advisory five days later.

---

## 55.5 — [Race Against The Patch: Four Exploit Chains in LiteLLM](https://starlabs.sg/blog/2026/05-race-against-the-patch-the-evolution-of-four-exploit-chains-in-litellm/) — Shi Weiming & Bruce Chen, STAR Labs

**REMOVED** · Meaningful combination · confidence High

**What is new.** Two composition patterns: deliberately exhausting the database connection pool to reach a fail-open branch, and second-order secret exfiltration where an environment-variable indirection is stored through an unpatched validation path and resolved later inside a privileged request.

**What was already known.** The headline environment-reference leak and the template-injection RCE were published concurrently or earlier by others (McCaulay, 18 days earlier); the rest is textbook authorisation and Python-jail material on a new target.

---

## 55.2 — [Living Off The Pipeline: Defensive Research, Weaponized (SmokedMeat / Brisket)](https://labs.boostsecurity.io/articles/introducing-smokedmeat/) — François Proulx, Boost Security Labs

**REMOVED** · Tooling / methodology · confidence Medium

**What is new.** A purpose-built post-exploitation implant for CI runners, packaging the full recon to post-exploitation to pivot kill chain rather than a one-shot shell.

**What was already known.** Every constituent technique comes from the author's own earlier catalog and from existing tooling that the article explicitly names as what this extends; the announcement post is short, with the substance in the released source.

---

## 55.2 — [Scanning the Scanners: Turning Security Vendors Into Supply Chain Weapons](https://i.blackhat.com/BH-USA-26/Presentations/US-26-Karger-Scanning-The-Scanners-Thursday.pdf) — Raphael Karger, ZeroPath

**REMOVED** · Tooling / methodology · confidence Medium

**What is new.** The empirical adversarial sweep of 20 hosted scanners with five confirmed boundary failures, a five-boundary model with an evidence bar separating a backend path firing from real worker impact, and a released regression corpus plus a deliberately-vulnerable scanner.

**What was already known.** All the primitives it fires are known: build files executing during analysis and symlink escape to the process environment. Vendor credentials in the worker is a consequence, not a discovery.

---

## 54.5 — [HermeticReader: turning Adobe's 300M-install extension into a WhatsApp takeover](https://guard.io/labs/hermeticreader---the-vulnerability-that-turned-adobe-300m-install-extension-into-a-full-whatsapp-takeover) — Shaked Biner, Guardio Labs

**REMOVED** · Meaningful combination · confidence High

**What is new.** Three modest primitives: predicting a tab ID because Chrome allocates sequentially and the attacker opens the tab, an unauthenticated extension-storage write to flip a dormant feature flag, and exfiltrating a rendered DOM by relocating the body into a form select so option text is POSTed cross-origin.

**What was already known.** The bulk of the chain is a documented extension antipattern with a nine-year paper trail (Space Raccoon 2024, in archive; Reutov 2017), and form hijacking to bypass CSP is 2017 work. Install count and CVE are impact, not novelty.

---

## 54.5 — [Pass the Passkey: A Novel Attack Surface in Passwordless Authentication](https://unit42.paloaltonetworks.com/passwordless-authentication-security-risks/) — Arie Olshtein, Unit 42

**REMOVED** · Meaningful extension · confidence Medium

**What is new.** The strongest element is that during the pending state after forced re-registration the cloud authenticator does not validate attestation of newly registered verification keys, so an attacker can enrol their own and authenticate remotely without touching the device again.

**What was already known.** The other two land closer to known ground: reusing a wrapped device key from disk and scraping a master secret from browser process memory are the same post-compromise credential-theft patterns already established, and the architectural reverse-engineering came from parts 1 and 2 of the series.

---

## 54.5 — [Re:CACHE — Excessive reflection, type confusion, and 0-click SXSS on Next.js](https://zhero-web-sec.github.io/research-and-things/re-cache-excessive-reflection-type-confusion-and-0-click-sxss-on-nextjs) — zhero; & inzo\_

**REMOVED** · Meaningful extension · confidence High

**What is new.** Turning header reflection into Content-Type type confusion so a cached RSC payload renders as HTML, then chaining a second poisoned entry carrying a Refresh header to make the stored XSS zero-click.

**What was already known.** RSC payloads cacheable because CDNs ignore the Vary header (the authors' own 2024 work), flipping a poisoned response to text/html (their 2025 follow-up), SSR-to-SSG poisoning (CVE-2024-46982), and redirect-gadget cache chaining (Kettle 2018).

---

## 54.2 — [H3Act: Automated Measuring Semantic Conversion Anomalies of HTTP/3-to-HTTP/1.1 Translation in CDNs](https://www.usenix.org/conference/usenixsecurity26/presentation/peng-qihang) — Qihang Peng et al., USENIX Security '26

**REMOVED** · Meaningful extension · confidence Medium

**What is new.** The scale and the generator: a dual-agent pipeline turning RFC text and historical smuggling knowledge into HTTP/3 payloads, applied black-box to nine commercial CDNs with seven attack vectors, every one vulnerable to at least one.

**What was already known.** The thesis and method shape are established: that translating a framed protocol down to HTTP/1.1 reintroduces ambiguity, and that differential fuzzing across front-end and back-end pairs is how you find it; an explicit HTTP/3 smuggling detection methodology was published two years earlier.

---

## 54.2 — [Identifying Logical Vulnerabilities in QUIC Implementations](https://www.ndss-symposium.org/wp-content/uploads/2026-s1777-paper.pdf) — Wang, Chen, Chen, Zhuge, Bai, Duan, Tsinghua

**REMOVED** · Tooling / methodology · confidence High

**What is new.** An oracle for logic rather than crashing bugs, built from differential semantic comparison plus resource-consumption monitoring, combined with segmental mutation and snapshot restore to make long sequences tractable; fourteen logic bugs and five CVEs.

**What was already known.** Black-box and greybox QUIC fuzzing, automata-learning noncompliance checking and packet-sequence protocol fuzzing all predate it, as does differential testing as an oracle; the six bug categories are resource-exhaustion DoS rather than new web-facing techniques.

---

## 53.8 — [AI Server-Side Browser Security Whitepaper](https://xlab.tencent.com/cn/2026/02/02/ai-browser-crawler-whitepaper/) — Guancheng Li & Zheng Wang, Tencent Xuanwu Lab (Chinese)

**REMOVED** · Tooling / methodology · confidence Medium

**What is new.** A systematised five-stage kill chain for server-side browsers in AI pipelines with two reusable twists: laundering attacker content into an allowlisted origin by chaining a product's own read, share and screenshot features, and an undocumented asynchronous backend indexer as a delayed invisible entry point. Plus an open-sourced hardened browser.

**What was already known.** Server-side browsers as a hidden attack surface including attacking the engine itself was systematically established academically four years earlier; open-redirect allowlist bypass, metadata SSRF from headless renderers and N-day chaining are long-standing practice.

---

## 53.5 — [Exploiting Auth0 Defaults in XSS Attacks](https://www.elttam.com/blog/exploiting-auth0-defaults-in-xss-attacks/) — Alex Brown, elttam

**REMOVED** · Useful application · confidence Medium

**What is new.** The specific default chain: implicit grant left enabled and APIs authorising all tenant applications by default, so one XSS mints tokens for unrelated APIs, plus default user access to an identity-linking scope enabling account-linking persistence.

**What was already known.** That XSS in a browser-based OAuth client can silently mint fresh tokens through a hidden iframe regardless of token storage is specified in the OAuth browser-based-apps draft, and the implicit grant is deprecated precisely for this exposure. Account-linking-as-backdoor is a known pattern.

---

## 53.2 — [L3akCTF 2026 "Squid": racing `/proc/self/fd` symlinks against Flask `send_file`'s stat/open TOCTOU to read zero-length files](https://jorianwoltjer.com/blog/p/ctf/l3akctf-2026-squid) — Jorian Woltjer

**REMOVED** · Meaningful combination · confidence Medium

**What is new.** A crisp reusable gadget: because the file sender calls stat then open separately, a second request recycling the same descriptor number lets you point it at a zero-length special file while the response borrows a normal file's length, defeating the truncation of zero-size files.

**What was already known.** Everything else in the chain was published, including the JSON key-collision and URL parsing differentials, both cited by the author; the descriptor trick is acknowledged as remembered from a past CTF and no novelty is claimed.

---

## 53.0 — [SekaiCTF 2026 "Filtered Reality": invalid Signed HTTP Exchange fallback navigation as a redirect and CSP-nonce escape primitive](https://github.com/project-sekai-ctf/sekaictf-2026/blob/main/web/filtered-reality/solution/writeup.md) — dimasma0305, Project Sekai

**REMOVED** · Meaningful combination · confidence Medium

**What is new.** Repurposing the documented Chromium SXG graceful-degradation path: serve an invalid signed exchange and the browser performs a fallback navigation to the embedded URL, whose re-request omits the SXG Accept header and so escapes the original per-request nonce CSP. No valid signature or certificate needed, unlike all prior SXG attack work.

**What was already known.** The fallback is by design and documented; the closest attack work (CrossSXG, NDSS 2025) needs a valid SXG with a signing certificate. The other four stages of the chain are established.

---

## 53.0 — [OffGuard: Breaking the Most Popular AI Gateway (LiteLLM) from Auth Bypass to Cloud Compromise](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Yaara%20Shriki%20-%20OffGuard%20Breaking%20the%20Most%20Popular%20AI%20Gateway%20from%20Auth%20Bypass%20to%20Cloud%20Compromise.pdf) — Yaara Shriki, Wiz

**REMOVED** · Useful application · confidence Medium

**What is new.** The packaging: a ghost-guardrail persistence primitive where deleting a guardrail removes the database row but not the in-memory callback so planted code keeps running, and a demonstration that a header-prefix-stripping feature hands an attacker arbitrary forwarded headers, enough to complete the metadata-service handshake.

**What was already known.** Everything else is textbook on a newly popular target: a documented default master key, a fail-open exception branch, a sandbox applied on only one endpoint, pass-through SSRF, and a Shodan coverage survey. Header control past a reverse proxy as a metadata primitive was published in 2021 (in archive).

---

## 52.9 — [Never Trust the Output: Data Pollution in AI Agents and MCP](https://blog.slonser.info/posts/smugglle-ai-ouputs/) — Slonser

**REMOVED** · Meaningful extension · confidence Medium

**What is new.** The framing that an LLM consuming a tool response acts as a lenient parser rather than a real one, so the attack surface is the serialization boundary, with homoglyph quotes and fabricated error tags escaping a data field; the blind variant for unseen outputs is a useful addition.

**What was already known.** That tool outputs are an injection surface and must be treated as untrusted is the explicit thesis of CyberArk 2025 work and the indirect-prompt-injection literature since 2023, and Unicode smuggling into model context predates this by two years. The post cites none of them.

---

## 52.8 — [Node.js TLS hostname-normalisation differentials: Unicode dot separators defeat wildcard depth](https://hackerone.com/reports/3688064) [Embedded-NUL authority rebinding](https://hackerone.com/reports/3656716) [Session reuse with a different servername](https://hackerone.com/reports/3649802) [Fix commit with the test vector](https://github.com/nodejs/node/commit/1efb4ff51a) — tmeletlidis

**REMOVED** · Meaningful extension · confidence Medium

**What is new.** A resolver-vs-verifier normalisation differential: U+3002 counts as one label to the Node verifier so it matches a wildcard, while the resolver applies IDNA mapping and connects deeper. Wildcard depth is defined by whoever counts the dots is a clean portable framing.

**What was already known.** The class was published six years earlier for Java and Apache HttpClient (GoSecure 2020), the embedded-NUL sibling rebinds the Marlinspike 2009 NUL-prefix idea, and U+3002 as a label separator is specified IDNA behaviour.

---

## 52.5 — [Critical Flaws in Anthropic, Google and OpenAI's Coding Agents: the trust-handoff primitive](https://novee.security/blog/critical-flaws-in-anthropic-google-and-openais-coding-agents/) [Gemini CLI chain](https://novee.security/blog/gemini-cli-cvss-10-rce-novee-security/) — Elad Meged, Novee Security

**REMOVED** · Meaningful combination · confidence Medium

**What is new.** One sharp parser differential: the validator strips single-quoted content before checking while git receives the quotes intact and treats the flag as executable, a clean validator-versus-executor disagreement.

**What was already known.** The rest re-labels known ground: git upload-pack argument injection is long-standing, the prefix-matching allowlist gap was already public, and the pass-1-writes pass-2-reads config pattern was documented repeatedly through 2025. Trust-handoff is a naming exercise over confused-deputy, and several load-bearing claims could not be verified.

---

## 52.2 — [FirefUXSS: universal XSS in Firefox Focus/Klar for iOS](https://github.com/v12-security/pocs/tree/main/firefox) — V12 Security with Renwa

**REMOVED** · Meaningful extension · confidence Medium

**What is new.** The race: flooding the redirect handler desynchronises the dangerous-scheme validator from the navigation commit, so a trailing javascript redirect commits before rejection. The transferable lesson is that asynchronous URL-policy checks are inherently racy.

**What was already known.** The payoff mechanism is known: a javascript-scheme redirect executing with the previous document's inherited origin was published as semi-UXSS against Firefox for iOS in 2020 (CVE-2019-17004).

---

## 52.2 — [XSS via i18n translation-template injection in NodeBB](https://www.aikido.dev/blog/eight-high-severity-vulnerabilities-nodebb) — Jorian Woltjer, Aikido

**REMOVED** · Meaningful extension · confidence Medium

**What is new.** The escalation craft: once translation keys can be injected into a post-escape pass, the catalogue's own HTML-bearing strings become breakout gadgets, and with the equals sign escaped you still reach code via a javascript URI. A reusable recipe for any i18n system storing markup in its catalogue.

**What was already known.** Injection into a second rendering pass whose metacharacters survive the first pass escaping (SSTI 2015, client-side template injection 2016, syntax confusion 2025, all in archive) and i18n-specific escaping mismatches in Rails, Angular and vue-i18n; the other seven bugs in the post are routine.

---

## 52.2 — [Drupal PostgreSQL SQL Injection: From SELECT-Only to RCE](https://blog.lexfo.fr/drupal-postgresql-sqli-to-rce.html) — N. Maccary, Ambionics/Lexfo

**REMOVED** · Useful application · confidence High

**What is new.** Only refinement: assembling bytes with large-object functions inside pure scalar sub-SELECTs, overwriting the auto-generated config rather than the main one, and validating across PostgreSQL 12 to 18 as one unauthenticated exploit.

**What was already known.** The chain was already published end-to-end in Phrack 71:8 (2024, in archive), which itself credits Andzakovic (2021) and sylsTyping (2022); the post does not cite it.

---

## 51.8 — [New Age of Collisions: Pre-Auth Arbitrary File Read as root in cPanel](https://slcyber.io/research-center/new-age-of-collisions-reading-arbitrary-files-pre-auth-as-root-in-cpanel-cve-2026-29205/) — Shah, Kues, Grobshäuser

**REMOVED** · Meaningful combination · confidence Medium

**What is new.** The pre-auth setup primitive, abusing plus-addressing autocreation to make the server create an attacker-named directory that then satisfies a regex, and secondarily a Perl guard-lifetime footgun where a privilege-dropping object is constructed without being stored so it destructs immediately.

**What was already known.** Both halves of the bypass are textbook: validating a raw URI with a regex before unescaping is classic validate-before-decode traversal (Orange Tsai 2018, in archive), and a discarded guard object destructing immediately is the direct analogue of a long-known C++ mistake.

---

## 51.6 — [Attacking and Defending AI Browsers](https://i.blackhat.com/BH-USA-26/Presentations/US-26-Chaikin-Attacking-Defending-AI-Browsers.pdf) [Companion post](https://brave.com/blog/indirect-prompt-injection/) — Artem Chaikin, Brave

**REMOVED** · Tooling / methodology · confidence High

**What is new.** The vendor-neutral defense taxonomy the deck systematises, plus the empirical point that one browser ran the full stack and still fell.

**What was already known.** The attacks are not new: fake closing tags, fake system prompts and fake turns are the same family analysed in entry 106, image-based injection is credited to Trail of Bits, and the companion post is standard injection applied to two new targets. Slides only, with asserted-not-evidenced claims.

---

## 51.5 — [Finding XSS on Shazzer (literally)](https://jorianwoltjer.com/blog/p/stories/finding-xss-on-shazzer) — Jorian Woltjer

**REMOVED** · Meaningful combination · confidence Medium

**What is new.** A small trick, pushing a non-cloneable function into the data array so postMessage throws and the blob URL is never revoked, plus a clean demonstration that sandboxing the frame does not sandbox a blob minted by the unsandboxed parent.

**What was already known.** All load-bearing primitives are known: blob URLs inheriting creator origin is spec behaviour and a documented sandbox-escape pattern, WebRTC DNS exfiltration is years old, and the drag-navigation trick is credited by the author to a Renwa challenge.

---

## 51.0 — [Sandcastles, Not Sandboxes: `ctypes.CDLL(None)` reaches Emscripten exports to escape Pyodide into the host JS runtime](https://www.cyera.com/research/sandcastles-not-sandboxes-how-one-architectural-flaw-exposed-seven-products) [Grist precursor](https://www.cyera.com/research/cellbreak-grists-pyodide-sandbox-escape-and-the-data-at-risk-blast-radius) — Saar Pearl & Vladimir Tokarev, Cyera Research Labs

**REMOVED** · Useful application · confidence High

**What is new.** Breadth: seven products confirmed, impact differentiation across runtimes, and a reusable three-layer triage checklist.

**What was already known.** The escape primitive itself was published by this same team twice before, in January 2026 for one product and in 2025 for another, using the same library-loading and script-evaluation routes. Coverage is not discovery.

---

## 50.6 — [Apache httpd HTTP/2 Memory Exhaustion (CVE-2025-53020)](https://galbarnahum.com/posts/apache-httpd-cve-2025-53020) — Gal Bar Nahum

**REMOVED** · Meaningful extension · confidence High

**What is new.** Inverting the classic HPACK bomb so amplification comes from the allocator per-header bookkeeping rather than large decoded values, reaching about 4000x; the transferable lesson is to count allocations, not decoded bytes.

**What was already known.** HPACK dynamic-table amplification has been public since 2016 (CVE-2016-6581); this is otherwise a single-implementation memory-management bug, and the general form of the insight was published later by others.

---

## 50.5 — [Blind enumeration of unreadable records via a sort oracle in Trello](https://bugcrowd.com/disclosures/0ecb51a3-2064-4f9d-aa19-aa7b6ae21812/blind-enumeration-of-private-card-names-via-sort-oracle-and-id-discovery) — BobAshEf

**REMOVED** · Meaningful extension · confidence Medium

**What is new.** That authorization was enforced on the read path but not the sort path, so an unreadable record still participates in ordering: you never read it, you binary-search its position using probe records you control.

**What was already known.** The comparison-oracle extraction loop is decades old, and the elttam ORM Leak work already covered leaking inaccessible field values through oracles including collation-ordering caveats; the ID-discovery half is ordinary enumeration.

---

## 50.5 — [Golang code review notes II](https://www.elttam.com/blog/golang-code-review-notes-ii) — Zoltan Madarassy & Alex Brown, elttam

**REMOVED** · Tooling / methodology · confidence High

**What is new.** A reviewer checklist collecting existing Go sharp edges, with accompanying Semgrep rules; its value is practical usability rather than discovery, and the article sources most items to earlier work.

**What was already known.** The only mildly fresh composition is JSON decoding tolerating trailing bytes plus unvalidated Content-Type enabling simple-request CSRF, and JSON-CSRF via text/plain padding predates this by years.

---

## 50.5 — [Fooling AI Agents: Web-Based Indirect Prompt Injection Observed in the Wild](https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/) — Kaleli, Farooqi, Starov, Mohamed, Unit 42

**REMOVED** · Useful application · confidence Medium

**What is new.** The empirical turn: moving indirect prompt injection from proof-of-concept to measured field data, with a taxonomy of 22 payload-delivery techniques and attacker-intent categories drawn from production telemetry.

**What was already known.** The attack class itself and its anecdotal in-the-wild forms. The methodology rests on proprietary telemetry with undisclosed denominators and no released dataset, so the percentages cannot be verified or reproduced.

---

## 50.5 — [Proto6: The Schema Was Not Supposed to Run](https://www.cyera.com/research/proto6-the-schema-was-not-supposed-to-run) — Vladimir Tokarev, Cyera

**REMOVED** · Useful application · confidence Medium

**What is new.** A concrete gadget where prototype pollution makes the runtime type lookup return attacker-controlled strings interpolated into a Function body, plus unescaped identifiers reaching generated source so a malicious schema in a pull request executes on require.

**What was already known.** Prototype pollution through the same option-path surface (CVE-2023-36665, 2023) — this is a bypass of that incomplete fix — and prototype-pollution-to-RCE via dynamic code-generation sinks as a gadget class (in archive).

---

## 50.4 — [Breaking the Control Plane: Exploiting MCP Servers in AI Workflows](https://troopers.de/downloads/troopers26/TR26_Breaking_the_Control_Plane_F3XCER.pdf) [Video](https://youtu.be/DAbyi6MZR9w) — Yotam Perkal, Pluto Security

**REMOVED** · Useful application · confidence High

**What is new.** Three CVEs in two real servers and one neat composition: config-write plus auto-reload used to inject a log format that harvests live admin tokens.

**What was already known.** Every primitive is known, and the exposure framing itself is sourced by the deck to the OWASP MCP list and prior vendor research; the speaker's own slides say the same eight mistakes over and over, and five old bugs one new blast radius.

---

## 50.2 — [Trusted Publishing, Untrusted Branch: Inside the Red Hat npm Compromise](https://labs.boostsecurity.io/articles/trusted-publishing-untrusted-branch-red-hat-npm) — François Proulx, Boost Security Labs

**REMOVED** · Useful application · confidence Medium

**What is new.** One addition beyond incident forensics: that the same throwaway branches carried developer-endpoint persistence via editor and agent hook files that survives package unpublishing.

**What was already known.** That trusted publishing binds to org, repo and workflow filename but not the git ref, and that a dedicated environment is the opt-in fix, is documented in the registry's own security model since 2023; this is one of four analyses of the same event published the same day.

---

## 50.0 — [The SQL Server Unicode problem: Best-Fit mapping as a universal filter bypass](https://www.synacktiv.com/en/publications/the-sql-server-unicode-problem-why-your-data-might-not-be-what-you-think-it-is) — Alexandre Zanni, Synacktiv

**REMOVED** · Independent rediscovery · confidence High

**What is new.** Quantitative and modern packaging: 22 characters collapse to a less-than sign under Best-Fit versus 2 under NFKC, with payloads that only become dangerous after storage.

**What was already known.** The mechanism, SQL Server Best-Fit-mapping Unicode into a narrow column after validation, was described 18 years earlier in SQL Smuggling (2008, in archive), and the mapping tables come from WorstFit.

---

## 50.0 — [Content-Type Override to Stored XSS on public objects](https://blog.voorivex.team/content-type-override-to-stored-xss-on-public-objects) — Amirmohammad Safari, Voorivex

**REMOVED** · Meaningful combination · confidence Medium

**What is new.** A small bridging step: because a public-read object is readable by any principal, an attacker can sign the response-content-type override with their own credentials, defeating the restriction that overrides cannot be used for anonymous requests.

**What was already known.** Response-header override parameters are vendor-documented, overriding content type in presigned URLs was blogged in 2014, serve-time content-type abuse for XSS is a bug-bounty staple, and upload-time validation is not serve-time enforcement is long established.

---

## 50.0 — [Hack the Elephant One Bite at a Time: NUL byte SQL Injection in pdo\_firebird](https://swarm.ptsecurity.com/hack-the-elephant-one-bite-at-a-time-nul-byte-sql-injection-in-pdo_firebird-and-null-pointer-dereference-in-pdo-pgsql/) [JPEG memory-safety bugs in PHP](https://swarm.ptsecurity.com/hack-the-elephant-one-bite-at-a-time-jpeg-related-memory-safety-bugs-in-php/) — Aleksey Solovev & Nikita Sveshnikov, PT SWARM

**REMOVED** · Meaningful extension · confidence High

**What is new.** That a correct escaper can still yield injection because a later re-parse in the same library is binary-unsafe: the string concatenation honours the NUL and drops the closing quote, so quote-then-prepare becomes injectable.

**What was already known.** NUL-byte truncation in C-based DB drivers is documented (msphpsql 2016-17), and injection through the PDO emulation parser was published by Searchlight in 2025 (in archive). Reach is small.

---

## 50.0 — [When Filenames Become Attack Surfaces: Weaponizing NASA's CFITSIO Extended Filename Syntax](https://blog.doyensec.com/2026/05/19/cfitsio-weaponized-filenames.html) — Adrian Denkiewicz, Doyensec

**REMOVED** · Useful application · confidence Medium

**What is new.** The specific primitives found in this library: an outfile clause copying a file before any validation, CRLF injection into the network driver request line, and raw-reinterpretation clauses combined into local-file exfiltration, with a Docker playground.

**What was already known.** The entire class, a filename parameter that is secretly a mini-language of coders and protocol handlers, was established by ImageTragick for ImageMagick in 2016 and by ffmpeg protocol handling the same year; this is that lesson applied to a new library.

---

## 49.6 — [The CSRF-token leak both Claude Code and Codex Security missed (SAML IdP form helpers)](https://gmo-cybersecurity.com/blog/claude-codex-missed-csrf-token-leak/) — Yamazaki, GMO Cybersecurity by IERAE

**REMOVED** · Useful application · confidence Medium

**What is new.** The concrete instantiation and evidence: a form helper auto-injecting the CSRF token even when the action is an external service-provider URL, so an identity provider ships its own token cross-origin, demonstrated in a widely-used gem's sample code with a fix PR and PoC.

**What was already known.** That CSRF tokens must never be placed in forms targeting third-party endpoints is long-standing, with existing lint tooling for exactly this leak; the article frames the pattern as overlooked rather than new. The two-AI-reviewers-missed-it framing is publicity and was excluded.

---

## 49.5 — [Charting your way in: Helm template injection](https://www.synacktiv.com/en/publications/charting-your-way-in-helm-template-injection) — Paul Barbé, Synacktiv

**REMOVED** · Useful application · confidence Medium

**What is new.** Careful exploitation mechanics for this sink: how block scalars, indentation and document separators let a single value field emit whole additional Kubernetes objects, the ArgoCD threat model where chart edits are restricted but value overrides are not, and a Helm v4 trick to survive server-side validation.

**What was already known.** The mechanism itself is textbook injection: unquoted interpolation of untrusted input into templated YAML, with Helm documentation already telling chart authors to quote values, and injecting extra documents via a separator is standard YAML-injection technique.

---

## 49.5 — [My Road to Black-Box RCE in LLM Products: `postinstall` in AI preview builders, weakest-model-wins guardrail bypass, and DLP evasion by channel choice](https://mp.weixin.qq.com/s/whv4LzJTiJt-i2zHzdG8Eg) — 行之 (Chinese; author-authorized mirror of `xz.aliyun.com/news/92273`, which is WAF-gated)

**REMOVED** · Useful application · confidence Medium

**What is new.** Two transferable heuristics: weakest-model-wins, where the same injection refused by strong models executes under the weakest selectable one so the platform's security is its weakest model; and DLP evasion by channel choice, where the inspector watches the response stream but not what the tools do.

**What was already known.** Prompt-controlled dependency selection reaching install-hook execution composes two thoroughly documented parts that the article itself cites, cloud-metadata probing from a build container is routine, and the identifier-increment case is textbook IDOR through a tool call.

---

## 49.2 — [Gotta Phish 'Em All! Novel Attack Techniques via Persistent Browser-in-the-Middle](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Giacomo%20Lenzini%20-%20Gotta%20Phish%20%27Em%20All%20Novel%20Attack%20Techniques%20via%20Persistent%20Browser-in-the-Middle%20-%20v2.pdf) — Giacomo Lenzini, EY Italy

**REMOVED** · Tooling / methodology · confidence Medium

**What is new.** The engineering: a WebRTC transport with runtime cursor hijacking, a hardened kiosk build, and most interestingly weaponised extensions inside the relay browser that intercept logout and merely delete cookies locally so the victim believes they signed out while the operator keeps the session.

**What was already known.** The whole paradigm and its MFA-defeating property, containerised per-victim browsers with load balancing, live monitoring, keylogging and profile capture were published in March 2025; the deck itself labels several components Old but Gold.

---

## 49.0 — [BodySnatcher: agentic hijacking in ServiceNow](https://appomni.com/ao-labs/bodysnatcher-agentic-ai-security-vulnerability-in-servicenow/) — Aaron Costello, AppOmni Labs

**REMOVED** · Useful application · confidence High

**What is new.** The observation that a supervised human-in-the-loop confirmation is not an authorization boundary when delivered out-of-band, plus an undocumented internal invoker topic as a reachable execution path.

**What was already known.** Every link is textbook broken authentication: a universal hardcoded shared secret, email-as-proof-of-identity linking, and identical identifiers across tenants; the confused-deputy shape is the core of the indirect-prompt-injection literature since 2023. The blast radius is impact, not novelty.

---

## 48.8 — [No Socket, No Privs, No Problem: Weaponizing OCI Registries for SSRF, Credential Theft, and Container Escapes](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20David%20Rochester%2C%20Nicholas%20Gould%20-%20No%20Socket%2C%20No%20Privs%2C%20No%20Problem%20Weaponizing%20OCI%20Registries%20for%20SSRF%2C%20Credential%20Theft%2C%20and%20Container%20E.pdf) — Rochester & Gould

**REMOVED** · Tooling / methodology · confidence Medium

**What is new.** The framing and taxonomy: the OCI registry treated as a hostile input channel against its clients, with a primitive map extended into the AI model-distribution ecosystem.

**What was already known.** The individual findings are known-class or already CVE-assigned: malicious-registry credential coercion dates to ContainerDrip (2020), realm-hijack SSRF was CVE-assigned months earlier, and the digest-traversal finding is the same bug class as Probllama. The deck is slides with mechanics in screenshots.

---

## 48.8 — [Beyond Normalization: The Expanding Unicode Attack Surface](https://i.blackhat.com/BH-USA-26/Presentations/BHUSA26-Barnett-Beyond-Normalization-Slides.pdf) — Ryan Barnett & Isabella Barnett, Akamai

**REMOVED** · Useful application · confidence Medium

**What is new.** RE2 latin1-vs-UTF-8 configuration changing what a regex actually matches, Jackson-core charToHex truncation, and the framing of Unicode as a distributed-parsing rather than normalization problem.

**What was already known.** Nearly every other section has an antecedent: the __Host- whitespace cookie bypass is PortSwigger Cookie Chaos (2025), invisible tag smuggling is Trojan Source (2021), best-fit mapping is Weber (2009) and WorstFit (2024-25), and normalization-gap WAF bypass is the authors' own BH USA 2025 talk.

---

## 48.7 — [Pwning Agentic Browsers with PleaseFix](https://zenity.io/research/pleasefix-vulnerabilities) — Bargury, Cohen, Donato, Onitza-Klugman, Ishay Sharbat, Zenity Labs

**REMOVED** · Useful application · confidence Medium

**What is new.** Two subfamilies not previously judged: Agent127, where the agent reaches localhost as a first-party user rather than as a script so SOP, CORS, Private Network Access and DNS-rebinding pinning simply do not apply to it; and HistoryFixing, planting fabricated browser-history entries the agent later reads as user-authored fact, which sits outside agent-memory mitigations because it is not agent memory.

**What was already known.** The umbrella scores below its own parts. Grand Theft Atlas (59.1) and the Claude in Chrome chain (59.2) were already judged and cannot be re-banked. PleaseFix as the hub itself defines it is indirect prompt injection (Greshake 2023, in archive; Brave's agentic-browser series from Aug 2025), intent collision was published as Task Injection in Dec 2025 and used by this same team in Mar 2026, and Agent127's thesis is Microsoft's AutoJack from seven weeks earlier. HistoryFixing is the one durable idea and the least documented: no dedicated writeup, no PoC, and the browser feature is never even named.

---

## 48.0 — [CVE-2026-21876: bypassing OWASP CRS by overwriting the multipart charset in a later segment](https://habr.com/ru/articles/984632/) — daytriftnewgen (Russian)

**REMOVED** · Meaningful extension · confidence High

**What is new.** A rule-engine semantics bug: when the first rule in a ModSecurity chain iterates a collection, the capture variables are last-write-wins, so the rule validated only the final multipart part charset. A reusable auditing pattern for chained-capture CRS rules.

**What was already known.** The evasion it enables, declaring a charset in an early part so the backend decodes what the WAF read as plain bytes, is decades-old charset-switching evasion, and multipart-parser-vs-WAF discrepancies were systematised before this.

---

## 48.0 — [Beyond the Ceremony: The 2026 Passkey Attack Surface](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Matteo%20Giordano%20-%20Beyond%20the%20Ceremony%20The%202026%20Passkey%20Attack%20Surface%20-%20v2.pdf) — Matteo Giordano, Anvil Secure

**REMOVED** · Tooling / methodology · confidence High

**What is new.** Organisation rather than discovery: a six-layer map, an 18-item verification checklist, a creativity list of relying-party mistakes, and a Burp extension whose differentiator is auto re-signing on passthrough.

**What was already known.** Everything the map contains is other people's published work, and the deck says so on its own not-the-first-tool slide, ranking another tool above it for tampering at scale; many findings appear only as screenshots.

---

## 47.2 — [Breaking SameSite=Strict in Chrome](https://lab.ctbb.show/writeups/breaking-samesite-strict-in-chrome) — mianHIZB & bug\_blitzer

**REMOVED** · Useful application · confidence Medium

**What is new.** A concrete demonstration that a spec-violating DevTools request, once intercepted by a service worker that re-issues it, is laundered into a same-site request carrying SameSite=Strict cookies.

**What was already known.** That site-for-cookies is not propagated through pass-through service workers was raised on whatwg/fetch issue 1332 in 2021; realistic reach is near-zero since it requires the victim to open DevTools.

---

## 47.2 — [Keys to the Kingdom: Anonymous SQL Injection in Drupal Core (CVE-2026-9082)](https://slcyber.io/research-center/keys-to-the-kingdom-anonymous-sql-injection-in-drupal-core-cve-2026-9082/) — Grobshäuser, Gervot, Williamson

**REMOVED** · Useful application · confidence High

**What is new.** The reachability analysis showing two anonymous paths that hand user input into array keys is a reusable audit pattern.

**What was already known.** The injection mechanism is precisely Drupageddon (CVE-2014-3704, 2014), rediscovered in the PostgreSQL backend override twelve years later; confined to Drupal on PostgreSQL.

---

## 46.9 — [Hidden security risks in Jupyter notebooks](https://www.sonarsource.com/blog/hidden-security-risks-in-jupyter-notebooks/) — Yaniv Nizry, Sonar

**REMOVED** · Useful application · confidence High

**What is new.** One fresh gadget: a LaTeX and MathJax sanitization bypass giving attacker-controlled navigation from an untrusted notebook, which then funnels into an already-known chain.

**What was already known.** The XSS-to-RCE-via-unauthenticated-Electron-IPC pattern (ElectroVolt, BH USA 2022, in archive) and the leak-the-local-token-then-use-the-REST-API outcome (2023, in archive) were both published years earlier.

---

## 46.8 — [CosmosEscape: Taking Over Every Database in Azure Cosmos DB](https://www.wiz.io/blog/cosmosescape-taking-over-every-database-in-azure-cosmos-db) — Wiz Research

**REMOVED** · Useful application · confidence Medium

**What is new.** That a platform-wide signing key sat on a shared multi-tenant gateway together with a config store permitting tenant-targeted lookup: a strong architectural datapoint, but architecture-of-one-vendor rather than a new primitive.

**What was already known.** The escape is the long-known host-runtime-reflection-from-a-query-language-sandbox, and the cloud pattern of escaping a shared data-plane component to recover a shared credential is what the same team's ChaosDB and Orca SynLapse already established. No exploit detail or PoC published.

---

## 46.5 — [CDN Tsunami: Exploiting HTTP/3-HTTP/1.1 Conversion for DoS Attacks](https://arxiv.org/abs/2607.26589) — Lin, Su, Lin, Gope, Cao, Liu, Sikdar

**REMOVED** · Meaningful extension · confidence High

**What is new.** The QPACK variant of proxy header-expansion amplification and the observation that it needs no victim-side configuration because CDNs enable HTTP/3 by default, plus a Tranco-1M measurement.

**What was already known.** The exact mechanism, a CDN decompressing headers into raw HTTP/1.1 toward the origin to amplify, is CDN Judo's HPACK attack from NDSS 2020, and slow-frame connection exhaustion through a proxy is long established; the paper itself frames its attack as the analogous conversion.

---

## 45.8 — [Before the first prompt: Code execution paths in trusted coding-agent projects](https://securitylabs.datadoghq.com/articles/coding-agent-project-trust-code-execution-before-first-prompt/) — Nick Frichette, Datadog Security Labs

**REMOVED** · Independent rediscovery · confidence High

**What is new.** A narrow variant plus detection value: prepending a malicious directory to PATH via project-local settings to intercept automatic startup subprocess invocations, distinct from the hooks path defenders were watching, plus ripgrep patterns usable immediately.

**What was already known.** The whole framing plus one half verbatim was published four months earlier without being cited: project-local config auto-executing on open, and the principle that such config is implicitly-trusted executable content.

---

## 45.5 — [Jupyter Enterprise Gateway: SSTI and YAML break-out to cluster takeover](https://www.elttam.com/blog/jupyter-enterprise-gateway) — Ben Cambourne, elttam

**REMOVED** · Useful application · confidence High

**What is new.** Only the target: three known injection classes found in one product's environment-variable path and chained to cluster admin.

**What was already known.** Everything load-bearing was established: SSTI as a class (Kettle 2015, in archive), YAML manifest injection, and user-controlled pod-spec fields escalating to Kubernetes takeover.

---

## 45.2 — [Same-site DOM XSS using cookie injection via the TikTok analytics pixel](https://medium.com/@renwa/site-dom-xss-using-cookie-injection-the-ai-hackers-are-coming-faster-than-you-think-3ef82f2a991d) — Renwa

**REMOVED** · Useful application · confidence Medium

**What is new.** One narrow observation: the pixel writes URL-decoded values straight into document.cookie and the reader regex splits on whitespace, so a plus sign smuggles a second pseudo-cookie, removing the usual subdomain-XSS precondition.

**What was already known.** Cookie-value-into-script-src is textbook DOM-based cookie manipulation, and injecting extra pairs through sloppy parsers is documented prior work; another researcher reported the identical bug seven days earlier.

---

## 44.8 — [Securing the Supply Chain: Cache Vulnerability in RubyGems](https://trufflesecurity.com/blog/rubygems-cache-vulnerability) — Luke Marshall, Truffle Security

**REMOVED** · Useful application · confidence High

**What is new.** The wrinkle that only the compressed representation was cacheable, so the bug hid behind a content-encoding vary: a reminder to retest each content-coding variant separately.

**What was already known.** A CDN storing an authenticated response because the origin sent no-cache without private while authorization was absent from the vary key is a textbook misconfiguration, mapped in detail by the web cache deception literature since 2017 and measured at scale in 2020 (both in archive).

---

## 44.5 — [HTTP Request Smuggling via `Connection: close<TAB>` in Node.js llhttp](https://hackerone.com/reports/3723248) — nadav0077

**REMOVED** · Useful application · confidence High

**What is new.** One concrete parser quirk: the llhttp Connection-token matcher takes a fallback path on HTAB that drops the pending close state, so Node keeps the connection alive and parses trailing bytes as a second request.

**What was already known.** That RFC 9110 OWS is SP/HTAB and parsers disagree on it is textbook, and llhttp has a long run of near-identical header-tolerance desync bugs (CVE-2022-35256). Adds a payload to the wordlist, not a mechanism; no end-to-end desync demonstrated.

---

## 44.2 — [Wrestling with a Python: Escaping Copilot Studio's AI-Guarded Sandbox](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Ryan%20Hausknecht%2C%20Simon%20Maxwell-Stewart%20-%20Wrestling%20with%20a%20Python%20Escaping%20Copilot%20Studio%27s%20AI-Guarded%20Sandbox%20-%20DEFCON2026%20embargo.pptx) — Ryan Hausknecht & Simon Maxwell-Stewart, BeyondTrust Phantom Labs *(the filename still reads "embargo"; it is the only published artifact)*

**REMOVED** · Independent rediscovery · confidence Low

**What is new.** The operational finding that an LLM-based guard is probabilistic rather than deterministic, with the same prompt failing or succeeding run to run, and that encoding plus prompt injection converts that into reliable success.

**What was already known.** The escape payload is the canonical Python jail ladder combined with string concatenation to defeat a substring filter; both halves have been standard pyjail canon for over a decade. The only artifact is a deck with a TODO placeholder and a redacted slide.

---

## 44.2 — [UI consent bypass via comma injection in Burp's MCP `addAutoApproveTarget`](https://hackerone.com/reports/3717354) — hacker-kartel

**REMOVED** · Useful application · confidence High

**What is new.** New only as an instance: one click on an attacker-supplied comma-joined host list persists four independent allow-list entries because the store joins on write and splits on read while the hostname passes through unvalidated.

**What was already known.** Injecting the delimiter of a delimiter-joined store so one displayed value becomes many stored values, with the consent UI showing something different from what is persisted, is a long-established class with no new primitive added.

---

## 44.0 — [Navigating Lax Load Balancers: When an Intersection Gets You Inside](https://blog.doyensec.com/2026/05/25/cloudsectidbits-elbaph-alb.html) — Lacerenza & Ouad, Doyensec

**REMOVED** · Tooling / methodology · confidence High

**What is new.** The tool plus the framing that reachability must be audited as a graph across every listener and load balancer rather than rule-by-rule.

**What was already known.** All three findings are established classes: hitting an internet-facing origin directly to skip the CDN and WAF is a decade old, listener-rule priority is documented behaviour so rule shadowing is a configuration consequence, and load-balancer authentication bypass was published as ALBeast in 2024.

---

## 43.8 — [Chaos by Design: The Death of Stochastic Race Conditions in HTTP/3](https://i.blackhat.com/BH-USA-26/Presentations/BHUS26-Chatzoglou-Chaos-by-Design-Slides.pdf) [Tool](https://github.com/efchatz/timeorch) — Chatzoglou, Kampourakis, Kambourakis, Stavrou

**REMOVED** · Meaningful extension · confidence Medium

**What is new.** Using QPACK Required-Insert-Count blocking as a deliberate synchronization gate, parking fully-parsed streams in proxy memory and releasing them with one byte, addresses the real problem that proxy buffering defeats wire-level alignment.

**What was already known.** Single-packet attack (Kettle 2023), first-sequence-sync (GMO Flatt 2024), CyberArk QuicDraw(H3) which already did last-byte-sync over HTTP/3 in 2025, and the same lead author's own Single Datagram Attack work. Slides also misattribute RFC 7540 priority weights to HTTP/3.

---

## 43.8 — [8 Out of 10 Banks in Belgium HATE This One Weird eID RCE](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20James%20Arnott%20-%208%20Out%20of%2010%20Banks%20in%20Belgium%20HATE%20This%20One%20Weird%20eID%20RCE%20-%20MEDIA%20SERVER%20Belgi.pdf) — James Arnott

**REMOVED** · Useful application · confidence High

**What is new.** The specific crypto failure chain in the vendor binary: a signed activation token with no origin or machine binding and a clock-rollback-defeatable TTL, a key derived from the even-indexed bytes of its own plaintext, and a substring extension check feeding a library load that a polyglot filename turns into drive-by RCE.

**What was already known.** The transferable residue, an extension forwarding page messages to a native host without carrying the caller origin, is precisely the class Space Raccoon systematised in 2024 (in archive), which even called out PKI smart-card extensions as the archetype.

---

## 43.5 — [The Forgotten Bug: How a Node.js Core Design Flaw Enables HTTP Request Splitting](https://r3verii.github.io/cve/2026/02/27/nodejs-toctou.html) — Martino Spagnuolo

**REMOVED** · Meaningful extension · confidence High

**What is new.** The framing that the CVE-2018-12116 fix is incomplete because the path regex runs only in the constructor while the header writer re-reads the mutable path at flush time, plus a seven-library ecosystem survey.

**What was already known.** That the path property is writable and read late was documented in nodejs/node#25864 (Feb 2019); the CRLF request-line primitive is classic (CVE-2018-12116; Bobrov 2023). Node rejected the report as by-design.

---

## 43.2 — [AgenticBlabbering: how AI browsers' verbose reasoning fuels the ultimate scamming machine](https://guard.io/labs/agenticblabbering---how-ai-browsers-verbose-reasoning-fuels-the-ultimate-scamming-machine) — Shaked Chen, Guardio Labs

**REMOVED** · Meaningful combination · confidence Medium

**What is new.** The framing that an agentic browser's verbose user-visible reasoning is itself an exploitable side channel, a free reward signal enabling black-box optimisation of a scam page against guardrails, plus a proxy extension for observing agent traffic.

**What was already known.** Agent-targeted scams that need only fool the AI (the same team's earlier work), generative phishing content, and automated iterative attack refinement against browsing agents. Evidence is one browser, one scenario, no released tooling.

---

## 43.2 — [Ghosts of Encryption Past: Salesforce Marketing Cloud / ExactTarget](https://slcyber.io/research-center/ghosts-of-encryption-past-salesforce-exacttarget/) — Pindur, Williamson, Shah, Kues

**REMOVED** · Useful application · confidence High

**What is new.** A hunting heuristic, that a platform still accepting a legacy ciphertext format alongside a modern one is only as strong as the legacy format when the key is static and shared across tenants, plus pairing the padding oracle with an in-product encryption oracle.

**What was already known.** The cryptanalysis is off-the-shelf: unauthenticated CBC padding oracles (Vaudenay 2002; Rizzo and Duong 2010, in archive), IV recovery with known plaintext structure, and repeated-key XOR; decryption used the existing padre tool.

---

## 43.0 — [CargoWise WebTracker — The Keys Were in the Cargo](https://slcyber.io/research-center/cargowise-webtracker-the-keys-were-in-the-cargo/) — Grobshäuser, Shah, Kues, Pindur

**REMOVED** · Useful application · confidence High

**What is new.** Only the product-specific chain: shipped keys turning an encrypted query string into attacker-controlled input, an auto-login token falling back to a hardcoded user, and handlers escaping the page-only session teardown.

**What was already known.** Every primitive was public: ViewState RCE with a known machine key (2019, in archive), the two-stage type-filter bypass (2019, in archive), the handler-versus-page auth-lifecycle gap (2023, in archive), and UNC-path NTLM leaks.

---

## 43.0 — [Remote-content-blocking and CSS-sanitizer bypasses in Roundcube's washtml via SVG `feImage` and SMIL animation attributes](https://hackerone.com/reports/3486747) — nullcathedral

**REMOVED** · Useful application · confidence High

**What is new.** One allowlist gap: the SVG filter href is routed through the link washer instead of the image check, so an off-screen filtered rect fetches a remote URL with image blocking on. The lesson is that SVG filter primitives also fetch external resources.

**What was already known.** Remote-content-blocking bypasses via SVG features in the same sanitizer, including the animate XSS fixed in Dec 2025 which is cited as the audit motivation. The entry title also claimed SMIL and CSS bypasses that are in a separate, uncited follow-up.

---

## 43.0 — [SECCON CTF 14 Finals: Shadow CSS and friends](https://blog.arkark.dev/2026/03/08/seccon-finals/) [Solver writeup](https://nanimokangaeteinai.hateblo.jp/entry/2026/03/02/235931) — arkark, st98

**REMOVED** · Useful application · confidence Medium

**What is new.** Only the assembly: header injection to emit a stylesheet Link response header (Firefox-only) so CSS injection reaches a closed shadow tree, with SRI validation against a size-varied response as a per-character oracle.

**What was already known.** Every component is established. CSS injection exfiltration (2018-2024, all in archive), closed shadow DOM documented as not a security boundary, and the SRI-as-oracle idea is the same author's own SECCON 2023 challenge, which the writeup points back to.

---

## 42.8 — [FCSC 2026 "Aquarium": escaping the Node.js Permission Model via `data:` URL import and `SIGUSR1` inspector activation](https://worty.fr/post/writeups/fcsc2026/fcsc_aquarium/) — \_Worty

**REMOVED** · Useful application · confidence Medium

**What is new.** A clean end-to-end demonstration plus an exfiltration detail for an egress-less container.

**What was already known.** Each primitive was public: data URLs are a documented import scheme, the spawn binding in an inspector context is an old jail escape, and the load-bearing step of signalling another process to open its inspector is an explicitly documented non-guarantee of the permission model that maintainers classify as intentional.

---

## 42.5 — [Can a Predicted `window.open` Target Really Be That Impactful?](https://lab.ctbb.show/research/can-a-predicted-window-open-target-really-be-that-impactful) — Achbani Ismail

**REMOVED** · Useful application · confidence High

**What is new.** A practical assembly detail: the hijacking iframe must be same-origin with the opener, satisfied by framing a static JS path that ships no frame-ancestors.

**What was already known.** The entire primitive, pre-registering a named browsing context so window.open resolves into the attacker frame, was filed against the HTML spec in 2016 and demonstrated as frame hijacking in 2008.

---

## 41.5 — [Ghost Dependency: version ghosts and name ghosts as supply-chain primitives under agentic coding](https://xlab.tencent.com/cn/2026/02/28/ghost-dependency-agentic-coding-supply-chain-threat/) — Tianchu Chen, Tencent Xuanwu Lab (Chinese)

**REMOVED** · Independent rediscovery · confidence High

**What is new.** At most the packaging: the version-ghost framing alongside name hallucination, and a pre-execution hook that intercepts an agent's install action to patch, retry or block.

**What was already known.** The entire name-ghost half, including registering the hallucinated name and watching downloads accrue, was demonstrated in 2023 and measured at scale in a 2025 distinguished paper; the post cites no prior work and its numbers come with no stated methodology.

---

## 40.5 — [postMessage targetOrigin bypass via IP normalization](https://lab.ctbb.show/research/postmessage-targetorigin-bypass-via-ip-normalization) — Mathias Karlsson

**REMOVED** · Duplicate / already known · confidence High

**What is new.** Only the specific payload shape using a decimal-integer host followed by the expected domain as a path, which matches a subdomain regex on the raw string while the URL parser normalises the host and discards the rest.

**What was already known.** Both halves are old: WHATWG IPv4 parsing of decimal hosts is spec-documented and in every URL-validation cheat sheet, and targetOrigin ignoring the path was discussed on the WHATWG list in 2010 and filed with Gecko in 2016.

---

## 39.2 — [Mini Shai-Hulud Returns: 42 Malicious npm Packages Fake Sigstore Badges](https://www.endorlabs.com/learn/mini-shai-hulud-returns-42-malicious-npm-packages-fake-sigstore-badges-in-antv-ecosystem-attack) — Peyton Kennedy, Endor Labs

**REMOVED** · Duplicate / already known · confidence Medium

**What is new.** Telemetry-backed incident reporting on a follow-on wave with useful indicator inventory and a dormant-account targeting observation.

**What was already known.** The headline mechanism, the worm minting valid provenance at install time so packages are indistinguishable from legitimate releases at the verification layer, was documented for the first wave a week earlier.

---

## 38.5 — [Elasticsearch Painless execution via a pass-through `sort_query` GraphQL argument](https://hackerone.com/reports/3694007) — disclosed by HackerOne

**REMOVED** · Useful application · confidence Medium

**What is new.** A testing heuristic, that an untyped string argument beside a typed input lets you bypass the schema and hand raw query DSL to the backend, and a differential-ordering trick to prove script execution with no output channel.

**What was already known.** The class is long documented as search injection (Solr Injection 2019, in archive), script-injection CVEs run back to 2014, and scripted sort is a documented feature. The scripting language is sandboxed, so the code-execution framing outruns what was demonstrated.

---

## 38.5 — [OAuth Client ID Spoofing: Why Fake Client IDs Are Gaining Traction for Stealthy Enumeration](https://www.proofpoint.com/us/blog/threat-insight/oauth-client-id-spoofing-why-fake-client-ids-are-gaining-traction-stealthy) — Rachel Rabin, Proofpoint

**REMOVED** · Useful application · confidence Medium

**What is new.** The narrow observation that the identity provider evaluates credentials before validating that the client ID corresponds to a registered application, so fabricated IDs still leak account and password validity while the log rows carry a blank application name.

**What was already known.** Legacy-endpoint credential validation producing no successful-sign-in event, and error-code differentials revealing account state, were published by Secureworks in 2021 with tooling from 2020. Campaign size and press coverage carry no weight.

---

## 38.2 — [Unauthenticated RCE in Taskcluster via a GraphQL filter reaching sift's `$where`](https://hackerone.com/reports/3782701) — griffinf

**REMOVED** · Duplicate / already known · confidence High

**What is new.** One well-evidenced instance on an unauthenticated endpoint plus a blind-context trick, throwing an error to smuggle command output back through a filter response.

**What was already known.** The exact primitive, an untrusted JSON filter reaching a query library where-clause compiled with Function, was published in the Mongoose CVE-2024-53900 research 18 months earlier, and the underlying JavaScript injection is over a decade old.

---

## 37.5 — [Domain Decoupling Attack: Exploiting the Validation Gap Between Protective DNS and Shared Edge Routing](https://arxiv.org/abs/2608.00643) — Wang, Dong, Li et al.

**REMOVED** · Duplicate / already known · confidence High

**What is new.** Only the framing against modern DNS-derived IP authorisation and a one-million-domain measurement, plus a co-location chain notion extending one domain pair to a group of co-tenants.

**What was already known.** That an IP allowlist derived from a DNS answer does not bind to a domain on a name-based-virtual-hosting or multi-tenant address is structural and long-standing, and the paper's own related work concedes domain fronting, borrowing and shadowing cover the evasion goal; the headline exposure figure is close to definitional.

---

## 36.2 — [Install Me Maybe: Turning Claimable VS Code Extension IDs into Supply-Chain Attacks](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Raphael%20Silva%20-%20Install%20Me%20Maybe%20Turning%20Claimable%20VS%20Code%20Extension%20IDs%20into%20Supply-Chain%20Attacks%20-%20v1.pdf) — Raphael Silva, Aikido

**REMOVED** · Independent rediscovery · confidence Medium

**What is new.** At most breadth: cataloguing where extension IDs travel and a mass registration-and-callback measurement.

**What was already known.** The entire primitive, separate namespace ownership between Marketplace and Open VSX making a trusted name claimable on the other, was published by Koi Security in January 2026 including the same methodology; underneath it is Birsan dependency confusion aimed at a new registry. The deck has a TO BE FINISHED slide.

---

## 35.1 — [Bandwidth amplification with a factor of x783 caused by HTTP/2 → HTTP/1.1 translation in Cloudflare](https://habr.com/ru/articles/1063428/) — tnkwa (Russian)

**REMOVED** · Independent rediscovery · confidence High

**What is new.** Only the measurement: that Cloudflare defaults to HTTP/1.1 toward origins and that repeated identical long headers ride the HPACK dynamic table down to 1-3 byte indices for a 783x factor against one named CDN.

**What was already known.** This is the published HTTP/2 Tsunami attack, HPACK indexing weaponised through H2-to-H1 translating proxies, demonstrated in 2017 against nginx and nghttp2 at up to 196x. The post cites no prior work.

---

## 34.8 — [A Billion-User Blast Radius: Owning ChatGPT's Secure Sandbox](https://appsecvillage.com/events/dc-2026/a-billion-user-blast-radius-owning-chatgpt-s-secure-sandbox-1248604) — Simcha K, Palo Alto Networks

**REMOVED** · Insufficient evidence · confidence Low

**What is new.** Unassessable. The only public artifact is a village abstract for a talk given the day of evaluation; no writeup, paper, PoC or vendor blog exists.

**What was already known.** Sandbox exploration and file-read escapes in the same product were published from 2023, and prompt-injection exfiltration channels are long documented. No prior art found for the rate-limit-as-covert-channel claim, but it cannot be verified either.

---

## 34.7 — [Cline Kanban WebSocket Hijack](https://www.oasis.security/blog/cline-kanban-websocket-hijack) [Breaking the Paperclip](https://www.oasis.security/blog/paperclip-agent-vulnerabilities) — Sagi Layani, Oasis Security

**REMOVED** · Duplicate / already known · confidence High

**What is new.** Nothing at the mechanism level: two products found vulnerable to origin-unchecked local WebSocket access and DNS rebinding past localhost isolation.

**What was already known.** Cross-site WebSocket hijacking, DNS rebinding and unauthenticated localhost dev servers are all long established, and the specific framing was published by this same team three months earlier, making these applications of their own prior class to further targets.

---

## 34.0 — [Trailing-dot hostname normalisation in curl: IP-literal guard bypass to wildcard SAN match, and multi-dot HSTS bypass](https://hackerone.com/reports/3734921) [Multi-trailing-dot HSTS](https://hackerone.com/reports/3733984) — giant_anteater

**REMOVED** · Useful application · confidence High

**What is new.** A real pointer and length desync: the host matcher decrements the length to strip a trailing dot but passes the unstripped pointer to the IP-literal guard, so an IP-literal URL gets wildcard-matched against a DNS SAN.

**What was already known.** The HSTS half is explicitly an incomplete-fix variant of curl CVE-2022-30115 (2022), whose advisory already noted similar issues in Firefox and Chrome. curl closed both Informative.

---

## 33.0 — [DOMPurify mXSS via Re-Contextualization (CVE-2026-0540)](https://fluidattacks.com/advisories/daft) — Camilo Vera, Cristian Vargas, Scott Moore

**REMOVED** · Duplicate / already known · confidence High

**What is new.** Essentially only the extension of an already-published bypass to five more raw-text element names missing from the DOMPurify regex.

**What was already known.** CVE-2025-15599 (VulnCheck, Mar 2026) is the identical mechanism using textarea over the same version range, and the DOMPurify wiki documents the class as attack class 5.

---

## 32.0 — [BioShocking AI: "Gaming" the AI Browser and Escaping its Guardrails](https://layerxsecurity.com/blog/bioshocking-ai-gaming-the-ai-browser-and-escaping-its-guardrails/) — Roy Paz, LayerX

**REMOVED** · Duplicate / already known · confidence High

**What is new.** Essentially nothing at the mechanism level; the finding is that six agentic browsers rather than one fall to it, which is coverage.

**What was already known.** Roleplay and fictional-framing jailbreaks are among the oldest published guardrail bypasses, and persisting an injected frame via assistant memory was published in 2024. The writeup asserts a new class without a mechanism beyond game logic replacing safety logic.

---

## 32.0 — [Dollar-Quote Bypass: Blind SQLi Against Regex-Sanitized Dynamic PL/pgSQL](https://jrbusiness.github.io/Dollar-Quote-Desync/) — Jerry Luong

**REMOVED** · Duplicate / already known · confidence High

**What is new.** Nothing new as a primitive.

**What was already known.** Dollar-quoted literals to avoid single quotes are standard PostgreSQL-injection material, injection at the unquoted identifier position is the anti-pattern the PostgreSQL docs warn about, and boolean-oracle extraction is decades old. The author admits only that the combination seemed undocumented; the demo is a purpose-built function and the payloads are blocked by default CRS.

---

## 31.8 — [Duplicate chunked `Transfer-Encoding` smuggles a response across reused proxy connections in curl](https://hackerone.com/reports/3795615) [Bare-LF variant](https://hackerone.com/reports/3785919) — violet12331

**REMOVED** · Useful application · confidence Medium

**What is new.** A precise code-level guard bypass: the duplicate-chunked branch returns success for the whole header, so the chunked-must-be-last rejection is never reached.

**What was already known.** Duplicate and obfuscated Transfer-Encoding as a desync primitive (Kettle 2019; curl issue 13451 in 2024) and response-queue desync over reused connections (Doyhenard, DEF CON 29, in archive). curl closed this Informative and the sibling Not Applicable; both presuppose an attacker-controlled origin that could emit Set-Cookie directly.

---

## 31.2 — [SSRF filter bypass via the RFC 8215 local-use NAT64 prefix `64:ff9b:1::/48`](https://hackerone.com/reports/3634400) — tipsen

**REMOVED** · Duplicate / already known · confidence High

**What is new.** Nothing but one missing CIDR: the gem blocked the well-known NAT64 prefix and omitted the RFC 8215 local-use sibling.

**What was already known.** Reaching internal IPv4 through an alternate IPv6 representation is the founding idea of SSRF-blocklist bypass (Orange Tsai, BH 2017, in archive), and this exact gap was reported across at least five unrelated projects in the same period.

---

## 30.2 — [Nested APP Authentication — Undocumented Risk and Conditional Access Bypass](https://troopers.de/troopers26/talks/ezcteq/) — Shang-De Jiang & Jun Sheng Shi, CyCraft

**REMOVED** · Insufficient evidence · confidence Low

**What is new.** Claimed but unverified: two bypass families and a token exchange reaching the resource manager, the latter of which would go beyond the closest public work.

**What was already known.** The headline result, broker token exchange skipping conditional-access evaluation, was published in full technical detail by NetSPI two days before this talk, and the underlying brokered-cross-client primitive traces to Secureworks 2022. The page is an abstract only, with slides and video marked coming soon.

---

## 30.0 — [Reflections on Disregarding Trust: Weaponizing CDP and MHTML for Header-Agnostic Session Hijacking](https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20presentations/DEF%20CON%2034%20presentations/DEF%20CON%2034%20-%20Gregory%20Disney-Leugers%20-%20Reflections%20on%20Disregarding%20Trust%20%28Weaponizing%20CDP%20and%20MHTML%20for%20Header-Agnostic%20Session%20Hijacking%29%20-%201umberhac.pdf) — Gregory Disney-Leugers

**REMOVED** · Insufficient evidence · confidence Medium

**What is new.** Two potentially new ideas: using a display-isolated browser error page as a telemetry-blind staging ground where the debug protocol retains control, and reaching component-extension privilege via an internal RPC key.

**What was already known.** The cited artifact is a 46-page deck that is almost entirely images with bullet-point assertions, no PoC, no whitepaper, one linked tool that is an unrelated generic proxy and another returning 404. Debug-protocol session hijacking and browser-in-the-middle session stealing including keylogging and profile theft were published in March 2025.

---

## 26.8 — [curl HTTP/2 server push accepts a non-authoritative `:scheme=https` over cleartext h2c](https://hackerone.com/reports/3630310) [Incomplete fix](https://hackerone.com/reports/3674275) — argareksapatii

**REMOVED** · Duplicate / already known · confidence High

**What is new.** A conformance gap in one library: the pushed URL is built from a server-supplied scheme without checking it against the connection.

**What was already known.** RFC 7540 section 8.2 (2015) already requires clients to verify push authority, and pseudo-headers as spoofable cache-key input was published years earlier. curl closed both reports Informative; server push is deprecated everywhere.

---

## 22.5 — [ROP for the Web: Smuggling XSS, SQLi and Web Shells Past Every WAF Using Compression Dictionaries](https://appsecvillage.com/events/dc-2026/rop-for-the-web-smuggling-xss-sqli-and-web-shells-past-every-waf-using-compression-dictionaries-1250560) — Lenin Alevski

**REMOVED** · Insufficient evidence · confidence Low

**What is new.** Unassessable. The only artifact is a session listing for a workshop scheduled two days after evaluation, with no slides, whitepaper or released tool; the speaker's blog carries nothing on the topic.

**What was already known.** The abstract's idea is plausible but does not address the RFC 9842 same-origin dictionary restriction; hiding payloads from signature engines behind content-coding is long-standing WAF-evasion practice.

---

## 15.5 — [The Hidden Cost of Sanitization: How Secure Parsing Can Introduce New XSS Attack Surfaces](https://nullcon.net/talk/the-hidden-cost-of-sanitization-how-secure-parsing-can-introduce-new-xss-attack-surfaces/) [Video](https://www.youtube.com/watch?v=BJCgSLGq308) — Ashish Kataria

**REMOVED** · Insufficient evidence · confidence Low

**What is new.** Unassessable. The talk page 403s, the linked video yielded no transcript, no slides or paper exist, and the only recoverable text is a three-sentence promotional abstract naming no mechanism or sink.

**What was already known.** Not assessable without a mechanism. Confirmed only that the talk is real. A flag-for-revisit, not a judgement that the work lacks value.

---

## 14.8 — [Demystifying the (In)Security of OAuth-based Account Linking in Connector Ecosystems](https://sp2026.ieee-security.org/accepted-papers.html) — Luo, Wang, Fung, Lau, CUHK

**REMOVED** · Insufficient evidence · confidence Low

**What is new.** Unassessable. The cited URL is an accepted-papers list yielding only title and authors; there is no abstract, PDF or preprint.

**What was already known.** What is public from the same group is adjacent and substantial, a USENIX 2025 paper on cross-app OAuth account-linking attacks, so the marginal contribution over it is exactly the unknown.

