# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-site-bootstrap`
- Eval: `eval-002-repeat-bootstrap-idempotent`

## Test Set / Fixture Version

- Fixture: `ws2-bootstrap-v1`
- Branch fixture commit: `71bbb09`

## Latest Result

**PASS** — fresh judge 对 3 条 assertions 全部判定 PASS。with-skill 对 4 个物化代表目标逐字节比较一致，并按 fixture 等价规则将其余 31 个目标视为一致；35 项均分类为 `skipped-identical`，manifest、`createdAt`、change-map、release metadata 和正式页面均未改写。

## With-Skill Behavior

- Manifest 回读有效，4 个物化目标的持久状态保持 `skipped-identical`，`createdAt` 保持 `2026-07-16T08:00:00+08:00`。
- Manifest 前后 SHA-256 一致，工作区与暂存区内容 diff 均为空。
- 明确报告 0 created、0 kept-as-is、0 conflicting，并保留宿主 change-map、release metadata 和页面状态。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，使用相同原始 prompt 与 fixture，新生成且未接触 skill 文档或 Agent README。
- baseline 同样正确利用 `fixture-scope.json`，最终文件、manifest、状态与时间均无差异，核心 assertions 也成立。
- with-skill 的增益主要是更完整的持久状态语义、精确 manifest 哈希、逐项分类和后续 handoff；本用例的最终行为与 baseline 没有实质差异。

## Failures

- 无 assertion failure。with-skill 的首个本地校验命令遗漏 Ruby `time` 模块，补充后完成同一轮只读验证，未产生文件改写。

## Next Steps

- 保留本结果；幂等分类或 manifest 状态机变化时重跑此 eval。

## Runtime Artifact Policy

- 本次 transcripts、workspace 副本和 judge verdict 仅位于 `tmp/eval-runs/118/eval-002-repeat-bootstrap-idempotent/`，不提交到 git。
