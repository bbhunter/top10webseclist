import "./pdf-reader-polyfills.mjs";
import { safePdfUrl } from "./pdf-reader-url.mjs";

const $ = (selector) => document.querySelector(selector);
const PDFJS_ROOT = new URL("./vendor/pdfjs/", import.meta.url);
const MAX_ZOOM = 2;
const MIN_ZOOM = .75;
const MAX_RENDERED_PAGES = 7;
const MAX_CANVAS_PIXELS = 8_000_000;

let pdfDocument = null;
let loadingTask = null;
let renderObserver = null;
let pageObserver = null;
let pageStates = [];
let currentPage = 1;
let zoom = 1;
let generation = 0;
let resizeTimer = null;

function applyTheme(value) {
  document.documentElement.dataset.theme = value === "light" ? "light" : "dark";
}

applyTheme(new URLSearchParams(location.search).get("theme"));
window.addEventListener("message", (event) => {
  if (event.origin !== "https://webhacklist.com" || event.source !== parent || event.data?.type !== "pdf-reader-theme") return;
  applyTheme(event.data.theme);
});

function setMessage(text) {
  $("#reader-message-text").textContent = text;
}

function showError(error, source) {
  const message = error instanceof Error ? error.message : String(error || "Unknown viewer error");
  $("#reader-message").hidden = true;
  $("#pdf-pages").hidden = true;
  $("#reader-error").hidden = false;
  $("#reader-error-text").textContent = `${message}. Use the browser or system PDF viewer instead.`;
  if (source) $("#open-direct").href = source.href;
  else $("#open-direct").hidden = true;
}

function updateControls() {
  const count = pdfDocument?.numPages || 0;
  $("#page-status").textContent = count ? `Page ${currentPage} / ${count}` : "Page —";
  $("#previous-page").disabled = !count || currentPage <= 1;
  $("#next-page").disabled = !count || currentPage >= count;
  $("#zoom-out").disabled = !count || zoom <= MIN_ZOOM;
  $("#zoom-in").disabled = !count || zoom >= MAX_ZOOM;
  $("#zoom-status").textContent = zoom === 1 ? "Fit width" : `${Math.round(zoom * 100)}%`;
}

function cancelRender(state) {
  try { state.renderTask?.cancel(); }
  catch { /* A completed render has nothing left to cancel. */ }
  state.renderTask = null;
}

function releasePage(state) {
  if (!state.rendered && !state.rendering) return;
  cancelRender(state);
  state.generation++;
  state.rendering = false;
  state.rendered = false;
  state.canvas.hidden = true;
  state.canvas.width = 1;
  state.canvas.height = 1;
  state.section.classList.remove("is-rendered");
  try { state.page?.cleanup(); }
  catch { /* Cleanup is an optional memory hint. */ }
  state.page = null;
}

function releaseDistantPages(focus) {
  const rendered = pageStates.filter((state) => state.rendered && !state.visible);
  rendered.sort((left, right) => Math.abs(right.number - focus) - Math.abs(left.number - focus));
  const keep = Math.max(0, MAX_RENDERED_PAGES - pageStates.filter((state) => state.rendered && state.visible).length);
  rendered.slice(keep).forEach(releasePage);
}

async function renderPage(state) {
  if (!pdfDocument || state.rendered || state.rendering) return;
  state.rendering = true;
  const localGeneration = ++state.generation;
  const documentGeneration = generation;
  try {
    const page = await pdfDocument.getPage(state.number);
    if (documentGeneration !== generation || localGeneration !== state.generation) return page.cleanup();
    state.page = page;
    const baseViewport = page.getViewport({ scale: 1 });
    const availableWidth = Math.max(240, $("#pdf-pages").clientWidth - 24);
    const viewport = page.getViewport({ scale: availableWidth / baseViewport.width * zoom });
    const desiredScale = Math.min(window.devicePixelRatio || 1, 2);
    const pixelLimitScale = Math.sqrt(MAX_CANVAS_PIXELS / Math.max(1, viewport.width * viewport.height));
    const outputScale = Math.max(1, Math.min(desiredScale, pixelLimitScale));
    const canvas = state.canvas;
    canvas.width = Math.max(1, Math.floor(viewport.width * outputScale));
    canvas.height = Math.max(1, Math.floor(viewport.height * outputScale));
    canvas.style.width = `${Math.floor(viewport.width)}px`;
    canvas.style.height = `${Math.floor(viewport.height)}px`;
    state.section.style.width = `${Math.floor(viewport.width)}px`;
    state.section.style.minHeight = `${Math.floor(viewport.height)}px`;
    state.section.style.marginInline = zoom > 1 ? "0" : "auto";
    const context = canvas.getContext("2d", { alpha: false });
    const transform = outputScale === 1 ? null : [outputScale, 0, 0, outputScale, 0, 0];
    state.renderTask = page.render({ canvasContext: context, transform, viewport });
    await state.renderTask.promise;
    if (documentGeneration !== generation || localGeneration !== state.generation) return;
    state.renderTask = null;
    state.rendering = false;
    state.rendered = true;
    state.lastUsed = performance.now();
    canvas.hidden = false;
    state.section.classList.add("is-rendered");
    releaseDistantPages(currentPage);
  } catch (error) {
    state.renderTask = null;
    state.rendering = false;
    if (error?.name === "RenderingCancelledException") return;
    state.section.querySelector(".page-loading").textContent = "This page could not be rendered";
  }
}

function nearestPage() {
  const scroller = $("#document-scroll");
  const target = scroller.getBoundingClientRect().top + scroller.clientHeight * .38;
  let nearest = pageStates[0];
  let distance = Number.POSITIVE_INFINITY;
  for (const state of pageStates) {
    const rect = state.section.getBoundingClientRect();
    const candidate = rect.top <= target && rect.bottom >= target ? 0 : Math.min(Math.abs(rect.top - target), Math.abs(rect.bottom - target));
    if (candidate < distance) {
      distance = candidate;
      nearest = state;
    }
  }
  return nearest?.number || 1;
}

let pageUpdateFrame = null;
function updateCurrentPage() {
  if (pageUpdateFrame !== null) return;
  pageUpdateFrame = requestAnimationFrame(() => {
    pageUpdateFrame = null;
    const nextPage = nearestPage();
    if (nextPage === currentPage) return;
    currentPage = nextPage;
    updateControls();
    releaseDistantPages(currentPage);
  });
}

function observePages() {
  const scroller = $("#document-scroll");
  if ("IntersectionObserver" in window) {
    renderObserver = new IntersectionObserver((entries) => {
      for (const entry of entries) {
        const state = pageStates[Number(entry.target.dataset.page) - 1];
        if (!state) continue;
        state.visible = entry.isIntersecting;
        if (entry.isIntersecting) renderPage(state);
      }
      releaseDistantPages(currentPage);
    }, { root: scroller, rootMargin: "100% 0px", threshold: 0 });
    pageStates.forEach((state) => renderObserver.observe(state.section));

    pageObserver = new IntersectionObserver(updateCurrentPage, { root: scroller, threshold: [0, .25, .6] });
    pageStates.forEach((state) => pageObserver.observe(state.section));
  } else {
    pageStates.slice(0, 2).forEach((state) => {
      state.visible = true;
      renderPage(state);
    });
    scroller.addEventListener("scroll", () => {
      updateCurrentPage();
      const focus = nearestPage();
      pageStates.slice(Math.max(0, focus - 2), focus + 1).forEach((state) => renderPage(state));
    }, { passive: true });
  }
  scroller.addEventListener("scroll", updateCurrentPage, { passive: true });
}

function buildPagePlaceholders() {
  const pages = $("#pdf-pages");
  const template = $("#pdf-page-template");
  const fragment = document.createDocumentFragment();
  pageStates = [];
  for (let number = 1; number <= pdfDocument.numPages; number++) {
    const section = template.content.firstElementChild.cloneNode(true);
    section.dataset.page = String(number);
    section.setAttribute("aria-label", `Page ${number} of ${pdfDocument.numPages}`);
    section.querySelector(".page-number").textContent = `${number} / ${pdfDocument.numPages}`;
    const state = {
      number,
      section,
      canvas: section.querySelector("canvas"),
      page: null,
      renderTask: null,
      rendering: false,
      rendered: false,
      visible: false,
      generation: 0,
      lastUsed: 0
    };
    pageStates.push(state);
    fragment.append(section);
  }
  pages.replaceChildren(fragment);
  pages.hidden = false;
  $("#reader-message").hidden = true;
  observePages();
}

function scrollToPage(number) {
  const target = pageStates[Math.max(1, Math.min(pdfDocument?.numPages || 1, number)) - 1];
  if (!target) return;
  currentPage = target.number;
  updateControls();
  renderPage(target);
  target.section.scrollIntoView({ behavior: "smooth", block: "start" });
}

function setZoom(nextZoom) {
  const bounded = Math.max(MIN_ZOOM, Math.min(MAX_ZOOM, Math.round(nextZoom * 4) / 4));
  if (bounded === zoom) return;
  zoom = bounded;
  generation++;
  pageStates.forEach(releasePage);
  updateControls();
  pageStates.filter((state) => state.visible || state.number === currentPage).forEach(renderPage);
}

function wireControls() {
  $("#previous-page").addEventListener("click", () => scrollToPage(currentPage - 1));
  $("#next-page").addEventListener("click", () => scrollToPage(currentPage + 1));
  $("#zoom-out").addEventListener("click", () => setZoom(zoom - .25));
  $("#zoom-in").addEventListener("click", () => setZoom(zoom + .25));
  window.addEventListener("resize", () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
      generation++;
      pageStates.forEach(releasePage);
      pageStates.filter((state) => state.visible || state.number === currentPage).forEach(renderPage);
    }, 180);
  }, { passive: true });
}

async function start() {
  wireControls();
  const source = safePdfUrl(new URLSearchParams(location.search).get("file"));
  parent.postMessage({ type: "pdf-reader-loaded" }, "https://webhacklist.com");
  if (!source) return showError("The document address was missing or did not pass validation", null);
  $("#open-direct").href = source.href;
  try {
    const pdfjs = await import(new URL("build/pdf.mjs", PDFJS_ROOT));
    pdfjs.GlobalWorkerOptions.workerSrc = new URL("./pdf-worker.mjs", import.meta.url).href;
    loadingTask = pdfjs.getDocument({
      url: source.href,
      cMapUrl: new URL("web/cmaps/", PDFJS_ROOT).href,
      cMapPacked: true,
      standardFontDataUrl: new URL("web/standard_fonts/", PDFJS_ROOT).href,
      wasmUrl: new URL("web/wasm/", PDFJS_ROOT).href,
      enableXfa: false,
      isEvalSupported: false,
      useSystemFonts: true
    });
    loadingTask.onProgress = ({ loaded, total }) => {
      if (total > 0) setMessage(`Loading the document… ${Math.min(100, Math.round(loaded / total * 100))}%`);
    };
    pdfDocument = await loadingTask.promise;
    if (!pdfDocument.numPages) throw new Error("The PDF contains no pages");
    document.title = `PDF reader · ${pdfDocument.numPages} pages`;
    buildPagePlaceholders();
    updateControls();
  } catch (error) {
    showError(error, source);
  }
}

window.addEventListener("pagehide", () => {
  generation++;
  renderObserver?.disconnect();
  pageObserver?.disconnect();
  pageStates.forEach(releasePage);
  loadingTask?.destroy();
});

start();
