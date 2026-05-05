# Paper Review Skills for Codex

A small collection of Codex skills for reviewing, stress-testing, and polishing ML/AI research papers.

These skills are designed for practical paper work rather than generic summarization: conference-style review, experimental number auditing, rebuttal planning, artifact release checks, and camera-ready cleanup.

## Skills

| Skill | Use it for |
| --- | --- |
| `ai-paper-review` | Full NeurIPS/ICML/ICLR-style paper review with source, PDF, checklist, bibliography, figure, and artifact checks. |
| `paper-data-auditor` | Auditing tables, reported numbers, system measurements, arithmetic, configs, and external plausibility. |
| `paper-rebuttal-strategist` | Triage reviewer comments, plan evidence, and draft concise rebuttal responses. |
| `artifact-release-auditor` | Check research code or supplement packages for reproducibility, anonymity, security, and release hygiene. |
| `camera-ready-polisher` | Final pass for accepted or near-final papers: claims, checklist, captions, LaTeX/source package, and upload risks. |

## Install

Copy any skill folder into your Codex skills directory:

```powershell
Copy-Item -Recurse .\ai-paper-review $env:USERPROFILE\.codex\skills\
```

Restart Codex or open a new thread, then invoke a skill explicitly:

```text
Use $ai-paper-review to review this paper like a rigorous NeurIPS reviewer.
```

Each skill is self-contained and includes its own `SKILL.md`. Some skills include scripts or reference checklists that Codex can load or run when useful.

## Suggested Workflow

1. Use `ai-paper-review` for the broad conference-style review.
2. Use `paper-data-auditor` when the decision depends on tables, metrics, claims, or system feasibility.
3. Use `paper-rebuttal-strategist` after reviews arrive.
4. Use `artifact-release-auditor` before uploading supplements or code.
5. Use `camera-ready-polisher` for the final accepted-paper pass.

## Notes

- The scripts are conservative scanners. Treat their findings as leads for expert review, not proof of paper flaws.
- When current venue rules matter, verify the official venue instructions before relying on procedural advice.
- These skills are prompt/workflow tools, not a substitute for domain expertise or author judgment.
