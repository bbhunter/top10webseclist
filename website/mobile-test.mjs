// Touch navigation and compact-header regressions against the local website.
import assert from "node:assert/strict";
const playwright = await import(process.env.PLAYWRIGHT_MODULE || "playwright");
const browserName = process.env.WEBSEC_TEST_BROWSER || "chromium";
const browser = await playwright[browserName].launch({headless:true});
const base = process.env.WEBSEC_TEST_URL || "http://127.0.0.1:8000/website/";
const views = ["desk", "time", "museum", "library", "signals", "constellation", "terminal", "evidence", "favourites"];
const errors = [];
const screens = [{width:320,height:568},{width:390,height:844},{width:768,height:1024}];
async function ready(page, view) {
  await page.waitForFunction((view) => document.documentElement.dataset.view === view && document.querySelector('#view-root').textContent.trim().length > 50, view);
  if (["desk","time"].includes(view)) await page.waitForSelector(".discovery-record");
  if (view === "constellation") await page.waitForSelector("#constellation-canvas");
}
async function fits(page, selector, label) {
  assert.ok(await page.locator(selector).evaluate((element) => {
    const rect = element.getBoundingClientRect();
    return rect.left >= -1 && rect.right <= innerWidth + 1 && rect.width > 0;
  }), `${label} fits the viewport`);
}
try {
  for (const viewport of screens) {
    const context = await browser.newContext({viewport,hasTouch:true,isMobile:true,deviceScaleFactor:1});
    const page = await context.newPage();
    page.on("pageerror", (error) => errors.push(error.message));
    page.on("console", (message) => { if (message.type() === "error") errors.push(message.text()); });
    await page.goto(`${base}#desk`);
    await ready(page,"desk");
    await page.waitForFunction(() => !document.querySelector("#boot-screen"));
    assert.equal(await page.locator("html").getAttribute("data-discovery-theme"), "dark");
    assert.equal(await page.locator(".nav-item").count(), 9);
    assert.equal(await page.locator('.nav-item[data-view="guide"],.nav-item[data-view="gazette"]').count(), 0);
    // Give the personal collection a record, through the actual Save control.
    await page.locator(".discovery-record [data-favourite]").first().tap();
    for (const view of views) {
      await page.evaluate(() => scrollTo({top:600,behavior:"instant"}));
      await page.locator("#mobile-menu").tap();
      await page.locator(`.nav-item[data-view="${view}"]`).tap();
      await ready(page,view);
      assert.equal(await page.locator("#mobile-menu").getAttribute("aria-expanded"), "false");
      assert.equal(await page.locator("#concept-sidebar").getAttribute("inert"), "");
      assert.ok(await page.evaluate(() => scrollY < 2), `${view} opens at its top after mobile navigation`);
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false, `${view}/${viewport.width} has no page overflow`);
      assert.equal(await page.evaluate(() => getComputedStyle(document.documentElement).colorScheme), "dark");
      if (["desk","time"].includes(view)) {
        assert.equal(await page.locator(".discovery-lead").count(),0);
        const control = view === "desk" ? "#desk-query" : "#time-topic";
        assert.ok((await page.locator(control).boundingBox()).y < 320, `${view} primary filter is near the top`);
        await fits(page,".view-intro",`${view} header`);
      }
      const record = page.locator("#view-root [data-artifact]:visible").first();
      if (await record.count()) {
        await record.tap();
        await page.waitForSelector("#artifact-dialog[open]");
        await fits(page,"#artifact-dialog",`${view} record popup`);
        await page.locator("#artifact-dialog .dialog-close").tap();
        await page.waitForSelector("#artifact-dialog[open]",{state:"hidden"});
      }
      if (view === "constellation") {
        const before = await page.evaluate(() => constellationExperience.camera.distance);
        await page.locator("#space-zoom-in").tap();
        assert.ok(await page.evaluate((before) => constellationExperience.camera.distance < before, before));
      }
      if (view === "terminal") {
        await page.locator("#terminal-command").fill("help");
        await page.locator("#terminal-command").press("Enter");
        await page.waitForFunction(() => document.querySelector("#terminal-output").textContent.includes("Available commands"));
      }
      // Direct-link refresh must reopen the same route on a phone.
      await page.reload();
      await ready(page,view);
      await page.waitForFunction(() => !document.querySelector("#boot-screen"));
      await fits(page,"#main-content",`${view} direct link`);
    }
    await page.goto(`${base}#desk`);
    await ready(page,"desk");
    await page.locator('[data-discovery-value="light"]').tap();
    await page.reload();
    await ready(page,"desk");
    assert.equal(await page.locator("html").getAttribute("data-discovery-theme"), "light");
    await page.locator('[data-discovery-value="dark"]').tap();
    await page.setViewportSize({width:844,height:390});
    await fits(page,"#main-content","landscape layout");
    assert.equal(await page.locator("#concept-sidebar").getAttribute("inert"), null);
    await page.setViewportSize(viewport);
    await page.locator("#mobile-menu").tap();
    await page.locator("#close-mobile-menu").tap();
    assert.equal(await page.locator("#mobile-menu").getAttribute("aria-expanded"), "false");
    await context.close();
    console.log(`Mobile ${browserName}: all 9 themes at ${viewport.width}px; touch navigation, direct links, popups, dark default, saved appearance and rotation pass`);
  }
  // Exercise the CSS fullscreen fallback used when element fullscreen is
  // unavailable, including a short landscape phone where Exit must stay visible.
  const fallback = await browser.newContext({viewport:{width:667,height:375},hasTouch:true,isMobile:true});
  await fallback.addInitScript(() => {
    Object.defineProperty(Element.prototype,"requestFullscreen",{value:undefined,configurable:true});
    Object.defineProperty(Element.prototype,"webkitRequestFullscreen",{value:undefined,configurable:true});
  });
  const landscape = await fallback.newPage();
  landscape.on("pageerror",(error) => errors.push(error.message));
  await landscape.goto(`${base}#desk`);
  await ready(landscape,"desk");
  await landscape.waitForFunction(() => !document.querySelector("#boot-screen"));
  for (const view of views) {
    await landscape.locator("#mobile-menu").tap();
    await landscape.locator(`.nav-item[data-view="${view}"]`).tap();
    await ready(landscape,view);
    await landscape.locator("#view-fullscreen").tap();
    await landscape.waitForSelector("main.view-fullscreen-fallback");
    if (view === "terminal") assert.ok((await landscape.locator("#terminal-output").boundingBox()).height >= 100, "Terminal results stay visible in landscape fullscreen");
    assert.ok(await landscape.locator("#view-fullscreen").isVisible(), `${view} landscape fallback keeps its Exit control visible`);
    await landscape.locator("#view-fullscreen").tap();
    await landscape.waitForSelector("main.view-fullscreen-fallback",{state:"hidden"});
  }
  await fallback.close();
  console.log("Mobile landscape: all 9 themes enter and exit fullscreen without the native Fullscreen API");
  assert.deepEqual(errors,[]);
} finally { await browser.close(); }
