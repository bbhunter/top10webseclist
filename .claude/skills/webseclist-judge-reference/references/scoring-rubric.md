# Scoring rubric — anchors, examples, and traps

Read this when you are unsure where a candidate lands on a category. Each category
is scored 0–100 independently; the weights only enter when `score.py` combines them.
The bands are the same everywhere: **0–19** little/none · **20–39** limited ·
**40–59** moderate · **60–79** strong · **80–100** exceptional. Score against the
*underlying contribution* you extracted, not against the impact of the demo.

A recurring trap runs through all six categories: **letting impact leak into the
score.** Each section below names the specific version of that leak to watch for.

---

## Original contribution (25%)

*How much genuinely new knowledge, capability, or understanding does the work add?*

Score this against **prior art that was public before the candidate's earliest
verified public disclosure**, not against your own prior ignorance or later work.
The question is whether the field could have known this when the candidate appeared,
not whether you know it now. A later publication covering the same idea cannot lower
this score. It may show continued relevance or later rediscovery, but count it as
influence only when citation, attribution, or other evidence establishes that link.

- **0–19** — Restates or re-demonstrates a technique already well known by the
  cutoff; a new target for an established bug class with no new mechanism.
- **20–39** — Minor variation or a fresh payload for a primitive public before the
  cutoff; independent rediscovery of something already public then.
- **40–59** — A real but incremental extension, or a combination of ideas known by
  the cutoff whose novelty is modest.
- **60–79** — A new primitive, a non-obvious combination that yields a capability that
  had not been publicly described or demonstrated by the cutoff, or a materially
  deeper understanding of a known area.
- **80–100** — Introduces a new class, mechanism, or way of seeing a problem that
  reframes how others will approach it after the cutoff.

**Trap:** a critical-severity, widely-covered CVE can score *low* here if the
technique behind it is textbook. Severity is not on this axis. Conversely, a
"low-impact" quirk that introduces a reusable primitive can score high.

**Rediscovery:** if the same idea was public before the candidate's novelty cutoff,
score novelty against that earlier work even when the candidate reached it
independently — credit the independence in the verdict and confidence, not in this
number. Work first published after the cutoff is not prior art.

---

## Transferability (20%)

*Can the underlying contribution apply beyond the exact reported target or environment?*

You already stripped the target-specific detail in step 1; score what remains.

- **0–19** — Bound to one product, version, or configuration; nothing generalises.
- **20–39** — Might apply to a couple of close cousins, with significant caveats.
- **40–59** — Applies across a family (one framework's ecosystem, one protocol
  feature) given similar preconditions.
- **60–79** — Applies across many technologies that share a mechanism, not just a
  vendor.
- **80–100** — A cross-cutting insight that recurs wherever the underlying assumption
  holds (a parsing model, an encoding step, a trust boundary).

**Trap (both directions):** "product-specific" is not automatically low — a bug in
one CMS may turn on a language-level footgun every app in that language shares. And
"affects thousands of sites" is not automatically high — that can be the reach of a
single well-known misconfiguration, i.e. coverage, not transferable insight.

---

## Lasting value (20%)

*Is it likely to influence future research, testing, tooling, or methodology?*

- **0–19** — A point-in-time fix; nothing to carry forward once patched.
- **20–39** — Useful now, little reason to cite it in a year.
- **40–59** — A solid datapoint others may reference occasionally.
- **60–79** — Likely to be built on, cited, or folded into testing methodology.
- **80–100** — Reshapes how a class of problems is tested or reasoned about for years.

**Patch status does not belong here as a penalty.** A fully-patched technique can
still be foundational (it changed how everyone tests). Judge influence on future
work, not whether today's targets are still vulnerable — that is current
applicability, a different thing.

For an older candidate, use later citations, adaptations, tooling, and rediscoveries
as retrospective evidence in this category. Similarity alone can show continued
relevance or rediscovery, but claim influence only with attribution or another
demonstrated connection. Keep all of this out of the historical Original
contribution comparison.

---

## Technical soundness (15%)

*Are the reasoning, evidence, and conclusions technically convincing?*

- **0–19** — Claims unsupported, mechanism hand-waved, or demonstrably wrong.
- **20–39** — Plausible but thinly evidenced; gaps in the causal chain.
- **40–59** — Mostly sound with some unverified leaps.
- **60–79** — Well-reasoned, evidence matches the claims, limitations acknowledged.
- **80–100** — Rigorous: mechanism explained, claims proven, scope and failure modes
  honest.

Judge the **argument**, not the prose polish or the platform it was published on. A
rough writeup with a correct, well-evidenced mechanism outscores a slick one that
asserts more than it shows.

Later replications, critiques, and corrections may inform this score because they
can test whether the original mechanism and claims hold up. Use them as post-cutoff
technical evidence, never as prior art that rewrites historical novelty.

---

## Practical usability (10%)

*Can others use the contribution in useful security work or further research?*

- **0–19** — Not actionable; needs conditions no one realistically has.
- **20–39** — Usable only in narrow, contrived setups.
- **40–59** — Usable with real but surmountable effort or preconditions.
- **60–79** — Readily applicable in normal testing or research.
- **80–100** — Immediately actionable and broadly applicable; lowers the bar for
  everyone after.

Tooling and methodology contributions often score high here even when Original
contribution is moderate — making an existing idea *usable at scale* is itself value.

---

## Clarity and reproducibility (10%)

*Is there enough information to understand, verify, or reproduce the work?*

- **0–19** — Vague teaser; no steps, no detail to reproduce.
- **20–39** — Gist conveyed, key steps missing.
- **40–59** — Reproducible with effort and some gap-filling.
- **60–79** — Clear, with steps/PoC/enough detail to follow.
- **80–100** — Fully reproducible: precise steps, code or PoC, preconditions stated.

This scores the *evidence available to a reader*, which is distinct from confidence.
Confidence is about *your* certainty in the verdict; clarity is about *the source's*
completeness. A perfectly clear writeup of a duplicate still scores well here — and
still gets a "duplicate" verdict.

---

## Worked mini-examples

These illustrate the impact-vs-novelty split; they are calibration aids, not quotas.

- **Textbook bug, huge target.** SQL injection on a major site via a standard union
  payload, no new mechanism. Original ~10, Transferability ~15, Lasting ~10, even
  though the impact and press were enormous. The technique is decades old.

- **Small quirk, new primitive.** A parser discrepancy in how one library handles a
  delimiter, shown to enable request smuggling in a way not described before the
  candidate's cutoff. Original ~75, Transferability ~70, Lasting ~70 — the target is
  narrow but the primitive generalises and others will hunt for it elsewhere.

- **Strong combination.** Chaining two behaviours known before the cutoff (say a
  client-side path traversal plus a CSRF sink) into a reliable account-takeover
  pattern nobody had assembled by then. Do not anchor on "both parts were known" —
  score the new capability. Often Original ~55–65, Transferability and Lasting high
  if the pattern recurs.

- **Tooling over known ideas.** A fuzzer that automates discovery of a discrepancy
  class public before the cutoff. Original may be ~40, but Practical usability and
  Lasting value can be high because it scales what was previously manual.

- **Independent rediscovery.** A clearly-written technique that a paper publicly
  described two years before the candidate's cutoff. Original scored against that
  prior work (~25–35), verdict "independent rediscovery," confidence set by how
  firmly you established precedence — and the independence noted in the reasoning,
  not added to the number. If the equivalent paper appeared two years *after* the
  candidate, it cannot reduce historical novelty; use it only as post-cutoff context.
