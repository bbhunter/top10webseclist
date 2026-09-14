// Module workers have their own global object, so the iPhone compatibility
// layer must run here as well as in the viewer before PDF.js is evaluated.
import "./pdf-reader-polyfills.mjs";

// PDF.js also imports this entrypoint in its isolated viewer when a dedicated
// worker is unavailable. Preserve the handler export for that fallback path.
const { WorkerMessageHandler } = await import("./vendor/pdfjs/build/pdf.worker.mjs");
export { WorkerMessageHandler };
