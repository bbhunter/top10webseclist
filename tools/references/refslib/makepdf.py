"""Turn an archived Markdown file into a self-contained HTML document, and hand
it to the headless browser to print as a PDF.

The `pdf` command exists so a reference can be read or shared as one file. It
prints OUR archived Markdown, not the third-party page: the conversion is
offline and deterministic, it carries the same attribution block the Markdown
does, and nothing here reaches the network. A source that is ALREADY a PDF is
copied rather than re-rendered, so its own typesetting is kept.

The Markdown these files use is small and regular - it is what `render.py` emits
and what the extractors produce - so this is a compact block converter rather
than a full CommonMark implementation. Anything it does not recognise degrades
to a paragraph of escaped text, which is safe: the worst case is plain text, not
broken markup, and never a network fetch. Images are rendered as a labelled link
rather than an `<img>`, precisely so printing cannot pull a remote asset.
"""

import html as html_module
import re

# A print stylesheet, inlined so the document owes nothing to the network. A4
# with comfortable margins; the browser's `preferCSSPageSize` honours the @page.
STYLE = """
@page { size: A4; margin: 18mm 16mm; }
* { box-sizing: border-box; }
body {
  font-family: -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  font-size: 11pt; line-height: 1.5; color: #1b1b1b; margin: 0;
  word-wrap: break-word; overflow-wrap: break-word;
}
h1 { font-size: 20pt; line-height: 1.25; margin: 0 0 .4em; }
h2 { font-size: 15pt; margin: 1.4em 0 .4em; border-bottom: 1px solid #ddd; padding-bottom: .15em; }
h3 { font-size: 13pt; margin: 1.2em 0 .35em; }
h4, h5, h6 { font-size: 11.5pt; margin: 1em 0 .3em; }
p { margin: .5em 0; }
a { color: #0b5cad; text-decoration: none; word-break: break-all; }
ul, ol { margin: .5em 0 .5em 1.4em; padding: 0; }
li { margin: .2em 0; }
blockquote {
  margin: .6em 0; padding: .3em .9em; border-left: 3px solid #cfcfcf;
  color: #444; background: #fafafa;
}
code {
  font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
  font-size: 9.5pt; background: #f2f2f2; padding: .08em .3em; border-radius: 3px;
}
pre {
  background: #f6f8fa; border: 1px solid #e3e3e3; border-radius: 5px;
  padding: .7em .9em; overflow-x: auto; page-break-inside: avoid;
}
pre code { background: none; padding: 0; font-size: 9pt; line-height: 1.4; }
table { border-collapse: collapse; margin: .7em 0; width: 100%; font-size: 10pt; }
th, td { border: 1px solid #ccc; padding: .35em .55em; text-align: left; vertical-align: top; }
th { background: #f2f2f2; }
hr { border: none; border-top: 1px solid #ddd; margin: 1.2em 0; }
img { max-width: 100%; }
.src-note { color: #666; font-size: 9pt; margin-top: 2em; border-top: 1px solid #eee; padding-top: .6em; }
"""

_FENCE = re.compile(r"^\s*```")
_ATX = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
_HR = re.compile(r"^\s*([-*_])(?:\s*\1){2,}\s*$")
_UL = re.compile(r"^(\s*)[-*+]\s+(.*)$")
_OL = re.compile(r"^(\s*)\d+[.)]\s+(.*)$")
_TABLE_SEP = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)+\|?\s*$")
_BLOCKQUOTE = re.compile(r"^\s*>\s?(.*)$")

# Inline constructs. Order matters: code spans are pulled out first and masked so
# nothing inside them is treated as markup.
_CODE_SPAN = re.compile(r"`([^`]+)`")
_IMAGE = re.compile(r"!\[([^\]]*)\]\(\s*([^)\s]+)[^)]*\)")
_LINK = re.compile(r"\[([^\]]+)\]\(\s*([^)\s]+)[^)]*\)")
_BOLD = re.compile(r"(\*\*|__)(?=\S)(.+?)(?<=\S)\1")
_ITALIC = re.compile(r"(?<![\*_\w])([*_])(?=\S)(.+?)(?<=\S)\1(?![\*_\w])")


def strip_frontmatter(text):
    """Drop a leading YAML frontmatter block; the PDF shows the body only."""
    if text.startswith("---\n") or text.startswith("---\r\n"):
        end = text.find("\n---", 3)
        if end != -1:
            rest = text[end + 4:]
            return rest.lstrip("\r\n")
    return text


def _inline(text):
    """Escape a run of prose and apply inline Markdown to it."""
    spans = []

    def stash(match):
        spans.append("<code>%s</code>" % html_module.escape(match.group(1)))
        return "\x00%d\x00" % (len(spans) - 1)

    masked = _CODE_SPAN.sub(stash, text)
    masked = html_module.escape(masked)
    # Images first (a subset of link syntax): render as a labelled link so no
    # remote asset is ever loaded while printing.
    masked = _IMAGE.sub(
        lambda m: '<a href="%s">[image: %s]</a>'
        % (html_module.escape(m.group(2), quote=True), m.group(1) or "image"), masked)
    masked = _LINK.sub(
        lambda m: '<a href="%s">%s</a>'
        % (html_module.escape(m.group(2), quote=True), m.group(1)), masked)
    masked = _BOLD.sub(lambda m: "<strong>%s</strong>" % m.group(2), masked)
    masked = _ITALIC.sub(lambda m: "<em>%s</em>" % m.group(2), masked)
    return re.sub(r"\x00(\d+)\x00", lambda m: spans[int(m.group(1))], masked)


def _list_item_html(items):
    return "".join("<li>%s</li>" % _inline(item) for item in items)


def markdown_to_html_body(md_text):
    """The Markdown body converted to an HTML fragment."""
    lines = strip_frontmatter(md_text).replace("\r\n", "\n").split("\n")
    out = []
    index = 0
    total = len(lines)
    while index < total:
        line = lines[index]

        # Fenced code block.
        if _FENCE.match(line):
            fence = line.strip()[:3]
            body = []
            index += 1
            while index < total and not lines[index].strip().startswith(fence):
                body.append(lines[index])
                index += 1
            index += 1  # consume the closing fence (or run off the end)
            out.append("<pre><code>%s</code></pre>"
                       % html_module.escape("\n".join(body)))
            continue

        if not line.strip():
            index += 1
            continue

        heading = _ATX.match(line)
        if heading:
            level = len(heading.group(1))
            out.append("<h%d>%s</h%d>" % (level, _inline(heading.group(2)), level))
            index += 1
            continue

        if _HR.match(line):
            out.append("<hr>")
            index += 1
            continue

        # Table: a header row followed by a separator row.
        if "|" in line and index + 1 < total and _TABLE_SEP.match(lines[index + 1]):
            header = _split_row(line)
            index += 2
            rows = []
            while index < total and "|" in lines[index] and lines[index].strip():
                rows.append(_split_row(lines[index]))
                index += 1
            out.append(_table_html(header, rows))
            continue

        # Blockquote: consecutive `>` lines.
        if _BLOCKQUOTE.match(line):
            quote = []
            while index < total and _BLOCKQUOTE.match(lines[index]):
                quote.append(_BLOCKQUOTE.match(lines[index]).group(1))
                index += 1
            out.append("<blockquote>%s</blockquote>"
                       % _inline(" ".join(part for part in quote if part).strip()
                                 or " "))
            continue

        # Lists: consecutive bullet or numbered lines. Nesting by indent, in
        # steps of two spaces, one level deep - enough for these documents.
        if _UL.match(line) or _OL.match(line):
            index, block = _consume_list(lines, index, total)
            out.append(block)
            continue

        # Paragraph: gather until a blank line or a block starter.
        para = []
        while index < total and lines[index].strip() and not _is_block_start(lines, index):
            para.append(lines[index].strip())
            index += 1
        out.append("<p>%s</p>" % _inline(" ".join(para)))
    return "\n".join(out)


def _is_block_start(lines, index):
    line = lines[index]
    if _FENCE.match(line) or _ATX.match(line) or _HR.match(line) \
            or _UL.match(line) or _OL.match(line) or _BLOCKQUOTE.match(line):
        return True
    return "|" in line and index + 1 < len(lines) and _TABLE_SEP.match(lines[index + 1])


def _consume_list(lines, index, total):
    """One list block, supporting a single level of indented nesting."""
    def indent_of(match):
        return len(match.group(1).replace("\t", "  "))

    first = _UL.match(lines[index]) or _OL.match(lines[index])
    base_indent = indent_of(first)
    ordered = bool(_OL.match(lines[index]))
    items = []          # each item: (text, nested_html or "")
    while index < total:
        match = _UL.match(lines[index]) or _OL.match(lines[index])
        if not match:
            break
        if indent_of(match) < base_indent:
            break
        if indent_of(match) > base_indent:
            # Nested list under the previous item.
            index, nested = _consume_list(lines, index, total)
            if items:
                items[-1] = (items[-1][0], items[-1][1] + nested)
            continue
        items.append((match.group(2), ""))
        index += 1
    tag = "ol" if ordered else "ul"
    body = "".join("<li>%s%s</li>" % (_inline(text), nested)
                   for text, nested in items)
    return index, "<%s>%s</%s>" % (tag, body, tag)


def _split_row(line):
    cells = line.strip().strip("|").split("|")
    return [cell.strip() for cell in cells]


def _table_html(header, rows):
    head = "".join("<th>%s</th>" % _inline(cell) for cell in header)
    body = []
    for row in rows:
        # Pad or trim to the header width so a ragged row still renders.
        cells = (row + [""] * len(header))[:len(header)]
        body.append("<tr>%s</tr>"
                    % "".join("<td>%s</td>" % _inline(cell) for cell in cells))
    return "<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>" \
        % (head, "".join(body))


def markdown_to_html(md_text, title="", source_url=""):
    """A complete, self-contained HTML document for one archived Markdown file."""
    body = markdown_to_html_body(md_text)
    note = ""
    if source_url:
        note = ('<p class="src-note">Archived from '
                '<a href="%s">%s</a>. Rendered offline from the local Markdown copy.</p>'
                % (html_module.escape(source_url, quote=True),
                   html_module.escape(source_url)))
    return ("<!doctype html><html><head><meta charset=\"utf-8\">"
            "<title>%s</title><style>%s</style></head><body>%s%s</body></html>"
            % (html_module.escape(title or "Reference"), STYLE, body, note))


def is_pdf_bytes(data):
    """True when these bytes are a PDF, so the original is copied not re-rendered."""
    return bool(data) and data[:5] == b"%PDF-"
