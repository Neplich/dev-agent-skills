# Designer Test Helpers

Run a regression eval with:

```bash
uv run agents/designer/test/run_eval.py \
  agents/designer/test/ui-ux-design/workspace/eval-4-pm-spec-handoff/eval_metadata.json
```

The helper writes runtime-only diagnostics under `tmp/eval-runs/designer/` and
fails with a non-zero exit code when required outputs are missing or any
machine-checkable assertion fails. Keep the durable latest result in
`comparison.md`; do not commit generated diagnostics.

Run all designer evals that define `eval_metadata.json` with:

```bash
uv run agents/designer/test/run_all_evals.py
```
