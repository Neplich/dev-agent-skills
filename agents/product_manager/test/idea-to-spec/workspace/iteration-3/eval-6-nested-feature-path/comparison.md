# Eval Result: eval-006-nested-feature-path

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-006-nested-feature-path`
- Test case: nested-feature-path
- Workspace: `workspace/iteration-3/eval-6-nested-feature-path`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: approved PM PRDs for `chat-interface`, `chat-interface/messages`, and `chat-interface/messages/history`
- Expected output: scan existing PRDs, resolve search under `chat-interface/messages/history/search`, avoid parallel / truncated paths, and include feature path fields in the handoff packet.

## Assertions

- `scan_existing_prds`: scan or read existing PM PRDs first
- `nested_feature_path`: resolve to `chat-interface/messages/history/search`
- `no_parallel_top_level`: do not choose `docs/pm/history-search/PRD.md` or `docs/pm/chat-interface/history-search/PRD.md`
- `handoff_fields`: include `feature_path`, `feature`, `parent_feature`, `feature_level`, and `feature_path_evidence`

## With Skill

- `idea-to-spec` requires scanning `docs/pm/**/PRD.md` before choosing or writing a feature folder.
- The fixture establishes an approved parent chain: `chat-interface` -> `chat-interface/messages` -> `chat-interface/messages/history`.
- Message history search is a child under the confirmed history feature, so the correct `feature_path` is `chat-interface/messages/history/search`, with `feature=search`, `parent_feature=chat-interface/messages/history`, and `feature_level=4`.
- The handoff packet must include the feature path fields and `{source, reason}` evidence from the existing PRDs.

## Without Skill / without_skill Baseline

- The baseline read the eval item and fixture before target skill docs. A generic response could choose the shorter display-name path `docs/pm/history-search/PRD.md` or reuse the older two-level `docs/pm/chat-interface/history-search/PRD.md`.
- It may also omit `parent_feature`, `feature_level`, or structured `feature_path_evidence`.

## Failures

- None. The current `idea-to-spec` feature document memory rules satisfy all nested feature path assertions.

## Next Steps

- Keep this eval as issue #37 coverage for multi-level PM feature ownership.
- Re-run fresh validation if feature path inheritance or handoff fields change.

## Runtime Artifacts Policy

- No runtime artifacts were created or committed. Transcripts, verdicts, timing, outputs, and diagnostics must remain outside git.
