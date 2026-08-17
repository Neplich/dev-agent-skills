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
- target_skill_sha256: `62f7a88900be8a0aae1af9e34b28dc32abd76006ca95f89107567b68f5780813`
- eval_definition_sha256: `02e5d899a7687cd28d5b7fe3ed85f267cd9ce62f15d9844aa4281eff90859ac1`
- metadata_sha256: `6b28964c95e54c379988fdfd7c54f486a5c872824039a926ede4358e3117f378`
- fixture_sha256: `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `7d015813fae4cd945c52acc28425338fd81878adf050d1ecc956ba13abe7bc00`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `2ab3ca8b74dd55c90856f6dfac8c03932d3fb9eacb469271c944f9a989eec4b0`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `7b19869a4835a1feeb491815cac7af7bde071247819525989c10dbfbc0acd2f7`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `does_not_use_pm_api_adr_generators` | PASS | With-skill output explicitly states PM does not directly generate API/ADR and identifies them as Engineer-owned; no forbidden PM generator is used. |
| `routes_to_trd_gen` | PASS | With-skill output names `engineer-agent:trd-gen` as the recommended iteration and assigns the API/ADR work to Engineer. |
| `engineer_paths_mirror_feature_path` | PASS | With-skill output requires `docs/engineer/chat-interface/history-search/API.md` and `ADR-search-index.md`, mirroring the confirmed feature path. |
| `handoff_contains_feature_path_evidence` | PASS | The handoff includes `feature_path`, `parent_feature`, `feature_level`, the PRD path in `source_documents` and `feature_path_evidence`, plus API and search-index ADR decision context in `scope_decision` and required outputs. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2ab3ca8b74dd55c90856f6dfac8c03932d3fb9eacb469271c944f9a989eec4b0; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=7f5f4ecd11ad7908184fe70366b3eb433ac4c66fc9cf79d96bcf368e03759d43; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes the stable feature's API/ADR work to Engineer trd-gen, preserves the nested feature path, and supplies a complete handoff without mutation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2ab3ca8b74dd55c90856f6dfac8c03932d3fb9eacb469271c944f9a989eec4b0; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=b1b163e80fec531efd0a60b33eb9d156167c05e746107620c52e8398f08ab957; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline correctly avoids PM-owned generation but proposes incorrect docs/api and docs/adr paths and provides no structured handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
