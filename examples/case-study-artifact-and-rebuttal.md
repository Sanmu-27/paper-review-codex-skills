# Case Study 2: Anonymous Artifact Audit And Rebuttal

## Scenario

A user had received reviews and needed two things fast:

- an artifact-readiness check for anonymous submission
- a rebuttal draft that addressed reviewer concerns without inventing new experiments

## Input Snapshot

Artifact package:

- `README.md`: "One command fully reproduces all paper tables."
- `demo.py`: toy example only
- `configs/table2.yaml`: local absolute path
- `.env`: contained an API key
- `paper_source.zip`: included `__pycache__` and an older PDF name

Reviews:

- Reviewer 1 questioned whether the budget definition made the comparison unfair.
- Reviewer 2 said the artifact language overclaimed reproduction.

## What A Strong Agent Should Surface

### Artifact audit

- `P0`: secret leak in `.env`
- `P0` or strong `P1`: local absolute path that will break external execution and may hurt anonymity
- `P1`: README overclaims full reproduction
- `P2`: stale package hygiene (`__pycache__`, old PDF)

### Rebuttal strategy

- prioritize the budget-definition concern first
- concede and clarify what the current artifact actually supports
- avoid claiming new full benchmark reruns
- promise wording and config-table fixes that are actually feasible before deadline

## Example Output Excerpt

> **Artifact verdict:** not ready for anonymous submission.
>
> **P0:** `.env` contains an API credential. This is both a security issue and an avoidable submission mistake.
>
> **P1:** The repository documents only a toy demo, yet the README claims one-command reproduction of all paper tables. The package should instead separate smoke test, benchmark driver, and unavailable components.
>
> **Rebuttal note:** Reviewer 1's concern should be answered before the artifact wording issue because it directly affects fairness of the main comparison. The response should acknowledge the budget-definition ambiguity, state how the paper will be revised, and avoid implying that new full experiments were completed.

## Why This Is A Good Showcase

- covers both code artifact and review response workflows
- shows conservative honesty under deadline pressure
- demonstrates release hygiene plus decision-aware rebuttal planning
