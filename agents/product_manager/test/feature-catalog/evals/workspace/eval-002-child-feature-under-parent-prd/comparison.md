# Eval Result: eval-002-child-feature-under-parent-prd

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-002-child-feature-under-parent-prd`
- Test case: child-feature-under-parent-prd
- Workspace: `workspace/eval-002-child-feature-under-parent-prd`
- Latest result: BLOCKED - 本条是新增 skill 的首个 eval 定义，本轮只提交了 eval 定义与 fixture，尚未执行模型 transcript 生成和 fresh Codex subagent validation；`without_skill` baseline 也尚未生成。模型 eval 由维护者在 PR 上决定触发。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: 初版（本次随 skill 一起提交）——已有 `docs/pm/order-management/PRD.md` 父 PRD，代码新增 `src/orders/refund/` 退款模块与测试
- Expected output: 复用父 feature_path，退款作为 order-management 下子功能提案，parent_feature/feature_level 一致，说明确认后 prd-gen / trd-gen 链路，handoff packet 字段完整

## Assertions

- `parent_prd_context_read`: 先读父 PRD 并复用其 feature_path
- `child_nested_under_parent`: 子功能嵌套在父路径下
- `feature_level_metadata`: 父子元数据一致
- `handoff_packet_fields`: handoff packet 字段完整
- `no_bulk_prd`: 不越界生成 PRD/TRD

## With Skill

- 尚未运行。首次 fresh subagent validation 执行后在此记录 with-skill 行为摘要。

## Without Skill / Baseline

- BLOCKED: 尚未生成本 eval 的 `without_skill` baseline。按 Fresh Sub-Agent 门禁，首次执行时必须基于同一份 prompt 和 fixture 重新生成新的 baseline，不得复用历史 baseline。
- 在 baseline 与 with-skill 结果生成并被评审前，本文件不构成 eval PASS 结论。

## Failures

- 无（尚未执行）。

## Next Steps

- 维护者在 PR 上决定是否触发模型 eval workflow / fresh Codex subagent validation。
- 执行后更新本文件的 Latest result、With Skill 和 Without Skill / Baseline 小节。

## Runtime Artifacts Policy

- 运行期 transcripts、verdicts、outputs、timing 和 diagnostics 写入隔离 scratch workspace（如 `tmp/eval-runs/...`），不提交到 git；长期提交的结果只有本 `comparison.md`。
