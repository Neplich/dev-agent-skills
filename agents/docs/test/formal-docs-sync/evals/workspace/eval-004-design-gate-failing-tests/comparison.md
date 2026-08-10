# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-004-design-gate-failing-tests`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `888ec3cd17fb382d54d3506afed12dac820d7455abc356bb02ec550713d0ad9f` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-004-design-gate-failing-tests`.
- Fixture SHA-256: `888ec3cd17fb382d54d3506afed12dac820d7455abc356bb02ec550713d0ad9f`
- Prompt SHA-256: `b1f3e3ab8206fcdb669e596904dfb22d806d7f56cf42f82f0bf3acedbbed78d7`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f24bfeb12dba77a74fcf3f0161749ae4671b83762eac08484e7ae08621d9bacb`
- Skill overlay SHA-256: `5dbb8d8559bfab3926047aa028e19f362490751247c2142101cfd687fff5239e`
- Judge schema SHA-256: `0669292f176355ed06a0f6f5bb030af6a23cb5add4a747bfc08b3a96f60fa065`
- Eval definition SHA-256: `ba23dfdb0f9a8ca4993196db1cc72ad98dc4f1e2f6b1b9055f218642fc040702`
- Metadata SHA-256: `b892d7f11434df5d87e026ef6208862e030c7c37761a266263d03ebecbf3949f`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_failing_tests` | PASS | With_skill identifies `test_compact_summary_handles_empty_values` as `FAILED` and states the gate is blocked before scope confirmation and writing. |
| `design_zero_change` | PASS | With_skill locked git evidence shows unchanged HEAD, empty worktree/index status, and no file snapshot or diff; its final report states both design targets were not modified. |
| `names_missing_evidence` | FAIL | With_skill names the failed test and Engineer as the person to fix it, but does not explicitly require rerunning all plan-required tests to obtain an all-pass record before re-entering the design closeout gate. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b1f3e3ab8206fcdb669e596904dfb22d806d7f56cf42f82f0bf3acedbbed78d7; fixture_sha256=888ec3cd17fb382d54d3506afed12dac820d7455abc356bb02ec550713d0ad9f; output_sha256=b0b59b515af9d7d65f18c27e831b639e97132d460e0b8b5a50e19683392eb582; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocked the design sync and preserved zero changes, but incompletely specified the evidence required to unlock the gate.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b1f3e3ab8206fcdb669e596904dfb22d806d7f56cf42f82f0bf3acedbbed78d7; fixture_sha256=888ec3cd17fb382d54d3506afed12dac820d7455abc356bb02ec550713d0ad9f; output_sha256=f1fb88e6e689681163c825068d4ce1547731ac2d53f7758275d290632a84230d; snapshot_sha256=08932d269df6c3c92dbe1d590184d8bc3503974b519171208868ab4d70ea0272
- Behavior: Updated the design page despite the failed required test, creating a design-only worktree change.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane omits the required complete unlock path: rerun all plan-required tests, obtain a fully passing record, then re-enter the design closeout gate.
- Next: State that Engineer/test owner must fix the implementation or test, rerun all plan-required tests, obtain an all-pass record, and then re-enter the design closeout gate.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
