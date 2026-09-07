// Optional browser regression checks; see README.md for the isolated setup.
import assert from "node:assert/strict";
const { chromium } = await import(process.env.PLAYWRIGHT_MODULE || "playwright");
const browser = await chromium.launch({ headless: true });
const baseUrl = process.env.WEBSEC_TEST_URL || "http://127.0.0.1:8000/website/";
const views = ["museum", "library", "signals", "constellation", "terminal", "evidence", "favourites", "desk", "time"];
const errors = [];
const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
page.on("pageerror", (error) => errors.push(error.message));

async function keyboardClick(selector) {
  const control = page.locator(selector).first();
  await control.focus();
  await page.keyboard.press("Enter");
  await page.waitForFunction((selector) => document.activeElement.matches(selector), selector);
}

try {
  await page.goto(baseUrl);
  await page.waitForSelector("#app-shell:not([hidden])");
  await page.waitForFunction(() => !document.querySelector("#boot-screen"));
  for (const width of [1440, 768, 390, 320]) {
    await page.setViewportSize({ width, height: 1000 });
    for (const view of views) {
      await page.evaluate((view) => setView(view), view);
      const layout = await page.evaluate(() => ({
        overflow: document.documentElement.scrollWidth > innerWidth,
        view: document.documentElement.dataset.view,
        heading: document.querySelector("#view-mode").textContent,
        scheme: getComputedStyle(document.documentElement).colorScheme
      }));
      assert.equal(layout.overflow, false, `${view} overflows at ${width}px`);
      assert.equal(layout.view, view);
      assert.ok(layout.heading);
      assert.equal(layout.scheme, "dark");
    }
  }
  console.log("Layouts: 9 views at 4 viewport widths passed");
  await page.evaluate(async () => {
    await setView("terminal");
    await setView("museum");
    await new Promise(requestAnimationFrame);
  });

  await page.setViewportSize({ width: 1440, height: 1000 });
  await page.evaluate(() => setView("museum"));
  await keyboardClick('[data-room-filter="XSS"]');
  assert.equal(await page.locator('[data-room-filter="XSS"]').getAttribute("aria-pressed"), "true");
  await page.locator('[data-room-filter="reset"]').focus();
  await page.keyboard.press("Enter");
  assert.ok(await page.evaluate(() => document.activeElement.hasAttribute("data-room-filter")));
  for (const view of ["museum", "library", "constellation", "evidence"]) {
    await page.evaluate((view) => setView(view), view);
    await keyboardClick('[data-year="2024"]');
  }
  await page.evaluate(() => setView("signals"));
  await keyboardClick('[data-signal-topic="HTTP"]');
  await keyboardClick('[data-signal-year="2024"]');
  console.log("Keyboard: topic, reset and year controls retain focus");

  await page.evaluate(() => setView("constellation"));
  await page.locator("#motion-toggle").click();
  await page.waitForFunction(() => document.querySelector("#space-autorotate").disabled);
  const yaw = await page.evaluate(() => constellationExperience.camera.yaw);
  const visualTime = await page.evaluate(() => constellationExperience.visualTime);
  await page.waitForTimeout(150);
  assert.equal(await page.evaluate(() => constellationExperience.camera.yaw), yaw);
  assert.equal(await page.evaluate(() => constellationExperience.visualTime), visualTime);
  assert.equal(await page.locator("#space-autorotate").getAttribute("aria-pressed"), "false");
  assert.equal(await page.evaluate(() => getComputedStyle(document.documentElement).scrollBehavior), "auto");
  await page.reload();
  await page.waitForSelector("#app-shell:not([hidden])");
  assert.equal(await page.locator("#motion-toggle").getAttribute("aria-pressed"), "true");
  await page.waitForFunction(() => !document.querySelector("#boot-screen"));
  await page.locator("#motion-toggle").click();
  await page.emulateMedia({ reducedMotion: "reduce" });
  await page.waitForFunction(() => document.querySelector("#motion-toggle").disabled);
  assert.equal(await page.locator("#motion-toggle").getAttribute("aria-pressed"), "true");
  await page.emulateMedia({ reducedMotion: "no-preference" });
  await page.waitForFunction(() => !document.querySelector("#motion-toggle").disabled);
  assert.equal(await page.locator("#motion-toggle").getAttribute("aria-pressed"), "false");
  console.log("Motion: camera pauses, preference persists, system changes are respected");

  // Test the actual reader controls with a small, benign document. Archive file
  // availability is checked separately by smoke-test.mjs.
  await page.route("**/archived-references/md/**", (route) => route.fulfill({
    contentType: "text/plain", body: "# Theme review\n\n[Research source](https://example.org/)\n\n## Details\n\nA readable document."
  }));
  for (const view of views) {
    await page.evaluate((view) => setView(view), view);
    await page.evaluate(() => openReader(state.items.find((item) => item.mdPath)));
    await page.waitForSelector("#reader-content a");
    for (const theme of ["light", "dark"]) {
      await page.evaluate((theme) => { state.readingTheme = theme; applyReadingTheme(); }, theme);
      const contrast = await page.evaluate(() => {
        const luminance = (color) => {
          const rgb = color.match(/[\d.]+/g).slice(0, 3).map(Number).map((v) => {
            v /= 255;
            return v <= .04045 ? v / 12.92 : ((v + .055) / 1.055) ** 2.4;
          });
          return rgb[0] * .2126 + rgb[1] * .7152 + rgb[2] * .0722;
        };
        const link = getComputedStyle(document.querySelector("#reader-content a")).color;
        const background = getComputedStyle(document.querySelector("#reader-scroll")).backgroundColor;
        // Dark reader scroll areas are transparent; their dialog owns the fill.
        const canvas = document.createElement("canvas").getContext("2d");
        const backdrop = background === "rgba(0, 0, 0, 0)"
          ? getComputedStyle(document.querySelector("#reader-dialog")).backgroundColor : background;
        const rgb = (color) => {
          canvas.fillStyle = color;
          canvas.fillRect(0, 0, 1, 1);
          return `rgb(${[...canvas.getImageData(0, 0, 1, 1).data].slice(0, 3).join(",")})`;
        };
        const a = luminance(rgb(link)), b = luminance(rgb(backdrop));
        return (Math.max(a, b) + .05) / (Math.min(a, b) + .05);
      });
      assert.ok(contrast >= 4.5, `${view} ${theme} link contrast is ${contrast.toFixed(2)}:1`);
    }
    await page.evaluate(() => new Promise((resolve) => {
      const dialog = document.querySelector("#reader-dialog");
      dialog.addEventListener("close", resolve, { once: true });
      dialog.close();
    }));
  }
  await page.evaluate(() => openReader(state.items.find((item) => item.mdPath)));
  await page.locator("#reader-theme-toggle").click();
  assert.equal(await page.evaluate(() => localStorage.getItem(READING_THEME_STORAGE_KEY)), "light");
  assert.equal(new URL(page.url()).searchParams.get("theme"), "light");
  assert.equal(await page.locator("#pdf-dialog").getAttribute("data-reading-theme"), "light");
  for (const width of [390, 320]) {
    await page.setViewportSize({ width, height: 800 });
    assert.ok(await page.evaluate(() => {
      const box = document.querySelector("#reader-dialog").getBoundingClientRect();
      return box.left >= 0 && box.right <= innerWidth && box.bottom <= innerHeight;
    }), `Reader fits at ${width}px`);
  }
  console.log("Readers: light/dark link contrast passes in every view; theme sharing and phone layouts pass");
  assert.deepEqual(errors, []);
  console.log("Theme test: PASS (no browser errors)");
} finally {
  await browser.close();
}
