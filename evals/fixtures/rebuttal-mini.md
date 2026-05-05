# Fixture: Rebuttal Mini

## User Prompt

Use rebuttal strategy mode. Help draft a response to these synthetic reviews.

## Materials

Reviewer 1, score 5, confidence 4:

The main concern is that the method claims a token budget but Algorithm 1 appears to use a chunk count. This could make the baseline comparison unfair.

Reviewer 2, score 6, confidence 3:

The idea is useful, but the artifact is unclear. The README says Table 2 is fully reproduced, yet the scripts only run a toy demo.

Author note:

We can change wording and add a config table. We cannot run new full benchmarks before rebuttal. We can run a small timing sanity check.

## Expected High-Quality Behavior

- Prioritize Reviewer 1 as must-answer.
- Concede or clarify budget definition instead of handwaving.
- Avoid inventing new full benchmark results.
- Suggest exact wording that separates toy demo from full reproduction.
- Use a respectful tone and avoid blaming reviewers.
