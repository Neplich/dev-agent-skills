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
- Fixture SHA-256: `d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45`
- Prompt SHA-256: `8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049`
- Repository HEAD: `f2aa9b2c49be68550ec45538c221425607f428ce`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `dd975083d3977d90b71b3396dff2498ef2b7e8d49c50fab50b5462a26f3248ee`
- Skill overlay SHA-256: `9667198915198da0404e03a7d4c962d38742b19c5de4de5f0cf1473f02db2bf1`
- Judge schema SHA-256: `9176713527a4959d0641a1feea488e487885b76c3aa23f11bb3b81f29825c3ae`
- Eval definition SHA-256: `ac42526e36e715108f7b75fd8273d1a27b06b53f2d88401d4e0acf869a7f27d9`
- Metadata SHA-256: `5fd28d9378e7eecda587e4671ac17460a0dd3663cff48d75fd068b1dc2cb5f0c`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_unconfirmed_batch_read_only` | PASS | With-skill Git evidence changes only Product Analytics pages and its mapping; Accounts, Billing, and unrelated mappings remain unchanged. |
| `creates_complete_product_tree` | PASS | Locked delivery snapshot contains product/index.md, product/analytics/index.md, and product/analytics/view-dashboard.md. |
| `keeps_every_task_navigable` | PASS | Snapshots show root→Analytics→dashboard links, dashboard→parent links, visibility: both, unverified versions, and successful public/internal builds. |
| `writes_evidence_backed_task_behavior` | PASS | Dashboard page records allowed roles, empty/ready states, load retry, unauthorized recovery, and exact implementation plus acceptance-test references. |
| `updates_product_map_atomically` | PASS | Git evidence adds the three-document Analytics required_docs closure while preserving Billing and support mapping fields. |
| `runs_product_host_checks` | PASS | Raw trace contains test:docs, build:public, and build:internal commands with exit code 0; final handoff records cwd docs/site and unverified versions. |
| `blocks_audit_without_confirmed_version` | PASS | Handoff records the completed batch, affected docs/map, evidence, exclusions, blocked status, and target_release_version: missing. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049; fixture_sha256=d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45; output_sha256=bccb7ed3c47b4e80924f335d50e1bb239d02fb1cb33679c4a274a464566cd3f2; snapshot_sha256=05acda6729cc2dea706e0f369b4f4ebd6908bf2d3766c4616f03549a5def661b
- Behavior: Completed the confirmed Analytics documentation batch with atomic mapping updates, host checks, and a blocked audit handoff pending release-version confirmation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049; fixture_sha256=d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45; output_sha256=5a10d7ad41048ad28260a3f114aa69865a10ce1c685d05ddf491f2e3d068e1c6; snapshot_sha256=53140729720ae159c6d8af6cd9ebbd5dfc76061747e258a655fecb7ff53f4bc6
- Behavior: Created the Analytics pages and ran only the documentation test claim; it omitted the change-map update, build checks, detailed handoff, and version block.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
