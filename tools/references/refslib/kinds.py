"""What kind of thing a reference is.

"Full content" means something different per kind, so the kind decides which
extractor runs and, before that, whether a page belongs in the browser ladder at
all. The measured case: 13 YouTube pages classified as `js-rendered`, which is
true and useless. A video reference is metadata, description and captions; it is
not an article whose body a browser should be waiting for.

Kind is decided from the URL first and the response second, because the URL is
what the archive has before it fetches anything.
"""

import re
from urllib.parse import urlsplit

VIDEO_HOSTS = ("youtube.com", "youtu.be", "vimeo.com", "bilibili.com",
               "youku.com", "dailymotion.com")

SLIDE_HOSTS = ("speakerdeck.com", "slideshare.net", "slides.com")

# NEVER DOWNLOADED, WHATEVER THE CITATION SAYS. A program is not a document,
# and this archive has no use for one: the technique lives in the write-up.
# Fetching one gains nothing and costs plenty - it puts an executable on the
# maintainer's disk and in the content store, where a scanner will eventually
# find it.
#
# `.chm` is in the list for the reason the whole list exists: it LOOKS like a
# help file and is a compiled, scriptable Windows binary. Judge by what a format
# can execute, not by how harmless its name sounds. Archive formats are here too
# because what is inside one is not known until it is unpacked, and unpacking is
# how an executable arrives without ever being named.
#
# Source TEXT is not an executable and stays archivable: `.py`, `.ps1`, `.cs`
# and friends are read as text, never run.
EXECUTABLE_SUFFIXES = frozenset((
    # Windows
    ".exe", ".dll", ".msi", ".msix", ".appx", ".com", ".scr", ".cpl", ".ocx",
    ".sys", ".drv", ".efi", ".chm", ".hta", ".lnk", ".pif", ".vbe", ".jse",
    ".wsf", ".wsh", ".msc", ".reg", ".ps1xml",
    # macOS
    ".dmg", ".pkg", ".app", ".mpkg", ".kext",
    # Linux and BSD
    ".deb", ".rpm", ".appimage", ".snap", ".flatpak", ".run", ".ko", ".so",
    # Cross-platform runtimes and mobile
    ".jar", ".war", ".ear", ".apk", ".aab", ".ipa", ".xpi", ".crx", ".swf",
    ".air", ".elf", ".o", ".a", ".dylib", ".bin", ".out", ".wasm",
    # Disc and disk images: a container for any of the above
    ".iso", ".img", ".vhd", ".vhdx", ".vmdk", ".ova", ".ovf",
    # Archives: the contents are unknown until unpacked, and unpacking is how an
    # executable arrives unnamed.
    ".zip", ".rar", ".7z", ".tar", ".gz", ".tgz", ".bz2", ".xz", ".cab",
    ".arj", ".lzh", ".ace", ".zst",
))

DOCUMENT_SUFFIXES = {
    ".pdf": "whitepaper",
    ".ppt": "slides", ".pptx": "slides",
    ".doc": "whitepaper", ".docx": "whitepaper",
    ".txt": "code", ".py": "code", ".cs": "code", ".ps1": "code",
    ".json": "code", ".xml": "code", ".yaml": "code", ".yml": "code",
}

CONTENT_TYPE_KINDS = (
    ("application/pdf", "whitepaper"),
    ("presentationml", "slides"),
    ("application/vnd.ms-powerpoint", "slides"),
    ("text/plain", "code"),
    ("image/", "image"),
)

# A repository URL is a package, not a page: the owner/name pair with nothing
# after it. A URL deeper into the tree is a FILE in a repository, which is a
# different thing and is archived as code.
GITHUB_REPO = re.compile(r"^/([\w.-]+)/([\w.-]+?)(?:\.git)?/?$")

# github.com/<something>/<something> is NOT always a repository. These first
# segments are GitHub's own pages, and treating them as repositories sent six
# security advisories to `git clone` and failed all six.
GITHUB_RESERVED = frozenset((
    "advisories", "orgs", "topics", "features", "settings", "sponsors",
    "collections", "events", "explore", "marketplace", "notifications",
    "pulls", "issues", "security", "enterprise", "about", "site", "apps",
))


def from_url(url):
    """The kind implied by the address alone, or "" when it is not obvious.

    A WAYBACK REPLAY IS NOT ITS OWN KIND. `web.archive.org/web/<ts>/<url>` has
    the archive's host, so every rule below read the wrapper rather than the
    page: five YouTube talks and a PDF cited as replays were filed as `article`,
    which sent a video into the browser ladder and put it on the document-gaps list
    as though a write-up were missing. The kind belongs to what was CAPTURED.
    """
    from . import wayback
    url = wayback.original_url(url or "")
    parts = urlsplit(url or "")
    host = (parts.hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]
    path = parts.path or "/"

    # Asked BEFORE every other rule, including the document suffixes: a
    # `.zip` on a research host is still an archive, and `github.com/o/n.git`
    # must not become a clone. Nothing downloads what this returns.
    if _suffix(path) in EXECUTABLE_SUFFIXES:
        return "executable"

    if any(host == video or host.endswith("." + video) for video in VIDEO_HOSTS):
        return "video"
    if host in SLIDE_HOSTS:
        return "slides"
    if host == "docs.google.com":
        if path.startswith("/presentation/d/"):
            return "slides"
        if path.startswith("/document/d/"):
            return "whitepaper"
    if host == "github.com":
        match = GITHUB_REPO.match(path)
        if match and match.group(1).lower() not in GITHUB_RESERVED:
            return "repo"
        if "/advisories/" in path or path.startswith("/advisories"):
            return "advisory"
        if "/issues/" in path or "/pull/" in path or "/discussions/" in path:
            return "article"
        # A repository is a fine place to publish a paper, and three browser
        # security whitepapers live in one. Calling those "code" sent them down
        # the source-file route, which read several megabytes of PDF as text.
        # The suffix decides first; only what it does not recognise is code.
        return DOCUMENT_SUFFIXES.get(_suffix(path), "code")

    suffix = _suffix(path)
    if suffix in DOCUMENT_SUFFIXES:
        return DOCUMENT_SUFFIXES[suffix]
    if "advisor" in path or "/cve" in path.lower() or host.endswith("zerodayinitiative.com"):
        return "advisory"
    # Vendor documentation, recognised by PATH rather than by naming a vendor,
    # so a fork inherits the rule instead of this corpus's hosts.
    if "/docs/" in path or "/documentation/" in path:
        return "vendor-doc"
    return ""


def never_download(kind):
    """Whether this kind must never be fetched to disk at all."""
    return kind == "executable"


def from_response(url, content_type):
    """Refine the kind once a response has actually been seen."""
    kind = from_url(url)
    if kind:
        return kind
    lowered = (content_type or "").lower()
    for marker, name in CONTENT_TYPE_KINDS:
        if marker in lowered:
            return name
    return "article"


def wants_browser(kind):
    """Whether a walled or script-rendered page of this kind is worth a browser.

    A video page is never worth it: its useful content is metadata and captions,
    which come from the platform rather than from the rendered DOM. Driving a
    browser at one costs 90 seconds to obtain a player.
    """
    return kind not in ("video", "image")


def _suffix(path):
    tail = path.rsplit("/", 1)[-1].lower()
    if "." not in tail:
        return ""
    return "." + tail.rsplit(".", 1)[-1]
