// Only archive-controlled PDF paths may enter the separate-origin renderer.
// Keep this helper dependency-free so the production smoke test can exercise
// the exact URL boundary without loading the browser-only PDF.js bundle.
export function safePdfUrl(value) {
  let url;
  try { url = new URL(String(value || "")); }
  catch { return null; }
  if (url.username || url.password || url.hash) return null;
  if ([...url.searchParams].some(([key, token]) => key !== "v" || !/^\d{8,20}$/.test(token))) return null;
  const cloudflarePath = /^\/(?:archived-references\/pdf\/[a-z0-9-]+\/[a-z0-9._-]+|original-listings\/[0-9-]+-(?:top10|nominees-and-top10))\.pdf$/i;
  const githubPath = /^\/webhacklist\/(?:archived-references\/pdf\/[a-z0-9-]+\/[a-z0-9._-]+|original-listings\/[0-9-]+-(?:top10|nominees-and-top10))\.pdf$/i;
  if (url.origin === "https://webhacklist.com" && cloudflarePath.test(url.pathname)) return url;
  if (url.origin === "https://irsdl.github.io" && githubPath.test(url.pathname)) return url;
  return null;
}
