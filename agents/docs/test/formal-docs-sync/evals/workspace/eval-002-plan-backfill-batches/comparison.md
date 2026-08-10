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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f24bfeb12dba77a74fcf3f0161749ae4671b83762eac08484e7ae08621d9bacb`
- Skill overlay SHA-256: `5dbb8d8559bfab3926047aa028e19f362490751247c2142101cfd687fff5239e`
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
| `keeps_unconfirmed_batch_read_only` | PASS | With-skill snapshot and Git status show only Analytics Product pages and mapping changed; Accounts, Billing, and unrelated entries remain unchanged. |
| `creates_complete_product_tree` | PASS | Snapshot contains Product root, Analytics index, and dashboard task page. |
| `keeps_every_task_navigable` | PASS | Internal generated navigation and page links provide root-to-domain-to-task and task-to-parent navigation; root visibility remains both and no invalid public body link was added. |
| `writes_evidence_backed_task_behavior` | PASS | Dashboard page records roles, empty state, load failure, retry, and unauthorized recovery, with implementation and acceptance-test bindings. |
| `updates_product_map_atomically` | PASS | Git evidence contains the three Analytics required_docs entries and preserves existing Billing/support triggers, excludes, and fields. |
| `runs_product_host_checks` | PASS | Trace records test:docs, build:public, and build:internal in docs/site, all exiting 0; generated navigation resolved and pages retain unverified versions. |
| `blocks_audit_without_confirmed_version` | PASS | With-skill handoff lists affected files, evidence, exclusions, completed batch, and explicitly marks audit blocked because target_release_version is missing. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049; fixture_sha256=d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45; output_sha256=5bfcc0a9862f049d3eb0d04aa497307630d6fb03cf06ad6c73b2852ff6274e79; snapshot_sha256=1de67455c0edca35167ee5f4e1461ce791f1de6311ef2cc4b38f5727688ba471
- Behavior: Delivered the complete Analytics Product subtree, evidence-backed behavior documentation, atomic change-map update, successful host checks, and a correctly blocked audit handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049; fixture_sha256=d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45; output_sha256=a3a933f37b159ceeb1f1c3b6a6e3b395131d09fb7584b66c81521d802cadc086; snapshot_sha256=ec75c7a1d00a0fab51134285ffaf1b1628accb37a91bbe1b2a3cc5e6a20488de
- Behavior: Delivered Analytics pages and a public build, but provided less complete verification and no confirmed blocked audit handoff in its user-visible result.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
