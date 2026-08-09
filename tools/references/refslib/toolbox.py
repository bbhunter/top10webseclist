"""The sandbox for data collection this tool will not do in-process.

ONE CONTAINER, several jobs. Everything here shares a property: it is either
third-party code the archive would otherwise run on this machine, or a fetch
that deliberately relaxes something the in-process client must never relax.
Keeping both in one place means the in-process fetcher stays strict, the
third-party code stays contained, and there is a single set of container rules
to read rather than one per tool.

What lives here today:

* **`captions`** - `yt-dlp`, for a talk's transcript.
* **`fetch_insecure`** - `curl` WITHOUT certificate verification, for a source
  whose certificate has expired. The maintainer decided on 2026-08-04 that this
  is acceptable for collecting a public document. It lives here rather than in
  the fetcher so that "our client always verifies" stays true: the exception is
  a different process, in a container, and cannot be reached by accident.
* **`fetch_public`** - ordinary verified `curl`, for a public archive endpoint
  that serves different bytes to Python's HTTP stack. It is a second client,
  not a certificate bypass, and its bytes face the ordinary archive guards.
* **`pdf_page_images`** - `pdftoppm`, rendering a PDF whose text layer is
  unreadable into one image per page, so a reader can be shown the pages.
* **`browser_dom`** - Chromium in headless mode, for a page whose useful DOM
  appears only after JavaScript has run and a short wait has elapsed.
* **`browser_pdf`** - Chromium in headless mode, printing the archive's inert,
  self-contained HTML to PDF without giving a host browser the document.
* **`waymore_urls`** - pinned waymore, querying several public URL indexes for
  migrations and alternate paths after direct Wayback lookup fails.

Original note, on why the first of these needed a container at all:

WHY A CONTAINER. These are the places the archive runs code that is not this
repository's. `yt-dlp` is a large, fast-moving project that exists to keep up
with a hostile platform; `pdftoppm` is a C parser fed documents chosen by
somebody else. Running either directly would give it this machine, this checkout
and the content store; running it in a container gives it a throwaway directory
and nothing else. The maintainer asked for exactly this, and it is the right
call whatever a tool's reputation.

WHY IT IS NEEDED AT ALL. Measured 2026-08-04: YouTube refuses timed text by
every route this tool owns. A plain fetch gets http 404 or a zero-byte body; the
same fetch made BY the page, with its session and origin, gets a zero-byte body;
and the page's own "Show transcript" opens a panel that spins forever. The
caption URL now needs a token the real player generates. `yt-dlp` asks a
different player client that still answers, which is why 13 talks in this corpus
have transcripts again.

WHAT THE CONTAINER GETS, and nothing more:

* one throwaway output directory, the only writable mount;
* no repository, no content store, no home directory, no environment variables;
* a read-only root filesystem with a small no-exec tmpfs for scratch;
* every capability dropped, no new privileges, a memory and process cap;
* a non-root user inside.

It does get the NETWORK, because fetching is the job. Nothing it downloads is
executed: the output is JSON that this module parses.

OPTIONAL BY DESIGN. No Docker, or no image, means a clear skip with a reason,
never a failure and never a silent empty transcript.
"""

import json
import os
import re
import shutil
import subprocess
import tempfile

# Pinned. The base image is pinned by DIGEST so a rebuild cannot silently become
# a different image, and yt-dlp by version so a run is reproducible. YouTube
# breaks these tools regularly, so expect to bump YT_DLP when a fetch starts
# failing - that is a deliberate, visible edit rather than a moving tag.
BASE_IMAGE = ("python:3.12-alpine@sha256:"
              "6d43704baacd1bfbe7c295d7f13079d5d8104ed33568873133f8fc69980419df")
YT_DLP = "2026.07.04"
WAYMORE = "8.9"
IMAGE = "webseclist-refs-toolbox:" + YT_DLP + "-chromium-waymore-2"

# `curl` for the certificate exception, `poppler-utils` for `pdftoppm`, and
# Chromium for rendered DOM collection. Their
# versions come from the pinned base image's package repository rather than
# being pinned themselves: pinning an apk version breaks the build the moment
# that repository moves on, and the digest pin already fixes the distribution
# release. A stated limit rather than an oversight.
#
# `poppler-data` IS NOT OPTIONAL, and its absence fails silently. It carries the
# CJK character-collection maps (Adobe-Japan1, Adobe-GB1, Adobe-Korea1); without
# them poppler cannot map an `Identity-H` CID font and DROPS EVERY GLYPH IT
# CANNOT MAP - `pdftotext` returns the Latin fragments only, `pdftoppm` renders
# the slide with its Japanese text simply absent, and neither reports an error a
# caller can see. A 180-page Japanese conference deck came back as bullets and
# emoji, was judged a broken text layer, and had 103 blank-ish pages transcribed
# by hand from renders that had already thrown the text away. With the pack the
# same file extracts cleanly and needs no transcription at all.
DOCKERFILE = """FROM %s
RUN apk add --no-cache chromium curl poppler-utils poppler-data \\
 && pip install --no-cache-dir "yt-dlp==%s" "waymore==%s" \\
 && adduser -D -u 10001 fetcher
USER fetcher
""" % (BASE_IMAGE, YT_DLP, WAYMORE)

# What the container may spend. A talk's caption track is a few hundred KB, so
# these are generous; they exist to bound a runaway, not to tune throughput.
MEMORY = "512m"
PIDS = "256"
TIMEOUT = 900

RUN_ARGS = (
    "--rm",
    "--network", "bridge",
    "--read-only",
    "--tmpfs", "/tmp:rw,noexec,nosuid,size=64m",
    "--cap-drop", "ALL",
    "--security-opt", "no-new-privileges",
    "--memory", MEMORY,
    "--pids-limit", PIDS,
)


def run_args():
    """Container isolation arguments, using the host's non-root UID on POSIX.

    The image's fixed UID 10001 cannot write a bind-mounted directory owned by
    the operator. `pdftoppm` therefore produced no pages and yt-dlp could not
    save captions. Run as the host UID/GID where those exist; Docker Desktop's
    file sharing handles ownership itself on platforms without `getuid`.
    """
    args = list(RUN_ARGS)
    if hasattr(os, "getuid") and hasattr(os, "getgid"):
        args += ["--user", "%d:%d" % (os.getuid(), os.getgid())]
    return args


def _run_container(command, timeout, stdout=subprocess.PIPE, stderr=subprocess.PIPE):
    """Run one disposable container and force-remove it on every exit path.

    Docker's ``--rm`` only runs after the container process exits. If the host
    client times out or is interrupted, killing that client can leave Chromium
    running indefinitely. A host-side cidfile lets this wrapper remove the
    exact container in ``finally`` without matching names, images, or other
    Docker work.
    """
    control = tempfile.mkdtemp(prefix="webseclist_refs_container_")
    cidfile = os.path.join(control, "cid")
    command = list(command[:2]) + ["--cidfile", cidfile] + list(command[2:])
    try:
        return subprocess.run(command, stdout=stdout, stderr=stderr, timeout=timeout)
    finally:
        identifier = ""
        try:
            with open(cidfile, "r", encoding="ascii") as handle:
                identifier = handle.read().strip()
        except OSError:
            pass
        if re.fullmatch(r"[0-9a-f]{12,64}", identifier):
            try:
                subprocess.run(["docker", "rm", "--force", identifier],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                               timeout=30)
            except (OSError, subprocess.SubprocessError):
                pass
        shutil.rmtree(control, ignore_errors=True)

# Captions only, never the media. `--skip-download` is what keeps a 400 MB video
# off this machine; the rest asks for English, manual first then automatic.
YT_DLP_ARGS = (
    "--skip-download",
    "--write-subs",
    "--write-auto-subs",
    "--sub-langs", "en.*",
    "--sub-format", "json3",
    "--no-playlist",
    "--no-progress",
    "--ignore-errors",
    "-o", "%(id)s",
    "-P", "/out",
)

VIDEO_ID = re.compile(r"(?:v=|youtu\.be/|/embed/|/shorts/)([A-Za-z0-9_-]{6,})")


class Unavailable(Exception):
    """No container runtime, or the image could not be built. Reported, never guessed."""


def video_id(url):
    """The YouTube id in this URL, or ""."""
    match = VIDEO_ID.search(str(url or ""))
    return match.group(1) if match else ""


def available():
    """True when a container runtime is present and answering."""
    if not shutil.which("docker"):
        return False
    try:
        done = subprocess.run(["docker", "info", "--format", "{{.ServerVersion}}"],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
        return done.returncode == 0
    except (OSError, subprocess.SubprocessError):
        return False


def ensure_image(log=None):
    """Build the pinned image if it is not present. Returns the image tag."""
    if not available():
        raise Unavailable("no container runtime: install Docker, or skip the container route")
    have = subprocess.run(["docker", "image", "inspect", IMAGE],
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if have.returncode == 0:
        return IMAGE
    if log:
        log("building %s (yt-dlp %s, pinned base image)" % (IMAGE, YT_DLP))
    build = subprocess.run(["docker", "build", "-t", IMAGE, "-"],
                           input=DOCKERFILE.encode("utf-8"),
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=TIMEOUT)
    if build.returncode != 0:
        raise Unavailable("could not build the reference toolbox image: "
                          + build.stdout.decode("utf-8", "replace")[-400:])
    return IMAGE


def fetch(urls, log=None):
    """{video url: json3 caption text} for as many as answered.

    A url that produced nothing is simply absent from the result: the caller
    reports it as a gap, exactly as before. One container run covers the whole
    batch, so the image is built and started once rather than per video.
    """
    urls = [url for url in urls if video_id(url)]
    if not urls:
        return {}
    ensure_image(log=log)

    output = tempfile.mkdtemp(prefix="webseclist_refs_captions_")
    try:
        command = ["docker", "run"] + run_args()
        command += ["-v", _mount(output) + ":/out"]
        command += [IMAGE, "yt-dlp"] + list(YT_DLP_ARGS) + urls
        if log:
            log("fetching %d caption track(s) in a container" % len(urls))
        done = _run_container(command, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, timeout=TIMEOUT)
        if done.returncode != 0 and log:
            # --ignore-errors means a non-zero exit can still have produced most
            # of the batch, so this is reported and the results are still read.
            log("yt-dlp exited %d; reading whatever it wrote"
                % done.returncode)
        return _collect(urls, output)
    except subprocess.TimeoutExpired:
        raise Unavailable("the transcript container did not finish within %ds" % TIMEOUT)
    finally:
        shutil.rmtree(output, ignore_errors=True)


CURL_ARGS = (
    "--silent", "--show-error", "--location", "--max-redirs", "5",
    "--max-time", "60", "--max-filesize", "33554432",
    "--user-agent", "webseclist-refs/1 (reference archive)",
)


def fetch_insecure(url, log=None):
    """Fetch a URL WITHOUT verifying its certificate. Returns bytes.

    Maintainer decision 2026-08-04: acceptable for collecting a public document
    from a source whose certificate has expired. One reference in this corpus
    needs it, and the browser recorded the interstitial as if it were the page.

    It lives in the container and not in the fetcher on purpose. "Our client
    always verifies" stays true, because the exception is a different process
    behind a container boundary that nothing else reaches by accident, and what
    comes back is bytes that go through the same extraction as any other fetch.
    """
    ensure_image(log=log)
    output = tempfile.mkdtemp(prefix="webseclist_refs_insecure_")
    try:
        command = ["docker", "run"] + run_args()
        command += ["-v", _mount(output) + ":/out"]
        command += [IMAGE, "curl", "--insecure"] + list(CURL_ARGS)
        command += ["--output", "/out/body", url]
        if log:
            log("fetching without certificate verification, in a container")
        done = _run_container(command, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, timeout=TIMEOUT)
        body = b""
        path = os.path.join(output, "body")
        if os.path.exists(path):
            with open(path, "rb") as handle:
                body = handle.read()
        if not body:
            raise Unavailable("the insecure fetch returned nothing: "
                              + done.stdout.decode("utf-8", "replace")[-200:])
        return body
    except subprocess.TimeoutExpired:
        raise Unavailable("the insecure fetch did not finish within %ds" % TIMEOUT)
    finally:
        shutil.rmtree(output, ignore_errors=True)


def fetch_public(url, log=None):
    """Fetch public bytes with verified curl inside the locked-down container.

    This is a bounded fallback for route-dependent archive responses. It does
    not disable TLS verification and it never executes what it downloads.
    """
    ensure_image(log=log)
    output = tempfile.mkdtemp(prefix="webseclist_refs_public_")
    try:
        command = ["docker", "run"] + run_args()
        command += ["-v", _mount(output) + ":/out"]
        command += [IMAGE, "curl"] + list(CURL_ARGS)
        command += ["--output", "/out/body", url]
        if log:
            log("fetching with verified curl, in a container")
        done = _run_container(command, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, timeout=TIMEOUT)
        body = b""
        path = os.path.join(output, "body")
        if os.path.exists(path):
            with open(path, "rb") as handle:
                body = handle.read()
        if not body:
            raise Unavailable("the container fetch returned nothing: "
                              + done.stdout.decode("utf-8", "replace")[-200:])
        return body
    except subprocess.TimeoutExpired:
        raise Unavailable("the container fetch did not finish within %ds" % TIMEOUT)
    finally:
        shutil.rmtree(output, ignore_errors=True)


def waymore_urls(domains, log=None, limit_requests=50):
    """Collect historical URLs from waymore's public indexes in Docker.

    Inputs are domain names, not arbitrary command fragments. The container
    receives one throwaway directory and no repository, store, home directory,
    or credentials. Results are evidence for source research; callers must
    still verify a candidate is the cited document before importing it.
    """
    domains = sorted(set(str(domain or "").strip().lower() for domain in domains
                         if re.fullmatch(r"[a-z0-9.-]+",
                                         str(domain or "").strip().lower())))
    if not domains:
        return []
    ensure_image(log=log)
    work = tempfile.mkdtemp(prefix="webseclist_refs_waymore_")
    try:
        source = os.path.join(work, "targets.txt")
        target = os.path.join(work, "urls.txt")
        with open(source, "w", encoding="ascii") as handle:
            handle.write("\n".join(domains) + "\n")
        command = ["docker", "run"] + run_args()
        command += ["--env", "HOME=/tmp", "-v", _mount(work) + ":/work"]
        command += [IMAGE, "waymore", "-i", "/work/targets.txt", "-mode", "U",
                    "--providers", "commoncrawl,otx,urlscan", "-lcc", "5",
                    "-r", "0", "-oU", "/work/urls.txt", "-ow", "-lr",
                    str(limit_requests)]
        if log:
            log("querying historical URL indexes for %d domain(s) with waymore %s, "
                "in a container" % (len(domains), WAYMORE))
        done = _run_container(command, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, timeout=TIMEOUT)
        if not os.path.exists(target):
            raise Unavailable("waymore wrote no URL result: "
                              + done.stdout.decode("utf-8", "replace")[-300:])
        return _waymore_results(target)
    except subprocess.TimeoutExpired:
        if os.path.exists(target):
            partial = _waymore_results(target)
            if partial:
                if log:
                    log("waymore reached its %ds limit; keeping %d partial URL(s)"
                        % (TIMEOUT, len(partial)))
                return partial
        raise Unavailable("waymore did not finish within %ds" % TIMEOUT)
    finally:
        shutil.rmtree(work, ignore_errors=True)


def _waymore_results(path):
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        return sorted(set(line.strip() for line in handle
                          if line.strip().startswith(("http://", "https://"))))


# External pages run only in the toolbox. `--dump-dom` serialises the rendered
# document after Chromium has loaded it; the virtual-time budget is the wait
# which lets client-side rendering replace an empty shell. No host directory is
# mounted for this route, and downloads, extensions and background services are
# disabled.
CHROMIUM_ARGS = (
    "--headless=new",
    "--no-sandbox",  # Docker is the sandbox; every container capability is dropped.
    "--disable-dev-shm-usage",
    "--disable-gpu",
    "--disable-extensions",
    "--disable-plugins",
    "--disable-sync",
    "--disable-background-networking",
    "--disable-component-update",
    "--disable-client-side-phishing-detection",
    "--disable-features=Translate,OptimizationHints,MediaRouter",
    "--no-first-run",
    "--no-default-browser-check",
    "--no-service-autorun",
    "--password-store=basic",
    "--use-mock-keychain",
    "--deny-permission-prompts",
    "--disable-file-system",
    "--block-new-web-contents",
    "--dump-dom",
)

# Chromium normally exits within a few seconds of its virtual-time budget. A
# generous 90-second grace let a broken page leave each rung waiting for
# minutes, even though the cidfile wrapper could now clean it up safely. This is
# process-exit grace, not page-rendering time: the caller already owns that
# budget and retries with longer rungs when useful content has not appeared.
BROWSER_PROCESS_GRACE = 20


def browser_dom(url, wait_seconds=10, log=None):
    """Return Chromium's rendered DOM for one public URL, from the container.

    `wait_seconds` becomes Chromium's virtual-time budget. The caller inspects
    visible text and wall markers, and can retry with a longer budget; this
    function deliberately returns evidence, not a truth verdict.
    """
    ensure_image(log=log)
    wait_seconds = max(1.0, min(float(wait_seconds), 120.0))
    milliseconds = int(wait_seconds * 1000)
    command = ["docker", "run"] + run_args()
    command += [IMAGE, "chromium-browser"] + list(CHROMIUM_ARGS)
    command += ["--user-data-dir=/tmp/browser-profile",
                "--virtual-time-budget=%d" % milliseconds, url]
    if log:
        log("rendering the page for %.0fs in headless Chromium, in a container"
            % wait_seconds)
    try:
        done = _run_container(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              timeout=wait_seconds + BROWSER_PROCESS_GRACE)
    except subprocess.TimeoutExpired:
        raise Unavailable("the browser container did not finish after %.0fs" % wait_seconds)
    dom = done.stdout.decode("utf-8", "replace")
    if not dom.strip():
        detail = done.stderr.decode("utf-8", "replace")[-300:]
        raise Unavailable("headless Chromium returned no DOM: " + detail)
    return dom


# PDF printing takes only a local, self-contained HTML file. Network is disabled
# for the entire container, and makepdf renders remote images as labelled links,
# so Chromium cannot turn a PDF build into an accidental third-party fetch.
BROWSER_PDF_ARGS = (
    "--headless=new",
    "--no-sandbox",  # Docker is the sandbox; every container capability is dropped.
    "--disable-dev-shm-usage",
    "--disable-gpu",
    "--disable-extensions",
    "--disable-plugins",
    "--disable-sync",
    "--disable-background-networking",
    "--disable-component-update",
    "--disable-client-side-phishing-detection",
    "--disable-features=Translate,OptimizationHints,MediaRouter",
    "--no-first-run",
    "--no-default-browser-check",
    "--no-service-autorun",
    "--password-store=basic",
    "--use-mock-keychain",
    "--deny-permission-prompts",
    "--disable-file-system",
    "--block-new-web-contents",
    "--no-pdf-header-footer",
    "--run-all-compositor-stages-before-draw",
)


def browser_pdf(html, log=None, image=None):
    """Print self-contained archive HTML to PDF in Docker; return PDF bytes.

    Only one throwaway working directory is mounted. It contains the inert HTML
    on entry and the PDF on exit; the checkout, store, home directory and host
    browser profile are never mounted. The container has no network.
    """
    image = image or ensure_image(log=log)
    work = tempfile.mkdtemp(prefix="webseclist_refs_pdfprint_")
    try:
        source = os.path.join(work, "document.html")
        target = os.path.join(work, "document.pdf")
        with open(source, "w", encoding="utf-8") as handle:
            handle.write(html)
        command = ["docker", "run"] + run_args()
        command = [part if part != "bridge" else "none" for part in command]
        command += ["-v", _mount(work) + ":/work"]
        command += [image, "chromium-browser"] + list(BROWSER_PDF_ARGS)
        command += ["--user-data-dir=/tmp/browser-profile",
                    "--print-to-pdf=/work/document.pdf",
                    "file:///work/document.html"]
        if log:
            log("printing archived Markdown as PDF in headless Chromium, in a container")
        done = _run_container(command, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, timeout=180)
        payload = b""
        if os.path.exists(target):
            with open(target, "rb") as handle:
                payload = handle.read()
        if not payload.startswith(b"%PDF-"):
            raise Unavailable("containerized Chromium produced no PDF: "
                              + done.stdout.decode("utf-8", "replace")[-300:])
        return payload
    except subprocess.TimeoutExpired:
        raise Unavailable("containerized PDF printing did not finish within 180s")
    finally:
        shutil.rmtree(work, ignore_errors=True)


# One image per page, at a resolution a reader can actually read. 150 DPI keeps
# a slide legible while keeping a 60-page deck to a few megabytes.
PDFTOPPM_ARGS = ("-png", "-r", "150")

# `-layout` keeps columns and code indentation, which is most of what a security
# whitepaper's meaning rests on.
PDFTOTEXT_ARGS = ("-layout", "-enc", "UTF-8")


def pdf_text(pdf_bytes, log=None):
    """The text of a PDF, read by poppler in the container. Returns a string.

    THE ROUTE TO TRY BEFORE LOOKING AT PICTURES. The in-process extractor works
    from the PDF's own /ToUnicode map and gives up when that map is absent or
    wrong - correctly, because guessing produces confident nonsense. Poppler
    carries font tables that cover the same documents, and on this corpus it
    read three whitepapers cleanly that the in-process route could only render
    as replacement characters.

    `pdf_page_images` remains the last resort, for a PDF that is genuinely a
    scan: no text layer at all is a different problem from a text layer nothing
    can decode, and only the first needs a reader to look at pages.
    """
    ensure_image(log=log)
    source = tempfile.mkdtemp(prefix="webseclist_refs_pdftext_")
    try:
        with open(os.path.join(source, "in.pdf"), "wb") as handle:
            handle.write(pdf_bytes)
        command = ["docker", "run"] + run_args()
        # No network: this one only reads a file we already hold.
        command = [part if part != "bridge" else "none" for part in command]
        command += ["-v", _mount(source) + ":/in:ro"]
        command += [IMAGE, "pdftotext"] + list(PDFTOTEXT_ARGS)
        command += ["/in/in.pdf", "-"]
        if log:
            log("reading the PDF's text with poppler in a container")
        done = _run_container(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              timeout=TIMEOUT)
        text = done.stdout.decode("utf-8", "replace")
        if not text.strip():
            raise Unavailable("pdftotext produced no text: "
                              + done.stderr.decode("utf-8", "replace")[-200:])
        return text
    except subprocess.TimeoutExpired:
        raise Unavailable("reading the PDF did not finish within %ds" % TIMEOUT)
    finally:
        shutil.rmtree(source, ignore_errors=True)


def pdf_page_images(pdf_bytes, into, first=1, last=0, log=None):
    """Render each page of a PDF to a PNG in `into`. Returns the paths, in order.

    For the PDF whose text layer cannot be read: a scan, or a deck whose glyphs
    carry no usable encoding map. Extracting text from those produces confident
    nonsense - one in this corpus came out with 32% of its words containing a
    vowel - and the honest alternative is to LOOK at the pages.

    This only produces the images. Reading them is a separate, human or model
    step, because deciding what a page says is not a job for a converter.
    """
    ensure_image(log=log)
    source = tempfile.mkdtemp(prefix="webseclist_refs_pdf_")
    try:
        with open(os.path.join(source, "in.pdf"), "wb") as handle:
            handle.write(pdf_bytes)
        command = ["docker", "run"] + run_args()
        command += ["-v", _mount(source) + ":/in:ro", "-v", _mount(into) + ":/out"]
        command += [IMAGE, "pdftoppm"] + list(PDFTOPPM_ARGS)
        command += ["-f", str(first)]
        if last:
            command += ["-l", str(last)]
        command += ["/in/in.pdf", "/out/page"]
        if log:
            log("rendering the PDF to page images in a container")
        done = _run_container(command, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, timeout=TIMEOUT)
        pages = sorted(name for name in os.listdir(into) if name.endswith(".png"))
        if not pages:
            raise Unavailable("pdftoppm produced no pages: "
                              + done.stdout.decode("utf-8", "replace")[-200:])
        return [os.path.join(into, name) for name in pages]
    except subprocess.TimeoutExpired:
        raise Unavailable("rendering the PDF did not finish within %ds" % TIMEOUT)
    finally:
        shutil.rmtree(source, ignore_errors=True)


def _collect(urls, output):
    """Read the json3 files back, preferring a manual track over an automatic one."""
    found = {}
    for url in urls:
        identifier = video_id(url)
        # `<id>.en.json3` is the manual track where one exists; `<id>.en-orig`
        # and the rest are automatic. Prefer the plainest language tag.
        candidates = sorted(
            (name for name in os.listdir(output)
             if name.startswith(identifier + ".") and name.endswith(".json3")),
            key=lambda name: (len(name), name))
        for name in candidates:
            try:
                with open(os.path.join(output, name), "r", encoding="utf-8") as handle:
                    body = handle.read()
            except OSError:
                continue
            if _has_text(body):
                found[url] = body
                break
    return found


def _has_text(body):
    try:
        payload = json.loads(body or "{}")
    except ValueError:
        return False
    return any((segment.get("utf8") or "").strip()
               for event in (payload.get("events") or [])
               for segment in (event.get("segs") or []))


def _mount(path):
    """A host path Docker will accept.

    On Windows a POSIX-style path from a Git Bash shell reaches Docker as
    `C:/Program Files/Git/out` and the run dies on an "invalid working
    directory". Hand it the native path.
    """
    return os.path.abspath(path)
