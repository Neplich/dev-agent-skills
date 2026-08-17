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
- Source lock SHA-256: `c58f04d32c2ca3a22aec96f7ee027af648da5971453d2a5553d7ab2cd9272551`
- Prompt SHA-256: `bed66a02e7102d84cc8988d8318b854a858b57d12888f0168cc60650b6d45cd2`
- Repository HEAD: `60a4b3602dc07f3f6683a8873529bbdba6f8d27d`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84e19c3e634cfde176d2ff20ba8e9d25a4838db3ed1deb5def94a8d0f1d2ddd9`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_three_class_page_tree` | PASS | Locked delivery snapshot contains all 10 required pages, shared environment reference, three class indexes, child pages, and an entry index with navigation. |
| `cross_checks_environment_reference` | PASS | The locked environment-reference snapshot has a per-variable table covering purpose/format, requiredness/default, class applicability, safe example, secret/lifecycle status, effect, and evidence for APP_PORT, LOG_LEVEL, DATABASE_URL, and LEGACY_TIMEOUT; it explicitly marks LEGACY_TIMEOUT deprecated. |
| `separates_class_specific_contracts` | PASS | Locked pages separate Development, Docker Compose, and Kubernetes/Helm prerequisites, commands, success criteria, rollback, troubleshooting, image sources, values, secrets, hooks, rollout, and chart structure; unsupported Helm mappings are explicitly left unasserted. |
| `maps_each_class_atomically` | PASS | The locked change-map preserves the unrelated src/product entry and custom_owner_field, adds exact scripts/dev, deploy/docker, deploy/helm, and shared configuration mappings, and raw trace command evidence re-reads the map and generated pages after writing. |
| `runs_nested_docs_checks` | NOT_EXERCISED | Raw trace proves npm run test:docs ran in docs/site with exit code 0 and 3/3 tests passed; locked pages have internal visibility, unverified version markers, and resolving nested links. The final audit handoff is blocked/does not prove a completed docs-agent:docs-audit handoff because target release evidence is missing. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bed66a02e7102d84cc8988d8318b854a858b57d12888f0168cc60650b6d45cd2; fixture_sha256=4d8408c1113f0b188f486ff52a1805928dda107a5b4bcef41d15ff086a7d524c; output_sha256=497c7a5382d61c4024143d3411e5328bcc663b4f7d2f550caee80fd895ef5e87; snapshot_sha256=859210120066a7ab28897f0ab768ef71f230ec59fd2c95c2d032c7ee85bd867b
- Behavior: Delivered the complete 10-page deployment documentation tree, cross-source environment reference, scoped change-map updates, and passing nested documentation checks; recorded the release-context and documentation-site completeness limitations.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bed66a02e7102d84cc8988d8318b854a858b57d12888f0168cc60650b6d45cd2; fixture_sha256=4d8408c1113f0b188f486ff52a1805928dda107a5b4bcef41d15ff086a7d524c; output_sha256=133b0ff54020cfd366b66495da4b5bb27e7ee8a50151da53f85497cd33a2252f; snapshot_sha256=b0494708d509df0c769a589d12bbebd2663aaaba6747750014e9619e0f4e44b7
- Behavior: Fresh baseline also claimed a completed tree and passing checks, but its locked evidence showed an initial nested-link test failure before a later correction and less explicit evidence-boundary handling.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Confirm the target release version and complete the docs-agent:docs-audit handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
