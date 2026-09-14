import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import {launchBrowser} from "./browser-test.mjs";
const axeSource = await readFile(process.env.AXE_SOURCE || fileURLToPath(import.meta.resolve("axe-core/axe.min.js")), "utf8");
const browser = await launchBrowser();
const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
const url = process.env.WEBSEC_TEST_URL || "http://127.0.0.1:8000/website/";
const violations = [];
let checks = 0;
async function audit(label) {
  const found = await page.evaluate(() => axe.run(document, { runOnly: { type: "tag", values: ["wcag2a", "wcag2aa", "wcag21aa", "wcag22aa"] } }));
  violations.push(...found.violations.map((item) => ({ label, id: item.id, nodes: item.nodes.map((node) => ({ target: node.target, failure: node.failureSummary })) })));
  checks++;
}
async function close(id) {
  await page.evaluate((id) => new Promise((resolve) => {
    const dialog = document.getElementById(id);
    dialog.addEventListener("close", resolve, { once: true });
    dialog.close();
  }), id);
}
try {
  await page.goto(`${url}#desk`);
  await page.waitForSelector(".discovery-record");
  await page.waitForFunction(() => !document.querySelector("#boot-screen"));
  await page.evaluate(axeSource);
  for (const view of ["desk", "time"]) {
    await page.evaluate((view) => setView(view), view);
    for (const theme of ["light", "dark"]) {
      await page.locator(`[data-discovery-action="theme"][data-discovery-value="${theme}"]`).click();
      await audit(`${view}/${theme}/page`);
      await page.locator(".discovery-record [data-artifact]").first().click();
      await page.waitForSelector("#artifact-dialog[open]");
      await audit(`${view}/${theme}/record`);
      await page.locator("#report-inaccuracy").click();
      await page.waitForSelector("#report-dialog[open]");
      await audit(`${view}/${theme}/report`);
      await close("report-dialog");
      await close("artifact-dialog");
      await page.locator(".topbar [data-contribute]").click();
      await page.waitForSelector("#contribute-dialog[open]");
      await audit(`${view}/${theme}/submit`);
      await close("contribute-dialog");
    }
    await page.setViewportSize({ width: 390, height: 844 });
    await audit(`${view}/mobile`);
    await page.locator("#mobile-menu").click();
    await audit(`${view}/mobile-menu`);
    await page.locator("#close-mobile-menu").click();
    await page.setViewportSize({ width: 1440, height: 1000 });
  }
  assert.deepEqual(violations.map(({label,id,nodes}) => ({label,id,count:nodes.length,examples:nodes.slice(0,2)})), []);
  console.log(`Accessibility: ${checks} page, popup and mobile checks passed (zero automated WCAG A/AA violations)`);
} finally { await browser.close(); }
