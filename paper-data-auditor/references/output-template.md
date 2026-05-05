# Output Template

Use this shape for a full audit. Keep it concise when the task is narrow.

```markdown
**Verdict**
Overall risk: ...
Likely score / decision: ...
Confidence: ...

**Evidence Inspected**
- local files:
- commands run:
- external sources:

**Claim Ledger Summary**
| Claim | Evidence | Status | Notes |
|---|---|---|---|
| ... | ... | supported / partial / weak / contradicted | ... |

**Findings**
1. `P0/P1/P2` Title
   Evidence: file/line or source.
   Why it matters:
   Fix:

**External Calibration**
- Source:
- Comparison quality:
- Implication:

**Reproducibility Boundary**
- Runnable locally:
- Requires external assets:
- Requires unpublished hooks/checkpoints:

**Fix List**
- `P0` ...
- `P1` ...
- `P2` ...
```

For review-style output, put findings before praise. For author-support output, include a short strengths section after the main risks.
