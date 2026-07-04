# Eval Result: eval-001-legacy-project-catalog

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-001-legacy-project-catalog`
- Test case: legacy-project-catalog
- Workspace: `workspace/eval-001-legacy-project-catalog`
- Latest result: BLOCKED - 本条是新增 skill 的首个 eval 定义，本轮只提交了 eval 定义与 fixture，尚未执行模型 transcript 生成和 fresh Codex subagent validation；`without_skill` baseline 也尚未生成。模型 eval 由维护者在 PR 上决定触发。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: 初版（本次随 skill 一起提交）——无 PM 文档的 Node.js 老项目，含登录认证、订单、订单状态通知后台任务、订单模型和测试
- Expected output: 显式标记待确认的功能目录草案，条目带 suggested_feature_path、分类证据、置信度、open questions 和关联代码路径，以维护者确认 feature_path 收尾，不生成正式文档或 PRD

## Assertions

- `draft_before_formal_docs`: 草案先行，不落正式文档
- `evidence_and_confidence`: 条目带分类证据和置信度
- `business_capability_naming`: 按业务能力命名
- `open_questions_present`: 不确定项记录待确认问题
- `confirmation_gate`: 以确认门禁收尾

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
