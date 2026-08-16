# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-004-api-adr-owned-by-engineer`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116` from `agents/engineer/test/trd-gen/evals/workspace/eval-004-api-adr-owned-by-engineer`.
- Identity schema: `2`
- target_skill_sha256: `47bb3c8e8bad899368b78c2d70a8b75f85c0900f5ef5546caa9c9be9e034ebd2`
- eval_definition_sha256: `c2e125b845f0cfd23a8b77d0953e79c0dfdb8a47bc09cbe45bf84d70fdf9a2db`
- metadata_sha256: `62246848ad899e2c45f78627f4917a469fe8651f1607857696af955323ef348c`
- fixture_sha256: `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `2fb0119eb77903cfe9db053e59a3c85f9fb841609febdeb77953e7bac06ea0fe`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `b2bd7a022294f7539263ea78da33349f841bc77d827c181e2b2867a85cb18e8f`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `engineer_owns_api_and_adr` | PASS | All three delivered Engineer files carry `engineer_document_owner: engineer-agent:trd-gen`; the delivery summary identifies Engineer ownership for the TRD/API/ADR set. |
| `writes_all_engineer_docs_under_feature_path` | PASS | Locked delivery snapshot contains only `docs/engineer/chat-interface/history-search/TRD.md`, `API.md`, and `ADR-001-postgresql-full-text-search.md`. |
| `preserves_related_prd_and_metadata` | PASS | All three files preserve `feature_path`, `parent_feature: chat-interface`, `feature_level: "2"`, and `related_prd: docs/pm/chat-interface/history-search/PRD.md`. |
| `does_not_use_pm_generators` | PASS | Locked Engineer documents use `engineer-agent:trd-gen` and `generated_by: trd-gen`; no PM `api-gen` or `adr-gen` routing is present. |
| `no_plan_or_code` | PASS | Git status and delivery snapshot show only the three Engineer documentation files; no implementation plan, code, or test files were delivered, and the summary states downstream handoff was not executed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=fedf2a4170d93ecf4f64c59c59a4a99ec3207b12e7842cf11574e40cf548ba4c; snapshot_sha256=c0762151019da61999525da02dccfa25330ab4c35392299115bedd2d86c0f3a2
- Behavior: Created the requested Engineer-owned TRD, API, and ADR under the mirrored feature path, preserved metadata and PRD traceability, and stopped before implementation handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=c0b8a7011fd614fe7ec3d295b89d9b99b581e67093d6cae4fd145c4530986e0f; snapshot_sha256=c31139611031f1b227c715cc0e58c5e8e8e2a5e7f7cd08c075bcfe2ba89b96fb
- Behavior: Created TRD-like, API, and ADR documents under the PM path without Engineer ownership or mirrored Engineer paths.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
