#!/usr/bin/env python3
"""Validate the basic structure of the skill collection."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_TOP_KEYS = {"name", "description"}
REQUIRED_REPO_FILES = [
    "README.md",
    "SKILLS.md",
    "LICENSE",
    "PUBLISH.md",
    "adapters/README.md",
    "adapters/universal-agent-instructions.md",
    "prompts/full-review.md",
    "prompts/data-audit.md",
    "prompts/rebuttal.md",
    "prompts/artifact-audit.md",
    "prompts/camera-ready.md",
    "evals/README.md",
    "evals/rubric.md",
]


def parse_frontmatter(text: str) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, ["missing opening frontmatter delimiter"]
    end = text.find("\n---", 4)
    if end == -1:
        return {}, ["missing closing frontmatter delimiter"]
    raw = text[4:end].strip().splitlines()
    data: dict[str, str] = {}
    for line in raw:
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data, errors


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    skill_md = path / "SKILL.md"
    agent_yaml = path / "agents" / "openai.yaml"

    if not skill_md.exists():
        return [f"{path.name}: missing SKILL.md"]

    text = skill_md.read_text(encoding="utf-8")
    meta, meta_errors = parse_frontmatter(text)
    errors.extend(f"{path.name}: {err}" for err in meta_errors)

    missing = REQUIRED_TOP_KEYS - set(meta)
    for key in sorted(missing):
        errors.append(f"{path.name}: missing frontmatter key {key}")

    if meta.get("name") != path.name:
        errors.append(f"{path.name}: frontmatter name does not match directory")

    if len(meta.get("description", "")) < 80:
        errors.append(f"{path.name}: description is too short for reliable invocation")

    if not agent_yaml.exists():
        errors.append(f"{path.name}: missing agents/openai.yaml")
    else:
        yaml_text = agent_yaml.read_text(encoding="utf-8")
        if f"Use ${path.name}" not in yaml_text:
            errors.append(f"{path.name}: default_prompt should mention ${path.name}")
        if not re.search(r"display_name:\s*\".+\"", yaml_text):
            errors.append(f"{path.name}: missing display_name")
        if not re.search(r"short_description:\s*\".{25,64}\"", yaml_text):
            errors.append(f"{path.name}: short_description should be 25-64 chars")

    return errors


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED_REPO_FILES:
        if not (ROOT / rel).exists():
            errors.append(f"repo: missing {rel}")

    skill_dirs = [
        path for path in ROOT.iterdir()
        if path.is_dir()
        and (path / "SKILL.md").exists()
        and not path.name.startswith(".")
    ]
    if not skill_dirs:
        print("No skill directories found.", file=sys.stderr)
        return 1

    for path in sorted(skill_dirs):
        errors.extend(validate_skill(path))

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    print(f"Validated {len(skill_dirs)} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
