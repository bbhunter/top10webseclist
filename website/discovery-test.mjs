// Functional and popup tests against the real local archive. No external requests
// are needed: the mobile PDF checks reproduce production origins with local files.
import assert from "node:assert/strict";
import { readFile, stat } from "node:fs/promises";
import path from "node:path";
import {launchBrowser} from "./browser-test.mjs";
const browser = await launchBrowser();
const url = process.env.WEBSEC_TEST_URL || "http://127.0.0.1:8000/website/";
const views = ["desk", "time"];
const errors = [];
const context = await browser.newContext({ viewport: { width: 1440, height: 1000 } });
const page = await context.newPage();
page.on("pageerror", (error) => errors.push(error.message));
page.on("console", (message) => { if (message.type() === "error") errors.push(`${message.text()} (${message.location().url})`); });
const action = (name, value) => `[data-discovery-action="${name}"]${value === undefined ? "" : `[data-discovery-value="${value}"]`}`;
async function go(view) {
  await page.goto(`${url}#${view}`);
  await page.waitForSelector(".discovery-record");
  await page.waitForFunction(() => !document.querySelector("#boot-screen"));
}
async function closeDialog(id) {
  await page.evaluate((id) => new Promise((resolve) => {
    const dialog = document.getElementById(id);
    if (!dialog.open) return resolve();
    dialog.addEventListener("close", resolve, { once: true });
    dialog.close();
  }), id);
}
async function displayedItems(selector = "[data-discovery-record]") {
  return page.locator(selector).evaluateAll((elements) => elements.map((element) => {
    const item = state.items.find((item) => item.id === element.dataset.discoveryRecord);
    return { id: item.id, year: item.year, topic: item.topic, rank: item.rank, preliminary: item.preliminary, read: item.read, favourite: item.favourite };
  }));
}
try {
  for (const view of views) {
    await go(view);
    assert.equal(await page.locator(".nav-item[aria-current=page]").getAttribute("data-view"), view);
    if (view === "desk") await page.selectOption("#desk-video", "with");
    const markers = await page.locator("[data-discovery-record]").evaluateAll((cards) => cards.map((card) => {
      const item = state.items.find((item) => item.id === card.dataset.discoveryRecord);
      const confirmed = item.videos?.some((video) => video.confidence === "confirmed");
      const badge = card.querySelector(".record-video");
      return { hasVideo:Boolean(item.videos?.length), hasBadge:Boolean(badge), potential:badge?.classList.contains("is-potential") || false, expectedPotential:Boolean(item.videos?.length) && !confirmed, label:card.querySelector("[data-artifact]").getAttribute("aria-label") };
    }));
    assert.ok(markers.some((item) => item.hasVideo), `${view} has recorded fixtures`);
    assert.ok(markers.every((item) => item.hasBadge === item.hasVideo && item.potential === item.expectedPotential));
    assert.ok(markers.filter((item) => item.hasVideo).every((item) => item.label.includes("recording")));
  }
  await go("desk");
  assert.equal(await page.locator("[data-discovery-record]").count(), 20);
  const firstPage = await displayedItems();
  await page.locator(action("desk-next")).click();
  const secondPage = await displayedItems();
  assert.equal(secondPage.length, 20);
  assert.ok(secondPage.every((item) => !firstPage.some((first) => first.id === item.id)));
  await page.locator(action("desk-prev")).click();
  assert.deepEqual(await displayedItems(), firstPage);
  await page.selectOption("#desk-video", "with");
  assert.equal(await page.locator(".discovery-record .record-video").count(), await page.locator(".discovery-record").count());
  assert.equal(await page.evaluate(() => deskFilteredRecords().length), await page.evaluate(() => state.items.filter((item) => item.videos?.length).length));
  await page.locator(action("desk-next")).click();
  assert.equal(await page.locator(".discovery-record .record-video").count(), await page.locator(".discovery-record").count());
  await page.selectOption("#desk-video", "without");
  assert.equal(await page.locator(".discovery-record .record-video").count(), 0);
  await page.locator(action("desk-reset")).click();
  assert.equal(await page.locator("#desk-video").inputValue(), "all");
  await page.selectOption("#desk-year", "2024");
  await page.selectOption("#desk-standing", "winner");
  assert.equal(await page.locator("[data-discovery-record]").count(), 10);
  assert.ok((await displayedItems()).every((item) => item.year === "2024" && item.rank));
  await page.selectOption("#desk-video", "with");
  const combined = await page.evaluate(() => deskFilteredRecords());
  assert.ok(combined.length && combined.every((item) => item.year === "2024" && item.rank && item.videos?.length));
  await page.selectOption("#desk-topic", "HTTP");
  assert.ok((await displayedItems()).every((item) => item.topic === "HTTP"));
  await page.locator("#desk-query").fill("no-such-research-theme-regression");
  assert.equal(await page.locator("[data-discovery-record]").count(), 0);
  await page.locator(action("desk-reset")).click();
  await page.locator("#desk-author").fill("James Kettle");
  assert.ok(await page.locator("[data-discovery-record]").count());
  assert.ok((await page.locator(".discovery-credit").allTextContents()).every((text) => text.includes("James Kettle")));
  await page.locator(action("desk-reset")).click();
  await page.selectOption("#desk-sort", "title");
  const titles = await page.locator(".discovery-record h3").allTextContents();
  // ICU versions collate punctuation differently. Compare with the reader's
  // browser locale, rather than Node's separate collation implementation.
  assert.deepEqual(titles, await page.evaluate(titles => [...titles].sort((a, b) => a.localeCompare(b)), titles));
  await page.locator(action("desk-compact")).click();
  assert.equal(await page.locator(".discovery-summary:visible").count(), 0);
  const savedId = (await displayedItems())[0].id;
  await page.locator(`[data-favourite="${savedId}"]`).click();
  await page.locator(action("mark", savedId)).click();
  await page.selectOption("#desk-read", "read");
  assert.ok((await displayedItems()).every((item) => item.read));
  assert.ok((await displayedItems()).some((item) => item.id === savedId && item.favourite));
  await go("desk");
  assert.ok(await page.evaluate((id) => state.items.some((item) => item.id === id && item.read && item.favourite), savedId));
  console.log("Desk: pagination, combined filters, author search, sorting, video filtering and badges, empty/reset, density, and saved/read persistence pass");

  await go("time");
  assert.equal(await page.locator(".time-stop").first().getAttribute("id"), "time-2006");
  await page.selectOption("#time-order", "newest");
  assert.equal(await page.locator(".time-stop").first().getAttribute("id"), "time-2026-ai");
  await page.selectOption("#time-topic", "Crypto");
  assert.ok((await displayedItems()).every((item) => item.topic === "Crypto"));
  await page.selectOption("#time-jump", "2016-17");
  assert.equal(await page.evaluate(() => document.activeElement.id), "time-2016-17");
  assert.equal(new URL(page.url()).hash, "#time");
  await page.selectOption("#time-topic", "all");
  await page.locator(action("time-expand", "2025")).click();
  assert.equal(await page.locator("#time-2025 [data-discovery-record]").count(), await page.evaluate(() => state.items.filter((item) => item.year === "2025").length));
  await page.locator(action("time-expand", "2025")).click();
  assert.equal(await page.locator("#time-2025 [data-discovery-record]").count(), 3);
  console.log("Time Machine: chronology, subject comparisons, year jumps, expansion and collapse pass");

  for (const view of views) {
    await go(view);
    for (const theme of ["light", "dark"]) {
      await page.locator(action("theme", theme)).click();
      const palette = await page.evaluate(() => ({ accent:getComputedStyle(document.documentElement).getPropertyValue("--view-accent").trim(), paper:getComputedStyle(document.body).backgroundColor }));
      await page.locator(".discovery-record [data-artifact]").first().click();
      await page.waitForSelector("#artifact-dialog[open]");
      assert.deepEqual(await page.locator("#artifact-dialog").evaluate((dialog) => ({accent:getComputedStyle(dialog).getPropertyValue("--dialog-theme").trim(),paper:getComputedStyle(dialog).backgroundColor})), palette);
      await page.locator("#report-inaccuracy").click();
      assert.deepEqual(await page.locator("#report-dialog").evaluate((dialog) => ({accent:getComputedStyle(dialog).getPropertyValue("--dialog-theme").trim(),paper:getComputedStyle(dialog).backgroundColor})), palette);
      await closeDialog("report-dialog");
      await closeDialog("artifact-dialog");
      await page.locator(".topbar [data-contribute]").click();
      assert.deepEqual(await page.locator("#contribute-dialog").evaluate((dialog) => ({accent:getComputedStyle(dialog).getPropertyValue("--dialog-theme").trim(),paper:getComputedStyle(dialog).backgroundColor})), palette);
      await closeDialog("contribute-dialog");
      await page.locator("#global-search").fill("cache");
      assert.equal(await page.locator("#global-results").evaluate((element) => getComputedStyle(element).backgroundColor), await page.evaluate(() => getComputedStyle(document.documentElement).getPropertyValue("--panel").trim()).then((color) => page.evaluate((color) => { const el=document.createElement("span"); el.style.color=color; document.body.append(el); const rgb=getComputedStyle(el).color; el.remove(); return rgb; }, color)));
      await page.locator("#close-global-results").click();
    }
    await page.reload();
    await page.waitForSelector(".discovery-record");
    assert.equal(await page.locator("html").getAttribute("data-discovery-theme"), "dark");
    await page.setViewportSize({width:390,height:844});
    await page.locator("#mobile-menu").click();
    await page.locator(`.nav-item[data-view="${view}"]`).click();
    assert.equal(await page.locator("#mobile-menu").getAttribute("aria-expanded"), "false");
    await page.setViewportSize({width:1440,height:1000});
  }
  console.log("Overlays: record/report/submission/search palettes match all 4 page palettes; appearance persistence and mobile navigation pass");

  await go("time");
  const shared = await page.evaluate(() => {
    state.readingTheme = "light";
    const item = state.items.find((item) => item.mdPath);
    return {url:documentShareUrl(item, "reader"),title:item.title};
  });
  await page.goto(shared.url);
  await page.waitForSelector("#reader-dialog[open] .archive-warning");
  assert.equal(await page.locator("#reader-title").innerText(), shared.title);
  assert.equal(await page.locator("#reader-dialog").getAttribute("data-reading-theme"), "light");
  assert.equal(await page.locator("html").getAttribute("data-view"), "time");
  await closeDialog("reader-dialog");
  const recoveryContext = await browser.newContext();
  let failCollection = true;
  await recoveryContext.route("**/data/collections/2024.json*", (route) => failCollection
    ? route.fulfill({status:503,body:"Simulated temporary failure"}) : route.continue());
  const recovery = await recoveryContext.newPage();
  await recovery.goto(`${url}#desk`);
  await recovery.waitForSelector('[data-discovery-action="retry"]');
  failCollection = false;
  await recovery.locator('[data-discovery-action="retry"]').click();
  await recovery.waitForSelector(".discovery-record");
  assert.equal(await recovery.locator('[data-discovery-action="retry"]').count(), 0);
  await recoveryContext.close();
  console.log("Resilience: shared readers restore the view/theme and a failed collection recovers through Retry");

  // Use the real files and production origin rules to exercise the isolated PDF
  // reader entirely offline, including theme messages between frame and parent.
  const offline = await browser.newContext({viewport:{width:390,height:844}});
  const root = process.cwd();
  const mime = {".html":"text/html", ".js":"text/javascript", ".mjs":"text/javascript", ".json":"application/json", ".css":"text/css", ".svg":"image/svg+xml", ".pdf":"application/pdf", ".md":"text/plain", ".wasm":"application/wasm", ".bcmap":"application/octet-stream"};
  await offline.route("**/*", async (route) => {
    const request = new URL(route.request().url());
    if (!["webhacklist.com", "irsdl.github.io"].includes(request.hostname)) return route.abort();
    let relative = decodeURIComponent(request.pathname).replace(/^\/webhacklist\//, "").replace(/^\//, "");
    if (!relative) relative = "index.html";
    const file = path.resolve(root, /^(archived-references|original-listings)\//.test(relative) ? relative : `website/${relative}`);
    if (!file.startsWith(`${root}${path.sep}`)) return route.abort();
    try {
      const body = await readFile(file);
      await route.fulfill({status:200,contentType:mime[path.extname(file)] || "application/octet-stream",headers:{"access-control-allow-origin":"*"},body});
    } catch { await route.fulfill({status:404,body:"Local test file not found"}); }
  });
  const mobile = await offline.newPage();
  mobile.on("pageerror", (error) => errors.push(error.message));
  mobile.on("console", (message) => { if (message.type() === "error") errors.push(`${message.text()} (${message.location().url})`); });
  await mobile.goto("https://webhacklist.com/#desk");
  await mobile.waitForSelector(".discovery-record");
  const candidates = await mobile.evaluate(() => state.items.filter((item) => item.pdfPath && item.mdPath).map((item) => ({id:item.id,pdfPath:item.pdfPath})));
  const sizes = await Promise.all(candidates.map(async (item) => ({...item,size:(await stat(path.join(root,item.pdfPath))).size})));
  const small = sizes.sort((a,b) => a.size-b.size)[0];
  for (const view of views) {
    await mobile.evaluate((view) => setView(view), view);
    await mobile.evaluate((id) => openPdfViewer(state.items.find((item) => item.id === id)), small.id);
    await mobile.waitForFunction(() => document.querySelector("#pdf-frame")?.contentWindow && !document.querySelector("#pdf-frame").hidden);
    const frame = mobile.frameLocator("#pdf-frame");
    try { await frame.locator("canvas").first().waitFor({state:"visible"}); }
    catch (error) { console.log(await frame.locator("body").innerText()); throw error; }
    assert.equal(await frame.locator("html").getAttribute("data-palette"), view);
    await mobile.locator("#pdf-theme-toggle").click();
    await frame.locator('html[data-theme="light"]').waitFor();
    await mobile.locator("#pdf-open-markdown").click();
    await mobile.waitForSelector("#reader-content .archive-warning");
    assert.equal(await mobile.locator("#reader-dialog").getAttribute("data-reading-theme"), "light");
    await mobile.locator("#reader-theme-toggle").click();
    await mobile.evaluate(() => new Promise((resolve) => { const dialog=document.querySelector("#reader-dialog"); dialog.addEventListener("close",resolve,{once:true}); dialog.close(); }));
  }
  await offline.close();
  console.log("Documents: real PDF rendering in an isolated mobile frame, both palettes, theme messages and Markdown switching pass offline");
  assert.deepEqual(errors, []);
  console.log("Discovery test: PASS");
} finally { await browser.close(); }
