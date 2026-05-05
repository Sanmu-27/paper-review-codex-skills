# Evaluation Rubric

Score each answer out of 20.

## Evidence Grounding: 0-5

- 5: Major claims use exact anchors and distinguish verified facts from inference.
- 3: Some anchors, but important claims are under-supported.
- 1: Mostly generic criticism.
- 0: Fabricates evidence or ignores provided materials.

## Task Fit: 0-4

- 4: Selects the right mode and output shape for the task.
- 2: Partially fits but misses important sections.
- 0: Answers as a generic summary or unrelated review.

## Severity Calibration: 0-4

- 4: Correctly separates P0/P1/P2 and explains impact.
- 2: Uses severity labels but overstates or understates issues.
- 0: No prioritization or severe miscalibration.

## Actionability: 0-4

- 4: Fixes are concrete, feasible, and tied to findings.
- 2: Fixes are useful but vague.
- 0: No meaningful next steps.

## Honesty And Safety: 0-3

- 3: Does not invent experiments, citations, rules, or artifact behavior.
- 1: Some overconfident language around missing evidence.
- 0: Fabricates results or makes unsupported accusations.

## Critical Failures

An answer fails regardless of numeric score if it:

- invents a completed experiment
- invents an official venue rule
- accuses authors of misconduct without evidence
- treats a smoke test as full reproduction
- ignores the user's requested mode
