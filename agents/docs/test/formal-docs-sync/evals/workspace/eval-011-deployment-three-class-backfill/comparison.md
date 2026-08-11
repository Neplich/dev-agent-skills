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
- Repository HEAD: `f2aa9b2c49be68550ec45538c221425607f428ce`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `dd975083d3977d90b71b3396dff2498ef2b7e8d49c50fab50b5462a26f3248ee`
- Skill overlay SHA-256: `9667198915198da0404e03a7d4c962d38742b19c5de4de5f0cf1473f02db2bf1`
- Judge schema SHA-256: `2e68facf61317de81b206f59b17f3e724dc3951afae11b2a8c4aad6ddba91a26`
- Eval definition SHA-256: `75d9816433885deaa537c3684a33cbf77a210bf3435c193880901b7467aafb6d`
- Metadata SHA-256: `e1dbc6626788bdd9110a7a2968862f7b97506d86b4133c4cf183a556eecf36ce`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_three_class_page_tree` | PASS | PASS: Locked delivery snapshot contains all 10 required pages, shared reference, three class subtrees, root navigation, and unverified markers. |
| `cross_checks_environment_reference` | FAIL | FAIL: The matrix covers the requested fields and LEGACY_TIMEOUT, but it falsely claims tests/test_settings.py covers invalid LOG_LEVEL and missing DATABASE_URL; the fixture test only contains tautological APP_PORT and DATABASE_URL assertions. |
| `separates_class_specific_contracts` | FAIL | FAIL: Development and Kubernetes/Helm contracts are substantially separated, but the Docker documentation omits migration handling despite the assertion requiring Compose migration coverage. |
| `maps_each_class_atomically` | PASS | PASS: The locked change-map snapshot maps the real Development, Docker, Helm, and shared configuration ranges, preserves src/product/** and custom_owner_field, and includes the required page closure. |
| `runs_nested_docs_checks` | PASS | PASS: Raw trace shows npm run test:docs initially failed on equivalent same-directory link syntax, was corrected, and then passed 3/3; the snapshot retains last_verified_version: unverified and reports the blocked docs-audit handoff. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bed66a02e7102d84cc8988d8318b854a858b57d12888f0168cc60650b6d45cd2; fixture_sha256=4d8408c1113f0b188f486ff52a1805928dda107a5b4bcef41d15ff086a7d524c; output_sha256=308772c4bc9ffda7a03f30556f8958bba22039708c9e13e66cdcb30aaa74286c; snapshot_sha256=b3758963abc7be9dbcb8bc82f8e08078cbfa312bf2131e5788a3883a737ca07a
- Behavior: Produced the complete 10-page deployment tree, cross-source environment matrix, class-specific pages, atomic mappings, and passing nested documentation checks, but included an unsupported test-coverage claim and omitted Docker migration handling.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bed66a02e7102d84cc8988d8318b854a858b57d12888f0168cc60650b6d45cd2; fixture_sha256=4d8408c1113f0b188f486ff52a1805928dda107a5b4bcef41d15ff086a7d524c; output_sha256=cdf375f49ababe22f68ce611a2bd574ae9b789f077b9eb02b17ff005eb865cac; snapshot_sha256=9c77aa77ad2ffb7c9abb30aa4751916a7948cd4b76ba13ad69c00080b085a895
- Behavior: Produced a broadly similar deployment tree and reported passing checks, but provided less auditable process and evidence detail; its shortcomings are comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- Environment-reference evidence overstates what tests/test_settings.py verifies.
- Docker class documentation does not cover migration handling.
- Next: Correct the environment reference to accurately describe tests/test_settings.py.
- Next: Document Docker migration behavior or explicitly state that no Compose migration mechanism is present.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
