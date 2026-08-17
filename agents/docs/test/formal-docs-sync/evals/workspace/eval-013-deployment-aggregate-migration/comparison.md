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
- target_skill_sha256: `314b02febc2ef94201a8e1bf1080c874c355a0e47e6ac9a01b931425f08bfbd7`
- eval_definition_sha256: `2adf472912fe37066628cc2da23affed241d146a6c7c80728c7df93b4f2fccc7`
- metadata_sha256: `1730a36a001d532f328500208fe2ccb136183d8551b840ea714421749b8365ea`
- fixture_sha256: `b9cf5f02e5624842eefaa770fff8e84ccfc602f0eed28accf48a25400705d39e`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `cb68cc7396b4ed1007a2bd5b5970baa015053110168fade98a969dbebc84c1b1`
- Source lock SHA-256: `c58f04d32c2ca3a22aec96f7ee027af648da5971453d2a5553d7ab2cd9272551`
- Prompt SHA-256: `ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40`
- Repository HEAD: `60a4b3602dc07f3f6683a8873529bbdba6f8d27d`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84e19c3e634cfde176d2ff20ba8e9d25a4838db3ed1deb5def94a8d0f1d2ddd9`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `migrates_aggregate_path` | FAIL | The old aggregate file is deleted and the full page tree exists, but the root and class pages repeat shared facts such as APP_PORT=8080 and /healthz that the assertion requires to live only in environment-reference.md. |
| `repairs_inbound_and_internal_links` | PASS | ops/index.md and product/runtime.md point to deployment/index.md; child pages use resolvable relative links to the environment reference and root index. |
| `updates_change_map_without_data_loss` | PASS | The three deployment mappings use stable sorted closure lists including class pages, environment-reference.md, indexes, and preserved custom_owner_field, exclude, and src/product mapping. |
| `updates_navigation_atomically` | FAIL | The locked trace records npm run test:docs passing 2/2 and a zero residual-old-link/structure check, but the delivered pages still duplicate shared aggregate facts, so duplicate-content consolidation is incomplete. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=b9cf5f02e5624842eefaa770fff8e84ccfc602f0eed28accf48a25400705d39e; output_sha256=9e9a37fe4c24d5d46bf1093efad26fbd47673049c904b5b758364b13894956f4; snapshot_sha256=5b594e0eb3899906b5b220c525d503e762b858bab856fce8e80afd8e4e31cbc9
- Behavior: Migrated the aggregate path, repaired links, created the full page tree, and produced complete change-map closures, but retained duplicated shared facts in root and class pages.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=b9cf5f02e5624842eefaa770fff8e84ccfc602f0eed28accf48a25400705d39e; output_sha256=cb4394e4530863aa954df42461f005ed0a2038d7042557f3ccd24acae5f667cc; snapshot_sha256=305f4add72815b7e22c5a85f195a379ffc4b60fc2039d460d519a746e9b5fbba
- Behavior: Fresh baseline migrated the path and inbound links but mapped each code area only to its single class page and did not provide the complete shared/recursive change-map closure.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- Shared APP_PORT and /healthz facts are repeated in the deployment root and class pages instead of being retained only in environment-reference.md.
- The atomic migration therefore does not fully consolidate duplicate aggregate content.
- Next: Consolidate shared APP_PORT and /healthz facts into environment-reference.md and have the root/class pages link to it without repeating those facts.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
