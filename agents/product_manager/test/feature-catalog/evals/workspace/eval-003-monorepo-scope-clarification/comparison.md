# Eval Result: eval-003-monorepo-scope-clarification

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-003-monorepo-scope-clarification`
- Test case: monorepo-scope-clarification
- Workspace: `workspace/eval-003-monorepo-scope-clarification`
- Latest result: BLOCKED - 本条是新增 skill 的首个 eval 定义，本轮只提交了 eval 定义与 fixture，尚未执行模型 transcript 生成和 fresh Codex subagent validation；`without_skill` baseline 也尚未生成。模型 eval 由维护者在 PR 上决定触发。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: 初版（本次随 skill 一起提交）——pnpm monorepo，含 `apps/web`、`apps/admin`、`services/api` 三个独立 workspace，无 PM 文档
- Expected output: 识别多 workspace 且范围未指定，blocked 并只问一个最小范围澄清问题；不产出确认版功能目录，不写正式文档，不猜测并列顶层 feature_path 结论

## Assertions

- `blocked_on_scope`: 识别范围不清并 blocked
- `minimal_clarification`: 只问最小澄清问题
- `no_fabricated_catalog`: 不伪造确认版目录
- `no_parallel_top_level`: 不猜测并列顶层路径

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
