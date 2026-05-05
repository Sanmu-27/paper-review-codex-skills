# Deep AI Paper Review Workflow

Use this workflow for a reviewer stronger than a one-pass PAT-style critique. The goal is not only to write a review, but to build an evidence ledger that catches contradictions across the paper, appendix, bibliography, checklist, and submission package.

## Stage 0. Artifact Inventory

Input:
- paper PDF, `.tex`, `.bib`, checklist, appendix, supplementary code, source zip, screenshots, OpenReview metadata if provided

Actions:
- List available artifacts and identify the authoritative version.
- If both working source and submission-ready source exist, compare them for drift.
- Note files that cannot be inspected.

Output:
- "Artifacts inspected"
- "Artifacts missing"
- "Version drift risks"

Red flags:
- submission zip contains stale source
- checklist in main source differs from checklist in packaged source
- PDF was generated from a different `.tex` than the one under review

## Stage 0.5 Venue and Contribution Calibration

Actions:
- Identify the target venue and year.
- Infer the paper's contribution type: theory, empirical method, systems, benchmark, analysis, or artifact-heavy submission.
- Calibrate likely reviewer expectations and failure modes for that type.

Output:
- Venue calibration note
- Contribution type
- Likely decision criteria

Red flags:
- theory-style claims with only empirical support
- systems-style claims without credible implementation evidence
- benchmark/artifact claims without runnable scope boundaries

## Stage 1. Claim Ledger

Actions:
- Extract claims from title, abstract, intro bullets, main result table, limitations, and conclusion.
- Classify each claim as method, theory, empirical, system, reproducibility, or scope.
- For each claim, find where it is supported.

Output table:
- Claim
- Type
- Evidence location
- Risk level
- Reviewer attack surface

Red flags:
- "first", "novel", "guarantee", "drop-in", "low overhead", "reproducible" without direct evidence
- abstract claims not matched by experiments
- appendix contains stronger claims than main text

## Stage 1.5 Central-Claim Support Matrix

Actions:
- Identify the 1-3 claims that would actually determine acceptance.
- For each, list the minimum evidence needed for a reviewer to believe it.
- Mark whether the support is main-paper evidence, appendix-only evidence, artifact evidence, or unsupported.

Output table:
- Central claim
- Importance to verdict
- Evidence actually provided
- Support status
- Main reviewer attack

Red flags:
- headline claim supported only in appendix
- central system claim supported only by a prototype note
- broad generalization claim supported only by transfer diagnostics

## Stage 2. Definitions and Symbol Audit

Actions:
- Track all key symbols across equations, prose, algorithms, and appendix.
- Check whether constraints are dimensionally consistent.
- Check whether named quantities are normalized, signed, averaged, pooled, or detached.

Common targets:
- budget: steps vs tokens vs pages vs layers
- labels: gradient norm vs signed utility vs LOO labels
- scorer input: dimensions and feature list
- entropy: raw vs normalized
- similarity: dot product vs cosine
- complexity: asymptotic variables vs empirical latency

Output:
- List contradictions with exact source anchors.
- Proposed unifying definition.

Red flags:
- same symbol has two meanings
- an algorithm enforces a different constraint than experiments report
- a gradient is taken with respect to a representation outside the computation graph

## Stage 3. Algorithm-to-Implementation Audit

Actions:
- Read pseudocode line by line and simulate edge cases.
- Check variable initialization, variable shadowing, loop invariants, and budget invariants.
- Compare algorithm with system implementation and experiments.

Stress cases:
- variable-length chunks
- empty buffers
- malformed delimiters
- anchors larger than budget
- fragmented memory pages
- lazy re-ranking after score changes

Output:
- Algorithm correctness findings
- Implementation ambiguity findings
- Minimal patch suggestions

Red flags:
- capacity is a count of items but claim is memory/token budget
- eviction can violate an invariant
- serving stack assumes page alignment without handling partial pages

## Stage 4. Math and Theory Audit

Actions:
- Check whether derivations actually prove the stated result.
- Separate intuition, diagnostic assumptions, and deployed guarantees.
- Verify signs, norms, gradients, recurrence expansions, and approximation steps.

Common targets:
- Taylor expansion signs
- gradient magnitude vs signed utility
- RankNet target mapping
- EMA/staleness bounds
- submodularity/diminishing returns arguments
- facility-location to additive proxy transitions

Output:
- Math issues by severity.
- Suggested weaker but defensible statement.

Red flags:
- circular proof: assumes the property it claims to prove
- equality that requires an unstated non-redundancy assumption
- unsigned saliency used to justify filtering harmful tokens
- old formula remains in appendix after main text changed

## Stage 5. Experimental Protocol Audit

Actions:
- Reconstruct the experimental protocol from the paper.
- Check whether baselines receive equal budgets and comparable information.
- Check train/eval split, seeds, number of runs, standard deviations, and domain transfer claims.
- Identify which results support the central claim and which are diagnostic.

Output:
- Protocol summary
- Fairness concerns
- Missing ablations
- Overclaim risks

Red flags:
- learned method compared against weak or unprotected baseline
- diagnostic oracle included near deployable methods
- fallback mechanism drives gains but method claims ranking superiority
- transfer result is framed as generalization

## Stage 6. Figure-Text and Table-Text Audit

Actions:
- Compare every main figure/table against its caption and surrounding prose.
- Check whether plotted trends, table values, and qualitative examples support the exact claim being made.
- Verify axes, legends, units, budget definitions, confidence bands, seeds, and baseline names.
- Cross-check repeated numbers across abstract, intro bullets, main tables, appendix tables, and captions.
- Inspect rendered PDF pages when layout or readability matters.

Output:
- Figure/table consistency findings
- Visual evidence strength notes
- Caption or text rewrite suggestions

Red flags:
- caption claims a trend that is not visually shown
- plotted baseline names differ from table/prose names
- figure uses diagnostic results to support a deployable-method claim
- axes omit units, budgets, seeds, or whether values are mean/std
- qualitative examples are framed as representative without sampling details
- PDF rendering makes labels, legends, or table values unreadable

## Stage 7. Artifact Execution and Scope Audit

Actions:
- Run the documented quick-check or demo command when feasible.
- Compare what the artifact actually executes against what the paper/checklist imply.
- Distinguish inspectable policy logic, synthetic demos, benchmark drivers, and full end-to-end reproduction.

Output:
- Executed commands
- What they verify
- What they do not verify
- Scope mismatch findings

Red flags:
- README implies reproducibility but only runs a toy demo
- benchmark script measures a proxy instead of the claimed system metric
- required checkpoints or engine hooks are omitted from the reproducibility framing

## Stage 8. System Feasibility Audit

Actions:
- Check hardware feasibility with rough memory math.
- Separate algorithmic evaluation from serving benchmark.
- Inspect whether engine-specific hooks are required.
- Check whether latency numbers are batch-size, model-size, and hardware specific.

Output:
- Feasibility verdict
- Reproducibility caveat
- Hardware consistency notes

Red flags:
- 70B + long context + large batch claimed on one GPU without quantization or tensor parallelism
- "zero-copy" eviction ignores page fragmentation
- per-step latency from one setup cited as if universal

## Stage 9. Reproducibility and Submission Hygiene Audit

Actions:
- Check checklist answers against paper content.
- Check `.bib` keys, casing, missing citations, and wrong method references.
- Check source zip and working source are synchronized.
- Check code artifact scope: simulator vs full implementation.

Output:
- Submission hygiene report
- Source package risks
- Checklist risks

Red flags:
- unresolved placeholder in checklist
- wrong paper cited for a named method
- source package contains stale tex
- code cannot reproduce headline claims despite checklist saying yes

## Stage 10. Reviewer Attack Simulation

Actions:
- Generate the top 3 strongest reviewer attacks.
- For each, state whether it is a correctness issue, an evidence gap, or a trust/presentation problem.
- Estimate whether a rebuttal could realistically save it.

Output:
- Attack
- Type
- Likely reviewer severity
- Rebuttal survivability
- Best pre-submission fix

Red flags:
- paper depends on rebuttal to explain core protocol details
- central trust issue cannot be repaired without new experiments
- strongest likely attack is avoidable by wording or packaging but currently unaddressed

## Stage 11. Reviewer Review Form

Actions:
- Convert findings into a realistic review.
- Lead with the strongest concerns.
- Avoid listing every polish issue unless asked.
- Give a score only after weighing novelty, correctness, evidence, and trust.

Output:
- Summary
- Strengths
- Weaknesses
- Questions
- Score and confidence
- Actionable revision plan

Score heuristic:
- Strong accept: novel, correct, well-supported, reproducible, no major trust issues.
- Accept: clear contribution and solid evidence; only moderate weaknesses.
- Borderline accept: useful contribution but novelty or rigor concerns remain.
- Borderline reject: interesting but trust, reproducibility, or claim mismatch issues.
- Reject: core method, evaluation, or claims are not credible.

## Stage 12. Fix Plan Mode

Use when the user asks to improve the paper.

Actions:
- Convert review findings into edits ordered by acceptance impact.
- Prefer minimal wording changes when evidence cannot be improved.
- Prefer source edits when contradictions are purely textual.

Output:
- Fix now
- Fix if time
- Leave as is
- Risk after fix

Rule:
- Do not merely say "clarify"; propose the clarification.
