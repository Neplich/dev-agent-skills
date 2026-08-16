# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-002-plan-backfill-batches`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-002-plan-backfill-batches`.
- Identity schema: `2`
- target_skill_sha256: `314b02febc2ef94201a8e1bf1080c874c355a0e47e6ac9a01b931425f08bfbd7`
- eval_definition_sha256: `ac42526e36e715108f7b75fd8273d1a27b06b53f2d88401d4e0acf869a7f27d9`
- metadata_sha256: `5fd28d9378e7eecda587e4671ac17460a0dd3663cff48d75fd068b1dc2cb5f0c`
- fixture_sha256: `d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `9176713527a4959d0641a1feea488e487885b76c3aa23f11bb3b81f29825c3ae`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84e19c3e634cfde176d2ff20ba8e9d25a4838db3ed1deb5def94a8d0f1d2ddd9`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_unconfirmed_batch_read_only` | PASS | With-skill git evidence changes only the Analytics Product pages and change map; Accounts, API root, Billing, and unrelated mappings remain unchanged. |
| `creates_complete_product_tree` | PASS | The delivered tree and final mapping contain product/index.md, product/analytics/index.md, and product/analytics/view-dashboard.md. |
| `keeps_every_task_navigable` | PASS | Internal navigation/build evidence resolves the Analytics-to-task link and task-to-parent link; the existing Product root remains visibility: both, and the new pages are internal. |
| `writes_evidence_backed_task_behavior` | PASS | The task page records owner/admin/analyst access, empty state, load failure retry, unauthorized recovery, and links the dashboard implementation and acceptance test. |
| `updates_product_map_atomically` | PASS | The final change map adds src/product/analytics/** with all three required_docs; Billing and support entries retain their existing trigger, exclude, and review_policy fields. |
| `runs_product_host_checks` | PASS | Raw trace records npm run test:docs, npm run build:public, and npm run build:internal from docs/site/ with exit 0; all three delivered pages show last_verified_version: unverified. |
| `blocks_audit_without_confirmed_version` | PASS | The audit handoff lists blocked status, the completed Analytics three-page batch, affected pages/map, supporting evidence, exclusions, and target_release_version: missing while awaiting release confirmation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049; fixture_sha256=d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45; output_sha256=4bffca58fd581a4f51f24ab9ed0093e23312ee71b56cdc3b975e017ecc31e459; snapshot_sha256=264efcb8f23c713a7f08fb2f5caa01e14d2aed58655288be04846f718742b34d
- Behavior: Completed the confirmed Analytics backfill, updated the atomic change map, ran all required host checks, and blocked audit pending a confirmed release version.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049; fixture_sha256=d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45; output_sha256=5f896298587de9e7d49749a65ad3cf549551df18a45be1cc73a076fb934d06d8; snapshot_sha256=c870c01f3a28eea0ac53e6787e3ecbdcf424b91d772da44eeba17834fe1c1925
- Behavior: Fresh baseline created the Analytics pages and preserved Accounts, but did not update the change map or run the required host checks/audit handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
