# Eval Result: eval-006-nested-feature-path

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-006-nested-feature-path`
- Test case: nested-feature-path
- Workspace: `workspace/iteration-3/eval-6-nested-feature-path`
- Latest result: PASS - durable comparison coverage updated on 2026-06-25 for a real 4-level `feature_path`; no fresh model transcript or runtime output was generated in this worker pass.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Existing approved parent PRDs at `docs/pm/chat-interface/PRD.md`, `docs/pm/chat-interface/messages/PRD.md`, and `docs/pm/chat-interface/messages/history/PRD.md`.
- 4+ fixture path: `chat-interface/messages/history/search`.
- Expected output: scan existing PM PRDs, resolve `feature_path=chat-interface/messages/history/search`, avoid `docs/pm/history-search/PRD.md`, `docs/pm/search/PRD.md`, and `docs/pm/chat-interface/history-search/PRD.md`, and include feature path fields in the handoff packet.
- Validation context: current durable fixture and eval contract review on 2026-06-25 after the 4-level coverage gap was identified.

## Assertions

- PASS `scan_existing_prds`: first turn scans existing PM PRDs before choosing a target folder.
- PASS `nested_feature_path`: child feature resolves under the existing 4-level parent feature tree.
- PASS `no_parallel_top_level`: does not choose a parallel top-level or truncated child directory.
- PASS `handoff_fields`: handoff packet includes `feature_path`, `feature`, `parent_feature`, `feature_level`, and `feature_path_evidence`.

## With Skill

- Expected with-skill behavior is to scan `docs/pm/**/PRD.md`, find the existing message history parent at `docs/pm/chat-interface/messages/history/PRD.md`, and keep the new search capability under that parent.
- The target PM artifact is `docs/pm/chat-interface/messages/history/search/PRD.md` with `feature_path: chat-interface/messages/history/search`, `feature: search`, `parent_feature: chat-interface/messages/history`, and `feature_level: 4`.
- The handoff packet must preserve `feature_path`, `feature`, `parent_feature`, `feature_level`, and `feature_path_evidence` so Engineer, Designer, QA, DevOps, and Security can mirror the same path.
- The skill contract blocks `docs/pm/search/PRD.md`, `docs/pm/history-search/PRD.md`, and `docs/pm/chat-interface/history-search/PRD.md` because those paths drop confirmed ancestry.

## Without Skill / Baseline
- Not run in this worker pass.
- High-level baseline contrast: a generic PM response may scan only the display name and create `docs/pm/history-search/PRD.md` or reuse the older 2-level `docs/pm/chat-interface/history-search/PRD.md`, losing the confirmed `messages/history` ancestry and producing an incomplete handoff packet.

## Failures

- None in the durable eval definition, fixture, and assertion alignment reviewed on 2026-06-25.
- No transcript, verdict, output, or diagnostics artifact was generated in this worker pass.

## Next Steps

- Keep this eval as issue #37 PM coverage for 4-level `feature_path` routing.
- If model eval workflow is run later, compare transcript behavior against this durable expectation and keep runtime artifacts out of git.
- Future PM eval additions should preserve the no-parallel-top-level assertion for 4+ paths.

## Runtime Artifacts Policy

- No runtime artifacts were created in this worker pass. Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
