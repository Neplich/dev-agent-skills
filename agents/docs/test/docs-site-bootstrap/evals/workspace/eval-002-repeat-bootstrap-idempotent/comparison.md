# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-site-bootstrap`
- Eval: `eval-002-repeat-bootstrap-idempotent`

## Test Set / Fixture Version

- Current fixture: `issue-122-assets-v2-c5r`
- Last fresh-evaluated fixture: `issue-122-assets-v1` at branch commit `a2a30a3`
- Fresh validation date: `2026-07-19`
- C5R deterministic alignment: current materialized `docs/site/package.json` is byte-identical to the packaged asset; no fresh model eval was run.

## Latest Result

**PASS（最近一次 fresh 结论，fixture v1）** — fresh judge 对 3 条 assertions 全部判定 PASS。C5R 已把物化 `package.json` 对齐到 fixture v2，但没有运行新的 with-skill / without-skill，因此不把确定性字节检查表述为新的 fresh PASS。

## With-Skill Behavior

- 38 个静态资产与 `assets/docs/site/` 逐字节一致，创建、冲突和失败均为 0。
- Manifest 的 9 个物化代表目标保持 `skipped-identical`，`createdAt` 保持 `2026-07-16T08:00:00+08:00`，前后 SHA-256 均为 `0bb02c44054da996a17a489f0453ced2c03cde6b9bf757d4a035ac5f3e90017b`。
- `standards/change-map.yaml`、`.meta/releases.json` 和既有正式页面全部保留；工作区与暂存区内容 diff 均为 0。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，使用相同原始 prompt 与完整运行态 fixture，新生成且未提供任何 skill 文档或 Agent README。
- baseline 同样确认 38 项 zero-diff 和 9 条代表性 manifest 状态；主要依赖 fixture 的等价假设，未提供 with-skill 的完整逐项资产证据链。
- baseline 结果仅作为对照输入，不影响 with-skill 的 PASS 判定。

## Failures

- 无 assertion failure。

## Next Steps

- 保留最近一次 fresh 结果；资产清单、幂等分类或 manifest 状态机变化时重新生成 fresh with/without validation。C5R 仅改变物化 `package.json` 的宿主检查严格度，已完成字节对齐并明确记录未重跑。

## Runtime Artifact Policy

- 本次 transcripts、workspace 副本、baseline 和 judge verdict 仅位于 `tmp/eval-runs/122/eval-002-repeat-bootstrap-idempotent/`，不提交到 git。
