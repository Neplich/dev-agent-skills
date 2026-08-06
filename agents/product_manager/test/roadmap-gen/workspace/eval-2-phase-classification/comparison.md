# Eval Result: roadmap-phase-classification

## Evaluation Target

- Skill: `roadmap-generator` → `roadmap-gen`（PASS 结论基于旧名，待重跑验证）
- Eval: `eval-002-phase-classification`
- Prompt: 为 `microsoft/vscode` 生成项目路线图
- Test set / fixture version: `evals.json` schema `1.0`; empty fixture context; live GitHub data queried on 2026-07-31
- Candidate source: `tmp/eval-runs/issue-196-l2-3-4/roadmap-gen/eval-002-phase-classification/with_skill/`
- Fresh baseline source: `tmp/eval-runs/issue-196-l2-3-4/roadmap-gen/eval-002-phase-classification/without_skill/`

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- Overall result: BLOCKED
- 注：以下 PASS 结论基于改名前的  评测记录保留；改名后待 fresh eval 重跑验证新入口。

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `open_closed` | PASS | Open milestones 按截止日期进入当前冲刺/近期计划，最近 5 个 closed milestones 进入“已完成”。 |
| `large_backlog` | PASS | Live 查询到 9,986 个未关联 milestone 的 open issue，仅列 20 条并汇总其余 9,966 条。 |
| `issue_details` | PASS | 1.132.0 issue 按 Agent/Chat、修复、API/功能、工程/发布分组，保留 checkbox、assignee 与链接。 |

## With Skill

- 完整区分 open/closed milestone，并在同一文档保留进度、日期阶段和已完成区域。
- 对超大 backlog 执行明确的 20 条截断，保留总数而不展开 9,986 条。
- Issue 分组使用仓库标签与主题语义，保留 assignee 和 GitHub 链接；空 milestone 仍显示并注明无 issue。

## Fresh Without-Skill Baseline

- 生成了简洁的版本阶段路线图，能保留部分 issue 链接、assignee 和主题分组。
- 没有呈现最近 closed milestone 的“已完成”区域，也没有查询并压缩 9,986 条未关联 milestone 的 backlog；因此在 `open_closed` 与 `large_backlog` 上弱于 with-skill。
- Baseline 更接近优先级规划摘要，with-skill 更完整地执行了 eval 的 GitHub 同步契约。

## Failures

- None.
- `release-blocker` 场景未命中，但它不属于本 eval 的 assertions，不影响 Coverage result。

## Next Steps

- 保留此 eval，持续验证 open/closed 分类、超大 backlog 压缩和 issue 细节保留。

## Runtime Artifact Policy

- 本轮 `with_skill`、fresh `without_skill`、transcript、final message 与生成的 roadmap 仅存于 `tmp/eval-runs/`。
- Git 只提交本 `comparison.md`；运行期产物不提交。
