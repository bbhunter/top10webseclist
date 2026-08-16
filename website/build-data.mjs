#!/usr/bin/env node
/**
 * Build the progressive web-app catalogue from the canonical year lists and
 * reference manifest. The browser consumes these files; it never needs to
 * download the multi-megabyte manifest or parse every collection at startup.
 */

import { createHash } from "node:crypto";
import { promises as fs } from "node:fs";
import path from "node:path";
import process from "node:process";
import vm from "node:vm";
import { fileURLToPath } from "node:url";

const APP_DIR = path.dirname(fileURLToPath(import.meta.url));
const REPO = path.dirname(APP_DIR);
const REGISTRY_PATH = path.join(APP_DIR, "archive-years.json");
const HOSTING_PATH = path.join(APP_DIR, "hosting.json");
const MANIFEST_PATH = path.join(REPO, "archived-references", "manifest.json");
const VOCABULARY_PATH = path.join(REPO, "archived-references", "tag-vocabulary.json");
const OUTPUT_DIR = path.join(APP_DIR, "data");
const COLLECTIONS_DIR = path.join(OUTPUT_DIR, "collections");
const ID_PATTERN = /^\d{4}(?:-\d{2}|-ai)?$/;

function stableJson(value) {
  return JSON.stringify(value);
}

function hash(value) {
  return createHash("sha256").update(value).digest("hex");
}

async function readJson(file) {
  return JSON.parse(await fs.readFile(file, "utf8"));
}

async function atomicWrite(file, contents) {
  const temporary = `${file}.tmp-${process.pid}`;
  await fs.writeFile(temporary, contents, "utf8");
  await fs.rename(temporary, file);
}

/**
 * technique tag -> the OWASP Top 10 category tags it earns.
 *
 * Derived from the vocabulary rather than restated, so editing the mapping in
 * archived-references/tag-vocabulary.json is the only place it has to change.
 */
function owaspMap(vocabulary) {
  const map = Object.create(null);
  for (const category of vocabulary?.owasp?.categories || []) {
    const id = String(category?.id || "");
    if (!id) continue;
    const label = `owasp-${id.replace(":", "-").toLowerCase()}`;
    for (const tag of category?.tags || []) {
      const key = String(tag || "").trim().toLowerCase();
      if (!key) continue;
      if (!Object.hasOwn(map, key)) map[key] = [];
      if (!map[key].includes(label)) map[key].push(label);
    }
  }
  return map;
}

function parserContext(appSource, registry, manifest, owasp) {
  const storage = new Map();
  const context = vm.createContext({
    URL,
    console,
    location: { href: "http://archive.invalid/website/", search: "", hash: "" },
    localStorage: {
      getItem: (key) => storage.get(key) ?? null,
      setItem: (key, value) => storage.set(key, String(value))
    },
    __registry: registry,
    __manifest: manifest,
    // The OWASP mapping is passed IN rather than restated here. It is a
    // maintainer's judgement kept in archived-references/tag-vocabulary.json,
    // and a second copy in JavaScript would drift from it silently.
    __owasp: owasp
  });
  const parserSource = appSource.replace(/\nloadArchive\(\);\s*$/, "\n");
  if (parserSource === appSource) throw new Error("could not isolate app parser from its browser boot call");
  vm.runInContext(parserSource, context, { filename: "app.js" });
  vm.runInContext(`
    YEAR_RECORDS = __registry.years;
    YEAR_FILES = YEAR_RECORDS.map((record) => record.id);
    globalThis.__recordLookup = new Map();
    Object.entries(__manifest.urls || {}).forEach(([url, record]) => {
      if (!record || typeof record !== "object") return;
      const spellings = Array.isArray(record.spellings) ? record.spellings : [];
      const alsoAt = Array.isArray(record.also_at) ? record.also_at : [];
      const aliases = [url, ...spellings, record.health?.final_url, ...alsoAt]
        .map(safeExternalUrl).filter(Boolean);
      aliases.forEach((alias) => __recordLookup.set(normalizeUrl(alias), record));
    });
  `, context, { filename: "build-data-bootstrap.js" });
  return context;
}

function collectionSummary(record, items) {
  const topicCounts = {};
  for (const item of items) topicCounts[item.topic] = (topicCounts[item.topic] || 0) + 1;
  return {
    ...record,
    file: `data/collections/${record.id}.json`,
    count: items.length,
    winners: items.filter((item) => item.section === "winner").length,
    archived: items.filter((item) => item.archived).length,
    markdown: items.filter((item) => item.mdPath).length,
    pdf: items.filter((item) => item.pdfPath).length,
    topicCounts
  };
}

async function main() {
  const checkOnly = process.argv.slice(2).includes("--check");
  const unknownArgs = process.argv.slice(2).filter((argument) => argument !== "--check");
  if (unknownArgs.length) throw new Error(`unknown argument(s): ${unknownArgs.join(", ")}`);
  const [registry, hosting, manifest, appSource, vocabulary] = await Promise.all([
    readJson(REGISTRY_PATH),
    readJson(HOSTING_PATH),
    readJson(MANIFEST_PATH),
    fs.readFile(path.join(APP_DIR, "app.js"), "utf8"),
    readJson(VOCABULARY_PATH)
  ]);
  if (registry?.schema !== 1 || !Array.isArray(registry.years) || !registry.years.length) {
    throw new Error("archive-years.json must contain a non-empty schema-1 years array");
  }
  const ids = registry.years.map((record) => record?.id);
  if (ids.some((id) => typeof id !== "string" || !ID_PATTERN.test(id)) || new Set(ids).size !== ids.length) {
    throw new Error("archive-years.json contains an invalid or duplicate collection id");
  }
  if (hosting?.schema !== 1 || !Number.isSafeInteger(hosting.cloudflareMaxAssetBytes) || hosting.cloudflareMaxAssetBytes < 1 || !hosting.largePdfFallbacks || typeof hosting.largePdfFallbacks !== "object") {
    throw new Error("hosting.json must contain a schema-1 Cloudflare asset limit and fallback map");
  }
  for (const [archivePath, fallbackUrl] of Object.entries(hosting.largePdfFallbacks)) {
    if (!/^archived-references\/pdf\/[a-z0-9-]+\/[a-z0-9._-]+\.pdf$/i.test(archivePath) || !/^https:\/\/irsdl\.github\.io\/webhacklist\/archived-references\/pdf\//i.test(fallbackUrl)) {
      throw new Error(`hosting.json contains an invalid large-PDF fallback: ${archivePath}`);
    }
  }

  const context = parserContext(appSource, registry, manifest, owaspMap(vocabulary));
  const parsed = [];
  for (const record of registry.years) {
    context.__year = record.id;
    context.__markdown = await fs.readFile(path.join(REPO, `${record.id}.md`), "utf8");
    const items = vm.runInContext(
      "parseYearMarkdown(__markdown, __year, __recordLookup, yearRecordFor(__year))",
      context,
      { filename: `${record.id}.md.parser.js` }
    );
    const portableItems = JSON.parse(JSON.stringify(items));
    parsed.push({ record, items: portableItems, summary: collectionSummary(record, portableItems) });
  }

  const contentFingerprint = stableJson({ parsed: parsed.map(({ record, items }) => ({ record, items })), hosting });
  const version = hash(contentFingerprint).slice(0, 20);
  const manifestCount = Object.keys(manifest?.urls || {}).length;
  const generated = new Date().toISOString();

  const expectedFiles = new Set();
  const shardBodies = new Map();
  for (const collection of parsed) {
    const shard = {
      schema: 1,
      version,
      collection: collection.record,
      count: collection.items.length,
      items: collection.items
    };
    const body = `${stableJson(shard)}\n`;
    const filename = `${collection.record.id}.json`;
    expectedFiles.add(filename);
    shardBodies.set(filename, body);
    collection.summary.bytes = Buffer.byteLength(body);
    collection.summary.sha256 = hash(body);
  }

  const catalogue = {
    schema: 1,
    version,
    generated,
    manifestCount,
    total: parsed.reduce((sum, collection) => sum + collection.items.length, 0),
    source: {
      registry: "archive-years.json",
      manifest: "archived-references/manifest.json"
    },
    hosting,
    years: parsed.map((collection) => collection.summary)
  };
  const catalogueBody = `${stableJson(catalogue)}\n`;

  if (checkOnly) {
    const actualCatalogue = await readJson(path.join(OUTPUT_DIR, "catalogue.json"));
    const comparableCatalogue = { ...catalogue, generated: actualCatalogue.generated };
    if (stableJson(actualCatalogue) !== stableJson(comparableCatalogue)) {
      throw new Error("progressive catalogue is stale; run node website/build-data.mjs");
    }
    const actualFiles = (await fs.readdir(COLLECTIONS_DIR, { withFileTypes: true }))
      .filter((entry) => entry.isFile() && entry.name.endsWith(".json"))
      .map((entry) => entry.name);
    if (actualFiles.length !== expectedFiles.size || actualFiles.some((filename) => !expectedFiles.has(filename))) {
      throw new Error("progressive collection file set is stale; run node website/build-data.mjs");
    }
    for (const [filename, body] of shardBodies) {
      if (await fs.readFile(path.join(COLLECTIONS_DIR, filename), "utf8") !== body) {
        throw new Error(`${filename} is stale; run node website/build-data.mjs`);
      }
    }
  } else {
    await fs.mkdir(COLLECTIONS_DIR, { recursive: true });
    for (const [filename, body] of shardBodies) await atomicWrite(path.join(COLLECTIONS_DIR, filename), body);

    // Collection files are generated output. Prune only stale JSON shards inside
    // this dedicated directory when a registry entry is deliberately removed.
    for (const entry of await fs.readdir(COLLECTIONS_DIR, { withFileTypes: true })) {
      if (entry.isFile() && entry.name.endsWith(".json") && !expectedFiles.has(entry.name)) {
        await fs.unlink(path.join(COLLECTIONS_DIR, entry.name));
      }
    }
    await atomicWrite(path.join(OUTPUT_DIR, "catalogue.json"), catalogueBody);
  }

  const shardBytes = parsed.reduce((sum, collection) => sum + collection.summary.bytes, 0);
  console.log(`progressive catalogue ${version}: ${catalogue.total} records in ${parsed.length} collection(s), ${shardBytes} shard bytes${checkOnly ? " (fresh)" : ""}`);
}

main().catch((error) => {
  console.error(`build-data failed: ${error.stack || error.message}`);
  process.exitCode = 1;
});
