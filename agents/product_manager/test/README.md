# Product Manager Skill Evals

Product manager eval definitions live under
`agents/product_manager/test/<skill>/evals/`. When an eval has a workspace, the
durable result for that workspace is `comparison.md`.

Runtime transcripts, generated reports, status files, timing data, and
diagnostics belong in an isolated scratch location such as
`tmp/eval-runs/product_manager/...`; do not commit them.

After any actual skill eval run or fresh Codex subagent validation, update the
workspace's durable `comparison.md` in the same change. PR comments and
conversation summaries must match the committed or proposed `comparison.md`; if
there is no comparison file to update, record the blocked or not-applicable
reason.

Some skills may also have more specific running guides, such as
`idea-to-spec/README.md`; follow the specific guide plus the durable comparison
rule above.
