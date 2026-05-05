# Expert Rubric

Use this rubric after the internal and external checks.

## Severity

`P0`:

- central table cannot be traced to any plausible evaluation path
- method in code is materially different from method in paper
- final PDF/source/version mismatch could cause wrong upload
- arithmetic or memory feasibility error invalidates a headline claim
- benchmark protocol contradicts official task definition

`P1`:

- configs differ from hyperparameter table
- artifact supports only a demo while checklist implies full reproduction
- baseline implementation or prompt protection is underspecified
- training label definition drifts across method, appendix, and code
- system results depend on unpublished hooks but are framed too strongly

`P2`:

- stale terminology in caption or README
- unclear units, missing rounding rules, missing std definition
- packaging hygiene such as cache files or local logs
- citation/version ambiguity

## Confidence

High confidence:

- directly verified in source/code/output
- arithmetic recomputed
- external primary source confirms mismatch

Medium confidence:

- strong inference from available files
- missing artifact prevents full verification
- external setting is close but not identical

Low confidence:

- plausible concern but needs author clarification
- external evidence is only directional

## Acceptance Risk Translation

- Multiple unresolved P0s: likely reject regardless of novelty.
- One P0 plus strong idea: borderline/weak reject unless easy to fix before submission.
- Several P1s: reviewer trust risk; can move a 6 to a 5.
- Mostly P2s: hygiene; unlikely to decide acceptance alone.

## Expert Questions

Ask these before final verdict:

- What exact mechanism does the data support?
- What alternative explanation remains?
- Are improvements larger than expected for the change made?
- Does the artifact prove the main claim or only show the shape of the algorithm?
- Would an area chair view the limitation as honest scope control or missing evidence?
