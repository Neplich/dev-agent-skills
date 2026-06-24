# Eval Result: eval-002-existing-project-update

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-002-existing-project-update`
- Test case: existing-project-update
- Workspace: `workspace/iteration-1/eval-2-existing-project-update`
- Latest result: PARTIAL - prior skill validation evidence is preserved; without_skill baseline was not generated for this historical comparison.
- Prior validation note: fresh Codex subagent validation on 2026-06-23 after the feature_path doc-schema update

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that idea-to-spec handles existing-project-update and produces the expected role-specific artifact.
- Expected output: 识别为 existing-project-update；先总结 delta 和影响范围；优先走 change-impactor / iteration 思路而不是整份重写；明确受影响文档和后续迭代路径。
- Validation context: fresh Codex subagent semantic validation on 2026-06-23 after `prd-schema.md`, `brd-schema.md`, `test-spec-schema.md`, and `trd-schema.md` added explicit `feature_path` metadata requirements.

## Assertions

- `update`: 识别 update 场景
- `delta_blast_radius`: 先做 delta 与 blast radius 分析
- `assertion_3`: 优先迭代而非重写
- `assertion_4`: 文档路径明确

## With Skill

Observed behavior:

- The current `idea-to-spec` and shared skill-map route approved behavior changes to `existing-project-update`.
- The required behavior is to summarize the requested delta and blast radius first, then prefer `change-impactor` / targeted iteration over full regeneration.
- The fixture contains approved notification-center `DECISIONS.md`, `PRD.md`, and Engineer `TRD.md`; the durable docs now preserve the hybrid event-driven transition and explicitly reject permanent polling-only delivery, satisfying the update and decision-history expectations.
- The feature_path schema update is compatible with this eval: legacy single-level `notification-center` docs remain readable as a level-1 feature, while any updated formal docs or handoff should preserve `feature_path=notification-center`, `feature=notification-center`, `parent_feature=N/A`, and `feature_level=1`.

## Without Skill / Baseline
- BLOCKED: No actual without_skill baseline result is recorded for this historical comparison. This file is not treated as a full eval PASS until a baseline result is generated and written here.
- Without the skill contract, the likely risk is treating the request as a new design or rewriting documents without retiring the prior polling decision.

## Failures

- None found in this fresh Codex subagent validation after the feature_path doc-schema update.
- No transcript, verdict, output, or diagnostics artifact was generated in this worker pass.

## Next Steps

- 后续可继续强化旧决策退役/修订断言，并在产生新版 PRD/TRD/Test Spec 时校验 feature_path frontmatter。

## Runtime Artifacts Policy

- No runtime artifacts were created in this worker pass. Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
