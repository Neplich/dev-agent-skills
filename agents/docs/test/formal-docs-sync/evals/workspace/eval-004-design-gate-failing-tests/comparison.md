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
- Identity schema: `2`
- target_skill_sha256: `a3e1263ac8acb74f106913f935cefb0ebe0f7f059ccc011cd16715592fd0163d`
- eval_definition_sha256: `ba23dfdb0f9a8ca4993196db1cc72ad98dc4f1e2f6b1b9055f218642fc040702`
- metadata_sha256: `b892d7f11434df5d87e026ef6208862e030c7c37761a266263d03ebecbf3949f`
- fixture_sha256: `888ec3cd17fb382d54d3506afed12dac820d7455abc356bb02ec550713d0ad9f`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `0669292f176355ed06a0f6f5bb030af6a23cb5add4a747bfc08b3a96f60fa065`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `b1f3e3ab8206fcdb669e596904dfb22d806d7f56cf42f82f0bf3acedbbed78d7`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `b6ae3621879be63fa5b02212924eed11dd010ad027f0308f85d7666d26a57421`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_failing_tests` | PASS | With_skill identifies `test_compact_summary_handles_empty_values` as FAILED, marks required test gate 6 BLOCKED, and states no document or change-map write occurred; the matrix records scope confirmation was not reached. |
| `design_zero_change` | PASS | With_skill reports zero writes, and locked git evidence shows unchanged HEAD/branch, empty status, empty index/worktree diffs, and no untracked files. |
| `names_missing_evidence` | PASS | With_skill names the failed test, assigns responsibility to Engineer, and specifies fixing the implementation followed by rerunning all three required tests before re-entering closeout; it explicitly rejects rerunning only the failed test. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b1f3e3ab8206fcdb669e596904dfb22d806d7f56cf42f82f0bf3acedbbed78d7; fixture_sha256=888ec3cd17fb382d54d3506afed12dac820d7455abc356bb02ec550713d0ad9f; output_sha256=c034ae292e711011ab28d05afba709a5208d78f91892fca9c212493866c3c6f2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocked the design synchronization on the failed required test and preserved zero-change delivery state.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b1f3e3ab8206fcdb669e596904dfb22d806d7f56cf42f82f0bf3acedbbed78d7; fixture_sha256=888ec3cd17fb382d54d3506afed12dac820d7455abc356bb02ec550713d0ad9f; output_sha256=05d4cde42e1f49797bae0025abfec849aa55fb54e2b14ccf86e05ea372f65345; snapshot_sha256=1dca550beaa5bf960b90fe98d001a18003f83ba18f0b8594903542a708510d8c
- Behavior: Incorrectly modified the design document and change map despite the failed required test.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
