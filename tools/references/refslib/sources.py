"""Which tracked reading-list documents feed the reference archive.

Finalized lists are named explicitly in config. Preliminary ``YYYY-ai.md``
lists are discovered by filename and must bound their publishable citations
with exact markers, so scoring notes and watchlists never become archive input.
"""

import os
import re

from .paths import SetupError


DEFAULT_PATTERN = r"^\d{4}-ai\.md$"
DEFAULT_START = "<!-- archived-references:start -->"
DEFAULT_END = "<!-- archived-references:end -->"


def _settings(config):
    section = (config or {}).get("preliminary_documents") or {}
    return (
        section.get("pattern") or DEFAULT_PATTERN,
        section.get("start_marker") or DEFAULT_START,
        section.get("end_marker") or DEFAULT_END,
    )


def is_preliminary(relative, config=None):
    pattern, _start, _end = _settings(config)
    base = os.path.basename(str(relative or "").replace("\\", "/"))
    return bool(re.match(pattern, base))


def source_files(config, tracked=()):
    """Configured finalized documents plus tracked preliminary documents."""
    found = []
    for relative in config.get("curated_documents") or []:
        if relative not in found:
            found.append(relative)
    for relative in tracked or []:
        if is_preliminary(relative, config) and relative not in found:
            found.append(relative)
    return found


def bounded_lines(relative, text, config=None):
    """Yield real ``(line_number, line)`` pairs allowed into the archive."""
    lines = text.splitlines()
    if not is_preliminary(relative, config):
        return list(enumerate(lines, start=1))

    _pattern, start, end = _settings(config)
    starts = [index for index, line in enumerate(lines) if line.strip() == start]
    ends = [index for index, line in enumerate(lines) if line.strip() == end]
    if len(starts) != 1 or len(ends) != 1 or starts[0] >= ends[0]:
        raise SetupError(
            "%s must contain exactly one ordered %r / %r marker pair; "
            "preliminary files are harvested only inside that boundary."
            % (relative, start, end)
        )
    return [(index + 1, lines[index]) for index in range(starts[0] + 1, ends[0])]
