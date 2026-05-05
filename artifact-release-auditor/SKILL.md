---
name: artifact-release-auditor
description: Audit research code and supplementary artifacts before paper submission, rebuttal, artifact evaluation, or public release. Use when the user asks whether a paper artifact, GitHub repo, zip, scripts, checkpoints, configs, README, environment, license, or benchmark package is reproducible, clean, reviewer-ready, anonymous, or suitable for NeurIPS/ICML/ICLR artifact review.
---

# Artifact Release Auditor

## Purpose

Use this skill to review a research artifact the way a careful artifact evaluator or skeptical reviewer would. Focus on whether the package lets another person understand what is included, run the intended checks, and trust the boundary between reproduced results and demonstration code.

## Workflow

### 1. Identify Release Mode

Classify the target:

- anonymous submission supplement
- rebuttal-only evidence bundle
- artifact evaluation package
- public GitHub release
- camera-ready archival repository

Different modes have different risks. Anonymous supplements prioritize identity hygiene and reproducibility claims; public releases also need license, citation, and long-term usability.

### 2. Inventory Contents

Check for:

- README, quickstart, environment files, dependency lock files
- scripts for training, evaluation, plotting, and table generation
- configs matching paper tables
- checkpoints, datasets, download instructions, and hashes
- logs or result files that support claimed numbers
- license, citation, model/data usage notes
- hidden files, cache files, local paths, secrets, credentials, or user names

### 3. Run Lightweight Verification

When feasible:

- run the documented install or quick-check command
- run help flags for scripts
- inspect import failures and missing paths
- verify expected outputs are created
- compare generated sample output with README claims

Do not turn a passing smoke test into a claim that the whole paper is reproduced.

### 4. Paper-Artifact Alignment

Compare artifact claims with the paper:

- algorithm object in code versus method section
- config defaults versus hyperparameter table
- metrics and aggregation versus result tables
- dataset split names versus paper protocol
- baseline implementation and budget matching
- figure/table generation scripts versus published figures

Mark exact missing links: "Table 3 cannot be traced to any script" is better than "reproducibility is weak."

### 5. Release Hygiene

Flag:

- secrets, API keys, absolute local paths, personal names in anonymous mode
- `__pycache__`, `.pyc`, large accidental binaries, stale PDFs, old titles
- vague claims such as "fully reproduces all results" when only a demo is included
- missing licenses or incompatible data/model redistribution
- overly broad installation instructions that have not been tested

## Output Format

Use:

1. artifact verdict
2. inspected contents
3. runnable boundary
4. paper-alignment findings
5. anonymity/security/license findings
6. P0/P1/P2 fix list
7. suggested README/release wording

Severity:

- `P0`: wrong artifact, secret leak, identity leak for anonymous submission, central claim cannot be traced, impossible install path.
- `P1`: serious reproducibility ambiguity, missing config/checkpoint/script for major table, misleading checklist or README claim.
- `P2`: cleanup, wording, packaging, citation, minor docs.

## Reference Files

Read `references/release-checklist.md` for a checklist and README wording templates.
