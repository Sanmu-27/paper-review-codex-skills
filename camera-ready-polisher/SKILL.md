---
name: camera-ready-polisher
description: Polish accepted or near-final research papers for camera-ready submission. Use when the user asks for camera-ready checks, final paper polish, LaTeX cleanup, checklist consistency, title/abstract/conclusion tightening, limitation wording, citation hygiene, figure/table caption fixes, supplementary consistency, or final upload risk reduction for ML/AI conference papers.
---

# Camera-Ready Polisher

## Purpose

Use this skill after a paper is accepted, conditionally accepted, or close to submission-final. The goal is to reduce final-upload risk and improve clarity without accidentally changing claims, invalidating reviewer commitments, or introducing formatting problems.

## Workflow

### 1. Establish Constraints

Identify:

- venue and year
- page limit, appendix policy, checklist policy, author-response commitments
- whether the paper is anonymous or de-anonymized
- final submission artifacts: PDF, source zip, supplement, code link

If venue rules may have changed, verify official instructions before giving final-upload advice.

### 2. Commitments From Reviews

If reviews or rebuttal are provided:

- list every promised change
- verify each appears in the draft
- mark promises that were only partially addressed
- avoid adding new claims that were not reviewed unless necessary and safe

### 3. Consistency Sweep

Check:

- title, abstract, intro contributions, conclusion, limitations
- method names and notation across main text and appendix
- table/figure numbers, captions, legends, axis labels, units
- result values across abstract, text, tables, appendix, README
- checklist answers versus paper content
- bibliography casing, venue names, arXiv versions, missing citations

### 4. Claim Tightening

Improve wording by:

- replacing broad claims with scope-controlled claims
- making limitations honest but not self-damaging
- separating evidence-backed results from intuition
- removing stale novelty language after rebuttal concessions
- making contribution bullets concrete and non-overlapping

Do not hide limitations that reviewers or venue policy expect to see.

### 5. Upload Package Audit

Check source and supplement:

- no stale PDFs or old titles
- source zip contains all required style files, bibliography, figures, checklist
- no build artifacts that violate policy
- no local absolute paths in scripts or LaTeX
- final PDF builds from the packaged source when feasible

## Output Format

Use:

1. final-readiness verdict
2. promised-change checklist
3. high-risk consistency issues
4. wording improvements
5. LaTeX/source/package issues
6. exact P0/P1/P2 final actions

For editing tasks, provide exact replacement text or patch the files when possible.

## Reference Files

Read `references/final-pass-checklist.md` for a camera-ready checklist and wording patterns.
