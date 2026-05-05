# PAT-Style Review Checklist

Use this checklist to emulate a strong automated reviewer that can still surface reviewer-grade issues.

## A. Claims and Scope

Check:
- Do abstract and intro match the true contribution?
- Are diagnostic results mislabeled as deployment claims?
- Are theoretical motivations overstated as guarantees?
- Are transfer/generalization claims larger than the evidence?
- Are the central acceptance-driving claims obvious and narrowly stated?

Typical findings:
- "design motivation presented as proof"
- "diagnostic comparator described too close to deployable method"
- "scope statement too broad for evaluated evidence"

## B. Method Correctness

Check:
- Are all symbols defined before use?
- Do equations match prose?
- Does algorithm pseudocode implement the stated constraint?
- Are pooled features, gradients, and labels mathematically compatible?
- Are dot products later called cosine similarity without normalization?
- Are complexity claims dimensionally correct?

Typical findings:
- token budget vs step budget mismatch
- inconsistent MLP input dimension
- undefined gradient target
- stale or incorrect recurrence/EMA bound

## C. System Feasibility

Check:
- Does the stated hardware fit the claimed model/batch/context?
- Is the serving prototype clearly separated from algorithmic results?
- Are engine-specific hooks required but hidden?
- Does block/page alignment create unmentioned implementation overhead?

Typical findings:
- impossible VRAM budget
- metadata-only eviction claim ignores fragmented pages
- batch-size-specific latency reused as if universal

## D. Experimental Credibility

Check:
- Are baselines fair and strong?
- Are all methods evaluated under the same counted budget?
- Are train/eval domains or seeds separated?
- Are error bars defined?
- Are there contradictions across tables, figures, and appendix?
- Are gains caused by the main method or by fallback/guard logic?
- Are the decisive claims supported in the main paper, or only in appendix diagnostics?

Typical findings:
- strong headline but fallback drives performance on dense tasks
- proxy/diagnostic confusion
- reported overhead inconsistent across sections
- acceptance-driving claim supported only by appendix or artifact caveat

## E. Figure-Text Consistency

Check:
- Do figures and tables support the exact prose claim attached to them?
- Do captions describe the plotted data, not a stronger interpretation?
- Are axes, legends, units, budgets, datasets, seeds, and error bars defined?
- Are visual trends consistent with main and appendix tables?
- Are qualitative examples clearly marked as examples rather than evidence of typical behavior?
- Does the rendered PDF keep labels and table values readable?

Typical findings:
- caption overstates trend shown in plot
- figure/table values disagree with abstract or main text
- diagnostic visual used as deployable-method evidence
- missing units, seed count, or budget definition in figure
- unreadable legend or compressed table in PDF

## F. Writing and Presentation Hygiene

Check:
- broken LaTeX refs
- unresolved placeholders
- bibliography casing
- wrong citations
- mismatched figure captions
- checklist completeness
- README / manifest / checklist / paper all agree on what is reproducible

Typical findings:
- wrong paper cited for method name
- checklist not filled
- appendix and submission-ready source out of sync
- artifact README over-promises relative to actual runnable scope

## G. Severity Rubric

Use:
- `Hard blocker`: likely to hurt acceptance if noticed by reviewers
- `Major weakness`: not fatal alone, but materially weakens confidence
- `Moderate issue`: should be fixed for rebuttal/submission quality
- `Polish`: hygiene or wording issue

Escalate severity when a problem:
- undermines correctness
- makes reproduction impossible
- creates distrust in the results
- implies unfair comparison
