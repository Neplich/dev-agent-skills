# idea-to-spec Eval Summary

本文件汇总 `idea-to-spec` 当前 6 个核心 eval case 的状态、主要发现和后续待补点。

## Case Overview

| Eval | Scenario | Status | Main Finding | Follow-up |
| --- | --- | --- | --- | --- |
| Eval 1 | Existing project feature | PASS + Auto-checked | 2026-06-12 fresh subagent validation 通过；deterministic runner 已改为检查交互式首轮 transcript 协议，不再要求确认前生成最终 PM artifact | 可用多轮或 seeded artifact eval 另测最终落档 |
| Eval 2 | Existing project update | PASS + Auto-checked | 2026-06-12 fresh subagent validation 和 deterministic `decision_history_handled` 均通过 | 可继续增强 blast-radius 细粒度检查 |
| Eval 3 | Greenfield discovery | PASS + Subagent-checked | 2026-06-12 fresh subagent validation 通过；无 deterministic artifact assertions | 可继续增强“延后文档化”的文本信号检查 |
| Eval 4 | Empty-workspace PM-first bootstrap routing | PASS + Subagent-checked | 2026-06-12 fresh subagent validation 通过；无 deterministic artifact assertions | 可继续观察后续 prompt 演化是否仍稳定 |
| Eval 5 | PM agent direct delegation | PASS + Subagent-checked | 2026-06-12 fresh subagent validation 通过；dispatcher request 仍直接转交 `idea-to-spec` | 可继续增强 dispatcher handoff 断言 |
| Eval 6 | Nested feature path | PENDING validation | 2026-06-23 新增 issue #37 覆盖：已有父 PRD 时子功能应落到 `chat-interface/history-search`，不创建并列顶层目录 | 需要 fresh subagent validation 或 eval workflow 后更新 durable comparison |

## Key Conclusions

- 当前 `idea-to-spec` 协议在 fresh subagent semantic validation 中保持稳定，author 元数据规则没有破坏 PM-first 路由、section gate、DECISIONS 记忆或 existing-project-update 路由
- 本轮暴露并修复的问题主要在 eval 定义精度，而不是 author 元数据改动本身
- Eval 1 的 deterministic check 已对齐交互式首轮：验证 context summary、existing-project lane、确认门禁、PM 文档下一步和结构化问题/范围信号
- Eval 2 的 deterministic check 通过，证明 existing-project-update 产物路径和 decision history 更新仍可自动验证
- Eval 4 新增了空工作区 PM-first 守门场景，用于回归“不要直接初始化项目”
- Eval 5 覆盖 PM dispatcher 直接委托边界，用于回归“dispatcher 不直接替 specialist 完成产物”
- Eval 6 覆盖 `feature_path` 父功能识别，用于回归“子功能不生成并列顶层 PM 目录”
- `run_eval.py` 现在会先生成 fresh transcript，再执行断言；baseline 仍然是硬性必需产物
- 最新一次真实回归里，Eval 1 / Eval 2 的 deterministic checks 通过，Eval 3/4/5 按 metadata 生成 not-applicable 报告并依赖 fresh subagent validation
- `idea-to-spec` 的新协议已经形成可回归的最小基线：
  - context summary
  - 单决策点推进
  - `2-3` 个方案加 trade-off
  - section-based progression
  - `DECISIONS.md` 作为持久记忆
  - 增量落档与阶段收束

## Linked Artifacts

- 总体运行说明: [README.md](README.md)
- 人工对比模板: [COMPARISON_TEMPLATE.md](COMPARISON_TEMPLATE.md)
- Eval definitions: [evals.json](evals/evals.json)

### Eval 1

- Metadata: [eval_metadata.json](workspace/iteration-1/eval-1-existing-project-feature/eval_metadata.json)
- Review: [comparison.md](workspace/iteration-1/eval-1-existing-project-feature/comparison.md)

### Eval 2

- Metadata: [eval_metadata.json](workspace/iteration-1/eval-2-existing-project-update/eval_metadata.json)
- Review: [comparison.md](workspace/iteration-1/eval-2-existing-project-update/comparison.md)

### Eval 3

- Metadata: [eval_metadata.json](workspace/iteration-1/eval-3-greenfield-discovery/eval_metadata.json)
- Review: [comparison.md](workspace/iteration-1/eval-3-greenfield-discovery/comparison.md)

### Eval 4

- Metadata: [eval_metadata.json](workspace/iteration-2/eval-4-greenfield-bootstrap-routing/eval_metadata.json)
- Fixture: [README.md](workspace/iteration-2/eval-4-greenfield-bootstrap-routing/README.md)
- Review: [comparison.md](workspace/iteration-2/eval-4-greenfield-bootstrap-routing/comparison.md)

### Eval 5

- Metadata: [eval_metadata.json](workspace/iteration-2/eval-5-pm-agent-direct-delegation/eval_metadata.json)
- Fixture: [README.md](workspace/iteration-2/eval-5-pm-agent-direct-delegation/README.md)
- Review: [comparison.md](workspace/iteration-2/eval-5-pm-agent-direct-delegation/comparison.md)

### Eval 6

- Metadata: [eval_metadata.json](workspace/iteration-3/eval-6-nested-feature-path/eval_metadata.json)
- Fixture: [README.md](workspace/iteration-3/eval-6-nested-feature-path/README.md)
- Review: [comparison.md](workspace/iteration-3/eval-6-nested-feature-path/comparison.md)

## Next Improvements

1. Add separate multi-turn or seeded artifact checks for final `DECISIONS.md` / PRD generation when that behavior needs deterministic coverage.
2. Add stronger automated checks for behavioral assertions instead of relying mostly on manual review.
3. Standardize transcript format so turn-by-turn confirmation discipline is easier to verify.
4. Run fresh validation for Eval 6 and update the durable comparison with observed with-skill / baseline behavior.
