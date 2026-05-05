# External Calibration Guide

Use external sources to check whether the paper's numbers are plausible, not to demand exact equality across different settings.

## Source Priority

1. Official benchmark papers, benchmark websites, and task documentation.
2. Original method papers for baselines and ablations.
3. Official model reports or model cards for model size, context, precision, and memory assumptions.
4. Artifact repositories linked from papers.
5. Survey papers only for orientation, not as numeric authority.

Avoid relying on leaderboard screenshots, blog summaries, or uncited social posts unless the user explicitly asks for zeitgeist context.

## Search Plan

For every central benchmark or baseline:

- Search the exact benchmark name plus "paper", "dataset", "evaluation protocol".
- Search the baseline method name plus "KV cache", "latency", "memory", or metric.
- Search the model name plus "parameters", "context length", "KV cache", "GQA", "num key value heads".

Record:

- source title
- year/version
- metric and setting
- whether it is apples-to-apples, close, or only directional
- any mismatch such as model size, data split, budget, decoding, prompt format

## Comparison Templates

Benchmark metric:

```text
Paper claims X on benchmark B with model M and protocol P.
External source reports Y under protocol P' with model M'.
Comparison quality: apples-to-apples / close / directional.
Plausibility: consistent / high but possible / suspicious / unsupported.
Reason: ...
```

Systems metric:

```text
Paper claims latency or memory X under batch B, context L, precision P, model M.
Check model weights, KV-cache size, activation/workspace assumptions, and hardware memory.
If exact inference engine hooks are missing, mark it as prototype evidence.
```

## Common Red Flags

- A baseline is far below known values without an explained protocol difference.
- A result uses a much larger model but compares to smaller-model baselines.
- A memory number ignores batch size, layers, heads, precision, or GQA/MQA.
- A latency table is reported as end-to-end but the artifact benchmark measures only a CPU or scorer microbenchmark.
- A transfer result is presented as if it were trained/evaluated in-domain.
- A public benchmark split or task count does not match official docs.

## Citation Discipline

When using web search, include links in the final response. Quote sparingly. Prefer paraphrase plus exact numeric references.
