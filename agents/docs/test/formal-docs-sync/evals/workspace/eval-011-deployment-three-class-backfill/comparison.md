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
- Fixture SHA-256: `4d8408c1113f0b188f486ff52a1805928dda107a5b4bcef41d15ff086a7d524c`
- Prompt SHA-256: `bed66a02e7102d84cc8988d8318b854a858b57d12888f0168cc60650b6d45cd2`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a0fd1ad6b8713d6036307d1b20788b4771cc4b6ba53645fe17625e0dd55bbb5b`
- Skill overlay SHA-256: `73e88fe8c07f988c3353f81f9b058d4f8350c48ee381f924fe8c8201b9f92bb4`
- Judge schema SHA-256: `2e68facf61317de81b206f59b17f3e724dc3951afae11b2a8c4aad6ddba91a26`
- Eval definition SHA-256: `75d9816433885deaa537c3684a33cbf77a210bf3435c193880901b7467aafb6d`
- Metadata SHA-256: `e1dbc6626788bdd9110a7a2968862f7b97506d86b4133c4cf183a556eecf36ce`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_three_class_page_tree` | PASS | Locked delivery snapshots include the required deployment index, shared environment page, Development (2), Docker (2), and Kubernetes/Helm (4) pages, with navigation and selection guidance. |
| `cross_checks_environment_reference` | FAIL | The environment table omits an explicit APP_PORT default, incorrectly marks APP_PORT as required for Development despite the source default, omits Kubernetes/Helm applicability for DATABASE_URL, and does not fully document effective mechanisms for each parameter. |
| `separates_class_specific_contracts` | FAIL | The class pages separate prerequisites, commands, success criteria, rollback, and troubleshooting, but Docker lacks documented network and migration coverage, while Kubernetes/Helm lacks ConfigMap handling and a real chart package tree. |
| `maps_each_class_atomically` | PASS | The locked change-map snapshot maps the real Development, Docker, Helm, and shared-configuration globs to the corresponding pages, preserves the unrelated existing custom_owner_field, and records the delivered navigation and mappings. |
| `runs_nested_docs_checks` | NOT_EXERCISED | The candidate reports npm run test:docs passed, but the locked test only proves nested internal links and change-map coverage; it cannot prove public/internal recursive navigation, and the docs-agent:docs-audit handoff remains blocked by the missing target release version. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bed66a02e7102d84cc8988d8318b854a858b57d12888f0168cc60650b6d45cd2; fixture_sha256=4d8408c1113f0b188f486ff52a1805928dda107a5b4bcef41d15ff086a7d524c; output_sha256=d1b8bf77a362faea4960996013e0e0206e8aa4af4397dffd5a6368a9e0a0eef0; snapshot_sha256=a287d9732496cf0e1756fed9d0dc414dddb90ddba45ef57b2325d1ee0d70e0e0
- Behavior: Delivered the requested page tree, evidence-linked mappings, and documented test execution, but with substantive contract omissions and inaccuracies.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bed66a02e7102d84cc8988d8318b854a858b57d12888f0168cc60650b6d45cd2; fixture_sha256=4d8408c1113f0b188f486ff52a1805928dda107a5b4bcef41d15ff086a7d524c; output_sha256=3f3fe6248ec2a39c1f2d8f6b211339c5339f3103ea32decaa962ba7a3e1d42e7; snapshot_sha256=387a2737eac2c4832db3caf15bc9b3f8953934d677e9824b30dd32a739d4e7c1
- Behavior: Delivered a similar page tree and concise verification claim, used only as comparison context.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill delivery has material environment-reference inaccuracies and omissions.
- The with_skill class-specific contracts omit required Docker and Kubernetes/Helm details.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
