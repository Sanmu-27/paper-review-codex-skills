# Fixture: Full Review Mini

## User Prompt

Use the paper review workflow to review the following synthetic paper excerpt.

## Materials

Title: FastCache: Token Budgeting for Long-Context Generation

Abstract excerpt:

FastCache reduces KV-cache memory by 70% with negligible overhead while preserving accuracy across all LongBench tasks.

Method excerpt:

The method keeps the top-scoring chunks under a fixed step budget B. Algorithm 1 evicts chunks until `len(heap) <= B`.

Experiment excerpt:

Table 2 reports retained token ratios of 30%, 40%, and 50%. The baseline is FullCache with no compression. The paper says all methods use the same token budget.

Artifact README excerpt:

The quickstart runs `python demo.py --toy`. Full benchmark scripts will be released after acceptance. This repository fully reproduces Table 2.

## Expected High-Quality Behavior

- Identify budget mismatch: step/chunk budget versus token budget.
- Flag "negligible overhead" as unsupported without timing protocol.
- Flag "across all LongBench tasks" as broad unless task list/results are provided.
- Flag artifact README contradiction: toy demo and future scripts versus "fully reproduces Table 2".
- Avoid claiming fraud or impossible results.
