#!/usr/bin/env node
/**
 * Stage one dependency-free static site for GitHub Pages or Cloudflare Pages.
 * Only archive documents referenced by generated collection shards are copied.
 */

import { promises as fs } from "node:fs";
import path from "node:path";
import process from "node:process";
import { fileURLToPath } from "node:url";

const APP_DIR = path.dirname(fileURLToPath(import.meta.url));
const REPO = path.dirname(APP_DIR);
const STATIC_FILES = [
  ".nojekyll",
  "_headers",
  "app.js",
  "brand-mark.svg",
  "constellation.js",
  "index.html",
  "robots.txt",
  "site.webmanifest",
  "sitemap.xml",
  "styles.css"
];
const GITHUB_INDEX = `<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>Web Hack List file origin</title></head>
<body><main><h1>Web Hack List file origin</h1><p>This GitHub Pages project serves only oversized preserved files for <a href="https://webhacklist.com/">webhacklist.com</a>.</p></main></body>
</html>
`;

function parseArguments() {
  const args = process.argv.slice(2);
  const targetIndex = args.indexOf("--target");
  const outputIndex = args.indexOf("--output");
  const target = targetIndex >= 0 ? args[targetIndex + 1] : "cloudflare";
  const outputName = outputIndex >= 0 ? args[outputIndex + 1] : target === "github" ? "_site" : "dist";
  const consumed = new Set();
  if (targetIndex >= 0) { consumed.add(targetIndex); consumed.add(targetIndex + 1); }
  if (outputIndex >= 0) { consumed.add(outputIndex); consumed.add(outputIndex + 1); }
  const unknown = args.filter((_, index) => !consumed.has(index));
  if (!new Set(["cloudflare", "github"]).has(target)) throw new Error("--target must be cloudflare or github");
  if (!new Set(["dist", "_site"]).has(outputName)) throw new Error("--output must be dist or _site");
  if (unknown.length) throw new Error(`unknown argument(s): ${unknown.join(", ")}`);
  return { target, output: path.join(REPO, outputName) };
}

async function readJson(file) {
  return JSON.parse(await fs.readFile(file, "utf8"));
}

function validateRelative(relative) {
  if (typeof relative !== "string" || !relative || path.isAbsolute(relative) || relative.includes("\\") || relative.split("/").includes("..")) {
    throw new Error(`unsafe staged path: ${relative}`);
  }
  return relative;
}

// A translated reference publishes BOTH files: the English one the reader opens
// and the source-language original it was made from. Staging only the served
// path would leave the app's "Original language" action pointing at a 404.
function archivePaths(items) {
  const paths = new Set();
  const add = (holder) => {
    for (const archivePath of [holder?.mdPath, holder?.pdfPath, holder?.originalMdPath, holder?.originalPdfPath]) {
      if (archivePath) paths.add(validateRelative(archivePath));
    }
  };
  for (const item of items) {
    add(item);
    for (const link of item?.links || []) add(link);
  }
  return paths;
}

function manifestFaultPaths(manifest) {
  const faults = new Map();
  for (const record of Object.values(manifest?.urls || {})) {
    if (!record || typeof record !== "object" || !String(record.content_gap || "").includes("faulty capture:")) continue;
    for (const archivePath of [record.steps?.render?.file, record.steps?.pdf?.file]) {
      if (archivePath) faults.set(archivePath, record.content_gap);
    }
  }
  return faults;
}

async function listFiles(directory, prefix = "") {
  const result = [];
  for (const entry of await fs.readdir(directory, { withFileTypes: true })) {
    const relative = prefix ? `${prefix}/${entry.name}` : entry.name;
    if (entry.isDirectory()) result.push(...await listFiles(path.join(directory, entry.name), relative));
    else if (entry.isFile()) result.push(relative);
    else throw new Error(`refusing to stage non-regular file: ${path.join(directory, relative)}`);
  }
  return result;
}

async function main() {
  const { target, output } = parseArguments();
  const [catalogue, manifest] = await Promise.all([
    readJson(path.join(APP_DIR, "data", "catalogue.json")),
    readJson(path.join(REPO, "archived-references", "manifest.json"))
  ]);
  if (catalogue?.schema !== 1 || !Array.isArray(catalogue.years) || catalogue.hosting?.schema !== 1) {
    throw new Error("generated catalogue is missing or invalid; run node website/build-data.mjs first");
  }

  const assetLimit = Number(catalogue.hosting.cloudflareMaxAssetBytes);
  const largeFallbacks = catalogue.hosting.largePdfFallbacks || {};
  const faults = manifestFaultPaths(manifest);
  const archive = new Set();
  for (const year of catalogue.years) {
    const shard = await readJson(path.join(APP_DIR, year.file));
    if (shard?.version !== catalogue.version || shard?.collection?.id !== year.id || !Array.isArray(shard.items)) {
      throw new Error(`${year.file} does not match catalogue ${catalogue.version}`);
    }
    archivePaths(shard.items).forEach((archivePath) => archive.add(archivePath));
  }

  const tasks = [];
  if (target === "github") {
    // GitHub Pages is deliberately a small file origin, not a duplicate site.
    // Cloudflare owns the full archive; only its explicitly registered
    // over-limit files are published here.
    tasks.push({ source: path.join(APP_DIR, ".nojekyll"), relative: ".nojekyll", required: true });
    for (const archivePath of Object.keys(largeFallbacks).sort()) {
      validateRelative(archivePath);
      if (!archive.has(archivePath)) throw new Error(`GitHub fallback is not referenced by generated data: ${archivePath}`);
      tasks.push({ source: path.join(REPO, archivePath), relative: archivePath, required: true });
    }
  } else {
    for (const filename of STATIC_FILES) tasks.push({ source: path.join(APP_DIR, filename), relative: filename, required: true });
    for (const filename of await listFiles(path.join(APP_DIR, "data"))) {
      tasks.push({ source: path.join(APP_DIR, "data", filename), relative: `data/${filename}`, required: true });
    }
    for (const archivePath of [...archive].sort()) {
      tasks.push({ source: path.join(REPO, archivePath), relative: archivePath, required: false });
    }
    for (const filename of (await fs.readdir(path.join(REPO, "original-listings"))).filter((name) => name.endsWith(".pdf")).sort()) {
      tasks.push({ source: path.join(REPO, "original-listings", filename), relative: `original-listings/${filename}`, required: true });
    }
  }

  await fs.rm(output, { recursive: true, force: true });
  await fs.mkdir(output, { recursive: true });
  const skippedLarge = [];
  const skippedFaults = [];
  let totalBytes = 0;
  let fileCount = 0;
  if (target === "github") {
    await fs.writeFile(path.join(output, "index.html"), GITHUB_INDEX, "utf8");
    totalBytes += Buffer.byteLength(GITHUB_INDEX);
    fileCount++;
  }
  for (const task of tasks) {
    validateRelative(task.relative);
    let stat;
    try {
      stat = await fs.lstat(task.source);
    } catch (error) {
      if (error.code === "ENOENT" && !task.required && faults.has(task.relative)) {
        skippedFaults.push(task.relative);
        continue;
      }
      throw new Error(`staged source is missing: ${task.relative}`);
    }
    if (!stat.isFile()) throw new Error(`staged source is not a regular file: ${task.relative}`);
    if (target === "cloudflare" && stat.size > assetLimit) {
      if (!Object.hasOwn(largeFallbacks, task.relative)) {
        throw new Error(`${task.relative} is ${stat.size} bytes, over Cloudflare's ${assetLimit}-byte limit, and has no configured fallback`);
      }
      skippedLarge.push(task.relative);
      continue;
    }
    const destination = path.join(output, task.relative);
    await fs.mkdir(path.dirname(destination), { recursive: true });
    await fs.copyFile(task.source, destination);
    totalBytes += stat.size;
    fileCount++;
  }

  if (target === "cloudflare" && fileCount > 20000) throw new Error(`Cloudflare free-site file limit exceeded: ${fileCount} files`);
  if (target === "github" && totalBytes >= 1_000_000_000) throw new Error(`GitHub Pages site-size limit exceeded: ${totalBytes} bytes`);
  console.log(`${target} site staged in ${path.relative(REPO, output)}/: ${fileCount} files, ${totalBytes} bytes`);
  if (skippedLarge.length) console.log(`large PDFs delegated to GitHub Pages: ${skippedLarge.join(", ")}`);
  if (skippedFaults.length) console.warn(`filed faulty captures omitted: ${skippedFaults.length} (${skippedFaults.join(", ")})`);
}

main().catch((error) => {
  console.error(`build-site failed: ${error.stack || error.message}`);
  process.exitCode = 1;
});
