# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-013-deployment-aggregate-migration`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b9cf5f02e5624842eefaa770fff8e84ccfc602f0eed28accf48a25400705d39e` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-013-deployment-aggregate-migration`.
- Identity schema: `2`
- target_skill_sha256: `a3e1263ac8acb74f106913f935cefb0ebe0f7f059ccc011cd16715592fd0163d`
- eval_definition_sha256: `2adf472912fe37066628cc2da23affed241d146a6c7c80728c7df93b4f2fccc7`
- metadata_sha256: `1730a36a001d532f328500208fe2ccb136183d8551b840ea714421749b8365ea`
- fixture_sha256: `b9cf5f02e5624842eefaa770fff8e84ccfc602f0eed28accf48a25400705d39e`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `cb68cc7396b4ed1007a2bd5b5970baa015053110168fade98a969dbebc84c1b1`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `b6ae3621879be63fa5b02212924eed11dd010ad027f0308f85d7666d26a57421`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `migrates_aggregate_path` | PASS | With-skill delivery snapshot deletes `ops/deployment.md` and contains the root index, environment reference, and all three class pages. The root and class pages separate shared and class-specific content without retaining the old aggregate body. |
| `repairs_inbound_and_internal_links` | PASS | The snapshot updates `ops/index.md` and `product/runtime.md` to `deployment/index.md`; root-to-child and child-to-environment links are present and structurally resolvable. The docs test passes. |
| `updates_change_map_without_data_loss` | PASS | The with-skill `change-map.yaml` maps each deployment glob to its class page plus the shared/navigation closure, preserves `custom_owner_field`, the `exclude`, and the unrelated product mapping, and the trace records deduplicated stable ordering. |
| `updates_navigation_atomically` | PASS | The locked file-change event covers deletion, page-tree creation, inbound-link repairs, navigation, and change-map updates in one confirmed batch. `npm run test:docs` exits 0 with 2/2 passing, and the only old-path match is a test fixture assertion rather than a link. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=b9cf5f02e5624842eefaa770fff8e84ccfc602f0eed28accf48a25400705d39e; output_sha256=6a3dd58e32a65c3c10424eac6245951334c014fe27ac3a90607671935e306cf1; snapshot_sha256=b454c27e3038a117b2d9dbf848dcba2a9a9666edee638f02cc4070e0151569d4
- Behavior: Completed the deployment documentation migration, repaired links and mappings, preserved change-map data, and passed the host docs test.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=b9cf5f02e5624842eefaa770fff8e84ccfc602f0eed28accf48a25400705d39e; output_sha256=ba6ea37ca1ea417f87a989f1eccdfd6b186f54d516840404b0ea4b0f0b6682b9; snapshot_sha256=44b32c1da8cb63fc0059e30497e3a205abf5d4bd3dc82729ef9ce7211cc28bee
- Behavior: Also completed the basic migration and link repairs, but its change-map snapshot only points each source glob to its individual class page rather than the full shared/navigation closure.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
