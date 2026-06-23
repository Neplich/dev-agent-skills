# Eval Result: eval-006-nested-feature-path

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-006-nested-feature-path`
- Test case: nested-feature-path
- Workspace: `workspace/iteration-3/eval-6-nested-feature-path`
- Latest result: PASS - fresh Codex subagent validation on 2026-06-23 after the feature_path doc-schema update

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Existing approved parent PRD at `docs/pm/chat-interface/PRD.md`.
- Expected output: scan existing PM PRDs, resolve `feature_path=chat-interface/history-search`, avoid `docs/pm/history-search/PRD.md`, and include feature path fields in the handoff packet.
- Validation context: fresh Codex subagent semantic validation on 2026-06-23 after `prd-schema.md`, `brd-schema.md`, `test-spec-schema.md`, and `trd-schema.md` added explicit `feature_path` metadata requirements.

## Assertions

- `scan_existing_prds`: first turn scans existing PM PRDs before choosing a target folder.
- `nested_feature_path`: child feature resolves under the existing parent feature path.
- `no_parallel_top_level`: does not choose a parallel top-level child directory.
- `handoff_fields`: handoff packet includes `feature_path`, `feature`, `parent_feature`, `feature_level`, and `feature_path_evidence`.

## With Skill

Observed behavior:

- The current `idea-to-spec` skill, shared skill-map, output conventions, and gen conventions require scanning `docs/pm/**/PRD.md` before writing PM feature docs.
- The fixture contains an approved level-1 parent PRD at `docs/pm/chat-interface/PRD.md` with `feature_path: "chat-interface"`, `feature: "chat-interface"`, `parent_feature: "N/A"`, and `feature_level: "1"`.
- The prompt asks for chat history search under an existing Chat Interface PRD. The feature path gate therefore resolves the child feature as `feature_path=chat-interface/history-search`, `feature=history-search`, `parent_feature=chat-interface`, `feature_level=2`, with `feature_path_evidence` pointing to the parent PRD and fixture prompt.
- The skill contract explicitly blocks creating a parallel top-level `docs/pm/history-search/PRD.md` when an existing parent PRD clearly owns the child feature.
- The feature_path doc-schema update directly supports this eval: PRD and BRD schemas require the same feature metadata, TEST_SPEC consumes the confirmed PM/Engineer path, and legacy PM-side TRD validation mirrors `docs/engineer/{feature_path}/TRD.md`.

## Without Skill / Baseline

- Baseline behavior is diagnostic only.
- Without the skill-specific PM feature path gate, the likely risk is treating `history-search` as a standalone level-1 feature and writing `docs/pm/history-search/PRD.md`.

## Failures

- None found in this fresh Codex subagent validation after the feature_path doc-schema update.
- No transcript, verdict, output, or diagnostics artifact was generated in this worker pass.

## Next Steps

- Keep this eval as issue #37 PM coverage for nested `feature_path` routing.
- If model eval workflow is run later, compare transcript behavior against this durable expectation and keep runtime artifacts out of git.
- Future PM eval additions should preserve the no-parallel-top-level assertion for level-2 and level-3 paths.

## Runtime Artifacts Policy

- No runtime artifacts were created in this worker pass. Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
