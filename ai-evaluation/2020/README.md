# 2020 missed-technique audit

This folder records the bounded 2026-08-09 audit for web-security research first
published in 2020 but absent from the original 2020 nomination round. The
exclusion set contained 63 distinct URLs from [`2020.md`](../../2020.md). Exact
URL filtering was followed by semantic comparison against that file and
backward mechanism checks through the 2006–2019 lists and local reference text.

The historical-list gate is **60 or above plus a qualifying non-duplicate
verdict**. A score alone cannot rescue prior disclosure, an existing nomination
under another URL, or work outside offensive web scope. The five entries found
by the earlier audit were retained and reassessed alongside the fresh leads.

## Coverage

- Primary programs and papers from NDSS, IEEE S&P, ACM CCS and USENIX Security.
- PortSwigger Research, Black Hat materials, Project Zero and researcher-hosted
  2020 publications already represented in the year list.
- Browser messaging, framing policy, extension fingerprinting, link previews,
  cookies, upload handling, cache behavior, timing, origins and CDN forwarding.
- Backward searches for `postMessage`, file uploads, clickjacking, extension and
  website fingerprinting, cookie hijacking, cache deception, DOM clobbering,
  prototype pollution, sender authentication and origin rehosting.
- Strict first-publication checks: a 2020 venue appearance did not override an
  earlier public preprint or an earlier-year nomination.

No archive capture was opened, validated or changed during this audit.

## Results

- 23 credible leads were retained.
- 12 candidates received full scorecards: five already-present missed entries
  were reassessed and seven fresh qualifying techniques were added.
- 11 other leads were resolved during screening as wrong-year, already covered,
  measurement/defensive work, scope-adjacent research or a same-mechanism
  companion.
- No full scorecard fell below 60; the screened table preserves the rejected
  leads so a later run need not rediscover them.

| Score | Decision | Verdict | Candidate |
|---:|---|---|---|
| 86.7 | retained; reassessed | Original technique | [Timeless Timing Attacks](https://www.usenix.org/conference/usenixsecurity20/presentation/van-goethem) |
| 84.7 | retained; reassessed | Original technique | [Composition Kills](https://www.usenix.org/conference/usenixsecurity20/presentation/chen-jianjun) |
| 82.2 | retained; reassessed | Original technique | [Prototype Pollution and client-side sanitizer bypasses](https://www.securitum.com/prototype-pollution-and-bypassing-client-side-html-sanitizers.html) |
| 81.5 | added | Tooling or methodology contribution | [PMForce](https://publications.cispa.saarland/3164/) |
| 80.2 | added | Meaningful extension | [Carnus](https://www.ndss-symposium.org/ndss-paper/carnus-exploring-the-privacy-threats-of-browser-extension-fingerprinting/) |
| 78.9 | added | Original technique | [CDN Judo](https://www.ndss-symposium.org/ndss-paper/cdn-judo-breaking-the-cdn-dos-protection-with-itself/) |
| 78.8 | added | Tooling or methodology contribution | [FUSE](https://www.ndss-symposium.org/ndss-paper/fuse-finding-file-upload-bugs-via-penetration-testing/) |
| 77.2 | added | Tooling or methodology contribution | [The Cookie Hunter](https://www.cs.uic.edu/~polakis/classes/CS568/fall-2020/cookiehijacker-ccs20.pdf) |
| 75.0 | added | Tooling or methodology contribution | [A Tale of Two Headers](https://www.usenix.org/conference/usenixsecurity20/presentation/calzavara) |
| 73.5 | retained; reassessed | Original technique | [Melting Pot of Origins](https://www.ndss-symposium.org/ndss-paper/melting-pot-of-origins-compromising-the-intermediary-web-services-that-rehost-websites/) |
| 72.0 | retained; reassessed | Meaningful extension | [DOM Clobbering strikes back](https://portswigger.net/research/dom-clobbering-strikes-back) |
| 71.7 | added | Meaningful extension | [Deceptive Previews](https://www.ndss-symposium.org/ndss-paper/deceptive-previews-a-study-of-the-link-preview-trustworthiness-in-social-platforms/) |

## Screened leads

| Candidate | Outcome | Screening evidence |
|---|---|---|
| [Cached and Confused](https://www.usenix.org/conference/usenixsecurity20/presentation/mirheidari) | already recorded / wrong target year | The work was already nominated as 2019's #1 through its author-hosted paper; the 2020 venue page does not make it a missed 2020 technique. |
| [JIT Leaks](https://sites.cs.ucsb.edu/~rosner/papers/JITleaks-TechReport2018.pdf) | wrong year | The primary technical report is explicitly dated 2018, before the IEEE S&P 2020 appearance. |
| [Cross-Origin State Inference Attacks](https://arxiv.org/abs/1908.02204) | wrong year | The primary preprint was public on 6 August 2019. |
| [On Using Application-Layer Middlebox Protocols for Peeking Behind NAT Gateways](https://www.ndss-symposium.org/ndss-paper/on-using-application-layer-middlebox-protocols-for-peeking-behind-nat-gateways/) | same mechanism / existing nominee | NAT-ALG traversal is represented by NAT Slipstreaming in the original 2020 Top 10; this paper is a parallel systematic treatment, not a separate missed class. |
| [Meddling Middlemen](https://seclab.bu.edu/papers/proxy_browsers-oakland20.pdf) | measurement of known mechanisms | Measures TLS, proxy and header failures in data-saving browsers; it does not introduce a distinct offensive primitive. |
| [High Precision Open-World Website Fingerprinting](https://www.cs.sfu.ca/~taowang/wf/Wa-open.pdf) | scope-adjacent extension | Precision optimization materially improves an established network-traffic fingerprinting line, but is not sufficiently web-mechanism-specific for this list. |
| Complex Security Policy? A Longitudinal Analysis of Deployed CSP | measurement | Longitudinal CSP deployment analysis informs defenses without adding a reusable attack method. |
| Shim Shimmeny: Evaluating the Security and Privacy Contributions of Link Shimming in the Modern Web | measurement / defensive | Studies tracking and protection behavior around link shims rather than introducing a hacking technique. |
| You’ve Changed: Detecting Malicious Browser Extensions through Update Deltas | defensive | Detects malicious extension updates; no separate offensive contribution. |
| Zero-delay defenses for timing attacks during web authentication | defensive | Mitigates timing attacks; Timeless Timing Attacks captures the distinct offensive contribution. |
| NoJITsu / Slimium / browser-renderer isolation work | defensive | These systems reduce browser attack surfaces without defining an offensive web mechanism. |

## Gate note

All seven fresh additions are above 70, but this audit applies the repository's
current **60-or-above** historical gate. The wording in `2020.md` was corrected
accordingly. This pass did not run the reference archiver or refresh either web
application.
