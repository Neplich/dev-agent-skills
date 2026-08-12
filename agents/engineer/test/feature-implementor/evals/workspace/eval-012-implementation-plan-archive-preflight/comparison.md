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
- target_skill_sha256: `2cef9a078b25940be2cd93c65c4193da4205d9703e5924079fcda5ac81b0dc82`
- eval_definition_sha256: `7f61bff44513e544647aa068492b4fc39b7ba0f0b8a502c36472dbc74575e45e`
- metadata_sha256: `158f5bafaa3ad4ac6ba561642292db5794c29432044a423049518391aa4f0dbd`
- fixture_sha256: `681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `097d311377d0abb4f2fcb1bfa46de1df83e6feccaa7b6f38bb1fb185a5118ab5`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `7ac19d358ca18ef7b2d109aeec17239bc9d0f4c0`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `runs_pre_plan_archive_scan` | PASS | With-skill trace shows the active plan and archive directory were scanned before the planning gate completed. |
| `blocks_direct_overwrite` | PASS | The with-skill output explicitly says the active plan cannot be overwritten; locked git evidence shows no changes. |
| `offers_implemented_handling_options` | PASS | The output presents both required archive choices and does not offer continuing the Implemented plan. |
| `keeps_active_entry_fixed` | PASS | The output states the active entry remains fixed and archives are restricted to archive/. |
| `does_not_implement_directly` | PASS | The with-skill output and locked evidence show no code changes, implementation, or verification claim. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c7650cd9313e12223d2a68ebc3c37905ca839128cbb6b36d20fc7541af57b74; fixture_sha256=681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e; output_sha256=0aa2d5ac10795899933762bd2019c3c83ae84b8545c803666e63b3cbb8712c7b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Scanned the existing plan and archive state, blocked mutation, and requested an archive decision before proceeding.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c7650cd9313e12223d2a68ebc3c37905ca839128cbb6b36d20fc7541af57b74; fixture_sha256=681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e; output_sha256=ac293871507deb1a87e46aca731a0190180380cc82afa670a56c372e84b65500; snapshot_sha256=28630f936804fb4d65193a9b0c9cc650d6a1d99a5f7d536e0768cea5bf818e3d
- Behavior: Directly updated the active plan and archived the previous plan without the required decision gate.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
