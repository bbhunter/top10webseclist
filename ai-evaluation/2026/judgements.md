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

## 71.2 — [We Need to Talk About CSRF Again](https://blog.voorivex.team/we-need-to-talk-about-csrf-again) — Amirmohammad Safari, Voorivex

**KEPT** · Meaningful extension · confidence Medium

**What is new.** A fourth CORS-safelisted content type that the Fetch standard does not list: Chromium safelists `message/ad-auction-trusted-signals-request` for the Protected Audience API behind `kProtectedAudienceCorsSafelistKVv2Signals`, enabled by default, so a cross-origin POST carrying it took no preflight in every Chromium browser. That defeats the whole content-type-allowlist/blocklist family of CSRF defences rather than one implementation of it, demonstrated against Express and Apollo Server and then amplified into an XS-Leak: Apollo automatic persisted queries prime 36 hash-addressed queries, GraphQL aliases inflate a hit to tens of kilobytes, and `performance.getEntriesByName()` reads the fast/slow split back character by character. Chromium has since replaced the default-on flag with a per-request `TrustedParams` bool.

**What was already known.** The safelist-of-three and its CSRF consequence are textbook, the FastAPI half (an absent `Content-Type` parsed as JSON) is credited by the author to an earlier write-up, and timing XS-Leaks are long established. The load-bearing claim is that the browser's real safelist is wider than the specified one, which no earlier public source I could find had noted; a failed search is not proof of first discovery, hence Medium confidence and the separate attribution of the Chromium fix.

---

## 71.1 — [The State of Passkeys: Studying the Adoption and Security of Passkeys on the Web](https://www.usenix.org/conference/usenixsecurity26/presentation/jannett) [Paper](https://github.com/RUB-NDS/state-of-passkeys-artifacts/blob/main/paper.pdf) [Artifacts](https://github.com/RUB-NDS/state-of-passkeys-artifacts) [Tool](https://passkeys.tools) — Jannett, Mayer, Westers, Mladenov, Mainka, Schwenk

**KEPT** · Tooling / methodology · confidence High

*(Fourth re-check round, 14 August 2026.)*

**What is new.** PASSKEYS-ATTACKER emulates *both* the client and the authenticator layer, so every WebAuthn field can be altered at every step of registration and authentication — which is what makes relying-party validation testable at all. 15 attack types and 28 detection methods were run against 103 live RPs under a plain web-attacker model (victim browser and authenticator assumed honest): all 103 fail at least one, 53 at high severity, 18 at critical. The load-bearing new attack type is **Credential Overwrite** — the attacker registers their own public key under the *victim's* credential ID, which RPs hand out unauthenticated, so one credential appears to belong to two users; depending on how the RP resolves the duplicate the victim is locked out or the account is taken over. Five sites skip signature verification outright. PASSKEYS-RADAR adds a continuously updated adoption dataset (872 RPs; domain scanning finds ~125% more than all 12 community directories combined), and the whole thing — scanner, tool, Chrome extension, deliberately vulnerable learning platform — is released.

**What was already known.** RP-side WebAuthn evaluation exists, but small and under different attacker models: Grammatopoulos et al.'s WebDevAuthn assessed 16 RPs for conformance, [Kuchhal et al. (CCS 2023)](https://dl.acm.org/doi/10.1145/3576915.3623063) studied 29 RPs assuming a *compromised client*, and Yadav et al. covered local threats such as malicious extensions. Most of the 15 attack types are checks WebAuthn §7.1/§7.2 already mandates, so the catalogue systematises the standard more than it invents attacks; credential-binding confusion has precedent in the FIDO2 mis-binding literature and in [w3c/webauthn issue #579](https://github.com/w3c/webauthn/issues/579) on vague credential-ID uniqueness, though not previously demonstrated across live RPs. A concurrent adoption census exists ([Bhardwaj & Sastry, PAM 2026](https://arxiv.org/abs/2602.15135), Fidentikit over the Tranco 100K) but measures deployment only, with no security testing. Distinct from the three passkey items already judged for 2026: Pass-the-Passkey (73.0) attacks Windows Hello/Entra credential material, the Unit 42 post (54.5) and Beyond the Ceremony (48.0) survey the ceremony — none test RP server-side validation at scale.

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

## 66.3 — [JavaScript Functions Overload Confusion](https://blog.voorivex.team/javascript-functions-overload-confusion) — Yashar Shahinzadeh, Voorivex

**KEPT** · Tooling / methodology · confidence Medium

**What is new.** The census, not the trick. Walking 2,228 Blink IDL files to ask which overloaded operations resolve on argument *type* and then reach a sink or a security decision: 112 operations are genuinely overloaded, about 30 reach a sink, only 4 type forks gate a security decision, 2 fork on argument count, and about 22 Trusted Types sinks fork on genuine-object-versus-string inside C++ — so a value that is a string to the check and an object to the sink walks past enforcement. That map of where validator and sink can disagree on one value did not exist publicly.

**What was already known.** The primitive itself: structured clone preserves an array's named own properties while the array stringifies to its single element, so one value satisfies two type expectations. That is documented community postMessage-exploitation material, and the specific case came from a challenge by joaxcar that the author solved before generalising. `setTimeout` compiling non-callables and `document.write` forking on `TrustedHTML` are specified behaviour. Scored down for soundness and reproducibility: the enumeration is author-reported as LLM-assisted and no tool, repo or full table is published, so the census cannot be independently re-run from the post.

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

## 64.7 — [When HTTP 402 Meets the Blockchain: Risks on Emerging x402 Payments](https://www.usenix.org/conference/usenixsecurity26/presentation/wang-qinying) [Paper](https://arxiv.org/abs/2607.19545) [Tool](https://github.com/HexHive/x402scope) — Qinying Wang, Yong Yang, Yuan Chen, Shouling Ji, Mathias Payer

**KEPT** · Meaningful extension · confidence Medium

*(Fourth re-check round, 14 August 2026.)*

**What is new.** Treats the x402 *facilitator* — the shared third party that verifies payment proofs and settles them on-chain for many independent merchants — as security infrastructure, and distils eight checkable rules over it, split into authorization correctness (SR1–SR4) and execution safety (SR5–SR8). The reusable core is the SR4 gap: a facilitator that returns `valid` before settlement actually succeeds makes *verified* and *paid* two different facts, and the merchant gates access on the wrong one — the Coinbase Flask SDK v0.2.1 releases the resource after verification alone. The execution-safety half has no analogue in earlier payment-logic work: because facilitators sponsor gas, proofs chosen to revert, or ERC-1271/6492 contract-wallet signature checkers running attacker-supplied code, turn a third party's wallet into an unbounded cost sink (Gas Abuse). X402SCOPE is released and does capability discovery before testing so it only fires applicable probes; 15 facilitators carrying 99% of x402 traffic yield 49 rule violations and 31 previously unknown vulnerabilities, every facilitator violating at least one rule, alongside a 119M-transaction measurement.

**What was already known.** The method — derive the invariants of a three-party payment flow, then test merchants and the shared cashier against them — is [How to Shop for Free Online (S&P 2011)](https://www.ieee-security.org/TC/SP2011/PAPERS/2011/paper029.pdf), whose own term "free shopping" this paper reuses, and the e-commerce logic-flaw line that followed it (NDSS 2014; multi-party black-box attack patterns 2016-17), all three already in the archive. Closer and more awkward: [Five Attacks on x402 Agentic Payment Protocol](https://arxiv.org/abs/2605.11781) (Li, Q. Wang, Z. Wang, 12 May 2026) published authorization, binding, replay-protection and web-layer attacks on x402 two months earlier and is **not cited here** — concurrent and independent, but the public record was not empty. What survives as this paper's own: the facilitator-side rule set, the sponsored-execution attack class, and the scale.

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

## 59.3 — [The Usual Suspect: Type Confusion in Twelve Bytes](https://blog.voorivex.team/usual-suspect-type-confusion-in-twelve-bytes) — HamidSj, Voorivex

**REMOVED** · Meaningful extension · confidence Medium

**What is new.** A reusable observation about magic-byte sniffers rather than about one library: ISO-BMFF detection in `file-type` matches `ftyp` at offset 4 and the brand at offset 8 but never validates the 4-byte box-size field at offset 0, so any format sniffed by a suffix of its header hands the attacker free control of the bytes *before* the magic — exactly where a comment opener has to go. `/*` there and `*/` after the brand yields a file that is a valid HEIC to the validator and valid JavaScript, HTML, CSS or JSON to the consumer.

**What was already known.** Polyglot uploads and comment-wrapped image headers are old (GIF89a= as a JS assignment is the canonical example), detection-versus-consumption gaps are the standard framing, and the author positions the work as the same pattern they previously described for libmagic. One library, one version, and served-by-extension is the precondition doing most of the work; the score lands just under the keep-cut on marginal novelty, not on quality.

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

## 59.1 — [Patch-Guided Vulnerability Detection: Extracting Java API Security Rules via Attack–Defense Cross-Analysis (VulGenie)](https://www.usenix.org/conference/usenixsecurity26/presentation/chen-bofei) [Artifact](https://zenodo.org/records/18039660) — Chen, Liao, Zhang (Fudan); Zhang, Payer (EPFL)

**REMOVED** · Tooling / methodology · confidence Low-Medium

*(Fourth re-check round, 14 August 2026. USENIX 403s automated fetches, so this was judged from the abstract, the Zenodo artifact record and secondary summaries — **re-judge if the full text becomes readable**.)*

**What is new.** A denoising step that most patch-mining work skips: a modification-behaviour dependency patch graph isolates the constraint the patch actually added from the refactoring around it, and attack–defense cross-validation then decides which security-sensitive API that constraint was protecting. Deviation-guided static analysis keeps the resulting rules affordable to run. 198 rules from 150 Java patches at 81.82% precision, 177 of them with no CodeQL equivalent, 46 0-days across ten Java applications and ten CVEs.

**What was already known.** Deriving misuse rules by diffing insecure against fixed code is SEADER's approach (21 misuse templates from 28 code pairs) and the data-driven / example-based Java vulnerability-detection line before it; "security patches encode an invariant" is the standing premise of that whole field. Web bearing is indirect — this is a Java API-misuse detector whose targets happen to be web applications, closer in kind to the Bullseye prototype-pollution detector (57.8, removed) than to the gadget-chain work kept at 68.8.

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

## 57.7 — [Three 0-Day Vulnerabilities in Adminer](https://blog.voorivex.team/three-0-day-vulnerabilities-in-adminer) — Yashar Shahinzadeh & Amirmohammad Safari, Voorivex

**REMOVED** · Useful application · confidence High

**What is new.** Three concrete primitives against a database client, of which two transfer past the product. A malicious MySQL server controls the version banner, and Adminer's `~^(\d\.?\d).*~s` extraction returns the raw string when the match fails — landing attacker text inside a `<script>` that already carries a valid CSP nonce, so the policy signs the payload. That "the server you connect to is untrusted input" pattern applies to any DB-admin UI. `VACUUM INTO` also survives a blocklist that only knows `ATTACH`, a useful note on blocklists chasing named statements instead of capabilities.

**What was already known.** ODBC DSN injection through unsanitised connection strings, and `TraceFile`/`TraceOn` as the write primitive, are established MSSQL tradecraft. `VACUUM INTO` as a file-write has been documented since at least the 2020 osquery discussion and sits in PayloadsAllTheThings. Rogue-MySQL-server attacks on Adminer are a line the same team already contributed to (the file-read that became CVE-2021-43008). Good vulnerability research, low class novelty.

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

## 55.3 — [Shaking the MCP Tree: a security deep dive](https://blog.voorivex.team/shaking-the-mcp-tree) — Amirmohammad Safari, Voorivex

**REMOVED** · Useful application · confidence Medium

**What is new.** An early field survey of what unprotected RFC 7591 Dynamic Client Registration actually buys an attacker on real MCP deployments: self-registering a client with a `javascript:` redirect URI to reach a client-side redirect handler, `redirect_uri` reflected into a consent-screen script, an encoded-`../` path-normalisation escape chained with an OAuth open-redirect gadget for SSRF, and authenticating straight to MCP endpoints that assume only an assistant will ever call them.

**What was already known.** The author says so directly — "the attack techniques I'm about to show you aren't brand new" — and credits PortSwigger's OAuth work as the base. Open DCR abuse, `javascript:` redirect URIs, consent-screen reflection and normalisation bypasses are each long established; what changes is the deployment surface, and 2026 already carries several MCP entries that go further into mechanism.

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

## 54.9 — [When Two Parsers Disagree: Exploiting Query String Differentials for XSS](https://blog.voorivex.team/when-two-parsers-disagree-exploiting-query-string-differentials-for-xss) — Amirmohammad Safari, Voorivex

**REMOVED** · Useful application · confidence Medium

**What is new.** Two specific disagreements between Express's `qs` and the browser's `URLSearchParams`, packaged as a 20-line reproducible challenge: `qs` splits on `]=` in preference to a plain `=`, so the two parsers disagree about where the key ends; and `qs` strips bracket notation while honouring a 1000-parameter default limit that `URLSearchParams` does not, so a payload parked past the limit is invisible to the validator and visible to the page. The framing — server validates, client executes, `redirect_uri` as the realistic sink — is the useful part.

**What was already known.** Parser-differential exploitation is a deep line: HTTP Parameter Pollution (2009, in archive), the year-2025 syntax-confusion work already in `2025.md`, and `qs`'s bracket-notation quirks are documented in its own issue tracker and advisories. No prior work is cited in the post. A well-built teaching artifact rather than a new primitive.

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

## 53.0 — [Salesforce Apex Predator: Breaking Salesforce Sites](https://dcworkshop.reco.ai/) [Field manual](https://www.reco.ai/blog/salesforce-experience-site-pentest-apex-predator) [LWRed](https://github.com/nitay-bachrach/lwred) — Nitay Bachrach & Cynthia Ardman, Reco

**REMOVED** · Meaningful extension · confidence Medium

*(Fourth re-check round, 14 August 2026.)*

**What is new.** The material increment is the *next-generation* Salesforce site framework rather than Aura: an undocumented `RecordUiController.executeGraphQL` method that runs GraphQL directly against the org, full route enumeration through `ComponentController.getComponent` with `siteforce:routerInitializer`, and recovering callable custom Apex methods out of compiled LWC bundles by tracing import indices to invocation sites. Packaged as six live labs, two field manuals and the LWRed recon tool, which is what makes it usable rather than just readable. The transferable lesson is stated cleanly: reachable API surface is not what page crawling shows you.

**What was already known.** Everything on the Aura half is long-established — Aaron Costello's October 2020 work on calling Aura controllers as an anonymous guest user, the `@AuraEnabled` system-context problem, AppOmni's Apex-security treatise and Mandiant's Aura data-exposure auditing guidance. SOQL injection, guest-user object enumeration and unauthenticated route discovery are standing practice on this platform, so the marginal contribution is the LWR/GraphQL surface and the enumeration mechanics around it, on one SaaS product.

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

## 52.5 — [PANGOLIN: Fuzzing Multilingual IoT Firmware with LLM-Driven Code Analysis](https://www.usenix.org/conference/usenixsecurity26/presentation/jia-zhipeng) — Jia, Zhipeng et al.

**REMOVED** · Tooling / methodology · confidence Low-Medium

*(Fourth re-check round, 14 August 2026. Judged from the abstract and secondary summaries; USENIX 403s automated fetches.)*

**What is new.** The cross-language step: IoT web services are split across C, Python and Lua, so an LLM agent reads the dispatch mechanism in one language and reconstructs parameter specifications that are consumed in another, with response-driven feedback correcting the specification before it is handed to a semantics-aware fuzzer. 68 previously unknown vulnerabilities, 45 of them behind interfaces the frontend never exposes, 31 identifiers assigned.

**What was already known.** That a large share of an embedded device's HTTP attack surface never appears in the frontend, and that you recover it from the dispatcher rather than from the UI, is exactly [EAGLEYE (NDSS 2025)](https://www.ndss-symposium.org/wp-content/uploads/2025-399-paper.pdf) — hidden web interfaces in IoT devices via routing analysis — and IoT firmware fuzzing from snippet or message inference (IoTFuzzer, Snipuzz) predates both. The new component is the multilingual analysis, not the hidden-interface insight. Web bearing is real but narrow: the finding classes are the usual command injection, XSS and file upload on embedded HTTP servers.

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

## 52.1 — [uXSS on Samsung Browser (CVE-2025-58485 · SVE-2025-1879)](https://blog.voorivex.team/uxss-on-samsung-browser-cve-2025-58485-sve-2025-1879) — Omid Rezaei & Yashar Shahinzadeh, Voorivex

**REMOVED** · Useful application · confidence High

**What is new.** The concrete asymmetry: `BixbySBrowserLauncherActivity` validates the incoming intent, `SBrowserMainActivity` is exported and does not, so an intent carrying `extra_access_url=javascript:…` reaches the currently loaded page and executes in its origin. The transferable habit is the one the authors name — read `AndroidManifest.xml` for exported components and check whether the guard sits on the entry point an attacker actually has to use, rather than intercepting traffic.

**What was already known.** Universal XSS through an exported Android activity that accepts a `javascript:` URL is a well-trodden class with a long CVE trail across mobile browsers, and "validation on one entry point, none on the sibling" is the standard shape of it. First public disclosure is February 2026 (reported September 2025, patched January 2026), so it is judged as 2026 work despite the 2025 CVE year. Large blast radius, which the rubric deliberately does not reward.

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

## 50.1 — [Story of Abusing a Fully Secured redirect_uri in an OAuth Flow](https://blog.voorivex.team/story-of-abusing-a-fully-secured-redirect-uri-in-an-oauth-flow) — Yashar Shahinzadeh, Voorivex

**REMOVED** · Useful application · confidence Medium

**What is new.** A clean worked example of decode-count asymmetry surviving genuinely strict validation: the validator decodes once and sees `a.com%23@www.company.com`, reading the allow-listed host as the authority, while the redirect path decodes again so the browser sees a real `#` and treats `a.com` as the destination with the authorization code in the fragment. The reusable rule is to count decodes on each side rather than to test the validator in isolation.

**What was already known.** Double-encoding past a validator, and `@` userinfo confusion between a checker and a parser, are foundational URL-confusion material — Orange Tsai's URL-parser work and the long lineage of `redirect_uri` bypasses already in the lists. One target, no tool, and the primitive is unchanged.

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

## 44.5 — [My First RCE by Reverse Engineering an EXE File With the Help of AI](https://blog.voorivex.team/first-rce-via-reverse-engineering-with-ai) — Yashar Shahinzadeh, Voorivex

**REMOVED** · Useful application · confidence High

**What is new.** Little, and the post says so. A vendor's Windows service listens on `ws://127.0.0.1:3100`, never checks `Origin`, and exposes a `{RUN:'DRIVE', URL:…}` method that falls back to launching `explorer.exe` with attacker-supplied arguments, so any web page reaches command execution. The only durable observation is the eight-year persistence of the anti-pattern.

**What was already known.** The author names the prior art himself: Tavis Ormandy's 2018 Electrum finding is the same shape, and cross-site WebSocket hijacking against unauthenticated localhost services has been a standing class since. The AI-assisted reverse-engineering framing is methodology colour, not a contribution to it.

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

## 43.0 — [Remote-content-blocking and CSS-sanitizer bypasses in Roundcube's washtml via SVG `feImage` and SMIL animation attributes](https://hackerone.com/reports/3486747) [SMIL values and by](https://hackerone.com/reports/3590576) [Unquoted body background](https://hackerone.com/reports/3590583) [Fixed-position override](https://hackerone.com/reports/3590586) [Round one](https://nullcathedral.com/posts/2026-02-08-roundcube-webmail-svg-feimage/) [Round two](https://nullcathedral.com/posts/2026-03-18-roundcube-round-two-three-more-sanitizer-bypasses/) — nullcathedral

**REMOVED** · Useful application · confidence High

*(Amended in the fifth re-check round, 18 August 2026: the follow-up bypasses this entry's title always claimed are now cited here rather than left uncited, and the author's own two posts are recorded as the real first publication — 8 February and 18 March 2026 — ahead of the April platform disclosure. The code is Roundcube's `rcube_washtml`; the reports are filed against Nextcloud Mail because it bundles it.)*

**What is new.** One allowlist gap: the SVG filter href is routed through the link washer instead of the image check, so an off-screen filtered rect fetches a remote URL with image blocking on. The lesson is that SVG filter primitives also fetch external resources. The three follow-ups add marginally to that, and only one has reach beyond the product: the earlier patch blocked SMIL animation only where the animated attribute was the hyperlink reference, so animating other fetching attributes still loads remote content — patching one attribute name does not patch the class — with multi-value timing lists giving dwell-time beacons and cursor animation giving hover tracking. The other two are textbook: a closing parenthesis inside a data URI escaping an unquoted URL built by string concatenation, and an importance override defeating an exact-match position check.

**What was already known.** Remote-content-blocking bypasses via SVG features in the same sanitizer, including the animate XSS fixed in Dec 2025 which is cited as the audit motivation. Unquoted-URL CSS injection is a standard class, and a vendor writeup had already covered overlay-link phishing through this client's CSS filter. The judged CSS: the bomb inside your inbox (77.0) is not prior art, being later, but now occupies this ground far more deeply.

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

## 42.0 — [Two cPanel Zero Day Vulnerabilities](https://blog.voorivex.team/two-cpanel-zero-day-vulnerabilities) — Yashar Shahinzadeh & Amirmohammad Safari, Voorivex

**REMOVED** · Useful application · confidence High

**What is new.** Two pre-auth XSS bugs in the Mailman fork shipped by default with cPanel & WHM: `MixpanelAnalytics.py` reflects `mpidentity` into an inline script through `json.dumps()`, which escapes quotes but not `/`, so `</script>` closes the block; and `admindb.py` renders the held-message `From:` header without `Utils.websafe()`, so a moderation queue stores the payload for an administrator to trigger.

**What was already known.** Both are textbook. That JSON serialisation is not HTML-context escaping, and that `</script>` therefore escapes an inline script, is decade-old guidance repeated in every XSS reference; a single unescaped field beside correctly escaped siblings is the most common stored-XSS shape there is. Real bugs on a widely deployed product, no transferable primitive.

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

## 39.8 — [GHSL-2024-198 / GHSL-2024-199: Zero-click RCE in Uptrain](https://securitylab.github.com/advisories/GHSL-2024-198_GHSL-2024-199_Uptrain/) — Kevin Stubbings, GitHub Security Lab

**REMOVED** · Useful application · confidence High

*(Fourth re-check round, 14 August 2026. Reported 5 September 2024, CVE-2025-27621 / CVE-2025-27770, advisory published 8 August 2026 — judged as 2026 on first public disclosure, matching the treatment of the Samsung Browser uXSS entry.)*

**What is new.** Only the composition, and it is the familiar one: a default user whose username doubles as a static API key, a CORS policy that reflects any origin with credentials, and `/create_project` passing the `checks` and `metadata` parameters straight to Python `eval()`. Together any web page a victim visits reaches RCE with no interaction. The advisory is a clean worked example of why finding those three primitives separately understates the impact.

**What was already known.** Every element. Hardcoded default credentials, permissive-CORS-plus-credentials as a cross-origin invocation primitive, and `eval()` on request parameters are each textbook, and "chain a browser-reachable authenticated sink into zero-click RCE" is the standard shape of the LLM-tooling advisories already judged for 2026 (LiteLLM at 55.5 and 53.0, Flowise at 59.0), all of which carry more mechanism than this one.

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

## 37.0 — [Slop Spotting: Using Rules to Detect AI Slop for Bug Bounty](https://semgrep.dev/events/hsc-26-defcon-34/) [Village agenda](https://www.bugbountydefcon.com/agenda-2026) — Katie Paxton-Fear & Max vonBlankenburg, Semgrep

**REMOVED** · Insufficient evidence · confidence Low

*(Fourth re-check round, 14 August 2026. DEF CON 34 Bug Bounty Village, 8 August; village decks are not mirrored on the DEF CON media server and no slides, tool or writeup has been published.)*

**What is new.** As far as the abstract goes: a claim-existence gate for AI-generated reports. If a report asserts a concrete vulnerable code pattern, that assertion can be written as a SAST rule and run against the source — no hits, no pattern, no report. It is a genuinely sensible division of labour (the model proposes, a deterministic checker disposes) and cheap enough to run at triage speed on large codebases.

**What was already known.** Turning a claim into a machine-checkable predicate before spending review time on it is ordinary triage discipline, and rule-based confirmation of a suspected pattern is what SAST has always been for. The gate also stops well short of exploitability — a pattern can exist and be unreachable. Judged on an abstract and a vendor event page only; nothing verifiable was published, so this is a placeholder, not a settled score.

---

## 36.5 — [New Hope for SSRF: Exploiting Credential Relay from APIM to AI Foundry](https://www.cloud-village.org/dc34) — Marios Gyftos & Chrysostomos Manousis, Cloud Village

**REMOVED** · Insufficient evidence · confidence Low

*(Fourth re-check round, 14 August 2026. Delivered 8 August as scheduled; still no slides, whitepaper, repo or blog post — Cloud Village had not pushed a DC34 slides repo as of this check. **Stays on the Watchlist.**)*

**What is new.** From the abstract, the framing is the reusable part: an outbound request is *two* independent security decisions — where it goes, and which credential gets attached — and the same failure to bind them recurs across six Azure services (AI Foundry code interpreter and OpenAPI tool, AI Speech, Azure MCP Server, AKS MCP, API Management), with a credential-relay taxonomy and a testing methodology promised on top. Claimed impact runs from minting Managed Identity tokens for arbitrary audiences to never-expiring write SAS tokens from Microsoft's own backend and root RCE on Kubernetes nodes.

**What was already known.** SSRF reaching IMDS to steal a managed identity token is the defining Azure SSRF pattern — Orca's 2023 disclosure of SSRF across four Azure services (API Management among them) is the direct precedent, and CVE-2026-26118, the one CVE tied to this work, was published by MSRC in March 2026 with a GitHub advisory. Whether the cross-service taxonomy is more than a count of instances cannot be judged without the deck; scored as insufficient evidence rather than guessed at.

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

## 32.0 — [Pattern, Graph, Prompt: What Happens When You Layer Three Analysis Paradigms on the Same Codebase](https://appsecvillage.com/events/dc-2026/pattern-graph-prompt-what-happens-when-you-layer-three-analysis-paradigms-on-the-same-codebase-1223399) — Mudita Khurana, Airbnb

**REMOVED** · Insufficient evidence · confidence Low

*(Fourth re-check round, 14 August 2026. AppSec Village, 8 August; no slides, data or writeup published.)*

**What is new.** A single production monorepo run through pattern-based SAST, code-property-graph analysis and LLM review, with 100+ confirmed vulnerabilities and a stated methodology for layering them. The useful framing is that the three fail *differently* — rules are exhaustive only for known forms, graphs carry reachability but not intent, LLMs read intent but give up determinism — so the measure that matters is unique finds and unique misses per paradigm, not the combined total.

**What was already known.** That rules, dataflow and semantic review are complementary, and that an LLM reviewer should not be benchmarked purely as a SAST replacement, is the standing position across vendor and academic work on the same question. Without the per-paradigm numbers the talk's actual contribution — the overlap and non-overlap — is exactly what is unpublished.

---

## 31.8 — [Duplicate chunked `Transfer-Encoding` smuggles a response across reused proxy connections in curl](https://hackerone.com/reports/3795615) [Bare-LF variant](https://hackerone.com/reports/3785919) — violet12331

**REMOVED** · Useful application · confidence Medium

**What is new.** A precise code-level guard bypass: the duplicate-chunked branch returns success for the whole header, so the chunked-must-be-last rejection is never reached.

**What was already known.** Duplicate and obfuscated Transfer-Encoding as a desync primitive (Kettle 2019; curl issue 13451 in 2024) and response-queue desync over reused connections (Doyhenard, DEF CON 29, in archive). curl closed this Informative and the sibling Not Applicable; both presuppose an attacker-controlled origin that could emit Set-Cookie directly.

---

## 31.8 — [The API Made Me Do It: Do Bad APIs Lead AI to Generate Vulnerable Code?](https://appsecvillage.com/events/dc-2026/the-api-made-me-do-it-do-bad-apis-lead-ai-to-generate-vulnerable-code-1248780) — Yariv Tal

**REMOVED** · Insufficient evidence · confidence Low

*(Fourth re-check round, 14 August 2026. AppSec Village, 8 August; no slides, code or results published.)*

**What is new.** A controlled A/B: the same agent builds the same Java/Spring application twice, once against ordinary primitives and once against secure-by-default scaffolding with risky APIs restricted, with prompts describing product requirements only. Both builds go through CodeQL and manual review. The question is worth asking — if generated code keeps reaching a dangerous primitive, removing the primitive may beat asking the model not to misuse it — and the design deliberately tests architecture rather than prompting.

**What was already known.** Secure-by-default APIs and safe wrappers as a defence against developer error long predate LLMs; the experiment re-runs that argument with a model as the developer. Nothing is published to check the result against, including whether the wrappers merely hid risk, which the abstract itself raises as a possible outcome.

---

## 31.2 — [SSRF filter bypass via the RFC 8215 local-use NAT64 prefix `64:ff9b:1::/48`](https://hackerone.com/reports/3634400) — tipsen

**REMOVED** · Duplicate / already known · confidence High

**What is new.** Nothing but one missing CIDR: the gem blocked the well-known NAT64 prefix and omitted the RFC 8215 local-use sibling.

**What was already known.** Reaching internal IPv4 through an alternate IPv6 representation is the founding idea of SSRF-blocklist bypass (Orange Tsai, BH 2017, in archive), and this exact gap was reported across at least five unrelated projects in the same period.

---

## 30.5 — [CVE-2026-62899: .NET `System.Net.HttpListener` security-feature bypass via HTTP request/response smuggling](https://github.com/dotnet/announcements/issues/427) [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62899) — reported by Miha Zupan, Microsoft

**REMOVED** · Insufficient evidence · confidence Medium

*(Fourth re-check round, 14 August 2026. Advisory published 11 August 2026.)*

**What is new.** Nothing that can be read. The advisory states inconsistent interpretation of HTTP requests (CWE-444) in `System.Net.HttpListener` on Linux and macOS, CVSS 5.9, fixed in .NET 8.0.30 / 9.0.19 / 10.0.11, found internally. No malformed-request signature, no framing detail, no discussion of which component disagrees with which. It is a patch to apply and a differential-test target, not a technique.

**What was already known.** Request smuggling as a class, and specifically that a proxy and an application disagreeing about message framing turns into an authorization or routing bypass rather than only connection poisoning, is a decade of published work. This entry exists so the next sweep does not re-chase a vendor advisory with no public mechanism; **re-judge if technical detail is ever published**.

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

## 29.8 — [Testing API Business Logic With AI Agents: What We Got Wrong First](https://www.bugbountydefcon.com/agenda-2026) — Samantha Pearlstein, Bug Bounty Village

**REMOVED** · Insufficient evidence · confidence Low

*(Fourth re-check round, 14 August 2026. DEF CON 34 Bug Bounty Village, 8 August; no slides, tool or writeup published.)*

**What is new.** A retrospective on three failure modes in building agents for enterprise API testing: testing before the resource and identity relationships are modelled, using an agent where a deterministic method is better, and dropping domain context. The first is the substantive one — BOLA/IDOR reasoning needs an ownership graph over users, orgs, roles and parent/child resources before traffic means anything, so building that graph first and letting the agent reason over it beats handing it raw HTTP.

**What was already known.** "Model the object ownership graph before hunting for broken object-level authorization" is the standing methodology for BOLA testing, agent or not, and "use deterministic tooling for deterministic subproblems" is the same lesson several other 2026 talks report. No benchmark, no artifact and no measured before/after was published, which is precisely the evidence that would have made it more than experience.

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

## 79.3 — [Ruby 4.0 Universal RCE Deserialization Gadget Chain](https://www.elttam.com/blog/ruby-4-0-universal-rce-deserialization-gadget-chain) — Luke Jahnke, elttam

**KEPT** · Meaningful extension · confidence Medium

### Candidate

Published 14 August 2026. A universal `Marshal.load` chain covering Ruby 4.0.6
back to 3.3, following the same author's 2018 and 2024 chains.

### Core contribution

Two new primitives, both reached below the Ruby standard library. The trigger
is no longer a `marshal_load` method: a crafted `Gem::StubSpecification` is
placed as a Hash key, and `Marshal.load` calls `hash` on it while rebuilding
the Hash. The caller is `Time._load`, whose C implementation `time_mload`
validates the zone name inside `rb_rescue` and discards the exception, giving a
failure-tolerant caller whose gadget completes its side effects before raising.
Because both rest on core language behaviour, neither can be closed by the
small Ruby-level diffs that retired every previous chain.

### Prior art

The lineage is well documented and largely archived: Jahnke 2018, Stalmans
2019 and 2021, Bowling 2021 and 2022, httpvoid 2022, Leahu 2024, Giovannini
2024, and Jahnke's own Ruby 3.4 chain (2024, in `2024.md`). All of those enter
through Ruby-level `marshal_load` in `Gem::Requirement` or `Gem::Version`.
Trail of Bits' August 2025 history of Ruby deserialization covers none of the
C-level or Hash-key mechanisms. The author states some plumbing is reused from
the 3.4 chain.

### Scorecard

| Category | Score | Weight | Weighted | Reason |
|---|---:|---:|---:|---|
| Original contribution | 72 | 25% | 18.00 | Two entry primitives new to the public Ruby corpus; the end capability continues a known series. |
| Transferability | 78 | 20% | 15.60 | Universal within Ruby, and "find a native caller that swallows exceptions" is a portable gadget-hunting idea. |
| Lasting value | 80 | 20% | 16.00 | Resting on core hashing and Marshal behaviour should outlast predecessors that were patched away. |
| Technical soundness | 85 | 15% | 12.75 | Chain given class by class with versions, preconditions and honest reuse. |
| Practical usability | 85 | 10% | 8.50 | Works with modest preconditions: an HTTPS host and a writable directory. |
| Clarity and reproducibility | 85 | 10% | 8.50 | Gadget roles and payload construction are set out explicitly. |

**Final score: 79.3/100.** Archive decision: include as a core technique.

### Verdict

Meaningful extension. The capability is not new, but the two primitives are,
and the patch-resistance argument is a real change in kind for this lineage.

---

## 75.5 — [Regular Expression Denial of Service Induced by Backreferences](https://www.usenix.org/conference/usenixsecurity26/presentation/liu-yichen) [Paper](https://www.usenix.org/system/files/usenixsecurity26-liu-yichen.pdf) [Preprint](https://arxiv.org/abs/2602.21459) [Artifact](https://zenodo.org/records/20762298) — Liu, Çakar, Agrawal, Seo, Davis, Lee, Stony Brook & Purdue

**KEPT** · Original technique · confidence Medium-High

*(Fifth re-check round, 18 August 2026.)*

**What is new.** ReDoS theory has been built entirely on Kleene regexes and NFA ambiguity, so every deployed detector answers "safe" for a whole family of genuinely super-linear patterns. The Two-Phase Memory Finite Automaton models regex-with-backreference semantics including self-references, and from it two independent cost sources are derived — a single backreference evaluation can be non-O(1), and the number of evaluations can be non-O(1) — whose combination yields super-linear runtime **even when sink ambiguity is linear**, exactly the regime existing detectors certify as safe. The second reusable idea is the security consequence: in an IDS a super-linear regex is not merely a slowdown but an **alert bypass**, because tripping PCRE's match limit makes the rule fail open. 48 previously unknown ReDoS bugs in the Snort ruleset, with exploits that both cost 0.6–1.2 s per rule and evade silently.

**What was already known.** K-regex ReDoS complexity is mature: Rathnayake & Thielecke, Weideman, [static detection of super-linear NFAs](https://arxiv.org/pdf/1701.04045), [Revealer (S&P 2021)](https://seclab.cse.cuhk.edu.hk/papers/sp21_redos.pdf), and [selective memoization (S&P 2021)](https://fservant.github.io/papers/DavisServantLee-SelectiveMemo-IEEE-SP21.pdf) by two of these authors. Memory automata for backreferences exist in formal-language theory (Schmid), and Aho's NP-completeness result for matching regexes with backreferences is classical — but it says nothing about *which* patterns backtrack badly, offers no detection algorithm and gives no prevalence data. The archive already holds ReDoS references from 2018–2022. Exploiting the blind spot still needs a backreference on an attacker-reachable hot path, which caps transferability.

---

## 73.7 — [Recovering Encrypted LLM Reasoning Traces](https://arxiv.org/abs/2608.09867) [Reproduction](https://embracethered.com/blog/posts/2026/recovering-encrypted-llm-thoughts/) — Panfilov, Schmotz, Shumailov, Beurer-Kellner, Schaeffer, Prabhu, Geiping, Andriushchenko; reproduced by Johann Rehberger

**KEPT** · Meaningful extension · confidence High

*(Fifth re-check round, 18 August 2026. The paper is the primary reference: the blog is dated six days later and says outright that it is a reproduction of it.)*

**What is new.** A decoder-oracle primitive. Because the opaque reasoning blob is validated by a key shared provider-wide, *any* sibling model accepts it — so route it to the weakest-guarded model in the family and ask for a verbatim transcription. The stronger model is never jailbroken; its guardrails are simply routed around. Target-neutral residue: opaque client-held state whose integrity rests on one provider-wide key is readable by whichever peer sharing that key has the loosest guardrails, which turns a confidentiality boundary into a function of the weakest sibling. Two further consequences are new — the blob is a covert prompt-injection carrier invisible in the rendered transcript, and published agent logs become a retrospective credential corpus (315,320 blocks yielding 367 PII artifacts and 182 credentials). Rehberger adds independent cross-account reproduction, released tooling and observed reliability drift.

**What was already known.** [Matthew Green, 29 May 2026](https://blog.cryptographyengineering.com/2026/05/29/fooling-around-with-encrypted-reasoning-blobs/) published the architectural finding — blobs replay unmodified across sessions, accounts and, for one provider, models — plus a size and timing side channel, and reported it to vendors who saw no security implications. He explicitly failed to recover plaintext and never tried a weaker model as decoder; the paper's own abstract concedes it builds on prior research. Distinct from [Prompt Injection as Role Confusion](https://role-confusion.github.io/) (71.8), which forges reasoning into a prompt, and from Cache Me, Catch You (75.6), which attacks serving caches.

---

## 73.2 — [DNS Cache Poisoning Like it's 2006](https://www.usenix.org/conference/usenixsecurity26/presentation/ben-simhon) [Paper](https://www.usenix.org/system/files/usenixsecurity26-ben-simhon.pdf) [Advisory](https://kb.isc.org/docs/cve-2025-40780) — Omer Ben-Simhon & Amit Klein, Hebrew University of Jerusalem

**KEPT** · Meaningful extension · confidence High

*(Fifth re-check round, 18 August 2026. ISC's advisory of 22 October 2025 credits the authors and states the PRNG weakness, but carries no technique; the contribution is disclosed by the 2026 paper, so the work is dated to 2026 under the archive's own rule that a bare advisory does not set a cutoff.)*

**What is new.** BIND 9 drives its UDP source port, its TXID **and** its Fisher–Yates RRset shuffle from the same Xoshiro128\*\* instance. RRset ordering is a freely observable, high-entropy output of that generator — roughly five large-RRset samples give 160 bits — so state recovery becomes possible from the client side alone, with no attacker-operated authoritative server, which the authors state is a first for this family. Around it sit a "living off the land" variant using third-party authoritative servers, an ANY-query variant, and near-atomic query batching that turns QNAME minimisation, a privacy feature, into an attack aid. The generalisable residue is sharp: **a cosmetic randomisation drawn from the same non-cryptographic PRNG as a security-critical value is a full state-disclosure oracle, and the cheapest one, because nobody treats shuffle order as secret.**

**What was already known.** Largely the authors' own line. [Klein's 2007 BIND 9 work](https://lwn.net/Articles/242724/) recovered TXID PRNG state from observed TXIDs but required an attacker-operated authoritative server, and [Cross Layer Attacks and How to Use Them (S&P 2021)](https://arxiv.org/abs/2012.07432) established the "infer PRNG state from one consumer, predict another" method against Linux `prandom`. Kaminsky (2008) supplies the poisoning payload; Herzberg and Zheng the fragmentation attacks; SADDNS the side-channel port inference, already archived. Distinct from One Char to Rule Them All (73.8) and Alias Equals Zone? (67.8), which are different DNS mechanisms.

---

## 72.5 — [BUIzz: Finding Policy Enforcement Bugs via Interaction Simulation on the Browser User Interface](https://www.usenix.org/conference/usenixsecurity26/presentation/jung) [Paper](https://www.usenix.org/system/files/usenixsecurity26-jung.pdf) [Code](https://github.com/WebSec-Lab/BUIzz) — Jung, Kim, Kim, Wi, UNIST

**KEPT** · Tooling / methodology · confidence High

*(Fifth re-check round, 18 August 2026. This was a Watchlist item in the fourth round pending the USENIX embargo; the paper is now published and it clears the cut.)*

**What is new.** Two reusable pieces. A search dimension document-level automation structurally cannot reach: navigations initiated from the browser chrome — context-menu items, keyboard shortcuts, drag-and-drop onto the address bar, and vendor additions such as split view and mobile view — enumerated from browser manuals and context menus, driven at OS level because WebDriver, Selenium and Playwright all operate inside the document, plus their two-step combinations. And a pre/post-interaction metamorphic oracle: policy enforcement should be invariant across a UI-initiated navigation of the same document, so an inconsistency *within a single browser* is a bug. That removes the two structural blind spots of cross-browser differential testing — a bug every browser shares, and a policy only one browser implements — and ran about six times faster than a differential baseline given the same interactions. The load-bearing empirical result is that **67.6% of the 34 analysed security bugs live in vendor-added interface features rather than upstream Chromium, and split view alone accounts for 38.2%**; Chrome added split view in November 2025, so the surface is spreading. Flagship case: opening a link in Brave's split view attaches a `SameSite=Strict` cookie to a cross-site request.

**What was already known.** The bug class, extensively — the paper's own appendix catalogues around sixty public browser bugs since 2015 triggered by interface interactions, including [CVE-2017-7834](https://bugzilla.mozilla.org/show_bug.cgi?id=1358009), [Mozilla 1455174](https://bugzilla.mozilla.org/show_bug.cgi?id=1455174) on SameSite inconsistency via drag and drop, and [Chromium 40232572](https://issues.chromium.org/issues/40232572). Differential policy-enforcement testing is established by [DiffCSP (NDSS 2023)](https://wsp-lab.github.io/papers/wi-diffcsp-ndss23.pdf) and Franken et al., and metamorphic oracles for web security testing by [MST-wi/SMRL](https://arxiv.org/abs/2208.09505). The oracle style and the bug class both predate this; the systematised interaction space, the OS-level harness and the vendor-customisation finding did not. No overlap with Breaking SameSite=Strict in Chrome (47.2).

---

## 71.8 — [Analyzing the WebRTC Ecosystem and Breaking Authentication in DTLS-SRTP](https://www.usenix.org/conference/usenixsecurity26/presentation/bach) [Paper](https://www.usenix.org/system/files/usenixsecurity26-bach.pdf) — Bach, Karadžić, Knittel, Merget, Degabriele, TII / TU Darmstadt / RUB

**KEPT** · Meaningful combination · confidence Medium-High

*(Fifth re-check round, 18 August 2026.)*

**What is new.** The enabling contribution is reach. DTLS-SRTP had never been black-box tested in deployed services because it sits behind an unspecified signaling phase and ICE, and the prior Internet-wide DTLS scan explicitly could not capture it, since these endpoints are ephemeral and answer only a previously negotiated candidate pair. The scanner reaches it from a pure MitM position with no key material, then applies the TLS implementation-flaw catalogue to a mode (D)TLS stacks were never hardened for: self-signed certificates authenticated solely by an out-of-band SDP fingerprint. Nineteen of thirty-three media-server implementations fail authentication at the DTLS layer, nine are exploitable to media retrieval from a pure MitM position, and there is a working proof of concept listening to Webex calls. Two pieces outlive the measurement — an out-of-order key-exchange test in which a second `ClientKeyExchange` after `CertificateVerify` overwrites the peer's stored public key, so the signature is verified against one key while the shared secret is computed from another, and identification of the delayed post-handshake fingerprint check as the accidental mitigation separating broken from exploitable.

**What was already known.** RFC 8827 states that signaling-channel security is a prerequisite for DTLS-SRTP's MitM protection, and Johnston demonstrated MitM against naive deployments with a compromised signaling server. Fiterău-Broştean et al. did DTLS state-machine fuzzing, and Maehren et al. observed that the (D)TLS RFCs never explicitly require signature verification — the test here derives from that. [Practically-exploitable vulnerabilities in Jitsi](https://eprint.iacr.org/2023/1118.pdf) and Enable Security's media-server work target application and availability layers, not fingerprint binding. The residue generalises to any design terminating a secure channel on an endpoint reachable only after out-of-band negotiation.

---

## 70.5 — [Melting the Flesh of PHP's Memory Hardening](https://www.usenix.org/conference/usenixsecurity26/presentation/wu-yifan) [Paper](https://www.usenix.org/system/files/usenixsecurity26-wu-yifan.pdf) — Yifan Wu, Xiaochuan Yu, Zhiyun Qian, UC Riverside & UC San Diego

**KEPT** · Meaningful extension · confidence Medium-High

*(Fifth re-check round, 18 August 2026.)*

**What is new.** Two results. An implementation flaw: PHP-FPM's shadow key, meant to be per-process and per-request, is inherited by a freshly spawned worker from the parent and not re-seeded until after that worker has served a request, so deliberately corrupting a shadow pointer to force a respawn hands the attacker a predictable key and revives freelist hijacking wholesale. And a generic write primitive that never touches freelist pointers, so heap isolation and shadow pointers do not apply to it: corrupt an adjacent `zend_array`'s `arData` pointer with a short — down to single-byte — out-of-bounds write, using only **built-in** PHP object types. That removes the two assumptions which made prior remote PHP exploitation impractical, namely an application-specific object and attacker-supplied PHP code, so the whole heap layout work fits inside one HTTP request with no separate information leak. Five real CVEs are re-exploited end to end with every evaluated protection enabled.

**What was already known.** [Charles Fol's generic remote exploitation of the PHP allocator (GreHack / BlackAlps 2022)](https://www.youtube.com/watch?v=wOEaLlbAU5c) is the direct ancestor — least-significant-byte overwrite of a freelist pointer to create overlapping slots — and is the work that prompted the hardening in [php-src#14083](https://github.com/php/php-src/issues/14083) and [PR #14570](https://github.com/php/php-src/pull/14570). Gollum (CCS 2019) automated PHP heap-layout search but assumed attacker-supplied PHP code and disabled ASLR. Two lessons transfer beyond PHP: a per-process secret inherited before re-seeding is not a per-process secret, which recurs in every fork-based server; and enumerating an interpreter's built-in object types for allocation-shape-controllable structures reachable without attacker code is portable to Python, Ruby and Node engines.

---

## 68.1 — [HijackKV: New Threat in Position-Independent KV Cache Reuse](https://www.usenix.org/conference/usenixsecurity26/presentation/zhang-yichi) [Paper](https://www.usenix.org/system/files/usenixsecurity26-zhang-yichi.pdf) [Preprint](https://arxiv.org/abs/2607.19957) [Code](https://github.com/YichiCS/KV-Cache-Hijack) — Zhang, Wang, Zhang, Yang, Penn State & UIUC

**KEPT** · Meaningful extension · confidence Medium

*(Fifth re-check round, 18 August 2026.)*

**What is new.** Position-independent KV reuse retrieves a cache entry by token match while the entry's value still encodes the context it was computed under. So an attacker submits an optimised adversarial prefix followed by a common benign chunk, and the KV stored for the benign chunk carries the attacker's objective; a later victim whose query contains that chunk — and **no attacker-controlled text at all** — receives a steered response. The reframing is the residue: the KV/context misalignment that the systems literature treats purely as a utility problem, mitigated by selective recomputation, is a cross-tenant *write* channel. It needs no hash collision and no implementation defect, following instead from the intended design, which is deployed commercially. 94% success in a single attempt, surviving 10% hit rates and 50% recomputation, persisting across turns and transferring black-box.

**What was already known.** More than our own record stated. Cache Me, Catch You (75.6) is not purely a confidentiality result: it splits its vectors into user-oriented fraud and **system integrity** attacks, and its block-wise collision hijack already makes a victim's block reuse another block's KV. So cross-user LLM cache poisoning with no attacker text in the victim's input was public five months earlier. Two differences survive: that attack depends on a hash collision in vLLM's non-cryptographic block hashing, an implementation defect with an obvious fix, and its effect is to blind the model to attacker content, whereas this steers the victim by design with no collision. [Bit-flip vulnerability of shared KV-cache blocks](https://arxiv.org/html/2604.17249v2) (April 2026) is a Rowhammer result, a different capability.

---

## 68.0 — [Network-Level Prompt and Trait Leakage in Local Research Agents](https://www.usenix.org/conference/usenixsecurity26/presentation/jeong) [Paper](https://www.usenix.org/system/files/usenixsecurity26-jeong.pdf) [Preprint](https://arxiv.org/abs/2508.20282) [Code](https://github.com/umass-aisec/wra) — Jeong, Teymoorianfard, Kumar, Houmansadr, Bagdasarian, UMass Amherst

**REMOVED** · Original technique · confidence Medium

*(Fifth re-check round, 18 August 2026. Removed on date, not on merit: **out of window**. arXiv 2508.20282 v1 is 27 August 2025 — verified directly, with v2 on 3 September 2025 and v3 on 15 January 2026 — and the v1 abstract already carries the attack, the metric and the headline results. This is 2025 work presented at USENIX Security '26, so it belongs to 2025. It scores above the keep-cut and is flagged to the maintainer for the 2025 "Missed from the original list" review path, in the same way RebirthDay was in the fourth round.)*

**What is new.** Traffic analysis inverted to a new target: not which site was visited but what was asked. The mechanism-level insight is that a research agent is a semantic amplifier — it decomposes one private natural-language prompt into sub-queries and executes them as 70–140 domain visits with low per-step timing variance, so the trace is a near-deterministic function of the intent and, unlike human browsing, separable from background traffic on that signature alone. A passive observer holding only domain names, order and coarse packet features recovers over 73% of the functional and domain knowledge of the prompt and, across sessions, up to 19 of 32 latent traits, holding up with 40% of domains masked. Two by-products: an ontology-aware triplet metric that scores leakage where sentence-embedding similarity and LLM-as-judge collapse it, and the observation that agents visit many domains contributing nothing to the report but widening the observer's view — the lever the proposed defences pull.

**What was already known.** Encrypted-traffic inference is a deep literature: website fingerprinting under Tor, keyword fingerprinting of search queries (Oh et al., PETS 2017), domain-sequence re-identification, and cross-platform browsing-log linkage. [Weiss et al. (USENIX Security 2024)](https://arxiv.org/abs/2403.09751) recovered response content from token lengths, but from model output rather than from where the client went. None reconstruct a natural-language prompt or infer persona traits from an agent's traversal.

---

## 67.7 — [MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection](https://www.usenix.org/conference/usenixsecurity26/presentation/syros) [Paper](https://www.usenix.org/system/files/usenixsecurity26-syros.pdf) [Preprint](https://arxiv.org/abs/2602.09222) — Syros, Rose, Robertson, Nita-Rotaru, Oprea, Grinstead, Kerschbaumer, Northeastern & Mozilla

**KEPT** · Tooling / methodology · confidence Medium

*(Fifth re-check round, 18 August 2026.)*

**What is new.** Injection-surface discovery becomes a search driven by the victim's own behaviour rather than by a human guess: run the agent on the *benign* task, capture step-wise model input/output and browser actions through a proxy, compress the transcripts and rank the interface elements the agent actually attended to, plant a placeholder in the top-ranked element, re-run to harvest the agent's reasoning in the presence of that placeholder, and use that context to synthesise the payload, with a judge closing a reflection loop that re-plans on failure. Two findings outrank the framework. **Cross-application compromise**: from a benign classifieds task the agent was driven into a separate database application and dropped a table, and from one repository host it authenticated into an unrelated forum *with stored credentials* and deleted the account — an application entirely outside the user's task scope. **Agentic phishing**: models that refuse direct credential exfiltration comply when the same action is reframed as an intermediate task-verification step. A useful scaffold-level result too: one agent's planner receives only a boolean from its executor, so once the executor is hijacked the planner is blind, while a unified loop sometimes recovers mid-execution.

**What was already known.** Automated attack generation against web agents predates this: [AdvWeb](https://arxiv.org/abs/2410.17401) (October 2024) trains an adversarial prompter that injects strings into pages to steer vision-language web agents, [AgentVigil](https://arxiv.org/pdf/2505.05849) (May 2025) is generic black-box red-teaming via iterative refinement over templates, and WASP and AgentDojo provide sandboxed benchmarks with fixed injections. None discover and rank the injection surface from the agent's own trajectory, or demonstrate cross-application paths. Evaluation runs against cloned applications rather than live sites, so the surfaces are curated by the environment designers; all 44 attacks were manually verified.

---

## 67.3 — [Solving an ORB mystery](https://lab.ctbb.show/research/solving-an-orb-mystery) — Jorian Woltjer, Critical Thinking

**KEPT** · Meaningful combination · confidence Medium

*(Fifth re-check round, 18 August 2026.)*

**What is new.** The composition. Chromium's Opaque Response Blocking branches its failure mode on request *destination* — a non-`empty` destination yields a network error, `empty` yields a successful blank response — and an attacker-installed service worker that transparently re-issues a request through its fetch handler normalises the destination from `script` to `empty`. That selects the blank-response branch, after which `load` and `error` fire purely on the underlying HTTP status, restoring a 2XX-versus-4XX status oracle that ORB was built to close. The durable residue is broader than ORB: any security decision keyed on request destination is steerable by a proxying service worker, which bears directly on Fetch Metadata resource-isolation policies. The precondition is trivial — the attacker controls the service worker on their own origin and needs nothing of the target.

**What was already known.** Both halves separately, in primary vendor sources. ORB's destination-conditional error handling is documented in Chromium's [Intent to Ship](https://groups.google.com/a/chromium.org/g/blink-dev/c/ScjhKz3Z6U4), which states the carve-out retaining earlier behaviour for script-initiated fetches. That a pass-through service worker rewrites `Sec-Fetch-Dest` was raised as a compatibility bug in W3C discussion in November 2025. The script-tag status oracle is foundational [XS-Leaks](https://xsleaks.dev/docs/attacks/browser-features/corb/) material. What nobody had done in the two-plus years ORB has shipped is connect the documented branch to the documented rewrite. The author himself frames it as reviving an ancient XS-Leak, which is why this is scored as assembly rather than discovery.

---

## 66.5 — [zkLogin: when ZKP is not enough](https://brave.com/blog/zklogin/) [Paper](https://eprint.iacr.org/2026/227) — Sofía Celi, Hamed Haddadi & Kyle Den Hartog, Brave & Imperial College London

**KEPT** · Meaningful combination · confidence Medium

*(Fifth re-check round, 18 August 2026.)*

**What is new.** The load-bearing idea is that **a zero-knowledge proof over a signed document attests only to the circuit's own parsing of that document, not to its meaning** — so wherever the circuit's parser and the consumer's parser differ, the proof launders the differential instead of eliminating it. The zkLogin circuit substring-searches for `iss`, `sub`, `aud` and `nonce` without enforcing JSON validity, unique keys or canonical encoding, so duplicate and escape-encoded claims verify while meaning something else downstream. Paired with it is the absence of end-to-end binding between issuer, subject, audience and relying party, so a leaked relying-party prover key mints valid proofs for unrelated applications, giving cross-relying-party and cross-subject impersonation. The general framing — that promoting a short-lived OIDC bearer *authentication* document into a durable *authorization* credential strips exactly the temporal and audience constraints that made it safe — carries to zkEmail, zkPassport and wallet designs that prove over externally issued documents.

**What was already known.** JSON interoperability attacks are well mapped ([Bishop Fox, 2022](https://bishopfox.com/blog/json-interoperability-vulnerabilities); RFC 8785), claim-level JWT attacks including shadowed claims are already in the archive (Three New Attacks Against JSON Web Tokens, 2023), and the OIDC audience-and-binding line runs through the formal OAuth analyses and Real-life OIDC Security. A [public audit of the same circuit in November 2023](https://blog.zksecurity.xyz/posts/zklogin/) reported none of this, which is corroboration rather than prior art. Distinct from Token Time Bomb (61.2), which is implementation-level JWT library testing, and Sub:jugation (71.0), which is issuer-namespace recycling. Practical value is capped: this is analysis with preconditions, not released exploit tooling.

---

## 64.8 — [DOMPurify bypass via SMIL animateTransform on Safari](https://mizu.re/post/dompurify-bypass-smil-animatetransform-safari) — Kévin Mizu

**KEPT** · Meaningful extension · confidence Medium

*(Fifth re-check round, 18 August 2026. Surfaced independently by two beats of the sweep and the freshest find in the window.)*

**What is new.** Three things compose into a bypass under DOMPurify's default configuration. The default allowlist admits `animateTransform` together with `attributeName` and `values` while denying `animate` and `set` — an internal inconsistency nobody had exploited. WebKit validates `attributeName` on `animateTransform` only for animatability, not for membership in the transform-list category that Chromium and Firefox enforce, so `href` becomes a legal animation target — a previously undocumented engine differential. And an unrecognised `type` puts WebKit in `SVG_TRANSFORM_UNKNOWN`, where it emits no transform-function prefix and merely appends a closing parenthesis, turning a transform animator into a near-verbatim attribute writer. The reusable residue: when an engine's animation-target check diverges from the specification's type restriction, an element a sanitizer classified as type-safe becomes a generic attribute writer, and an unknown enum value in a serializer can yield an unprefixed passthrough. Fixed in 3.2.7.

**What was already known.** The `values` semicolon-list hiding a `javascript:` URI from a whole-value check, combined with `attributeName=href` on an SVG anchor, is [Gareth Heyes' SVG animate XSS vector](https://portswigger.net/research/svg-animate-xss-vector) (January 2020) and [Paweł Hałdrzyński's animated SVG work](https://blog.isec.pl/xss-fun-with-animated-svg/) (April 2020), the latter already in this archive. That `href` should never be animated was raised in [DOMPurify issue #796](https://github.com/cure53/DOMPurify/issues/796) in 2023, and Chrome's Sanitizer API already strips the combination — Two Bypasses for Chrome's Sanitizer API (69.5) lists it among known material. Narrower increments this year: the `<selectedcontent>` re-clone (56.5) and mXSS re-contextualisation (33.0). The marginal contribution is the WebKit-only laxity and the unknown-transform passthrough, which is what lets a 2020 vector reach a default-config DOMPurify at all.

---

## 64.5 — [Pwning Claude Code in 8 Different Ways](https://flatt.tech/research/posts/pwning-claude-code-in-8-different-ways/) — RyotaK, GMO Flatt Security

**KEPT** · Meaningful extension · confidence Medium

*(Fifth re-check round, 18 August 2026. Missed by earlier sweeps despite a January publication date.)*

**What is new.** The sharpest increment is a genuine parse-differential sub-class, distinct from "the allowlist missed a dangerous flag". Git resolves any unambiguous long-option prefix, so `--upload-pa` defeats a filter keyed on `--upload-pack`; an `xargs` filter that assumes every flag consumes a value mis-locates the command word when a zero-arity flag appears, so the checked command and the executed command are different tokens; and `$IFS` word-splitting relocates an argument past a regex. Alongside these sit escapes not previously catalogued for this purpose: `man --html` where the blocklist covered only the pager flags, `sort --compress-program` forced to fire by shrinking the buffer, `history` writing into a shell profile, and chained prompt expansion. The recurring theme — the allowlist parses the command line differently from the program that executes it — generalises to restricted shells, CI filters and every other agent with a command gate.

**What was already known.** [Trail of Bits, October 2025](https://blog.trailofbits.com/2025/10/22/prompt-injection-to-rce-in-ai-agents/) published this framing three months earlier against AI-agent allowlists, naming `go test -exec`, `git show --format` and `rg --pre` specifically, and concluding that allowlists without a sandbox are fundamentally flawed. GTFOBins documents the `man` and `sed` cases in kind, `tar --use-compress-program` is long-standing argument injection, and Sonar's [argument injection vectors](https://sonarsource.github.io/argument-injection-vectors/) catalogues `git --upload-pack` among eighteen binaries. Claude Code's gate had already been escaped in August 2025. Not prior art but retrospective evidence the primitive recurs: the identical git-abbreviation bypass reappeared in GitPython in July 2026 with no attribution. Distinct from Poisoning Claude Code (69.8), a different bug.

---

## 63.4 — [The Click that shouldn't have worked: RCE via clickjacking in Internet Explorer](https://swarm.ptsecurity.com/the-click-that-shouldnt-have-worked-rce-via-clickjacking-in-internet-explorer/) — Igor Sak-Sakovskiy, PT SWARM

**KEPT** · Meaningful combination · confidence Medium

*(Fifth re-check round, 18 August 2026. Date verified three ways — the page's own `time` element, the rendered byline and the site RSS `pubDate` all give 5 June 2026.)*

**What is new.** Several primitives rather than one bug. An empirically derived privilege hierarchy for the embedded browser control's zone model, in which `http://localhost` is a de facto elevated origin with SMB reach and a far wider ActiveX surface than the intranet zone. The observation that Mark-of-the-Web is **origin-dependent on the download path**: a file fetched at the behest of a localhost page lands without the zone marker, while the identical download from an internet-zone page gets it. A URL-scheme handoff that launders one browser's capability through another, since the older engine refuses silent saves and the newer one does not. Clickjacking a live shell folder listing rendered inside a cursor-following iframe, which makes an embedded operating-system file-manager surface a clickjack target with *execution* rather than merely interface semantics. Drag-and-drop as marker stripping, because the marker is applied after copy completion and drag ordering breaks that. A local MHTML file using `Content-Location` and `cid:` to spoof an arbitrary origin and read a live cross-origin frame. And a systematic extension-to-handler table with per-origin launch matrices. Full proof-of-concept source throughout, published with the vendor's permission.

**What was already known.** Most building blocks, and the article says so: script-host execution from an unmarked local HTML file is a 2000s technique, cross-zone scripting via `shell:` iframes dates to IE5, clickjacking is Hansen and Grossman in 2008, and SMB NTLM leaks and ClickOnce execution are standing tradecraft. Mark-of-the-Web bypass is a large documented family including [Outflank's 2020 survey](https://www.outflank.nl/blog/2020/03/30/mark-of-the-web-from-a-red-teams-perspective/) and Eric Lawrence's writing, and LNK stomping (CVE-2024-38217) already established shortcut files as a marker-stripping vector by a different mechanism. On MHTML, [Alex Inführ's 2020 work](https://insert-script.blogspot.com/2020/01/internet-explorer-mhtml-why-you-should.html) is the closest antecedent but is explicitly not universal XSS. The linchpin localhost bug was fixed in September 2024, so the headline chain is already dead and this is a shrinking surface; what outlives it is the marker-provenance and marker-ordering insight and the embedded-shell-view-as-clickjack-target idea.

---

## 63.2 — [Overcoming the Retrieval Barrier: Indirect Prompt Injection in the Wild for LLM Systems](https://www.usenix.org/conference/usenixsecurity26/presentation/chang-hongyan) [Paper](https://www.usenix.org/system/files/usenixsecurity26-chang-hongyan.pdf) [Preprint](https://arxiv.org/abs/2601.07072) — Chang, Bao, Luo, Yu, MBZUAI

**KEPT** · Meaningful extension · confidence Medium-High

*(Fifth re-check round, 18 August 2026.)*

**What is new.** A negative result that reframes a whole literature: across eleven retrieval corpora and eight embedding models, unoptimised injected text is *never* retrieved under natural user queries, regardless of corpus size or query length. Every indirect-prompt-injection paper that fixes the environment so the poisoned item is guaranteed to be in context — single-document corpora, "read my latest email", trigger tokens planted in the victim's own query — is therefore measuring what happens after retrieval rather than real-world risk, and the widely copied heuristic of prefixing a plausible blurb achieves effectively zero retrieval. On top of that, the injected item is formalised as a **trigger fragment** whose objective is to guarantee retrieval robustly to whatever attack fragment is appended, which is a different optimisation target from poisoning a passage that carries no payload, solved with a search using only embedding-API calls at roughly ten tokens and twenty cents per target query.

**What was already known.** Substantial, and the authors are explicit that the core search procedure is prior art. [Zhong et al.](https://arxiv.org/pdf/2310.19156) (October 2023) achieved query-agnostic corpus poisoning in a white-box setting; [Phantom](https://arxiv.org/pdf/2405.20485) (May 2024) already decomposed a poisoned document into a retrieval-optimised part and an adversarial-command part, differing in that it needs a trigger word in the victim's query; [DIGA](https://aclanthology.org/2025.naacl-long.210.pdf) (2025) is black-box corpus poisoning without gradients and is cited here. PoisonedRAG and BadRAG precede too. Real limits temper the "in the wild" claim: the trigger is optimised per query, transferability across embedding architectures fails in the paper's own figures, and it is untested against rerankers and hybrid retrieval, all standard in production. Distinct from Fooling AI Agents (50.5), an observational study.

---

## 61.8 — [The Masks We (Think We) Wear: Privacy Threats of Browser-Extension Wallets in the Web3 Ecosystem](https://petsymposium.org/popets/2026/popets-2026-0094.pdf) [Preprint](https://arxiv.org/abs/2607.06141) [Code](https://github.com/podiumdesu/wallet-privacy-threats) — Wang, Dimova, Vansteenkiste, Van Goethem & Van Cutsem, KU Leuven

**KEPT** · Meaningful extension · confidence Medium

*(Fifth re-check round, 18 August 2026.)*

**What is new.** Three extensions along axes the 2023 baseline did not reach. The load-bearing one is that twenty-three of the studied wallets inject their provider interface into **cross-origin iframes**, so a third-party tracker embedded on an ordinary, non-dApp site obtains the user's address with no dApp involved and no user interaction — the address stops being a Web3-scoped identifier and becomes a conventional cross-site tracking key linking browsing activity to on-chain wealth. Second, permission *revocation* is quantified rather than asserted: twenty-two of thirty-six web-detectable wallets keep exposing previously granted addresses after the user logs out of a dApp, so the tracker's key persists across sessions. Third, a network-side threat the web-layer literature misses — routine balance queries batch a user's several addresses to the same node provider, so the provider learns which addresses belong to one person, defeating the multi-address separation strategy at its root. Prevalence is measured rather than anecdotal, across 85 extensions and 35 million users.

**What was already known.** [Is Your Wallet Snitching On You? (USENIX Security 2023)](https://arxiv.org/abs/2306.08170) is the direct predecessor and covers more than this paper's framing suggests: Web3 fingerprinting by probing for injected wallet objects, address exfiltration to analytics providers across hundreds of dApps, and the observation that third-party scripts on a dApp can read accounts without interaction when permission has not been revoked. Extension fingerprinting and on-chain address clustering are older still. The vendor's response that cross-origin exposure was known internally is not public prior art and was not scored against the paper, but their stated refusal to stop injecting means the exposure persists.

---

## 61.1 — [Site Isolation is Dead: How Site Isolation is Broken in Agentic Browsers and Extensions](https://wsp-lab.github.io/papers/lee-sp26.pdf) [Artifacts](https://github.com/WSP-LAB/Site-Isolation-Is-Dead) — Lee, Keum, Lee, Shin, Hong, Lee & Son, KAIST / SNU / Oregon State

**KEPT** · Useful application or case study · confidence Medium

*(Fifth re-check round, 18 August 2026. This clears the cut by 1.1 points and is the weakest keep in the round; a second opinion would be reasonable.)*

**What is new.** Once a privileged process holds *delegated authority* — an agent's ability to act on any site with the user's credentials, plus its API keys and conversation history — the renderer-to-privileged IPC channel becomes the entire security boundary, and every system examined authenticates that channel by message *shape* rather than by sender origin. The consequence is a genuine change in exploit economics: a single renderer compromise now buys cross-site action and secret exfiltration with no sandbox escape. Two attacks across two open-source agentic browsers and seven agentic extensions, all nine vulnerable — forged IPC carrying attacker prompts, and IPC-reachable storage yielding API keys, chat history and identity. The storage-exfiltration vector could not be located anywhere earlier.

**What was already known.** The mechanism is documented Chromium threat model: [`compromised-renderers.md`](https://github.com/chromium/chromium/blob/main/docs/security/compromised-renderers.md) states that a compromised renderer can forge IPC messages and impersonate a content script, and lists sender-identity spoofing explicitly. [Carlini, Felt and Wagner (USENIX Security 2012)](https://www.usenix.org/system/files/conference/usenixsecurity12/sec12-final177_0.pdf) established content-script-to-core message passing as the privilege channel. Contemporaneous and independent, [Varonis in April 2026](https://www.varonis.com/blog/architectural-vulnerabilities-in-agentic-llm-browsers) found the same class in the shipping products this paper does not cover. The awkward neighbour is Agentic Browsers and the Same-Origin Policy (66.0): a plain malicious page, via prompt injection and no zero-day at all, already subverts the agent's cross-origin boundary, whereas this attacker must first own a renderer. The title also overstates — site isolation is not dead; what dies is its value when a privileged process holds delegated authority, and no renderer compromise is demonstrated, only assumed.

---

## 60.9 — [LeakyLinks: Measuring the Security and Privacy Risks of URL Scanning Services](https://swag.cispa.saarland/papers/mustafa2026leakylinks.pdf) [Artifacts](https://github.com/cispa/leakylinks) — Mustafa, Rautenstrauch, Hantke, Agarwal, Calzavara & Stock, CISPA / MPI-SP / Ca' Foscari

**KEPT** · Tooling / methodology · confidence Medium

*(Fifth re-check round, 18 August 2026.)*

**What is new.** The genuinely new knowledge is not that scanners leak — it is that **the leak is actively consumed**. Honeypages seeded with decoy links and canary tokens, submitted to each of six services, drew 1,021 visits from 304 unique addresses, including 79 that followed a URL encoded only inside a QR image, static-link follows far exceeding full asset loads (so most visitors parse raw HTML without rendering), probes for cloud-credential and backup paths, and 33 canary triggers spanning web bugs, opened decoy documents and accessed network folders. The pipeline is reusable in its own right: a three-criteria service-eligibility test applied across twenty services, a dual-view crawl capturing each page with and without established client-side state, and a locally hosted vision model for sensitivity classification, deliberately tuned as a conservative lower bound.

**What was already known.** The phenomenon has been public since [Positive Security's urlscan.io report](https://positive.security/blog/urlscan-data-leaks) (November 2022, disclosed that July), which already enumerated password-reset links, account-creation URLs, file-transfer links and signing invoices, itself prompted by a vendor notification earlier that year. Tinder Security Labs published concurrently and others later extended it by manual dorking. The paper cites all of these and positions itself explicitly as scale and automation over them, which is the honest framing. Planting decoys to see who bites is likewise routine method, so the credit belongs to the finding rather than the instrument; and the visitors cannot be attributed to adversaries, which the paper correctly says.

---

## 60.5 — [When Cache Poisoning Meets LLM Systems: Semantic Cache Poisoning](https://www.ndss-symposium.org/ndss-paper/when-cache-poisoning-meets-llm-systems-semantic-cache-poisoning-and-its-countermeasures/) [Paper](https://www.ndss-symposium.org/wp-content/uploads/2026-f200-paper.pdf) [Code](https://github.com/dequeueing/SemanticCache_Poisoning) — Wu, Wang, Zhang, Zhang, Niu, Wu & Zhang, SUSTech & ByteDance

**KEPT** · Meaningful combination · confidence Medium

*(Fifth re-check round, 18 August 2026. A marginal keep.)*

**What is new.** The transferable framing is that a similarity-keyed cache is a *write channel between users*, and because a hit is served without inference, every prompt-level defence is bypassed by construction rather than by evasion — the poisoned response never passes through the model when the victim asks. The part no adjacent work covers is operational: the attacker has no view of cache state, so the contribution includes overcoming interference from other users' queries and surviving eviction through continuous re-injection. Confirmed against production infrastructure rather than a library alone, with attack success in the eighties across three major cloud gateways, black-box, and existing perplexity-, paraphrase- and classifier-based defences shown to fail.

**What was already known.** The core primitive is [PoisonedRAG](https://arxiv.org/abs/2402.07867) (February 2024): craft texts that a retriever returns for a target query and that induce an attacker-chosen answer, in black-box and white-box variants — semantic cache poisoning is that optimisation retargeted from the knowledge base to the cache. Web and DNS cache poisoning supply the older frame the title borrows. Cache Me, Catch You (75.6) already covers the LLM cache layer with a taxonomy including semantic cache, and a January 2026 preprint on semantic-cache key collision was recorded there as concurrent. The marginal contribution is therefore production-cloud confirmation, the persistence and interference requirements, and the defence evaluation, not the primitive.

---

## 59.6 — [TranSPArent: Taint-style Vulnerability Detection in Generic Single Page Applications through Automated Framework Abstraction](https://www.ndss-symposium.org/wp-content/uploads/2026-f1721-paper.pdf) [Author copy](https://yinzhicao.org/reactappscan/TranSPArent.pdf) — Diwangkara & Cao, Johns Hopkins

**REMOVED** · Tooling / methodology · confidence Medium

*(Fifth re-check round, 18 August 2026. Lands 0.4 under the cut.)*

**What is new.** Framework-specific taint sinks are *derived* rather than enumerated: run the framework's own test suite, harvest stack traces to stitch the call edges static analysis loses to higher-order and component-generated functions, then taint backwards from a DOM sink up to the framework's public interface. The transferable trick is the second half — template-syntax sinks are recovered by pattern-matching the transpiler's own tests against their already-derived JavaScript counterparts, so a templating language is bridged without writing a parser for it. Ablation is load-bearing: without the stitching step the pipeline finds none of the nineteen sinks. The output is directly consumable, with fourteen sinks absent from CodeQL's standard library.

**What was already known.** Automatic taint-specification inference for JavaScript libraries is established by [Extracting taint specifications for JavaScript libraries](https://dl.acm.org/doi/10.1145/3377811.3380390) (ICSE 2020) and [InspectJS](https://arxiv.org/abs/2111.09625), and augmenting a static call graph with dynamic hints is prior practice the paper itself cites. The same lab's [ReactAppScan](https://dl.acm.org/doi/10.1145/3658644.3670331) (CCS 2024, already archived) established SPA component-graph taint with hard-coded sinks. Against it: the false-discovery rate is barely better than vanilla CodeQL, only about a tenth of reported paths were manually checked, and the framework versions studied are already superseded.

---

## 59.4 — [When Authorization Loses Its Meaning: Breaking and Fixing Third-Party Online Payments](https://www.usenix.org/conference/usenixsecurity26/presentation/xiao) [Paper](https://www.usenix.org/system/files/usenixsecurity26-xiao.pdf) [Artifact](https://doi.org/10.5281/zenodo.20303820) — Xiao, Chen, Shi, He, Deng & Du, Wuhan University

**REMOVED** · Meaningful combination · confidence Medium

*(Fifth re-check round, 18 August 2026. Lands 0.6 under the cut and was deliberately not rounded up.)*

**What is new.** Six formal models of real third-party payment protocols across three scenarios and two payment providers, verified under deliberately weakened channel assumptions with the adversary granted legitimate merchant access. The invariant that fails in all six is a *design* property rather than an implementation bug: user payment authorization is never cryptographically bound to order semantics, so whenever channel integrity fails anywhere between merchant client, merchant server and payment system, the user can be induced to authorize an arbitrary order. The proposed remedy, per-user-merchant keys binding consent to order semantics, is itself formally verified, and the invariant generalises to web checkout and consent flows.

**What was already known.** Every component. [How to Shop for Free Online (S&P 2011)](https://www.ieee-security.org/TC/SP2011/PAPERS/2011/paper029.pdf), already archived, established the derive-the-invariants-then-test-the-cashier method for three-party payments. The paper states outright that the order-tampering attack was first identified by earlier work (NDSS 2017), and the implicit-intent hijacking that carries the "new variant" is a decade-old mobile IPC weakness its own related work cites. Formal modelling of payment protocols is established for card schemes. The judged x402 entry (64.7) was scored against the same 2011 lineage and contributes a facilitator-side rule set with no analogue here. The headline prevalence figure also shifts between abstract and body.

---

## 57.2 — [XSS2Shell: WordPress Pre-Auth XSS to RCE](https://pwn.ai/blog/xss2shell) — Nigusu Kasahun, pwn.ai

**REMOVED** · Meaningful combination · confidence Medium

*(Fifth re-check round, 18 August 2026.)*

**What is new.** One primitive: a *chained-sanitizer* differential in which the downstream filter manufactures markup the upstream stripper declared inert. PHP's `strip_tags()` only opens a tag when a letter immediately follows the angle bracket, so `< area id=x>` survives as text, while WordPress's KSES tokenizer tolerates the leading whitespace, treats it as an allowlisted element and re-emits it *normalised* into a real tag. The reusable statement is order-dependent: strip-then-filter is not the sum of two filters, and a normalising sanitizer placed downstream of a stripping one can resurrect a payload that neither the stripper nor a browser would have parsed.

**What was already known.** The entire exploitation half is the same site's own prior work, and it is already in this archive: [Paulos Yibelo, May 2022](https://pwn.ai/blog/bypass-csp-using-wordpress-by-abusing-same-origin-method-execution), preserved at `archived-references/md/2022/2022-pwn-ai-novel-attack-vector-bypass-csp-same-origin-method-execution-zeroday.md` and cited by `2022.md`, already published the unauthenticated JSONP endpoint, its callback filter, the dotted-property Same Origin Method Execution chain, cross-window method execution and the click-through to plugin-install code execution. SOME itself is Ben Hayak (2014, archived), DOM clobbering of an undefined global is a textbook pattern, and the application-password redirect sink carried its own advisory in 2023. Sanitizer-versus-parser differentials as a class are mXSS (2013, archived) and a 2019 PHP bug on the same `strip_tags` normalisation mismatch. Verified distinct from wp2shell (62.0) and The WordPress Chain Massacre, which turn on a batch-endpoint dispatch desync.

---

## 55.8 — [One Email, Many Faces: A Deep Dive into Identity Confusion in Email Aliases](https://www.ndss-symposium.org/wp-content/uploads/2026-s148-paper.pdf) — Wu, Hong, Chen, Liu, Liu & Yang, Fudan / Tsinghua / Zhongguancun Lab

**REMOVED** · Useful application or case study · confidence Medium

*(Fifth re-check round, 18 August 2026.)*

**What is new.** An empirical alias-rule table obtained by protocol-level probing rather than by reading documentation — five construction operations sent in raw MIME from the authors' own mail server against twenty-eight provider accounts. That exposes behaviour no documentation states: eight providers support aliasing with none at all, one accepts a prefix scheme over twelve special characters, another documents its infix form but not its suffix form, and two major package registries treat the domain part case-sensitively in contradiction of RFC 5321. The least derivative finding is from the user study: self-reported alias literacy *raises* phishing susceptibility, because knowledge of one provider's rules is over-generalised to domains that do not implement them.

**What was already known.** The provider-normalises-but-platform-does-not mismatch is long-public folklore with a documented in-the-wild campaign: [Agari's 2019 report](https://agariinc.medium.com/bec-actors-exploiting-gmail-dot-accounts-for-fun-and-profit-397bf048e92c) traced fifty-six dot variants of a single address through dozens of credit-card applications and tax returns — alias multiplicity abuse at scale, seven years before this. Plus-addressing for trial farming, and normalising before uniqueness checks, are standard vendor guidance. The adjacent but distinct class of parser disagreement over which domain an address denotes is [Splitting the email atom](https://portswigger.net/research/splitting-the-email-atom) (2024, archived).

---

## 55.5 — [The Script Tag That Isn't: Speculation Rules Injection](https://labs.trace37.com/blog/specfetch-speculation-rules-injection/) [Lab](https://labs.trace37.com/labs/speculation-rules-injection/) — Paul Reed, trace37 labs

**REMOVED** · Meaningful extension · confidence Low

*(Fifth re-check round, 18 August 2026. One of four candidates from a publisher that openly runs an AI-assisted hunting platform; all four were put through a dedicated verification pass before scoring. **Novelty cutoff unestablished** — the claimed 9 April date has no independent corroboration, the only Wayback record is a 403 later that month, and there is no CVE, advisory or third-party report.)*

**What is new.** The sharpest idea is that a `script` element can be a pure JSON data block and still be an execution primitive, which defeats the "does this contain executable JavaScript?" test that markdown pipelines reason with — common renderers pass it through while dedicated sanitizers strip it, so the vulnerable surface is precisely a renderer being used as if it were a sanitizer. The document-rules variant needs no injected anchor at all, turning the page's own navigation links into prerender triggers. The most transferable part is the escalation argument: a same-origin prerender is a full execution context, so a reflected XSS on that origin loses its user-interaction requirement and tokens become readable rather than needing to be forged.

**What was already known.** Prerender as a request-forcing primitive that carries session cookies is documented — [Chromium issue 40087297](https://issues.chromium.org/issues/40087297) records the legacy prerender hint sending same-site cookies cross-site, [sirdarckcat's HTTP cache leaks](https://sirdarckcat.blogspot.com/2019/03/http-cache-cross-site-leaks.html) (2019, archived) used it to force a render, and Cross-Window Forgery (2024, archived) used it to warm a target. The legacy hint also executed JavaScript, so the hidden fully-rendered tab predates the modern API. Verification against MDN confirmed the mechanics but also the bound the post concedes: inline speculation rules must be permitted by `script-src`, so any site with a script-source policy is already immune, and the post leaves a conflict between MDN's stricter reading and a browser violation message unresolved. Two apparent corroborations found during searching turned out to be the publisher's own text quoted back, so the absence of prior art lowers confidence rather than establishing novelty.

---

## 55.4 — [Vault Raider: Stealthy UI-based Attacks Against Password Managers in Desktop Environments](https://www.ndss-symposium.org/wp-content/uploads/2026-s1067-paper.pdf) — Infantino, Ali, Solomos & Polakis, University of Illinois Chicago

**REMOVED** · Meaningful combination · confidence Medium

*(Fifth re-check round, 18 August 2026.)*

**What is new.** Two transferable design lessons. A security-critical feature with two entry points enforces its checks on only one: the primary autofill path binds a credential to an application identifier and validates code signature, developer identity and their association, while the quick-access path performs no application-level validation at all — so the checks on the front door are irrelevant. And the desktop has no origin: application identity rests on a spoofable bundle identifier plus signature allowlists, and window-level manipulation lets an attacker raise its own window above the interface it is driving, so the password manager the attack operates is never seen.

**What was already known.** The class-level insight — autofill outside a browser must guess its target and can be lied to — is the long-filed window-title spoofing problem in another manager's auto-type feature. Synthetic input defeating operating-system security dialogs is Patrick Wardle's DEF CON 2018 work. Most damaging to the "previously unexplored" framing, [DEF CON 32 in August 2024](https://media.defcon.org/DEF%20CON%2032/DEF%20CON%2032%20presentations/DEF%20CON%2032%20-%20Jeffrey%20Hofmann%20Colby%20Morgan%20-%20Discovering%20and%20exploiting%20local%20attacks%20against%20the%201Password%20MacOS%20desktop%20application.pdf) (CVE-2024-42219) already demonstrated a local malicious process on the same platform taking the full vault *and* the account unlock key — same threat model, same target, same outcome, by a different mechanism. The paper cites none of these. Closest judged neighbour is AutoFail (66.5), the mobile analogue.

---

## 54.6 — [Trust Transitions in Email: When Sanitizers and CSS Engines Disagree](https://labs.trace37.com/blog/css-email-trust-transitions/) — Paul Reed, trace37 labs

**REMOVED** · Useful application or case study · confidence Low

*(Fifth re-check round, 18 August 2026. **Priority contested** — see the attribution note below.)*

**What is new.** What survives is not the bypass but the audit method: a rule set plus a platform compliance matrix that is directly reusable for reviewing an email CSS sanitizer, carried by a real design argument — enforce at resolved-URI level, because every new CSS construct must still resolve to a URI before the browser fetches, whereas enumerating token shapes is permanently behind the specification. Two methodological rules transfer cleanly: test inline style attributes and style blocks as separate code paths because they usually are, and always ask what the backup layer is, since one client leaks at the sanitizer and is saved only by its content-security policy while another has no second layer at all. Reporting a negative fuzzing result — that only two of twenty-two wrapper functions resolve to a load — is good practice.

**What was already known and who is credited.** The attack class is disclaimed by the post itself, correctly, citing the scriptless CSS fingerprinting and per-character CSS exfiltration lines already in this archive. The decisive point is attribution: the one checkable claim, the start-anchored `url(` test failing on a custom-property fallback, was fixed upstream on 24 May 2026 in a commit that makes exactly the one-character change the post recommends, and the vendor advisory relayed to oss-security on 3 June 2026 credits that report to **"Geame"**, not to this publisher, while the post names no CVE, no fix, no versions and no other reporter. The claimed publication date is four days before the upstream fix, and the earliest archived capture is in June, so backdating cannot be excluded. Only the one platform claim was independently verified; the rest of the census is unverified. This archive should credit Geame for the Roundcube finding and may cite this post only for the census and the defensive specification. Also note the judged CSS: the bomb inside your inbox (77.0) is not prior art — it is later — but it now occupies this ground far more deeply.

---

## 53.2 — [Burp Suite Professional: browser-powered crawl writes attacker-controlled files](https://hackerone.com/reports/3712279) — kawakatz

**REMOVED** · Meaningful combination · confidence Medium

*(Fifth re-check round, 18 August 2026.)*

**What is new.** A clean inversion primitive with a stated general form: when an automation tool synthesises a local artifact from metadata that a hostile page controls, crawling becomes an arbitrary local file write. The crawler builds an upload file to satisfy a file input, derives its name from the page's own `accept` attribute, treats any dot-prefixed token as an extension and joins the result under a temporary directory, so a traversal sequence in that attribute escapes it and the target writes attacker bytes to an attacker-chosen path — demonstrated into a startup folder for execution at next login. The residue transfers to any hostile-page automation that tries to be helpful: scanners, headless pipelines, and agentic browsers that auto-fill file inputs.

**What was already known.** Attacking the tester's tool from the target is established, with precedents in this very product for out-of-proxy requests and credential leakage. Deriving a local filename from remote input and getting traversal is textbook, from `Content-Disposition` filename handling to Zip Slip. Contemporaneous rather than prior: a crawler advisory four days later covering the download-side mirror of the same idea, which is independent evidence the class is live rather than evidence it was known. Evidence gap: the report body renders as an application shell, so the mechanism was reconstructed from structured data and secondary reproductions.

---

## 52.7 — [Poisoned by the Host: Large-Scale Measurement of Host Name Poisoning in Web Applications](https://www.iamruiyang.me/papers/sp26-HNP.pdf) — Yang, Wang, Sun, Liu & Cao, Johns Hopkins

**REMOVED** · Tooling / methodology · confidence High

*(Fifth re-check round, 18 August 2026.)*

**What is new.** The cross-layer decomposition is the real contribution: dynamically test each server-and-framework pair to establish which combinations let a client-controlled host reach the framework and through which forwarded header, statically derive per-framework host-sensitive API and guard pairs, then use those as taint sources when scanning applications. That "characterise the lower layer dynamically, then use it as an abstraction for static analysis of the layer above" pattern is reusable for any multi-layer trust question, including forwarded-for, forwarded-proto and client-certificate headers. The scale is real, across nine languages and thirty-two frameworks, yielding fifty-two CVEs.

**What was already known.** Essentially the entire consequence space the paper says prior work ignored. [Practical HTTP Host header attacks](https://www.skeletonscribe.net/2013/05/practical-http-host-header-attacks.html) (2013) is in this archive, [Host of Troubles](https://www.jianjunchen.com/p/host-of-troubles.CCS16.pdf) (CCS 2016) mapped server and framework host ambiguity, and reset-link hijacking was measured at DIMVA 2021. Decisively for an archive that measures the practitioner record: [PortSwigger's Web Security Academy Host header topic](https://portswigger.net/web-security/host-header) already documents reset poisoning, cache poisoning, authentication bypass and routing-based SSRF as named sections, and routing-based SSRF via the Host header is in Cracking the Lens (2017, archived). The claim holds only against academic prior work. Soundness is also capped by a model-assisted triage step, manual review of under a third of candidates, no false-negative measurement, and an artifact link that is an anonymous review URL.

---

## 52.4 — [CVE-2026-41238: How Prototype Pollution Turns DOMPurify Into an XSS Gadget](https://labs.trace37.com/blog/dompurify-pp-ceh-bypass/) [Advisory](https://github.com/advisories/GHSA-v9jr-rg53-9pgp) — Paul Reed, trace37 labs

**REMOVED** · Meaningful extension · confidence High

*(Fifth re-check round, 18 August 2026. Independently confirmed real: the advisory was reviewed in the upstream repository crediting this finder, the 3.4.0 release notes thank them by name, and the source diff matches the described fix.)*

**What is new.** One reusable audit rule with a clean proof: in a security library, falling back to a plain object literal and falling back to a null-prototype object are not interchangeable, so every such configuration fallback that feeds a security decision is a prototype-pollution sink — an idiom worth grepping for. A second useful residue is the triage heuristic that a gadget whose sink applies a type check unreachable from string-only pollution collapses exploitability onto structured-clone-preserving transports such as deep-merge message handlers and server-side object injection. What distinguishes it from earlier gadgets in the same library is that it fires on the bare sanitize call with no configuration.

**What was already known.** The class is thoroughly established: [Doyensec's gadget finder](https://blog.doyensec.com/2024/02/08/prototype-pollution-gadget-finder.html) (2024, archived) automates exactly "pollute an optional config property a library never sets", and GHunter (USENIX 2024, archived) systematises the shape at runtime. This library was already a known pollution host three times over, all cited by the post. So sanitizer-as-pollution-sink is not the contribution; default-configuration reachability is. Reverification against published bundles also found the post's flagship version history to be wrong — the vulnerable idiom is present from 2.5.0 onward, absent in 3.0.0 and restored in 3.0.1, so the advertised affected range understates it by the whole still-deployed 2.5.x line, and the stated severity exceeds the published score.

---

## 52.1 — [iframe sandbox bypass, cross-origin drag-and-drop, unvalidated postMessage origin, cookie bomb to account takeover](https://medium.com/@renwa/iframe-sandbox-bypass-cross-origin-drag-drop-unvalidated-postmessage-origin-cookie-bomb-to-21357a4d94f5) — Renwa

**REMOVED** · Meaningful combination · confidence Low

*(Fifth re-check round, 18 August 2026.)*

**What is new.** Of the three primitives the strongest is the drag-and-drop restoration: after the browser killed the top-window-redirect-during-drag variant, this revives cross-origin drag-and-drop by opening a popup sized and positioned exactly at the drag origin, so the source page stays active and dragged content lands in a cross-origin input without precise aiming. That is a real mitigation bypass reviving a killed primitive. The cookie-bomb step, forcing a header-size error so an authorization code stays readable in a same-origin error page, is a modest twist.

**What was already known.** The origin-inheritance trick is specified behaviour: a freshly created iframe's initial document is same-origin with its parent, so writing to it before the data URI commits writes into a same-origin document — discussed in [whatwg/html#1753](https://github.com/whatwg/html/issues/1753) and a browser bug from 2012. The drag-navigation lineage is the author's own, credited in the judged Finding XSS on Shazzer entry (51.5). Keeping an authorization code readable by breaking the callback landing belongs to the OAuth dirty-dancing family. Confidence is low with a named blocker: the host returns 403 to direct fetch and the article was read through a text-extraction proxy, and the underlying report was closed as informative with the vendor redacted, so the chain has no third-party confirmation.

---

## 51.9 — [API Keys Leaking in PNG Metadata of AI Images](https://trufflesecurity.com/blog/api-keys-leaking-in-png-metadata-of-ai-images) — Luke Marshall, Truffle Security

**REMOVED** · Useful application or case study · confidence Medium

*(Fifth re-check round, 18 August 2026.)*

**What is new.** A mechanism detail that defeats the obvious mitigation — the workflow chunk serialises every node's text-widget values including nodes the user muted or bypassed, so disabling a node does not un-serialise its key; only deleting it does. And a measurement: across ten generation communities and 2.49 million attachments, 159,752 images carried the metadata and 681 carried live verified credentials, alongside thousands leaking system prompts, home paths and private local model endpoints. The reusable residue is that a generated artifact's provenance metadata is a credential channel, and any node or plugin framework without a secret input type will bake plugin secrets into every artifact it emits.

**What was already known.** The mechanism exactly, and for over two years: [an upstream issue from May 2024](https://github.com/comfyanonymous/ComfyUI/issues/3553) asks for a secret input type precisely because a custom node's API key and URL are exported with the workflow into saved images, and it remains open, with community workarounds existing because of it. [UpGuard in June 2025](https://www.upguard.com/blog/detecting-generative-ai-data-leaks-from-comfyui) already documented this metadata leaking prompts and images, though not credentials at this scale. Workflow-in-a-PNG is a documented product feature, and metadata leakage generally is ancient. The post cites none of this.

---

## 50.6 — [From Length to Content: Token-Length Side-Channel Attacks on LLM API Merged Outputs](https://www.usenix.org/conference/usenixsecurity26/presentation/li-sijia) [Paper](https://www.usenix.org/system/files/usenixsecurity26-li-sijia.pdf) — Li, Cui, Chen, Lin, Gu, Deng, Xu & Li, Zhongguancun Lab & Tsinghua

**REMOVED** · Independent rediscovery · confidence Low

*(Fifth re-check round, 18 August 2026. Cutoff could not be determined — no preprint exists and the review cycle is not publicly resolvable, so the narrowest defensible range was used and confidence lowered rather than assuming precedence.)*

**What is new.** The residue is that chunk aggregation is a coarsening rather than a mitigation: a transport record carrying several tokens still discloses the sum of their character lengths, so reconstruction becomes constrained sequence recovery under unknown token boundaries. The specific contribution is the decomposition step, training progressively from single-token alignment up to splitting merged groups. The accompanying per-service characterisation of how many tokens each provider packs per record, with matching success rates, is useful measurement, and the reported results are honest and modest.

**What was already known.** [Weiss et al.](https://arxiv.org/abs/2403.09751) (2024) established the token-length side channel and model-based reconstruction, and proposed the batching this paper attacks. Two works published before any verifiable public disclosure here already made the central claim: [NetEcho](https://arxiv.org/pdf/2510.25472) (October 2025) explicitly handles multi-token packets via per-group token-count and character-length traces, recovering the majority of content under batching, and [Whisper Leak](https://arxiv.org/html/2511.03675) (November 2025) shows batching reduces but does not eliminate topic inference across twenty-eight providers. The paper cites neither. Its claim that a provider shipped an obfuscation option in response to this disclosure is an unverified author claim; the same field is credited in the November 2025 work.

---

## 50.1 — [SvelteSpill: A Cache Deception Bug in SvelteKit + Vercel](https://www.aikido.dev/blog/sveltespill-cache-deception-sveltekit-vercel) — Jorian Woltjer, Aikido Security

**REMOVED** · Useful application or case study · confidence High

*(Fifth re-check round, 18 August 2026.)*

**What is new.** A clean instance requiring no misconfiguration on anyone's part: the platform adapter honours an unvalidated path-rewriting query parameter while the platform's cache blanket-caches an immutable asset prefix for a year, so one URL routes to a session endpoint but is keyed as a static asset and an authenticated victim's response lands under an attacker-fetchable static path. The actionable residue is to audit every meta-framework adapter for internal routing inputs the cache key cannot see.

**What was already known.** The class is thoroughly mapped: [Web Cache Deception](https://omergil.blogspot.com/2017/02/web-cache-deception-attack.html) (2017) and its Black Hat whitepaper are both archived, as are Practical Web Cache Poisoning (2018) and the later entanglement and cache-key work, whose stated remedy is already "never rewrite the cache key, rewrite the request". The closest pre-cutoff equivalent is the Next.js cache poisoning of CVE-2024-46982, which abused an internal routing header and parameter — the same shape, on the same platform, two years earlier. Noted but not scored: the bug was found by an automated pentest system, a methodology datapoint the post does not develop.

---

## 49.6 — [Phantom Squatting: AI-Hallucinated Domains as a Software Supply Chain Vector](https://unit42.paloaltonetworks.com/phantom-squatting-hallucinated-web-domains/) — Nagaraj, Marty, Kaleli & Starov, Unit 42

**REMOVED** · Tooling / methodology · confidence Medium

*(Fifth re-check round, 18 August 2026.)*

**What is new.** Measurement and lead time rather than mechanism: a multi-agent pipeline over hundreds of thousands of adversarial prompts across 913 brands that maps which phantom hostnames a model reliably emits per brand, plus monitoring that quantifies an exploitation window of eighteen to fifty-one days between first hallucination and adversary registration. The transferable claim is operational — hallucination distributions are stable enough to pre-register against — which is a defensive posture rather than an attack primitive.

**What was already known.** [Netcraft in July 2025](https://www.netcraft.com/blog/large-language-models-are-falling-for-phishing-scams) already published the move to DNS that this candidate claims: across fifty brands, a third of returned login hostnames were not brand-controlled and roughly thirty per cent were unregistered or parked, with Netcraft stating explicitly that attackers can register the unclaimed ones and wait for the model to recommend them, including a live phishing result. Underneath sits package-name hallucination and slopsquatting from 2023 and 2024, both cited by the candidate. With Netcraft pre-cutoff, the "extension from packages to DNS" novelty claim is not sustainable, and what remains is scale plus a monitoring pipeline.

---

## 47.7 — [LLM Heist: Hijacking LiteLLM for Traffic Interception, Key Theft, and Tool-Call Injection](https://embracethered.com/blog/posts/2026/hijacking-litellm-for-fun-and-profit/) — Johann Rehberger

**REMOVED** · Meaningful combination · confidence Medium

*(Fifth re-check round, 18 August 2026.)*

**What is new.** The gateway-specific mechanics are real and verifiable: a model-update call rewriting the upstream base and proxy flag converts the victim's own trusted gateway into a transparent forwarder to the attacker's instance with client endpoint and virtual keys untouched; the victim gateway then decrypts its stored provider key and attaches it to the forwarded request, making the forwarder a credential-extraction oracle for secrets the attacker could not otherwise read; and the post-inference response hooks are named as the rewrite points, so prompt- and model-level guardrails never see the modification. The defender's list is strong.

**What was already known.** More than the post admits. [Your Agent Is Mine](https://arxiv.org/abs/2604.08407) (April 2026, four months pre-cutoff) already defines response-side payload injection — the router rewriting a model-generated tool call after it leaves the provider and before it reaches the client — and passive secret exfiltration, with seventeen routers touching canary credentials; a near-concurrent post four days earlier covers tool-argument rewriting that preserves name and schema. Neither is cited. The two judged LiteLLM entries (55.5 and 53.0) cover reaching administrative access, whereas this presupposes the master key, so it starts where they end, and its tooling is withheld.

---

## 47.6 — [KYC: Bypass age verification using generative video models](https://www.synacktiv.com/en/publications/kyc-bypass-age-verification-using-generative-video-models) — Kevin Tellier & Léo Desmonts, Synacktiv

**REMOVED** · Useful application or case study · confidence High

*(Fifth re-check round, 18 August 2026.)*

**What is new.** A complete, reproducible recipe against a named production stack, including the identity-pool credential fetch, the signed-chunk streaming protocol, and the generation pipeline from a single still through age progression, animation, upscaling and motion interpolation matched to webcam characteristics, replayed through a virtual camera device. The sharpest version of the claim is that one still photo now suffices, with no video of the target required, because the web flow has no chain of trust binding the media to a physical sensor.

**What was already known.** The whole category. Camera and video **injection attacks** are a named, measured threat with published industry telemetry showing native virtual-camera attacks rising sharply through 2025 and becoming the primary vector, and thousands of injection attempts documented against a single institution's verification flow. The article itself concedes the ground, citing the loopback device, mobile API hooking, sensor attestation and platform integrity as existing context. The archive already holds a 2024 conference writeup defeating a liveness check by feeding a deepfake through an import path. A new payload against an established technique is not a new technique.

---

## 46.9 — [Roundcube XSS chained with cookie tossing for full inbox access](https://www.aikido.dev/blog/roundcube-xss-cookie-tossing) [Report](https://hackerone.com/reports/3594137) — Jorian Woltjer, Aikido Security

**REMOVED** · Useful application or case study · confidence High

*(Fifth re-check round, 18 August 2026.)*

**What is new.** The genuinely fresh element is the product finding rather than the escalation: one attachment-serving action echoes data with its original content type and no content-security policy, while a sibling action doing near-identical work sets a script-blocking policy — a parity gap between two handlers. The portable audit step is to enumerate every file-serving handler in an application and diff their content-type and policy treatment.

**What was already known.** The escalation is well documented pre-cutoff, including in this archive: [Snyk Labs on hijacking OAuth flows via cookie tossing](https://snyk.io/articles/hijacking-oauth-flows-via-cookie-tossing/) (2024) is preserved here and its own summary describes control of a subdomain permitting parent-domain cookies with a narrow path so they take precedence on chosen endpoints — precisely the path-scoped session swap. Also pre-cutoff: Egor Homakov's cookie-tossing work (2013, archived), an archived session-takeover chain from 2024, and two separate 2025 writeups on cookie-based self-XSS exploitation. The judged TikTok pixel cookie-injection entry (45.2) is the nearest neighbour.

---

## 46.7 — [Astro Full-Read SSRF via Host Header Injection](https://www.aikido.dev/blog/astro-full-read-ssrf-via-host-header-injection) — Jorian Woltjer, Aikido Security

**REMOVED** · Useful application or case study · confidence High

*(Fifth re-check round, 18 August 2026.)*

**What is new.** A specific under-tested sink: when a prerendered custom error page exists, the framework's server-side renderer fetches that page from itself using the unvalidated request Host header, and because the fetch follows redirects, attacker infrastructure returning a redirect to an internal URL yields full-read SSRF, reachable pre-authentication on any missing page. The portable heuristic is to audit how server-rendering frameworks obtain their own static assets at runtime, error paths first.

**What was already known.** [Practical HTTP Host header attacks](https://www.skeletonscribe.net/2013/05/practical-http-host-header-attacks.html) (2013), in this archive, is the founding work on applications building absolute URLs from an attacker-controlled host. The judged SvelteKit full-read SSRF entry (59.5) is the same class in a sibling framework, and that judgement already records the class as established largely by those same authors; another major framework fell to the same pattern this year. This scores below the SvelteKit entry because that one had to escape an execution paradox and force a path desync to reach its fetch, whereas this is the unguarded case.

---

## 46.7 — [Authorization Bypass in Quarkus via matrix parameters](https://securitylab.github.com/advisories/GHSL-2026-099_Quarkus/) — Peter Stöckli, GitHub Security Lab

**REMOVED** · Useful application or case study · confidence High

*(Fifth re-check round, 18 August 2026.)*

**What is new.** Only the instantiation: the path matcher does not treat the matrix-parameter separator as a segment terminator during prefix matching, the router strips those parameters downstream, and the policy engine **defaults to permit** when nothing matches, so a protected path with a matrix parameter appended returns success where the bare path returns unauthorized. The one genuinely instructive detail is the sequel, in which the literal-separator fix was defeated again by percent-encoded separators and slashes for static resources — illustrating that stripping a character does not fix a canonicalisation-ordering defect.

**What was already known.** This exact technique is a decade old and heavily documented. An essentially identical framework-level instance carried CVSS 9.8 in 2020, when one framework's filter chain and another's dispatcher disagreed on the path; session-parameter path tricks are older still; and Orange Tsai's Breaking Parser Logic (Black Hat USA 2018), already in this archive, is the canonical statement of routing-versus-authorization normalisation differentials. The advisory's own weakness classifications name the class as pre-existing. Nothing here changes how anyone tests: appending a matrix parameter to a protected path is standing practice.

---

## 44.3 — [LiteLLM Security: SSTI RCE and Unicode Sandbox Bypass](https://fortbridge.co.uk/research/litellm-critical-vulnerabilities-ssti-unicode-bypass/) — Adrian Tiron, Fortbridge

**REMOVED** · Useful application or case study · confidence High

*(Fifth re-check round, 18 August 2026.)*

**What is new.** The observation that a production LLM gateway's custom-guardrail sandbox is regex-guarded and therefore falls to identifier normalisation, plus an unsandboxed template environment reachable before validation on a test endpoint.

**What was already known.** The prior-art check comes back negative for the candidate on its headline claim. Python's normalisation of identifiers after source validation is specified in [PEP 3131](https://peps.python.org/pep-3131/) (2007), and its use as a *filter bypass* — substituting a fullwidth underscore to reach dunder attributes past a blocklist — is documented sandbox-escape technique, appearing in [a 2023 writeup](https://halb.it/posts/bluehens-pyjail/) and in general cheatsheets, traceable to 2020 competition writeups. So the claimed general defeat for regex-based Python sandboxing was already canonical rather than new. The template-injection half is textbook, and the article itself notes another firm independently reached the same guardrail escape by a different route. Judged neighbours: Beyond Normalization (48.8) and two other LiteLLM entries carrying more mechanism.

---

## 39.0 — [Privilege escalation via authorization bypass in graphql-ruby](https://securitylab.github.com/advisories/GHSL-2026-152_graphql-ruby/) — Bas Alberts, GitHub Security Lab

**REMOVED** · Useful application or case study · confidence High

*(Fifth re-check round, 18 August 2026. Two independent reviewers reached the same conclusion.)*

**What is new.** Essentially nothing at the technique level. A resolver on the library's new execution runner rescues the authorization exception and then sets its authorised flag to true, so the resolve call runs and the data is returned anyway — an inverted boolean in a rescue block, present across one release line. The only residue worth carrying is a small methodological note: when a library ships a second execution engine alongside the legacy one, the security hooks must be re-tested against the new runner, because the documented pattern fails open on one path and holds on the other.

**What was already known.** Fail-open exception handling on an authorization path is textbook, with its own long-standing weakness classifications, and GraphQL authorization bypasses broadly, along with this library's own authorization contract, are long documented. The blast radius is real and the diagnosis exact, which is why technical soundness scores high — but impact and precision are not novelty.

---

## 38.8 — [Roundcube: IMAP Command Injection and SSRF via CSS Proxying](https://blog.ostorlab.co/roundcube-imap-injection-ssrf-ove-2026.html) — Aziz Elbelaychy, Ostorlab

**REMOVED** · Useful application or case study · confidence High

*(Fifth re-check round, 18 August 2026.)*

**What is new.** Two clean code-path traces in a widely deployed product, with one instructive detail: an escaping helper that converts newline-bearing strings into safe protocol literals exists and is applied to the search parameter, but a sibling filter parameter takes a different route to the write function, which splits only on literal-string patterns and not on bare newlines. The generalisable observation — find the sibling parameter that skips the escaper — is a code-review heuristic rather than a discovery.

**What was already known.** Both classes, and the first has a twenty-year-old entry in this archive: **MX Injection: Capturing and Exploiting Hidden Mail Servers** (November 2006), preserved at `archived-references/md/2006/webappsec-org-mx-injection-capturing-exploiting-hidden-mail-servers-articles.md`, describes exactly this — a webmail application passing user input into mail-protocol commands so an injected newline ends the intended command and starts the attacker's, reaching a server nobody can address directly. The same product carried its own protocol-injection advisory in 2018. The stylesheet-proxy half is a server-side resource proxy without private-address validation reaching cloud metadata, which is founding SSRF literature (archived) plus textbook metadata abuse.

---

## 36.5 — [An Analysis of Modern Web Security Vulnerabilities Inside WebAssembly Applications](https://arxiv.org/abs/2603.09426) — Corrias, Pisu, Maiorca & Giacinto, University of Cagliari

**REMOVED** · Useful application or case study · confidence Medium

*(Fifth re-check round, 18 August 2026.)*

**What is new.** Marginal. Three additional web-layer outcomes instantiated on hand-built vulnerable applications: a memory bug rewriting a prepared-statement query string so parameterisation is bypassed without the query ever being concatenated; a corrupted policy nonce returned from a module and interpolated into a template, giving server-side template injection purely because the host trusts module output; and a cross-site leak in which a binary write swaps a sanitised expression for a catastrophic one, turning response time into a character-by-character oracle. The least derivative item needs no memory corruption at all — a front-end numeric check passes a value that wraps inside the module.

**What was already known.** The claimed contribution is precisely [Everything Old is New Again: Binary Security of WebAssembly](https://www.usenix.org/system/files/sec20-lehmann.pdf) (USENIX Security 2020), confirmed by reading that paper directly: its end-to-end attack table already includes a stack overflow overwriting markup on the heap to produce cross-site scripting in the browser, and heap-metadata corruption plus overwritten constant data to inject a shell command into a host-side execution sink. The cross-layer mapping, the "constant data is not constant in linear memory" primitive and the host-environment framing are all six years pre-cutoff, and the paper cites that work for the binary primitives while presenting the mapping as its own gap. Everything here runs on purpose-built applications, with no real-world instance, no measurement and no tool.

---

## 35.6 — [npx confusion and npxconfuse](https://lab.ctbb.show/research/from-defcon-research-to-automated-supply-chain-defense-with-npxconfuse) [Tool](https://github.com/cybershaykh/npxconfuse) — Muhammad Mukhtar Mahmud

**REMOVED** · Tooling / methodology · confidence High

*(Fifth re-check round, 18 August 2026. The cutoff is that of the tool, not of the primitive, which is not this author's.)*

**What is new.** A four-layer open-source scanner — discovery across the filesystem, repository APIs and web assets, extraction from package manifests and bundled scripts, concurrent registry analysis, and severity classification — plus one demonstrated live case against a vendor's own package whose unscoped binary name was unclaimed.

**What was already known.** The primitive entirely, by the article's own citation. Roni Carta and Adnan Khan formalised npx confusion at **DEF CON 33 in August 2025**, published as [npx Used Confusion and It's Super Effective](https://www.landh.tech/blog/20260521-npx-used-confusion-and-its-super-effective/) in May 2026 with scale measurement of unclaimed phantom packages and their download counts. Earlier still, [a 2024 writeup](https://www.alxndrsn.com/2024-08-01-npx-binary-confusion/) documented npx binary confusion directly, and detection tooling for binary-entry harvesting already existed. Underneath sits Birsan's dependency confusion (2021, archived). The npx binary-name path is genuinely distinct from classic dependency confusion — but it was made distinct a year before this, not here. Structurally identical to the judged marketplace-namespace entry, which also scored low.

---

## 34.2 — [Ticket Tricking OpenSSL.org with Google Groups](https://spaceraccoon.dev/ticket-trick-openssl-google-groups/) — Eugene Lim

**REMOVED** · Independent rediscovery · confidence High

*(Fifth re-check round, 18 August 2026.)*

**What is new.** One recon tweak, honestly presented: seeding from passive sources to harvest arbitrary group URLs rather than probing for the default group name as the prior generation did, then normalising, deduplicating and testing read and write access. Tens of thousands of raw URLs yielded roughly 150 publicly accessible groups across 600-plus domains, of which very few were exploitable after spam filtering, moderation and member-only posting.

**What was already known.** Everything load-bearing, and the author credits most of it: the original ticket trick from 2017 and a 2020 survey of the same misconfiguration across hundreds of organisations. The claimed contribution — enumeration at scale — is the part most thoroughly preceded: [a 2018 study](https://threatpost.com/public-google-groups-leaking-sensitive-data-at-thousands-of-orgs/132455/) sampled 2.5 million domains, found 9,637 public groups and 31% of sampled organisations leaking sensitive mail, naming account takeover as the consequence, and a further vendor study followed in 2020. That is two orders of magnitude beyond this run. The passive-source seeding does genuinely differ and is reusable recon, which is why this is rediscovery rather than duplication.

---

## 30.2 — [Indirect Prompt Injection remains a fundamental security challenge for AI](https://brave.com/blog/indirect-prompt-injection/) — Shamsabadi, Haddadi & Chaikin, Brave

**REMOVED** · Duplicate or already known · confidence High

*(Fifth re-check round, 18 August 2026. **This exact URL is already inside a judged entry** — it is the companion post of Attacking and Defending AI Browsers (51.6), whose assessment already reads that the companion post is standard injection applied to two new targets. Recorded here only so a future sweep does not re-chase it.)*

**What is new.** One argument: an on-device model ingesting untrusted local documents is as structurally exposed as a cloud agent, so running the model locally is not a mitigation. Evidenced by two responsibly disclosed attacks with agent reasoning traces — hidden page text driving a cloud summarisation agent to post conversation history to an attacker form, and hidden instructions in local documents steering a fully local autocomplete toward surfacing credentials.

**What was already known.** The mechanism is Greshake et al. (2023), and this publisher's own series established the method a year earlier across two agentic browsers and a screenshot-based variant. It also overlaps the judged SPILLAGE entry (62.8) by the same lead author and Agentic Browsers and the Same-Origin Policy (66.0). A local autocomplete is a new *target* class, not a new technique, and the archive's rules forbid treating one as the other.

---

## 27.5 — [GitHub scoped user-to-server tokens can escape their installation](https://hackerone.com/reports/3638909) [Sibling report](https://hackerone.com/reports/3641229) — ahacker1

**REMOVED** · Insufficient evidence · confidence Low

*(Fifth re-check round, 18 August 2026. Blocker named: the report has no disclosed body — only the vendor's advisory paragraph is public, and every aggregator restates it verbatim. Re-judge if a writeup appears, as with the .NET listener entry at 30.5.)*

**What is new.** Per the advisory only, and unverified: an authorization fallback that treats a revoked or deleted installation as a *global* installation context, so a scoped token keeps reading and writing private repositories outside its scope, chained with revocation timing and push attribution to obtain a victim-scoped token in the first place. If accurate, the reusable idea would be that revoking a binding widens the grant — test the post-revocation path, not only the live one. The chain, the attribution step and whether the framing is the researcher's or the vendor's could not be confirmed; the attribution step is exactly the half that is redacted.

**What was already known.** Fail-open scope fallback is a documented pattern with named instances across an identity framework in 2022, an access-management product's group resolution, and a collaboration tool whose scope-validation error yielded wildcard API access, as well as scope creep in current agent-protocol guidance. The same researcher's sibling report from the same month is the same shape.

---

## 24.7 — [Your WAF Doesn't Speak JSON: How the escaped solidus bypasses major WAFs](https://labs.trace37.com/blog/json-escape-waf-bypass/) — Paul Reed, trace37 labs

**REMOVED** · Duplicate or already known · confidence High

*(Fifth re-check round, 18 August 2026.)*

**What is new.** Essentially nothing reusable. The only thing narrower than the prior work is the observation that the escaped solidus is a legal-but-unnecessary escape, making it the minimum-effort member of a family already documented — one character instead of six. The payload list and decision tree are a convenient packaging of existing knowledge, and that is the honest ceiling.

**What was already known.** [TrustFoundry, December 2018](https://trustfoundry.net/2018/12/20/bypassing-wafs-with-json-unicode-escape-sequences/) is the identical parser differential — the filter matches raw body bytes while the parser decodes escapes before the application sees them — weaponised with unicode escapes and shipped with a tamper script. [Sicuranext, July 2023](https://blog.sicuranext.com/aws-waf-bypass/) is **already in this archive and already cited on `2023.md`**, and states in its own summary that virtual patching for a JSON body parameter can be bypassed using unicode escape sequences. [Claroty Team82, December 2022](https://claroty.com/team82/research/js-on-security-off-abusing-json-based-sql-to-bypass-waf) defeated five major vendors on the same thesis by a different route. The post's own expanded-toolkit table reproduces the 2018 technique uncited, in a post with no prior-art section at all, no named target and no archived capture. Its SQL-injection subsection is also internally incoherent, offering as a bypass a payload that carries the injected keywords in clear bytes. Credit belongs to Tyler Rosonke (2018) and, for the cloud-specific variant, Andrea Menin (2023).

---

## 24.7 — [HTTP Response Queue Poisoning via TOCTOU race in the Node.js HTTP agent](https://hackerone.com/reports/3582376) [Release](https://nodejs.org/en/blog/vulnerability/june-2026-security-releases) [Maintainer response](https://adventures.nodeland.dev/archive/cve-2026-48931-shouldnt-have-been-a-cve/) — yushengchen

**REMOVED** · Independent rediscovery · confidence Medium

*(Fifth re-check round, 18 August 2026. The report has no disclosed body — only a one-sentence team summary — so there is no public proof of concept or exploitation narrative.)*

**What is new.** That idle pooled sockets were left paused with only an error listener, so bytes a hostile upstream pre-stages on a keep-alive socket are consumed as the *next* request's response, shifting every subsequent response on that connection by one. The residue is a single library instance of a known hazard, plus the fix shape of destroying an idle pooled socket that receives unsolicited bytes.

**What was already known.** [RFC 9112 §6.3](https://datatracker.ietf.org/doc/html/rfc9112) (2022) already directs clients not to treat post-response data as a separate response, naming cache poisoning as the reason. Poisoning a *client's* connection pool was published as client-side desync in [Browser-Powered Desync Attacks](https://portswigger.net/research/browser-powered-desync-attacks) (2022, archived), and response queue poisoning in [Making HTTP header injection critical](https://portswigger.net/research/making-http-header-injection-critical-via-response-queue-poisoning) (2022, archived); the runtime had prior socket-reuse race work in 2020. Post-cutoff but decisive on soundness: the maintainer who wrote the fix argued publicly that this is a property of the protocol rather than a bug, that several other major clients share it, and that the fix broke widely deployed downstream packages.
