# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-007-route-manual-gen`
- Target behavior: route a screenshot-evidenced illustrated manual request to `manual-gen` without executing its gate

## Test Set / Fixture Version

- Fixture version: `manual-routing-v0.1.0`
- Entry fixture: `manual-handoff.md`
- Validation status: not executed as of `2026-08-05`

## Latest Result

- Behavior result: `FAIL`（with）/ `FAIL`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `FULL`（with）/ `FULL`（without）— 本轮重跑实际触发的断言场景
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

Overall result: FAIL

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| accepts_manual_entry_basis | PASS | PASS | with_skill 明确称“已完成入口校验”，并引用 handoff 中的范围、证据来源和预期产物；without_skill 明确称“已验证”，同样识别了范围、证据、目标和 `standard` 等入口信息。 |
| routes_manual_gen | PASS | FAIL | with_skill 明确选择 `docs-agent:manual-gen`；without_skill 仅写“manual specialist gate”，未明确选择 `manual-gen`。 |
| preserves_manual_handoff_context | FAIL | FAIL | with_skill 仅保留范围、证据和输出，遗漏 `request_type`、`change_tier`、`feature_path`、`host_repository`、`blockers_risks`；without_skill 也遗漏 `feature_path`、`host_repository`，且未完整保留原始阻塞风险字段。 |
| references_manual_gate_only | PASS | FAIL | with_skill 明确将截图、环境确认、候选步骤确认和写入交给“`manual-gen` 专项流程”，且声明当前未生成或修改文件；without_skill 未明确指向 `manual-gen` gate，仅泛称“manual specialist gate”，并额外自行判断 `docs/site/` 缺失为阻塞。 |

未满足断言（with/without 任一 FAIL）：`routes_manual_gen`、`preserves_manual_handoff_context`、`references_manual_gate_only`



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Not observed. The future lane must stop after selecting and pointing to `manual-gen`.

## Fresh Without-Skill Baseline

- Source: pending fresh baseline from the same prompt and pristine fixture without reading or applying docs-agent.
- Behavior summary: unavailable; no historical baseline may substitute.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- No behavior failure is recorded because the eval has not run.
- Infrastructure blocker: with-skill, without-skill, and independent review lanes are pending.

## Next Steps

- Run both isolated lanes and have an independent fresh reviewer evaluate every assertion.

## Runtime Artifact Policy

- Candidate outputs, transcripts, manifests, verdicts, timing, status, and diagnostics remain in isolated runtime scratch space and are not committed.
