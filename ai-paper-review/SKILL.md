---
name: ai-paper-review
description: Review machine learning, systems-for-ML, and LLM papers at rigorous conference-review depth. Use whenever the user asks for 审稿, 评审, 论文review, paper review, NeurIPS/ICML/ICLR水平, 按顶会水平看, critique a paper, score a submission, audit rebuttal readiness, inspect a LaTeX/PDF draft, or find mathematical inconsistencies, reproducibility gaps, checklist issues, broken references, experimental weaknesses, figure-text mismatches, artifact problems, or writing problems. Especially use for PAT-style or reviewer-style strengths/weaknesses, section-by-section issue finding, actionable revision advice, central-claim support checks, top reviewer attacks, and structured review forms.
---

# AI Paper Review

## Overview

Review papers like a sharp conference reviewer, not a summarizer. Prefer finding concrete weaknesses, inconsistencies, missing assumptions, unfair comparisons, implementation ambiguity, and reproducibility risks over giving vague praise.

When possible, inspect the source `.tex`, bibliography, checklist, and submission package instead of only reading a rendered PDF. Treat the paper as a claim set that must be stress-tested for internal consistency.

## Installation And Use

For automatic discovery, place this folder at:

```text
%USERPROFILE%\.codex\skills\ai-paper-review
```

Then start a new Codex thread or reload the app. Trigger it with requests such
as:

```text
Use the ai-paper-review skill. Perform a full NeurIPS-style audit of this paper.
Inspect the source, PDF, checklist, bibliography, figures, and supplementary
code. Give central claims, hard blockers, likely reviewer score, and P0/P1/P2
fixes.
```

If the skill is not installed globally, pass its folder path explicitly:

```text
Use the ai-paper-review skill at <path-to-this-folder>.
Review <path-to-paper.pdf> and the matching source folder.
```

For LaTeX submissions, run the static audit helper early:

```powershell
python <skill_dir>\scripts\audit_tex_submission.py <path-to-main.tex>
```

For maximum effect, provide the rendered PDF, main `.tex`, `.bib`, checklist,
submission-ready zip/folder, and supplementary code. By default, produce a
complete review in one pass rather than a brief verdict: include artifact
audit, central claims, support matrix, major findings, section-by-section
analysis, likely reviewer attacks, score rationale, and a prioritized fix plan.

## Default Workflow

Use the full workflow in `references/deep-review-workflow.md` by default for any generic "审稿", "review this paper", "按 NeurIPS 水平看", or submission-readiness request. It is the primary operating procedure for this skill.

Use the shorter workflow below only when the user explicitly asks for a quick
review, asks for a concise verdict, when artifacts are limited, or when
time/compute makes the full workflow impossible.

1. Identify the review mode:
- If the user asks for a score, produce a conference-style review with verdict and confidence.
- If the user asks for revision help, prioritize actionable fix lists.
- If the user asks whether a paper is "safe to submit", prioritize hard blockers.
- Calibrate to the venue and contribution type before scoring: theory, empirical ML, systems-for-ML, LLM agents, benchmarks, or artifacts can fail for different reasons.

2. Gather artifacts in this order when available:
- Main `.tex`
- `checklist.tex`
- `.bib` / `.bbl`
- submission-ready source folder or zip
- rendered PDF or screenshots if layout matters
- supplementary code / artifact README / manifest
- rebuttal, reviews, or venue form if the user provides them

Run `scripts/audit_tex_submission.py <main.tex>` early when reviewing LaTeX submissions. Use its findings as leads, not as final judgments.
If a runnable artifact exists, execute its documented quick-check command when feasible. Treat successful execution as evidence about artifact scope, not proof that the paper's main claims are reproduced.

3. Read for claims before judging details:
- title, abstract, intro contributions
- method definition and objective
- experimental setup
- main tables/figures
- limitations, ethics, checklist, appendix claims

4. Stress-test the paper along four axes:
- scientific correctness
- implementation/reproducibility
- empirical credibility
- submission hygiene
- figure-text consistency
- reviewer attack surface

5. Prefer quoting exact symbols, equations, table names, section names, and file/line references when working from source. Make issues falsifiable.

6. Distinguish clearly between:
- hard errors: contradictions, broken math, impossible hardware claims, unfair baselines, missing checklist content
- soft weaknesses: novelty concerns, thin ablations, under-motivated design choices, writing clarity

7. Separate evidence for the central claim from supporting color:
- Which 1-3 experiments actually carry acceptance weight?
- Which appendix analyses are diagnostic only?
- Which attractive figures are illustrative but not decisive?
- Could the paper survive if a skeptical reviewer ignored every appendix-only result?

## Review Priorities

### 1. Attack internal inconsistency first

Check whether the same concept changes across sections:
- training label definition
- optimization target
- budget definition
- architecture dimensions
- complexity notation
- hardware setup
- benchmark protocol
- figure/table values
- checklist statements

If the paper says one thing in the main text and another in the appendix, treat that as a reviewable issue even if either version could be valid by itself.

### 2. Prefer source-grounded criticism

Good review comments usually look like:
- "Eq. 2 defines X, but Appendix C.4 trains on Y."
- "Algorithm 1 enforces a step budget while Section 4 reports a token budget."
- "Table 7 implies a hardware configuration that does not fit in the stated GPU memory."

Avoid generic comments like:
- "the math is unclear"
- "experiments could be stronger"

### 3. Be strict about evaluation credibility

Check:
- whether baselines are strong and fairly budget-matched
- whether "diagnostic" comparators are mistakenly presented as deployable baselines
- whether means/std, seeds, splits, and training domains are stated
- whether transfer claims are overstated relative to evidence
- whether latency/system claims use a reproducible stack

### 4. Treat checklists and references as part of the paper

A paper can look strong scientifically and still feel sloppy if:
- checklist is incomplete
- bibliography casing is broken
- citations point to the wrong paper
- unresolved LaTeX references remain
- source package and main draft disagree

### 5. Compare figures/tables against the text

Treat every figure, table, and caption as a claim. Check whether the visual
evidence actually supports the surrounding prose:
- Does the caption match what is plotted?
- Do axis labels, legends, colors, units, budgets, and baselines match the text?
- Are figure callouts consistent with the main numerical tables?
- Does the PDF rendering preserve readability, ordering, and visual hierarchy?
- Are qualitative figures illustrative only, or are they being used as evidence?

Escalate the issue when a figure is used to support a central claim but the
visual, caption, or surrounding prose tells a different story.

### 6. Simulate a skeptical reviewer

Before finalizing, ask:
- What are the top 3 reasons a strong reviewer would reject this paper?
- Which of those are real scientific problems versus avoidable trust problems?
- If the authors had only 24 hours, which edits would most improve the score?

## Output Style

When the user asks for a review, default to a full-length report rather than a
compressed memo. Unless the user explicitly asks for a quick or short review,
the default output must be long enough to read like a real conference review
package, not just a verdict summary.

Default full-review order:
1. artifact audit
2. venue calibration
3. short overall summary
4. central claims and support status
5. strengths
6. top hard blockers / major weaknesses
7. section-by-section findings
8. theory / math / algorithm audit when applicable
9. experiments / figures / tables / artifact audit
10. questions for authors
11. suggested score / confidence / confidence rationale
12. top reviewer attacks
13. concrete revision actions

Minimum expectations for a default full review:
- cover the main sections of the paper, not only the final verdict
- include enough evidence and explanation that the user can see why each major
  criticism matters
- surface both scientific-risk issues and trust / packaging / reproducibility
  issues
- use file, section, equation, algorithm, figure, or table anchors whenever
  possible
- prefer a report that is too complete over one that is too short

Do not collapse a generic "review this paper" request into a 1-3 paragraph
answer unless the user explicitly asks for brevity.

When the user asks for revision help instead of a formal review:
1. hard blockers
2. moderate issues
3. polish issues
4. exact edits to make

For strong audits, also surface:
- the 1-3 central claims
- whether each central claim is convincingly supported
- the top reviewer attack that is most likely to land
- the specific evidence chain behind each high-severity concern
- the difference between fatal issues, salvageable issues, and polish issues

If the request is "objective reviewer view", be fair but do not hedge away real problems.

## Scoring Guidance

Use the venue's actual scale if known. If the venue/year is current or could have changed, verify it.

If no official scale is available, give:
- likely accept/reject leaning
- rough confidence
- the top 2-4 reasons driving that judgment

Do not inflate scores just because the idea is interesting. Penalize papers that would trigger reviewer distrust through inconsistency or poor reproducibility framing.

## References

Read these when you need deeper structure:
- `references/deep-review-workflow.md` for the full multi-stage audit workflow
- `references/review-checklist.md` for a PAT-style issue taxonomy
- `references/output-template.md` for structured review templates and severity wording
- `references/prompts.md` for ready-to-use prompts

## Validation Habit

Before finalizing a review, do one last pass:
- Are all major criticisms tied to specific evidence?
- Are any supposed errors already fixed in another file/version?
- Are you mixing "could be better" with "is wrong"?
- If a problem is severe, have you explained why it matters for acceptance?
