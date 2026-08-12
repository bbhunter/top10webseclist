# Web Hacking Techniques Index

`website/` is the production, dependency-free interface for exploring the Top 10 Web
Hacking Techniques archive. Generated collection shards keep it synchronized with the
repository's real year lists, preliminary collection registry, and reference manifest.

## Run it

Serve the repository root (not this directory) so the mockup can load the archive:

```bash
python3 -m http.server 8000
```

Then open:

<http://localhost:8000/website/>

Run the archive/link smoke test with:

```bash
node website/smoke-test.mjs
```

Regenerate or check the progressive data with:

```bash
node website/build-data.mjs
node website/build-data.mjs --check
```

Build the same static output used by the production hosts with:

```bash
node website/build-site.mjs --target cloudflare  # writes dist/
node website/build-site.mjs --target github      # writes _site/
```

## Publish webhacklist.com with Cloudflare Pages

Cloudflare Pages is the preferred public host for `webhacklist.com`: the app has no
server functions, and static asset requests are free and unlimited. Create a Pages
project connected to this repository with these settings:

- Production branch: `master`
- Build command: `node website/build-data.mjs && node website/build-site.mjs --target cloudflare`
- Build output directory: `dist`
- Root directory: the repository root

Add `webhacklist.com` in **Workers & Pages → Custom domains**. For the apex domain,
Cloudflare requires the domain to be a Cloudflare zone using Cloudflare nameservers.
Add `www.webhacklist.com` separately if it should resolve too, and redirect it to the
apex in Cloudflare.

The build enforces the free plan's 20,000-file and 25 MiB-per-asset limits. Two
preserved PDFs currently exceed 25 MiB. Cloudflare omits those exact files and the app
offers their GitHub Pages copies after its same-origin check fails. The allowlist lives
in `hosting.json`; a newly oversized file fails the build instead of disappearing.
Cloudflare's `_headers` file applies security headers, immediately revalidates the tiny
catalogue, caches versioned year shards for a year, and gives archive documents a
one-day cache with stale revalidation.

## The name search engines print

Google, Bing and the rest take the site name from the home page only, and from
several signals at once: `WebSite` structured data in `index.html`, `og:site_name`,
`application-name`, the `<title>`, the manifest `name`, and the page's single `h1` —
the masthead one, which is why the reading area heads its records with an `h2` naming
the mode instead. All of them say **Web Hacking Techniques Index**, with
`alternateName` and the manifest `short_name` keeping *Web Hack List* eligible as the
domain-shaped short form. Never let an archive mode's name reach one of those fields:
a search engine would print it as the name of the site. The smoke test fails if any
signal disagrees, if a view title leaks in, or if a second `h1` appears.

A search engine may take days or weeks to re-crawl and adopt a changed site name.

## Publish the backup with GitHub Pages

The repository workflow in `.github/workflows/pages.yml` publishes the contents of this
directory at the Pages site root and stages every archive document used by the generated
collections plus the annual listing PDFs. Keep this deployment on its default
`https://irsdl.github.io/webhacklist/` URL: it is the backup origin for the two PDFs
that exceed Cloudflare's per-file limit.

In repository **Settings → Pages**, select **GitHub Actions** as the source. Add the
custom domain to Cloudflare Pages, not to this backup deployment. The workflow may also
be started manually.

## Mobile and full-screen use

All archive routes support 320 px-wide screens. The Investigation Board becomes a
single-column tap list on narrow phones; the Terminal, Constellation, readers and PDF
viewer use dynamic viewport units and safe-area insets. Normal desktop browsers show
a persistent top-bar control that puts the complete website into full screen. Signals,
Constellation, Terminal and Investigation Board also show a mode-level control for a
focused, interface-free view. The web app manifest enables an installed standalone
window from a phone's **Add to Home Screen** action, including on iPhones where element
fullscreen is unavailable.

## Archive routes

Every route is a way into the same archive, so the browser tab always reads
*Web Hacking Techniques Index* and the archive names itself once, in the masthead
heading beside the brand mark. Above the records a route shows only its own name, as
the mode currently open — never as the name of the site.

- Museum at Night — one room per collection, styled in the Signal Observatory's
  instrument theme so both views read as the same receiver
- Infinite Security Library
- Signal Observatory — a longitudinal frequency map for comparing technique
  families across every collection and opening the research behind each peak
- Research Constellation — a freely navigable 3D map of every selected year
- The Hacker Terminal — a CRT archive shell with safe regular-expression search
- The Investigation Board — a draggable corkboard archive view and a compact tap list
  on narrow phones
- Favourite Research — a browser-persistent shortlist shared by every view

This directory is the single production website source and is intended to be committed.

Every artifact can be marked read. Read status persists across all concepts and
appears on exhibits, books, stars and case files. Preserved Markdown opens
in a shared formatted reader with a table of contents, reading progress, code and
table formatting, and links to the raw Markdown, PDF and original source.
The Markdown and PDF viewers share a persistent light/dark reading-theme control.
For PDFs the theme changes the viewer controls and surrounding stage while the
browser-native document keeps its original page colours.

Every artifact can also be added to or removed from favourites in the shared
record panel, Markdown reader, PDF viewer, constellation selection and terminal.
Favourite markers appear in every concept, and the Favourites section filters
the saved shortlist by year or topic. The shortlist is stored only in the local
browser and uses normalized source URLs so the same research stays synchronized
when it appears in more than one collection.

## Submitting research

The top bar, the phone menu and the footer all open one submission form
(`#contribute-dialog`, deep-linkable as `#submit`). It is a static page throughout:
nothing is posted from here. The form does the one thing GitHub cannot — as a source URL
is typed it is matched against every loaded collection, reporting an exact record, the
closest titles, or nothing at all — and then builds a prefilled link to the issue form in
[`.github/ISSUE_TEMPLATE/01-submit-research.yml`](../.github/ISSUE_TEMPLATE/01-submit-research.yml).

A URL matches on two keys: the exact normalized address, and a looser host-and-path key
that sees through `http`, `www.`, a trailing slash, a campaign parameter or a Wayback
replay wrapper. Query strings that are not tracking parameters are kept — on a blog of
the era this archive covers, `?p=123` *is* the article.

The prefill parameter names are the field ids in that YAML file, and the year options
must cover the years the collections span; both couplings are asserted by
`smoke-test.mjs`, because a renamed field would otherwise drop an answer silently.

Every selected record has a share action. Sharing from the artifact panel
restores that record in the current archive concept; sharing from the Markdown
reader or PDF viewer restores the exact format and light/dark reading theme.
Yearly results PDFs are shareable too. Browsers with Web Share use the native
share sheet, with a clipboard copy fallback on desktop.

### Signal Observatory controls

- Tune **All traffic** or one topic family to redraw the twenty-year waveform.
- Select a year pulse to inspect its preservation, reading progress and topic
  distribution without losing the longitudinal context.
- The paper list defaults to **All**, visibly carries the Top 10 block into the
  wider nomination field, and offers counted **Top 10** and **Other nominations**
  filters. Long lists expand 12 records at a time instead of being silently cut.
- Open any paper on the selected frequency in the same artifact, Markdown and
  PDF flow used by every other archive concept.
- Preliminary collections remain explicitly labelled and never show Top 10
  counts or ranking semantics.

### Hacker Terminal controls

- Type `help` for the complete command list.
- `pwd`, `cd /2024`, `cd ..`, `cd /`, and path-aware `ls` navigate a read-only
  virtual filesystem with one directory per collection plus `/favourites`.
- `grep /xss|csrf/i [/path]` searches titles, publishers, topics and URLs with
  regular expressions. Pattern length and input are bounded, while assertions,
  backreferences, repeated groups and ambiguous quantifier combinations are
  rejected before JavaScript's regex engine runs.
- `fav <id>`, `unfav <id>` and `favorites` manage the shared shortlist.
- `open <id> --md` and `open <id> --pdf` use the same shared viewers as every
  other concept; `open <id> --web` opens the original source.
- `history` prints recent commands; Up/down recalls them and Tab completes
  commands, paths and ids.

### Investigation Board controls

- Select a case-folder tab to switch year.
- Drag cards to rearrange the case; the winning evidence remains joined by live
  red string.
- Dense mode fits more evidence on screen, and Reset layout restores the
  deterministic case arrangement.
- Select any card to open the shared artifact panel, Markdown reader or PDF viewer.

### PDF viewer and safety boundary

Preserved PDFs and yearly result listings open in a large browser-native viewer
with fit-width, fit-page, Markdown switching, read-state, download and separate-tab
controls. The application verifies the file with a same-origin `HEAD` request and
an `application/pdf` response before embedding it.

Archive paths are restricted to the expected local Markdown, PDF and yearly-list
directories. External links accept HTTP(S) only and use opener isolation. Raw
Markdown is escaped before formatting, capped at 8 MB, and protected from stale
request races; generated heading ids are namespaced so archived content cannot
clobber the application's own elements. Remote images embed over HTTPS only
(http-only images become links) with referrers suppressed. A restrictive
content-security policy blocks inline scripts, objects, cross-origin frames,
forms, media, workers and cleartext image loads. The smoke test validates these
invariants, actively exercises hostile Markdown and URL payloads, and validates
every referenced local file.

### Constellation controls

- Drag empty space to orbit; drag a research star to tug it into a nearby position
- Use **Tidy stars** to spring moved research back to its original cluster layout
- Scroll, pinch, use the logarithmic on-screen zoom rail, or press `W` / `S` to fly in and out
- `A` / `D` or left/right arrows orbit; `Q` / `E` move vertically
- Click a research star to identify it; double-click or press `F` to fly to it
- Press `Enter` to inspect the selected article and `R` to return to the full map
- Hold the circular navigator's arrows to move up, down, left or right; use its
  curved arrows to turn and its central thrusters to fly forward or backward
- Toggle **Titles** for collision-aware labels whose size and density respond to
  camera depth
- Use the bottom **All / Top 10 / Nominees** filter independently of the topic
  buttons to isolate ranked research or the wider nomination field

Topic buttons isolate one cluster without losing its three-dimensional layout. The
year buttons rebuild the map from that year's real titles, while read markers stay
synchronized with every other archive view. Article stars are shaded miniature
planets with deterministic surface bands, grids, continents, fractures, rings and
occasional moons. Top 10 selections are larger and carry restrained white-gold
coronas, crisp rays and compact `✦ #rank` markers. Tugged stars
remain close to their home cluster and settle with a
small spring, while reduced-motion preferences remove the animated return. Rare
comets cross the background slowly, with reduced-motion preferences respected.
