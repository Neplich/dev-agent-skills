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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a0fd1ad6b8713d6036307d1b20788b4771cc4b6ba53645fe17625e0dd55bbb5b`
- Skill overlay SHA-256: `73e88fe8c07f988c3353f81f9b058d4f8350c48ee381f924fe8c8201b9f92bb4`
- Judge schema SHA-256: `9176713527a4959d0641a1feea488e487885b76c3aa23f11bb3b81f29825c3ae`
- Eval definition SHA-256: `be4dca3fd3a1f9f483cdce9c1cd23eedce67742046720ec2fe530fb1b240c258`
- Metadata SHA-256: `5fd28d9378e7eecda587e4671ac17460a0dd3663cff48d75fd068b1dc2cb5f0c`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_unconfirmed_batch_read_only` | PASS | With-skill Git evidence changes only Analytics Product pages and change-map; Accounts, Billing, and unrelated paths are untouched. |
| `creates_complete_product_tree` | PASS | Locked delivery snapshot contains product/index.md, product/analytics/index.md, and product/analytics/view-dashboard.md. |
| `keeps_every_task_navigable` | FAIL | Analytics index links the task and the task links its parent, but product/index.md contains plain text stating Analytics is reached through internal navigation without an actual link. |
| `writes_evidence_backed_task_behavior` | PASS | The task page records allowed roles, empty state, load failure retry, unauthorized recovery, and binds them to dashboard.py::view_dashboard and the named acceptance test. |
| `updates_product_map_atomically` | PASS | Final Git evidence includes all three Analytics required_docs and preserves existing Billing and support entries, including triggers, excludes, and review_policy fields. |
| `runs_product_host_checks` | FAIL | The output records all three docs-site host checks with cwd docs/site and exit 0, and all three pages retain last_verified_version: unverified; however the root-to-Analytics navigation link is absent, so navigation resolution is incomplete. |
| `blocks_audit_without_confirmed_version` | PASS | The audit handoff is explicitly blocked, lists the batch, affected docs, evidence, exclusions, and target_release_version: missing; it does not claim audit readiness or infer a version. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049; fixture_sha256=d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45; output_sha256=ac30ae9227f11b82d06a35d296220343d8767b459e7e4fe642e9b22da0e48f52; snapshot_sha256=2f59080876003ee128f9f3b6253d2c8e5eaa8dfa88fcb04ffb0f80680d32179d
- Behavior: Delivered the confirmed Analytics three-page tree and mapping, with evidence-backed task behavior and a correctly blocked audit handoff, but omitted the required root navigation link.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049; fixture_sha256=d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45; output_sha256=12599600c13bc6c93ce714f315811aae6e9ab968cb4053c9c67e3aaf3982b8ee; snapshot_sha256=796267faee13160336978a3a5f383e7a3bcb2e638962746cd04c65072088267b
- Behavior: Fresh baseline also delivered Analytics pages and mapping, but provided less explicit evidence-backed behavior and audit gating.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- product/index.md does not contain an actual navigable link to the Analytics domain.
- The host-check requirement is not fully satisfied because the root navigation link is missing.
- Next: Add a Markdown link from docs/site/product/index.md to docs/site/product/analytics/index.md or its directory.
- Next: Re-run the docs host checks after repairing root navigation.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
