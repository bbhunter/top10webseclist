#!/usr/bin/env python3
"""Render archived Mermaid fences to inert SVGs in the isolated PDF toolbox.

Pass --bundle with Mermaid 11.16.0's dist/mermaid.min.js. The pinned bundle is
checked before execution; the container has no network or repository mount.
Only exact source matches are advertised to the static site's Markdown reader.
"""
import argparse
import hashlib
import html
import json
import re
import shutil
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

from refslib import toolbox

BUNDLE_SHA = "74d7c46dabca328c2294733910a8aa1ed0c37451776e8d5295da38a2b758fb9b"
ROOT = Path(__file__).resolve().parents[2]
FENCE = re.compile(r"^```mermaid\s*\n(.*?)^```\s*$", re.M | re.S)


def checked_svg(value):
    # Chromium expands local marker URLs to its temporary document URL.
    # Restore fragment-only references before validating the standalone SVG.
    value = value.replace("file:///out/index.html#", "#")
    root = ET.fromstring(value)
    if root.tag != "{http://www.w3.org/2000/svg}svg":
        raise ValueError("renderer did not produce SVG")
    styles = []
    for node in root.iter():
        if node.tag.split("}")[-1].lower() == "style":
            styles.append(node.text or "")
        if node.tag.split("}")[-1].lower() in {"script", "foreignobject", "iframe", "image", "use"}:
            raise ValueError("active or externally referenced SVG element")
        for key, val in node.attrib.items():
            styles.append(val)
            name = key.split("}")[-1].lower()
            if name.startswith("on") or (name in {"href", "src"} and not val.startswith("#")):
                raise ValueError("active or external SVG attribute")
    style_text = "\n".join(styles)
    if re.search(r"@import", style_text, re.I) or any(
        not target.strip().strip("\"'").startswith("#")
        for target in re.findall(r"url\((.*?)\)", style_text, re.I)
    ):
        raise ValueError("external SVG stylesheet reference")
    return value


def render(sources, bundle):
    with tempfile.TemporaryDirectory(prefix="websec_diagrams_") as folder:
        scratch = Path(folder)
        shutil.copyfile(bundle, scratch / "mermaid.js")
        data = json.dumps(sources).replace("<", "\\u003c")
        page = '''<!doctype html><meta charset="utf-8"><script src="mermaid.js"></script>
<textarea id="result"></textarea><script>
mermaid.initialize({startOnLoad:false,securityLevel:'strict',htmlLabels:false,
 deterministicIds:true, maxTextSize:50000,maxEdges:500,
 flowchart:{htmlLabels:false},theme:'default'});
(async()=>{const output=[];for(const [id,source] of SOURCES){
 try {const result=await mermaid.render('diagram'+id,source);output.push([id,result.svg]);}
 catch(error){output.push([id,null,String(error)]);}}
 document.getElementById('result').textContent=JSON.stringify(output);})();</script>'''.replace("SOURCES", data)
        (scratch / "index.html").write_text(page)
        args = toolbox.run_args()
        args[args.index("--network") + 1] = "none"
        command = ["docker", "run"] + args + ["-v", toolbox._mount(folder) + ":/out:ro", toolbox.IMAGE, "chromium-browser"]
        command += list(toolbox.CHROMIUM_ARGS) + ["--user-data-dir=/tmp/chromium", "--virtual-time-budget=20000", "file:///out/index.html"]
        done = toolbox._run_container(command, timeout=90)
        match = re.search(r'<textarea id="result">(.*?)</textarea>', done.stdout.decode("utf-8", "replace"), re.S)
        if done.returncode or not match or not match[1]:
            raise RuntimeError("diagram container failed: " + done.stderr.decode("utf-8", "replace")[-500:])
        return json.loads(html.unescape(match[1]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, required=True)
    args = parser.parse_args()
    if hashlib.sha256(args.bundle.read_bytes()).hexdigest() != BUNDLE_SHA:
        raise ValueError("unexpected Mermaid bundle bytes")
    archive = ROOT / "archived-references"
    manifest = json.loads((archive / "manifest.json").read_text())
    sources = {}
    for entry in manifest["urls"].values():
        filename = entry.get("steps", {}).get("render", {}).get("file")
        if not filename or not (ROOT / filename).is_file():
            continue
        for match in FENCE.finditer((ROOT / filename).read_text()):
            source = match[1].strip()
            sources[hashlib.sha256(source.encode()).hexdigest()] = source
    output = archive / "diagrams"
    output.mkdir(exist_ok=True)
    pending = [(digest, source) for digest, source in sorted(sources.items()) if not (output / (digest + ".svg")).is_file()]
    toolbox.ensure_image()
    errors = []
    for start in range(0, len(pending), 12):
        for row in render(pending[start:start + 12], args.bundle):
            digest, svg = row[:2]
            if svg is None:
                errors.append({"sha256": digest, "source": sources[digest], "error": row[2]})
                continue
            (output / (digest + ".svg")).write_text(checked_svg(svg) + "\n")
        print("rendered batch", start // 12 + 1, flush=True)
    if errors:
        print(json.dumps(errors, indent=2))
        raise SystemExit("invalid Mermaid diagrams; fix source fences and rerun")
    records = []
    for digest, source in sorted(sources.items()):
        path = output / (digest + ".svg")
        checked_svg(path.read_text())
        records.append({"source": source, "path": path.relative_to(ROOT).as_posix(), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    index = {"schema": 1, "renderer": "Mermaid 11.16.0", "bundle_sha256": BUNDLE_SHA, "diagrams": records}
    (archive / "diagram-assets.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n")
    print("Published", len(records), "inert SVG diagrams")


if __name__ == "__main__":
    main()
