# Eval Result: eval-004-greenfield-bootstrap-routing

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-004-greenfield-bootstrap-routing`
- Test case: greenfield-bootstrap-routing
- Workspace: `workspace/iteration-2/eval-4-greenfield-bootstrap-routing`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-06-04 against the current uncommitted `idea-to-spec` skill

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that idea-to-spec handles greenfield-bootstrap-routing and produces the expected role-specific artifact.
- Expected output: 先输出空工作区 context summary；识别为 PM-first 的 greenfield-discovery 或 greenfield-bootstrap 路径；保持在 PM/idea-to-spec 路径里，不直接运行脚手架；明确下一步是需求澄清、PRD/DECISIONS 文档化或等价的 PM 动作，而不是工程实现。

## Assertions

- `assertion_1`: 先做空工作区检测
- `pm_first_lane`: 识别为 PM-first lane
- `pm_first`: 保持 PM-first，不直接工程化
- `assertion_4`: 给出文档化下一步

## With Skill

Observed behavior:

- PASS - fresh Codex subagent validation on 2026-06-04 confirmed all eval
  assertions pass, and E2E QA document generation is aligned to
  `docs/qa/e2e/{一级功能}/{二级功能}/{三级功能}/` with `TEST_SUITE.md`,
  `FLOW_INDEX.md`, `cases/`, and `scripts/`, including the `project-init`
  scaffolding example.
- 当前 skill 对空或近空 workspace 的产品请求要求先输出 context summary，选择 greenfield-discovery/bootstrap PM-first lane，不运行脚手架，并把 PRD/DECISIONS/project-init 作为下一步。

## Without Skill / Baseline

- Baseline behavior is diagnostic only.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in fresh Codex subagent validation.
- No residual legacy QA TEST_SPEC path, test-cases directory, or file
  exploration document requirements were found.

## Next Steps

- fixture 中 PRD.md 属于 cleanup 目标，不应视为本轮新产物。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
