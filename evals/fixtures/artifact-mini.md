# Fixture: Artifact Audit Mini

## User Prompt

Use artifact release audit mode. Check whether this synthetic artifact is ready for anonymous submission.

## Materials

Files:

- `README.md`: "One command fully reproduces all paper tables."
- `demo.py`: runs a toy example only.
- `configs/table2.yaml`: references `C:\Users\alice\paper\data`.
- `results/table2.csv`: contains numbers but no generation script.
- `paper_source.zip`: includes `__pycache__/helper.cpython-311.pyc` and `old_icml_version.pdf`.
- `.env`: contains `WANDB_API_KEY=...`.

## Expected High-Quality Behavior

- Flag `.env` as P0 secret leak.
- Flag local absolute path as P0/P1 depending framing.
- Flag anonymous/stale file risks.
- Distinguish result CSV from reproducible generation.
- Suggest safer README scope wording.
