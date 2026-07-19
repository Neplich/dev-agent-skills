# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-001-route-formal-docs-sync`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- 评估基线：`a273a00` 加本轮 issue #116 R2 working tree
- Harness：完整 `agents/docs/` 与 PM 共享契约；without-skill 零 skill/README；独立 fresh judge

## Latest Result

**PASS（4/4 assertions）** — router 接受完整 PM handoff、保留全部 packet 字段、正确选择 `formal-docs-sync`，并只引用 specialist gate 与共享 consumption contract。

## With-Skill Behavior

- `routes_formal_docs_sync`：PASS。识别实现后正式文档同步，排除 bootstrap 与 audit。
- `accepts_complete_handoff`：PASS。保留 request_type、change_tier、全部 feature scope、source/scope/output/risk 字段。
- `references_specialist_gate_only`：PASS。只指向 `formal-docs-sync/SKILL.md` 及内部指令，不复制执行协议。
- `recognizes_shared_consumption_contract`：PASS。仅保留 PM 共享 `consumption-contract.md` 的权威指针。

## Without-Skill Baseline

- 来源：同一 prompt 与 fixture 全新生成，不含 skill/README，未复用历史 baseline。
- baseline 路由方向正确，但未逐字段保留 packet，也缺少 consumption contract 权威指针。

## Failures

- 无 assertion failure；router pristine/with_skill 仅新增 candidate output，没有 specialist 执行产物。

## Next Steps

- 后续 router eval 继续使用完整 harness 与独立 judge。

## Runtime Artifact Policy

- 运行期产物仅保留在 `tmp/eval-runs/116/`，不提交到 git。
