"""The controlled tag vocabulary, kept as JSON so it can be unified.

WHY A FILE AND NOT A COUNT. The vocabulary used to be derived: whatever tags
were in use, counted. That is self-consistent and impossible to correct. A word
could not be renamed, two spellings of one idea could not be merged, and a
newly agreed tag could not exist until something already carried it - so the
first document to need it was refused. `tag-vocabulary.json` is the durable
answer: aliases and OWASP mappings are stated once and survive every rebuild,
while the counts are recomputed from the manifest.

THREE PARTS, AND ONLY ONE IS GENERATED.

    tags     - every canonical tag, with the number of documents carrying it.
               Counted from the manifest on each rebuild.
    aliases  - a spelling that must never be published, and the canonical tag
               it becomes. Curated. Survives rebuilds.
    owasp    - the OWASP Top 10 categories, and which tags belong to each.
               Curated. Survives rebuilds.

A tag is NOT refused for being new. Archiving adds it, because refusing it lost
the reviewer's reading of the document - the one moment someone had actually
read the thing. What stops drift is normalisation and aliases: `XSS`, `xss` and
`  XSS ` are one tag before anything is stored, so the vocabulary grows by real
ideas rather than by spellings.
"""
import json
import re

# The OWASP Top 10:2021. Categories are a FACET, not tags a reviewer types: a
# document earns its categories from the techniques it was already tagged with,
# so nobody has to remember the mapping and nothing has to be tagged twice.
#
# The mapping is a judgement and it is meant to be edited. It lives in the JSON
# after the first write, and this seed is only used to create that file.
OWASP_2021 = [
    ("A01:2021", "Broken Access Control", [
        "auth-bypass", "idor", "privilege-escalation", "csrf", "cors",
        "mass-assignment", "path-traversal", "lfi", "sop-bypass",
        "same-origin-policy", "directory-listing"]),
    ("A02:2021", "Cryptographic Failures", [
        "tls", "https", "hash-collision", "predictable-token", "crypto",
        "charset"]),
    ("A03:2021", "Injection", [
        "injection", "sqli", "nosqli", "xss", "mutation-xss", "blind-xss",
        "csti", "ssti", "command-injection", "header-injection",
        "response-splitting", "xxe", "css-injection", "prompt-injection",
        "argument-injection", "lfi"]),
    ("A04:2021", "Insecure Design", [
        "race-condition", "toctou", "abuse-of-functionality",
        "algorithmic-complexity", "clickjacking", "ui-redress", "phishing",
        "user-enumeration", "captcha-bypass", "open-redirect"]),
    ("A05:2021", "Security Misconfiguration", [
        "csp", "mime", "content-type", "waf", "waf-bypass", "docker",
        "kubernetes", "filter-bypass", "sanitizer-bypass"]),
    ("A06:2021", "Vulnerable and Outdated Components", [
        "dependency-confusion", "typosquatting", "supply-chain"]),
    ("A07:2021", "Identification and Authentication Failures", [
        "sso", "oauth", "openid", "saml", "passkeys", "webauthn",
        "session-fixation", "cookie", "jwt", "identity"]),
    ("A08:2021", "Software and Data Integrity Failures", [
        "deserialization", "gadget-chain", "prototype-pollution",
        "class-pollution", "dom-clobbering", "ci-cd", "github-actions"]),
    ("A09:2021", "Security Logging and Monitoring Failures", [
        "detection"]),
    ("A10:2021", "Server-Side Request Forgery", [
        "ssrf", "dns-rebinding"]),
]

# Spellings that must never reach a published file, and what they become.
# Case is handled by `normalise` and needs no entry here; this is for genuine
# synonyms, where two different words name one idea.
SEED_ALIASES = {
    "wasm": "webassembly",
}

_ALLOWED = re.compile(r"[^a-z0-9?-]+")
_RUNS = re.compile(r"-{2,}")


def normalise(tag):
    """The canonical spelling of one tag, before any alias is applied.

    Lower-cases, turns separators into hyphens and drops everything else. This
    is what makes `XSS` and `xss` one tag rather than two, which they were: the
    archive carried both, and the capitalised one had exactly one document.

    A leading `?` is preserved, because it marks a proposal and is read before
    the tag is stored.
    """
    text = str(tag or "").strip().lower()
    proposed = text.startswith("?")
    if proposed:
        text = text[1:]
    text = _ALLOWED.sub("-", text.replace("_", "-").replace(" ", "-"))
    text = _RUNS.sub("-", text).strip("-")
    return ("?" + text) if (proposed and text) else text


def default_vocabulary():
    """The vocabulary file as it looks before anything has been counted."""
    return {
        "schema": 1,
        "aliases": dict(SEED_ALIASES),
        "owasp": {
            "edition": "2021",
            "categories": [
                {"id": ident, "title": title, "tags": sorted(members)}
                for ident, title, members in OWASP_2021
            ],
        },
        "tags": {},
    }


def load(path):
    """Read the vocabulary, falling back to the seed when there is no file."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default_vocabulary()
    if not isinstance(data, dict):
        return default_vocabulary()
    seed = default_vocabulary()
    for key in ("aliases", "owasp", "tags"):
        data.setdefault(key, seed[key])
    data.setdefault("schema", 1)
    return data


def save(path, data):
    """Write the vocabulary in the manifest's format, so diffs read the same."""
    path.write_text(
        json.dumps(data, indent=1, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8", newline="\n")
    return path


_CACHE = {}


def current(root=None, config=None):
    """The vocabulary on disk, read once per process.

    `render` needs the OWASP mapping for every document it writes, and a
    thousand-document run must not read the file a thousand times. Falls back
    to the seed when there is no file, so rendering never depends on one.
    """
    from refslib import paths as paths_module
    root = root or paths_module.repo_root()
    if config is None:
        config = paths_module.config()
    path = (root / ((config or {}).get("archive_dir") or "archived-references")
            / "tag-vocabulary.json")
    key = str(path)
    if key not in _CACHE:
        _CACHE[key] = load(path)
    return _CACHE[key]


def resolve(tag, vocabulary):
    """One tag, normalised and folded through the alias table.

    Aliases are followed to a fixed point so a chain (`a`->`b`->`c`) cannot
    publish `b`, with a hard stop rather than a loop: a table that points at
    itself is a maintainer's typo, not a reason to hang the run.
    """
    aliases = (vocabulary or {}).get("aliases") or {}
    seen = set()
    current = normalise(tag)
    while current in aliases and current not in seen:
        seen.add(current)
        current = normalise(aliases[current])
    return current


def owasp_categories(tags, vocabulary):
    """The OWASP Top 10 categories a document earns from its tags."""
    members = {}
    for category in ((vocabulary or {}).get("owasp") or {}).get("categories") or []:
        for tag in category.get("tags") or []:
            members.setdefault(normalise(tag), []).append(category.get("id"))
    found = []
    for tag in tags:
        for ident in members.get(normalise(tag), []):
            if ident and ident not in found:
                found.append(ident)
    return sorted(found)


def owasp_tag(identifier):
    """`A03:2021` as the tag a reader can search on: `owasp-a03-2021`.

    Prefixed, so the category cannot be mistaken for a technique tag and so
    every category sorts together in a tag list.
    """
    return "owasp-" + normalise(str(identifier).replace(":", "-"))


def register(vocabulary, tags):
    """Add tags that are not in the vocabulary yet, and report which were new.

    This is the auto-add the archive runs on: a reviewer who has read the
    document and needs a word the vocabulary lacks gets to use it. The word is
    already normalised and alias-folded by `resolve`, so what enters is an
    idea rather than a spelling.
    """
    known = vocabulary.setdefault("tags", {})
    added = []
    for tag in tags:
        if tag and tag not in known:
            known[tag] = {"documents": 0}
            added.append(tag)
    return added


def recount(vocabulary, counts):
    """Refresh document counts, keeping every curated field and every tag.

    A tag that has fallen to zero documents is KEPT, with `documents: 0`. It was
    agreed once, and dropping it silently would let the same word be re-argued
    later - and would delete the maintainer's OWASP mapping with it.
    """
    known = vocabulary.setdefault("tags", {})
    for tag, count in counts.items():
        known.setdefault(tag, {})["documents"] = count
    for tag, record in known.items():
        if tag not in counts:
            record["documents"] = 0
    return vocabulary
