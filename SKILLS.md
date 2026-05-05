# Skill Index

This repository supports two usage layers:

- Codex-native skill folders, each with `SKILL.md` and optional resources.
- Cross-agent adapters in `adapters/` and reusable prompts in `prompts/`.

## `ai-paper-review`

Best for broad, adversarial paper review. It includes a deep workflow, a review checklist, output templates, reusable prompts, and a LaTeX submission scanner.

## `paper-data-auditor`

Best for checking whether reported numbers and empirical claims are credible. It includes external calibration guidance, an expert severity rubric, and a numeric/artifact scanner.

## `paper-rebuttal-strategist`

Best after reviews arrive. It maps reviewer beliefs, triages issues, plans evidence, and drafts concise responses.

## `artifact-release-auditor`

Best before uploading code, supplements, or artifact-evaluation packages. It checks runnable boundaries, anonymity, security, licensing, README wording, and paper-artifact alignment.

## `camera-ready-polisher`

Best for final papers. It checks promised changes, claim scope, checklist consistency, captions, bibliography hygiene, and source-package upload risks.

## Cross-Agent Materials

- `adapters/universal-agent-instructions.md`: portable system prompt for any capable agent.
- `adapters/chatgpt-instructions.md`: ChatGPT project/custom GPT instructions.
- `adapters/claude-project-instructions.md`: Claude project instructions.
- `adapters/coding-agent-rules.md`: repo-based coding-agent rules.
- `prompts/`: task-specific prompts that work across agents.
- `evals/`: mini fixtures and rubric for judging answer quality.
