---
name: webseclist-refresh-web-apps
description: Refreshes the production website from the repository's year-list Markdown, archive manifest, and year registry. Use when a finalized year list, preliminary *-ai collection, preserved reference, original listing, or generated website collection changes, or when the archive UI appears stale.
---

# Refresh Web Apps

Keep the production static archive synchronized without confusing an AI-collected snapshot with a community-ranked Top 10.

## Preserve the data boundaries

- Treat root year lists such as `2006.md` through `2025.md` as hand-curated source material. Never rewrite them during an app refresh.
- Treat `website/archive-years.json` as the publishing registry.
- Treat `website/hosting.json` as the checked-in hosting constraint registry. Keep its oversized-file fallbacks exact and fail deployment when an unlisted file exceeds the host limit.
- Treat `website/data/catalogue.json` and `website/data/collections/*.json` as generated output. Regenerate them with `node website/build-data.mjs`; never edit them directly. The catalogue and every shard share a content version.
- If finalized or preliminary citations changed, or a referenced capture is faulty, follow the repository faulty-capture rule in `CLAUDE.md` (faulty captures are filed, not worked around) and the `webseclist-archive-references` skill. Do not hide the fault in app code.

## Classify the update

1. Inspect the changed root Markdown, `archived-references/manifest.json`, and `original-listings/`.
2. For a finalized year, register it with `status: "final"` and `ranked: true`. Its annual results PDF may be exposed.
3. For an AI-collected or otherwise provisional year, use a distinct filename such as `2026-ai.md` and register it with all of:
   - `status: "preliminary"`
   - `ranked: false`
   - a plain-language `notice` saying it is incomplete, unranked, not community-vetted, and subject to change
   - `asOf`, `provenance`, `contentStart`, and `contentEnd`
   - exact `<!-- archived-references:start -->` and `<!-- archived-references:end -->` boundaries around publishable research bullets
4. Keep scoring notes, watchlists, and dropped candidates outside the registered content boundaries. Only research leads between the two exact headings become app records.
5. Never create a Top 10 filter, winner count, rank badge, or yearly results-PDF action for a preliminary record.

## Refresh the archive

If finalized or preliminary citations, their collection status, or preserved copies changed, use `webseclist-archive-references` first and complete its durable-store workflow. That workflow owns reference acquisition, promotion/pruning, Markdown/PDF preservation, manifest updates, validation queues, and `document-gaps.md` generation.

Then run the bundled refresh command from the repository root:

```bash
python3 .claude/skills/webseclist-refresh-web-apps/scripts/refresh_web_apps.py
```

It validates registry coverage and preliminary boundaries, regenerates the website's versioned progressive catalogue, enforces raw payload budgets, checks JavaScript syntax, and runs the archive smoke test. Use `--check-only` when reviewing without changing generated output.

Publish generated shards before (or atomically with) `data/catalogue.json`. Give the catalogue a short cache lifetime or revalidation policy; collection URLs include the catalogue content version and may be cached for a long time. The app opens one collection first, then fetches other collections during browser idle time. It skips background prefetch on Save-Data and 2G connections and still loads any requested collection on demand.

Before publishing, stage the selected host and enforce its limits:

```bash
node website/build-site.mjs --target cloudflare
node website/build-site.mjs --target github
```

The Cloudflare build must stay below 20,000 files and 25 MiB per static asset. GitHub Pages remains the backup origin for exact oversized PDFs registered in `website/hosting.json`; do not add a broad cross-origin fallback.

## Publish and synchronize the hosts

The checked-in pipeline has two independent deployments from `master`:

- Cloudflare Pages is the production host for `https://webhacklist.com/`. Its Git integration must use the repository root, the build command `node website/build-data.mjs && node website/build-site.mjs --target cloudflare`, and output directory `dist`.
- GitHub Pages is the narrow oversized-file origin at `https://irsdl.github.io/webhacklist/`. Repository **Settings → Pages → Build and deployment** must use **GitHub Actions**; `.github/workflows/pages.yml` stages only a small landing page and the exact fallback files, not a second copy of the full archive.

For the one-time dashboard and DNS setup, follow the local launch guide at `.tmp/webhacklist-launch/README.md` when it is present. That directory is intentionally gitignored because it is an operator checklist, not site content. Keep the custom domain only on Cloudflare; do not add a GitHub Pages custom domain or a `CNAME` file. Do not add a blanket **Cache Everything** rule: Pages already applies deployment-aware edge caching, while `website/_headers` gives the catalogue a revalidation policy, immutable collection shards long-lived browser caching, and archive documents bounded caching.

After every successful refresh:

1. Review and commit the changed source files plus generated `website/data/catalogue.json` and `website/data/collections/*.json`, then push `master`.
2. No routine manual upload, DNS edit, Cloudflare cache purge, or GitHub Pages action is needed. The push triggers both deployments automatically.
3. In GitHub **Actions**, confirm **Deploy archive website to GitHub Pages** completed. In Cloudflare **Workers & Pages → webhacklist → Deployments**, confirm the production deployment completed.
4. Open `https://webhacklist.com/` and verify the catalogue version/current collection. If oversized fallback PDFs changed, wait for GitHub Pages first and test every exact URL from `website/hosting.json`, then test the same record through the Cloudflare site.
5. Purge Cloudflare cache only when a successful deployment is confirmed but the custom domain still serves stale content. A failed deployment, missing source file, or filed capture fault must be fixed at its source rather than hidden with a purge or app exception.

Dashboard work is required again only when the domain/DNS, production branch, build command, output directory, Pages workflow, or an oversized fallback mapping changes. Report both deployment results and any required operator action in the refresh handoff.

## Review the result

- Confirm the website reports the expected finalized-year and document totals.
- In `website`, open every one of Museum, Library, Constellation, Hacker Terminal, and Investigation Board on a preliminary year.
- Confirm the warning is prominent, the item count matches the source range, no item has a rank, and no annual results PDF is offered.
- Confirm preserved Markdown, preserved PDF, original-source links, read state, search, and artifact details still work wherever corresponding files exist.
- Confirm the initial route requests `data/catalogue.json` and one collection shard, not `archived-references/manifest.json` or every root year Markdown file. Confirm global search and Favourites complete after the remaining shards load.
- At 320 px width, confirm the evidence list is tappable without dragging and the terminal, constellation, Markdown reader, and PDF viewer fit the dynamic viewport. In a normal desktop browser, confirm the persistent top-bar control enters and exits site-wide full screen on every route. Confirm the per-view control is visible and enters/exits focused full screen in Museum, Library, Signals, Constellation, Hacker Terminal, Investigation Board, and Favourites & Read; when the browser withholds its native Fullscreen API, confirm the full-window fallback enters and exits instead.
- Confirm the Markdown reader escapes raw HTML, never loads third-party images automatically, gives those images explicit outbound links, and rejects executable or credential-bearing URLs. Confirm terminal `grep` rejects lookarounds, backreferences, quantified groups, unbounded repetition, excessive bounds, and unsupported flags before constructing a regular expression.
- Report which source lists changed, whether the archive workflow ran, generated-data counts, preliminary counts, and all validation commands.
- Report the GitHub Actions and Cloudflare Pages deployment state after the push, or clearly say that the operator still needs to push and verify them.
