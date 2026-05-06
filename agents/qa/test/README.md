# QA Eval Runner

QA evals use a two-stage protocol:

1. Generate a candidate QA output for `with_skill` and `without_skill`.
2. Ask a fresh Codex judge to read the candidate output, the QA skill document,
   the QA README, the fixture workspace, and `evals.json`, then write
   `subagent-verdict.md`.

This avoids treating transcript or output-file existence as the source of truth.
The semantic pass/fail decision comes from the fresh judge verdict.

## Run One Eval

```bash
uv run agents/qa/test/run_eval.py \
  agents/qa/test/qa-agent/evals/workspace/eval-2-empty-qa-directory-expands-cases/eval_metadata.json
```

## Run All QA Evals

```bash
uv run agents/qa/test/run_all_evals.py
```

## Outputs

Each eval run may create runtime-only files such as:

- `with_skill/outputs/candidate-output.md`
- `with_skill/outputs/subagent-verdict.md`
- `without_skill/outputs/candidate-output.md`
- `without_skill/outputs/subagent-verdict.md`
- `diagnostics/run.json`
- `comparison.auto.md`

Do not commit these runtime files. The durable latest result for a workspace is
`comparison.md`.

Runner failure is based on the `with_skill` path:

- candidate output must exist
- fresh judge verdict must exist
- fresh judge verdict must report `Overall: PASS`

The `without_skill` path is diagnostic. A `FAIL` verdict there is useful
contrast, but a `PASS` verdict is not a runner failure when the prompt or fixture
is enough for a general model to satisfy the assertions.
