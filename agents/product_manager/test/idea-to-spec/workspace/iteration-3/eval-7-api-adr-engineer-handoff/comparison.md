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
- Fixture SHA-256: `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116`
- Prompt SHA-256: `2ab3ca8b74dd55c90856f6dfac8c03932d3fb9eacb469271c944f9a989eec4b0`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c0da2e0366232678672d0c64ce9fa764d3b78f3caaaa8493348af1a7e1cd00fe`
- Skill overlay SHA-256: `8f09b52303d9393824dd3e732e656dd74f7ac606a082939547181274986dfb2d`
- Judge schema SHA-256: `7d015813fae4cd945c52acc28425338fd81878adf050d1ecc956ba13abe7bc00`
- Eval definition SHA-256: `02e5d899a7687cd28d5b7fe3ed85f267cd9ce62f15d9844aa4281eff90859ac1`
- Metadata SHA-256: `6b28964c95e54c379988fdfd7c54f486a5c872824039a926ede4358e3117f378`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `does_not_use_pm_api_adr_generators` | PASS | With-skill output assigns API/ADR generation to engineer-agent:trd-gen and states PM/idea-to-spec does not generate them, satisfying the ownership boundary. |
| `routes_to_trd_gen` | PASS | With-skill output explicitly routes the work to engineer-agent:trd-gen. |
| `engineer_paths_mirror_feature_path` | PASS | With-skill output specifies docs/engineer/chat-interface/history-search/API.md and ADR-001-search-index-strategy.md. |
| `handoff_contains_feature_path_evidence` | PASS | The handoff YAML includes feature_path, parent_feature, feature_level, the PRD path, and decision-background evidence for API/search-index work. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2ab3ca8b74dd55c90856f6dfac8c03932d3fb9eacb469271c944f9a989eec4b0; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=80fa67a50a5ece3a8947629915b40e3c096c71220aa06b547a0d15bb14afdecb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes API and ADR generation to Engineer trd-gen, mirrors the feature path, and provides the required handoff evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2ab3ca8b74dd55c90856f6dfac8c03932d3fb9eacb469271c944f9a989eec4b0; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=52a346aec878c3c3f192665c7b5684918358fbbcd40475334022ff19a389a59a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline suggests unrelated API/ADR owners and paths, with no Engineer trd-gen routing or feature-path handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
