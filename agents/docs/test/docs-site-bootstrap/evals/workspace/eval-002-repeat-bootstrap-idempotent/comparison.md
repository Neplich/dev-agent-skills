# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-site-bootstrap`
- Eval: `eval-002-repeat-bootstrap-idempotent`

## Test Set / Fixture Version

- Fixture: `issue-122-assets-v2-c5r`
- Fresh-evaluated asset snapshot: C6 final commit `fix: 修复 strict affected 门禁 CI 场景并收尾 review 意见`（本文件随该提交交付，SHA 以提交后的 Git 记录为准）
- Fresh validation date: `2026-07-19`
- Materialized scope: 9 个代表性目标保持与当前资产逐字节一致；C6 修改的 4 个脚本/测试目标属于 fixture 明示的完整 38 资产运行态，本轮已实际物化并逐字节核验。

## Latest Result

**PASS（C6 fresh）** — 全新的 with-skill、全新的 without-skill baseline 与独立 judge 已闭合证据链。Judge 对 `produces_zero_diff`、`reports_skipped_identical`、`preserves_existing_state` 三条 assertions 全部判定 PASS。

## With-Skill Behavior

- 完整读取并应用 `docs-site-bootstrap` 入口、opt-in、inventory、manifest、回读和 zero-diff 协议。
- 当前 C6 的 38/38 个静态资产与隔离宿主逐字节一致，分类均为 `skipped-identical`；`created`、`kept-as-is`、冲突和失败均为 0。
- Durable fixture manifest 的 9 个物化代表目标保持 `skipped-identical`，`createdAt` 保持 `2026-07-16T08:00:00+08:00`。
- Manifest 前后 SHA-256 均为 `0bb02c44054da996a17a489f0453ced2c03cde6b9bf757d4a035ac5f3e90017b`，tracked 内容快照前后一致，站点 staged/unstaged diff 均为 0。
- `standards/change-map.yaml`、`.meta/releases.json` 和既有正式页面均未重置。

## Without-Skill Baseline

- 来源：本轮全新 Codex subagent，使用同一原始 prompt 与独立的完整运行态 fixture；明确禁止读取或应用目标 skill、Docs Agent README、旧 comparison 和旧 runtime。
- Baseline 同样报告 38 项 `skipped-identical`、manifest 的 9 项状态稳定、`createdAt` 不变、Git/content zero-diff。
- Baseline 对 29 个未物化目标主要依赖 `fixture-scope.json` 的等价假设；with-skill 则逐项对照当前 C6 源资产，并补齐入口凭据、完整 inventory、manifest 协议和后续 handoff 边界。
- Baseline 仅作为对照输入，不替代 with-skill 的 assertion 判定。

## Failures

- 无 assertion failure 或阻断项。
- Judge 记录的证据限制：内容零差异与状态保留有完整文件/Git 证据；“运行过程中从未发生同字节重写”依赖本轮响应的前后哈希与状态记录，而非 syscall 级审计。该限制不影响本 eval 的内容幂等性 PASS。

## Next Steps

- 保留本轮 fresh PASS。后续若资产 inventory、物化清单、manifest 状态机或幂等分类变化，重新生成同 prompt 的 fresh with-skill、fresh without-skill 与独立 judge。
- syscall 级写操作审计可作为未来 runner 增强，不是当前 assertion 的前置条件。

## Runtime Artifact Policy

- 本轮响应和 judge verdict 仅位于 `tmp/eval-runs/125-c6-20260719/eval-002-repeat-bootstrap-idempotent/`，不提交到 git。
- 长期提交结果仅为本 `comparison.md`；runtime workspace、response、verdict、日志和诊断继续保持隔离。
