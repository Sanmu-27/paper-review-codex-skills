---
name: paper-data-auditor
description: "Audit whether a research paper's reported numbers, tables, experimental claims, system measurements, and reproducibility evidence are reasonable by combining internal consistency checks, artifact/source checks, external literature calibration, and expert-domain plausibility review. Use for ML/AI papers, NeurIPS/ICML/ICLR submissions, empirical results, ablations, throughput/memory claims, benchmark tables, review reports, \u6570\u636e\u5408\u7406\u6027\u5ba1\u67e5, \u6570\u636e\u53ef\u4fe1\u5ea6\u6838\u67e5, \u5b9e\u9a8c\u6570\u5b57\u6838\u67e5, \u8868\u683c\u6570\u503c\u6838\u67e5, or \u8bba\u6587\u6570\u636e sanity check."
---

# Paper Data Auditor

## Purpose

Use this skill to judge whether a paper's data story is credible. The output should feel like a careful expert reviewer: concrete, sourced, skeptical without being theatrical, and explicit about what is verified, inferred, or still unverified.

## Required Mindset

- Treat every number as a claim with units, scope, and provenance.
- Separate internal consistency from external plausibility.
- Do not assume a result is false just because it is strong; ask what evidence would make it believable.
- If the user asks for current external calibration or recent related work, browse and cite primary sources. For ML/system claims, prefer papers, official benchmark docs, official model docs, and artifact repositories.
- Never overstate what the artifact proves. Distinguish runnable demos, driver interfaces, benchmark scripts, trained checkpoints, and production hooks.

## Workflow

### 1. Inventory The Evidence

Identify available artifacts:

- paper source: `.tex`, `.bib`, figures, appendix, checklist
- rendered PDF or submitted PDF
- supplementary code, configs, manifests, zips
- logs, result JSON/CSV, checkpoints, scripts
- external pages: OpenReview, arXiv, Papers with Code, benchmark docs

Run the local static scanner when source files are available:

```bash
python <skill_dir>/scripts/audit_numbers.py <paper_or_repo_path>
```

Use its output as leads, not final truth.

### 2. Extract Claim Ledger

Build a compact ledger of the paper's important data claims:

- headline metrics: accuracy, SR, BLEU/Rouge, PPL, latency, memory, cost
- budgets and constraints: token budget, context length, batch size, GPU type, precision
- training details: data size, seeds, epochs, batch size, optimizer, checkpoints
- ablations and deltas: "improves by X", "retains Y%", "reduces Z"
- scope qualifiers: transfer, diagnostic, prototype, oracle, full-cache, fallback

For each claim record:

- value and unit
- where it appears
- what it is compared against
- whether it is main evidence, diagnostic evidence, or illustrative evidence
- what artifact/config/script should support it

### 3. Internal Consistency Audit

Check these high-yield inconsistencies:

- Same number differs across abstract, main text, tables, captions, appendix, checklist, README, configs.
- Table deltas do not match table values.
- Percent retention and absolute values are mixed incorrectly.
- Budget is defined as tokens in text but steps/chunks/examples in code.
- Training/eval split claims conflict with configs or scripts.
- "Mean +/- std" lacks seeds or aggregation unit.
- Model/hardware memory arithmetic is physically impossible.
- Throughput/latency table conflicts with benchmark script scope.
- Transfer/diagnostic results are framed as in-domain main evidence.
- Figure captions use old terminology after method changes.
- PDF/source/zips have stale title, venue, author, checklist, or old figures.

For formulas and derived claims, recompute simple arithmetic by hand or with a scratch script.

### 4. Artifact And Reproducibility Audit

Inspect code and package boundaries:

- Does the implementation match the paper's algorithmic object?
- Are configs aligned with hyperparameter tables?
- Are evaluation scripts actually applying the method in the generation/inference loop?
- Are there missing checkpoints, missing environments, or external hooks?
- Is a script a runnable reproducer, a benchmark driver, or only an interface scaffold?
- Does the checklist honestly describe what can and cannot be reproduced?
- Are zips clean of `__pycache__`, `.pyc`, local paths, logs, or identifying metadata?

If the artifact cannot reproduce a table, say exactly which missing piece blocks it.

### 5. External Literature Calibration

Use external papers to ask whether reported numbers are plausible for the benchmark/model/task regime.

When browsing is needed:

- search for the benchmark's official paper/docs and the closest baselines
- prefer the original method papers for baseline capabilities
- compare against same model scale, same budget, same context length, same metric
- note when no apples-to-apples comparison exists

Use `references/external-calibration.md` for source selection rules and comparison templates.

Common calibration questions:

- Is the baseline value in the expected range?
- Is the claimed improvement unusually large for the setting?
- Does the hardware/memory/latency claim match known model sizes and KV-cache formulas?
- Are benchmark splits and task counts consistent with official benchmark docs?
- Are citations attached to the right methods and versions?

### 6. Expert Plausibility Review

After internal and external checks, reason as a domain expert:

- What mechanism would explain the result?
- Does the ablation isolate that mechanism?
- Is there a confound such as prompt protection, oracle budget, transfer leakage, task selection, or fallback behavior?
- Would a serious reviewer trust this evidence?
- What exact change would make the claim rebuttal-safe?

Use `references/expert-rubric.md` for scoring severity and confidence.

## Output Format

Use concise sections:

- **Verdict**: score/risk level and confidence.
- **Evidence Inspected**: files, scripts, PDFs, external sources.
- **Claim Ledger Summary**: the main claims and whether they are supported.
- **Findings**: ordered by severity, with file/line references when local files exist.
- **External Calibration**: what outside papers/docs suggest.
- **Reproducibility Boundary**: what can be run, what is only an interface, what is missing.
- **Fix List**: P0/P1/P2 actions.

Severity labels:

- `P0`: could invalidate central claim, cause rejection, or indicate wrong upload/version.
- `P1`: serious trust or reproducibility problem, but fixable without changing core idea.
- `P2`: clarity, hygiene, caption, packaging, or wording issue.

When local files are available, use clickable absolute file links in the final answer.

## What Not To Do

- Do not cite blogs or secondary summaries when primary papers/docs are available.
- Do not call a result impossible without checking units and assumptions.
- Do not confuse a synthetic demo with benchmark reproduction.
- Do not treat external literature as exact ground truth if settings differ.
- Do not bury major data problems after a long praise section.
