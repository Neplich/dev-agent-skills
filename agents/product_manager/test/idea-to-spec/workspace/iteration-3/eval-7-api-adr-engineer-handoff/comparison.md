# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-007-api-adr-engineer-handoff`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116` from `agents/product_manager/test/idea-to-spec/workspace/iteration-3/eval-7-api-adr-engineer-handoff`.
- Identity schema: `2`
- target_skill_sha256: `34042e851466ff927567e09fc5777d952f1546cabc96fbe4de98617d27f5b1fb`
- eval_definition_sha256: `02e5d899a7687cd28d5b7fe3ed85f267cd9ce62f15d9844aa4281eff90859ac1`
- metadata_sha256: `6b28964c95e54c379988fdfd7c54f486a5c872824039a926ede4358e3117f378`
- fixture_sha256: `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `7d015813fae4cd945c52acc28425338fd81878adf050d1ecc956ba13abe7bc00`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `2ab3ca8b74dd55c90856f6dfac8c03932d3fb9eacb469271c944f9a989eec4b0`
- Repository HEAD: `c13c53a9b6e4cf18215450050bc9e7d0a810b73c`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `55d032569bbd4014a60103aafb1c0773a93ff9dbe0ea681c46297ebeef4a35b3`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_to_trd_gen` | PASS | With-skill output explicitly states `engineer-agent:trd-gen` generates the API and ADR. |
| `does_not_use_pm_api_adr_generators` | PASS | With-skill output states both documents are Engineer-owned and PM should not use PM generators. |
| `engineer_paths_mirror_feature_path` | PASS | With-skill output lists `docs/engineer/chat-interface/history-search/API.md` and `ADR-001-search-index-strategy.md`. |
| `handoff_contains_feature_path_evidence` | PASS | The structured handoff includes `feature_path`, `parent_feature`, `feature_level`, the PRD path, and API/ADR decision-background evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2ab3ca8b74dd55c90856f6dfac8c03932d3fb9eacb469271c944f9a989eec4b0; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=6dd161c484022b2ddf0bacde7da8a06b80214a109266063e8ac3d14181ef21c7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes API/ADR work to Engineer trd-gen, preserves the feature path, and provides the required handoff evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2ab3ca8b74dd55c90856f6dfac8c03932d3fb9eacb469271c944f9a989eec4b0; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=a2024cc12e8f14736ddee4729b4705658feb622eb94ac26998a9ce234e3e890f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Routes to generic backend and architecture owners with incorrect API/ADR paths and no required Engineer handoff packet.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
