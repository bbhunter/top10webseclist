// A new record starts at its heading while the page behind it keeps its place.
import assert from "node:assert/strict";
import {launchBrowser, mobileEmulation} from "./browser-test.mjs";
const browser = await launchBrowser();
const base = process.env.WEBSEC_TEST_URL || "http://127.0.0.1:4173/";
const views = ["evidence","museum","library","time","signals","constellation","terminal","desk","favourites"];
const errors = [];
let checks = 0;
try {
  for (const viewport of [{width:1440,height:900},{width:390,height:844},{width:320,height:568}]) {
    const touch = viewport.width < 820;
    const context = await browser.newContext({viewport,hasTouch:touch,isMobile:touch && mobileEmulation});
    // Exercise the real play button and iframe lifecycle without requesting a
    // third-party video. Playback by YouTube itself is outside this regression.
    await context.route("https://www.youtube-nocookie.com/embed/**", route => route.fulfill({
      contentType:"text/html", body:"<!doctype html><title>Local player fixture</title><p>Video player loaded</p>"
    }));
    const page = await context.newPage();
    page.on("pageerror", error => errors.push(error.message));
    page.on("console", message => { if (message.type() === "error") errors.push(message.text()); });
    await page.goto(`${base}#desk`);
    await page.waitForSelector(".discovery-record");
    await page.waitForFunction(() => !document.querySelector("#boot-screen"));
    const fixtures = await page.evaluate(() => ({
      recorded: state.items.filter(item => playableTalk(item)).sort((a,b) => (b.summary?.length || 0) - (a.summary?.length || 0)).slice(0,2).map(item => item.id),
      plain: state.items.find(item => !item.videos?.length)?.id
    }));
    assert.equal(fixtures.recorded.length, 2, "Two real records with playable recordings are available");
    assert.ok(fixtures.plain);
    const dialog = page.locator("#artifact-dialog");
    async function open(id) {
      await page.evaluate(id => openArtifact(id), id);
      await page.waitForSelector("#artifact-dialog[open]");
      // Allow layout, focus and scroll anchoring to settle before checking.
      await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
    }
    async function atTop(label) {
      if (process.env.WEBSEC_TEST_DEBUG) console.log(label, await page.evaluate(() => ({
        top:document.querySelector("#artifact-dialog").scrollTop, focus:document.activeElement?.id
      })));
      assert.equal(await dialog.evaluate(el => el.scrollTop), 0, `${label}: article starts at the top`);
      assert.ok(await page.locator("#artifact-title").evaluate(title => {
        const heading = title.getBoundingClientRect(), pane = title.closest("dialog").getBoundingClientRect();
        return heading.top >= pane.top && heading.top < pane.bottom;
      }), `${label}: article heading is visible`);
    }
    async function scrollDown() {
      const offset = await dialog.evaluate(el => {
        el.scrollTo({top:el.scrollHeight,behavior:"instant"});
        return el.scrollTop;
      });
      assert.ok(offset > 100, "The previous article really was scrolled down");
    }
    async function close() {
      // Dismiss without focusing a toolbar control that might change scroll.
      const point = await dialog.evaluate(el => ({x:el.getBoundingClientRect().left / 2,y:innerHeight / 2}));
      if (touch) await page.touchscreen.tap(point.x,point.y);
      else await page.mouse.click(point.x,point.y);
      await page.waitForFunction(() => !document.querySelector("#artifact-dialog").open && !document.body.classList.contains("document-dialog-open"));
    }
    for (const view of views) {
      await page.evaluate(view => setView(view),view);
      // Board layout and mobile scrolling can settle on later rendering frames.
      // Capture the user's starting position after those updates, not mid-layout.
      await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
      for (const appearance of (["desk","time"].includes(view) ? ["dark","light"] : ["dark"])) {
        if (["desk","time"].includes(view)) await page.locator(`[data-discovery-value="${appearance}"]`).click();
        for (const play of [false,true]) {
          const label = `${view}/${appearance}/${viewport.width}/${play ? "played" : "scrolled"}`;
          await page.evaluate(() => scrollTo({top:400,behavior:"instant"}));
          await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
          const pageScroll = await page.evaluate(() => scrollY);
          await open(fixtures.recorded[0]);
          assert.equal(await page.evaluate(() => lockedDialogScrollY), pageScroll, `${label}: opening preserves the pre-dialog page offset`);
          await atTop(label);
          await scrollDown();
          let player;
          if (play) {
            await page.locator(".talk-play-action").click();
            await page.frameLocator("#artifact-talk iframe").getByText("Video player loaded").waitFor();
            player = await page.locator("#artifact-talk iframe").elementHandle();
            await scrollDown();
          }
          await close();
          if (player) {
            assert.equal(await player.evaluate(el => el.isConnected),false,"Closing removes the previous player");
            await player.dispose();
          }
          const restoredScroll = await page.evaluate(() => scrollY);
          assert.ok(Math.abs(restoredScroll - pageScroll) < 2, `${label}: background scroll ${restoredScroll} matches ${pageScroll}`);
          await open(fixtures.recorded[1]);
          await atTop(label);
          assert.equal(await page.locator("#artifact-talk iframe").count(),0,"The next recording waits for the user to press play");
          await scrollDown();
          await close();
          await open(fixtures.recorded[1]);
          await atTop(`${label}/reopened`);
          await scrollDown();
          await close();
          await open(fixtures.plain);
          await atTop(`${label}/without-video`);
          await close();
          checks++;
        }
      }
    }
    await context.close();
    console.log(`Article scroll: all 9 views at ${viewport.width}px pass new/reopened records, video teardown and page-position preservation`);
  }
  assert.deepEqual(errors,[]);
  console.log(`Article scroll: ${checks} scenarios passed with no browser errors`);
} finally { await browser.close(); }
