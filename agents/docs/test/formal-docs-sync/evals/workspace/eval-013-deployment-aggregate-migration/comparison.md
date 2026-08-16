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
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84e19c3e634cfde176d2ff20ba8e9d25a4838db3ed1deb5def94a8d0f1d2ddd9`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `migrates_aggregate_path` | PASS | with_skill delivery_snapshot deletes docs/site/ops/deployment.md and adds deployment/index.md, environment-reference.md, and all three class directories without retaining the old aggregate file. |
| `repairs_inbound_and_internal_links` | FAIL | Inbound links in ops/index.md and product/runtime.md point to the new root. However, each class page links to ../../environment-reference.md, which resolves outside the deployment tree; the correct relative path is ../environment-reference.md. |
| `updates_change_map_without_data_loss` | PASS | with_skill change-map.yaml maps each deployment glob to its class page plus the shared environment and root pages, preserves custom_owner_field and exclude, and retains the unrelated src/product mapping. |
| `updates_navigation_atomically` | FAIL | The locked snapshot shows the deletion, new both-visibility page tree, navigation and mapping updates in one delivery; runner evidence shows npm run test:docs passed and no old aggregate links in site documents. The broken nested links mean the claimed link-repair/navigation result is not fully satisfied. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=b9cf5f02e5624842eefaa770fff8e84ccfc602f0eed28accf48a25400705d39e; output_sha256=80914870e7e8daf9a1f5add56dd64978f62404fede94b9879e004120302d44a5; snapshot_sha256=cc9a0e4678a1e5108ed354b6591bfd913d21fb39578a62d746a8a3c9809935a7
- Behavior: Migrated the aggregate page, created the full page tree, repaired inbound links, and expanded change-map entries, but left all three class-page links to the shared environment page broken.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=b9cf5f02e5624842eefaa770fff8e84ccfc602f0eed28accf48a25400705d39e; output_sha256=ecf22dcfd5aee37d8d261c11efe45ba052d8ba2c6d9a9684308b4cf4ab32b38f; snapshot_sha256=6b4a1a586d2facdb59b279598368294d6d672eeeb62dd2f1ed4d257b58e21e23
- Behavior: Fresh baseline also migrated the page tree and repaired inbound links; its change map only points to class pages and omits the shared/root mappings, while its child-to-shared links are correct.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill class pages contain broken relative links to environment-reference.md.
- The navigation/link-repair assertion is not fully satisfied because nested internal links do not resolve.
- Next: Change each class page's environment-reference link from ../../environment-reference.md to ../environment-reference.md, then rerun the documentation link check.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
