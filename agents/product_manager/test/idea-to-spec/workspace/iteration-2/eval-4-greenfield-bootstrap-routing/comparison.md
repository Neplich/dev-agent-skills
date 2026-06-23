# Eval Result: eval-004-greenfield-bootstrap-routing

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-004-greenfield-bootstrap-routing`
- Test case: greenfield-bootstrap-routing
- Workspace: `workspace/iteration-2/eval-4-greenfield-bootstrap-routing`
- Latest result: PASS - fresh Codex subagent validation on 2026-06-23 after the feature_path doc-schema update

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that idea-to-spec handles greenfield-bootstrap-routing and produces the expected role-specific artifact.
- Expected output: 先输出空工作区 context summary；识别为 PM-first 的 greenfield-discovery 或 greenfield-bootstrap 路径；保持在 PM/idea-to-spec 路径里，不直接运行脚手架；明确下一步是需求澄清、PRD/DECISIONS 文档化或等价的 PM 动作，而不是工程实现。
- Validation context: fresh Codex subagent semantic validation on 2026-06-23 after `prd-schema.md`, `brd-schema.md`, `test-spec-schema.md`, and `trd-schema.md` added explicit `feature_path` metadata requirements.

## Assertions

- `assertion_1`: 先做空工作区检测
- `pm_first_lane`: 识别为 PM-first lane
- `pm_first`: 保持 PM-first，不直接工程化
- `assertion_4`: 给出文档化下一步

## With Skill

Observed behavior:

- The current `idea-to-spec` skill requires Phase 0 context summary for empty or near-empty product requests, with tech stack and existing docs marked as TBD/none.
- The PM-first guardrail keeps this request in `greenfield-discovery` or `greenfield-bootstrap`, recommends PRD/DECISIONS/project-init style document work, and does not run scaffolding commands.
- The fixture README says the workspace is intentionally empty except eval metadata. The stale root `PRD.md` remains only as an `execution_cleanup` target, so it does not change the expected PM-first routing.
- The feature_path schema update reinforces the PM-first lane: before `project-init` or PRD skeleton output becomes formal, the flow must establish a valid 1-3 level `feature_path` and include the required feature metadata fields.

## Without Skill / Baseline

- Baseline behavior is diagnostic only.
- Without the skill contract, the likely risk is starting `npm create`, `create-next-app`, or another engineering bootstrap before PM requirements are settled.

## Failures

- None found in this fresh Codex subagent validation after the feature_path doc-schema update.
- No transcript, verdict, output, or diagnostics artifact was generated in this worker pass.

## Next Steps

- fixture 中 `PRD.md` 属于 cleanup 目标，不应视为本轮新产物。
- 后续若将该 fixture 扩展为真实 PRD 产物校验，应断言输出使用 `docs/pm/{feature_path}/PRD.md` 而不是根目录 `PRD.md`。

## Runtime Artifacts Policy

- No runtime artifacts were created in this worker pass. Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
