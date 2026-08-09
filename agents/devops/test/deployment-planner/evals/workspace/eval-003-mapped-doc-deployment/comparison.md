# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-003-mapped-doc-deployment`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471` from `agents/devops/test/deployment-planner/evals/workspace/eval-003-mapped-doc-deployment`.
- Fixture SHA-256: `beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471`
- Prompt SHA-256: `40b086c239ff14f46936633adeb5d9079306a48046e93c803af236ab43d646d6`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `762ea3248d76c5c9e715368b11ab616562bb9bdb0e2bd6a6aad38d47cc80b3af`
- Skill overlay SHA-256: `52ed13d453014671ce8cc7f7f7ce4b4108c3a5cc943fcf3bece1ac66b08625d5`
- Judge schema SHA-256: `3fd213f6de3f610cad1c014e643471913a0678af0ef96531f1f973bd669f4005`
- Eval definition SHA-256: `3a6f0e2dac2acec4b2146c1f3b14a82dc89e2d78da9249fb55fda45906586c82`
- Metadata SHA-256: `d4f866ac92cff8803e8f120ce38631fed1d054cce30a482192275834ed6880bf`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | Locked outputs state that the mapped document is docs/site/api/runtime-server.md, but no raw execution/read-order evidence proves it was read first. |
| `verifies_against_code` | PASS | The with_skill output identifies server.conf as listen_port = 8081, contrasts it with the documented 8080, and gives EXPOSE and docker port-mapping guidance using 8081. |
| `treats_unverified_as_low_trust` | PASS | The with_skill output explicitly identifies last_verified_version: unverified as low trust and relies on the code configuration for the deployment port. |
| `omits_unselected_targets` | PASS | The with_skill output provides only container deployment guidance and states that no deploy/ files were generated. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=40b086c239ff14f46936633adeb5d9079306a48046e93c803af236ab43d646d6; fixture_sha256=beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471; output_sha256=10b0854c280e55b93fb1cd131b10706d9bf79aeb7457f28a22025ca6832e9147; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly recommends exposing and mapping container port 8081, explains the 8080 documentation mismatch, treats the unverified document as low trust, and does not generate unselected deployment assets.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=40b086c239ff14f46936633adeb5d9079306a48046e93c803af236ab43d646d6; fixture_sha256=beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471; output_sha256=aeafb4a6d08011fd88260c3dcbae0d7dd17fbd9161deeefb32a45346e641d718; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Also identifies 8081 and provides container guidance, but does not explicitly treat the unverified documentation as low trust or state the deployment-target omission gate.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
