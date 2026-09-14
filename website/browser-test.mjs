// Shared launch selection for the isolated browser suites.
const playwright = await import(process.env.PLAYWRIGHT_MODULE || "playwright");
export const browserName = process.env.WEBSEC_TEST_BROWSER || "chromium";
if (!["chromium", "chrome", "msedge", "firefox", "webkit"].includes(browserName)) {
  throw Error(`Unknown test browser: ${browserName}`);
}
export const mobileEmulation = browserName !== "firefox";
export async function launchBrowser() {
  const channel = ["chrome", "msedge"].includes(browserName) ? browserName : undefined;
  const browser = await playwright[channel ? "chromium" : browserName].launch({
    headless:process.env.WEBSEC_TEST_HEADED !== "1", ...(channel ? {channel} : {})
  });
  console.log(`Browser: ${browserName} ${browser.version()}`);
  return browser;
}
