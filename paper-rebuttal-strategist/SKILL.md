---
name: paper-rebuttal-strategist
description: Plan rigorous author responses for ML, AI, and systems paper reviews. Use when the user provides reviewer comments, meta-review notes, scores, rebuttal constraints, OpenReview discussions, or asks for rebuttal strategy, response drafting, reviewer triage, score rescue, weakness prioritization, or camera-ready response positioning for NeurIPS/ICML/ICLR-style submissions.
---

# Paper Rebuttal Strategist

## Purpose

Use this skill to turn reviews into a disciplined rebuttal plan. The goal is not to argue every point, but to identify which reviewer beliefs decide the outcome, what evidence can change those beliefs, and how to write concise, credible responses under strict space and time limits.

## Workflow

### 1. Inventory The Review Packet

Collect:

- reviewer scores, confidence, recommendation text, and private/public comment boundaries
- official rebuttal instructions, word limits, deadline, and allowed new experiments
- paper, appendix, artifact, and any already-run follow-up experiments
- reviewer identities only if openly available and relevant; otherwise ignore speculation

If venue rules are current-year or unclear, verify the official instructions before giving procedural advice.

### 2. Build A Reviewer Belief Map

For each reviewer, identify:

- decision stance: likely accept, borderline, likely reject
- top decision drivers
- factual misunderstandings versus real weaknesses
- what evidence would plausibly move the score
- points that should be conceded rather than fought

Prioritize reviewers whose score or confidence can realistically move the decision.

### 3. Triage Issues

Use these labels:

- `Must-answer`: directly affects score or meta-review risk.
- `Worth-answering`: improves trust or resolves a recurring concern.
- `Defer`: better handled in revision or camera-ready.
- `Do-not-fight`: arguing would sound defensive or reveal a larger weakness.

Prefer one strong answer to a central concern over many shallow replies.

### 4. Evidence Plan

For each must-answer issue:

- identify the minimum evidence needed
- choose whether evidence should be a citation, clarification, table, ablation, error analysis, theorem fix, or artifact note
- state what can be finished before rebuttal deadline
- mark risks if new experiments are incomplete or negative

Never invent completed experiments. If evidence is planned but not finished, phrase it as a limitation or future revision only when venue rules allow.

### 5. Draft The Response

Use a respectful, compressed style:

- start with gratitude only once, not in every paragraph
- answer the central concern first
- acknowledge valid weaknesses plainly
- correct misunderstandings with exact paper anchors
- avoid blaming reviewer reading effort
- do not overclaim that a clarification fully resolves a missing experiment

When space is tight, write in issue blocks rather than reviewer-by-reviewer blocks unless the venue asks otherwise.

## Output Format

Default output:

1. decision diagnosis
2. reviewer-by-reviewer belief map
3. issue triage table
4. evidence/action plan
5. rebuttal outline
6. polished rebuttal draft
7. risks and what not to say

For short requests, provide only the issue triage and draft response.

## Reference Files

Read `references/rebuttal-playbook.md` when the user wants a full response strategy or a final draft.
