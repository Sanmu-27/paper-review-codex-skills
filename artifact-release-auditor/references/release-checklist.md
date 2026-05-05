# Artifact Release Checklist

## Minimum Reviewer-Ready Package

- README states what is included and what is not included.
- One quickstart command exercises the method on a tiny input.
- Environment instructions include Python version, CUDA notes if relevant, and install commands.
- Evaluation scripts document expected inputs and outputs.
- Configs are named consistently with paper experiments.
- Checkpoints or download instructions include size and expected location.
- Tables or figures have traceable scripts or explicit notes explaining why not.

## Anonymous Submission Checks

- No author names in paths, metadata, notebook outputs, git remotes, logs, PDFs, or comments.
- No institutional cluster paths.
- No API keys, tokens, `.env`, wandb credentials, or cloud bucket credentials.
- License is included only if venue anonymity policy permits it.

## Public Release Checks

- License is explicit.
- Citation file or BibTeX is present.
- Model/data licenses are not contradicted by redistribution.
- README distinguishes pretrained weights, derived data, and external downloads.
- Release tag or commit hash is recorded for the paper.

## Safe README Wording

Use precise scope wording:

- "This repository provides the implementation and scripts used for the main experiments."
- "The quickstart runs a small sanity check, not the full benchmark."
- "Full reproduction of Table 2 requires downloading the listed datasets and checkpoints."
- "We include plotting scripts and result logs for the reported tables."

Avoid:

- "Fully reproducible" unless every central result can be regenerated.
- "One-command reproduction" if downloads, credentials, or manual setup are required.
- "Production-ready" for research prototypes.
