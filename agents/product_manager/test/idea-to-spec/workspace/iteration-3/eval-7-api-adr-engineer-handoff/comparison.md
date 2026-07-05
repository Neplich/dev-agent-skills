# Eval Result: eval-007-api-adr-engineer-handoff

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-007-api-adr-engineer-handoff`
- Test case: api-adr-engineer-handoff
- Workspace: `workspace/iteration-3/eval-7-api-adr-engineer-handoff`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: confirmed PM PRD at `docs/pm/chat-interface/history-search/PRD.md`
- Expected output: PM does not generate Engineer API or ADR docs directly; it hands a feature path packet to `engineer-agent:trd-gen` and mirrors output paths under `docs/engineer/chat-interface/history-search/`.

## Assertions

- `does_not_use_pm_api_adr_generators`: API and ADR are Engineer-owned
- `routes_to_trd_gen`: next owner is `engineer-agent:trd-gen`
- `engineer_paths_mirror_feature_path`: Engineer outputs mirror `chat-interface/history-search`
- `handoff_contains_feature_path_evidence`: handoff packet includes feature path fields, PRD path, and API / ADR context

## With Skill

- The shared `idea-to-spec` skill map routes API and ADR generation to `engineer-agent:trd-gen`; PM internal API / ADR resources are not used to create Engineer-owned documents.
- The confirmed PRD provides `feature_path=chat-interface/history-search`, `parent_feature=chat-interface`, and `feature_level=2`.
- The required Engineer-owned outputs are under `docs/engineer/chat-interface/history-search/`, including `API.md` and `ADR-*.md`, not `docs/engineer/history-search/`.
- The handoff packet carries `feature_path`, `parent_feature`, `feature_level`, PRD source path, API goals, and search-index decision background.

## Without Skill / without_skill Baseline

- The baseline read the eval item and fixture before target skill docs. A generic PM response could directly draft API and ADR documents from the PRD.
- It may also choose a terminal-only Engineer path such as `docs/engineer/history-search/`, losing the confirmed feature-path mirror.

## Failures

- None. The current `idea-to-spec` ownership and handoff rules satisfy all API / ADR assertions.

## Next Steps

- Keep this eval as PM coverage for Engineer-owned API / ADR handoff and path mirroring.
- Re-run fresh validation if API / ADR ownership or Engineer handoff paths change.

## Runtime Artifacts Policy

- No runtime artifacts were created or committed. Transcripts, verdicts, timing, outputs, and diagnostics must remain outside git.
