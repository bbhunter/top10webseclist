/* Web Hacking Techniques Index — dependency-free and powered by the real research archive. */

let YEAR_RECORDS = [];
let YEAR_FILES = [];
let ARCHIVE_CATALOGUE = null;
let LARGE_PDF_FALLBACKS = new Map();
const loadedCollections = new Set();
const collectionRequests = new Map();

// A path the manifest advertises through an old step record but the working
// archive does not hold. Empty is the healthy state: paths come from the
// archive's own rule (see archivePathsFor), not from a step record that a
// later rename or withdrawal left behind.
const KNOWN_MISSING_PATHS = new Set([]);
// Kinds the archive never prints a PDF for - `config.json -> pdf.skip_kinds`.
const NO_PDF_KINDS = new Set(["video"]);
// The archive's own name, never the name of the mode being viewed. The browser
// tab reads the same in every room; the mode names itself in the heading above
// the records, and in the masthead h1 the site names itself once.
const SITE_TITLE = "Web Hacking Techniques Index";
const SITE_DOCUMENT_TITLE = `${SITE_TITLE} — Research archive`;
const READ_STORAGE_KEY = "technique-vault-read-v1";
const FAVOURITE_STORAGE_KEY = "websec-favourites-v1";
const READING_THEME_STORAGE_KEY = "technique-vault-reading-theme-v1";
// Every archive mode can fill the screen. The four immersive views additionally
// get a focused full-screen layout in styles.css; the reading views (Museum,
// Library and the personal collection) simply gain the whole viewport.
const FULLSCREEN_VIEWS = new Set(["museum", "library", "signals", "constellation", "terminal", "evidence", "favourites"]);
// Which personal collection view 07 is showing. Favourites and read state are
// two independent browser-local lists over the same records.
const SAVED_MODES = ["favourites", "read", "all"];

function loadStoredKeys(storageKey) {
  try {
    const saved = JSON.parse(localStorage.getItem(storageKey) || "[]");
    const safeKeys = Array.isArray(saved)
      ? saved.filter((key) => typeof key === "string" && key.length > 0 && key.length <= 2048).slice(0, 5000)
      : [];
    return new Set(safeKeys);
  } catch {
    return new Set();
  }
}

function loadReadKeys() {
  return loadStoredKeys(READ_STORAGE_KEY);
}

function loadFavouriteKeys() {
  return loadStoredKeys(FAVOURITE_STORAGE_KEY);
}

function loadReadingTheme() {
  try {
    return localStorage.getItem(READING_THEME_STORAGE_KEY) === "light" ? "light" : "dark";
  } catch {
    return "dark";
  }
}

const VIEWS = {
  museum: {
    kicker: "Room 01 / exhibition mode",
    title: "Museum at Night",
    description: "Walk through twenty years of research as rooms, illuminated winners and recovered artifacts."
  },
  library: {
    kicker: "Stack 02 / reading mode",
    title: "Infinite Security Library",
    description: "Pull a title from the shelves, browse by subject and turn a very large collection into something tactile."
  },
  signals: {
    kicker: "Scope 03 / trend mode",
    title: "Signal Observatory",
    description: "Tune across twenty years of research, spot rising technique families and open the papers behind every change in frequency."
  },
  constellation: {
    kicker: "Field 04 / relationship mode",
    title: "Research Constellation",
    description: "Fly through individual papers as stars gathered around recurring technique families and follow unexpected neighbours in three dimensions."
  },
  terminal: {
    kicker: "Shell 05 / query mode",
    title: "The Hacker Terminal",
    description: "Query the archive through a recovered CRT shell, then open its records in the shared Markdown and PDF readers."
  },
  evidence: {
    kicker: "Case 06 / investigation mode",
    title: "The Investigation Board",
    description: "Open one corkboard case per year, rearrange its evidence and follow the red thread through the winning research."
  },
  favourites: {
    kicker: "Collection 07 / saved research",
    title: "Favourite Research",
    description: "Keep a durable shortlist across every archive view, then return to the papers that matter most."
  }
};

// View 07 is one surface over two browser-local lists. The copy follows the
// selected list so the page never claims a reading history is a shortlist.
const SAVED_VIEW_COPY = {
  favourites: VIEWS.favourites,
  read: {
    kicker: "Collection 07 / reading history",
    title: "Research You Have Read",
    description: "Every record you marked as read, across as many years as you want to compare at once."
  },
  all: {
    kicker: "Collection 07 / personal archive",
    title: "Saved And Read Research",
    description: "Your shortlist and your reading history together, filtered by any combination of years and topics."
  }
};

// Deep links into the two other collections. `favourites` stays the canonical
// view name so existing #favourites links keep working.
const VIEW_HASHES = {
  read: { view: "favourites", savedMode: "read" },
  saved: { view: "favourites", savedMode: "all" }
};

const TOPICS = [
  { name: "XSS", color: "#ff8e73", test: /\b(xss|cross[- ]site scripting|script injection|csp|css exfil|xs.leak|dom clobber)/i },
  { name: "HTTP", color: "#6ee7e7", test: /\b(http|request smuggling|desync|cache poison|cache deception|header|proxy|cdn|websocket|quic)/i },
  { name: "Identity", color: "#bda7ff", test: /\b(oauth|saml|authentication|authorization|account takeover|session|cookie|jwt|sso|passkey|permission)/i },
  { name: "Injection", color: "#f6c96b", test: /\b(sql|injection|ssti|template|xxe|deserialize|prototype pollution|parser differential|command execution)/i },
  { name: "Browser", color: "#82f5b2", test: /\b(browser|chrome|firefox|safari|edge|dom|iframe|same.origin|clickjack|extension|client.side)/i },
  { name: "Supply", color: "#ffb4d1", test: /\b(supply chain|dependency|package|npm|github action|repository|ci\/cd)/i },
  { name: "Server", color: "#80adff", test: /\b(ssrf|server|cloud|file upload|path traversal|rce|remote code|framework|java|php|\.net|node\.js)/i },
  { name: "Crypto", color: "#c7ee83", test: /\b(tls|ssl|crypto|certificate|padding oracle|entropy|encryption|hash|breach|crime|beast)/i },
  { name: "AI", color: "#ff9f7a", test: /\b(ai|llm|agentic|prompt injection|mcp|model context protocol|vllm|gptcache)\b/i },
  { name: "Other", color: "#93aaa2", test: /.*/ }
];

const state = {
  items: [],
  archiveTotal: 0,
  manifestCount: 0,
  view: "museum",
  year: "",
  query: "",
  starYear: "",
  starTopic: "all",
  starStatus: "all",
  signalYear: "",
  signalTopic: "all",
  signalStatus: "all",
  signalVisibleCount: 12,
  savedMode: "favourites",
  // Empty means "every year" / "every topic". Both filters are multi-select so
  // a shortlist can be read across several years at once.
  savedYears: new Set(),
  savedTopics: new Set(),
  terminalLines: [],
  terminalHistory: [],
  terminalHistoryIndex: 0,
  terminalCwd: "/",
  terminalPreviousCwd: "/",
  evidenceDense: false,
  motionReduced: false,
  readingTheme: loadReadingTheme(),
  readKeys: loadReadKeys(),
  favouriteKeys: loadFavouriteKeys(),
  readerItem: null,
  readerOriginal: false,
  pdfItem: null,
  pdfPath: "",
  pdfKind: "pdf",
  pdfVersion: "",
  pdfOriginal: false,
  pdfVerified: false,
  pdfViewMode: "page-width"
};

const $ = (selector, root = document) => root.querySelector(selector);
const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];
const h = (value = "") => String(value)
  .replaceAll("&", "&amp;")
  .replaceAll("<", "&lt;")
  .replaceAll(">", "&gt;")
  .replaceAll('"', "&quot;")
  .replaceAll("'", "&#039;");
// Markdown escapes are for the file, not for the reader: a title written
// `\[EN\] ...` in a list is read as `[EN] ...`.
const compact = (value = "") => String(value).replace(/\s+/g, " ").trim()
  .replace(/\\([\\`*_{}[\]()#+\-.!])/g, "$1");
const short = (value, length = 58) => value.length > length ? `${value.slice(0, length - 1)}…` : value;
const byRankThenTitle = (a, b) => (a.rank || 999) - (b.rank || 999) || a.title.localeCompare(b.title);
let constellationExperience = null;
let investigationResizeObserver = null;
let investigationCardInfo = new Map();
let pdfLoadTimer = null;
let pdfVerifyToken = 0;
let readerRequestToken = 0;
// Where the reader was in the result list when they opened a document from it.
let globalResultsScroll = 0;
let searchResumable = false;

function yearRecordFor(year) {
  return YEAR_RECORDS.find((record) => record.id === year) || { id: year, label: year, status: "final", ranked: true };
}

function yearLabel(year, short = false) {
  const record = yearRecordFor(year);
  return short && record.shortLabel ? record.shortLabel : record.label || record.id;
}

function isPreliminaryYear(year) {
  return yearRecordFor(year).status === "preliminary";
}

function preliminaryNotice(year) {
  const record = yearRecordFor(year);
  if (record.status !== "preliminary") return "";
  return `<aside class="preliminary-notice" role="note"><b>PRELIMINARY · SUBJECT TO CHANGE</b><span>${h(record.notice || "This collection is incomplete, unranked, and not a finalized Top 10.")}</span></aside>`;
}

function safeExternalUrl(value) {
  try {
    const url = new URL(String(value));
    if (!['http:', 'https:'].includes(url.protocol) || url.username || url.password) return "";
    return url.href;
  } catch {
    return "";
  }
}

// `inlineMarkdown` works on text after `h()` has escaped it. Decode exactly
// that one escaping layer before URL parsing, then escape the canonical URL
// again at the HTML sink. This prevents quote/entity tricks from manufacturing
// an attribute while keeping ordinary query strings intact.
function safeMarkdownUrl(value) {
  const decoded = String(value || "")
    .replaceAll("&quot;", '"')
    .replaceAll("&#039;", "'")
    .replaceAll("&lt;", "<")
    .replaceAll("&gt;", ">")
    .replaceAll("&amp;", "&");
  const safe = safeExternalUrl(decoded);
  return safe || "";
}

function safeArchivePath(value, kind) {
  if (typeof value !== "string" || !value || value.length > 500) return "";
  if (/[\\?#%\u0000-\u001f]/.test(value) || value.startsWith("/") || value.split("/").includes("..")) return "";
  const expected = kind === "md"
    ? /^archived-references\/md\/[a-z0-9-]+\/[a-z0-9._-]+\.md$/i
    : kind === "listingPdf"
      ? /^original-listings\/[0-9-]+-(?:top10|nominees-and-top10)\.pdf$/i
      : /^archived-references\/pdf\/[a-z0-9-]+\/[a-z0-9._-]+\.pdf$/i;
  return expected.test(value) ? value : "";
}

// A REDEPLOYED DOCUMENT NEEDS A NEW URL, or nobody sees it. Preserved documents
// are served `max-age=86400, stale-while-revalidate=604800`, which is right for
// files that almost never change - and means that when one DOES change, the edge
// keeps serving the old bytes for a day and revalidates lazily for a week. A
// reprint that replaced a text render with the publisher's own paper was invisible
// on the live site while the app around it had already updated, because the shell
// revalidates on every load and the documents do not.
//
// So the version travels in the URL, exactly as the collection shards already do.
// PER DOCUMENT rather than one token for the whole archive: the token is the
// moment that file was written, so adding one reference does not invalidate 1,500
// unchanged documents, and a 27 MiB PDF is re-fetched only when it is reprinted.
function versionToken(value) {
  const digits = String(value || "").replace(/\D/g, "");
  return digits ? digits.slice(0, 14) : "";
}

function archiveUrl(path, kind, version = "") {
  const safePath = safeArchivePath(path, kind);
  if (!safePath) return "";
  const pageDirectory = new URL(".", location.href);
  // In the repository the app lives at /website/ beside the archive. The
  // Pages workflow publishes website/* at the deployment root together with
  // those archive directories. Support both layouts without a domain-specific
  // base URL so custom domains and project Pages URLs behave identically.
  const archiveRoot = /\/website\/$/i.test(pageDirectory.pathname)
    ? new URL("../", pageDirectory)
    : pageDirectory;
  const url = new URL(safePath, archiveRoot);
  const token = versionToken(version);
  if (token) url.search = `v=${token}`;
  return url.href;
}

function documentShareUrl(item, format = "artifact") {
  const url = new URL(location.href);
  url.search = "";
  if (format === "reader" && item?.id) url.searchParams.set("reader", item.id);
  if (format === "pdf" && item?.id) url.searchParams.set("pdf", item.id);
  if (format === "results") {
    const year = /^original-listings\/([0-9-]+)-(?:top10|nominees-and-top10)\.pdf$/i.exec(state.pdfPath)?.[1];
    if (year) url.searchParams.set("results", year);
  }
  if (["reader", "pdf", "results"].includes(format)) url.searchParams.set("theme", state.readingTheme);
  const route = viewHash();
  url.hash = item?.id ? `${route}/${encodeURIComponent(item.id)}` : route;
  return url.href;
}

function syncDocumentUrl(item, format) {
  history.replaceState(history.state, "", documentShareUrl(item, format));
}

function clearDocumentUrl() {
  const url = new URL(location.href);
  ["reader", "pdf", "results", "theme"].forEach((key) => url.searchParams.delete(key));
  history.replaceState(history.state, "", url.href);
}

function fallbackCopy(value) {
  const input = document.createElement("textarea");
  input.value = value;
  input.readOnly = true;
  input.setAttribute("aria-hidden", "true");
  input.style.position = "fixed";
  input.style.opacity = "0";
  document.body.appendChild(input);
  input.select();
  const copied = document.execCommand?.("copy") === true;
  input.remove();
  return copied;
}

async function shareDocument(item, format = "artifact") {
  const shareUrl = documentShareUrl(item, format);
  const formatLabel = format === "reader" ? "Markdown reader" : format === "pdf" ? "PDF viewer" : format === "results" ? "results PDF" : "archive record";
  const title = item?.title || $("#pdf-title")?.textContent || "Web Hacking Techniques Index";
  if (typeof navigator.share === "function") {
    try {
      await navigator.share({ title, text: `Open this ${formatLabel} in the Web Hacking Techniques Index.`, url: shareUrl });
      toast("Share sheet opened");
      return;
    } catch (error) {
      if (error?.name === "AbortError") return;
    }
  }
  try {
    await navigator.clipboard.writeText(shareUrl);
    toast(`${formatLabel} link copied`);
  } catch {
    toast(fallbackCopy(shareUrl) ? `${formatLabel} link copied` : "Sharing is unavailable in this browser");
  }
}

// The publishing host, with a Wayback replay unwrapped to what it replays -
// otherwise every source cited as a capture reads as published by the archive.
function hostOf(value) {
  try {
    const replayed = /^https?:\/\/web\.archive\.org\/web\/[^/]+\/(https?:\/\/.+)$/i.exec(String(value));
    return new URL(replayed ? replayed[1] : value).hostname.replace(/^www\./, "");
  } catch {
    return "";
  }
}

// Who to credit in one line. The researcher leads and the publisher follows,
// because a name is what a reader recognises and a host is only where the file
// sat. Falls back to the publisher alone, which is every reference whose source
// declared no author.
function creditOf(item) {
  const names = (item.authors || []).join(", ");
  if (!names) return item.publisher || "";
  return item.publisher ? `${names} · ${item.publisher}` : names;
}

// The same credit for a slot too narrow to hold both. A card foot truncates at
// 25 characters, where a name and a domain together are cut off through the
// middle of the domain: the name alone is the part worth the space.
function briefCreditOf(item) {
  return (item.authors || []).join(", ") || item.publisher || "";
}

// The credit the shard carries. A cap keeps the payload bounded, but a cap that
// stops mid-list is the same failure this field exists to fix: the archive's
// longest byline is four names today and a conference paper carries more, so
// the eighth name is followed by the words that say there were others rather
// than by silence.
const CREDIT_LIMIT = 8;
function creditList(authors) {
  return authors.length > CREDIT_LIMIT
    ? [...authors.slice(0, CREDIT_LIMIT), "et al."]
    : [...authors];
}

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

function topicFor(title) {
  return TOPICS.find((topic) => topic.test.test(title)) || TOPICS.at(-1);
}

// Use the exact paths the archive manifest advertises. Inferring a directory
// from `cited_by[0]` breaks references cited in more than one collection: the
// citation list can be re-sorted while the preserved file correctly stays in
// its original collection. The strict path allowlist keeps manifest text from
// becoming an arbitrary client-side URL.
// The archive keeps a translation as a SECOND file beside the original, never as
// a section inside it (see the archive skill: `<slug>_translate.md`). This site
// is read in English, so where that English file exists it IS the document the
// reader opens, and the source's own words stay one action away. A translation
// only ever replaces the file it was made from: a reference whose Markdown was
// translated but whose PDF was not still offers its original PDF, unlabelled.
function archivePathsFor(record) {
  const empty = { mdPath: "", pdfPath: "", originalMdPath: "", originalPdfPath: "", translated: false };
  if (!record?.slug || !record?.grade || !record?.content_sha256) return empty;
  const noPdf = NO_PDF_KINDS.has(record.kind || "");
  const usable = (value, kind) => (value && !KNOWN_MISSING_PATHS.has(value) ? safeArchivePath(value, kind) : "");
  const sourceMd = usable(record.steps?.render?.file || "", "md");
  const sourcePdf = noPdf ? "" : usable(record.steps?.pdf?.file || "", "pdf");
  const englishMd = usable(record.steps?.render?.translation_file || "", "md");
  const englishPdf = noPdf ? "" : usable(record.steps?.["pdf-translation"]?.file || "", "pdf");
  // The moment each file was written, so the URL changes exactly when the file
  // does. `render` writes the Markdown and its translation together, so both
  // share its timestamp; the two PDFs are printed in separate passes.
  const renderedAt = record.steps?.render?.utc || "";
  const printedAt = record.steps?.pdf?.utc || "";
  const translatedAt = record.steps?.["pdf-translation"]?.utc || "";
  return {
    mdPath: englishMd || sourceMd,
    pdfPath: englishPdf || sourcePdf,
    mdVersion: renderedAt,
    pdfVersion: englishPdf ? translatedAt : printedAt,
    originalMdPath: englishMd ? sourceMd : "",
    originalPdfPath: englishPdf ? sourcePdf : "",
    originalPdfVersion: englishPdf ? printedAt : "",
    translated: Boolean(englishMd || englishPdf)
  };
}

function parseYearMarkdown(markdown, year, recordLookup, yearRecord = yearRecordFor(year)) {
  const preliminary = yearRecord.status === "preliminary";
  let section = preliminary ? "candidate" : "other";
  let position = 0;
  const items = [];
  // A label may hold ESCAPED brackets - three 2024 nominees are titled
  // `\[EN\] ...` and `\[Quick note\] ...`. A label pattern of `[^\]]+` stops at
  // the escaped `]`, finds no `(` after it, and the whole bullet then parses as
  // having no links at all, so those three researches were missing from the page.
  const LINK_RE = /\[((?:[^\]\\]|\\.)+)\]\((?:<(https?:\/\/[^>\s]+)>|(https?:\/\/[^)\s]+))\)/g;

  let inContentRange = !yearRecord.contentStart;
  for (const [lineIndex, line] of markdown.split(/\r?\n/).entries()) {
    if (yearRecord.contentStart && line.trim() === yearRecord.contentStart) {
      inContentRange = true;
      continue;
    }
    if (inContentRange && yearRecord.contentEnd && line.trim() === yearRecord.contentEnd) break;
    if (!inContentRange) continue;
    if (/^##\s+Top 10/i.test(line)) section = "winner";
    if (/^##\s+Other nominations/i.test(line)) section = "other";
    if (!/^\s*-\s/.test(line)) continue;

    let body = line.replace(/^\s*-\s*/, "");
    const rankMatch = body.match(/\*\*#(\d+)\*\*/);
    const rank = rankMatch ? Number(rankMatch[1]) : null;
    if (rankMatch) body = body.replace(rankMatch[0], "");

    // Trailing editorial note — **(...)** or (** ... **); its links are
    // references, not part of this research.
    let note = "";
    const noteMatch = body.match(/(?:\*\*\((?!#)([^)]*)\)\*\*|\(\*\*(.*?)\*\*\))\s*$/);
    if (noteMatch) {
      note = compact((noteMatch[1] ?? noteMatch[2] ?? "").replace(LINK_RE, "$1"));
      body = body.slice(0, noteMatch.index);
    }

    // One bullet = one research; every markdown link on it belongs to it
    // (talk video + slides + whitepaper, part II, ...).
    const links = [];
    let firstIndex = -1;
    for (const m of body.matchAll(LINK_RE)) {
      const url = safeExternalUrl(m[2] || m[3]);
      if (!url) continue;
      if (firstIndex === -1) firstIndex = m.index;
      const record = recordLookup.get(normalizeUrl(url));
      links.push({ label: compact(m[1]), url, record, ...archivePathsFor(record) });
    }
    if (!links.length) continue;

    const lead = compact(body.slice(0, firstIndex)).replace(/^[-* ]+|[-*: ]+$/g, "");
    const title = lead.length >= 4 ? lead : links[0].label;
    const originalUrl = links[0].url;
    const excluded = /excluded|held out/i.test(note) || /excluded|held out/i.test(body.slice(firstIndex));
    const lookupKey = normalizeUrl(originalUrl);
    const record = links[0].record || links.find((link) => link.record)?.record;
    const topic = topicFor(title);
    // the reader opens the first preserved copy across the research's links
    const documentLink = links.find((link) => link.mdPath) || links.find((link) => link.pdfPath) || links[0];
    // The PDF can come from a different link than the Markdown, so its
    // original-language counterpart has to be read off that same link - pairing
    // it with the Markdown's link would offer the wrong document.
    const pdfLink = links.find((link) => link.pdfPath) || documentLink;
    const mdPath = documentLink.mdPath || "";
    const pdfPath = pdfLink.pdfPath || "";
    const originalMdPath = documentLink.originalMdPath || "";
    const originalPdfPath = pdfLink.originalPdfPath || "";
    // Read off the SAME link as the path each one versions.
    const mdVersion = documentLink.mdVersion || "";
    const pdfVersion = pdfLink.pdfVersion || "";
    const originalPdfVersion = pdfLink.originalPdfVersion || "";

    items.push({
      id: `${year}-${position++}`,
      year,
      yearLabel: yearRecord.label || year,
      preliminary,
      provenance: yearRecord.provenance || "community-curated",
      line: lineIndex + 1,
      title,
      originalUrl,
      // An explicit allowlist: `record` is the whole manifest entry and must not
      // reach the shard. Translation keys are emitted only where they apply, so
      // the 72 translated references cost payload and the other 1,600 do not.
      links: links.map((link) => ({
        label: link.label,
        url: link.url,
        mdPath: link.mdPath,
        pdfPath: link.pdfPath,
        ...(link.translated
          ? { originalMdPath: link.originalMdPath, originalPdfPath: link.originalPdfPath, translated: true }
          : {})
      })),
      note,
      rank,
      section,
      excluded,
      topic: topic.name,
      topicColor: topic.color,
      // Whoever published the document the reader can OPEN. The citation's own
      // link is often a talk the archive cannot keep, and naming its video host
      // attributes the research to YouTube rather than to Black Hat or the
      // author's own site.
      // The page's own <title> is NOT a publisher: probing a dead or taken-over
      // source records the error page's title, so that fallback printed
      // "404 Not Found", "wrong number (404)" and a squatter's gambling-site
      // name as the publisher of 16 references. The host is always honest.
      publisher: documentLink.record?.publisher || hostOf(documentLink.url),
      // WHO DID THE RESEARCH, where the archive knows. The publisher above is a
      // host for most references, and a host credits a domain rather than a
      // person: whole runs of nominations read as the work of a parked domain
      // that outlived the blog on it. Read off the same link as the publisher,
      // because it is the copy the reader opens. Emitted only where known, for
      // the payload reason above: a reference that names nobody looks exactly as
      // it did, and falls back to its publisher everywhere.
      ...(documentLink.record?.authors?.length
        ? { authors: creditList(documentLink.record.authors) }
        : {}),
      kind: record?.kind || "link",
      language: record?.language || "",
      published: record?.published || "",
      grade: record?.grade || "",
      depth: record?.depth || "",
      health: record?.health?.status || "unknown",
      archiveStatus: mdPath && pdfPath ? "preserved" : mdPath || pdfPath ? "partial" : record?.health?.status === "ok" ? "live" : "missing",
      mdPath,
      pdfPath,
      ...(mdVersion ? { mdVersion } : {}),
      ...(pdfVersion ? { pdfVersion } : {}),
      // The Markdown hotlinks the publisher's images, because publishing 4,500
      // of them would double this repository. Where the archive holds its own
      // re-encoded copies they are printed into the PDF, so a picture the
      // reader cannot load has somewhere to send them. Emitted only where true,
      // for the same payload reason as the translation keys.
      ...(pdfLink.record?.steps?.images?.result === "stored" ? { figuresInPdf: true } : {}),
      ...(originalMdPath || originalPdfPath
        ? { originalMdPath, originalPdfPath, originalPdfVersion, translated: true }
        : {}),
      archived: Boolean(mdPath || pdfPath),
      citedBy: record?.cited_by || [`${year}.md:${lineIndex + 1}`],
      readKey: lookupKey,
      read: state.readKeys.has(lookupKey),
      favouriteKey: lookupKey,
      favourite: state.favouriteKeys.has(lookupKey)
    });
  }

  return items;
}

function collectionSummaryFor(year) {
  return YEAR_RECORDS.find((record) => record.id === year) || null;
}

function archiveFieldTotal(field) {
  return YEAR_RECORDS.reduce((sum, record) => sum + Number(record?.[field] || 0), 0);
}

function collectionYearForItem(id) {
  const value = String(id || "");
  return [...YEAR_FILES].sort((a, b) => b.length - a.length).find((year) => value === year || value.startsWith(`${year}-`)) || "";
}

function collectionUrl(year) {
  const record = collectionSummaryFor(year);
  if (!record || !/^\d{4}(?:-\d{2}|-ai)?$/.test(record.id)) return "";
  const version = encodeURIComponent(String(ARCHIVE_CATALOGUE?.version || ""));
  return `data/collections/${record.id}.json?v=${version}`;
}

function applyStoredState(item) {
  item.read = state.readKeys.has(item.readKey);
  item.favourite = state.favouriteKeys.has(item.favouriteKey);
  return item;
}

async function ensureCollection(year) {
  if (loadedCollections.has(year)) return itemsForYear(year);
  if (collectionRequests.has(year)) return collectionRequests.get(year);
  const record = collectionSummaryFor(year);
  const url = collectionUrl(year);
  if (!record || !url) throw new Error(`Unknown archive collection: ${year}`);

  const request = (async () => {
    const response = await fetch(url, { credentials: "same-origin", cache: "default" });
    if (!response.ok) throw new Error(`${year} collection returned ${response.status}`);
    const shard = await response.json();
    if (shard?.schema !== 1 || shard.version !== ARCHIVE_CATALOGUE.version || shard.collection?.id !== year || !Array.isArray(shard.items)) {
      throw new Error(`${year} collection does not match catalogue ${ARCHIVE_CATALOGUE.version}`);
    }
    if (shard.items.length !== Number(record.count) || shard.items.some((item) => item?.year !== year || typeof item?.id !== "string")) {
      throw new Error(`${year} collection failed its count or record validation`);
    }
    const items = shard.items.map(applyStoredState);
    state.items = state.items.filter((item) => item.year !== year).concat(items);
    loadedCollections.add(year);
    updateReadingProgress();
    updateFavouriteCount();
    return items;
  })();
  collectionRequests.set(year, request);
  try {
    return await request;
  } finally {
    collectionRequests.delete(year);
  }
}

async function ensureAllCollections() {
  await Promise.all(YEAR_FILES.map(ensureCollection));
  return state.items;
}

async function ensureItemLoaded(id) {
  const existing = state.items.find((item) => item.id === id);
  if (existing) return existing;
  const year = collectionYearForItem(id);
  if (!year) return null;
  await ensureCollection(year);
  return state.items.find((item) => item.id === id) || null;
}

function shouldPrefetchArchive() {
  const connection = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
  return !connection?.saveData && !/^(slow-)?2g$/.test(connection?.effectiveType || "");
}

function scheduleArchivePrefetch() {
  if (!shouldPrefetchArchive()) return;
  const queue = YEAR_FILES.filter((year) => !loadedCollections.has(year));
  const schedule = window.requestIdleCallback
    ? (callback) => window.requestIdleCallback(callback, { timeout: 2500 })
    : (callback) => setTimeout(callback, 800);
  const next = () => {
    const year = queue.shift();
    if (!year) return;
    ensureCollection(year).then(() => {
      if (state.query) updateGlobalSearch();
      if (state.view === "favourites" && !queue.length) renderFavourites();
    }).catch((error) => console.warn(`Background archive load failed for ${year}:`, error)).finally(() => schedule(next));
  };
  schedule(next);
}

async function loadArchive() {
  const bootStatus = $("#boot-status");
  try {
    bootStatus.textContent = "Reading the progressive archive catalogue…";
    const catalogueResponse = await fetch("data/catalogue.json", { credentials: "same-origin", cache: "no-cache" });
    if (!catalogueResponse.ok) throw new Error(`Archive catalogue returned ${catalogueResponse.status}`);
    const catalogue = await catalogueResponse.json();
    const catalogueYears = Array.isArray(catalogue?.years) ? catalogue.years : [];
    const validIds = catalogueYears.map((record) => record?.id).filter((id) => typeof id === "string" && /^\d{4}(?:-\d{2}|-ai)?$/.test(id));
    if (catalogue?.schema !== 1 || typeof catalogue.version !== "string" || !validIds.length || validIds.length !== catalogueYears.length || new Set(validIds).size !== validIds.length) {
      throw new Error("Archive catalogue is empty or invalid");
    }
    ARCHIVE_CATALOGUE = catalogue;
    YEAR_RECORDS = catalogueYears;
    YEAR_FILES = validIds;
    LARGE_PDF_FALLBACKS = new Map(Object.entries(catalogue?.hosting?.largePdfFallbacks || {}).flatMap(([path, value]) => {
      const safePath = safeArchivePath(path, "pdf");
      const safeUrl = safeExternalUrl(value);
      return safePath && safeUrl?.startsWith("https://") ? [[safePath, safeUrl]] : [];
    }));
    state.archiveTotal = Number(catalogue.total) || YEAR_RECORDS.reduce((sum, record) => sum + Number(record.count || 0), 0);
    state.manifestCount = Number(catalogue.manifestCount) || 0;
    const latestFinal = [...YEAR_RECORDS].reverse().find((record) => record.status === "final")?.id || YEAR_FILES.at(-1);
    state.year = latestFinal;
    state.starYear = latestFinal;
    state.signalYear = latestFinal;

    const requestedDocument = new URLSearchParams(location.search);
    const requestedTheme = requestedDocument.get("theme");
    if (["light", "dark"].includes(requestedTheme)) state.readingTheme = requestedTheme;
    const [hashView, sharedArtifact] = location.hash.replace("#", "").split("/");
    const requestedView = resolveViewHash(hashView);
    if (requestedView) {
      state.view = requestedView.view;
      if (requestedView.savedMode) state.savedMode = requestedView.savedMode;
    }
    const readerId = requestedDocument.get("reader");
    const pdfId = requestedDocument.get("pdf");
    const initialDocument = readerId || pdfId || sharedArtifact;
    const initialYear = collectionYearForItem(initialDocument) || latestFinal;

    bootStatus.textContent = `Opening ${yearLabel(initialYear)}…`;
    await ensureCollection(initialYear);
    if (state.view === "favourites") await ensureAllCollections();
    $("#sidebar-count").textContent = state.archiveTotal.toLocaleString();
    updateReadingProgress();
    updateFavouriteCount();

    wireShell();
    applyReadingTheme();
    render();
    $("#app-shell").hidden = false;
    if (sharedArtifact) requestAnimationFrame(() => openArtifact(sharedArtifact));
    if (readerId) {
      const readerItem = await ensureItemLoaded(readerId);
      if (readerItem?.mdPath) requestAnimationFrame(() => openReader(readerItem));
    }
    if (pdfId && !readerId) {
      const pdfItem = await ensureItemLoaded(pdfId);
      if (pdfItem?.pdfPath) requestAnimationFrame(() => openPdfViewer(pdfItem));
    }
    const resultsYear = requestedDocument.get("results");
    if (resultsYear && !readerId && !pdfId) {
      const resultsPath = annualPdfPath(resultsYear);
      if (resultsPath) requestAnimationFrame(() => openPdfViewer(null, {
        path: resultsPath,
        kind: "listingPdf",
        title: `${resultsYear} Top 10 results`,
        kicker: `Official archive listing / ${resultsYear}`
      }));
    }
    requestAnimationFrame(() => $("#boot-screen").classList.add("done"));
    setTimeout(() => $("#boot-screen").remove(), 700);
    scheduleArchivePrefetch();
  } catch (error) {
    console.error(error);
    bootStatus.innerHTML = `The archive could not be loaded. Serve the <strong>repository root</strong> with <code>python3 -m http.server 4173</code>, then open <code>/website/</code>.<br><br><small>${h(error.message)}</small>`;
  }
}

function wireShell() {
  $$(".nav-item").forEach((button) => button.addEventListener("click", () => setView(button.dataset.view)));

  $("#mobile-menu").addEventListener("click", () => {
    const open = document.body.classList.toggle("menu-open");
    $("#mobile-menu").setAttribute("aria-expanded", String(open));
  });

  $("#global-search").addEventListener("input", (event) => {
    state.query = event.target.value.trim();
    updateGlobalSearch();
    if (state.query) {
      const query = state.query;
      ensureAllCollections().then(() => {
        if (state.query === query) updateGlobalSearch();
      }).catch((error) => toast(`The full search index could not be loaded: ${error.message}`));
    }
  });
  $("#global-search").addEventListener("focus", updateGlobalSearch);
  $("#close-global-results").addEventListener("click", closeGlobalSearch);
  $("#global-results-list").addEventListener("click", (event) => {
    const target = event.target.closest("[data-artifact]");
    if (!target) return;
    hideGlobalResults();
    openArtifact(target.dataset.artifact);
  });

  $("#random-artifact").addEventListener("click", async () => {
    let offset = Math.floor(Math.random() * Math.max(1, state.archiveTotal));
    const record = YEAR_RECORDS.find((entry) => {
      offset -= Number(entry.count || 0);
      return offset < 0;
    }) || YEAR_RECORDS.at(-1);
    const items = await ensureCollection(record.id);
    const item = items[Math.floor(Math.random() * items.length)];
    if (item) openArtifact(item.id);
  });

  $("#motion-toggle").addEventListener("click", () => {
    state.motionReduced = !state.motionReduced;
    document.body.classList.toggle("reduce-motion", state.motionReduced);
    $("#motion-toggle").setAttribute("aria-pressed", String(state.motionReduced));
    toast(state.motionReduced ? "Ambient motion reduced" : "Ambient motion restored");
  });

  $("#view-fullscreen").addEventListener("click", toggleViewFullscreen);
  $("#site-fullscreen").addEventListener("click", toggleSiteFullscreen);
  document.addEventListener("fullscreenchange", syncFullscreenControls);
  document.addEventListener("webkitfullscreenchange", syncFullscreenControls);

  $("#browse-unread").addEventListener("click", async () => {
    await ensureAllCollections();
    const unread = state.items.filter((item) => !item.read);
    if (unread.length) openArtifact(unread[Math.floor(Math.random() * unread.length)].id);
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "/" && !/input|select|textarea/i.test(document.activeElement.tagName)) {
      event.preventDefault();
      $("#global-search").focus();
    }
    if (event.key === "Escape" && viewFullscreenFallbackActive()) {
      setViewFullscreenFallback(false);
      syncFullscreenControls();
    } else if (event.key === "Escape" && !$("#global-results").hidden) closeGlobalSearch();
  });

  window.addEventListener("hashchange", async () => {
    const [next, sharedArtifact] = location.hash.replace("#", "").split("/");
    const requested = resolveViewHash(next);
    if (requested) {
      const previousMode = state.savedMode;
      if (requested.savedMode) state.savedMode = requested.savedMode;
      else if (requested.view === "favourites") state.savedMode = "favourites";
      if (requested.view !== state.view) setView(requested.view, false);
      else if (state.savedMode !== previousMode) render();
    }
    if (sharedArtifact) {
      await ensureItemLoaded(sharedArtifact);
      requestAnimationFrame(() => openArtifact(sharedArtifact));
    }
  });

  $("#view-root").addEventListener("click", handleViewClick);
  $("#view-root").addEventListener("keydown", (event) => {
    const artifactTarget = event.target.closest("[data-artifact]");
    if (artifactTarget && (event.key === "Enter" || event.key === " ")) {
      event.preventDefault();
      openArtifact(artifactTarget.dataset.artifact);
    }
  });
  $("#view-root").addEventListener("pointerover", (event) => {
    const book = event.target.closest?.(".book");
    if (book) showShelfPlate(book);
    else hideShelfPlates();
  });
  $("#view-root").addEventListener("pointerleave", () => hideShelfPlates());
  $("#view-root").addEventListener("focusin", (event) => {
    const book = event.target.closest?.(".book");
    if (book) showShelfPlate(book);
    else hideShelfPlates();
  });
  $("#view-root").addEventListener("scroll", trackShelfScroll, true);
  $("#reader-scroll").addEventListener("scroll", (event) => {
    const element = event.currentTarget;
    const progress = element.scrollTop / Math.max(1, element.scrollHeight - element.clientHeight);
    $("#reader-progress-bar").style.width = `${clampNumber(progress * 100, 0, 100)}%`;
  });
  $("#reader-toc").addEventListener("click", (event) => {
    const target = event.target.closest("[data-reader-target]");
    if (target) $("#reader-content").querySelector(`#${CSS.escape(target.dataset.readerTarget)}`)?.scrollIntoView({ behavior: "smooth", block: "start" });
  });
  $("#reader-dialog").addEventListener("close", () => {
    readerRequestToken++;
    state.readerItem = null;
    if (!$("#pdf-dialog").open) clearDocumentUrl();
  });

  ["#artifact-dialog", "#reader-dialog", "#pdf-dialog"].forEach((id) => {
    $(id).addEventListener("close", () => requestAnimationFrame(restoreGlobalSearch));
  });

  $("#pdf-frame").addEventListener("load", () => {
    if (!state.pdfPath) return;
    const expectedUrl = archiveUrl(state.pdfPath, state.pdfKind, state.pdfVersion);
    if (!expectedUrl || !$("#pdf-frame").src.startsWith(expectedUrl)) return;
    clearTimeout(pdfLoadTimer);
    $("#pdf-loading").hidden = true;
    $("#pdf-fallback").hidden = true;
    $("#pdf-frame").hidden = false;
  });
  $("#pdf-dialog").addEventListener("close", clearPdfViewer);
  $("#pdf-links-toggle").addEventListener("click", () => togglePdfLinks());
  $("#pdf-links-close").addEventListener("click", () => togglePdfLinks(false));
  $("#pdf-fit-width").addEventListener("click", () => setPdfView("page-width"));
  $("#pdf-fit-page").addEventListener("click", () => setPdfView("page-fit"));
  $("#pdf-read-toggle").addEventListener("click", () => {
    if (state.pdfItem) setReadState(state.pdfItem);
  });
  $("#pdf-favourite-toggle").addEventListener("click", () => {
    if (state.pdfItem) setFavouriteState(state.pdfItem);
  });
  $("#pdf-open-markdown").addEventListener("click", () => {
    const item = state.pdfItem;
    if (!item?.mdPath) return;
    $("#pdf-dialog").close();
    openReader(item);
  });
  $("#pdf-theme-toggle").addEventListener("click", toggleReadingTheme);
  $("#pdf-share").addEventListener("click", () => shareDocument(state.pdfItem, state.pdfKind === "listingPdf" ? "results" : "pdf"));
}

function toggleInSet(set, value) {
  if (set.has(value)) set.delete(value);
  else set.add(value);
  return set;
}

async function handleViewClick(event) {
  const favouriteTarget = event.target.closest("[data-favourite]");
  if (favouriteTarget) {
    const item = state.items.find((entry) => entry.id === favouriteTarget.dataset.favourite);
    if (item) setFavouriteState(item);
    return;
  }

  const unreadTarget = event.target.closest("[data-saved-unread]");
  if (unreadTarget) {
    const item = state.items.find((entry) => entry.id === unreadTarget.dataset.savedUnread);
    if (item) setReadState(item, false);
    return;
  }

  const artifactTarget = event.target.closest("[data-artifact]");
  if (artifactTarget) {
    if (artifactTarget.dataset.dragged === "true") {
      artifactTarget.dataset.dragged = "";
      return;
    }
    openArtifact(artifactTarget.dataset.artifact);
    return;
  }

  const yearTarget = event.target.closest("[data-year]");
  if (yearTarget) {
    const year = yearTarget.dataset.year;
    await ensureCollection(year);
    if (state.view === "constellation") state.starYear = year;
    else state.year = year;
    render();
    return;
  }

  const topicTarget = event.target.closest("[data-topic-filter]");
  if (topicTarget) {
    state.starTopic = topicTarget.dataset.topicFilter;
    render();
    return;
  }

  const starStatusTarget = event.target.closest("[data-star-status]");
  if (starStatusTarget) {
    state.starStatus = starStatusTarget.dataset.starStatus;
    render();
    return;
  }

  const signalTopicTarget = event.target.closest("[data-signal-topic]");
  if (signalTopicTarget) {
    const topic = signalTopicTarget.dataset.signalTopic;
    if (topic === "all" || TOPICS.some((entry) => entry.name === topic)) state.signalTopic = topic;
    state.signalStatus = "all";
    state.signalVisibleCount = 12;
    render();
    return;
  }

  const signalYearTarget = event.target.closest("[data-signal-year]");
  if (signalYearTarget && YEAR_FILES.includes(signalYearTarget.dataset.signalYear)) {
    await ensureCollection(signalYearTarget.dataset.signalYear);
    state.signalYear = signalYearTarget.dataset.signalYear;
    state.signalStatus = "all";
    state.signalVisibleCount = 12;
    render();
    return;
  }

  const signalStatusTarget = event.target.closest("[data-signal-status]");
  if (signalStatusTarget && ["all", "top10", "nominee"].includes(signalStatusTarget.dataset.signalStatus)) {
    state.signalStatus = signalStatusTarget.dataset.signalStatus;
    state.signalVisibleCount = 12;
    render();
    return;
  }

  if (event.target.closest("[data-signal-more]")) {
    state.signalVisibleCount += 12;
    render();
    return;
  }

  const savedModeTarget = event.target.closest("[data-saved-mode]");
  if (savedModeTarget) {
    setSavedMode(savedModeTarget.dataset.savedMode);
    return;
  }

  const savedYearTarget = event.target.closest("[data-saved-year]");
  if (savedYearTarget) {
    const year = savedYearTarget.dataset.savedYear;
    if (year === "all") state.savedYears.clear();
    else if (YEAR_FILES.includes(year)) toggleInSet(state.savedYears, year);
    render();
    return;
  }

  const savedTopicTarget = event.target.closest("[data-saved-topic]");
  if (savedTopicTarget) {
    const topic = savedTopicTarget.dataset.savedTopic;
    if (topic === "all") state.savedTopics.clear();
    else if (TOPICS.some((entry) => entry.name === topic)) toggleInSet(state.savedTopics, topic);
    render();
    return;
  }

  if (event.target.closest("[data-saved-clear]")) {
    state.savedYears.clear();
    state.savedTopics.clear();
    render();
    return;
  }

}

// Route names are looked up with hasOwn: a plain `VIEWS[name]` also answers for
// every inherited Object.prototype key, so `#__proto__` or `#constructor` would
// pass the guard and then break rendering.
function isViewName(value) {
  return typeof value === "string" && Object.hasOwn(VIEWS, value);
}

function resolveViewHash(value) {
  const name = String(value || "");
  if (isViewName(name)) return { view: name };
  if (Object.hasOwn(VIEW_HASHES, name)) return { ...VIEW_HASHES[name] };
  return null;
}

function viewHash(view = state.view) {
  if (view !== "favourites") return view;
  return state.savedMode === "read" ? "read" : state.savedMode === "all" ? "saved" : "favourites";
}

function viewCopy(view = state.view) {
  if (view === "favourites") {
    return Object.hasOwn(SAVED_VIEW_COPY, state.savedMode) ? SAVED_VIEW_COPY[state.savedMode] : SAVED_VIEW_COPY.favourites;
  }
  return isViewName(view) ? VIEWS[view] : VIEWS.museum;
}

function setSavedMode(mode) {
  if (!SAVED_MODES.includes(mode) || mode === state.savedMode) return;
  state.savedMode = mode;
  history.replaceState(history.state, "", `#${viewHash("favourites")}`);
  render();
}

async function setView(view, updateHash = true) {
  if (!isViewName(view)) return;
  if (constellationExperience) {
    constellationExperience.destroy();
    constellationExperience = null;
  }
  destroyInvestigationLayout();
  state.view = view;
  document.body.classList.remove("menu-open");
  $("#mobile-menu").setAttribute("aria-expanded", "false");
  if (updateHash) history.pushState(null, "", `#${viewHash(view)}`);
  render();
  if (view === "favourites" && loadedCollections.size !== YEAR_FILES.length) {
    await ensureAllCollections();
    if (state.view === view) renderFavourites();
  }
}

function fullscreenElement() {
  return document.fullscreenElement || document.webkitFullscreenElement || null;
}

function fullscreenAvailable(target = document.documentElement) {
  return Boolean(target && (target.requestFullscreen || target.webkitRequestFullscreen));
}

function viewFullscreenFallbackActive() {
  return $("#main-content")?.classList.contains("view-fullscreen-fallback") || false;
}

function setViewFullscreenFallback(active) {
  const target = $("#main-content");
  target?.classList.toggle("view-fullscreen-fallback", Boolean(active));
  document.body.classList.toggle("view-fullscreen-fallback-open", Boolean(active));
}

function updateFullscreenButton(button, active, title) {
  if (!button) return;
  button.setAttribute("aria-pressed", String(active));
  button.innerHTML = active
    ? '<span aria-hidden="true">×</span> Exit full screen'
    : '<span aria-hidden="true">⛶</span> Full screen';
  button.title = active ? "Exit full screen" : title;
}

function syncFullscreenControls() {
  const current = fullscreenElement();
  const active = Boolean(current);
  const siteButton = $("#site-fullscreen");
  siteButton.hidden = !fullscreenAvailable(document.documentElement);
  updateFullscreenButton(siteButton, active, "Fill the screen with the complete website");

  const viewButton = $("#view-fullscreen");
  const supportedView = FULLSCREEN_VIEWS.has(state.view);
  // Focus mode is a safe CSS fallback when a browser exposes no Fullscreen API
  // (or refuses it because of browser UI policy). Every real archive view keeps
  // the control, including the Museum and Library reading views.
  viewButton.hidden = !supportedView;
  updateFullscreenButton(viewButton, active || viewFullscreenFallbackActive(), "Fill the screen with this archive mode");
}

async function requestFullscreen(target) {
  if (target?.requestFullscreen) await target.requestFullscreen({ navigationUI: "hide" });
  else if (target?.webkitRequestFullscreen) await target.webkitRequestFullscreen();
}

async function exitFullscreen() {
  const exit = document.exitFullscreen || document.webkitExitFullscreen;
  if (exit) await exit.call(document);
}

async function toggleSiteFullscreen() {
  try {
    if (viewFullscreenFallbackActive()) setViewFullscreenFallback(false);
    if (fullscreenElement()) await exitFullscreen();
    else await requestFullscreen(document.documentElement);
  } catch (error) {
    toast(`Full screen is unavailable: ${error.message}`);
  }
  syncFullscreenControls();
}

async function toggleViewFullscreen() {
  const target = $("#main-content");
  if (viewFullscreenFallbackActive()) {
    setViewFullscreenFallback(false);
    syncFullscreenControls();
    return;
  }
  try {
    if (fullscreenElement()) await exitFullscreen();
    else if (FULLSCREEN_VIEWS.has(state.view) && fullscreenAvailable(target)) await requestFullscreen(target);
    else if (FULLSCREEN_VIEWS.has(state.view)) setViewFullscreenFallback(true);
  } catch (error) {
    // A rejected native request still gets a full-window, scrollable mode. It
    // does not claim access to browser chrome; it only keeps the archive usable.
    setViewFullscreenFallback(true);
    toast("Browser full screen was unavailable; using full-window focus mode");
  }
  syncFullscreenControls();
}

function applyReadingTheme() {
  const light = state.readingTheme === "light";
  [$("#reader-dialog"), $("#pdf-dialog")].filter(Boolean).forEach((dialog) => {
    dialog.dataset.readingTheme = state.readingTheme;
  });
  [$("#reader-theme-toggle"), $("#pdf-theme-toggle")].filter(Boolean).forEach((button) => {
    button.classList.toggle("is-light", light);
    button.textContent = light ? "☾ Dark" : "☀ Light";
    button.setAttribute("aria-label", `Switch to ${light ? "dark" : "light"} reading theme`);
    button.title = button.id === "pdf-theme-toggle"
      ? "Changes the viewer controls and surround; PDF page colours remain original"
      : `Switch to ${light ? "dark" : "light"} reading theme`;
  });
}

function toggleReadingTheme() {
  state.readingTheme = state.readingTheme === "light" ? "dark" : "light";
  try { localStorage.setItem(READING_THEME_STORAGE_KEY, state.readingTheme); }
  catch { toast("Reading theme could not be saved in this browser"); }
  applyReadingTheme();
  if ($("#reader-dialog").open && state.readerItem) syncDocumentUrl(state.readerItem, "reader");
  else if ($("#pdf-dialog").open) syncDocumentUrl(state.pdfItem, state.pdfKind === "listingPdf" ? "results" : "pdf");
  toast(`${state.readingTheme === "light" ? "Light" : "Dark"} reading theme`);
}

function render() {
  const copy = viewCopy();
  $("#view-kicker").textContent = copy.kicker;
  $("#view-mode").textContent = copy.title;
  $("#view-description").textContent = copy.description;
  document.title = SITE_DOCUMENT_TITLE;
  $$(".nav-item").forEach((button) => {
    const active = button.dataset.view === state.view;
    button.classList.toggle("active", active);
    if (active) button.setAttribute("aria-current", "page");
    else button.removeAttribute("aria-current");
  });

  const renderers = {
    museum: renderMuseum,
    library: renderLibrary,
    signals: renderSignals,
    constellation: renderConstellation,
    terminal: renderTerminal,
    evidence: renderEvidence,
    favourites: renderFavourites
  };
  (Object.hasOwn(renderers, state.view) ? renderers[state.view] : renderMuseum)();
  syncFullscreenControls();
}

function updateGlobalSearch() {
  const panel = $("#global-results");
  const results = state.query ? queryItems(state.items, state.query) : [];
  if (!state.query) {
    panel.hidden = true;
    return;
  }
  const complete = loadedCollections.size === YEAR_FILES.length;
  $("#global-results-label").textContent = complete
    ? `${results.length.toLocaleString()} result${results.length === 1 ? "" : "s"} for “${state.query}”`
    : `${results.length.toLocaleString()} result${results.length === 1 ? "" : "s"} so far · loading ${YEAR_FILES.length - loadedCollections.size} collection(s)…`;
  // YEAR, TITLE, RESEARCHER. The name sits under the title rather than beside
  // the publisher, because the two are not the same fact and the narrow layout
  // drops the trailing column entirely: fusing them meant a phone showed the
  // one credit line the archive has and then hid it.
  $("#global-results-list").innerHTML = results.length
    ? results.slice(0, 40).map((item) => {
        const names = (item.authors || []).join(", ");
        return `
        <button type="button" data-artifact="${h(item.id)}">
          <span><b>${h(item.yearLabel || item.year)}</b>${item.favourite ? "★ favourite" : item.rank ? `#${item.rank}` : item.preliminary ? "preliminary" : "nominee"}</span>
          <div><strong>${h(item.title)}</strong>${names ? `<em>${h(names)}</em>` : ""}</div>
          <small>${h(item.publisher || item.topic)}</small>
        </button>`;
      }).join("") + (results.length > 40 ? `<p>Showing the first 40 results. Add another word to narrow the index.</p>` : "")
    : `<p>No archive records matched those words. A word can name its field —
       <b>author:</b>, <b>publisher:</b>, <b>title:</b>, <b>year:</b> or <b>topic:</b>.</p>`;
  panel.hidden = false;
}

function closeGlobalSearch() {
  state.query = "";
  searchResumable = false;
  $("#global-search").value = "";
  $("#global-results").hidden = true;
}

// Opening a record from a search is not the end of the search. The list is put
// away rather than thrown away, so closing the document returns the reader to
// the results they came from - same words, same place in the list - instead of
// an empty box they have to type into again.
function hideGlobalResults() {
  const panel = $("#global-results");
  if (panel.hidden) return;
  globalResultsScroll = $("#global-results-list").scrollTop;
  searchResumable = Boolean(state.query);
  panel.hidden = true;
}

function documentDialogOpen() {
  return ["#artifact-dialog", "#reader-dialog", "#pdf-dialog"].some((id) => $(id).open);
}

// Called a frame after a document dialog closes, because moving between the
// record, the reader and the PDF viewer closes one dialog before opening the
// next - and mid-move is not a closed document.
function restoreGlobalSearch() {
  if (!searchResumable || !state.query || documentDialogOpen()) return;
  searchResumable = false;
  updateGlobalSearch();
  $("#global-results-list").scrollTop = globalResultsScroll;
}

function setMetric(count, label) {
  $("#view-count").textContent = Number(count).toLocaleString();
  $("#view-count-label").textContent = label;
}

function itemsForYear(year) {
  return state.items.filter((item) => item.year === year);
}

// A word may name the PART OF THE RECORD it is asking about. Free text searches
// everything and cannot say which field it meant, so "kettle" answers with the
// research of a person and any title that happens to use the word. Naming the
// field is how a reader asks the question the byline made possible - who wrote
// this - rather than a question that merely tends to find them.
const SEARCH_FIELDS = {
  author: (item) => (item.authors || []).join(" "),
  publisher: (item) => item.publisher || "",
  title: (item) => item.title || "",
  year: (item) => String(item.yearLabel || item.year || ""),
  topic: (item) => item.topic || "",
};

// "author:" while it is still being typed is not a request for nothing, so a
// qualifier with no word yet is dropped rather than matched against "".
function parseQuery(query) {
  return query.toLowerCase().split(/\s+/).filter(Boolean).map((word) => {
    const mark = word.indexOf(":");
    const field = mark > 0 ? word.slice(0, mark) : "";
    return SEARCH_FIELDS[field]
      ? { pick: SEARCH_FIELDS[field], word: word.slice(mark + 1) }
      : { pick: null, word };
  }).filter((term) => term.word);
}

function queryItems(items, query = state.query) {
  if (!query) return items;
  const terms = parseQuery(query);
  if (!terms.length) return items;
  return items.filter((item) => {
    // Searching a research archive by researcher is the obvious question, and
    // until the author reached the shard the only way to ask it was to know
    // which domain they blogged on twenty years ago.
    const haystack = `${item.title} ${creditOf(item)} ${item.topic} ${item.year} ${item.kind}`.toLowerCase();
    return terms.every((term) => (term.pick
      ? term.pick(item).toLowerCase().includes(term.word)
      : haystack.includes(term.word)));
  });
}

function setReadState(item, nextState = !item.read) {
  if (!item) return;
  if (nextState) state.readKeys.add(item.readKey);
  else state.readKeys.delete(item.readKey);
  state.items.forEach((entry) => {
    if (entry.readKey === item.readKey) entry.read = nextState;
  });
  try { localStorage.setItem(READ_STORAGE_KEY, JSON.stringify([...state.readKeys])); }
  catch { toast("Read status could not be saved in this browser"); }
  state.items.filter((entry) => entry.readKey === item.readKey).forEach((entry) => {
    $$(`[data-artifact="${CSS.escape(entry.id)}"]`).forEach((element) => {
      element.classList.toggle("is-read", nextState);
      if (element.classList.contains("artifact-card")) {
        element.querySelector(".card-read")?.remove();
        if (nextState) element.insertAdjacentHTML("beforeend", `<span class="card-read">✓ read</span>`);
      }
    });
  });
  constellationExperience?.refreshReadState?.();
  syncReadButtons(item);
  updateReadingProgress();
  if (state.view === "favourites") renderFavourites();
  toast(nextState ? "Marked as read" : "Marked as unread");
}

function setFavouriteState(item, nextState = !item.favourite) {
  if (!item) return;
  if (nextState) state.favouriteKeys.add(item.favouriteKey);
  else state.favouriteKeys.delete(item.favouriteKey);
  const related = state.items.filter((entry) => entry.favouriteKey === item.favouriteKey);
  related.forEach((entry) => { entry.favourite = nextState; });
  try { localStorage.setItem(FAVOURITE_STORAGE_KEY, JSON.stringify([...state.favouriteKeys])); }
  catch { toast("Favourite status could not be saved in this browser"); }
  related.forEach((entry) => {
    $$(`[data-artifact="${CSS.escape(entry.id)}"]`).forEach((element) => {
      element.classList.toggle("is-favourite", nextState);
      if (element.classList.contains("artifact-card")) {
        element.querySelector(".card-favourite")?.remove();
        if (nextState) element.insertAdjacentHTML("beforeend", `<span class="card-favourite" aria-label="Favourite">★</span>`);
      }
      if (element.classList.contains("investigation-card")) {
        element.querySelector(".evidence-favourite")?.remove();
        if (nextState) element.insertAdjacentHTML("beforeend", `<b class="evidence-favourite">★ SAVED</b>`);
      }
    });
  });
  constellationExperience?.refreshFavouriteState?.();
  syncFavouriteButtons(item);
  updateFavouriteCount();
  toast(nextState ? "Added to favourites" : "Removed from favourites");
  if (state.view === "favourites") renderFavourites();
}

function favouriteItems() {
  return state.items.filter((item) => item.favourite);
}

function readItems() {
  return state.items.filter((item) => item.read);
}

// The records view 07 lists for the selected personal collection.
function savedItems(mode = state.savedMode) {
  if (mode === "read") return readItems();
  if (mode === "all") return state.items.filter((item) => item.favourite || item.read);
  return favouriteItems();
}

// An empty year or topic selection means "all of them", so several years can be
// combined into one shortlist instead of paging through them one at a time.
function savedFilteredItems(items = savedItems()) {
  return items.filter((item) =>
    (!state.savedYears.size || state.savedYears.has(item.year))
    && (!state.savedTopics.size || state.savedTopics.has(item.topic))
  ).sort((a, b) => b.year.localeCompare(a.year) || byRankThenTitle(a, b));
}

function updateFavouriteCount() {
  const count = loadedCollections.size === YEAR_FILES.length
    ? favouriteItems().length
    : Math.min(state.archiveTotal || state.favouriteKeys.size, state.favouriteKeys.size);
  const label = $("#favourite-count");
  if (label) label.textContent = count.toLocaleString();
}

function updateReadingProgress() {
  const total = state.archiveTotal || state.items.length;
  const read = loadedCollections.size === YEAR_FILES.length
    ? state.items.filter((item) => item.read).length
    : Math.min(total, state.readKeys.size);
  const progress = total ? read / total * 100 : 0;
  const label = $("#reading-progress-label");
  const bar = $("#reading-progress-bar");
  const button = $("#browse-unread");
  const navCount = $("#read-count");
  if (navCount) navCount.textContent = read.toLocaleString();
  if (label) label.textContent = `${read.toLocaleString()} / ${total.toLocaleString()}`;
  if (bar) bar.style.width = `${clampNumber(progress, 0, 100)}%`;
  if (button) {
    button.disabled = Boolean(total && read === total);
    button.textContent = total && read === total ? "Archive reading complete ✓" : "Resume with an unread record →";
  }
}

function syncReadButtons(item) {
  const current = state.readKeys.has(item.readKey);
  [$("#artifact-read-toggle"), $("#reader-read-toggle"), $("#pdf-read-toggle")].filter(Boolean).forEach((button) => {
    button.setAttribute("aria-pressed", String(current));
    button.textContent = current ? "✓ Read" : "○ Mark as read";
  });
}

function syncFavouriteButtons(item) {
  const current = state.favouriteKeys.has(item.favouriteKey);
  [$("#artifact-favourite-toggle"), $("#reader-favourite-toggle"), $("#pdf-favourite-toggle")].filter(Boolean).forEach((button) => {
    button.setAttribute("aria-pressed", String(current));
    button.textContent = current ? "★ Favourite" : "☆ Add favourite";
  });
}

function archiveLabel(item) {
  return item.archiveStatus === "preserved" ? "MD + PDF" : item.archiveStatus === "partial" ? "Partial copy" : item.archiveStatus === "live" ? "Original live" : "Link only";
}

function statusMarkup(item) {
  const className = item.archiveStatus === "preserved" ? "" : item.archiveStatus;
  return `<span><i class="status-dot ${h(className)}"></i>${h(archiveLabel(item))}</span>`;
}

function artifactCard(item, compactCard = false) {
  const rank = item.rank ? `<span class="rank-token">#${item.rank}</span>` : item.preliminary ? `<span class="preliminary-token">PRELIMINARY</span>` : `<span>${h(item.kind)}</span>`;
  return `
    <article class="artifact-card topic-${h(item.topic)} ${compactCard ? "compact-card" : ""} ${item.read ? "is-read" : ""} ${item.favourite ? "is-favourite" : ""}" data-artifact="${h(item.id)}" tabindex="0" role="button" aria-label="Open ${h(item.title)}${item.favourite ? ", favourite" : ""}">
      <div class="card-top"><span>${h(item.yearLabel || item.year)} / ${h(item.topic)}</span>${rank}</div>
      <h3>${h(item.title)}</h3>
      <div class="card-foot"><span>${h(short(briefCreditOf(item) || "Unknown publisher", 25))}</span>${statusMarkup(item)}</div>
      ${item.favourite ? `<span class="card-favourite" aria-label="Favourite">★</span>` : ""}
      ${item.read ? `<span class="card-read">✓ read</span>` : ""}
    </article>`;
}

function yearPills(selected) {
  return YEAR_RECORDS.map((record) => `<button class="year-pill ${record.id === selected ? "active" : ""} ${record.status === "preliminary" ? "preliminary" : ""}" data-year="${h(record.id)}" aria-pressed="${record.id === selected}" title="${h(record.status === "preliminary" ? "Preliminary, unranked, and subject to change" : `Finalized ${record.label} archive`)}"><span>${h(record.label)}</span>${record.status === "preliminary" ? `<small>PRELIM</small>` : ""}</button>`).join("");
}

// A card's colour is its research topic and nothing else — the same topic named
// in the card's own header. Listing only the topics the room holds keeps the key
// short and makes it describe the cards actually in front of the reader.
function topicKey(items) {
  const present = TOPICS
    .map((topic) => ({ ...topic, count: items.filter((item) => item.topic === topic.name).length }))
    .filter((topic) => topic.count);
  if (!present.length) return "";
  return `
    <div class="topic-key" role="group" aria-label="What the card colours mean">
      <p>Card colour = research topic</p>
      <ul>${present.map((topic) => `<li style="--topic-color:${h(topic.color)}"><i aria-hidden="true"></i>${h(topic.name)} <b>${topic.count}</b></li>`).join("")}</ul>
    </div>`;
}

function renderMuseum() {
  const items = itemsForYear(state.year);
  const preliminary = isPreliminaryYear(state.year);
  const winners = items.filter((item) => item.section === "winner").sort(byRankThenTitle);
  const nominees = items.filter((item) => item.section !== "winner");
  setMetric(items.length, preliminary ? `preliminary leads · ${yearLabel(state.year)}` : `artifacts in room ${yearLabel(state.year)}`);
  $("#view-root").innerHTML = `
    <section class="museum-map">
      <div class="museum-years" aria-label="Museum rooms">${yearPills(state.year)}</div>
      ${preliminaryNotice(state.year)}
      <div class="room-marquee">
        <p class="eyebrow">${preliminary ? "Research snapshot" : "Gallery room"}</p>
        <div class="room-number">${h(yearLabel(state.year))}</div>
        <p>${preliminary ? `${items.length} ${h(yearRecordFor(state.year).provenance || "preliminary")} leads · no ranking · subject to change` : `${winners.length} winning exhibits · ${nominees.length} nominated works`} · ${items.filter((item) => item.archived).length} preserved locally</p>
      </div>
      ${topicKey(items)}

      ${preliminary ? "" : `<div class="section-head"><div><p class="eyebrow">The central gallery</p><h2>Top 10 illuminated exhibits</h2></div><p>Selected by community vote and panel</p></div>
      <div class="winner-plinths">${winners.map((item) => artifactCard(item)).join("") || empty("No ranked exhibits recorded for this room.")}</div>`}

      <div class="section-head"><div><p class="eyebrow">${preliminary ? "Open review" : "The long gallery"}</p><h2>${preliminary ? "Preliminary research leads" : "Every other nomination"}</h2></div><p>${nominees.length} ${preliminary ? "changeable leads" : "artifacts on the wall"}</p></div>
      <div class="nominee-wall">${nominees.map((item) => artifactCard(item, true)).join("") || empty(preliminary ? "No preliminary leads recorded." : "No other nominations recorded.")}</div>
    </section>`;
}

function renderLibrary() {
  platedBook = null;
  const items = itemsForYear(state.year);
  const preliminary = isPreliminaryYear(state.year);
  const groups = TOPICS.map((topic) => ({ ...topic, items: items.filter((item) => item.topic === topic.name) })).filter((group) => group.items.length);
  setMetric(items.length, `${preliminary ? "preliminary volumes" : "volumes shelved"} for ${yearLabel(state.year)}`);

  $("#view-root").innerHTML = `
    ${preliminaryNotice(state.year)}
    <div class="library-desk">
      <section class="librarian-note">
        <p class="eyebrow">Curator's desk / shelf ${h(yearLabel(state.year))}</p>
        <h2>Browse by title, not by filename.</h2>
        <p>Each spine is one real technique. Pull it from the shelf to choose the preserved Markdown, printable PDF or original source.</p>
      </section>
      <aside class="checkout-card">
        <p class="eyebrow" style="color:#655f48">Reading room card</p>
        <p><strong>${items.length}</strong> volumes<br><strong>${groups.length}</strong> subject shelves<br><strong>${items.filter((item) => item.archived).length}</strong> locally preserved</p>
      </aside>
    </div>
    <div class="control-strip" aria-label="Select library year">${yearPills(state.year)}</div>
    <section class="library-hall">
      ${groups.map((group) => `
        <div class="shelf-section">
          <div class="shelf-label"><span>${h(group.name)} studies</span><span>${group.items.length} volumes</span></div>
          <div class="book-shelf">
            ${group.items.map((item, index) => `<button class="book ${item.read ? "is-read" : ""} ${item.favourite ? "is-favourite" : ""}" data-artifact="${h(item.id)}" aria-label="Open ${h(item.title)}${item.read ? ", read" : ""}${item.favourite ? ", favourite" : ""}" style="--book-height:${125 + ((index * 19) % 48)}px;--book-color:${h(group.color)}">${h(short(item.title, 48))}<b>${h(yearLabel(item.year, true))}</b></button>`).join("")}
          </div>
          <div class="shelf-plate" aria-hidden="true"><i class="shelf-plate-notch"></i><b class="shelf-plate-title"></b><span class="shelf-plate-meta"></span></div>
        </div>`).join("")}
    </section>`;
}

// A spine read vertically is slow, so hovering or focusing one drops a label into
// the shelf-edge holder directly beneath it — horizontal, full title, never clipped.
let platedBook = null;

function positionShelfPlate(plate, shelf, book) {
  const shelfBox = shelf.getBoundingClientRect();
  const bookBox = book.getBoundingClientRect();
  const centre = bookBox.left - shelfBox.left + bookBox.width / 2;
  const width = plate.offsetWidth;
  const left = Math.max(0, Math.min(centre - width / 2, shelfBox.width - width));
  plate.style.setProperty("--plate-x", `${Math.round(left)}px`);
  plate.style.setProperty("--notch-x", `${Math.round(Math.min(Math.max(centre - left, 14), Math.max(width - 14, 14)))}px`);
}

function showShelfPlate(book) {
  const shelf = book.closest(".book-shelf");
  const plate = shelf?.parentElement?.querySelector(".shelf-plate");
  const item = plate && state.items.find((entry) => entry.id === book.dataset.artifact);
  if (!item) return;
  hideShelfPlates(plate);
  plate.querySelector(".shelf-plate-title").textContent = item.title;
  const standing = item.rank ? `#${item.rank}` : item.preliminary ? "PRELIMINARY" : item.kind;
  plate.querySelector(".shelf-plate-meta").textContent = [
    standing,
    item.publisher || "Unknown publisher",
    `${item.yearLabel || item.year} · ${item.topic}`,
    archiveLabel(item)
  ].filter(Boolean).join("  ·  ");
  plate.classList.add("is-open");
  positionShelfPlate(plate, shelf, book);
  platedBook = book;
}

function hideShelfPlates(except = null) {
  if (!platedBook) return;
  $$(".shelf-plate.is-open").forEach((plate) => {
    if (plate !== except) plate.classList.remove("is-open");
  });
  if (!except) platedBook = null;
}

function trackShelfScroll(event) {
  const shelf = event.target;
  if (!shelf.classList?.contains("book-shelf")) return;
  const plate = shelf.parentElement?.querySelector(".shelf-plate.is-open");
  if (!plate || !platedBook || !shelf.contains(platedBook)) return;
  positionShelfPlate(plate, shelf, platedBook);
}

const SAVED_MODE_COPY = {
  favourites: {
    label: "★ Favourites",
    noun: "favourite",
    lead: "Your research shortlist",
    heading: "Build a shortlist from any archive view",
    help: `Favourites stay in this browser. Open any record elsewhere and use <b>☆ Add favourite</b>; the terminal also supports <code>fav &lt;id&gt;</code>.`,
    blank: "Nothing saved yet. Open a research record in Museum, Library, Signals, Constellation, Terminal, or Investigation Board to add it here."
  },
  read: {
    label: "✓ Read",
    noun: "read",
    lead: "Your reading history",
    heading: "Mark records as read to build a history",
    help: `Read state stays in this browser. Open any record and use <b>○ Mark as read</b> in the record, Markdown reader or PDF viewer.`,
    blank: "Nothing marked as read yet. Open a research record and use ○ Mark as read to track what you have been through."
  },
  all: {
    label: "Both",
    noun: "saved or read",
    lead: "Your personal archive",
    heading: "Save or read a record to collect it here",
    help: `Both lists stay in this browser. A record appears here once it is a favourite, marked as read, or both.`,
    blank: "Nothing collected yet. Add a favourite or mark a record as read from any archive view."
  }
};

function renderFavourites() {
  if (!SAVED_MODES.includes(state.savedMode)) state.savedMode = "favourites";
  const copy = SAVED_MODE_COPY[state.savedMode];
  const counts = {
    favourites: favouriteItems().length,
    read: readItems().length,
    all: savedItems("all").length
  };
  const all = savedItems();
  // Drop selections that no longer describe anything the registry still knows,
  // so a retired year or renamed topic cannot leave the view permanently empty.
  [...state.savedYears].forEach((year) => { if (!YEAR_FILES.includes(year)) state.savedYears.delete(year); });
  [...state.savedTopics].forEach((topic) => { if (!TOPICS.some((entry) => entry.name === topic)) state.savedTopics.delete(topic); });
  const filtered = savedFilteredItems(all);
  // Offer every year/topic this collection holds, plus any still-selected one it
  // no longer holds, so a selection left over from the other list stays visible
  // and clickable instead of silently emptying the grid.
  const yearRecords = YEAR_RECORDS.filter((record) => state.savedYears.has(record.id) || all.some((item) => item.year === record.id));
  const topicRecords = TOPICS.filter((topic) => state.savedTopics.has(topic.name) || all.some((item) => item.topic === topic.name));
  const filtering = Boolean(state.savedYears.size || state.savedTopics.size);
  const selectedYearCount = state.savedYears.size;
  setMetric(all.length, `${copy.noun} record${all.length === 1 ? "" : "s"} saved in this browser`);
  $("#view-root").innerHTML = `
    <section class="favourites-view">
      <header class="favourites-summary">
        <div><p class="eyebrow">${h(copy.lead)}</p><h2>${all.length ? `${all.length.toLocaleString()} ${h(copy.noun)} record${all.length === 1 ? "" : "s"}` : h(copy.heading)}</h2><p>${copy.help}</p></div>
        <span aria-hidden="true">${state.savedMode === "read" ? "✓" : "★"}</span>
      </header>
      <div class="saved-modes" role="group" aria-label="Choose a personal collection">
        ${SAVED_MODES.map((mode) => `<button type="button" class="${state.savedMode === mode ? "active" : ""}" data-saved-mode="${mode}" aria-pressed="${state.savedMode === mode}">${h(SAVED_MODE_COPY[mode].label)} <b>${counts[mode].toLocaleString()}</b></button>`).join("")}
      </div>
      ${all.length ? `<div class="favourite-filters">
        <div role="group" aria-label="Filter by one or more years"><span>Years</span><button type="button" class="${selectedYearCount ? "" : "active"}" data-saved-year="all" aria-pressed="${!selectedYearCount}">All years <b>${all.length}</b></button>${yearRecords.map((record) => {
          const active = state.savedYears.has(record.id);
          const count = all.filter((item) => item.year === record.id).length;
          return `<button type="button" class="${active ? "active" : ""}" data-saved-year="${h(record.id)}" aria-pressed="${active}">${h(record.shortLabel || record.label || record.id)} <b>${count}</b></button>`;
        }).join("")}</div>
        <div role="group" aria-label="Filter by one or more topics"><span>Topics</span><button type="button" class="${state.savedTopics.size ? "" : "active"}" data-saved-topic="all" aria-pressed="${!state.savedTopics.size}">All topics</button>${topicRecords.map((topic) => {
          const active = state.savedTopics.has(topic.name);
          const count = all.filter((item) => item.topic === topic.name).length;
          return `<button type="button" class="${active ? "active" : ""}" data-saved-topic="${h(topic.name)}" aria-pressed="${active}" style="--topic-color:${h(topic.color)}">${h(topic.name)} <b>${count}</b></button>`;
        }).join("")}</div>
        <p class="saved-filter-note">${filtering
          ? `Showing <b>${filtered.length.toLocaleString()}</b> of ${all.length.toLocaleString()} · ${selectedYearCount ? `${selectedYearCount} year${selectedYearCount === 1 ? "" : "s"}` : "all years"}${state.savedTopics.size ? ` · ${state.savedTopics.size} topic${state.savedTopics.size === 1 ? "" : "s"}` : ""} <button type="button" class="saved-clear" data-saved-clear>Clear filters</button>`
          : "Select several years or topics to combine them."}</p>
      </div>` : ""}
      <div class="favourite-grid mode-${h(state.savedMode)}">
        ${filtered.map((item) => `<div class="favourite-entry">${artifactCard(item)}<div class="saved-actions"><span class="saved-flags">${item.favourite ? "★" : ""}${item.read ? "✓" : ""}</span>${item.favourite ? `<button class="remove-favourite" type="button" data-favourite="${h(item.id)}" aria-label="Remove ${h(item.title)} from favourites">★ Remove</button>` : ""}${item.read ? `<button class="remove-favourite" type="button" data-saved-unread="${h(item.id)}" aria-label="Mark ${h(item.title)} as unread">✓ Unread</button>` : ""}</div></div>`).join("")
          || empty(all.length ? "No records match those filters." : copy.blank)}
      </div>
    </section>`;
}

function terminalWelcome() {
  const preliminaryCount = YEAR_RECORDS.filter((record) => record.status === "preliminary").length;
  return [
    `<pre class="terminal-banner" aria-label="The Hacker Terminal">╔══════════════════════════════════╗\n║  THE HACKER TERMINAL // ARCHIVE  ║\n╚══════════════════════════════════╝</pre>`,
    `<p class="term-dim">web-hacking-techniques-index v2.6 · read-only mount · ${YEAR_FILES.length} volumes detected${preliminaryCount ? ` · ${preliminaryCount} preliminary` : ""}</p>`,
    `<p><span class="term-bright">${state.archiveTotal.toLocaleString()}</span> documents indexed · <span class="term-gold">${archiveFieldTotal("markdown").toLocaleString()} md</span> · <span class="term-gold">${archiveFieldTotal("pdf").toLocaleString()} pdf</span></p>`,
    `<p>Type <button data-term-command="help">help</button> for commands, or try <button data-term-command="grep request smuggling">grep request smuggling</button>.</p>`
  ];
}

function renderTerminal() {
  setMetric(state.archiveTotal, "records available to query");
  if (!state.terminalLines.length) state.terminalLines = terminalWelcome();
  const mdCount = archiveFieldTotal("markdown");
  const pdfCount = archiveFieldTotal("pdf");
  $("#view-root").innerHTML = `
    <section class="hacker-terminal" aria-label="Interactive Hacker Terminal">
      <header class="hacker-terminal-head">
        <strong>THE HACKER TERMINAL</strong><span>·</span>
        <nav aria-label="List an archive year">${YEAR_FILES.map((year) => `<button data-term-command="ls /${h(year)}">${h(yearLabel(year, true))}</button>`).join("")}</nav>
      </header>
      <div class="terminal-output" id="terminal-output" role="log" aria-live="polite">${state.terminalLines.join("")}</div>
      <form class="terminal-input" id="terminal-form">
        <label for="terminal-command">guest@top10:${h(terminalPromptPath())}$</label>
        <input id="terminal-command" maxlength="500" autocomplete="off" autocapitalize="off" spellcheck="false" aria-label="Terminal command; type help for commands" autofocus>
        <i aria-hidden="true">▊</i>
      </form>
      <footer class="hacker-terminal-foot">
        <span>concept: <b>the hacker terminal</b></span><span>${state.archiveTotal.toLocaleString()} docs</span><span>md ${Math.round(mdCount / Math.max(1, state.archiveTotal) * 100)}%</span><span>pdf ${Math.round(pdfCount / Math.max(1, state.archiveTotal) * 100)}%</span><span>↑/↓ history · Tab completes</span>
      </footer>
    </section>`;

  $("#terminal-form").addEventListener("submit", (event) => {
    event.preventDefault();
    const input = $("#terminal-command");
    runTerminalCommand(input.value);
  });
  $$("[data-term-command]", $("#view-root")).forEach((button) => button.addEventListener("click", () => runTerminalCommand(button.dataset.termCommand)));
  $$('[data-terminal-md]', $("#view-root")).forEach((button) => button.addEventListener("click", () => {
    const item = state.items.find((entry) => entry.id === button.dataset.terminalMd);
    if (item?.mdPath) openReader(item);
  }));
  $$('[data-terminal-pdf]', $("#view-root")).forEach((button) => button.addEventListener("click", () => {
    const item = state.items.find((entry) => entry.id === button.dataset.terminalPdf);
    if (item?.pdfPath) openPdfViewer(item);
  }));
  $$('[data-terminal-web]', $("#view-root")).forEach((button) => button.addEventListener("click", () => {
    const item = state.items.find((entry) => entry.id === button.dataset.terminalWeb);
    const url = safeExternalUrl(item?.originalUrl);
    if (url) window.open(url, "_blank", "noopener,noreferrer");
  }));
  const input = $("#terminal-command");
  input.addEventListener("keydown", (event) => {
    if (event.key === "ArrowUp" || event.key === "ArrowDown") {
      if (!state.terminalHistory.length) return;
      event.preventDefault();
      const delta = event.key === "ArrowUp" ? -1 : 1;
      state.terminalHistoryIndex = clampNumber(state.terminalHistoryIndex + delta, 0, state.terminalHistory.length);
      input.value = state.terminalHistory[state.terminalHistoryIndex] || "";
    } else if (event.key === "Tab") {
      event.preventDefault();
      input.value = terminalCompletion(input.value);
    }
  });
  requestAnimationFrame(() => {
    const output = $("#terminal-output");
    output.scrollTop = output.scrollHeight;
    input.focus({ preventScroll: true });
  });
}

function terminalPromptPath() {
  return state.terminalCwd === "/" ? "~" : state.terminalCwd;
}

function resolveTerminalPath(rawPath = ".") {
  let value = String(rawPath || ".").trim();
  if (value === "-") return state.terminalPreviousCwd;
  if (value === "~") value = "/";
  else if (value.startsWith("~/")) value = `/${value.slice(2)}`;
  const segments = value.startsWith("/") ? [] : state.terminalCwd.split("/").filter(Boolean);
  value.split("/").forEach((part) => {
    if (!part || part === ".") return;
    if (part === "..") segments.pop();
    else segments.push(part);
  });
  if (segments.length === 1 && ["2016", "2017"].includes(segments[0])) segments[0] = "2016-17";
  return `/${segments.join("/")}`;
}

function terminalPathExists(path) {
  const name = path.split("/").filter(Boolean)[0] || "";
  return path === "/" || path === "/favourites" || path === "/favorites" || (path === `/${name}` && YEAR_FILES.includes(name));
}

function terminalItemsAtPath(path = state.terminalCwd) {
  const name = path.split("/").filter(Boolean)[0] || "";
  if (path === "/") return state.items;
  if (["/favourites", "/favorites"].includes(path)) return favouriteItems();
  return YEAR_FILES.includes(name) ? itemsForYear(name) : [];
}

function terminalTokens(command) {
  const tokens = [];
  let token = "";
  let quote = "";
  for (const character of command) {
    if (quote) {
      if (character === quote) quote = "";
      else token += character;
    } else if (character === "'" || character === '"') quote = character;
    else if (/\s/.test(character)) {
      if (token) { tokens.push(token); token = ""; }
    } else token += character;
  }
  if (quote) return { tokens: [], error: "unterminated quote" };
  if (token) tokens.push(token);
  return { tokens, error: "" };
}

// JavaScript regexes cannot be interrupted once running. Keep grep inside a
// deliberately conservative, FINITE subset: no assertions/backreferences,
// no quantified groups and no unbounded *, + or {n,} repetition. A small
// number of bounded atom repeats remains useful for CVEs and similar records.
function regexSafetyIssue(source) {
  let inClass = false;
  let previous = "start";
  let quantifiers = 0;
  let rangedRepeats = 0;
  let alternatives = 0;
  const groups = [];

  for (let index = 0; index < source.length; index++) {
    const character = source[index];
    if (character === "\\") {
      const escaped = source[index + 1] || "";
      if (!inClass && (/[1-9]/.test(escaped) || (escaped === "k" && source[index + 2] === "<"))) {
        return "backreferences are disabled for ReDoS safety";
      }
      index++;
      previous = "atom";
      continue;
    }
    if (inClass) {
      if (character === "]") { inClass = false; previous = "atom"; }
      continue;
    }
    if (character === "[") { inClass = true; continue; }
    if (character === "(") {
      if (source[index + 1] === "?") {
        if (source[index + 2] !== ":") return "lookarounds and special groups are disabled for ReDoS safety";
        index += 2;
      }
      groups.push(index);
      previous = "group-open";
      continue;
    }
    if (character === ")") {
      groups.pop();
      previous = "group";
      continue;
    }
    if (character === "|") {
      if (++alternatives > 12) return "pattern has too many alternatives for the safe grep engine";
      previous = "alternative";
      continue;
    }
    if (character === "*" || character === "+") return "unbounded repetition is disabled for ReDoS safety; use a bounded repeat such as {0,32}";

    let repeat = null;
    if (character === "{") repeat = /^\{(\d+)(?:,(\d*))?\}/.exec(source.slice(index));
    if (character === "?" || repeat) {
      if (previous === "group") return "quantified groups are disabled for ReDoS safety";
      if (previous === "quantifier") return "stacked quantifiers are disabled for ReDoS safety";
      if (++quantifiers > 4) return "pattern is too complex for the safe grep engine";
      if (repeat) {
        const lower = Number(repeat[1]);
        const upper = repeat[2] === undefined ? lower : repeat[2] === "" ? Infinity : Number(repeat[2]);
        if (!Number.isFinite(upper)) return "unbounded repetition is disabled for ReDoS safety";
        if (lower > 64 || upper > 64 || upper < lower) return "repeat bounds must be ordered and no greater than 64";
        if (repeat[2] !== undefined && ++rangedRepeats > 1) return "multiple ranged repeats are disabled for ReDoS safety";
        index += repeat[0].length - 1;
      }
      previous = "quantifier";
      continue;
    }
    previous = "atom";
  }
  return "";
}

function compileSafeGrep(expression, insensitive = true) {
  let source = String(expression || "");
  let flags = insensitive ? "i" : "";
  const slashPattern = source.match(/^\/(.*)\/([a-z]*)$/s);
  if (slashPattern) {
    source = slashPattern[1];
    flags = slashPattern[2];
  }
  if (!source) return { error: "empty regular expression" };
  if (source.length > 160) return { error: "pattern exceeds the 160-character safety limit" };
  if (/[^im]/.test(flags) || new Set(flags).size !== flags.length) return { error: "only the i and m regex flags are supported" };
  const safetyIssue = regexSafetyIssue(source);
  if (safetyIssue) return { error: safetyIssue };
  try { return { regex: new RegExp(source, flags), source, flags }; }
  catch (error) { return { error: `invalid regular expression: ${error.message}` }; }
}

function terminalRows(items, limit = 60) {
  if (!items.length) return `<p class="term-error">No records matched.</p>`;
  return items.slice(0, limit).map((item, index) => `<div class="term-row ${item.favourite ? "is-favourite" : ""}"><span>${String(index + 1).padStart(3, "0")}</span><b>${item.favourite ? `★${item.rank ? `#${item.rank}` : ""}` : item.rank ? `#${item.rank}` : item.preliminary ? "PRE" : "·"}</b><button data-term-command="open ${h(item.id)}">${h(item.title)}</button><small>${h(yearLabel(item.year, true))}${item.archived ? "" : " · not archived"}</small></div>`).join("") + (items.length > limit ? `<p class="term-dim">… ${items.length - limit} more result(s). Refine the query to narrow them.</p>` : "");
}

function terminalRootListing() {
  return `<p class="term-bright">total ${YEAR_FILES.length + 1} directories, ${state.archiveTotal} documents</p>${YEAR_FILES.map((year) => {
    const summary = collectionSummaryFor(year);
    const count = Number(summary?.count || 0);
    const archived = Number(summary?.archived || 0);
    const bars = Math.round(archived / Math.max(1, count) * 10);
    return `<div class="term-volume"><span>drwx</span><button data-term-command="ls /${h(year)}">${h(yearLabel(year, true))}/</button><small>${String(count).padStart(3, " ")} docs${isPreliminaryYear(year) ? " · PRELIM" : ""}</small><i>[${"█".repeat(bars)}${"░".repeat(10 - bars)}] ${Math.round(archived / Math.max(1, count) * 100)}% archived</i></div>`;
  }).join("")}<div class="term-volume"><span>drwx</span><button data-term-command="ls /favourites">favourites/</button><small>${String(state.favouriteKeys.size).padStart(3, " ")} saved</small><i>browser-local shortlist</i></div>`;
}

function terminalGrep(args) {
  let insensitive = true;
  let inverted = false;
  while (args[0]?.startsWith("-") && !args[0].startsWith("/")) {
    const option = args.shift();
    if (option === "-i") insensitive = true;
    else if (option === "-v") inverted = true;
    else return `<p class="term-error">grep: unsupported option '${h(option)}' (supported: -i, -v)</p>`;
  }
  let scopePath = state.terminalCwd;
  if (args.length > 1) {
    const possiblePath = resolveTerminalPath(args.at(-1));
    if (terminalPathExists(possiblePath)) {
      scopePath = possiblePath;
      args.pop();
    }
  }
  const expression = args.join(" ");
  const compiled = compileSafeGrep(expression, insensitive);
  if (compiled.error) return `<p class="term-error">grep: ${h(compiled.error)}. Try a shorter expression such as <button data-term-command="grep /xss|csrf/i">grep /xss|csrf/i</button>.</p>`;
  const matches = terminalItemsAtPath(scopePath).filter((item) => {
    const haystack = `${item.title}\n${creditOf(item)}\n${item.topic}\n${item.year}\n${item.kind}\n${item.originalUrl}`.slice(0, 2048);
    compiled.regex.lastIndex = 0;
    const matched = compiled.regex.test(haystack);
    return inverted ? !matched : matched;
  });
  const shownPattern = `/${compiled.source}/${compiled.flags}`;
  return `<p class="term-bright">${matches.length} match${matches.length === 1 ? "" : "es"} for ${h(shownPattern)} in ${h(scopePath)}</p>${terminalRows(matches, 60)}`;
}

async function runTerminalCommand(rawCommand) {
  const command = String(rawCommand || "").trim().slice(0, 500);
  if (!command) return;
  const parsed = terminalTokens(command);
  const [verbRaw = "", ...args] = parsed.tokens;
  const verb = verbRaw.toUpperCase();
  const promptPath = terminalPromptPath();
  state.terminalHistory.push(command);
  state.terminalHistory = state.terminalHistory.slice(-80);
  state.terminalHistoryIndex = state.terminalHistory.length;
  state.terminalLines.push(`<p class="term-echo"><span>guest@top10:${h(promptPath)}$</span> ${h(command)}</p>`);

  try {
    if (!parsed.error) {
      const recordCommands = ["OPEN", "CAT", "SHOW", "FAV", "FAVOURITE", "FAVORITE", "UNFAV", "UNFAVOURITE", "UNFAVORITE"];
      if (recordCommands.includes(verb) && args[0]) await ensureItemLoaded(args[0]);
      if (["STATS", "FAVOURITES", "FAVORITES", "FAVS"].includes(verb)) await ensureAllCollections();
      if (["LS", "DIR", "LIST", "WINNERS"].includes(verb)) {
        const path = resolveTerminalPath(args[0] || (verb === "WINNERS" ? state.terminalCwd : "."));
        if (["/favourites", "/favorites"].includes(path)) await ensureAllCollections();
        else if (YEAR_FILES.includes(path.slice(1))) await ensureCollection(path.slice(1));
      }
      if (["FIND", "GREP", "SEARCH"].includes(verb)) {
        const possiblePath = args.length > 1 ? resolveTerminalPath(args.at(-1)) : "";
        const path = terminalPathExists(possiblePath) ? possiblePath : state.terminalCwd;
        if (["/", "/favourites", "/favorites"].includes(path)) await ensureAllCollections();
        else if (YEAR_FILES.includes(path.slice(1))) await ensureCollection(path.slice(1));
      }
      if (["RANDOM", "LUCKY"].includes(verb)) {
        if (["/", "/favourites", "/favorites"].includes(state.terminalCwd)) await ensureAllCollections();
        else if (YEAR_FILES.includes(state.terminalCwd.slice(1))) await ensureCollection(state.terminalCwd.slice(1));
      }
    }
  } catch (error) {
    state.terminalLines.push(`<p class="term-error">archive load failed: ${h(error.message)}</p>`);
    renderTerminal();
    return;
  }

  if (parsed.error) {
    state.terminalLines.push(`<p class="term-error">sh: ${h(parsed.error)}</p>`);
  } else if (["HELP", "MAN", "?"].includes(verb)) {
    state.terminalLines.push(`<p class="term-bright">Available commands</p><div class="terminal-man"><button data-term-command="pwd">pwd</button><span>print the current archive directory</span><button data-term-command="cd /2024">cd &lt;year|..|/&gt;</button><span>move between root, year and favourites directories</span><button data-term-command="ls">ls [path]</button><span>list the current or named directory</span><button data-term-command="grep /xss|csrf/i">grep [-i|-v] &lt;regex&gt; [path]</button><span>safe regex search in the current or named directory</span><button data-term-command="open ${h(state.items[0]?.id || "")}">open &lt;id&gt; [--md|--pdf|--web]</button><span>show or open a preserved record</span><button data-term-command="fav ${h(state.items[0]?.id || "")}">fav / unfav &lt;id&gt;</button><span>add or remove a browser-local favourite</span><button data-term-command="favorites">favorites</button><span>list the favourites directory</span><button data-term-command="history">history</button><span>show recent commands</span><button data-term-command="random">random</button><span>surface one document from the current directory</span><button data-term-command="clear">clear</button><span>wipe the screen</span></div><p class="term-dim">Aliases: dir/list, cat/show, search/find, favourite/favorite, lucky, cls · regexes are bounded and risky constructs are rejected before execution.</p>`);
  } else if (verb === "PWD") {
    state.terminalLines.push(`<p>${h(state.terminalCwd)}</p>`);
  } else if (verb === "CD") {
    const destination = resolveTerminalPath(args[0] || "/");
    if (!terminalPathExists(destination)) state.terminalLines.push(`<p class="term-error">cd: ${h(args[0] || "")}: no such directory</p>`);
    else {
      state.terminalPreviousCwd = state.terminalCwd;
      state.terminalCwd = destination === "/favorites" ? "/favourites" : destination;
    }
  } else if (verb === "STATS") {
    const preserved = state.items.filter((item) => item.archived).length;
    state.terminalLines.push(`<p>${state.archiveTotal} techniques / ${YEAR_FILES.length} year files / ${preserved} locally preserved / ${favouriteItems().length} favourites / ${new Set(state.items.map((item) => item.publisher)).size} publishers</p>`);
  } else if (["LS", "DIR", "LIST"].includes(verb)) {
    const requestedPath = resolveTerminalPath(args[0] || ".");
    if (!terminalPathExists(requestedPath)) state.terminalLines.push(`<p class="term-error">ls: cannot access '${h(args[0] || requestedPath)}': no such directory. Run <button data-term-command="ls /">ls /</button>.</p>`);
    else if (requestedPath === "/") state.terminalLines.push(terminalRootListing());
    else {
      const items = [...terminalItemsAtPath(requestedPath)].sort((a, b) => Number(b.section === "winner") - Number(a.section === "winner") || byRankThenTitle(a, b));
      const name = requestedPath === "/favourites" || requestedPath === "/favorites" ? "FAVOURITES" : yearLabel(requestedPath.slice(1));
      state.terminalLines.push(`<p class="term-bright">== ${h(name)} · ${items.length} document${items.length === 1 ? "" : "s"}${requestedPath.startsWith("/20") && isPreliminaryYear(requestedPath.slice(1)) ? " · PRELIMINARY / UNRANKED / SUBJECT TO CHANGE" : ""} ==</p>${terminalRows(items)}`);
    }
  } else if (verb === "WINNERS") {
    const path = args[0] ? resolveTerminalPath(args[0]) : state.terminalCwd;
    const year = path.slice(1);
    if (!YEAR_FILES.includes(year)) state.terminalLines.push(`<p class="term-error">winners: enter or name a finalized year directory first</p>`);
    else state.terminalLines.push(isPreliminaryYear(year)
      ? `<p class="term-error">${h(yearLabel(year))} has no winners or Top 10. It is an AI-collected, unranked snapshot subject to change.</p>`
      : terminalRows(itemsForYear(year).filter((item) => item.section === "winner").sort(byRankThenTitle)));
  } else if (["FIND", "GREP", "SEARCH"].includes(verb)) {
    state.terminalLines.push(terminalGrep([...args]));
  } else if (["OPEN", "CAT", "SHOW"].includes(verb)) {
    const item = state.items.find((entry) => entry.id.toLowerCase() === (args[0] || "").toLowerCase());
    const flag = args[1]?.toLowerCase();
    if (!item) state.terminalLines.push(`<p class="term-error">open: no document '${h(args[0] || "")}'. Try <button data-term-command="grep xss">grep xss</button>.</p>`);
    else if (flag && !["--md", "--pdf", "--web", "--www"].includes(flag)) state.terminalLines.push(`<p class="term-error">open: unknown flag '${h(flag)}' (use --md, --pdf or --web)</p>`);
    else if (flag === "--md" || flag === "--pdf") {
      const available = flag === "--md" ? item.mdPath : item.pdfPath;
      state.terminalLines.push(`<p class="term-dim">${available ? `opening the shared ${flag === "--md" ? "Markdown reader" : "PDF viewer"} for ${h(item.id)}…` : `${h(item.id)} has no ${flag.slice(2).toUpperCase()} copy.`}</p>`);
      renderTerminal();
      if (available) (flag === "--md" ? openReader(item) : openPdfViewer(item));
      return;
    } else if (["--web", "--www"].includes(flag)) {
      const url = safeExternalUrl(item.originalUrl);
      state.terminalLines.push(`<p class="term-dim">${url ? `opening ${h(url)}…` : "unsafe original URL rejected."}</p>`);
      renderTerminal();
      if (url) window.open(url, "_blank", "noopener,noreferrer");
      return;
    } else state.terminalLines.push(terminalDetail(item));
  } else if (["FAV", "FAVOURITE", "FAVORITE"].includes(verb) || ["UNFAV", "UNFAVOURITE", "UNFAVORITE"].includes(verb)) {
    const item = state.items.find((entry) => entry.id.toLowerCase() === (args[0] || "").toLowerCase());
    if (!item) state.terminalLines.push(`<p class="term-error">${h(verb.toLowerCase())}: supply a valid document id</p>`);
    else {
      const adding = ["FAV", "FAVOURITE", "FAVORITE"].includes(verb);
      setFavouriteState(item, adding);
      state.terminalLines.push(`<p>${adding ? "★ added" : "☆ removed"} ${h(item.id)} ${adding ? "to" : "from"} favourites</p>`);
    }
  } else if (["FAVOURITES", "FAVORITES", "FAVS"].includes(verb)) {
    state.terminalLines.push(`<p class="term-bright">== FAVOURITES · ${favouriteItems().length} saved ==</p>${terminalRows(favouriteItems())}`);
  } else if (verb === "HISTORY") {
    state.terminalLines.push(state.terminalHistory.slice(-20).map((entry, index) => `<p><span class="term-dim">${String(index + 1).padStart(3, " ")}</span> ${h(entry)}</p>`).join(""));
  } else if (verb === "ECHO") {
    state.terminalLines.push(`<p>${h(args.join(" "))}</p>`);
  } else if (["RANDOM", "LUCKY"].includes(verb)) {
    const pool = terminalItemsAtPath();
    if (!pool.length) state.terminalLines.push(`<p class="term-error">random: ${h(state.terminalCwd)} contains no documents</p>`);
    else {
      const item = pool[Math.floor(Math.random() * pool.length)];
      state.terminalLines.push(`<p class="term-dim">/dev/urandom says: ${h(item.id)} (${h(yearLabel(item.year))})</p>${terminalDetail(item)}`);
    }
  } else if (["CLEAR", "CLS"].includes(verb)) state.terminalLines = terminalWelcome();
  else if (verb === "WHOAMI") state.terminalLines.push(`<p>guest (read-only shell — the archive is watching you back)</p>`);
  else if (["EXIT", "LOGOUT"].includes(verb)) state.terminalLines.push(`<p class="term-dim">There is no exit. There is only more web hacking research.</p>`);
  else state.terminalLines.push(`<p class="term-error">sh: ${h(verb.toLowerCase())}: command not found — try <button data-term-command="help">help</button>.</p>`);

  state.terminalLines = state.terminalLines.slice(-260);
  renderTerminal();
}

function terminalDetail(item) {
  const mdAction = item.mdPath ? `<button data-terminal-md="${h(item.id)}">[md reader]</button>` : `<span>[md unavailable]</span>`;
  const pdfAction = item.pdfPath ? `<button data-terminal-pdf="${h(item.id)}">[pdf viewer]</button>` : `<span>[pdf unavailable]</span>`;
  const original = safeExternalUrl(item.originalUrl);
  const webAction = original ? `<button data-terminal-web="${h(item.id)}">[www]</button>` : `<span>[www blocked]</span>`;
  const favouriteAction = `<button data-term-command="${item.favourite ? "unfav" : "fav"} ${h(item.id)}">[${item.favourite ? "★ remove favourite" : "☆ add favourite"}]</button>`;
  const standing = item.rank
    ? `<b class="term-gold">★ TOP 10 · rank #${item.rank}</b>`
    : item.preliminary ? `<b class="term-warn">PRELIMINARY · UNRANKED · SUBJECT TO CHANGE</b>` : `<i>nominee</i>`;
  return `<section class="terminal-detail"><p class="term-dim">┌─ ${h(item.id)} ─────────────────────────</p><p><span>title</span><strong>${h(item.title)}</strong></p><p><span>year</span>${h(yearLabel(item.year))} ${standing}</p><p><span>source</span>${h(item.publisher || "unknown")} · ${h(item.kind)}</p><p><span>topic</span>${h(item.topic)} · ${h(item.archiveStatus)}${item.favourite ? " · ★ favourite" : ""}</p><p><span>url</span><small>${h(original || "blocked unsafe URL")}</small></p><p><span>actions</span>${mdAction}${pdfAction}${webAction}${favouriteAction}<button data-artifact="${h(item.id)}">[full record]</button></p><p class="term-dim">└────────────────────────────────────────</p></section>`;
}

function terminalCompletion(value) {
  const source = String(value || "").trimStart();
  const parts = source.split(/\s+/);
  const commands = ["help", "pwd", "cd", "ls", "open", "grep", "fav", "unfav", "favorites", "random", "stats", "winners", "history", "echo", "clear", "whoami", "exit"];
  let options = commands;
  if (parts.length > 1 && ["cd", "ls", "list", "winners"].includes(parts[0].toLowerCase())) options = ["/", "..", "-", "/favourites", ...YEAR_FILES.map((year) => `/${year}`)];
  if (parts.length > 1 && ["open", "cat", "show", "fav", "favourite", "favorite", "unfav"].includes(parts[0].toLowerCase())) options = parts.length > 2 ? ["--md", "--pdf", "--web"] : terminalItemsAtPath().map((item) => item.id);
  const stem = parts.at(-1).toLowerCase();
  const match = options.find((option) => option.toLowerCase().startsWith(stem));
  if (!match) return value;
  parts[parts.length - 1] = match;
  return parts.join(" ");
}

function hashString(seed) {
  let hash = 2166136261;
  for (let index = 0; index < seed.length; index++) hash = Math.imul(hash ^ seed.charCodeAt(index), 16777619);
  return hash >>> 0;
}

function seededRandom(seed) {
  let value = seed >>> 0;
  return () => {
    value += 0x6d2b79f5;
    let mixed = value;
    mixed = Math.imul(mixed ^ mixed >>> 15, mixed | 1);
    mixed ^= mixed + Math.imul(mixed ^ mixed >>> 7, mixed | 61);
    return ((mixed ^ mixed >>> 14) >>> 0) / 4294967296;
  };
}

function renderSignals() {
  if (!YEAR_FILES.includes(state.signalYear)) state.signalYear = YEAR_FILES.at(-1);
  const activeTopic = state.signalTopic === "all" ? null : TOPICS.find((topic) => topic.name === state.signalTopic);
  const signalColor = activeTopic?.color || "#7899ff";
  const topicLabel = activeTopic?.name || "All research";
  const chart = YEAR_FILES.map((year) => {
    const summary = collectionSummaryFor(year);
    const allItems = year === state.signalYear ? itemsForYear(year) : [];
    const items = activeTopic ? allItems.filter((item) => item.topic === activeTopic.name) : allItems;
    const count = activeTopic ? Number(summary?.topicCounts?.[activeTopic.name] || 0) : Number(summary?.count || 0);
    return { year, items, count, preliminary: isPreliminaryYear(year) };
  });
  const maxCount = Math.max(1, ...chart.map((point) => point.count));
  const total = chart.reduce((sum, point) => sum + point.count, 0);
  const peak = chart.reduce((best, point) => point.count > best.count ? point : best, chart[0]);
  const selectedPoint = chart.find((point) => point.year === state.signalYear) || chart.at(-1);
  const selectedItems = selectedPoint.items;
  const selectedArchived = selectedItems.filter((item) => item.archived).length;
  const selectedRead = selectedItems.filter((item) => item.read).length;
  const selectedWinners = selectedPoint.preliminary ? 0 : selectedItems.filter((item) => item.section === "winner").length;
  const chartWidth = Math.max(1080, chart.length * 72);
  const viewWidth = Math.max(100, chart.length * 100);
  const wavePoints = chart.map((point, index) => {
    const level = point.count / maxCount;
    return `${index * 100 + 50},${(88 - level * 64).toFixed(2)}`;
  }).join(" ");
  const distribution = TOPICS.map((topic) => ({
    ...topic,
    count: itemsForYear(state.signalYear).filter((item) => item.topic === topic.name).length
  })).sort((a, b) => b.count - a.count);
  const distributionMax = Math.max(1, ...distribution.map((topic) => topic.count));
  const winnerItems = selectedPoint.preliminary ? [] : selectedItems.filter((item) => item.section === "winner");
  const nomineeItems = selectedPoint.preliminary ? [] : selectedItems.filter((item) => item.section !== "winner");
  if (selectedPoint.preliminary || (state.signalStatus === "top10" && !winnerItems.length) || (state.signalStatus === "nominee" && !nomineeItems.length)) state.signalStatus = "all";
  const statusItems = state.signalStatus === "top10" ? winnerItems : state.signalStatus === "nominee" ? nomineeItems : selectedItems;
  const sortedStatusItems = [...statusItems].sort((a, b) =>
    Number(b.section === "winner") - Number(a.section === "winner") || byRankThenTitle(a, b)
  );
  // In All mode, reveal enough results to get beyond the ranked block. This
  // makes the wider nomination field visible immediately instead of presenting
  // a Top-10-looking slice while silently hiding the rest.
  const visibleLimit = state.signalStatus === "all" && !selectedPoint.preliminary
    ? Math.max(state.signalVisibleCount, winnerItems.length + 4)
    : state.signalVisibleCount;
  const focusItems = sortedStatusItems.slice(0, visibleLimit);
  const remainingItems = Math.max(0, sortedStatusItems.length - focusItems.length);
  const filteredArchived = statusItems.filter((item) => item.archived).length;
  const statusLabel = selectedPoint.preliminary
    ? "Preliminary leads"
    : state.signalStatus === "top10" ? "Top 10" : state.signalStatus === "nominee" ? "Other nominations" : topicLabel;

  setMetric(total, `${topicLabel.toLowerCase()} signals across ${chart.length} collections`);
  $("#view-root").innerHTML = `
    <section class="signal-observatory" style="--signal-color:${h(signalColor)}">
      <header class="signal-console">
        <div class="signal-console-mark" aria-hidden="true"><span>03</span><i></i></div>
        <div>
          <p class="eyebrow">Longitudinal research receiver</p>
          <h2>What is getting louder?</h2>
          <p>Each pulse is a real paper or nomination. Tune one technique family, move across the years, then open the research behind the shape.</p>
        </div>
        <dl>
          <div><dt>Frequency</dt><dd>${h(topicLabel)}</dd></div>
          <div><dt>Peak</dt><dd>${h(yearLabel(peak.year, true))} · ${peak.count}</dd></div>
          <div><dt>Sample</dt><dd>${total.toLocaleString()} records</dd></div>
        </dl>
      </header>

      <div class="signal-tuner" role="group" aria-label="Tune a research topic">
        <button class="${state.signalTopic === "all" ? "active" : ""}" data-signal-topic="all" aria-pressed="${state.signalTopic === "all"}" style="--topic-color:#7899ff"><i></i><span>All traffic</span><b>${state.items.length.toLocaleString()}</b></button>
        ${TOPICS.map((topic) => {
          const count = state.items.filter((item) => item.topic === topic.name).length;
          return `<button class="${state.signalTopic === topic.name ? "active" : ""}" data-signal-topic="${h(topic.name)}" aria-pressed="${state.signalTopic === topic.name}" style="--topic-color:${h(topic.color)}"><i></i><span>${h(topic.name)}</span><b>${count.toLocaleString()}</b></button>`;
        }).join("")}
      </div>

      <section class="signal-chart" aria-label="${h(topicLabel)} records by collection">
        <header><div><span class="signal-live"><i></i> Live archive signal</span><strong>${h(topicLabel)}</strong></div><p>Select a year to inspect its papers</p></header>
        <div class="signal-chart-scroll">
          <div class="signal-chart-canvas" style="width:${chartWidth}px">
            <svg viewBox="0 0 ${viewWidth} 100" preserveAspectRatio="none" aria-hidden="true">
              <defs><linearGradient id="signal-wave-gradient" x1="0" x2="1"><stop stop-color="#ffb454"/><stop offset=".25" stop-color="${h(signalColor)}"/><stop offset="1" stop-color="#6ee7e7"/></linearGradient></defs>
              <polyline points="${wavePoints}" vector-effect="non-scaling-stroke"></polyline>
            </svg>
            <div class="signal-year-columns" style="grid-template-columns:repeat(${chart.length},minmax(0,1fr))">
              ${chart.map((point) => {
                const level = point.count / maxCount;
                const active = point.year === state.signalYear;
                return `<button class="${active ? "active" : ""} ${point.preliminary ? "preliminary" : ""}" data-signal-year="${h(point.year)}" aria-pressed="${active}" title="${h(`${yearLabel(point.year)}: ${point.count} ${topicLabel.toLowerCase()} record${point.count === 1 ? "" : "s"}`)}" style="--signal-level:${level.toFixed(3)}">
                  <span>${h(yearLabel(point.year, true))}</span><i><b></b></i><strong>${point.count}</strong>${point.preliminary ? "<small>PRELIM</small>" : ""}
                </button>`;
              }).join("")}
            </div>
          </div>
        </div>
        <footer><span>QUIET</span><i></i><span>PEAK ${maxCount}</span></footer>
      </section>

      <section class="signal-focus">
        ${selectedPoint.preliminary ? preliminaryNotice(selectedPoint.year) : ""}
        <div class="signal-focus-grid">
          <aside class="signal-readout">
            <p class="signal-lock"><i></i> Frequency locked</p>
            <strong>${h(yearLabel(selectedPoint.year))}</strong>
            <span>${h(topicLabel)} / ${selectedItems.length} record${selectedItems.length === 1 ? "" : "s"}</span>
            <dl>
              <div><dt>Preserved</dt><dd>${selectedArchived}</dd></div>
              <div><dt>Read</dt><dd>${selectedRead}</dd></div>
              <div><dt>${selectedPoint.preliminary ? "Status" : "Top 10"}</dt><dd>${selectedPoint.preliminary ? "Open" : selectedWinners}</dd></div>
            </dl>
            <div class="signal-distribution" aria-label="Topic distribution for ${h(yearLabel(selectedPoint.year))}">
              ${distribution.map((topic) => `<div title="${h(`${topic.name}: ${topic.count}`)}"><span>${h(topic.name)}</span><i><b style="width:${(topic.count / distributionMax * 100).toFixed(1)}%;background:${h(topic.color)}"></b></i><strong>${topic.count}</strong></div>`).join("")}
            </div>
          </aside>
          <div class="signal-findings">
            <header><div><p class="eyebrow">Papers on this frequency</p><h3>${h(statusLabel)} in ${h(yearLabel(selectedPoint.year))}</h3></div><span>${filteredArchived}/${statusItems.length} preserved</span></header>
            <div class="signal-result-tools">
              ${selectedPoint.preliminary
                ? `<div class="signal-preliminary-filter" role="status"><i></i><span>All ${selectedItems.length} preliminary leads</span></div>`
                : `<div class="signal-status-filter" role="group" aria-label="Show all research, Top 10 selections, or other nominations">
                    <span>Show</span>
                    <button class="${state.signalStatus === "all" ? "active" : ""}" data-signal-status="all" aria-pressed="${state.signalStatus === "all"}">All <b>${selectedItems.length}</b></button>
                    <button class="${state.signalStatus === "top10" ? "active" : ""}" data-signal-status="top10" aria-pressed="${state.signalStatus === "top10"}" ${winnerItems.length ? "" : "disabled"}>Top 10 <b>${winnerItems.length}</b></button>
                    <button class="${state.signalStatus === "nominee" ? "active" : ""}" data-signal-status="nominee" aria-pressed="${state.signalStatus === "nominee"}" ${nomineeItems.length ? "" : "disabled"}>Other nominations <b>${nomineeItems.length}</b></button>
                  </div>`}
              <p>Showing <b>${focusItems.length}</b> of ${statusItems.length}${state.signalStatus === "all" && winnerItems.length ? " · Top 10 first" : ""}</p>
            </div>
            <div>
              ${focusItems.map((item) => `<button class="signal-finding ${item.read ? "is-read" : ""} ${item.favourite ? "is-favourite" : ""}" data-artifact="${h(item.id)}">
                <span>${item.rank ? `#${item.rank}` : item.preliminary ? "PRELIM" : "NOM"}</span><strong>${h(item.title)}</strong><small>${h(item.publisher || item.topic)} · ${h(item.archiveStatus)}</small><i aria-hidden="true">↗</i>
              </button>`).join("") || empty(`No ${statusLabel.toLowerCase()} are filed in ${yearLabel(selectedPoint.year)}.`)}
              ${remainingItems ? `<button class="signal-more" type="button" data-signal-more>Show 12 more <span>${remainingItems} remaining</span></button>` : statusItems.length ? `<p class="signal-end">All ${statusItems.length} matching records are shown</p>` : ""}
            </div>
          </div>
        </div>
      </section>
    </section>`;
  requestAnimationFrame(() => {
    const scroll = $(".signal-chart-scroll");
    const activeYear = $(".signal-year-columns button.active");
    if (scroll && activeYear) scroll.scrollLeft = Math.max(0, activeYear.offsetLeft - (scroll.clientWidth - activeYear.clientWidth) / 2);
  });
}

function renderConstellation() {
  const yearRecord = yearRecordFor(state.starYear);
  const preliminary = yearRecord.status === "preliminary";
  if (preliminary) state.starStatus = "all";
  const yearItems = itemsForYear(state.starYear);
  let topicItems = yearItems;
  if (state.starTopic !== "all") topicItems = topicItems.filter((item) => item.topic === state.starTopic);
  const winnerCount = topicItems.filter((item) => item.section === "winner").length;
  const nomineeCount = topicItems.length - winnerCount;
  if (state.starStatus === "top10" && winnerCount === 0) state.starStatus = "all";
  if (state.starStatus === "nominee" && nomineeCount === 0) state.starStatus = "all";
  let items = topicItems;
  if (state.starStatus === "top10") items = items.filter((item) => item.section === "winner");
  if (state.starStatus === "nominee") items = items.filter((item) => item.section !== "winner");
  const statusLabel = preliminary ? "preliminary stars" : state.starStatus === "top10" ? "Top 10 stars" : state.starStatus === "nominee" ? "nominee stars" : "stars";
  setMetric(items.length, `${statusLabel} visible for ${yearLabel(state.starYear)}`);

  $("#view-root").innerHTML = `
    <div class="sky-controls">
      <div class="control-strip" style="margin:0">${yearPills(state.starYear)}</div>
      <p class="eyebrow">Drag space to orbit · tug a star to move it · double-click to approach</p>
    </div>
    ${preliminaryNotice(state.starYear)}
    <section class="constellation-frame space-3d" id="constellation-space" tabindex="0" aria-label="Navigable three-dimensional research constellation. Drag empty space to orbit, or drag a research star to move it within its cluster.">
      <canvas id="constellation-canvas" class="constellation-canvas"></canvas>
      <div class="space-reticle" aria-hidden="true"><i></i><i></i></div>
      <div class="space-coordinates">
        <span>CAMERA / <b id="space-camera-distance">650</b> AU</span>
        <span>VISIBLE / <b>${items.length}</b> RESEARCH STARS</span>
        <span>YEAR / <b>${h(yearLabel(state.starYear))}</b></span>
        ${preliminary ? `<span class="space-preliminary-key"><b>△</b> UNRANKED SNAPSHOT</span>` : `<span class="space-winner-key"><b>✦</b> GOLD HALO / TOP 10</span>`}
      </div>
      <div class="space-toolbar">
        <button id="space-reset" type="button">Reset view <kbd>R</kbd></button>
        <button id="space-autorotate" type="button" aria-pressed="true">Drift on</button>
        <button id="space-labels" type="button" aria-pressed="false">Titles off</button>
        <button id="space-focus" type="button" disabled>Focus star <kbd>F</kbd></button>
        <button id="space-tidy" type="button" disabled>Tidy stars</button>
      </div>
      <div class="space-zoom" aria-label="Camera zoom">
        <button id="space-zoom-in" aria-label="Zoom in">+</button>
        <div class="space-zoom-track" id="space-zoom-range" role="slider" tabindex="0" aria-label="Camera distance: near at the top, far at the bottom" aria-orientation="vertical" aria-valuemin="120" aria-valuemax="1500" aria-valuenow="720"><i aria-hidden="true"></i></div>
        <button id="space-zoom-out" aria-label="Zoom out">−</button>
      </div>
      <div class="space-navigator" role="group" aria-label="Spatial navigation controller">
        <span class="space-nav-title">ORBITAL NAV</span>
        <div class="space-nav-dial">
          <button class="nav-up" data-space-nav="up" aria-label="Move up" title="Move up">↑<small>UP</small></button>
          <button class="nav-left" data-space-nav="left" aria-label="Move left" title="Move left">←</button>
          <button class="nav-right" data-space-nav="right" aria-label="Move right" title="Move right">→</button>
          <button class="nav-down" data-space-nav="down" aria-label="Move down" title="Move down">↓<small>DOWN</small></button>
          <button class="nav-turn-left" data-space-nav="turn-left" aria-label="Turn left" title="Turn left">↶</button>
          <button class="nav-turn-right" data-space-nav="turn-right" aria-label="Turn right" title="Turn right">↷</button>
          <div class="nav-thrust">
            <button data-space-nav="forward" aria-label="Fly forward" title="Fly forward">▲</button>
            <span>FLY</span>
            <button data-space-nav="back" aria-label="Fly backward" title="Fly backward">▼</button>
          </div>
          <i class="nav-sweep" aria-hidden="true"></i>
        </div>
        <small class="space-nav-hint">HOLD TO MANOEUVRE</small>
      </div>
      <aside class="space-selection" id="space-selection" hidden>
        <p class="eyebrow" id="space-selection-meta">Selected star</p>
        <h3 id="space-selection-title"></h3>
        <p id="space-selection-publisher"></p>
        <div><button id="space-open-artifact">Inspect artifact</button><button id="space-favourite-artifact">☆ Add favourite</button><button id="space-fly-artifact">Fly closer</button></div>
      </aside>
      <div class="sky-legend">
        <button class="${state.starTopic === "all" ? "active" : ""}" data-topic-filter="all" aria-pressed="${state.starTopic === "all"}" style="--topic-color:#edf9f1">ALL</button>
        ${TOPICS.map((topic) => `<button class="${state.starTopic === topic.name ? "active" : ""}" data-topic-filter="${h(topic.name)}" aria-pressed="${state.starTopic === topic.name}" style="--topic-color:${h(topic.color)}">${h(topic.name.toUpperCase())}</button>`).join("")}
      </div>
      ${preliminary ? `<div class="star-rank-filter preliminary-filter" role="status"><span>UNRANKED</span><button class="active" data-star-status="all" aria-pressed="true">Preliminary <b>${topicItems.length}</b></button></div>` : `<div class="star-rank-filter" role="group" aria-label="Filter research by Top 10 status">
          <span>SHOW</span>
          <button class="${state.starStatus === "all" ? "active" : ""}" data-star-status="all" aria-pressed="${state.starStatus === "all"}">All <b>${topicItems.length}</b></button>
          <button class="top-ten ${state.starStatus === "top10" ? "active" : ""}" data-star-status="top10" aria-pressed="${state.starStatus === "top10"}" ${winnerCount ? "" : "disabled"}><i aria-hidden="true">✦</i> Top 10 <b>${winnerCount}</b></button>
          <button class="${state.starStatus === "nominee" ? "active" : ""}" data-star-status="nominee" aria-pressed="${state.starStatus === "nominee"}" ${nomineeCount ? "" : "disabled"}><span class="full-label">Nominees</span><span class="short-label">Rest</span> <b>${nomineeCount}</b></button>
        </div>`}
      <div class="space-help"><span><kbd>Drag space</kbd> orbit</span><span><kbd>Drag star</kbd> tug</span><span><kbd>Shift + drag</kbd> pan</span><span><kbd>Wheel / pinch</kbd> zoom</span></div>
    </section>`;

  if (constellationExperience) constellationExperience.destroy();
  if (!window.Constellation3D) {
    $("#constellation-space").insertAdjacentHTML("beforeend", empty("The 3D space renderer could not be loaded."));
    return;
  }
  constellationExperience = new window.Constellation3D({
    canvas: $("#constellation-canvas"),
    shell: $("#constellation-space"),
    items,
    topics: TOPICS,
    onArtifact: (id) => openArtifact(id),
    onFavourite: (id) => {
      const item = state.items.find((entry) => entry.id === id);
      if (item) setFavouriteState(item);
    },
    onToast: (message) => toast(message)
  });
  constellationExperience.mount();
}

function renderEvidence() {
  destroyInvestigationLayout();
  const preliminary = isPreliminaryYear(state.year);
  const items = itemsForYear(state.year);
  const winners = items.filter((item) => item.section === "winner");
  const nominees = items.filter((item) => item.section !== "winner");
  const archived = items.filter((item) => item.archived).length;
  setMetric(items.length, `${preliminary ? "preliminary leads" : "case files"} pinned for ${yearLabel(state.year)}`);
  $("#view-root").innerHTML = `
    <section class="investigation-shell">
      <header class="investigation-tools">
        <div><strong>THE <span>INVESTIGATION</span> BOARD</strong><small>evidence archive 2006–2026 · preliminary material flagged</small></div>
        <div><button id="investigation-search" type="button">⌕ case index <kbd>/</kbd></button><button id="investigation-dense" type="button" aria-pressed="${state.evidenceDense}">⌗ dense</button><button id="investigation-reset" type="button">↺ reset layout</button></div>
      </header>
      <nav class="case-tabs" aria-label="Case files by year">${YEAR_FILES.map((year) => `<button class="case-tab ${isPreliminaryYear(year) ? "preliminary" : ""}" data-year="${h(year)}" aria-current="${year === state.year}">CASE ${h(yearLabel(year, true))}</button>`).join("")}</nav>
      ${preliminaryNotice(state.year)}
      <div class="case-slip ${preliminary ? "preliminary" : ""}"><b>CASE ${h(yearLabel(state.year))}</b><strong>${preliminary ? "PRELIMINARY WEB RESEARCH LEADS" : "TOP 10 WEB HACKING TECHNIQUES"}</strong><span>${preliminary ? `${items.length} unranked leads · AI-collected · subject to change` : `${winners.length} exhibits pinned · ${nominees.length} supporting leads`} · ${archived}/${items.length} on file</span></div>
      <div class="investigation-board-frame"><div class="investigation-board ${state.evidenceDense ? "dense" : ""}" id="investigation-board"><svg id="investigation-strings" aria-hidden="true"></svg></div></div>
      <footer class="investigation-key">${preliminary ? `<span><i class="gold"></i> Preliminary, unranked lead</span>` : `<span><i class="red"></i> Top 10 evidence</span><span><i class="gold"></i> Supporting lead</span>`}<span><i class="grey"></i> Local copy missing</span><span>Drag cards to rearrange the case. Select one to inspect its Markdown, PDF and source.</span></footer>
    </section>`;

  $("#investigation-dense").addEventListener("click", () => {
    state.evidenceDense = !state.evidenceDense;
    $("#investigation-dense").setAttribute("aria-pressed", String(state.evidenceDense));
    $("#investigation-board").classList.toggle("dense", state.evidenceDense);
    layoutInvestigationBoard();
  });
  $("#investigation-reset").addEventListener("click", layoutInvestigationBoard);
  $("#investigation-search").addEventListener("click", () => $("#global-search").focus());
  investigationResizeObserver = new ResizeObserver((entries) => {
    const width = Math.round(entries[0]?.contentRect.width || 0);
    const previous = Number($("#investigation-board")?.dataset.layoutWidth || 0);
    if (width && Math.abs(width - previous) > 16) layoutInvestigationBoard();
  });
  investigationResizeObserver.observe($("#investigation-board"));
  requestAnimationFrame(() => {
    $(".case-tab[aria-current='true']")?.scrollIntoView({ block: "nearest", inline: "center" });
    layoutInvestigationBoard();
  });
}

function investigationMetrics() {
  return state.evidenceDense
    ? { cellW: 112, cellH: 92, topW: 128, nomineeW: 98, pad: 18, topPad: 24 }
    : { cellW: 178, cellH: 158, topW: 204, nomineeW: 150, pad: 24, topPad: 30 };
}

function layoutInvestigationBoard() {
  const board = $("#investigation-board");
  if (!board || state.view !== "evidence") return;
  const items = [...itemsForYear(state.year)].sort((a, b) => Number(b.section === "winner") - Number(a.section === "winner") || byRankThenTitle(a, b));
  const metrics = investigationMetrics();
  const boardWidth = Math.max(280, board.clientWidth || 900);
  const columns = Math.max(2, Math.floor((boardWidth - metrics.pad * 2) / metrics.cellW));
  const rows = Math.max(2, Math.ceil(items.length / columns));
  const boardHeight = rows * metrics.cellH + metrics.topPad + metrics.pad + 36;
  const centreX = (columns - 1) / 2;
  const centreY = (rows - 1) / 2;
  const cells = [];
  for (let row = 0; row < rows; row++) {
    for (let column = 0; column < columns; column++) {
      const x = (column - centreX) * metrics.cellW;
      const y = (row - centreY) * metrics.cellH;
      cells.push({ row, column, distance: Math.hypot(x, y) });
    }
  }
  cells.sort((a, b) => a.distance - b.distance);
  investigationCardInfo = new Map();
  board.dataset.layoutWidth = String(Math.round(boardWidth));
  board.style.minHeight = `${boardHeight}px`;
  board.innerHTML = `<svg id="investigation-strings" aria-hidden="true"></svg>${items.map((item, index) => {
    const cell = cells[index] || cells.at(-1);
    const random = seededRandom(hashString(item.id));
    const winner = item.section === "winner";
    const width = winner ? metrics.topW : metrics.nomineeW;
    const x = clampNumber(metrics.pad + cell.column * metrics.cellW + (metrics.cellW - width) / 2 + (random() - .5) * metrics.cellW * .34, 4, boardWidth - width - 4);
    const y = clampNumber(metrics.topPad + cell.row * metrics.cellH + (random() - .5) * metrics.cellH * .26, 4, boardHeight - 60);
    const rotation = state.motionReduced ? 0 : (random() - .5) * (winner ? 6.5 : 9);
    const pinOffset = (random() - .5) * width * .4;
    investigationCardInfo.set(item.id, { item, x, y, width, pinOffset, winner, missing: !item.archived });
    return `<button type="button" class="investigation-card ${winner ? "top-evidence" : "supporting-evidence"} ${item.archived ? "" : "evidence-stub"} ${item.read ? "is-read" : ""} ${item.favourite ? "is-favourite" : ""}" data-artifact="${h(item.id)}" style="--card-rotation:${rotation.toFixed(2)}deg;left:${Math.round(x)}px;top:${Math.round(y)}px" aria-label="${h(`${item.rank ? `Rank ${item.rank}: ` : ""}${item.title}. ${item.archived ? "Local copy on file." : "Original source only."}${item.favourite ? " Favourite." : ""}`)}"><i class="evidence-pin ${item.archived ? winner ? "red" : "gold" : "grey"}" style="left:calc(50% + ${Math.round(pinOffset)}px)"></i>${winner ? `<span class="evidence-stamp">RANK #${item.rank}</span>` : ""}<strong>${h(item.title)}</strong>${item.archived ? `<small>${h(item.publisher || item.topic)} · ${h(item.kind)}</small>` : `<small class="missing-label">Evidence missing — original link only</small>`}${item.favourite ? `<b class="evidence-favourite">★ SAVED</b>` : ""}${item.read ? `<b class="evidence-read">READ</b>` : ""}</button>`;
  }).join("")}`;

  if (!window.matchMedia("(max-width: 560px)").matches) {
    $$(".investigation-card", board).forEach(makeInvestigationCardDraggable);
  }
  drawInvestigationStrings();
}

function investigationPinPoint(info) {
  return { x: info.x + info.width / 2 + info.pinOffset, y: info.y + (state.evidenceDense ? 7 : 11) };
}

function drawInvestigationStrings() {
  const board = $("#investigation-board");
  const svg = $("#investigation-strings");
  if (!board || !svg) return;
  const entries = [...investigationCardInfo.values()];
  const hub = entries.filter((info) => info.winner && !info.missing).sort((a, b) => (a.item.rank || 99) - (b.item.rank || 99))[0];
  svg.setAttribute("viewBox", `0 0 ${board.clientWidth} ${board.clientHeight}`);
  svg.replaceChildren();
  if (!hub) return;
  const start = investigationPinPoint(hub);
  const pathData = entries.filter((info) => info.winner && !info.missing && info !== hub).map((info) => {
    const end = investigationPinPoint(info);
    const distance = Math.hypot(end.x - start.x, end.y - start.y);
    return `M${start.x.toFixed(1)} ${start.y.toFixed(1)} Q${((start.x + end.x) / 2).toFixed(1)} ${((start.y + end.y) / 2 + Math.min(64, 14 + distance * .1)).toFixed(1)} ${end.x.toFixed(1)} ${end.y.toFixed(1)}`;
  }).join(" ");
  if (!pathData) return;
  const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
  path.setAttribute("d", pathData);
  path.setAttribute("fill", "none");
  path.setAttribute("stroke", "#c0232c");
  path.setAttribute("stroke-width", "2");
  path.setAttribute("stroke-linecap", "round");
  path.setAttribute("opacity", ".92");
  svg.appendChild(path);
}

function makeInvestigationCardDraggable(card) {
  const info = investigationCardInfo.get(card.dataset.artifact);
  if (!info) return;
  let pointerId = null;
  let startX = 0;
  let startY = 0;
  let originalX = 0;
  let originalY = 0;
  let moving = false;
  card.addEventListener("pointerdown", (event) => {
    if (event.pointerType === "mouse" && event.button !== 0) return;
    pointerId = event.pointerId;
    startX = event.clientX;
    startY = event.clientY;
    originalX = info.x;
    originalY = info.y;
    moving = false;
    card.setPointerCapture?.(pointerId);
  });
  card.addEventListener("pointermove", (event) => {
    if (pointerId === null || event.pointerId !== pointerId) return;
    const deltaX = event.clientX - startX;
    const deltaY = event.clientY - startY;
    if (!moving && Math.hypot(deltaX, deltaY) > 6) {
      moving = true;
      card.classList.add("dragging");
    }
    if (!moving) return;
    const board = $("#investigation-board");
    info.x = clampNumber(originalX + deltaX, 2, board.clientWidth - info.width - 2);
    info.y = clampNumber(originalY + deltaY, 2, board.clientHeight - 40);
    card.style.left = `${Math.round(info.x)}px`;
    card.style.top = `${Math.round(info.y)}px`;
    if (info.winner && !info.missing) drawInvestigationStrings();
  });
  const finish = (event) => {
    if (pointerId === null || event.pointerId !== pointerId) return;
    card.releasePointerCapture?.(pointerId);
    pointerId = null;
    if (moving) {
      card.classList.remove("dragging");
      card.dataset.dragged = "true";
      drawInvestigationStrings();
    }
    moving = false;
  };
  card.addEventListener("pointerup", finish);
  card.addEventListener("pointercancel", finish);
}

function destroyInvestigationLayout() {
  investigationResizeObserver?.disconnect();
  investigationResizeObserver = null;
  investigationCardInfo = new Map();
}

function annualPdfPath(year) {
  if (!YEAR_FILES.includes(year) || yearRecordFor(year).ranked === false) return "";
  const combined = ["2006", "2012", "2013", "2014", "2015"];
  const file = combined.includes(year) ? `${year}-nominees-and-top10.pdf` : `${year}-top10.pdf`;
  return `original-listings/${file}`;
}

async function openArtifact(id) {
  const item = await ensureItemLoaded(id);
  if (!item) return;
  const dialog = $("#artifact-dialog");
  const signalMode = state.view === "signals";
  dialog.classList.toggle("signal-artifact", signalMode);
  dialog.style.setProperty("--dialog-color", signalMode ? "#7899ff" : item.topicColor);
  $("#artifact-eyebrow").textContent = `${item.yearLabel || item.year} / ${item.preliminary ? "Preliminary · unranked · subject to change" : item.section === "winner" ? `Top 10 rank #${item.rank}` : item.excluded ? "Held out of vote" : "Other nomination"}`;
  $("#artifact-title").textContent = item.title;
  $("#artifact-badges").innerHTML = [item.topic, item.kind, item.archiveStatus, item.language, item.translated ? "English translation" : ""].filter(Boolean).map((badge) => `<span>${h(badge)}</span>`).join("");
  const contextText = item.preliminary
    ? `This is a ${item.provenance || "provisional"} research lead, not a nomination or Top 10 result. ${yearRecordFor(item.year).notice}`
    : item.rank
    ? `This technique placed #${item.rank} in the ${item.year} Top 10. The archive connects the curated listing to the preserved research and its original source.`
    : `This work was nominated in ${item.year}. It remains part of the long tail of research preserved alongside the winning techniques.`;
  $("#artifact-context").textContent = item.note ? `${contextText} Listing note: ${item.note}.` : contextText;
  const credited = (item.authors || []).join(", ");
  $("#artifact-facts").innerHTML = `
    ${credited ? `<div><dt>Author</dt><dd title="${h(credited)}">${h(credited)}</dd></div>` : ""}
    <div><dt>Publisher</dt><dd title="${h(item.publisher)}">${h(item.publisher || "Unknown")}</dd></div>
    <div><dt>Source type</dt><dd>${h(item.kind)}</dd></div>
    <div><dt>Preservation</dt><dd>${h(item.archiveStatus)}</dd></div>
    <div><dt>List citation</dt><dd>${h(`${item.year}.md:${item.line}`)}</dd></div>`;

  const actions = [];
  if (item.mdPath) actions.push(`<button id="open-reader" type="button">▤ Read article</button>`);
  else actions.push(`<span class="disabled">MD unavailable</span>`);
  if (item.pdfPath) actions.push(`<button class="secondary" id="open-pdf-reader" type="button">▧ View PDF</button>`);
  else actions.push(`<span class="disabled">PDF unavailable</span>`);
  // The two buttons above open the English translation for a translated
  // reference; these reach the words the author actually published.
  if (item.originalMdPath) actions.push(`<button class="secondary" id="open-original-reader" type="button">▤ Original ${h(item.language || "language")}</button>`);
  if (item.originalPdfPath) actions.push(`<button class="secondary" id="open-original-pdf" type="button">▧ Original ${h(item.language || "language")} PDF</button>`);
  // A rejected URL must not become `href=""`, which silently reloads the app.
  const originalUrl = safeExternalUrl(item.originalUrl);
  actions.push(originalUrl
    ? `<a class="secondary" href="${h(originalUrl)}" target="_blank" rel="noopener noreferrer">↗ Original source</a>`
    : `<span class="disabled">Original source blocked</span>`);
  (item.links || []).slice(1).forEach((link) => {
    const href = safeExternalUrl(link.url);
    if (href) actions.push(`<a class="secondary" href="${h(href)}" target="_blank" rel="noopener noreferrer">↗ ${h(short(link.label, 42))}</a>`);
  });
  const resultsPdf = annualPdfPath(item.year);
  if (resultsPdf) actions.push(`<button class="secondary" id="open-results-pdf" type="button">◇ ${h(item.year)} results</button>`);
  actions.push(`<button class="secondary read-toggle" id="artifact-read-toggle" type="button" aria-pressed="${item.read}">${item.read ? "✓ Read" : "○ Mark as read"}</button>`);
  actions.push(`<button class="secondary favourite-toggle" id="artifact-favourite-toggle" type="button" aria-pressed="${item.favourite}">${item.favourite ? "★ Favourite" : "☆ Add favourite"}</button>`);
  actions.push(`<button class="secondary" id="share-artifact" type="button">⌁ Share record</button>`);
  $("#artifact-actions").innerHTML = actions.join("");

  $("#open-reader")?.addEventListener("click", () => openReader(item));
  $("#open-pdf-reader")?.addEventListener("click", () => openPdfViewer(item));
  $("#open-original-reader")?.addEventListener("click", () => openReader(item, { original: true }));
  $("#open-original-pdf")?.addEventListener("click", () => openPdfViewer(item, { path: item.originalPdfPath, original: true }));
  $("#open-results-pdf")?.addEventListener("click", () => openPdfViewer(null, {
    path: resultsPdf,
    kind: "listingPdf",
    title: `${item.year} Top 10 results`,
    kicker: `Official archive listing / ${item.year}`
  }));
  $("#artifact-read-toggle").addEventListener("click", () => setReadState(item));
  $("#artifact-favourite-toggle").addEventListener("click", () => setFavouriteState(item));

  $("#share-artifact").addEventListener("click", () => shareDocument(item));

  if (!dialog.open) dialog.showModal();
}

function showPdfFallback(message = "The preserved file is still available using the Open tab or Download controls above.") {
  clearTimeout(pdfLoadTimer);
  $("#pdf-loading").hidden = true;
  $("#pdf-frame").hidden = true;
  $("#pdf-fallback").hidden = false;
  $("#pdf-fallback-message").textContent = message;
}

async function verifyPdf(mode, url, path) {
  const token = ++pdfVerifyToken;
  try {
    const response = await fetch(url, { method: "HEAD", credentials: "same-origin", redirect: "error", cache: "default" });
    const contentType = response.headers.get("content-type")?.split(";")[0].trim().toLowerCase();
    if (!response.ok || contentType !== "application/pdf") throw new Error(`Unexpected PDF response (${response.status || "network"}, ${contentType || "unknown type"})`);
    if (token !== pdfVerifyToken || path !== state.pdfPath) return;
    state.pdfVerified = true;
    setPdfView(mode);
  } catch (error) {
    if (token !== pdfVerifyToken || path !== state.pdfPath) return;
    const externalFallback = LARGE_PDF_FALLBACKS.get(path);
    if (externalFallback) {
      $("#pdf-new-tab").href = externalFallback;
      $("#pdf-new-tab").textContent = "Open backup ↗";
      $("#pdf-download").href = externalFallback;
      $("#pdf-download").removeAttribute("download");
      $("#pdf-download").target = "_blank";
      $("#pdf-download").rel = "noopener noreferrer";
      $("#pdf-download").textContent = "Backup PDF";
      showPdfFallback("This large document is hosted by the archive's GitHub Pages backup because it exceeds Cloudflare Pages' per-file limit. Open the verified backup in a new tab.");
      return;
    }
    showPdfFallback(`The document could not be safely verified: ${error.message}. Use Open tab or Download if you trust this local file.`);
  }
}

function setPdfView(mode) {
  if (!state.pdfPath || !["page-width", "page-fit"].includes(mode)) return;
  const url = archiveUrl(state.pdfPath, state.pdfKind, state.pdfVersion);
  if (!url) return showPdfFallback();
  state.pdfViewMode = mode;
  const frame = $("#pdf-frame");
  $("#pdf-fit-width").classList.toggle("active", mode === "page-width");
  $("#pdf-fit-page").classList.toggle("active", mode === "page-fit");
  $("#pdf-loading").hidden = false;
  $("#pdf-fallback").hidden = true;
  frame.hidden = true;
  clearTimeout(pdfLoadTimer);
  if (!state.pdfVerified) {
    verifyPdf(mode, url, state.pdfPath);
    return;
  }
  if (navigator.pdfViewerEnabled === false) return showPdfFallback();
  frame.src = `${url}#toolbar=1&navpanes=0&zoom=${mode}`;
  pdfLoadTimer = setTimeout(showPdfFallback, 9000);
}

function openPdfViewer(item, options = {}) {
  const kind = options.kind === "listingPdf" ? "listingPdf" : "pdf";
  const path = safeArchivePath(options.path || item?.pdfPath, kind);
  // An annual results PDF is not a preserved reference and carries no token.
  const version = kind === "listingPdf" ? ""
    : options.original ? (item?.originalPdfVersion || "") : (item?.pdfVersion || "");
  const url = archiveUrl(path, kind, version);
  if (!path || !url) {
    toast("This PDF path is unavailable or did not pass validation");
    return;
  }

  state.pdfItem = item || null;
  state.pdfPath = path;
  state.pdfKind = kind;
  // The token belongs to the path, so it is held beside it: the verify probe,
  // the frame and the download link must all ask for the same URL.
  state.pdfVersion = options.original ? (item?.originalPdfVersion || "") : (item?.pdfVersion || "");
  state.pdfVerified = false;
  const title = options.title || item?.title || "Preserved PDF";
  $("#pdf-title").textContent = title;
  const pdfLanguageNote = !item?.translated
    ? "PDF"
    : options.original
      ? `original ${item.language || "source"} PDF`
      : "English translation PDF";
  $("#pdf-kicker").textContent = options.kicker || `${item?.year || "Archive"} / ${(item && creditOf(item)) || item?.topic || "local preservation"} / ${pdfLanguageNote}`;
  const readButton = $("#pdf-read-toggle");
  readButton.hidden = !item;
  const favouriteButton = $("#pdf-favourite-toggle");
  favouriteButton.hidden = !item;
  if (item) {
    readButton.setAttribute("aria-pressed", String(item.read));
    readButton.textContent = item.read ? "✓ Read" : "○ Mark as read";
    favouriteButton.setAttribute("aria-pressed", String(item.favourite));
    favouriteButton.textContent = item.favourite ? "★ Favourite" : "☆ Add favourite";
  }
  $("#pdf-open-markdown").hidden = !item?.mdPath;
  state.pdfOriginal = Boolean(options.original);
  $("#pdf-links-toggle").hidden = !item?.mdPath;
  togglePdfLinks(false);
  $("#pdf-links").dataset.path = "";
  $("#pdf-new-tab").href = url;
  $("#pdf-new-tab").textContent = "Open tab ↗";
  $("#pdf-download").href = url;
  $("#pdf-download").textContent = "Download";
  $("#pdf-download").removeAttribute("target");
  $("#pdf-download").removeAttribute("rel");
  $("#pdf-download").setAttribute("download", path.split("/").at(-1));

  [$("#artifact-dialog"), $("#reader-dialog")].forEach((dialog) => {
    if (dialog.open) dialog.close();
  });
  syncDocumentUrl(item, kind === "listingPdf" ? "results" : "pdf");
  const dialog = $("#pdf-dialog");
  if (!dialog.open) dialog.showModal();
  setPdfView(state.pdfViewMode);
}

// A LINK INSIDE AN EMBEDDED PDF CANNOT OPEN A NEW TAB, and that is the viewer's
// decision rather than ours: the browser's own PDF viewer gives its links no
// target, so a click navigates the frame they sit in - which this page's
// `frame-src 'self'` then refuses, so the click does nothing at all.
//
// The alternative is shipping a JavaScript PDF viewer and telling it to target
// a new tab. That would run third-party PDFs - the actual subject matter of this
// archive - as script in this origin, next to the reader's own data, in place of
// the browser's sandboxed viewer process. Not for a link target.
//
// So the links get a route of their own. They are read from the preserved
// Markdown, which for a rendered PDF is the very document that was printed, and
// for a preserved original is the text extracted from it.
const PDF_LINK_LIMIT = 400;

function linksInMarkdown(markdown) {
  const found = new Map();
  const remember = (url, label) => {
    // Raw Markdown, so no HTML escaping layer to undo first.
    const safe = safeExternalUrl(url);
    if (!safe || found.has(safe) || found.size >= PDF_LINK_LIMIT) return;
    found.set(safe, (label || "").replace(/[*_`]/g, "").trim() || safe);
  };
  const body = String(markdown || "");
  for (const match of body.matchAll(/\[([^\]\n]{1,120})\]\((https?:\/\/[^\s)]+)\)/g)) {
    remember(match[2], match[1]);
  }
  for (const match of body.matchAll(/<(https?:\/\/[^>\s]+)>/g)) remember(match[1], "");
  for (const match of body.matchAll(/(?<![("<[])\bhttps?:\/\/[^\s)<>"'\]]+/g)) {
    remember(match[0], "");
  }
  return [...found].map(([url, label]) => ({ url, label }));
}

async function togglePdfLinks(force) {
  const panel = $("#pdf-links");
  const button = $("#pdf-links-toggle");
  const show = force ?? panel.hidden;
  panel.hidden = !show;
  button.setAttribute("aria-expanded", String(show));
  button.classList.toggle("active", show);
  if (!show || panel.dataset.path === state.pdfPath) return;

  const list = $("#pdf-links-list");
  const item = state.pdfItem;
  const markdownUrl = archiveUrl(state.pdfOriginal ? item?.originalMdPath : item?.mdPath, "md",
                                 item?.mdVersion);
  if (!markdownUrl) {
    list.innerHTML = `<p>No preserved text accompanies this document, so its links could not be listed.</p>`;
    return;
  }
  list.innerHTML = `<p>Reading the preserved text…</p>`;
  panel.dataset.path = state.pdfPath;
  try {
    const response = await fetch(markdownUrl, { credentials: "same-origin", cache: "default" });
    if (!response.ok) throw new Error(`Markdown returned ${response.status}`);
    const links = linksInMarkdown(await response.text());
    if (panel.dataset.path !== state.pdfPath) return;
    list.innerHTML = links.length
      ? links.map((link) => `<a href="${h(link.url)}" target="_blank" rel="noopener noreferrer">${h(short(link.label, 70))}<small>${h(link.url)}</small></a>`).join("")
      : `<p>This document carries no outbound links.</p>`;
  } catch (error) {
    panel.dataset.path = "";
    list.innerHTML = `<p>The preserved text could not be read. ${h(error.message)}</p>`;
  }
}

function clearPdfViewer() {
  clearTimeout(pdfLoadTimer);
  pdfVerifyToken++;
  pdfLoadTimer = null;
  state.pdfItem = null;
  state.pdfPath = "";
  state.pdfVersion = "";
  state.pdfVerified = false;
  if (!$("#reader-dialog").open) clearDocumentUrl();
  const frame = $("#pdf-frame");
  frame.hidden = true;
  frame.removeAttribute("src");
  $("#pdf-loading").hidden = true;
  $("#pdf-fallback").hidden = true;
  $("#pdf-links").hidden = true;
  $("#pdf-links").dataset.path = "";
  $("#pdf-links-toggle").setAttribute("aria-expanded", "false");
  $("#pdf-links-toggle").classList.remove("active");
}

function clampNumber(value, min, max) {
  return Math.max(min, Math.min(max, value));
}

// SYNTAX HIGHLIGHTING, WITHOUT A LIBRARY. The Content-Security-Policy is
// script-src 'self', so a CDN highlighter is not an option and vendoring one
// for a handful of token classes is not worth the weight. This scans the RAW
// source and escapes every piece as it emits it - never the other way round.
// Highlighting escaped text would mean matching against &quot; and &amp;, and
// one wrong boundary there turns archived exploit text into live markup.
const HL_KEYWORDS = {
  python: "and as assert async await break class continue def del elif else except finally for from global if import in is lambda nonlocal not or pass raise return try while with yield None True False self print",
  javascript: "async await break case catch class const continue debugger default delete do else export extends finally for function if import in instanceof let new return static super switch this throw try typeof var void while with yield null true false undefined",
  php: "abstract and array as break callable case catch class clone const continue declare default do echo else elseif empty enddeclare endfor endforeach endif endswitch endwhile extends final finally fn for foreach function global if implements include include_once instanceof insteadof interface isset list namespace new or print private protected public require require_once return static switch throw trait try unset use var while xor yield null true false",
  java: "abstract assert boolean break byte case catch char class const continue default do double else enum extends final finally float for goto if implements import instanceof int interface long native new package private protected public return short static strictfp super switch synchronized this throw throws transient try void volatile while null true false",
  ruby: "alias and begin break case class def defined do else elsif end ensure false for if in module next nil not or redo rescue retry return self super then true undef unless until when while yield puts require",
  elixir: "after and case catch cond def defmodule defp do else end fn for if import in not or quote raise rescue require try unless unquote use when nil true false",
  sql: "select from where insert update delete into values join left right inner outer on group by order having limit union all as and or not null convert cast char varchar int",
  bash: "if then else elif fi for while do done case esac function return export local echo cd exit",
  go: "break case chan const continue default defer else fallthrough for func go goto if import interface map package range return select struct switch type var nil true false",
};
HL_KEYWORDS.js = HL_KEYWORDS.javascript;
HL_KEYWORDS.nodejs = HL_KEYWORDS.javascript;
HL_KEYWORDS.jinja = HL_KEYWORDS.python;
HL_KEYWORDS.py = HL_KEYWORDS.python;
HL_KEYWORDS.sh = HL_KEYWORDS.bash;
HL_KEYWORDS.shell = HL_KEYWORDS.bash;

// Which comment openers are real for a language: '#' starts a comment in Python
// and Ruby but is a fragment in a URL and an id selector in CSS, so treating it
// as a comment everywhere greys out half of an HTTP listing.
const HL_HASH = new Set(["python", "py", "ruby", "bash", "sh", "shell", "php", "yaml", "jinja"]);
const HL_SLASH = new Set(["javascript", "js", "nodejs", "java", "php", "go", "c", "cpp", "csharp", "rust", "kotlin", "swift", "scala"]);

function highlightCode(code, language) {
  const lang = String(language || "").toLowerCase();
  const words = HL_KEYWORDS[lang];
  // An unknown or deliberately plain language still gets escaped, just not lit.
  if (!words && !HL_HASH.has(lang) && !HL_SLASH.has(lang)) return h(code);
  const keywords = new Set((words || "").split(" ").filter(Boolean));
  const parts = ["(\\/\\*[\\s\\S]*?\\*\\/|<!--[\\s\\S]*?-->)"];
  const lineComment = [HL_SLASH.has(lang) ? "\\/\\/[^\\n]*" : "", HL_HASH.has(lang) ? "#[^\\n]*" : ""]
    .filter(Boolean).join("|");
  parts.push(lineComment ? `(${lineComment})` : "(?!)()");
  parts.push('("(?:\\\\.|[^"\\\\\\n])*"|\'(?:\\\\.|[^\'\\\\\\n])*\'|`(?:\\\\.|[^`\\\\])*`)');
  parts.push("(\\b\\d[\\w.]*\\b)");
  parts.push("([A-Za-z_$][\\w$]*)");
  const scanner = new RegExp(parts.join("|"), "g");
  let out = "", last = 0, match;
  while ((match = scanner.exec(code))) {
    out += h(code.slice(last, match.index));
    const [text, block, line, string, number, word] = match;
    if (block || line) out += `<span class="tok-com">${h(text)}</span>`;
    else if (string) out += `<span class="tok-str">${h(text)}</span>`;
    else if (number) out += `<span class="tok-num">${h(text)}</span>`;
    else if (word && keywords.has(word)) out += `<span class="tok-kw">${h(text)}</span>`;
    else out += h(text);
    last = match.index + text.length;
  }
  return out + h(code.slice(last));
}

function formatInlineEmphasis(value) {
  return value
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .replace(/__([^_]+)__/g, "<strong>$1</strong>")
    .replace(/(^|[\s(])\*([^*\n]+)\*(?=$|[\s).,!?:;])/g, "$1<em>$2</em>")
    .replace(/~~([^~]+)~~/g, "<del>$1</del>");
}

function inlineMarkdown(value) {
  const safeTokens = [];
  const hold = (html) => {
    const token = `%%<inline:${safeTokens.length}>%%`;
    safeTokens.push(html);
    return token;
  };
  // The raw "<" in the placeholder cannot appear in escaped text, so document
  // content can never collide with (or forge) one of these trusted tokens.
  let output = h(value).replace(/`([^`]+)`/g, (_, code) => {
    return hold(`<code>${code}</code>`);
  });

  // Preserved Markdown is third-party input. Loading its images automatically
  // would let a document probe private-network URLs, make cookie-bearing image
  // requests, or track every reader. Keep the URL available behind an explicit
  // click; the archived PDF remains the durable visual copy where one exists.
  output = output.replace(/!\[([^\]]*)\]\((https?:\/\/[^\s)]+)(?:\s+&quot;[^&]*&quot;)?\)/g, (_, alt, url) => {
    const linkUrl = safeMarkdownUrl(url);
    if (!linkUrl) return alt;
    const label = formatInlineEmphasis(alt || "External article image");
    return hold(`<span class="external-image-reference"><span>${label}</span><a href="${h(linkUrl)}" target="_blank" rel="noopener noreferrer">Open publisher image ↗</a></span>`);
  });
  output = output.replace(/\[([^\]]+)\]\((https?:\/\/[^\s)]+)(?:\s+&quot;[^&]*&quot;)?\)/g, (_, label, url) => {
    const safe = safeMarkdownUrl(url);
    return safe ? hold(`<a href="${h(safe)}" target="_blank" rel="noopener noreferrer">${formatInlineEmphasis(label)}</a>`) : label;
  });
  output = output.replace(/&lt;(https?:\/\/[^&\s]+)&gt;/g, (_, url) => {
    const safe = safeMarkdownUrl(url);
    return safe ? hold(`<a href="${h(safe)}" target="_blank" rel="noopener noreferrer">${h(safe)}</a>`) : url;
  });
  output = formatInlineEmphasis(output);
  // Function form so "$&", "$'" etc. inside untrusted code spans are never
  // interpreted as replacement patterns. Reverse order restores a link that
  // contains an earlier code token before restoring the code inside its label.
  for (let index = safeTokens.length - 1; index >= 0; index--) {
    output = output.replace(`%%<inline:${index}>%%`, () => safeTokens[index]);
  }
  return output;
}

function demotedHeading(line) {
  return line.length > 300 && /^#{1,6}\s+/.test(line)
    ? line.replace(/^#{1,6}\s*/, "")
    : line;
}

function markdownDocument(markdown) {
  let body = String(markdown).replace(/^\uFEFF/, "");
  if (body.startsWith("---\n") || body.startsWith("---\r\n")) {
    const end = body.indexOf("\n---", 4);
    if (end !== -1) body = body.slice(body.indexOf("\n", end + 1) + 1);
  }

  const lines = body.split(/\r?\n/);
  const html = [];
  const headings = [];
  const usedSlugs = new Map();
  let paragraph = [];

  const flushParagraph = () => {
    if (!paragraph.length) return;
    html.push(`<p>${inlineMarkdown(paragraph.join(" "))}</p>`);
    paragraph = [];
  };
  const makeSlug = (title) => {
    const base = title.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "") || "section";
    const count = usedSlugs.get(base) || 0;
    usedSlugs.set(base, count + 1);
    // The md- namespace keeps untrusted heading ids from colliding with (and
    // clobbering lookups of) the application's own element ids.
    return `md-${count ? `${base}-${count + 1}` : base}`;
  };

  for (let index = 0; index < lines.length; index++) {
    const line = lines[index];
    const next = lines[index + 1] || "";
    if (/^```/.test(line.trim())) {
      flushParagraph();
      const language = line.trim().slice(3).replace(/[^a-z0-9_-]/gi, "");
      const code = [];
      index++;
      while (index < lines.length && !/^```/.test(lines[index].trim())) code.push(lines[index++]);
      html.push(`<pre><code${language ? ` class="language-${h(language)}"` : ""}>${highlightCode(code.join("\n"), language)}</code></pre>`);
      continue;
    }
    // A HEADING THE LENGTH OF AN ARTICLE IS NOT A HEADING. Some sources put a
    // whole slide's transcript inside an `<h2>`, and one blog leaves its article
    // in a hidden element as Markdown source whose newlines HTML collapses: the
    // reader then renders thousands of words as one wall of display type.
    // Measured over 13,865 archived headings, the median is 24 characters and the
    // 99th percentile is 206, so nothing above 300 is a title anybody wrote - it
    // is 30 lines across 13 documents, every one of them a flattened paragraph.
    // The ARCHIVE keeps what the source said; only the rendering is capped.
    const heading = line.length <= 300 ? line.match(/^(#{1,4})\s+(.+)$/) : null;
    if (heading) {
      flushParagraph();
      const level = heading[1].length;
      const title = heading[2].replace(/\s+#+$/, "");
      const slug = makeSlug(title);
      headings.push({ level, title: title.replace(/[*_`]/g, ""), slug });
      html.push(`<h${level} id="${slug}">${inlineMarkdown(title)}</h${level}>`);
      continue;
    }
    if (/^\s*(---+|___+|\*\*\*+)\s*$/.test(line)) {
      flushParagraph();
      html.push("<hr>");
      continue;
    }
    if (line.includes("|") && /^\s*\|?\s*:?-{3,}/.test(next)) {
      flushParagraph();
      const splitRow = (row) => row.trim().replace(/^\||\|$/g, "").split("|").map((cell) => cell.trim());
      const headers = splitRow(line);
      index += 2;
      const rows = [];
      while (index < lines.length && lines[index].includes("|") && lines[index].trim()) rows.push(splitRow(lines[index++]));
      index--;
      html.push(`<table><thead><tr>${headers.map((cell) => `<th>${inlineMarkdown(cell)}</th>`).join("")}</tr></thead><tbody>${rows.map((row) => `<tr>${row.map((cell) => `<td>${inlineMarkdown(cell)}</td>`).join("")}</tr>`).join("")}</tbody></table>`);
      continue;
    }
    if (/^\s*>/.test(line)) {
      flushParagraph();
      const quote = [];
      while (index < lines.length && /^\s*>/.test(lines[index])) quote.push(lines[index++].replace(/^\s*>\s?/, ""));
      index--;
      html.push(`<blockquote><p>${inlineMarkdown(quote.join(" "))}</p></blockquote>`);
      continue;
    }
    if (/^\s*[-+*]\s+/.test(line)) {
      flushParagraph();
      const items = [];
      while (index < lines.length && /^\s*[-+*]\s+/.test(lines[index])) items.push(lines[index++].replace(/^\s*[-+*]\s+/, ""));
      index--;
      html.push(`<ul>${items.map((item) => `<li>${inlineMarkdown(item)}</li>`).join("")}</ul>`);
      continue;
    }
    if (/^\s*\d+[.)]\s+/.test(line)) {
      flushParagraph();
      const items = [];
      while (index < lines.length && /^\s*\d+[.)]\s+/.test(lines[index])) items.push(lines[index++].replace(/^\s*\d+[.)]\s+/, ""));
      index--;
      html.push(`<ol>${items.map((item) => `<li>${inlineMarkdown(item)}</li>`).join("")}</ol>`);
      continue;
    }
    if (!line.trim()) flushParagraph();
    // An over-long heading reaches here instead of the heading branch above, and
    // printing its `##` markers in front of the prose is worse than the prose.
    // Conditional on it BEING one: `#nofilter` in a sentence is not a heading and
    // must keep its hash.
    else paragraph.push(demotedHeading(line).trim());
  }
  flushParagraph();
  return { html: html.join("\n"), headings };
}

// `options.original` opens the source-language file of a translated reference.
// Everything else about the view is identical - it is the same preserved
// document, in the words the author wrote it in.
async function openReader(item, options = {}) {
  const showOriginal = Boolean(options.original && item?.originalMdPath);
  const readerPath = showOriginal ? item.originalMdPath : item?.mdPath;
  if (!readerPath) return;
  const markdownUrl = archiveUrl(readerPath, "md", item?.mdVersion);
  if (!markdownUrl) return toast("This Markdown path did not pass validation");
  const requestToken = ++readerRequestToken;
  const originalUrl = safeExternalUrl(item.originalUrl);
  state.readerItem = item;
  state.readerOriginal = showOriginal;
  const dialog = $("#reader-dialog");
  const scroll = $("#reader-scroll");
  $("#reader-title").textContent = item.title;
  const languageNote = !item.translated
    ? "preserved Markdown"
    : showOriginal
      ? `original ${item.language || "source"} text`
      : "English translation";
  $("#reader-kicker").textContent = `${yearLabel(item.year)} / ${creditOf(item) || item.topic} / ${languageNote}`;
  $("#reader-content").innerHTML = `<div class="reader-loading"><i></i><p>Opening preserved Markdown…</p></div>`;
  $("#reader-toc").innerHTML = "";
  $("#reader-progress-bar").style.width = "0";
  // The switch to the other view of the same document leads, and sits in the
  // same first position in the PDF viewer, so one place on the toolbar always
  // moves between Markdown and PDF.
  $("#reader-actions").innerHTML = `
    ${item.pdfPath ? `<button id="reader-open-pdf" type="button">▧ PDF</button>` : ""}
    <button class="reading-theme-toggle" id="reader-theme-toggle" type="button" aria-label="Switch to light reading theme">☀ Light</button>
    <button id="reader-share" type="button" title="Share this exact Markdown view">⌁ Share</button>
    <button id="reader-read-toggle" type="button" aria-pressed="${item.read}">${item.read ? "✓ Read" : "○ Mark as read"}</button>
    <button id="reader-favourite-toggle" type="button" aria-pressed="${item.favourite}">${item.favourite ? "★ Favourite" : "☆ Add favourite"}</button>
    <a href="${h(markdownUrl)}" target="_blank" rel="noopener noreferrer">Raw MD</a>
    ${item.originalMdPath ? `<button id="reader-language-toggle" type="button">${showOriginal ? "⇄ English" : `⇄ ${h(item.language ? item.language.toUpperCase() : "Original language")}`}</button>` : ""}
    ${originalUrl ? `<a href="${h(originalUrl)}" target="_blank" rel="noopener noreferrer">Original ↗</a>` : `<span class="disabled">Original blocked</span>`}`;
  $("#reader-theme-toggle").addEventListener("click", toggleReadingTheme);
  $("#reader-share").addEventListener("click", () => shareDocument(item, "reader"));
  $("#reader-read-toggle").addEventListener("click", () => setReadState(item));
  $("#reader-favourite-toggle").addEventListener("click", () => setFavouriteState(item));
  $("#reader-open-pdf")?.addEventListener("click", () => openPdfViewer(item));
  $("#reader-language-toggle")?.addEventListener("click", () => openReader(item, { original: !showOriginal }));
  applyReadingTheme();
  if ($("#artifact-dialog").open) $("#artifact-dialog").close();
  if ($("#pdf-dialog").open) $("#pdf-dialog").close();
  syncDocumentUrl(item, "reader");
  if (!dialog.open) dialog.showModal();
  scroll.scrollTop = 0;

  try {
    const response = await fetch(markdownUrl, { credentials: "same-origin", cache: "default" });
    if (!response.ok) throw new Error(`Markdown returned ${response.status}`);
    const advertisedSize = Number(response.headers.get("content-length") || 0);
    if (advertisedSize > 8_000_000) throw new Error("Markdown exceeds the safe reader size limit");
    const markdown = await response.text();
    if (markdown.length > 8_000_000) throw new Error("Markdown exceeds the safe reader size limit");
    if (requestToken !== readerRequestToken || state.readerItem !== item) return;
    const documentView = markdownDocument(markdown);
    $("#reader-content").innerHTML = `<div class="archive-warning">Safe reader mode: third-party HTML is escaped, scripts cannot run, and external links and images require a separate click.</div>${documentView.html}`;
    $("#reader-toc").innerHTML = documentView.headings.slice(0, 40).map((heading) => `<button class="${heading.level > 2 ? "sub" : ""}" data-reader-target="${h(heading.slug)}">${h(short(heading.title, 52))}</button>`).join("");
  } catch (error) {
    if (requestToken !== readerRequestToken) return;
    $("#reader-content").innerHTML = `<div class="empty-state"><p>The preserved Markdown could not be opened.</p><small>${h(error.message)}</small></div>`;
  }
}

function empty(message) {
  return `<div class="empty-state"><p>${h(message)}</p></div>`;
}

let toastTimer;
function toast(message) {
  const element = $("#toast");
  element.textContent = message;
  element.classList.add("show");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => element.classList.remove("show"), 1900);
}

loadArchive();
