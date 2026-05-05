#!/usr/bin/env python3
"""Static audit helper for ML paper LaTeX submissions.

This script intentionally checks reviewer-trust issues rather than LaTeX style.
It is conservative: every finding should be inspected by a human/agent before
being presented as a paper flaw.
"""

from __future__ import annotations

import argparse
import json
import re
import zipfile
from pathlib import Path
from typing import Any


SUSPICIOUS_BIB_TITLE_PATTERNS = [
    r"\bH2o\b",
    r"\bSnapkv\b",
    r"\bChunkkv\b",
    r"\bFlashattention\b",
    r"\bSqueezeattention\b",
    r"\bLlm\b",
    r"\bllm\b",
    r"\bkv cache\b",
    r"\bkv-cache\b",
    r"\bpagedattention\b",
    r"\bleankv\b",
]

SUSPICIOUS_TEX_PATTERNS = {
    "unresolved_placeholder": [r"\bTODO\b", r"\[TODO\]", r"\?\?"],
    "raw_entropy_symbol": [r"(?<!bar\{)H\(f\)"],
    "old_step_budget_constraint": [r"\|\\hat\{M\}\|\s*\\leq\s*\\mathcal\{B\}"],
    "old_attn_symbol": [r"AttnNorm\("],
    "old_tscore_complexity": [r"O\(T\s*\\cdot\s*\\mathcal\{B\}\s*\+\s*T_\{score\}\)"],
    "wrong_kivi_cite": [r"KIVI\s*\\cite\{xia2025kitty\}"],
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def extract_labels(tex: str) -> set[str]:
    return set(re.findall(r"\\label\{([^}]+)\}", tex))


def extract_refs(tex: str) -> set[str]:
    refs: set[str] = set()
    for match in re.findall(r"\\(?:ref|cref|Cref|autoref)\{([^}]+)\}", tex):
        refs.update(part.strip() for part in match.split(",") if part.strip())
    return refs


def extract_cites(tex: str) -> set[str]:
    cites: set[str] = set()
    for match in re.findall(r"\\cite[a-zA-Z*]*\{([^}]+)\}", tex):
        cites.update(part.strip() for part in match.split(",") if part.strip())
    return cites


def extract_bib_keys(bib: str) -> set[str]:
    return set(re.findall(r"@\w+\{([^,\s]+),", bib))


def scan_tex_patterns(tex: str) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    lines = tex.splitlines()
    for kind, patterns in SUSPICIOUS_TEX_PATTERNS.items():
        for pattern in patterns:
            rx = re.compile(pattern)
            for i, line in enumerate(lines, start=1):
                if rx.search(line):
                    findings.append(
                        {
                            "severity": "high" if kind in {"unresolved_placeholder", "wrong_kivi_cite"} else "medium",
                            "kind": kind,
                            "line": i,
                            "snippet": line.strip()[:240],
                        }
                    )
    return findings


def scan_bib_patterns(bib: str) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    lines = bib.splitlines()
    for i, line in enumerate(lines, start=1):
        if "title" not in line:
            continue
        for pattern in SUSPICIOUS_BIB_TITLE_PATTERNS:
            if re.search(pattern, line):
                findings.append(
                    {
                        "severity": "low",
                        "kind": "suspicious_bib_title_casing",
                        "line": i,
                        "pattern": pattern,
                        "snippet": line.strip()[:240],
                    }
                )
    return findings


def find_bib_files(tex_path: Path, tex: str) -> list[Path]:
    names = []
    for match in re.findall(r"\\bibliography\{([^}]+)\}", tex):
        names.extend(part.strip() for part in match.split(",") if part.strip())
    paths = []
    for name in names:
        p = tex_path.parent / (name if name.endswith(".bib") else f"{name}.bib")
        if p.exists():
            paths.append(p)
    return paths


def compare_submission_ready(tex_path: Path, files: list[Path]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    root = tex_path.parent
    ready = root / "_submission_ready" / "paper_source"
    if not ready.exists():
        return findings
    for src in files:
        dst = ready / src.name
        if not dst.exists():
            findings.append(
                {
                    "severity": "medium",
                    "kind": "submission_ready_missing_file",
                    "file": str(dst),
                }
            )
            continue
        if read_text(src) != read_text(dst):
            findings.append(
                {
                    "severity": "high",
                    "kind": "submission_ready_source_drift",
                    "source": str(src),
                    "packaged": str(dst),
                }
            )
    return findings


def inspect_zip(root: Path, expected_files: list[str]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    zip_path = root / "_submission_ready" / "paper_source.zip"
    if not zip_path.exists():
        return findings
    with zipfile.ZipFile(zip_path) as zf:
        names = {Path(name).name for name in zf.namelist() if not name.endswith("/")}
    for name in expected_files:
        if name not in names:
            findings.append(
                {
                    "severity": "medium",
                    "kind": "source_zip_missing_file",
                    "file": name,
                    "zip": str(zip_path),
                }
            )
    return findings


def audit(tex_path: Path) -> dict[str, Any]:
    tex_path = tex_path.resolve()
    tex = read_text(tex_path)

    labels = extract_labels(tex)
    refs = extract_refs(tex)
    cites = extract_cites(tex)
    bib_paths = find_bib_files(tex_path, tex)
    bib_text = "\n".join(read_text(p) for p in bib_paths)
    bib_keys = extract_bib_keys(bib_text)

    checklist = tex_path.parent / "checklist.tex"
    files_to_compare = [tex_path]
    if checklist.exists():
        files_to_compare.append(checklist)
    files_to_compare.extend(bib_paths)

    findings: list[dict[str, Any]] = []
    for missing in sorted(refs - labels):
        findings.append({"severity": "high", "kind": "missing_label", "label": missing})
    for missing in sorted(cites - bib_keys):
        findings.append({"severity": "high", "kind": "missing_bib_key", "key": missing})

    findings.extend(scan_tex_patterns(tex))
    if checklist.exists():
        checklist_text = read_text(checklist)
        answer_count = len(re.findall(r"Answer:\s*\\answer(?:Yes|No|NA)\{\}", checklist_text))
        justification_count = checklist_text.count("Justification:")
        if answer_count == 0:
            findings.append({"severity": "high", "kind": "checklist_no_answers", "file": str(checklist)})
        if answer_count != justification_count:
            findings.append(
                {
                    "severity": "medium",
                    "kind": "checklist_answer_justification_count_mismatch",
                    "answers": answer_count,
                    "justifications": justification_count,
                }
            )
        if "TODO" in checklist_text or "[TODO]" in checklist_text:
            findings.append({"severity": "high", "kind": "checklist_placeholder", "file": str(checklist)})
    else:
        findings.append({"severity": "high", "kind": "missing_checklist", "expected": str(checklist)})

    findings.extend(scan_bib_patterns(bib_text))
    findings.extend(compare_submission_ready(tex_path, files_to_compare))
    findings.extend(inspect_zip(tex_path.parent, [p.name for p in files_to_compare]))

    severity_order = {"high": 0, "medium": 1, "low": 2}
    findings.sort(key=lambda x: (severity_order.get(x.get("severity", "low"), 9), x.get("kind", "")))

    return {
        "tex": str(tex_path),
        "bib_files": [str(p) for p in bib_paths],
        "checklist": str(checklist) if checklist.exists() else None,
        "counts": {
            "labels": len(labels),
            "refs": len(refs),
            "cites": len(cites),
            "bib_keys": len(bib_keys),
            "findings": len(findings),
        },
        "findings": findings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Static audit for ML paper LaTeX submissions.")
    parser.add_argument("tex", type=Path, help="Path to main .tex file")
    parser.add_argument("--json", action="store_true", help="Print full JSON")
    args = parser.parse_args()

    result = audit(args.tex)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Static audit: {result['tex']}")
        print(f"Findings: {result['counts']['findings']}")
        for finding in result["findings"]:
            sev = finding.get("severity", "low").upper()
            kind = finding.get("kind")
            detail = finding.get("snippet") or finding.get("label") or finding.get("key") or finding.get("file") or ""
            loc = f":{finding['line']}" if "line" in finding else ""
            print(f"- [{sev}] {kind}{loc} {detail}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
