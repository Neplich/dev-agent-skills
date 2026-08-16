# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-012-implementation-plan-archive-preflight`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e` from `agents/engineer/test/feature-implementor/evals/workspace/eval-012-implementation-plan-archive-preflight`.
- Identity schema: `2`
- target_skill_sha256: `248d30c2e10162217ecb1d6a0d7c66973ee945c6f2e9b7e4bf01a677aac7bc3c`
- eval_definition_sha256: `7f61bff44513e544647aa068492b4fc39b7ba0f0b8a502c36472dbc74575e45e`
- metadata_sha256: `d61de6289d375a4f846be423a72cc4b82b03d964cc2e5dac6f44d3f3c1fe9492`
- fixture_sha256: `681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `097d311377d0abb4f2fcb1bfa46de1df83e6feccaa7b6f38bb1fb185a5118ab5`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `9c7650cd9313e12223d2a68ebc3c37905ca839128cbb6b36d20fc7541af57b74`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `8002de5f5ec8cbba9c876b3fa5b95d04da373914039535f254ff8fce02f9cbab`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `runs_pre_plan_archive_scan` | PASS | runner_captured_trace shows the active plan was read and the archive directory was explicitly scanned before the checkpoint; the checkpoint records both paths and archive state. |
| `blocks_direct_overwrite` | PASS | The with_skill output explicitly blocks overwriting/replacing the active plan and creating a new plan, with no delivered file changes. |
| `offers_implemented_handling_options` | PASS | The output requests a choice between archiving then creating a new plan, or archiving as Superseded with a reason then creating one; it offers no Implemented-status update option. |
| `keeps_active_entry_fixed` | PASS | The output states the active entry remains docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md and archives belong only under archive/. |
| `does_not_implement_directly` | PASS | The output describes a blocked planning checkpoint and pending actions, without claiming code changes, implementation, or verification. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c7650cd9313e12223d2a68ebc3c37905ca839128cbb6b36d20fc7541af57b74; fixture_sha256=681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e; output_sha256=263a9d0a2efd3600356ba260fd08b228ea2d9567e4a15a2a36725358ca6c54ce; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Performed the required pre-plan scan, preserved the active plan, presented the two required archive choices, and stopped pending confirmation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c7650cd9313e12223d2a68ebc3c37905ca839128cbb6b36d20fc7541af57b74; fixture_sha256=681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e; output_sha256=074906397966e9b87d018ae9f657e2f030c7ce2967c0be3dc37dd5efb3547a11; snapshot_sha256=f749552a23359edd6c8d244fd709b2924cdf85c8ac22aa6a34752466adbd9ae9
- Behavior: Directly overwrote the active plan, created an archive and replacement plan, and claimed completion and verification.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: User must select one of the two archive-handling options before any plan or implementation changes proceed.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
