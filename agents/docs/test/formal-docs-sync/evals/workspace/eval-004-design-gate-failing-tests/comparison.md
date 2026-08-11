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
- Repository HEAD: `f2aa9b2c49be68550ec45538c221425607f428ce`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `dd975083d3977d90b71b3396dff2498ef2b7e8d49c50fab50b5462a26f3248ee`
- Skill overlay SHA-256: `9667198915198da0404e03a7d4c962d38742b19c5de4de5f0cf1473f02db2bf1`
- Judge schema SHA-256: `0669292f176355ed06a0f6f5bb030af6a23cb5add4a747bfc08b3a96f60fa065`
- Eval definition SHA-256: `ba23dfdb0f9a8ca4993196db1cc72ad98dc4f1e2f6b1b9055f218642fc040702`
- Metadata SHA-256: `b892d7f11434df5d87e026ef6208862e030c7c37761a266263d03ebecbf3949f`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_failing_tests` | PASS | With-skill output identifies `test_compact_summary_handles_empty_values` as FAILED, marks gate item 6 failed, and states it stopped before Step 4 confirmation and writes. |
| `design_zero_change` | PASS | With-skill output reports the design page and change-map entry were not modified; locked git evidence shows an unchanged HEAD and empty worktree status. |
| `names_missing_evidence` | PASS | With-skill output names the failed test, assigns responsibility to Engineer, and requires fixing implementation or test, rerunning all three required tests to all-pass, then re-entering the closeout gate. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b1f3e3ab8206fcdb669e596904dfb22d806d7f56cf42f82f0bf3acedbbed78d7; fixture_sha256=888ec3cd17fb382d54d3506afed12dac820d7455abc356bb02ec550713d0ad9f; output_sha256=4a95cf32dd54e273c213245e0e81d582f48f73bcbe8c2c039d69dd9f8e2bd30a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocked the design sync on the failed required test, preserved zero changes, and provided the owner and complete unlock path.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b1f3e3ab8206fcdb669e596904dfb22d806d7f56cf42f82f0bf3acedbbed78d7; fixture_sha256=888ec3cd17fb382d54d3506afed12dac820d7455abc356bb02ec550713d0ad9f; output_sha256=ee7371ae39a27cefe3254e5ef631691570686194334b418cea838d27ff42b467; snapshot_sha256=06bc00b72122dad78f284216c2cb664929078af2395d3212f44ee57ddaa95448
- Behavior: Fresh baseline incorrectly proceeded with design and change-map modifications despite the failed required test.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
