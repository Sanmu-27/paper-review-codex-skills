# Paper Data Audit Prompt

Audit this paper's numbers, tables, reported metrics, configs, plots, system measurements, and reproducibility evidence.

Build a claim ledger for headline results, budgets, training details, ablations, deltas, latency, memory, and artifact claims. Check:

- table arithmetic and deltas
- repeated numbers across abstract/text/tables/appendix
- metric units and aggregation
- seed/std/split reporting
- config and hyperparameter consistency
- budget matching across methods
- hardware and memory plausibility
- artifact support for the reported numbers
- external plausibility against primary benchmark/model sources when needed

Output verdict, evidence inspected, claim ledger summary, P0/P1/P2 findings, external calibration, reproducibility boundary, and fix list.
