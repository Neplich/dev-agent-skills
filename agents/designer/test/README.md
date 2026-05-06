# Designer Test Helpers

Run a regression eval with:

```bash
uv run agents/designer/test/run_eval.py \
  agents/designer/test/ui-ux-design/workspace/eval-4-pm-spec-handoff/eval_metadata.json
```

The helper may write `comparison.auto.md` as a runtime-only temporary report and
fails with a non-zero exit code when required outputs are missing or any
machine-checkable assertion fails. Keep the durable latest result in
`comparison.md`; do not commit `comparison.auto.md`.

Run all designer evals that define `eval_metadata.json` with:

```bash
uv run agents/designer/test/run_all_evals.py
```
