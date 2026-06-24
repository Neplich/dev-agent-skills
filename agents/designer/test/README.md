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

Metadata with no deterministic outputs or machine-checkable assertions is not a
deterministic runner eval. The helper writes a skip report for a direct run, and
`run_all_evals.py` excludes it from the deterministic batch. Fresh subagent
validation is still the semantic evaluation path, and the durable committed
result remains `comparison.md`.

After any actual eval run or fresh Codex subagent validation, update the
workspace's durable `comparison.md` in the same change. PR comments and
conversation summaries must match the committed or proposed `comparison.md`; if
there is no comparison file to update, record the blocked or not-applicable
reason.

Fresh Sub-Agent gate: every fresh Codex subagent validation must generate a new
`without_skill` baseline against the same eval prompt and fixture. Do not reuse
historical baseline text as the current run. The `without_skill` run is baseline
input for `comparison.md`; if it cannot be generated or reviewed, record its
impact in the comparison conclusion instead of treating baseline text as a
separate machine-graded result.

Run all designer evals that define `eval_metadata.json` with:

```bash
uv run agents/designer/test/run_all_evals.py
```
