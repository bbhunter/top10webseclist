#!/usr/bin/env python3
"""Run website regressions without giving archived content a host browser.

Mount only public archive inputs, staged website/test code and the three
already-approved test dependency packages. No network, checkout, credentials,
Docker socket or writable host output mount enters the test container.
"""
import argparse
from pathlib import Path
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools/references"))
from refslib import toolbox

IMAGE = "webseclist-browser-tests:source-workers-3"
ADAPTER = '''import * as real from "/deps/node_modules/playwright/index.mjs";
export const chromium = {launch: options => real.chromium.launch({...options,
 executablePath:"/usr/bin/chromium-browser", args:[...(options?.args || []),
 "--disable-dev-shm-usage"]})};
'''
BOOTSTRAP = '''import os,subprocess,time,urllib.request
environment=dict(os.environ,PLAYWRIGHT_MODULE="/deps/adapter.mjs",
 AXE_SOURCE="/deps/node_modules/axe-core/axe.min.js",WEBSEC_TEST_URL="http://127.0.0.1:4173/")
preview=subprocess.Popen(["node","website/preview.mjs"],env=environment)
try:
 for attempt in range(100):
  try:
   urllib.request.urlopen("http://127.0.0.1:4173/",timeout=1).close();break
  except OSError: time.sleep(.1)
 else: raise RuntimeError("test preview did not start")
 result=subprocess.call(["node","website/regression-test.mjs"],env=environment)
finally:
 preview.terminate();preview.wait(timeout=10)
raise SystemExit(result)
'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--node-modules", type=Path, required=True,
                        help="controller-selected directory containing approved playwright, playwright-core and axe-core")
    args = parser.parse_args()
    for name in ("playwright", "playwright-core", "axe-core"):
        if not (args.node_modules / name / "package.json").is_file():
            parser.error("missing approved test dependency: " + name)
    toolbox.ensure_image()
    present = subprocess.run(["docker", "image", "inspect", IMAGE], capture_output=True)
    if present.returncode:
        print("Building the isolated browser-test image", flush=True)
        subprocess.run(["docker", "build", "-t", IMAGE, "-"],
                       input=(ROOT / "website/Dockerfile.tests").read_bytes(), check=True, timeout=600)
    with tempfile.TemporaryDirectory(prefix="websec_browser_tests_") as folder:
        scratch = Path(folder)
        os.chmod(scratch, 0o755)
        stage = scratch / "work"
        stage.mkdir()
        for name in ("archived-references", "original-listings"):
            (stage / name).mkdir()
        shutil.copytree(ROOT / "website", stage / "website",
                        ignore=shutil.ignore_patterns("node_modules", ".tmp", ".env*", "__pycache__"))
        for path in ROOT.glob("*.md"):
            if re.fullmatch(r"\d{4}(?:-\d{2}|-ai)?\.md", path.name) or path.name in ("README.md", "CONTRIBUTING.md"):
                shutil.copyfile(path, stage / path.name)
        shutil.copytree(ROOT / ".github/ISSUE_TEMPLATE", stage / ".github/ISSUE_TEMPLATE")
        shutil.copyfile(ROOT / ".github/PULL_REQUEST_TEMPLATE.md", stage / ".github/PULL_REQUEST_TEMPLATE.md")
        adapter = scratch / "adapter.mjs"
        adapter.write_text(ADAPTER)
        command = ["docker", "run"] + toolbox.run_args()
        command[command.index("--network") + 1] = "none"
        command[command.index("--memory") + 1] = "2g"
        command[command.index("--pids-limit") + 1] = "1024"
        command[command.index("--tmpfs") + 1] = "/tmp:rw,noexec,nosuid,size=512m"
        command += ["-v", str(stage) + ":/work:ro", "-v", str(adapter) + ":/deps/adapter.mjs:ro"]
        for name in ("archived-references", "original-listings"):
            command += ["-v", str(ROOT / name) + ":/work/" + name + ":ro"]
        for name in ("playwright", "playwright-core", "axe-core"):
            command += ["-v", str((args.node_modules / name).resolve()) + ":/deps/node_modules/" + name + ":ro"]
        command += ["--workdir", "/work", IMAGE, "python", "-I", "-c", BOOTSTRAP]
        result = toolbox._run_container(command, timeout=900)
        sys.stdout.write(result.stdout.decode("utf-8", "replace"))
        sys.stderr.write(result.stderr.decode("utf-8", "replace"))
        return result.returncode


if __name__ == "__main__":
    sys.exit(main())
