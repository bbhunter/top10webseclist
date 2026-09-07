import assert from "node:assert/strict";
const { chromium } = await import(process.env.PLAYWRIGHT_MODULE || "playwright");
const base = process.env.WEBSEC_TEST_URL || "http://127.0.0.1:4173/";
const browser = await chromium.launch({headless:true});
const page = await browser.newPage({viewport:{width:390,height:844}});
const errors = [];
page.on("pageerror", (error) => errors.push(error.message));
page.on("console", (message) => { if (message.type() === "error") errors.push(message.text()); });
try {
  await page.goto(`${base}#desk`);
  await page.waitForSelector(".discovery-record");
  const id = await page.evaluate(() => state.items.find((item) => item.pdfPath?.endsWith("kuza55-blogspot-com-cookie-path-traversal.pdf"))?.id);
  assert.ok(id, "Local PDF fixture is available");
  for (const view of ["desk", "time"]) {
    await page.evaluate((view) => setView(view), view);
    await page.locator("#view-fullscreen").click();
    await page.waitForSelector('#view-fullscreen[aria-pressed="true"]');
    assert.equal(await page.evaluate(() => Boolean(document.fullscreenElement) || viewFullscreenFallbackActive()), true);
    await page.locator("#view-fullscreen").click();
    await page.waitForSelector('#view-fullscreen[aria-pressed="false"]');
    assert.equal(await page.locator("#view-fullscreen svg").count(), 1);
    await page.evaluate((id) => openPdfViewer(state.items.find((item) => item.id === id)), id);
    const frame = page.frameLocator("#pdf-frame");
    await frame.locator("canvas").first().waitFor({state:"visible"});
    const frameUrl = new URL(await page.locator("#pdf-frame").getAttribute("src"));
    assert.notEqual(frameUrl.origin, new URL(base).origin);
    assert.equal(frameUrl.hostname, "127.0.0.1");
    assert.equal(await frame.locator("html").getAttribute("data-palette"), view);
    await page.locator("#pdf-theme-toggle").click();
    await frame.locator('html[data-theme="light"]').waitFor();
    await page.locator("#pdf-open-markdown").click();
    await page.waitForSelector("#reader-dialog[open] .archive-warning");
    await page.locator("#reader-theme-toggle").click();
    await page.evaluate(() => new Promise((resolve) => { const dialog=document.querySelector("#reader-dialog"); dialog.addEventListener("close",resolve,{once:true}); dialog.close(); }));
  }
  const pdfPath = await page.evaluate((id) => state.items.find((item) => item.id === id).pdfPath, id);
  const partial = await fetch(new URL(pdfPath, base), {headers:{Range:"bytes=0-15"}});
  assert.equal(partial.status, 206);
  assert.equal((await partial.arrayBuffer()).byteLength, 16);
  assert.deepEqual(errors, []);
  console.log("Local preview: both palettes, fullscreen controls, isolated PDF rendering, theme messages, Markdown switching and PDF range requests pass");
} finally { await browser.close(); }
