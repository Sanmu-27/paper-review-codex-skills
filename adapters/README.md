# Cross-Agent Adapters

This repository is written as Codex skills, but the workflows can be used by any capable agent that supports custom instructions, project rules, or reusable prompts.

## Adapter Matrix

| Agent surface | Recommended file |
| --- | --- |
| Codex skills | Use the individual `*/SKILL.md` folders directly. |
| General system prompt | `adapters/universal-agent-instructions.md` |
| ChatGPT custom GPT / project instructions | `adapters/chatgpt-instructions.md` |
| Claude project instructions | `adapters/claude-project-instructions.md` |
| Cursor / Windsurf / coding-agent rules | `adapters/coding-agent-rules.md` |
| Gemini / other assistants | `adapters/universal-agent-instructions.md` plus the relevant prompt from `prompts/` |

## How To Use

1. Pick the adapter for your agent.
2. Paste it into the agent's custom instructions, project rules, or system prompt.
3. Add the task-specific prompt from `prompts/`.
4. Attach the paper PDF/source/artifact/reviews when available.

The adapters intentionally avoid product-specific APIs. They describe behavior, evidence standards, output shapes, and failure modes that any strong agent can follow.
