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

For metadata with `validation_method: "fresh_codex_subagent"`, this helper only
writes a skip report because Codex or Claude Code subagent validation is an
external evaluation path. `subagent-verdict.md` is a runtime-only diagnostic
artifact from that path, not a required fixture output and not a committed
artifact. The durable committed result remains `comparison.md`.

After any actual eval run or fresh Codex subagent validation, update the
workspace's durable `comparison.md` in the same change. PR comments and
conversation summaries must match the committed or proposed `comparison.md`; if
there is no comparison file to update, record the blocked or not-applicable
reason.

Run all designer evals that define `eval_metadata.json` with:

```bash
uv run agents/designer/test/run_all_evals.py
```
