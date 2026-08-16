# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-012-deployment-class-evidence-gap`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `94a440475528b183f978a35b0a119247396e300b3f4d27c6c1d0f2046bc60924` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-012-deployment-class-evidence-gap`.
- Identity schema: `2`
- target_skill_sha256: `a3e1263ac8acb74f106913f935cefb0ebe0f7f059ccc011cd16715592fd0163d`
- eval_definition_sha256: `649fb22000e8030404ac6361df8372e15d8183baaa675df886e6c740c229829a`
- metadata_sha256: `9b6d976d4601ac0de151b2a46d4bd90f68a76a475f804b7878df438cf1dba8d6`
- fixture_sha256: `94a440475528b183f978a35b0a119247396e300b3f4d27c6c1d0f2046bc60924`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `e93bcd19b2a81fd498c0a0b76bf2788577403b4eb3f684a80f1adbb170c93ef8`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `b6ae3621879be63fa5b02212924eed11dd010ad027f0308f85d7666d26a57421`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_only_missing_class` | PASS | With_skill marks Kubernetes/Helm blocked and lists missing Chart, values, template consumers, cluster authority/kubeconfig permission, and execution verification; it does not rely on the unexecuted plan as support. |
| `continues_confirmed_classes` | PASS | With_skill delivers all five required pages, required links, evidence-bounded Development/Docker environment mappings, and change-map entries while continuing the confirmed batch. |
| `creates_no_placeholder_commands` | PASS | With_skill delivery contains no Kubernetes/Helm page tree or placeholder Helm commands/content and explicitly lists the evidence needed before completion. |
| `keeps_class_boundaries` | PASS | Development and Docker snapshots each contain separate prerequisites, commands, success criteria, rollback, and troubleshooting; Docker image sourcing is explicitly kept separate from Kubernetes evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff; fixture_sha256=94a440475528b183f978a35b0a119247396e300b3f4d27c6c1d0f2046bc60924; output_sha256=d17f1fce7e7f39d60a74b98f7dc2ef552fbdd194b2f83fd657a432892e128861; snapshot_sha256=9eedaa71343ee7a44dbbbfd4bfae59d2cdd0b39f46022fef8bda3427949b67e9
- Behavior: Completed the confirmed Development and Docker documentation batch, blocked Kubernetes/Helm pending missing evidence, and passed the final documentation checks.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff; fixture_sha256=94a440475528b183f978a35b0a119247396e300b3f4d27c6c1d0f2046bc60924; output_sha256=5a7344c30f2e76763b9c666b2a1e9a3692152697e93411b3f7d1767b20801bd9; snapshot_sha256=610d11e6ef05e7874b008695f639966532d791c859b17a9a400851915077dbe1
- Behavior: Also delivered the confirmed documentation batch and left Kubernetes/Helm uncreated, providing a fresh baseline for comparison.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
