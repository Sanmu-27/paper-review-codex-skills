# Ready-to-Use Prompts

## Strong Full Audit

```text
Use the ai-paper-review skill. Perform the full Deep AI Paper Review Workflow, not a quick summary. Inspect the paper source, bibliography, checklist, appendix, and submission-ready package if available. Build a claim ledger, issue ledger, and fix ledger. Focus on reviewer-grade issues: mathematical ambiguity, algorithm/constraint mismatch, system feasibility, baseline fairness, reproducibility, checklist completeness, broken references, and overclaiming. Give a realistic NeurIPS/ICML-style verdict and confidence.
Also identify the 1-3 central claims, say whether each is actually supported, and simulate the top reviewer attacks most likely to land.
```

## Chinese Trigger Prompt

```text
审稿。按 NeurIPS 水平完整看这篇论文，调用 ai-paper-review 的全部流程：源文件、PDF、bib、checklist、图文对比、submission package、supplementary code、central claims、hard blockers、top reviewer attacks、likely score、P0/P1/P2 修稿建议。
```

## Strong Full Audit With Explicit Path

Use this when the skill has not been installed into `%USERPROFILE%\.codex\skills`.

```text
Use the ai-paper-review skill at <path-to-ai-paper-review>. Perform the full Deep AI Paper Review Workflow on <paper-or-source-path>. Inspect the rendered PDF, main tex, bibliography, checklist, figures, submission package, and supplementary code if available. Start with venue calibration, central claims, artifact audit, and top reviewer attacks. Then give hard blockers, major issues, likely score, confidence, and P0/P1/P2 fixes.
```

## Submission-Readiness Audit

```text
Use the ai-paper-review skill. Audit this paper for submission blockers. Prioritize hard errors that could trigger reviewer distrust or desk-check problems: stale source packages, missing checklist answers, wrong citations, broken refs, inconsistent equations/algorithms, impossible hardware claims, and unsubstantiated reproducibility statements. Output P0/P1/P2 fixes.
Run the artifact quick-check if present and distinguish toy verification from full reproduction.
```

## Fast Static LaTeX Audit

```text
Use the ai-paper-review skill. First run scripts/audit_tex_submission.py on the main tex file. Treat the script output as leads, then manually verify any high-severity findings against the source, checklist, bibliography, and submission-ready package. Output only confirmed blockers and high-value fixes.
```

## Reviewer Score Only

```text
Use the ai-paper-review skill. Act as an objective conference reviewer. Read the paper for contribution, evidence, novelty, correctness, clarity, and reproducibility. Give strengths, weaknesses, questions, a realistic score on the venue scale, confidence, and the top reasons driving the score. Be skeptical but fair.
```

## Rebuttal Preparation

```text
Use the ai-paper-review skill. Predict likely reviewer criticisms and prepare a rebuttal-readiness report. Separate criticisms into fix-before-submission, answer-in-rebuttal, and accept-as-limitation. For each likely criticism, provide the evidence a reviewer will cite and the best response or edit.
Prioritize the attacks that affect acceptance rather than cosmetic complaints.
```
