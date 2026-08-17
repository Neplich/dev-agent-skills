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
- target_skill_sha256: `314b02febc2ef94201a8e1bf1080c874c355a0e47e6ac9a01b931425f08bfbd7`
- eval_definition_sha256: `ba23dfdb0f9a8ca4993196db1cc72ad98dc4f1e2f6b1b9055f218642fc040702`
- metadata_sha256: `b892d7f11434df5d87e026ef6208862e030c7c37761a266263d03ebecbf3949f`
- fixture_sha256: `888ec3cd17fb382d54d3506afed12dac820d7455abc356bb02ec550713d0ad9f`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `0669292f176355ed06a0f6f5bb030af6a23cb5add4a747bfc08b3a96f60fa065`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `b1f3e3ab8206fcdb669e596904dfb22d806d7f56cf42f82f0bf3acedbbed78d7`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84e19c3e634cfde176d2ff20ba8e9d25a4838db3ed1deb5def94a8d0f1d2ddd9`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_failing_tests` | PASS | With-skill output identifies `test_compact_summary_handles_empty_values` as FAILED and states the Design Delivery Closeout Gate blocked before any write. |
| `design_zero_change` | PASS | Locked with-skill git evidence shows empty status, index diff, worktree diff, and no commits; output reports no design-page or change-map write and affected_docs as none. |
| `names_missing_evidence` | PASS | Output names the failed test, assigns remediation to Engineer, and requires fixing the compact filtering, rerunning all three required tests to all-pass, then re-entering the design gate. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b1f3e3ab8206fcdb669e596904dfb22d806d7f56cf42f82f0bf3acedbbed78d7; fixture_sha256=888ec3cd17fb382d54d3506afed12dac820d7455abc356bb02ec550713d0ad9f; output_sha256=566b923fe26e8821204495c7daf87426f26f36e4ad727437a55a3a655b7406e2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocked the sync after the required compact-rendering test failed; no files were changed.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b1f3e3ab8206fcdb669e596904dfb22d806d7f56cf42f82f0bf3acedbbed78d7; fixture_sha256=888ec3cd17fb382d54d3506afed12dac820d7455abc356bb02ec550713d0ad9f; output_sha256=19b6d3d8403c34f7d343bb0f0cba8fa2762eaa5cef414f8f331a1d008faeb850; snapshot_sha256=7aace380d691b4dce49c5726aea0d07ffe460b8f518d144912a77ec61ac834bf
- Behavior: Reported the failing test but proceeded with design and change-map modifications.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
