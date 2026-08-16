# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-011-deployment-three-class-backfill`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `4d8408c1113f0b188f486ff52a1805928dda107a5b4bcef41d15ff086a7d524c` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-011-deployment-three-class-backfill`.
- Identity schema: `2`
- target_skill_sha256: `314b02febc2ef94201a8e1bf1080c874c355a0e47e6ac9a01b931425f08bfbd7`
- eval_definition_sha256: `75d9816433885deaa537c3684a33cbf77a210bf3435c193880901b7467aafb6d`
- metadata_sha256: `e1dbc6626788bdd9110a7a2968862f7b97506d86b4133c4cf183a556eecf36ce`
- fixture_sha256: `4d8408c1113f0b188f486ff52a1805928dda107a5b4bcef41d15ff086a7d524c`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `2e68facf61317de81b206f59b17f3e724dc3951afae11b2a8c4aad6ddba91a26`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `bed66a02e7102d84cc8988d8318b854a858b57d12888f0168cc60650b6d45cd2`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84e19c3e634cfde176d2ff20ba8e9d25a4838db3ed1deb5def94a8d0f1d2ddd9`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_three_class_page_tree` | PASS | The with_skill delivery snapshot contains all ten required deployment pages, the shared environment reference, three class indexes, and root navigation. |
| `cross_checks_environment_reference` | FAIL | The environment matrix covers the required fields and evidence sources, but LEGACY_TIMEOUT is recorded without its fixture default value of 30, so the per-variable default requirement is incomplete. |
| `separates_class_specific_contracts` | PASS | The with_skill snapshot provides separate Development, Docker Compose, and Kubernetes/Helm pages with class-specific prerequisites, commands, success criteria, rollback, troubleshooting, image sources, and values/chart references. |
| `maps_each_class_atomically` | FAIL | The change map preserves src/product/** and custom_owner_field, and maps all three deployment classes, but the scripts/dev/** row omits the Development image-build page, leaving that class mapping incomplete as an atomic scope. |
| `runs_nested_docs_checks` | NOT_EXERCISED | The raw trace proves npm run test:docs passed 3/3, but does not prove the required docs/site working directory or a public/internal recursive build check; those later/hidden checks are not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bed66a02e7102d84cc8988d8318b854a858b57d12888f0168cc60650b6d45cd2; fixture_sha256=4d8408c1113f0b188f486ff52a1805928dda107a5b4bcef41d15ff086a7d524c; output_sha256=cfb0182e15803a002174518ea9de0a5b378cc20f8b108c29448a0540011e70af; snapshot_sha256=2da5eb5af030a545ce74da425d662d578c6bcc2e76320f46961b1a6f3af0ccc2
- Behavior: Delivered a complete ten-page deployment tree with substantially richer evidence-backed class pages and an environment matrix; the locked snapshot has the two noted coverage defects, while the locked trace shows the nested docs test passing 3/3.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bed66a02e7102d84cc8988d8318b854a858b57d12888f0168cc60650b6d45cd2; fixture_sha256=4d8408c1113f0b188f486ff52a1805928dda107a5b4bcef41d15ff086a7d524c; output_sha256=ccdb373573c1b37b5a6f1ad514267a1ca145f818f03abc4636b53fcd734244cb; snapshot_sha256=c4c0f9ed92351e471b3ea82b69afaaf3ddba61ffb13807ff2969d88887bad69c
- Behavior: Produced the same page tree and a passing nested-docs test, but with substantially thinner class contracts, a four-column environment table, and less complete change-map coverage; this is comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The environment reference omits LEGACY_TIMEOUT's actual default value.
- The scripts/dev/** change-map entry does not include development/image-build.md.
- Next: Add LEGACY_TIMEOUT=30 and its deprecated/unused status to the environment matrix.
- Next: Add development/image-build.md to the scripts/dev/** required_docs mapping.
- Next: Run any host-defined public/internal documentation checks if they become available, recording their working directory and results.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
