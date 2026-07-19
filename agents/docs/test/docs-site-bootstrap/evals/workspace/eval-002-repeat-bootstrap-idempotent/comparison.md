# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-site-bootstrap`
- Eval: `eval-002-repeat-bootstrap-idempotent`

## Test Set / Fixture Version

- Fixture: `issue-122-assets-v2-c5r`，本轮 omitted assumption 已对齐 40 项 inventory
- Asset snapshot: PR #126 R3 工作树中的 40 项权威 bootstrap assets
- Fresh validation date: `2026-07-19`
- Materialized scope: durable fixture 的 9 个代表性目标；隔离运行态实际物化完整 40 项

## Latest Result

**PASS（R3 fresh）** — 本轮全新 with-skill、同 prompt/fixture 的全新 without-skill baseline 与 assertion judge 已闭合证据链。`produces_zero_diff`、`reports_skipped_identical`、`preserves_existing_state` 三条 assertions 全部 PASS。

## With-Skill Behavior

- 完整读取并应用入口、opt-in、40 项 inventory、manifest、回读与 zero-diff 协议。
- durable fixture 的 9 个物化目标与当前资产逐字节一致，mismatch 为 0；隔离宿主进一步物化完整 40 项，包括新增 `package-lock.json` 与 `release-notes/README.md`。
- 完整运行态 40/40 项均分类为 `skipped-identical`；manifest 保持 `createdAt: 2026-07-16T08:00:00+08:00`，40 项状态均为 `skipped-identical`，SHA-256 为 `d2724b25ef44f1388eaa6ae2c0cd57429ad9d13e7b928559de1f0669a1dadf49`。
- 排除运行期 `node_modules` 后，重复执行前后 41 文件 SHA-256 清单完全一致；`standards/change-map.yaml`、`.meta/releases.json` 和既有正式页面均未重置。
- 在完整隔离宿主执行 `npm ci --ignore-scripts` 与 `npm run test:docs` 成功；frontmatter、strict affected、version metadata 和 Node tests 73/73 全部通过。

## Without-Skill Baseline

- 来源：本轮全新 baseline，使用相同原始 prompt、durable fixture 与 `fixture-scope.json`；明确不读取或应用目标 skill、内部指令、Docs Agent README、旧 comparison 或 with-skill 结果。
- baseline 依据 fixture 明示的 40 项等价假设，检查 9 个物化目标与既有 manifest 后不写任何文件，报告 `createdAt` 不变和内容 zero-diff。
- baseline 能保守维持宿主状态，但不能独立给出权威 asset-to-host mapping、完整 manifest 状态机或逐项 read-back；这些差异显示 skill 提供了可执行协议。
- baseline 仅作为对照输入，不替代 with-skill 的 assertion 判定。

## Failures

- 无 assertion failure 或阻断项。
- `npm ci` 报告 3 条非阻断 audit advisory；安装和全部 docs tests 仍成功，不影响本 eval 的幂等性结论。

## Next Steps

- 保留本轮 fresh PASS。后续若 inventory、物化清单、manifest 状态机或幂等分类变化，重新生成同 prompt 的 fresh with/without validation。

## Runtime Artifact Policy

- 本轮隔离宿主、hash 快照、依赖安装与测试输出仅位于 `tmp/eval-runs/pr126-r3-20260719-1256/eval-002/`，不提交到 git。
- 长期提交结果仅为本 `comparison.md`；`node_modules`、responses、verdicts、日志和 diagnostics 均保持运行期隔离。
