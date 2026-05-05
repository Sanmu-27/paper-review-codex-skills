# Evals

This directory contains lightweight evaluation fixtures for judging whether an agent follows the workflows in this repository.

The goal is not to benchmark model intelligence. The goal is to check whether the skill pack causes useful behavior:

- concrete evidence anchors
- severity and confidence labels
- no fabricated experiments or citations
- clear distinction between missing evidence and verified flaws
- actionable fixes

## How To Run Manually

1. Pick a fixture from `fixtures/`.
2. Give an agent the relevant adapter from `adapters/`.
3. Give it the fixture prompt and materials.
4. Score the answer with `rubric.md`.

## Passing Standard

A strong answer should score at least 16/20 overall and should not fail any critical safety criterion in the rubric.
