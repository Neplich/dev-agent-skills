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
- target_skill_sha256: `a3e1263ac8acb74f106913f935cefb0ebe0f7f059ccc011cd16715592fd0163d`
- eval_definition_sha256: `75d9816433885deaa537c3684a33cbf77a210bf3435c193880901b7467aafb6d`
- metadata_sha256: `e1dbc6626788bdd9110a7a2968862f7b97506d86b4133c4cf183a556eecf36ce`
- fixture_sha256: `4d8408c1113f0b188f486ff52a1805928dda107a5b4bcef41d15ff086a7d524c`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `2e68facf61317de81b206f59b17f3e724dc3951afae11b2a8c4aad6ddba91a26`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `bed66a02e7102d84cc8988d8318b854a858b57d12888f0168cc60650b6d45cd2`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `b6ae3621879be63fa5b02212924eed11dd010ad027f0308f85d7666d26a57421`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_three_class_page_tree` | PASS | Locked with_skill delivery_snapshot contains the complete 10-page three-class tree, shared environment reference, navigation, and an index with class status and links. |
| `cross_checks_environment_reference` | PASS | The with_skill environment matrix covers all four variables with purpose/type, defaults, requiredness, constraints, class-specific consumption, sensitivity, safe handling, lifecycle, and source evidence; LEGACY_TIMEOUT is marked deprecated. |
| `separates_class_specific_contracts` | PASS | Locked pages provide separate Development, Docker, and Kubernetes/Helm prerequisites, commands, success criteria, rollback, troubleshooting, and class-specific image/configuration details. |
| `maps_each_class_atomically` | PASS | The locked change-map preserves the unrelated src/product entry, adds real source globs and complete required-doc closures, and trace events show atomic file updates followed by readback and normalization checks. |
| `runs_nested_docs_checks` | NOT_EXERCISED | The with_skill trace records npm run test:docs from the docs site with 3/3 passing, plus recursive link/frontmatter checks; all pages retain last_verified_version: unverified. The later audit handoff is blocked by the missing target release version. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bed66a02e7102d84cc8988d8318b854a858b57d12888f0168cc60650b6d45cd2; fixture_sha256=4d8408c1113f0b188f486ff52a1805928dda107a5b4bcef41d15ff086a7d524c; output_sha256=e9c964cab7323a05b473d338663c2cb95ee27f4de16eee9d500c282ac25badf2; snapshot_sha256=70846557f55ec3f83fdbfe25d183e2e68151e0e00f59d7e5d9188ad9caf33acd
- Behavior: Delivered a semantically complete, evidence-backed three-class deployment documentation tree with a cross-source environment matrix, atomic mappings, and passing nested documentation checks; audit handoff remains blocked on the missing release version.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bed66a02e7102d84cc8988d8318b854a858b57d12888f0168cc60650b6d45cd2; fixture_sha256=4d8408c1113f0b188f486ff52a1805928dda107a5b4bcef41d15ff086a7d524c; output_sha256=fcbc7f3d10721e12e5ff63c03a2b60f2dfcdc53079f4ea35f2b1d35361697c20; snapshot_sha256=9b36e6347767c3d0d47528eac9091711ee7d266f463e05231c7498b179ad61f8
- Behavior: Delivered the basic page tree and eventually passed the host test, but its environment reference and class-specific contracts are materially less complete and its trace shows iterative link-fix failures before the final pass.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Confirm the target release version, then complete the docs-agent:docs-audit handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
