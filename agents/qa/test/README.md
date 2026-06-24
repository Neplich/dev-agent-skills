# QA Eval Runner

QA evals may use Codex or Claude subagents to execute or judge an E2E-style QA
flow, but `subagent-verdict.md` is only a runtime diagnostic artifact. It is not
the eval's durable result and must not be declared as a metadata output.

When a QA eval has deterministic outputs, metadata should point at the actual QA
or E2E result artifacts, such as a test report, generated test case, execution
summary, or evidence file. When a QA eval has no deterministic output, it should
not be included in the deterministic runner flow; the semantic result belongs in
the durable `comparison.md`.

## Run One Eval

```bash
uv run agents/qa/test/run_eval.py \
  agents/qa/test/qa-agent/evals/workspace/eval-2-empty-qa-directory-expands-cases/eval_metadata.json
```

## Run All QA Evals

```bash
uv run agents/qa/test/run_all_evals.py
```

`run_all_evals.py` only discovers metadata with deterministic QA or E2E output
fields. Metadata without those fields is handled by fresh subagent validation and
durable `comparison.md` updates instead of the deterministic helper runner.

## Outputs

Each eval run writes runtime-only files under `tmp/eval-runs/qa/`, such as:

- `with_skill/outputs/candidate-output.md`
- `without_skill/outputs/candidate-output.md`
- `diagnostics/run.json`
- `comparison.auto.md`

Do not commit these runtime files. The durable latest result for a workspace is
`comparison.md`.

After any actual eval run or fresh Codex subagent validation, update the
workspace's durable `comparison.md` in the same change. PR comments and
conversation summaries must match the committed or proposed `comparison.md`; if
there is no comparison file to update, record the blocked or not-applicable
reason.

Fresh Codex subagent validation must run both `with_skill` and `without_skill`
against the same eval prompt and fixture. The `without_skill` run is the
baseline input for `comparison.md`; if it cannot be generated or reviewed, do
not record a full `PASS`.

Runner failure is based on the deterministic outputs declared in metadata. The
`without_skill` semantic verdict may fail as useful baseline contrast, but its
candidate output and fresh judge verdict must be generated when the runner is
used. Fresh judge verdicts can inform manual review, but the committed durable
result is still `comparison.md`.
