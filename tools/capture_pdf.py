"""Archive the Top 10 Web Hacking Techniques announcement pages as PDFs.

Every year of the list was announced somewhere - Jeremiah Grossman's blog, then
WhiteHat Security's, then PortSwigger Research - and one of those hosts is
already gone. This captures both halves of each year's record (the full nominee
list and the post naming the winning ten) into `original-listings/`, with the
source URL and an HTTP status recorded for every file. Which page each file came
from is data and lives in `tools/sources.json`; no host is hardcoded here.

The browser is driven through `tools/references/refslib`, which owns the process
lifecycle and the hardened profile. This module owns the archival policy: what to
capture, how the page should be tidied before printing, and what counts as a
capture that actually worked.

    python tools/capture_pdf.py doctor            # is this machine set up?
    python tools/capture_pdf.py list              # what the manifest holds
    python tools/capture_pdf.py run               # capture whatever is missing
    python tools/capture_pdf.py verify            # check every PDF
    python tools/capture_pdf.py url URL OUT.pdf   # a one-off page
    python tools/capture_pdf.py text FILE.pdf     # read a PDF back
"""

import argparse
import datetime
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
# refslib owns the browser: one hardened profile per capture, closed over CDP.
sys.path.insert(0, os.path.join(HERE, "references"))

from refslib.browser import BROWSER_ENV, Ladder, find_browser  # noqa: E402

DEFAULT_MANIFEST = os.path.join(HERE, "sources.json")
DEFAULT_OUTDIR = os.path.join(REPO, "original-listings")
REPORT = os.path.join(HERE, "capture-report.json")

# A page that renders under this many bytes did not render. Used to trigger a
# retry, not to pass judgement - `verify` is where a capture is really assessed.
THIN_PDF_BYTES = 6000

# Replaying an archived page means waiting on the archive as well as the page, so
# these get a longer settle than a live host needs.
SLOW_HOSTS = ("web.archive.org", "archive.org")
SLOW_HOST_SETTLE = 6.0

# --- archival policy: what to do to a page before printing it ---------------

# Lazy-loaded images only fetch once they have been scrolled into view, so a
# straight print of a long post yields blank figures.
SCROLL_JS = r"""
(async () => {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const step = Math.max(400, Math.floor(window.innerHeight * 0.8));
  let y = 0, guard = 0;
  while (y < document.body.scrollHeight && guard++ < 400) {
    window.scrollTo(0, y);
    await sleep(60);
    y += step;
  }
  window.scrollTo(0, document.body.scrollHeight);
  await sleep(400);
  window.scrollTo(0, 0);
  await sleep(200);
  const imgs = [...document.images];
  await Promise.race([
    Promise.all(imgs.map(i => i.complete ? 1 : new Promise(r => {
      i.addEventListener('load', r, {once: true});
      i.addEventListener('error', r, {once: true});
    }))),
    sleep(8000),
  ]);
  return {images: imgs.length,
          loaded: imgs.filter(i => i.complete && i.naturalWidth > 0).length};
})()
"""

# Furniture that would otherwise land in the archive. The Wayback toolbar is the
# important one: it is injected into every replayed page, and these captures are
# the reason this list exists at all.
CLEANUP_JS = r"""
(() => {
  const killed = [];
  const furniture = [
    '#wm-ipp-base', '#wm-ipp', '#wm-ipp-print', '#donato', '#playback',
    '.wb-autocomplete-suggestions',
    '#onetrust-consent-sdk', '#onetrust-banner-sdk',
    '#CybotCookiebotDialog', '#CybotCookiebotDialogBodyUnderlay',
    '.cookie-banner', '.cookie-notice', '.cookie-consent', '#cookie-banner',
    '#cookieConsent', '.cc-window', '#gdpr-banner', '.js-consent-banner',
    '[aria-label="cookieconsent"]', '.newsletter-signup-modal', '.modal-backdrop'
  ];
  for (const selector of furniture) {
    for (const el of document.querySelectorAll(selector)) {
      el.remove();
      killed.push(selector);
    }
  }
  // A fixed or sticky element reprints on every page of the PDF, or covers the
  // text under it. Demote rather than remove: it is usually the site header,
  // which belongs in the archive once, at the top.
  let unstuck = 0;
  for (const el of document.querySelectorAll('body *')) {
    const position = getComputedStyle(el).position;
    if (position === 'fixed' || position === 'sticky') {
      el.style.setProperty('position', 'static', 'important');
      unstuck++;
    }
  }
  // Some archived pages scroll an inner container; let the whole document flow
  // so printing sees its full height.
  for (const el of [document.documentElement, document.body]) {
    el.style.setProperty('overflow', 'visible', 'important');
    el.style.setProperty('height', 'auto', 'important');
    el.style.setProperty('max-height', 'none', 'important');
  }
  const style = document.createElement('style');
  style.textContent = `
    * { -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important; }
    a { text-decoration: underline; }
    details { display: block !important; }
  `;
  document.head.appendChild(style);
  // A collapsed <details> prints as its summary alone, silently losing the body.
  for (const d of document.querySelectorAll('details')) d.open = true;
  return {killed: [...new Set(killed)], unstuck};
})()
"""

PREPARE = (SCROLL_JS, CLEANUP_JS)


def print_options(url, scale):
    """A4 portrait, with the source URL in the footer of every page.

    `scale` is the whole trick behind these looking like web pages rather than
    squeezed phone layouts: printToPDF lays out at the paper width, so A4 alone
    gives Chrome ~794 CSS px and a mobile breakpoint. At 0.7 it lays out at
    ~1100 px and renders that at 70%, which is a desktop layout at a readable
    size.
    """
    return {
        "printBackground": True,
        "displayHeaderFooter": True,
        "headerTemplate": "<div></div>",
        "footerTemplate": (
            '<div style="font-size:7px;width:100%;padding:0 12mm;color:#666;'
            'font-family:sans-serif;display:flex;justify-content:space-between;">'
            '<span>' + escape_html(url) + '</span>'
            '<span class="pageNumber"></span></div>'
        ),
        "paperWidth": 8.27,
        "paperHeight": 11.69,
        "marginTop": 0.35,
        "marginBottom": 0.5,
        "marginLeft": 0.35,
        "marginRight": 0.35,
        "scale": scale,
        "preferCSSPageSize": False,
    }


def escape_html(text):
    return (text.replace("&", "&amp;").replace("<", "&lt;")
                .replace(">", "&gt;").replace('"', "&quot;"))


# --- manifest ---------------------------------------------------------------


def load_manifest(path):
    try:
        with open(path, encoding="utf-8") as handle:
            data = json.load(handle)
    except FileNotFoundError:
        die("no manifest at %s" % path)
    except json.JSONDecodeError as error:
        die("manifest %s is not valid JSON: %s" % (path, error))
    entries = data.get("entries")
    if not isinstance(entries, list) or not entries:
        die("manifest %s has no 'entries' list" % path)
    for index, entry in enumerate(entries):
        for field in ("year", "kind", "url"):
            if not entry.get(field):
                die("manifest entry %d is missing '%s'" % (index, field))
    return data


def out_name(entry):
    return "%s-%s.pdf" % (entry["year"], entry["kind"])


def select(entries, only=None, kind=None):
    if only:
        wanted = {value.strip() for value in only.split(",") if value.strip()}
        entries = [e for e in entries if e["year"] in wanted]
    if kind:
        entries = [e for e in entries if e["kind"] == kind]
    return entries


def settle_for(entry, default):
    """The per-entry settle, defaulting longer for an archive replay."""
    if entry.get("settle") is not None:
        return float(entry["settle"])
    if any(host in entry["url"] for host in SLOW_HOSTS):
        return max(default, SLOW_HOST_SETTLE)
    return default


def die(message, code=2):
    print("error: %s" % message, file=sys.stderr)
    sys.exit(code)


def now_utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ")


# --- reading a PDF back -----------------------------------------------------


def pdf_text(path):
    """(page_count, text) for a PDF, or raise ImportError without pypdf."""
    from pypdf import PdfReader

    reader = PdfReader(path)
    return len(reader.pages), "\n".join(
        (page.extract_text() or "") for page in reader.pages)


def norm(text):
    """Collapse whitespace so assertions survive text-extraction quirks.

    Justified text extracts with non-breaking spaces and doubled gaps, so a
    literal substring test against the raw extraction reports content missing
    that is plainly on the page. This cost an afternoon once already.
    """
    return " ".join(text.replace("\xa0", " ").split()).lower()


def pdf_info(path, expect=()):
    try:
        pages, text = pdf_text(path)
    except ImportError:
        return {"pages": None, "text": None, "note": "pypdf not installed"}
    except Exception as error:  # a damaged PDF must not stop a batch
        return {"pages": None, "text": None, "note": "unreadable: %s" % error}
    haystack = norm(text)
    info = {"pages": pages, "text": len(text), "sample": text[:300]}
    if expect:
        info["expect_missing"] = [m for m in expect if norm(m) not in haystack]
    return info


def have_pypdf():
    try:
        import pypdf  # noqa: F401
        return True
    except ImportError:
        return False


# --- capture ----------------------------------------------------------------


def capture_one(ladder, url, dest, scale, settle, retries, verbose=False):
    """Capture one URL, retrying a thin render. Returns the stats dict."""
    stats = {}
    for attempt in range(1, retries + 1):
        try:
            payload, stats = ladder.render_url_pdf(
                url, prepare=PREPARE, print_options=print_options(url, scale),
                settle=settle)
            if len(payload) >= THIN_PDF_BYTES:
                write_pdf(dest, payload)
                break
            # Keep it anyway on the last attempt: a genuinely tiny page is
            # better archived than lost, and `verify` will flag it.
            if attempt == retries:
                write_pdf(dest, payload)
            print("      thin render (%d bytes) on attempt %d"
                  % (len(payload), attempt))
        except Exception as error:
            stats = {"error": "%s: %s" % (type(error).__name__, str(error)[:200])}
            print("      attempt %d failed: %s" % (attempt, stats["error"]))
        if attempt < retries:
            time.sleep(2)
    if verbose:
        print("      %s" % json.dumps(stats))
    return stats


def write_pdf(dest, payload):
    directory = os.path.dirname(os.path.abspath(dest))
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(dest, "wb") as handle:
        handle.write(payload)


def require_browser():
    browser = find_browser()
    if not browser:
        die("no Chrome, Chromium or Edge found. Install one, or set %s to its "
            "path. `python tools/capture_pdf.py doctor` shows what was checked."
            % BROWSER_ENV)
    return Ladder(browser=browser)


def load_report():
    if not os.path.exists(REPORT):
        return []
    try:
        with open(REPORT, encoding="utf-8") as handle:
            return json.load(handle).get("results", [])
    except (json.JSONDecodeError, OSError):
        return []


def save_report(results):
    with open(REPORT, "w", encoding="utf-8") as handle:
        json.dump({"generated": now_utc(), "results": results}, handle, indent=2)
        handle.write("\n")


# --- commands ---------------------------------------------------------------


def cmd_run(args):
    manifest = load_manifest(args.manifest)
    entries = select(manifest["entries"], args.only, args.kind)
    if not entries:
        die("no manifest entries matched --only/--kind", code=1)

    todo = []
    for entry in entries:
        dest = os.path.join(args.outdir, out_name(entry))
        if os.path.exists(dest) and not args.force:
            print("skip (exists)  %s" % out_name(entry))
            continue
        todo.append((entry, dest))

    if args.dry_run:
        for entry, _dest in todo:
            print("would capture  %-30s <- %s" % (out_name(entry), entry["url"]))
        print("\n%d to capture." % len(todo))
        return 0
    if not todo:
        print("Nothing to do. Use --force to re-capture.")
        return 0

    ladder = require_browser()
    results = [r for r in load_report()
               if r.get("file") not in {out_name(e) for e, _ in todo}]
    failed = []

    for index, (entry, dest) in enumerate(todo, 1):
        label = out_name(entry)
        print("[%d/%d] %s\n      %s" % (index, len(todo), label, entry["url"]))
        row = {"file": label, "year": entry["year"], "kind": entry["kind"],
               "url": entry["url"], "original_url": entry.get("original_url"),
               "note": entry.get("note", ""), "captured_at": now_utc()}
        row.update(capture_one(ladder, entry["url"], dest,
                               scale=float(entry.get("scale", args.scale)),
                               settle=settle_for(entry, args.settle),
                               retries=args.retries, verbose=args.verbose))
        if os.path.exists(dest):
            row.update(pdf_info(dest, entry.get("expect", [])))
            print("      OK %s bytes, %s pages, %s chars, http %s"
                  % (row.get("bytes"), row.get("pages"), row.get("text"),
                     row.get("status")))
            if row.get("expect_missing"):
                print("      WARNING expected text not found: %s"
                      % row["expect_missing"])
                failed.append(label)
        else:
            print("      FAILED - no PDF written")
            failed.append(label)
        results.append(row)
        save_report(results)

    print("\nCaptured %d of %d." % (len(todo) - len(failed), len(todo)))
    if failed:
        print("Needs attention: %s" % ", ".join(failed))
    print("Run `python tools/capture_pdf.py verify` to check the whole archive.")
    return 1 if failed else 0


def cmd_url(args):
    ladder = require_browser()
    dest = os.path.abspath(args.out)
    settle = args.settle
    if any(host in args.url for host in SLOW_HOSTS):
        settle = max(settle, SLOW_HOST_SETTLE)
    stats = capture_one(ladder, args.url, dest, scale=args.scale, settle=settle,
                        retries=args.retries, verbose=False)
    print(json.dumps(stats, indent=2))
    if os.path.exists(dest):
        info = pdf_info(dest)
        print("%s pages, %s chars of text" % (info["pages"], info["text"]))
        print("written to %s" % dest)
        return 0
    return 1


def cmd_verify(args):
    manifest = load_manifest(args.manifest)
    if not have_pypdf():
        print("note: pypdf is not installed, so page counts and content "
              "assertions are skipped.\n      pip install -r "
              "tools/requirements.txt\n")
    problems = 0
    print("%-30s %9s %6s %8s  status" % ("file", "bytes", "pages", "text"))
    for entry in select(manifest["entries"], args.only, args.kind):
        name = out_name(entry)
        dest = os.path.join(args.outdir, name)
        if not os.path.exists(dest):
            print("%-30s %9s %6s %8s  MISSING" % (name, "-", "-", "-"))
            problems += 1
            continue
        info = pdf_info(dest, entry.get("expect", []))
        size = os.path.getsize(dest)
        found = []
        if size < 20000:
            found.append("tiny-file")
        # Only judge text when pypdf could actually read it.
        if info["text"] is not None and info["text"] < 800:
            found.append("little-text")
        if info.get("expect_missing"):
            found.append("missing=%s" % info["expect_missing"])
        if found:
            problems += 1
        print("%-30s %9d %6s %8s  %s"
              % (name, size, info["pages"], info["text"],
                 "ok" if not found else "SUSPECT " + " ".join(found)))
    print("\n%d problem(s)." % problems)
    return 1 if problems else 0


def cmd_text(args):
    if not have_pypdf():
        die("pypdf is required to read a PDF back: "
            "pip install -r tools/requirements.txt")
    pages, text = pdf_text(os.path.abspath(args.pdf))
    print("--- %s: %d pages, %d chars ---" % (args.pdf, pages, len(text)))
    if args.grep:
        haystack = norm(text)
        for needle in args.grep.split(","):
            print("  %-44r -> %s" % (needle.strip(), norm(needle) in haystack))
    else:
        print(text[:args.limit])
    return 0


def cmd_list(args):
    manifest = load_manifest(args.manifest)
    entries = select(manifest["entries"], args.only, args.kind)
    for entry in entries:
        name = out_name(entry)
        present = "present" if os.path.exists(
            os.path.join(args.outdir, name)) else "MISSING"
        print("%-30s %-8s %s" % (name, present, entry["url"]))
    print("\n%d entries." % len(entries))
    return 0


def cmd_doctor(args):
    """Say whether this machine can run a capture, and what it would use."""
    ok = True
    browser = find_browser()
    override = os.environ.get(BROWSER_ENV)
    print("browser  : %s" % (browser or "NOT FOUND"))
    if override:
        print("           (from %s=%s)" % (BROWSER_ENV, override))
    if not browser:
        ok = False
        print("           install Chrome, Chromium or Edge, or set %s"
              % BROWSER_ENV)

    print("pypdf    : %s" % ("installed" if have_pypdf() else
                             "missing (verify/text degrade; "
                             "pip install -r tools/requirements.txt)"))
    print("python   : %s" % sys.version.split()[0])

    try:
        manifest = load_manifest(args.manifest)
        entries = manifest["entries"]
        years = sorted({e["year"] for e in entries})
        print("manifest : %s (%d entries, %d years: %s .. %s)"
              % (args.manifest, len(entries), len(years), years[0], years[-1]))
    except SystemExit:
        return 2

    present = sum(1 for e in entries
                  if os.path.exists(os.path.join(args.outdir, out_name(e))))
    print("archive  : %s (%d of %d captured)"
          % (args.outdir, present, len(entries)))

    if args.smoke:
        if not browser:
            print("\nsmoke    : skipped, no browser")
            return 1
        import tempfile
        dest = os.path.join(tempfile.mkdtemp(prefix="capture-smoke-"),
                            "smoke.pdf")
        print("\nsmoke    : capturing https://example.com ...")
        stats = capture_one(Ladder(browser=browser), "https://example.com", dest,
                            scale=0.7, settle=1.0, retries=1)
        if os.path.exists(dest):
            print("smoke    : OK %s bytes, http %s -> %s"
                  % (stats.get("bytes"), stats.get("status"), dest))
        else:
            ok = False
            print("smoke    : FAILED %s" % stats.get("error"))

    print("\n%s" % ("Ready." if ok else "Not ready - see above."))
    return 0 if ok else 1


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    subcommands = parser.add_subparsers(dest="command", required=True)

    def shared(sub, manifest=True, outdir=True, filters=False):
        if manifest:
            sub.add_argument("--manifest", default=DEFAULT_MANIFEST,
                             help="manifest JSON (default: tools/sources.json)")
        if outdir:
            sub.add_argument("--outdir", default=DEFAULT_OUTDIR,
                             help="where the PDFs go "
                                  "(default: original-listings/)")
        if filters:
            sub.add_argument("--only", help="comma-separated years, e.g. 2025,2024")
            sub.add_argument("--kind", help="one kind, e.g. nominees or top10")

    run = subcommands.add_parser("run", help="capture manifest entries")
    shared(run, filters=True)
    run.add_argument("--force", action="store_true",
                     help="re-capture entries that already have a PDF")
    run.add_argument("--dry-run", action="store_true")
    run.add_argument("--retries", type=int, default=3)
    run.add_argument("--scale", type=float, default=0.7)
    run.add_argument("--settle", type=float, default=3.0,
                     help="seconds to wait after load (archives get more)")
    run.add_argument("--verbose", action="store_true")
    run.set_defaults(func=cmd_run)

    url = subcommands.add_parser("url", help="capture one ad-hoc URL")
    url.add_argument("url")
    url.add_argument("out")
    url.add_argument("--scale", type=float, default=0.7)
    url.add_argument("--settle", type=float, default=3.0)
    url.add_argument("--retries", type=int, default=2)
    url.set_defaults(func=cmd_url)

    verify = subcommands.add_parser(
        "verify", help="size, pages, text and content assertions for every PDF")
    shared(verify, filters=True)
    verify.set_defaults(func=cmd_verify)

    listing = subcommands.add_parser("list", help="show the manifest")
    shared(listing, filters=True)
    listing.set_defaults(func=cmd_list)

    text = subcommands.add_parser("text", help="dump or grep one PDF's text")
    text.add_argument("pdf")
    text.add_argument("--grep", help="comma-separated strings to test for")
    text.add_argument("--limit", type=int, default=3000)
    text.set_defaults(func=cmd_text)

    doctor = subcommands.add_parser("doctor", help="check this machine's setup")
    shared(doctor)
    doctor.add_argument("--smoke", action="store_true",
                        help="also capture example.com as a live test")
    doctor.set_defaults(func=cmd_doctor)

    args = parser.parse_args()
    try:
        return args.func(args)
    except KeyboardInterrupt:
        print("\ninterrupted", file=sys.stderr)
        return 130


if __name__ == "__main__":
    sys.exit(main())
