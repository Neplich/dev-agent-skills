# Security Skill Evals

Security eval definitions live under `agents/security/test/<skill>/evals/`.
Every eval has a workspace, and the durable result for that workspace is
`comparison.md`.

Runtime transcripts, verdicts, timing data, generated outputs, and diagnostics
belong in an isolated scratch location such as `tmp/eval-runs/...`; do not
commit them.

After any actual skill eval run or fresh Codex subagent validation, update the
workspace's durable `comparison.md` in the same change. PR comments and
conversation summaries must match the committed or proposed `comparison.md`; if
there is no comparison file to update, record the blocked or not-applicable
reason.

Fresh Codex subagent validation should run both `with_skill` and `without_skill`
against the same eval prompt and fixture. The `without_skill` run is baseline
input for `comparison.md`; if it cannot be generated or reviewed, record its
impact in the comparison conclusion instead of treating baseline text as a
separate machine-graded result.
