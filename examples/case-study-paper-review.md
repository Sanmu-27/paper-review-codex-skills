# Case Study 1: Anonymous Paper Review

## Scenario

A user asked for a full NeurIPS-style review of an ML systems paper that claimed large KV-cache savings with minimal accuracy loss. They provided a PDF excerpt, source snippets, and an artifact README.

## Input Snapshot

- claim: "reduces KV-cache memory by 70% with negligible overhead"
- method text described a fixed budget
- algorithm enforced `len(heap) <= B`
- experiment section compared retained token ratios
- artifact README said the toy demo "fully reproduces Table 2"

## What A Strong Agent Should Surface

1. The budget object is inconsistent: the algorithm uses a chunk/step count while the evaluation claim is framed as a token budget.
2. "Negligible overhead" is too strong without a precise timing protocol, hardware, precision, and batching setup.
3. The artifact README overstates scope: a toy demo is not the same as benchmark reproduction.
4. The acceptance risk is trust and evaluation framing, not necessarily that the core idea is false.

## Example Output Excerpt

> **Verdict:** borderline reject to weak reject, medium confidence. The paper's main idea is plausible, but the central empirical claim is weakened by a budget-definition mismatch and an artifact scope contradiction.
>
> **P0:** Algorithm 1 enforces a count-style budget (`len(heap) <= B`), while Table 2 is framed as a retained-token budget. Without a clear mapping between chunks and tokens, the baseline comparison may not be capacity-matched.
>
> **P1:** The overhead claim is under-supported. No exact timing protocol, hardware stack, precision, or batch settings are given, so "negligible" reads stronger than the evidence.
>
> **P1:** The README states that the repository fully reproduces Table 2, but the documented entry point runs only a toy demo. This is a reproducibility-boundary problem rather than proof that the result is wrong.

## Why This Is A Good Showcase

- specific, falsifiable findings
- calibrated severity
- no fabricated experiments
- separates scientific risk from trust and packaging risk
