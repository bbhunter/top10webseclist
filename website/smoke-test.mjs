import { access, readdir, readFile } from "node:fs/promises";
import { constants } from "node:fs";
import path from "node:path";
import process from "node:process";
import vm from "node:vm";

const root = process.cwd();
const yearRegistry = JSON.parse(await readFile(path.join(root, "website/archive-years.json"), "utf8"));
const yearRecords = yearRegistry.years || [];
const years = yearRecords.map((record) => record.id);
// Empty is the healthy state: paths come from the archive's own rule below.
const knownMissingPaths = new Set([]);

function normalizeUrl(value) {
  try {
    const url = new URL(value);
    url.hash = "";
    url.hostname = url.hostname.toLowerCase();
    url.pathname = url.pathname.replace(/\/$/, "");
    return url.toString().replace(/\/$/, "");
  } catch {
    return String(value).replace(/\/$/, "");
  }
}

async function exists(file) {
  try {
    await access(path.join(root, file), constants.R_OK);
    return true;
  } catch {
    return false;
  }
}

const manifest = JSON.parse(await readFile(path.join(root, "archived-references/manifest.json"), "utf8"));
const lookup = new Map();
const unsafeManifestPaths = [];

// The same rule app.js uses: open the exact safe path advertised by the
// manifest. This matters when a reference is cited by more than one year and
// its citation ordering differs from the collection that owns its files.
const noPdfKinds = new Set(["video"]);
// Both halves of a translated pair are published, so both are path-checked here.
function archivePathsFor(record) {
  if (!record?.slug || !record?.grade || !record?.content_sha256) return { md: "", pdf: "", translatedMd: "", translatedPdf: "" };
  const noPdf = noPdfKinds.has(record.kind || "");
  return {
    md: record.steps?.render?.file || "",
    pdf: noPdf ? "" : record.steps?.pdf?.file || "",
    translatedMd: record.steps?.render?.translation_file || "",
    translatedPdf: noPdf ? "" : record.steps?.["pdf-translation"]?.file || ""
  };
}

for (const [url, record] of Object.entries(manifest.urls || {})) {
  const aliases = [url, ...(record.spellings || []), record.health?.final_url, ...(record.also_at || [])].filter(Boolean);
  for (const alias of aliases) lookup.set(normalizeUrl(alias), record);
  const { md: mdPath, pdf: pdfPath, translatedMd, translatedPdf } = archivePathsFor(record);
  for (const candidate of [mdPath, translatedMd]) {
    if (candidate && !/^archived-references\/md\/[a-z0-9-]+\/[a-z0-9._-]+\.md$/i.test(candidate)) unsafeManifestPaths.push(candidate);
  }
  for (const candidate of [pdfPath, translatedPdf]) {
    if (candidate && !/^archived-references\/pdf\/[a-z0-9-]+\/[a-z0-9._-]+\.pdf$/i.test(candidate)) unsafeManifestPaths.push(candidate);
  }
}

// One bullet is one research, however many links it carries - the same grouping
// app.js parses, so the counts here are the counts the page shows.
// Escaped brackets in a label are part of it - see app.js parseYearMarkdown.
const LINK_RE = /\[((?:[^\]\\]|\\.)+)\]\((?:<(https?:\/\/[^>\s]+)>|(https?:\/\/[^)\s]+))\)/g;
const artifacts = [];
for (const year of years) {
  const markdown = await readFile(path.join(root, `${year}.md`), "utf8");
  const yearRecord = yearRecords.find((record) => record.id === year) || {};
  let inContentRange = !yearRecord.contentStart;
  for (const line of markdown.split(/\r?\n/)) {
    if (yearRecord.contentStart && line.trim() === yearRecord.contentStart) {
      inContentRange = true;
      continue;
    }
    if (inContentRange && yearRecord.contentEnd && line.trim() === yearRecord.contentEnd) break;
    if (!inContentRange) continue;
    if (!/^\s*-\s/.test(line)) continue;
    const links = [...line.matchAll(LINK_RE)].map((match) => ({ title: match[1], url: match[2] || match[3] }));
    if (!links.length) continue;
    artifacts.push({
      year,
      rank: /\*\*#(\d+)\*\*/.exec(line)?.[1] || null,
      title: links[0].title,
      originalUrl: links[0].url,
      record: lookup.get(normalizeUrl(links[0].url)),
      links: links.map((link) => ({ ...link, record: lookup.get(normalizeUrl(link.url)) }))
    });
  }
}

const missingLocalFiles = [];
let markdownCount = 0;
let pdfCount = 0;
for (const artifact of artifacts) {
  // A reader opens the first preserved copy across the research's links.
  const resolved = artifact.links.map((link) => archivePathsFor(link.record));
  const md = resolved.map((paths) => paths.md).find((file) => file && !knownMissingPaths.has(file)) || "";
  const pdf = resolved.map((paths) => paths.pdf).find((file) => file && !knownMissingPaths.has(file)) || "";
  if (md) {
    markdownCount++;
    if (!(await exists(md))) missingLocalFiles.push(md);
  }
  if (pdf) {
    pdfCount++;
    if (!(await exists(pdf))) missingLocalFiles.push(pdf);
  }
}

const annualPdfFiles = yearRecords.filter((record) => record.ranked !== false).map(({ id: year }) => {
  const combined = ["2006", "2012", "2013", "2014", "2015"].includes(year);
  return `original-listings/${year}-${combined ? "nominees-and-top10" : "top10"}.pdf`;
});
const missingAnnualPdfs = [];
for (const file of annualPdfFiles) if (!(await exists(file))) missingAnnualPdfs.push(file);
const mockupFiles = [
  "website/404.html",
  "website/index.html",
  "website/archive-years.json",
  "website/brand-mark.svg",
  "website/styles.css",
  "website/app.js",
  "website/constellation.js",
  "website/build-site.mjs",
  "website/hosting.json",
  "website/site.webmanifest",
  "website/_headers"
];
const missingMockupFiles = [];
for (const file of mockupFiles) if (!(await exists(file))) missingMockupFiles.push(file);
const indexSource = await readFile(path.join(root, "website/index.html"), "utf8");
const appSource = await readFile(path.join(root, "website/app.js"), "utf8");
const constellationSource = await readFile(path.join(root, "website/constellation.js"), "utf8");
const stylesSource = await readFile(path.join(root, "website/styles.css"), "utf8");
const buildSiteSource = await readFile(path.join(root, "website/build-site.mjs"), "utf8");
const headersSource = await readFile(path.join(root, "website/_headers"), "utf8");
const notFoundSource = await readFile(path.join(root, "website/404.html"), "utf8");
const progressiveCatalogue = JSON.parse(await readFile(path.join(root, "website/data/catalogue.json"), "utf8"));
const progressiveRecord = [...progressiveCatalogue.years].reverse().find((record) => record.status === "final") || progressiveCatalogue.years.at(-1);
const progressiveShard = JSON.parse(await readFile(path.join(root, `website/data/collections/${progressiveRecord.id}.json`), "utf8"));
const sourceBundle = `${indexSource}\n${appSource}`;
const unsafeBlankTargets = sourceBundle.match(/<a\b(?=[^>]*target=["']_blank["'])(?![^>]*rel=["'][^"']*noopener)[^>]*>/gi) || [];

// Exercise the actual URL and Markdown renderers without a browser. All source
// content begins as untrusted text; only the allowlisted tags emitted by the
// renderer may reach an innerHTML sink.
const clientContext = vm.createContext({
  URL,
  location: { href: "https://archive.example/website/#museum" },
  localStorage: { getItem: () => null, setItem: () => {} },
  document: { querySelector: () => null, querySelectorAll: () => [] },
  navigator: {}
});
vm.runInContext(appSource.replace(/\nloadArchive\(\);\s*$/, ""), clientContext);
const clientEval = (expression) => vm.runInContext(expression, clientContext);
let progressiveRequestUrl = "";
clientContext.__progressiveCatalogue = progressiveCatalogue;
clientContext.__progressiveShard = progressiveShard;
clientContext.__progressiveYear = progressiveRecord.id;
clientContext.fetch = async (url) => {
  progressiveRequestUrl = String(url);
  return { ok: true, json: async () => progressiveShard };
};
const progressiveLoad = JSON.parse(await clientEval(`
  ARCHIVE_CATALOGUE = __progressiveCatalogue;
  YEAR_RECORDS = ARCHIVE_CATALOGUE.years;
  YEAR_FILES = YEAR_RECORDS.map((record) => record.id);
  state.archiveTotal = ARCHIVE_CATALOGUE.total;
  ensureCollection(__progressiveYear).then((items) => JSON.stringify({
    count: items.length,
    loaded: loadedCollections.has(__progressiveYear),
    year: items[0]?.year,
    read: items[0]?.read,
    favourite: items[0]?.favourite
  }))
`));
const hostileMarkdown = [
  "# <img src=x onerror=globalThis.pwned=1>",
  "<script>globalThis.pwned=2</script>",
  "[script link](javascript:globalThis.pwned=3)",
  "![breaker](https://example.test/x\" onerror=\"globalThis.pwned=4)",
  "[breaker](https://example.test/x\" onmouseover=\"globalThis.pwned=5)",
  "<svg onload=globalThis.pwned=6></svg>",
  "<https://example.test/?a=1&b=2>"
].join("\n\n");
const hostileHtml = clientEval(`markdownDocument(${JSON.stringify(hostileMarkdown)}).html`);
const externalImageHtml = clientEval(`markdownDocument("![private probe](https://127.0.0.1/admin)").html`);
const mutationMarkdown = "[**label**](https://example.test/a__b**c) and `code`";
const mutationHtml = clientEval(`markdownDocument(${JSON.stringify(mutationMarkdown)}).html`);
const hostileRegistryRecord = [{ id: "2025", label: '"><img src=x onerror=globalThis.pwned=7>', status: "final" }];
const hostileYearPills = clientEval(`YEAR_RECORDS = ${JSON.stringify(hostileRegistryRecord)}; yearPills("2025")`);
// The collection id reaches data-year/data-signal-year/data-term-command as an
// attribute value, so it has to be escaped at the sink and not only validated
// on the way in from the catalogue.
const hostileIdRecord = [{ id: '"><img src=x onerror=globalThis.pwned=8>', label: "2025", status: "final" }];
const hostileIdMarkup = clientEval(`
  YEAR_RECORDS = ${JSON.stringify(hostileIdRecord)};
  YEAR_FILES = YEAR_RECORDS.map((record) => record.id);
  yearPills(YEAR_FILES[0]) + terminalRootListing()
`);
const artifactShareUrl = clientEval(`state.view = "library"; documentShareUrl({ id: "2025-0" }, "artifact")`);
const readerShareUrl = clientEval(`state.view = "signals"; state.readingTheme = "light"; documentShareUrl({ id: "2025-0" }, "reader")`);
const resultsShareUrl = clientEval(`state.pdfPath = "original-listings/2025-top10.pdf"; documentShareUrl(null, "results")`);
const repositoryArchiveUrl = clientEval(`archiveUrl("archived-references/md/2025/example.md", "md")`);
const deployedArchiveUrl = clientEval(`location.href = "https://archive.example/webhacklist/#museum"; archiveUrl("archived-references/md/2025/example.md", "md")`);
const terminalPaths = clientEval(`YEAR_FILES = ["2016-17", "2024"]; state.terminalCwd = "/2024"; state.terminalPreviousCwd = "/"; JSON.stringify([resolveTerminalPath(".."), resolveTerminalPath("/"), resolveTerminalPath("../2016"), terminalPathExists("/favourites")])`);
// Favourites and read state are two independent browser-local lists, and both
// filter across any combination of years and topics.
const savedFilters = JSON.parse(clientEval(`
  state.items = [
    { id: "a", year: "2024", topic: "XSS", title: "A", rank: null, favourite: true, read: false },
    { id: "b", year: "2024", topic: "HTTP", title: "B", rank: null, favourite: false, read: true },
    { id: "c", year: "2019", topic: "XSS", title: "C", rank: null, favourite: true, read: true },
    { id: "d", year: "2011", topic: "HTTP", title: "D", rank: null, favourite: false, read: false }
  ];
  state.savedYears = new Set();
  state.savedTopics = new Set();
  const favourites = savedItems("favourites").length;
  const read = savedItems("read").length;
  const both = savedItems("all").length;
  state.savedMode = "all";
  state.savedYears = new Set(["2024", "2019"]);
  const twoYears = savedFilteredItems().length;
  state.savedYears = new Set(["2019"]);
  const oneYear = savedFilteredItems().length;
  state.savedYears = new Set(["2024", "2019"]);
  state.savedTopics = new Set(["XSS"]);
  const yearAndTopic = savedFilteredItems().length;
  state.items = [];
  state.savedMode = "favourites";
  state.savedYears = new Set();
  state.savedTopics = new Set();
  JSON.stringify({ favourites, read, both, twoYears, oneYear, yearAndTopic })
`));
const emittedTags = hostileHtml.match(/<[^>]+>/g) || [];
const unsafeRenderedTags = emittedTags.filter((tag) =>
  /<(?:script|iframe|svg|object|embed)\b/i.test(tag)
  || /\son[a-z]+\s*=/i.test(tag)
  || /\s(?:href|src)\s*=\s*["']\s*(?:javascript|data):/i.test(tag)
);
const activeClientSecurityChecks = [
  clientEval(`safeExternalUrl("javascript:alert(1)")`) === "",
  clientEval(`safeExternalUrl("data:text/html,<script>alert(1)</script>")`) === "",
  clientEval(`safeExternalUrl("https://user:pass@example.test/")`) === "",
  clientEval(`safeArchivePath("../app.js", "md")`) === "",
  clientEval(`safeArchivePath("archived-references/md/2025/example.md", "md")`) === "archived-references/md/2025/example.md",
  unsafeRenderedTags.length === 0,
  hostileHtml.includes("&lt;script&gt;"),
  hostileHtml.includes("https://example.test/?a=1&amp;b=2"),
  !hostileYearPills.includes("<img") && hostileYearPills.includes("&lt;img"),
  !hostileIdMarkup.includes('"><img') && hostileIdMarkup.includes("&lt;img"),
  artifactShareUrl === "https://archive.example/website/#library/2025-0",
  readerShareUrl === "https://archive.example/website/?reader=2025-0&theme=light#signals/2025-0",
  resultsShareUrl === "https://archive.example/website/?results=2025&theme=light#signals",
  repositoryArchiveUrl === "https://archive.example/archived-references/md/2025/example.md",
  deployedArchiveUrl === "https://archive.example/webhacklist/archived-references/md/2025/example.md",
  clientEval(`compileSafeGrep("/xss|csrf/i").regex.test("XSS research")`) === true,
  Boolean(clientEval(`compileSafeGrep("(a+)+$").error`)),
  Boolean(clientEval(`compileSafeGrep("(a|aa)+$").error`)),
  Boolean(clientEval(`compileSafeGrep("a.*b").error`)),
  Boolean(clientEval(`compileSafeGrep("a+a?$").error`)),
  clientEval(`compileSafeGrep("^CVE-\\\\d{4}-\\\\d{1,7}$").regex.test("CVE-2026-12345")`) === true,
  !externalImageHtml.includes("<img") && externalImageHtml.includes("external-image-reference") && externalImageHtml.includes("target=\"_blank\""),
  !mutationHtml.match(/(?:href|src)="[^"]*</) && mutationHtml.includes("<strong>label</strong>") && mutationHtml.includes("<code>code</code>"),
  terminalPaths === '["/","/","/2016-17",true]',
  // Route names must be own properties: a bare VIEWS[name] lookup also answers
  // for every Object.prototype key, so "#__proto__" would pass the guard.
  clientEval(`isViewName("__proto__") || isViewName("constructor") || isViewName("toString")`) === false,
  clientEval(`resolveViewHash("__proto__") === null && resolveViewHash("constructor") === null`) === true,
  clientEval(`resolveViewHash("museum").view`) === "museum",
  clientEval(`JSON.stringify(resolveViewHash("read"))`) === '{"view":"favourites","savedMode":"read"}',
  progressiveLoad.count === progressiveRecord.count,
  progressiveLoad.loaded && progressiveLoad.year === progressiveRecord.id,
  progressiveLoad.read === false && progressiveLoad.favourite === false,
  progressiveRequestUrl === `data/collections/${progressiveRecord.id}.json?v=${progressiveCatalogue.version}`
];
const securityChecks = [
  indexSource.includes("Content-Security-Policy"),
  indexSource.includes("object-src 'none'"),
  indexSource.includes("frame-src 'self'"),
  indexSource.includes("img-src 'self' data:") && !indexSource.includes("img-src 'self' data: https:"),
  indexSource.includes('id="pdf-dialog"'),
  indexSource.includes('id="pdf-frame"'),
  appSource.includes("function safeArchivePath"),
  appSource.includes('method: "HEAD"'),
  !/img-src[^;]*\bhttp:/.test(indexSource),
  !hostileHtml.includes("<img"),
  appSource.includes('`md-${'),
  !/\beval\s*\(|new\s+Function\s*\(|document\.write\s*\(/.test(sourceBundle),
  unsafeBlankTargets.length === 0,
  ...activeClientSecurityChecks
];
const constellationChecks = [
  constellationSource.includes("tugNode(node, deltaX, deltaY, timeStamp)"),
  constellationSource.includes("tidyStars()"),
  constellationSource.includes("separateArticleNodes() {"),
  constellationSource.includes("const radius = 62 + ring * 24 + random() * 46"),
  constellationSource.includes("drawWinnerHalo(node, projected, size, time, visibility)"),
  constellationSource.includes("const compactStar = !winner && size < 5.2"),
  constellationSource.includes("size * 3.15 * prominence"),
  constellationSource.includes("const badgeRects = []"),
  !constellationSource.includes("ctx.shadowBlur = selected ? 28 : hovered ? 20 : 10"),
  constellationSource.includes('const isTopTen = (item) => item?.section === "winner"'),
  constellationSource.includes("prefers-reduced-motion: reduce"),
  constellationSource.includes("refreshFavouriteState()"),
  constellationSource.includes("node.item.favourite"),
  appSource.includes('id="space-tidy" type="button" disabled'),
  appSource.includes("GOLD HALO / TOP 10"),
  appSource.includes('data-star-status="top10"'),
  appSource.includes('starStatus: "all"'),
  stylesSource.includes(".is-star-tugging")
];
const requestedViews = [...indexSource.matchAll(/data-view="([^"]+)"/g)].map((match) => match[1]);
const experienceChecks = [
  JSON.stringify(requestedViews) === JSON.stringify(["museum", "library", "signals", "constellation", "terminal", "evidence", "favourites"]),
  indexSource.includes('src="brand-mark.svg"'),
  indexSource.includes("WEB HACKING"),
  !indexSource.includes("brand-glyph"),
  stylesSource.includes("--accent: #ffb454"),
  stylesSource.includes("--signal: #7899ff"),
  !indexSource.includes('src="castle.js"'),
  !appSource.includes("function renderCastle"),
  !appSource.includes("function renderTimeline"),
  !appSource.includes("function renderDig"),
  !appSource.includes("function renderCatalogue"),
  appSource.includes('title: "The Hacker Terminal"'),
  appSource.includes('title: "The Investigation Board"'),
  appSource.includes('title: "Signal Observatory"'),
  // The page is named for the archive, not for the room being viewed. The one
  // h1 is the masthead's site name; over the records a small h2 names the mode,
  // and no display heading repeats the site name there.
  indexSource.includes('<h1 class="brand-copy"><strong>WEB HACKING</strong><b>TECHNIQUES INDEX</b>'),
  (indexSource.match(/<h1[ >]/g) || []).length === 2, // the masthead, plus the boot screen app.js removes
  indexSource.includes('<h2 class="view-mode" id="view-mode">'),
  !indexSource.includes("view-title"),
  !appSource.includes("#view-title"),
  !stylesSource.includes(".view-intro h1"),
  appSource.includes('$("#view-mode").textContent = copy.title'),
  appSource.includes("document.title = SITE_DOCUMENT_TITLE"),
  !appSource.includes("${copy.title} — Web Hacking Techniques Index"),
  clientEval("SITE_DOCUMENT_TITLE") === (indexSource.match(/<title>([^<]*)<\/title>/) || [])[1],
  stylesSource.includes(".view-intro .view-mode"),
  appSource.includes("function renderSignals"),
  appSource.includes('signalStatus: "all"'),
  appSource.includes('data-signal-status="top10"'),
  appSource.includes('data-signal-status="nominee"'),
  appSource.includes("data-signal-more"),
  appSource.includes('dialog.classList.toggle("signal-artifact", signalMode)'),
  appSource.includes("function documentShareUrl"),
  appSource.includes("function shareDocument"),
  indexSource.includes('id="pdf-share"'),
  appSource.includes('id="reader-share"'),
  appSource.includes("function terminalCompletion"),
  appSource.includes("function compileSafeGrep"),
  appSource.includes("function resolveTerminalPath"),
  appSource.includes("function renderFavourites"),
  appSource.includes("function setFavouriteState"),
  appSource.includes('fetch("data/catalogue.json"'),
  !appSource.includes('fetch("../archived-references/manifest.json"'),
  appSource.includes("scheduleArchivePrefetch"),
  appSource.includes("connection?.saveData"),
  indexSource.includes('id="favourite-count"'),
  indexSource.includes('id="read-count"'),
  appSource.includes("function savedItems"),
  appSource.includes("function readItems"),
  appSource.includes('const SAVED_MODES = ["favourites", "read", "all"]'),
  appSource.includes("state.savedYears.has(item.year)"),
  appSource.includes("state.savedTopics.has(item.topic)"),
  appSource.includes('data-saved-mode="'),
  appSource.includes("data-saved-year="),
  appSource.includes("data-saved-topic="),
  appSource.includes("data-saved-unread="),
  stylesSource.includes(".saved-modes"),
  stylesSource.includes(".saved-filter-note"),
  savedFilters.favourites === 2 && savedFilters.read === 2 && savedFilters.both === 3,
  savedFilters.twoYears === 3 && savedFilters.oneYear === 1 && savedFilters.yearAndTopic === 2,
  indexSource.includes('href="https://github.com/irsdl/webhacklist"'),
  indexSource.includes('href="https://github.com/irsdl/webhacklist/blob/master/.claude/skills/webseclist-judge-reference/SKILL.md"'),
  indexSource.includes('href="https://x.com/irsdl"'),
  indexSource.includes('class="site-footer"'),
  // Support asks: a sponsor entry in both navigations, and a footer block that
  // pairs the free ask (star) with the paid one.
  (indexSource.match(/href="https:\/\/github\.com\/sponsors\/irsdl"/g) || []).length === 3,
  indexSource.includes('class="support-actions"'),
  indexSource.includes('class="support-action is-star"') && indexSource.includes("Star it on GitHub"),
  indexSource.includes('class="support-action is-sponsor"'),
  indexSource.includes('href="https://github.com/irsdl/webhacklist/blob/master/SUPPORT.md"'),
  stylesSource.includes(".support-action.is-star") && stylesSource.includes(".support-action.is-sponsor"),
  indexSource.includes("Jeremiah Grossman") && indexSource.includes("created the list and curated 2006–2015"),
  indexSource.includes("James Kettle") && indexSource.includes("PortSwigger") && indexSource.includes("curators since 2016"),
  indexSource.includes("Every researcher behind the 1,100+ techniques collected here"),
  indexSource.includes("Soroush Dalili (@irsdl)"),
  appSource.includes("openReader(item)"),
  appSource.includes("openPdfViewer(item)"),
  appSource.includes("function layoutInvestigationBoard"),
  appSource.includes("function makeInvestigationCardDraggable"),
  stylesSource.includes(".hacker-terminal"),
  stylesSource.includes(".investigation-board"),
  stylesSource.includes(".signal-observatory"),
  stylesSource.includes(".artifact-dialog.signal-artifact"),
  stylesSource.includes(".signal-status-filter")
];
// Search engines print ONE name above the result, and they pick it from these
// signals together. They have to agree, or the name of whichever archive mode
// happens to be open gets printed as the name of the site.
const SITE_NAME = "Web Hacking Techniques Index";
const structuredData = JSON.parse((indexSource.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/) || [])[1] || "null");
const webManifest = JSON.parse(await readFile(path.join(root, "website/site.webmanifest"), "utf8"));
const metaContent = (name) => (indexSource.match(new RegExp(`<meta (?:name|property)="${name}" content="([^"]*)"`)) || [])[1];
const documentTitle = (indexSource.match(/<title>([^<]*)<\/title>/) || [])[1] || "";
const viewTitles = Object.values(JSON.parse(clientEval("JSON.stringify(VIEWS)"))).map((view) => view.title);
const deploymentChecks = [
  structuredData?.["@type"] === "WebSite",
  structuredData?.name === SITE_NAME,
  structuredData?.alternateName === "Web Hack List",
  structuredData?.url === "https://webhacklist.com/",
  metaContent("og:site_name") === SITE_NAME,
  metaContent("og:title") === SITE_NAME,
  metaContent("application-name") === SITE_NAME,
  webManifest.name === SITE_NAME,
  clientEval("SITE_TITLE") === SITE_NAME,
  documentTitle.startsWith(SITE_NAME),
  viewTitles.length === 7,
  !viewTitles.some((title) => `${documentTitle} ${metaContent("og:site_name")} ${structuredData?.name}`.includes(title)),
  indexSource.includes('rel="canonical" href="https://webhacklist.com/"'),
  indexSource.includes('rel="manifest" href="site.webmanifest"'),
  indexSource.includes('id="site-fullscreen"'),
  indexSource.includes('id="view-fullscreen"'),
  appSource.includes('const FULLSCREEN_VIEWS = new Set(["museum", "library", "signals", "constellation", "terminal", "evidence", "favourites"])'),
  clientEval(`[...FULLSCREEN_VIEWS].every((view) => Object.hasOwn(VIEWS, view)) && Object.keys(VIEWS).every((view) => FULLSCREEN_VIEWS.has(view))`) === true,
  appSource.includes("function toggleSiteFullscreen"),
  appSource.includes("requestFullscreen(document.documentElement)"),
  appSource.includes("function toggleViewFullscreen"),
  appSource.includes("function setViewFullscreenFallback") && appSource.includes("viewButton.hidden = !supportedView"),
  stylesSource.includes("height: 100dvh"),
  stylesSource.includes(".investigation-board { display: grid; min-height: 0 !important"),
  stylesSource.includes("main:fullscreen .favourites-view"),
  stylesSource.includes("main:fullscreen .museum-map"),
  stylesSource.includes("main.view-fullscreen-fallback .museum-map") && stylesSource.includes("main.view-fullscreen-fallback .library-hall"),
  progressiveCatalogue.hosting?.cloudflareMaxAssetBytes === 26214400,
  Object.keys(progressiveCatalogue.hosting?.largePdfFallbacks || {}).length >= 1,
  Object.values(progressiveCatalogue.hosting?.largePdfFallbacks || {}).every((url) => String(url).startsWith("https://irsdl.github.io/webhacklist/")),
  buildSiteSource.includes('target === "cloudflare" && stat.size > assetLimit'),
  buildSiteSource.includes("fileCount > 20000"),
  buildSiteSource.includes('target === "github"') && buildSiteSource.includes("Object.keys(largeFallbacks)"),
  buildSiteSource.includes("GitHub Pages site-size limit exceeded"),
  buildSiteSource.includes("default-src 'none'; base-uri 'none'; form-action 'none'; object-src 'none'"),
  headersSource.includes("frame-ancestors 'self'"),
  headersSource.includes("Cross-Origin-Opener-Policy: same-origin"),
  headersSource.includes("Cross-Origin-Resource-Policy: same-origin"),
  headersSource.includes("Origin-Agent-Cluster: ?1"),
  headersSource.includes("Strict-Transport-Security: max-age=31536000"),
  headersSource.includes("fullscreen=(self)"),
  notFoundSource.includes("default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'; object-src 'none'"),
  headersSource.includes("/data/collections/*"),
  headersSource.includes("max-age=31536000, immutable")
];

// The submission route crosses two files that nothing else keeps in step: the
// app prefills GitHub's issue form by field id, and a renamed field there would
// drop the answer silently rather than fail. So the ids, the template filenames
// and the year options are checked against each other here.
const submissionFormSource = await readFile(path.join(root, ".github/ISSUE_TEMPLATE/01-submit-research.yml"), "utf8");
// config.yml is the chooser's own configuration, not one of the forms.
const issueTemplateFiles = new Set((await readdir(path.join(root, ".github/ISSUE_TEMPLATE"))).filter((name) => name.endsWith(".yml") && name !== "config.yml"));
const submissionFieldIds = [...submissionFormSource.matchAll(/^ {4}id:\s*([a-z0-9-]+)\s*$/gm)].map((match) => match[1]);
const submissionFormYears = [...submissionFormSource.matchAll(/^ {8}- "(\d{4})"$/gm)].map((match) => match[1]);
const appTemplateNames = [...appSource.matchAll(/"(\d\d-[a-z0-9-]+\.yml)"/g)].map((match) => match[1]);
const indexTemplateNames = [...indexSource.matchAll(/issues\/new\?template=([0-9a-z-]+\.yml)/g)].map((match) => match[1]);
const catalogueYearIds = progressiveCatalogue.years.map((record) => record.id);
const offeredYears = JSON.parse(clientEval(`YEAR_FILES = ${JSON.stringify(catalogueYearIds)}; JSON.stringify(submissionYears())`));
const prefilledIssueUrl = clientEval(`issueUrl("research", {
  title: "[Research] Example",
  "research-url": "https://example.test/post",
  year: "2019",
  "whats-new": "line one\\n\\nline two"
})`);
// Six fields at the per-field cap would make an address GitHub answers with an
// error page instead of a form, so the overflow has to be dropped whole.
const floodedIssueUrl = clientEval(`issueUrl("research", Object.fromEntries(
  ["title", "research-url", "research-title", "researchers", "whats-new", "prior-art"].map((field) => [field, "x".repeat(9000)])
))`);
const submissionMatching = JSON.parse(clientEval(`
  state.items = [{
    id: "2019-1", year: "2019", yearLabel: "2019", rank: 1, topic: "HTTP",
    title: "HTTP Desync Attacks: Request Smuggling Reborn",
    originalUrl: "https://portswigger.net/research/http-desync-attacks",
    links: [{ url: "https://portswigger.net/research/http-desync-attacks" }, { url: "https://youtu.be/example" }]
  }, {
    id: "2008-4", year: "2008", yearLabel: "2008", rank: null, topic: "Other",
    title: "A blog on query-string permalinks",
    originalUrl: "https://oldblog.test/?p=123",
    links: [{ url: "https://oldblog.test/?p=123" }]
  }];
  submissionIndexCache = null;
  const match = (url, title = "") => submissionMatches({ url: safeExternalUrl(url), title });
  const result = {
    exact: match("https://portswigger.net/research/http-desync-attacks").exact?.id || "",
    loose: match("http://www.portswigger.net/research/http-desync-attacks/").exact?.id || "",
    tracked: match("https://portswigger.net/research/http-desync-attacks?utm_source=newsletter&fbclid=x").exact?.id || "",
    replayed: match("https://web.archive.org/web/20200101/https://portswigger.net/research/http-desync-attacks").exact?.id || "",
    secondLink: match("https://youtu.be/example").exact?.id || "",
    unrelated: match("https://example.test/nothing-like-it").exact?.id || "",
    // The query IS the article on a blog of that era, so a different post on
    // the same host is a different record - not a duplicate of it.
    permalink: match("https://oldblog.test/?p=123").exact?.id || "",
    otherPermalink: match("https://oldblog.test/?p=456").exact?.id || "",
    similar: match("https://example.test/nothing-like-it", "Request smuggling reborn, revisited").similar.map((item) => item.id),
    unrelatedTitle: match("https://example.test/nothing-like-it", "Prototype pollution in the wild").similar.length
  };
  state.items = [];
  submissionIndexCache = null;
  JSON.stringify(result)
`));
const contributionChecks = [
  // Every route the page offers has a form behind it, and every form the app
  // names is a file that exists.
  issueTemplateFiles.size === 5,
  appTemplateNames.length === 5 && appTemplateNames.every((name) => issueTemplateFiles.has(name)),
  indexTemplateNames.length >= 5 && indexTemplateNames.every((name) => issueTemplateFiles.has(name)),
  (await exists(".github/ISSUE_TEMPLATE/config.yml")) && (await exists(".github/PULL_REQUEST_TEMPLATE.md")) && (await exists("CONTRIBUTING.md")),
  ["research-url", "research-title", "year", "researchers", "whats-new", "prior-art"].every((id) => submissionFieldIds.includes(id)),
  // A year the site can offer but the form cannot accept loses that answer.
  offeredYears.length >= 20 && offeredYears.every((year) => submissionFormYears.includes(year)),
  JSON.stringify(offeredYears.slice(0, 3)) === JSON.stringify([...offeredYears].sort((a, b) => Number(b) - Number(a)).slice(0, 3)),
  prefilledIssueUrl.startsWith("https://github.com/irsdl/webhacklist/issues/new?template=01-submit-research.yml"),
  prefilledIssueUrl.includes("research-url=https%3A%2F%2Fexample.test%2Fpost") && prefilledIssueUrl.includes("year=2019"),
  prefilledIssueUrl.includes("whats-new=line+one%0A%0Aline+two"),
  clientEval(`issueUrl("no-such-form")`) === "https://github.com/irsdl/webhacklist/issues/new/choose",
  floodedIssueUrl.length <= 6000 && floodedIssueUrl.includes("template=01-submit-research.yml"),
  // A submitted address is not a URL the page will follow, but it is still
  // validated before it is written into an outbound link.
  clientEval(`submissionIssueUrl({ url: safeExternalUrl("javascript:alert(1)"), title: "", year: "", researchers: "", whatsNew: "" })`) === "https://github.com/irsdl/webhacklist/issues/new?template=01-submit-research.yml",
  clientEval(`issueFieldText("a\\u202Eb\\u0007c")`) === "abc",
  clientEval(`issueFieldText("first\\n\\n\\n\\nsecond")`) === "first\n\nsecond",
  submissionMatching.exact === "2019-1",
  submissionMatching.loose === "2019-1",
  submissionMatching.tracked === "2019-1",
  submissionMatching.replayed === "2019-1",
  submissionMatching.secondLink === "2019-1",
  submissionMatching.unrelated === "",
  submissionMatching.permalink === "2008-4",
  submissionMatching.otherPermalink === "",
  JSON.stringify(submissionMatching.similar) === '["2019-1"]',
  submissionMatching.unrelatedTitle === 0,
  indexSource.includes('id="contribute-dialog"'),
  (indexSource.match(/data-contribute\b/g) || []).length === 3,
  indexSource.includes('id="contribute-issue"') && indexSource.includes('id="contribute-check"'),
  appSource.includes("function openSubmissionDialog"),
  appSource.includes("function submissionMatches"),
  appSource.includes('if (next === "submit")'),
  stylesSource.includes(".contribute-check.is-match") && stylesSource.includes(".contribute-check.is-clear"),
  stylesSource.includes(".support-action.is-contribute")
];

const joined = artifacts.filter((artifact) => artifact.record).length;
const preliminaryRecords = yearRecords.filter((record) => record.status === "preliminary");
const preliminaryArtifacts = artifacts.filter((artifact) => preliminaryRecords.some((record) => record.id === artifact.year));
console.log(`Artifact titles:     ${artifacts.length}`);
console.log(`Manifest matches:    ${joined}`);
console.log(`Markdown actions:    ${markdownCount}`);
console.log(`PDF actions:         ${pdfCount}`);
console.log(`Original actions:    ${artifacts.length}`);
console.log(`Annual result PDFs:  ${annualPdfFiles.length}`);
console.log(`Preliminary leads:   ${preliminaryArtifacts.length}`);
console.log(`Interface assets:     ${mockupFiles.length}`);
console.log(`Security checks:     ${securityChecks.filter(Boolean).length}/${securityChecks.length}`);
console.log(`Constellation UX:    ${constellationChecks.filter(Boolean).length}/${constellationChecks.length}`);
console.log(`Requested views:     ${experienceChecks.filter(Boolean).length}/${experienceChecks.length}`);
console.log(`Mobile/deployment:   ${deploymentChecks.filter(Boolean).length}/${deploymentChecks.length}`);
console.log(`Contribution route:  ${contributionChecks.filter(Boolean).length}/${contributionChecks.length}`);

if (artifacts.length < 1000) throw new Error("Expected at least 1,000 artifact titles.");
if (!preliminaryRecords.length || preliminaryRecords.some((record) => record.ranked !== false || !record.notice || !record.contentStart || !record.contentEnd)) throw new Error("Every preliminary collection must be unranked, bounded, and carry a visible notice.");
if (!preliminaryArtifacts.length) throw new Error("No preliminary artifacts were parsed.");
if (preliminaryArtifacts.some((artifact) => artifact.rank !== null)) throw new Error("Preliminary artifacts cannot carry Top 10 ranks.");
if (joined < 900) throw new Error("Too few year-list URLs matched the preservation manifest.");
if (missingLocalFiles.length) throw new Error(`Missing ${missingLocalFiles.length} referenced archive file(s):\n${missingLocalFiles.slice(0, 10).join("\n")}`);
if (missingAnnualPdfs.length) throw new Error(`Missing annual result PDFs:\n${missingAnnualPdfs.join("\n")}`);
if (missingMockupFiles.length) throw new Error(`Missing mockup files:\n${missingMockupFiles.join("\n")}`);
if (unsafeManifestPaths.length) throw new Error(`Unsafe archive path(s) in manifest:\n${unsafeManifestPaths.slice(0, 10).join("\n")}`);
if (securityChecks.some((passed) => !passed)) throw new Error(`Security checks failed. Unsafe target=_blank tags: ${unsafeBlankTargets.length}; unsafe rendered tags: ${unsafeRenderedTags.join(" ") || "none"}`);
if (constellationChecks.some((passed) => !passed)) throw new Error("Constellation interaction checks failed.");
if (experienceChecks.some((passed) => !passed)) throw new Error(`Requested experience checks failed. Views found: ${requestedViews.join(", ")}`);
if (deploymentChecks.some((passed) => !passed)) throw new Error("Mobile/full-screen/deployment checks failed.");
if (contributionChecks.some((passed) => !passed)) throw new Error(`Contribution route checks failed at index ${contributionChecks.findIndex((passed) => !passed)}.`);

console.log("Smoke test:          PASS");
