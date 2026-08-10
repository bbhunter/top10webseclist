"""Trim the publisher's furniture off a converted document.

Container-level chrome removal (`extract_html`) catches a `<footer>` or a
`class="newsletter"`. It cannot catch furniture that sits in the article's own
flow with no class worth naming, and a lot of it does:

    ## Ready to engage
    with our team?

    [ Get in touch ](https://vendor.example/contact)

     Copyright 2026 The Vendor

That is the end of seven archived files. Another twenty-one end with a vendor's
"Learn how it works / See how you're protected" panel, nine with Medium's "Press
enter or click to view image in full size", and several with "Back to all" or
"Author Posts". None of it is the research.

THE PATTERNS COME FROM THE CORPUS, not from imagination: every one below was
found by counting the trailing blocks of all 503 archived documents. So were the
headings that must SURVIVE - `## References` (20 files), `## See also` (15),
`## Conclusion`, `### Disclosure timeline`, `### Credit` - and none of the rules
here touches them.

FOUR SAFETY RULES, because deleting content is worse than keeping an advert:

* Trimming works INWARD FROM THE EDGES and stops at the first block that is not
  furniture. An advert in the middle of an article stays; that is the price of
  not guessing.
* A block holding a fenced code block is never furniture.
* A long block is never furniture. Calls to action are short.
* No trim may take a large share of the document, the same rule the container
  chrome removal already lives under.

Every removal is REPORTED, so "we deleted something interesting" reaches the
record rather than quietly disappearing.
"""

import re

# A block this long is an article, whatever words it contains.
MAX_FURNITURE_CHARS = 400

# How many blocks to consider at each end, and the most of the document any
# trim may take.
MAX_BLOCKS_PER_EDGE = 8
MAX_SHARE = 0.25

# Each entry is (label, pattern). The label is what gets recorded, so a reader
# of the manifest can see WHICH rule fired rather than just "something went".
FURNITURE = (
    ("call-to-action", r"\bready to (?:engage|get started)\b|\bget in touch\b"
                       r"|\bcontact us\b|\bbook a demo\b|\brequest a demo\b"
                       r"|\btalk to (?:us|an expert)\b|\bstart your free trial\b"),
    ("copyright", r"\bcopyright\s*(?:\(c\)|©)?\s*(?:19|20)\d\d\b"
                  r"|\ball rights reserved\b|©\s*(?:19|20)\d\d"),
    ("vendor-panel", r"\blearn how it works\b|\bsee how you'?re protected\b"
                     r"|\bfeatured resources\b|\bwhy choose\b"),
    ("site-navigation", r"^\s*(?:back to all|author posts|previous|next|home)\s*$"
                        r"|\bback to (?:blog|top|all posts)\b"),
    ("subscribe", r"\bsubscribe to (?:our|the)\b|\bsign up for (?:our|the)\b"
                  r"|\bjoin our (?:newsletter|mailing list)\b|\bfollow us on\b"),
    ("share", r"\bshare (?:this|on)\b|\bshare this (?:post|article)\b"),
    ("legal", r"\bprivacy policy\b.*\bterms\b|\bterms of (?:use|service)\b"
              r"|\bcookie (?:policy|preferences)\b"),
    # A trailing byline: the avatar, the words, and the name heading left behind
    # when the two above it go. The author is already in the file's frontmatter,
    # so this is furniture rather than lost attribution.
    ("author-byline", r"^\s*written by\s*$|gravatar\.com/avatar"
                      r"|^\s*posted (?:by|in|on)\b"),
    # A block that is nothing but an image, or nothing but the tail of a link
    # whose text was in the previous block. Both are what a navigation panel
    # looks like after conversion, and a ZDI footer is eight of them in a row:
    # "Submit a vulnerability", "](.../portal/login/) [", "#### VENDORS",
    # "Learn how it works", and so on. The dangling fragment is what stopped the
    # tail sweep before it reached any of the rest.
    # An image with NO alt text. The empty alt is load-bearing: on a slide host
    # every slide is an image whose alt text IS the slide, and a rule that
    # matched any image-only block deleted 2,115 characters of one deck -
    # "ACTUAL MITIGATIONS / NEVER FORWARD AN AMBIGUOUS REQUEST", the conclusions,
    # and the questions slide.
    ("image-only", r"\A!\[\s*\]\([^)]*\)\Z"),
    ("link-fragment", r"\A\]\(\S+\)\s*\[?\Z|\A\[?\s*\]\(\S+\)\Z"),
    ("submit-panel", r"^\s*submit a vulnerability\s*$|^\s*#{2,6}\s*"
                     r"(?:vendors|organizations|researchers)\s*$"),
)

# Lines that are junk WHEREVER they appear, because they describe the website's
# behaviour rather than the document. Kept to exact, unambiguous wordings.
JUNK_LINES = (
    ("image-caption-hint", r"^\s*press enter or click to view image in full size\s*$"),
    ("skip-link", r"^\s*skip to (?:main )?content\s*$"),
)

_FURNITURE = [(label, re.compile(pattern, re.IGNORECASE | re.MULTILINE))
              for label, pattern in FURNITURE]
_JUNK = [(label, re.compile(pattern, re.IGNORECASE | re.MULTILINE))
         for label, pattern in JUNK_LINES]

FENCE = re.compile(r"^```", re.MULTILINE)


# WHAT A DEAD LINK LEAVES BEHIND. `[  ►  ]()` and `[↩︎]()` are a carousel arrow
# and a footnote's return arrow: once the empty target goes, the glyph is a line
# of its own that means nothing without the anchor it belonged to. Named
# individually rather than "any line of punctuation", because `---`, `|`, `>`
# and `*` are all Markdown that carries meaning, and a shell prompt or an ASCII
# diagram is content.
DECORATION = frozenset("►▶◄◀▲▼→←↑↓↩↪⇧⇨•·◦∙‣⁃🔗📎⌘¶§#*_~")
VARIATION_SELECTORS = frozenset("︎️")

# Empty-target link syntax, innermost first so `[![alt](img)]()` loses the outer
# construct and keeps the image.
_DEAD_IMAGE = re.compile(r"!\[[^\]\n]*\]\(\s*\)")
_DEAD_LINK = re.compile(r"\[([^\[\]\n]*)\]\(\s*\)")
# An anchor that wrapped BLOCK content converts with its brackets on lines of
# their own, so the single-line rule cannot see it - a collapsible "TOC Element"
# toggle and a site's "Platform / Solutions / Resources" menu both land this way.
# Bounded and tempered: the body may not contain another bracket or a live link
# target, so a stray `[` early in a document can never swallow the article.
_DEAD_BLOCK_ANCHOR = re.compile(
    r"(?<!!)\[[ \t]*\n((?:(?!\]\()[^\[\]]){0,400}?)\n[ \t]*\]\(\s*\)")
_FENCED = re.compile(r"^```.*?^```", re.MULTILINE | re.DOTALL)


def drop_dead_links(markdown):
    """(text, [labels]) with empty-target link syntax reduced to its label.

    A LINK WITH NO TARGET IS NOT A LINK, wherever it appears - so unlike `trim`
    this works over the whole document rather than inward from the edges. It is
    a syntax rule, not a judgement about content: `[Data request]()` becomes
    `Data request`, and nothing that a reader can act on is lost, because there
    was never anywhere to go.

    Fenced code is left exactly as it is. A write-up about Markdown injection
    quotes this syntax on purpose, and rewriting a payload is the one thing this
    archive must never do.
    """
    # NUL FIRST, because the fenced blocks are held behind `\x00N\x00` tokens and
    # this runs BEFORE `sanitise_text` removes control characters. A document
    # carrying its own NUL could otherwise forge a token and have another of its
    # own code blocks pasted in its place.
    text = (markdown or "").replace("\x00", "")
    removed = []
    held = []

    def hold(match):
        held.append(match.group(0))
        return "\x00%d\x00" % (len(held) - 1)

    body = _FENCED.sub(hold, text)

    before = body
    body = _DEAD_IMAGE.sub("", body)
    if body != before:
        removed.append("dead-image")

    before = body
    # Twice: `[[label]()]()` is a real shape on wiki-style pages, and one pass
    # only reaches the inner one.
    for _ in range(2):
        body = _DEAD_LINK.sub(lambda match: match.group(1), body)
    if body != before:
        removed.append("dead-link")

    before = body
    body = _DEAD_BLOCK_ANCHOR.sub(lambda match: match.group(1), body)
    if body != before:
        removed.append("dead-block-anchor")

    before = body
    body = "\n".join(line for line in body.split("\n") if not _is_decoration(line))
    if body != before:
        removed.append("orphaned-decoration")

    # Three or more blank lines is what a removed block leaves behind. Only when
    # something WAS removed: reflowing a document this rule did not touch turns a
    # surgical fix into a whole-corpus rewrite.
    if removed:
        body = re.sub(r"\n{3,}", "\n\n", body)
    text = re.sub(r"\x00(\d+)\x00", lambda match: held[int(match.group(1))], body)
    return text, sorted(set(removed))


_RULE = re.compile(r"^(?:\*{3,}|_{3,}|-{3,})$")


def _is_decoration(line):
    """True for a line that is only the glyph a dead anchor was wrapped around."""
    stripped = (line or "").strip()
    if not stripped or len(stripped) > 4:
        return False
    # `***` and `___` are horizontal rules made of characters this set contains.
    if _RULE.match(stripped):
        return False
    return all(char in DECORATION or char in VARIATION_SELECTORS
               for char in stripped)


def trim(markdown):
    """(text, [labels]) with the publisher's furniture removed from the edges."""
    text = markdown or ""
    removed = []

    for label, pattern in _JUNK:
        cleaned = pattern.sub("", text)
        if cleaned != text:
            removed.append(label)
            text = cleaned

    blocks = re.split(r"\n\s*\n", text)
    budget = max(len(text) * MAX_SHARE, 0)

    taken = 0
    # The tail first, then the head. Both stop at the first real block.
    for end in ("tail", "head"):
        for _ in range(MAX_BLOCKS_PER_EDGE):
            if len(blocks) < 2:
                break
            index = len(blocks) - 1 if end == "tail" else 0
            label = _furniture(blocks[index])
            if not label:
                break
            if taken + len(blocks[index]) > budget:
                break
            taken += len(blocks[index])
            removed.append(label)
            blocks.pop(index)

    text = "\n\n".join(block for block in blocks).strip() + "\n"
    return text, sorted(set(removed))


def _furniture(block):
    """The label of the rule this block matches, or "" when it is content."""
    body = (block or "").strip()
    if not body or len(body) > MAX_FURNITURE_CHARS:
        return ""
    if FENCE.search(body):
        return ""
    for label, pattern in _FURNITURE:
        if pattern.search(body):
            return label
    return ""
