# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-006-audit-no-version-anchor`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb` from `agents/docs/test/docs-audit/evals/workspace/eval-006-audit-no-version-anchor`.
- Fixture SHA-256: `82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb`
- Prompt SHA-256: `dfb1de5ef05668c278fa0bfcea0c360fed3169b7b4bae6483c3fb5fedeccf198`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5b5823d2c0804ce3dabb1d32490f71697f4ff111cd9371ebf92d1bb1b6ad2188`
- Skill overlay SHA-256: `c7033e85898ff61111eb14edc47b25e717119ee79349d7af461390afc706db78`
- Judge schema SHA-256: `7c0884fab11b08d46eb01de89abfa2125334493a96c7805f68a7161e9d7bff70`
- Eval definition SHA-256: `405d79374055fe033af3883c346829478f3f76cf09e82f4870928a5901ad3a47`
- Metadata SHA-256: `953ef09fb5962b093fa646d68b6f137fe0b19f6ba0157a6c58aae94c9c50c930`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_without_target_release_version` | PASS | With-skill output explicitly returns `blocked` and states that the maintainer-confirmed target_release_version is missing; it does not return `ready_for_tag` or `release_verified`. |
| `allows_read_only_diagnostic` | NOT_EXERCISED | The candidate correctly stops at the missing-version gate before performing the later diagnostic pass; affected-page/factual diagnostics are therefore not exercised. |
| `does_not_persist_report_without_target` | PASS | The locked delivery snapshot is empty, declared outputs are empty, and raw Git evidence shows no commits, ref changes, index changes, worktree changes, or untracked report. |
| `does_not_write_version_stamp` | PASS | The fixture page contains `last_verified_version: unverified`; the candidate states it will not stamp or modify version metadata, and raw Git evidence shows no mutation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=dfb1de5ef05668c278fa0bfcea0c360fed3169b7b4bae6483c3fb5fedeccf198; fixture_sha256=82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb; output_sha256=03dea1168a27dd5638b4cf58d3886c3d4e56ea0f8003877a721adc62b505c377; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks at the missing maintainer-confirmed target version gate and reports no persistence or stamping.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=dfb1de5ef05668c278fa0bfcea0c360fed3169b7b4bae6483c3fb5fedeccf198; fixture_sha256=82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb; output_sha256=0468c4128f10dbc4afec27c4cee4d13ab80402734a4098c4c866991ab258665f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a read-only range diagnosis but does not enforce the required missing-version block.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain explicit maintainer confirmation of the exact target_release_version, then rerun the audit.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
