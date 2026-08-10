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
- Fixture SHA-256: `b9cf5f02e5624842eefaa770fff8e84ccfc602f0eed28accf48a25400705d39e`
- Prompt SHA-256: `ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f24bfeb12dba77a74fcf3f0161749ae4671b83762eac08484e7ae08621d9bacb`
- Skill overlay SHA-256: `5dbb8d8559bfab3926047aa028e19f362490751247c2142101cfd687fff5239e`
- Judge schema SHA-256: `cb68cc7396b4ed1007a2bd5b5970baa015053110168fade98a969dbebc84c1b1`
- Eval definition SHA-256: `2adf472912fe37066628cc2da23affed241d146a6c7c80728c7df93b4f2fccc7`
- Metadata SHA-256: `1730a36a001d532f328500208fe2ccb136183d8551b840ea714421749b8365ea`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `migrates_aggregate_path` | FAIL | The old page is deleted and the page tree exists, but the root index and all three class pages repeat shared facts such as APP_PORT=8080; the snapshot therefore contradicts the requirement that shared facts remain only in environment-reference.md. |
| `repairs_inbound_and_internal_links` | PASS | Snapshot links update ops/index.md and product/runtime.md to deployment/index.md; child pages contain parseable relative links to the root and environment-reference.md. |
| `updates_change_map_without_data_loss` | PASS | The with_skill change map includes class-specific pages, environment-reference.md, and required ancestor/navigation pages; it preserves custom_owner_field, exclude, and the unrelated src/product mapping, with deduplicated stable ordering. |
| `updates_navigation_atomically` | PASS | The locked snapshot contains the migrated tree, repaired navigation and mappings, and no old-path markdown links. Raw trace item_16 records npm run test:docs from docs/site passing 2/2 with exit code 0. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=b9cf5f02e5624842eefaa770fff8e84ccfc602f0eed28accf48a25400705d39e; output_sha256=fd9f28c28a8c2a428f6ac09f7d7463dcc84477b47dd369bf1ecdb4b27eeab8b9; snapshot_sha256=a7717931bca143b7d235ed0d055f365375d90d2adcef0f197b19ea79fe27ece5
- Behavior: Completed the confirmed deployment-page migration with repaired links, expanded change-map closures, preserved fields, and passing documentation tests, but duplicated shared environment facts outside the dedicated reference page.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=b9cf5f02e5624842eefaa770fff8e84ccfc602f0eed28accf48a25400705d39e; output_sha256=64d318a5a7520a897de9a6a609f874757b94fd31a70c9ca2abdad04afc3cf0a7; snapshot_sha256=b1305fec62d686213f7ce3791e1088c12e6eab3530978293da547e8df437aabc
- Behavior: Fresh baseline also produced a migration-shaped delivery and passing test claim; used only as comparison context and not to determine with_skill assertion verdicts.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill delivery duplicates shared environment facts outside environment-reference.md, including APP_PORT=8080 in the root and class pages.
- Next: Move shared APP_PORT and health-check facts out of the root and class pages, leaving them only in environment-reference.md.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
