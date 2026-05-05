# Coding-Agent Rules

Use this file as project rules for coding agents such as Cursor, Windsurf, Aider-style agents, or repo-based assistants.

## Research Artifact Review Rules

- Inspect repository files directly before making claims about reproducibility.
- Prefer `rg` for searching when available.
- Trace paper tables and claims to scripts, configs, logs, checkpoints, or README statements.
- Do not run heavy training unless explicitly requested. Prefer smoke tests, help flags, config checks, and static scans first.
- Never delete user artifacts or rewrite results while auditing.
- Treat generated scanner output as leads, not final truth.
- Flag secrets, identity leaks, stale files, local absolute paths, and cache files.
- When editing README or docs, distinguish smoke tests, benchmark drivers, and full reproduction.

## Useful Commands

```bash
python ai-paper-review/scripts/audit_tex_submission.py path/to/main.tex
python paper-data-auditor/scripts/audit_numbers.py path/to/paper-or-artifact
python scripts/validate_skills.py
```

## Output Contract

For repository audits, report:

- artifact verdict
- files inspected
- runnable boundary
- paper-to-artifact traceability
- P0/P1/P2 findings
- exact commands attempted and results
- minimal fix list
