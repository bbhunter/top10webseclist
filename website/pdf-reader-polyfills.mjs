// PDF.js 5 follows the newest evergreen-browser baseline. Keep the renderer
// working on otherwise capable iPhones whose WebKit update trails that baseline.
// This module runs in both the isolated viewer window and its worker.
if (typeof Promise.withResolvers !== "function") {
  Promise.withResolvers = () => {
    let resolve;
    let reject;
    const promise = new Promise((promiseResolve, promiseReject) => {
      resolve = promiseResolve;
      reject = promiseReject;
    });
    return { promise, resolve, reject };
  };
}

if (typeof Promise.try !== "function") {
  Promise.try = (callback, ...args) => new Promise((resolve) => resolve(callback(...args)));
}

if (typeof Uint8Array.prototype.toHex !== "function") {
  Object.defineProperty(Uint8Array.prototype, "toHex", {
    configurable: true,
    value() { return [...this].map((byte) => byte.toString(16).padStart(2, "0")).join(""); }
  });
}

if (typeof Uint8Array.fromBase64 !== "function") {
  Object.defineProperty(Uint8Array, "fromBase64", {
    configurable: true,
    value(value) {
      const binary = atob(String(value));
      return Uint8Array.from(binary, (character) => character.charCodeAt(0));
    }
  });
}

if (typeof Uint8Array.prototype.toBase64 !== "function") {
  Object.defineProperty(Uint8Array.prototype, "toBase64", {
    configurable: true,
    value() {
      let binary = "";
      for (let offset = 0; offset < this.length; offset += 0x8000) {
        binary += String.fromCharCode(...this.subarray(offset, offset + 0x8000));
      }
      return btoa(binary);
    }
  });
}

if (typeof URL.parse !== "function") {
  URL.parse = (value, base) => {
    try { return new URL(value, base); }
    catch { return null; }
  };
}

if (typeof Math.sumPrecise !== "function") {
  Math.sumPrecise = (values) => {
    let sum = 0;
    let correction = 0;
    for (const value of values) {
      const next = sum + value;
      correction += Math.abs(sum) >= Math.abs(value) ? sum - next + value : value - next + sum;
      sum = next;
    }
    return sum + correction;
  };
}

if (typeof Set.prototype.intersection !== "function") {
  Object.defineProperty(Set.prototype, "intersection", {
    configurable: true,
    value(other) { return new Set([...this].filter((value) => other.has(value))); }
  });
}

if (typeof ArrayBuffer.prototype.transferToFixedLength !== "function") {
  Object.defineProperty(ArrayBuffer.prototype, "transferToFixedLength", {
    configurable: true,
    value(length = this.byteLength) { return this.slice(0, length); }
  });
}

if (typeof AbortSignal !== "undefined" && typeof AbortSignal.any !== "function") {
  AbortSignal.any = (signals) => {
    const controller = new AbortController();
    const abort = (signal) => controller.abort(signal.reason);
    for (const signal of signals) {
      if (signal.aborted) {
        abort(signal);
        break;
      }
      signal.addEventListener("abort", () => abort(signal), { once: true });
    }
    return controller.signal;
  };
}

if (typeof Response !== "undefined" && typeof Response.prototype.bytes !== "function") {
  Object.defineProperty(Response.prototype, "bytes", {
    configurable: true,
    value() { return this.arrayBuffer().then((buffer) => new Uint8Array(buffer)); }
  });
}
