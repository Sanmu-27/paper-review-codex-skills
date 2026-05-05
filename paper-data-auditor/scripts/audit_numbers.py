#!/usr/bin/env python3
"""
Static number and claim scanner for empirical papers.

This script extracts high-yield numeric/configuration clues from paper sources
and artifacts. It is intentionally conservative: findings are leads for expert
review, not proof of error.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from collections import defaultdict
from pathlib import Path


TEXT_EXTS = {".tex", ".bib", ".md", ".txt", ".yaml", ".yml", ".py", ".json", ".csv", ".tsv"}
SKIP_DIRS = {".git", "__pycache__", ".mypy_cache", ".pytest_cache", "node_modules"}

NUMBER_RE = re.compile(
    r"(?<![A-Za-z0-9_])[-+]?(?:\d+\.\d+|\d+)(?:\s*(?:%|x|GB|MB|TB|ms|s|us|GPU-hours|A100|seeds?|epochs?|trajectories?))?",
    re.IGNORECASE,
)

DANGER_PATTERNS = {
    "stale venue/title": re.compile(r"\b(ICML|Information-Theoretic|DynSplit|old title)\b", re.I),
    "over-strong reproduction": re.compile(r"\b(reproduces? Table|fully reproducible|faithfully reproduce)\b", re.I),
    "artifact boundary": re.compile(r"\b(prototype|driver interface|KV-cache hooks|not bundled|reference implementation)\b", re.I),
    "training label drift": re.compile(r"\b(gradient saliency|gradient-norm|signed first-order|signed_utility|label_type)\b", re.I),
    "budget ambiguity": re.compile(r"\b(token budget|step budget|budget_ratio|retained tokens|heap size|len\\(heap\\))\b", re.I),
    "config hyperparam": re.compile(r"\b(lambda_noise|lambda_2|batch_size|Batch Size|num_epochs|Epochs|learning_rate)\b", re.I),
}


def iter_files(root: Path):
    if root.is_file():
        yield root
        return
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file() and path.suffix.lower() in TEXT_EXTS | {".zip"}:
            yield path


def read_text(path: Path) -> str:
    for enc in ("utf-8", "utf-8-sig", "gb18030", "latin-1"):
        try:
            return path.read_text(encoding=enc)
        except UnicodeDecodeError:
            continue
    return ""


def line_context(text: str, pattern: re.Pattern):
    rows = []
    for idx, line in enumerate(text.splitlines(), start=1):
        if pattern.search(line):
            rows.append((idx, line.strip()))
    return rows


def scan_zip(path: Path):
    findings = []
    try:
        with zipfile.ZipFile(path) as zf:
            for info in zf.infolist():
                name = info.filename
                if "__pycache__" in name or name.endswith(".pyc"):
                    findings.append({"type": "zip-cache-file", "path": str(path), "entry": name})
                if re.search(r"(old|icml|example_paper\.pdf)", name, re.I):
                    findings.append({"type": "zip-stale-name", "path": str(path), "entry": name})
    except zipfile.BadZipFile:
        findings.append({"type": "bad-zip", "path": str(path)})
    return findings


def main():
    parser = argparse.ArgumentParser(description="Audit paper numbers and artifact consistency clues.")
    parser.add_argument("path", help="Paper source file, repo folder, or artifact folder")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    if not root.exists():
        print(f"Path not found: {root}", file=sys.stderr)
        return 2

    numbers = defaultdict(list)
    pattern_hits = []
    zip_findings = []
    files_scanned = 0

    for path in iter_files(root):
        files_scanned += 1
        if path.suffix.lower() == ".zip":
            zip_findings.extend(scan_zip(path))
            continue
        text = read_text(path)
        rel = str(path)
        for line_no, line in enumerate(text.splitlines(), start=1):
            for match in NUMBER_RE.finditer(line):
                token = " ".join(match.group(0).split())
                numbers[token].append({"path": rel, "line": line_no, "text": line.strip()[:240]})
        for label, pattern in DANGER_PATTERNS.items():
            for line_no, line in line_context(text, pattern):
                pattern_hits.append({"type": label, "path": rel, "line": line_no, "text": line[:240]})

    repeated = {
        k: v for k, v in numbers.items()
        if len(v) >= 3 and re.search(r"\d", k)
    }

    output = {
        "root": str(root),
        "files_scanned": files_scanned,
        "unique_numbers": len(numbers),
        "repeated_numbers": repeated,
        "pattern_hits": pattern_hits,
        "zip_findings": zip_findings,
    }

    if args.json:
        print(json.dumps(output, indent=2, ensure_ascii=False))
        return 0

    print(f"Paper data audit: {root}")
    print(f"Files scanned: {files_scanned}")
    print(f"Unique numeric tokens: {len(numbers)}")
    print()

    if zip_findings:
        print("Zip/package findings:")
        for item in zip_findings:
            print(f"- {item['type']}: {item['path']} :: {item.get('entry', '')}")
        print()

    if pattern_hits:
        print("Pattern hits:")
        for item in pattern_hits[:200]:
            print(f"- [{item['type']}] {item['path']}:{item['line']} :: {item['text']}")
        if len(pattern_hits) > 200:
            print(f"... {len(pattern_hits) - 200} more pattern hits omitted")
        print()

    print("Repeated numeric tokens (top leads):")
    for token, hits in sorted(repeated.items(), key=lambda kv: (-len(kv[1]), kv[0]))[:80]:
        print(f"- {token} ({len(hits)} hits)")
        for hit in hits[:3]:
            print(f"  {hit['path']}:{hit['line']} :: {hit['text']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
