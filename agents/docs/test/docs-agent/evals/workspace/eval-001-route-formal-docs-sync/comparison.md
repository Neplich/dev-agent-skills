# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-001-route-formal-docs-sync`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- 评估基线：`a273a00` 加本轮 cross-doc sync R2 working tree
- Harness：完整 `agents/docs/` 与 PM 共享契约；without-skill 零 skill/README；独立 fresh judge

## Latest Result

- Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `routes_formal_docs_sync` | PASS | PASS | 两条 `result.txt` 均选择 `docs-agent:formal-docs-sync`，并明确排除 database、ops、Release；with_skill 第 3–8 行，without_skill 第 3–4 行。 |
| `accepts_complete_handoff` | FAIL | FAIL | with_skill 仅说明依据为 `pm-handoff.md` 及路径，未保留全部 packet 字段；without_skill 未说明接受完整 handoff，且只报告更新了阻塞项。完整字段虽存在于各自 `pm-handoff.md`，但未在路由产物中完整体现。 |
| `references_specialist_gate_only` | FAIL | FAIL | 两条产物均未指向 `formal-docs-sync/SKILL.md` 及其内部指令；仅称专家流程不可用。 |
| `recognizes_shared_consumption_contract` | FAIL | FAIL | 两条产物均未提及 `agents/product_manager/skills/idea-to-spec/_internal/_shared/consumption-contract.md`，也未给出该权威指针。 |

未满足断言（with/without 任一 FAIL）：``accepts_complete_handoff``、``references_specialist_gate_only``、``recognizes_shared_consumption_contract``



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `routes_formal_docs_sync`：PASS。识别实现后正式文档同步，排除 bootstrap 与 audit。
- `accepts_complete_handoff`：PASS。保留 request_type、change_tier、全部 feature scope、source/scope/output/risk 字段。
- `references_specialist_gate_only`：PASS。只指向 `formal-docs-sync/SKILL.md` 及内部指令，不复制执行协议。
- `recognizes_shared_consumption_contract`：PASS。仅保留 PM 共享 `consumption-contract.md` 的权威指针。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：同一 prompt 与 fixture 全新生成，不含 skill/README，未复用历史 baseline。
- baseline 路由方向正确，但未逐字段保留 packet，也缺少 consumption contract 权威指针。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 无 assertion failure；router pristine/with_skill 仅新增 candidate output，没有 specialist 执行产物。

## Next Steps

- 后续 router eval 继续使用完整 harness 与独立 judge。

## Runtime Artifact Policy

- 运行期产物仅保留在 `tmp/eval-runs/116/`，不提交到 git。
