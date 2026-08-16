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
- target_skill_sha256: `a3e1263ac8acb74f106913f935cefb0ebe0f7f059ccc011cd16715592fd0163d`
- eval_definition_sha256: `ac42526e36e715108f7b75fd8273d1a27b06b53f2d88401d4e0acf869a7f27d9`
- metadata_sha256: `5fd28d9378e7eecda587e4671ac17460a0dd3663cff48d75fd068b1dc2cb5f0c`
- fixture_sha256: `d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `9176713527a4959d0641a1feea488e487885b76c3aa23f11bb3b81f29825c3ae`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `b6ae3621879be63fa5b02212924eed11dd010ad027f0308f85d7666d26a57421`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_unconfirmed_batch_read_only` | PASS | Final status and diff contain only Analytics pages and the Analytics mapping; Accounts, API root, Billing, and unrelated mappings remain unchanged. |
| `creates_complete_product_tree` | PASS | The final fixture state contains product/index.md, product/analytics/index.md, and product/analytics/view-dashboard.md, with the Analytics mapping requiring all three. |
| `keeps_every_task_navigable` | PASS | Internal recursive navigation builds successfully; Analytics links to the dashboard task, the task links back to Analytics, and the both-visible Product root has no public-invalid正文 link. |
| `writes_evidence_backed_task_behavior` | PASS | The task page records the three allowed roles, ready/empty states, load retry behavior, unauthorized behavior, and recovery guidance, with implementation and acceptance-test references. |
| `updates_product_map_atomically` | PASS | Git evidence adds the three-page Analytics required_docs closure while preserving Billing and support triggers, excludes, and review_policy fields. |
| `runs_product_host_checks` | PASS | Trace records npm run test:docs, npm run build:public, and npm run build:internal from docs/site/ with exit code 0; delivered pages retain last_verified_version: unverified. |
| `blocks_audit_without_confirmed_version` | PASS | The handoff identifies the completed Analytics batch, affected docs/map, evidence, exclusions, and missing target_release_version, with status blocked pending confirmation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049; fixture_sha256=d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45; output_sha256=5c09bebc793073c24455f8a5458d2896280d2641bb988b212906d1d66404e3a4; snapshot_sha256=3d3ca2d40325b020e398bd14b12b538806d51d85941777961d402dd488b4c07e
- Behavior: Completed the confirmed Analytics documentation batch with bounded scope, evidence-backed task content, atomic mapping, host checks, and a blocked version-dependent audit handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049; fixture_sha256=d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45; output_sha256=5502557b40b056f45acc30d04da91caf29b467a27087912c2c056bd388108885; snapshot_sha256=64fb50e6bb6c30b3913c24bbce8458bf10d195c8ba4d7e6a8bb67f43d48dab68
- Behavior: Created a partial Analytics tree and mapping, omitted the Product-root navigation update, and reported only documentation tests while not running the required builds or audit handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
