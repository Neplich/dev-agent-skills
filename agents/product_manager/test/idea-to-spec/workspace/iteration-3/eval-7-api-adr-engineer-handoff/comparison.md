# Eval Result: eval-007-api-adr-engineer-handoff

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-007-api-adr-engineer-handoff`
- Test case: api-adr-engineer-handoff
- Workspace: `workspace/iteration-3/eval-7-api-adr-engineer-handoff`
- Latest result: PARTIAL - prior skill validation evidence is preserved; without-skill baseline was not generated for this historical comparison.
- Prior validation note: fresh Codex subagent validation on 2026-06-23 after API / ADR ownership migration and PM deprecated stub cleanup

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Confirmed PM PRD at `docs/pm/chat-interface/history-search/PRD.md`.
- Expected output: PM does not generate Engineer API or ADR docs directly; it hands a feature path packet to `engineer-agent:trd-gen`.

## Assertions

- `does_not_use_pm_api_adr_generators`: PM does not directly generate API or ADR docs.
- `routes_to_trd_gen`: next owner is `engineer-agent:trd-gen`.
- `engineer_paths_mirror_feature_path`: Engineer output paths mirror `chat-interface/history-search`.
- `handoff_contains_feature_path_evidence`: handoff packet includes feature path fields, PRD path, and API / ADR context.

## With Skill

Observed behavior:

- The current `idea-to-spec` skill routes stable technical planning, API documentation, and ADR creation or revision to `engineer-agent:trd-gen` after PRD confirmation.
- PM keeps ownership of product requirements and decision context only. The historical PM internal `api-gen`, `adr-gen`, `api-iteration`, and `adr-iteration` resources are deprecated handoff stubs and must not write Engineer-owned documents.
- The handoff packet carries `feature_path=chat-interface/history-search`, `parent_feature=chat-interface`, `feature_level=2`, the PRD path, API goals, and the search-index decision background.
- API and ADR outputs are expected under `docs/engineer/chat-interface/history-search/`, preventing a parallel `docs/engineer/history-search/` directory.

## Without Skill / Baseline
- BLOCKED: No actual without-skill baseline result is recorded for this historical comparison. This file is not treated as a full eval PASS until a baseline result is generated and written here.
- Without the ownership gate, PM could directly use the historical internal API / ADR generators and write Engineer docs using only the terminal feature name.

## Failures

- None found in this fresh Codex subagent validation.

## Next Steps

- Keep this eval as PM coverage for API / ADR Engineer handoff and feature path mirroring.

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
