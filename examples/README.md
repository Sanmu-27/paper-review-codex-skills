# Examples

These examples show how to invoke the skills and what kind of output to expect. They are intentionally generic and do not include private paper content.

## Full Paper Review

Prompt:

```text
Use $ai-paper-review to review this ML paper like a rigorous NeurIPS reviewer. Inspect the PDF, LaTeX source, bibliography, checklist, figures, and artifact folder. Give central claims, hard blockers, score, confidence, and P0/P1/P2 fixes.
```

Expected output shape:

- artifact audit
- venue calibration
- central-claim support matrix
- strengths
- major weaknesses
- section-by-section findings
- likely reviewer attacks
- score and confidence
- prioritized revision plan

## Data And Table Audit

Prompt:

```text
Use $paper-data-auditor to audit this paper's reported numbers, tables, configs, and artifact evidence. Check internal consistency and external plausibility.
```

Expected output shape:

- verdict and risk level
- evidence inspected
- claim ledger summary
- arithmetic/table findings
- external calibration
- reproducibility boundary
- P0/P1/P2 fix list

## Rebuttal Strategy

Prompt:

```text
Use $paper-rebuttal-strategist to triage these reviews, identify decision-critical concerns, plan evidence, and draft a concise rebuttal.
```

Expected output shape:

- decision diagnosis
- reviewer belief map
- issue triage
- evidence/action plan
- polished response draft
- risky arguments to avoid

## Artifact Release Check

Prompt:

```text
Use $artifact-release-auditor to inspect this artifact zip and GitHub repo for reproducibility, anonymity, release hygiene, and paper-artifact alignment.
```

Expected output shape:

- artifact verdict
- runnable boundary
- paper-alignment findings
- anonymity/security/license findings
- README wording suggestions

## Camera-Ready Final Pass

Prompt:

```text
Use $camera-ready-polisher to audit this final paper/source package for camera-ready risks, consistency, and exact last edits.
```

Expected output shape:

- final-readiness verdict
- promised-change checklist
- high-risk consistency issues
- wording improvements
- source/package issues
- final P0/P1/P2 actions
