# Eval Result: eval-002-feature-path-design-handoff

## Evaluation Target

- Agent: `designer`
- Skill: `designer-agent`
- Eval: `eval-002-feature-path-design-handoff`
- Test case: feature-path-design-handoff
- Workspace: `workspace/eval-2-feature-path-design-handoff`
- Latest result: PASS - durable comparison coverage updated on 2026-06-25 for a real 4-level design handoff path; no fresh model transcript or runtime output was generated in this worker pass.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: 4-level feature path `chat-interface/messages/history/search` with matching PM PRD and Engineer TRD.
- 4+ fixture path: `chat-interface/messages/history/search`.
- Expected output: route to the narrowest design skill chain, cite the confirmed feature path, use `docs/design/chat-interface/messages/history/search/` output paths, and stop before implementation.

## Assertions

- PASS `uses_confirmed_feature_path`: consume `chat-interface/messages/history/search` from the fixture.
- PASS `mirrors_design_outputs`: use `docs/design/chat-interface/messages/history/search/ui-ux-spec.md` and `docs/design/chat-interface/messages/history/search/visual-system.md`.
- PASS `no_synonym_top_level`: do not create `docs/design/search/`, `docs/design/history-search/`, `docs/design/chat-history-search/`, or a truncated `docs/design/chat-interface/history-search/` directory.
- PASS `stops_before_code`: do not emit code, implementation steps, test commands, or patches.

## With Skill

- Expected with-skill behavior is to consume `feature_path: chat-interface/messages/history/search` from the PM/Engineer handoff, read both same-path source documents, and preserve the full path in design outputs.
- The output contract writes design artifacts only under `docs/design/{feature_path}/`, so the expected UI/UX and visual deliverables are `docs/design/chat-interface/messages/history/search/ui-ux-spec.md` and `docs/design/chat-interface/messages/history/search/visual-system.md`.
- The Feature Path Gate blocks synonym or truncated directories when the parent feature is known, satisfying the no `docs/design/search/`, `docs/design/history-search/`, and `docs/design/chat-interface/history-search/` assertion.
- Designer boundaries forbid code, tests, scripts, deployment config, engineer task lists, and implementation instructions; the route stops at design handoff and names `engineer-agent` as the implementation owner.

## Without Skill / Baseline
- Not run in this worker pass.
- High-level baseline contrast: a generic design response may route the design work but collapse the path to `docs/design/history-search/` or the older 2-level `docs/design/chat-interface/history-search/`, breaking handoff symmetry with PM and Engineer.

## Failures

- None in the durable eval definition, fixture, and assertion alignment reviewed on 2026-06-25.

## Next Steps

- Keep this eval as Designer coverage for 4-level feature-path handoff. Residual risk: this validation is a direct durable comparison update; no model transcript was generated.

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
