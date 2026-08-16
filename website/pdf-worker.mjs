// Module workers have their own global object, so the iPhone compatibility
// layer must run here as well as in the viewer before PDF.js is evaluated.
import "./pdf-reader-polyfills.mjs";

await import("./vendor/pdfjs/build/pdf.worker.mjs");
