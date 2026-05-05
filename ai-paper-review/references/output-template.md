# Output Templates

## 1. Formal Conference Review

Use this shape:

```md
Summary:
- 2-4 sentences on the paper's actual contribution and scope.

Strengths:
- ...
- ...

Weaknesses:
- ...
- ...

Questions for Authors:
- ...

Suggested Score:
- Overall: ...
- Confidence: ...

Why:
- 2-4 reasons that most affect the verdict.
```

## 2. Source-Audit / Revision Mode

Use this shape:

```md
Hard blockers:
1. ...
2. ...

Major issues:
1. ...
2. ...

Moderate / polish:
1. ...
2. ...

Suggested edits:
- In Section X, rewrite ...
- In Algorithm 1, change ...
- In Table Y, clarify ...
```

## 3. High-Signal Finding Format

When calling out a specific issue, prefer:

```md
Issue:
- what is inconsistent

Why it matters:
- why a reviewer would care

Fix:
- the smallest credible correction
```

## 4. Deep Workflow Ledgers

For serious audits, maintain these ledgers internally and surface them when useful.

Claim ledger:

```md
| Claim | Evidence | Risk | Reviewer attack |
|---|---|---|---|
| ... | Section/Table/Figure | Low/Med/High | ... |
```

Issue ledger:

```md
| Severity | Location | Issue | Why it matters | Fix |
|---|---|---|---|---|
| Hard blocker | Eq./Alg./Table | ... | ... | ... |
```

Fix ledger:

```md
| Priority | Edit | Files/sections | Expected impact |
|---|---|---|---|
| P0 | ... | ... | ... |
```

## 5. Better-Than-PAT Audit Output

Use this when the user asks for a very strong AI review:

```md
Artifact audit:
- inspected:
- missing:
- version drift:

Venue calibration:
- venue/year:
- contribution type:
- likely reviewer bar:

Central claims:
- claim:
  support:
  verdict:

Top hard blockers:
1. ...
2. ...

Major reviewer concerns:
1. ...
2. ...

Section-by-section findings:
- Introduction:
- Method:
- Experiments:
- Figures/Tables:
- Theory/Appendix:
- Systems:
- Checklist/References:

Likely reviewer score:
- score:
- confidence:
- score drivers:

Top reviewer attacks:
- ...
- ...
- ...

Revision plan:
- P0:
- P1:
- P2:
```

## 5.5 Default Full-Length Review

Use this by default for generic "review this paper", "审稿", "按 NeurIPS 水平看",
"完整评测", or submission-readiness requests unless the user explicitly asks
for a quick / concise review.

```md
Artifact audit:
- inspected:
- missing:
- authoritative version:
- version drift risks:

Venue calibration:
- venue/year:
- contribution type:
- likely acceptance bar:

Overall summary:
- 1 short paragraph on what the paper claims and what actually carries the verdict.

Central claims support matrix:
| Claim | Main evidence | Support status | Main risk | Reviewer attack |
|---|---|---|---|---|
| ... | ... | Convincing / Partial / Weak | ... | ... |

Strengths:
- ...
- ...

Top hard blockers:
1. ...
2. ...

Major concerns:
1. ...
2. ...
3. ...

Section-by-section findings:
- Title/Abstract:
- Introduction/Positioning:
- Related Work:
- Method:
- Theory/Math:
- Experiments:
- Figures/Tables:
- Systems/Artifact:
- Limitations/Checklist/References:

Reproducibility and artifact audit:
- what is actually reproducible from the package
- what is missing for faithful reproduction
- where the paper overstates or correctly scopes reproducibility

Questions for authors:
- ...
- ...

Likely reviewer score:
- overall:
- confidence:
- score drivers:

Top reviewer attacks:
- attack:
  type:
  why it lands:
  rebuttal survivability:

Revision plan:
- P0:
- P1:
- P2:
```

Rule of thumb:
- The default review should feel like a real reviewer report plus an internal
  author memo.
- If the review could plausibly fit into a very short chat reply, it is
  probably too compressed.

## 6. Good Reviewer Tone

Use:
- precise
- skeptical but fair
- concrete
- action-oriented

Avoid:
- empty praise
- vague negativity
- pretending uncertainty where the source already settles the point
