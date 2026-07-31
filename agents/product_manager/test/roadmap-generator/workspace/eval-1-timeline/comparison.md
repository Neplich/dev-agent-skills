# Eval Result: roadmap-timeline

## Evaluation Target

- Skill: `roadmap-generator`
- Eval: `eval-001-timeline`
- Prompt: 为 `flutter/flutter` 生成完整项目路线图
- Test set / fixture version: `evals.json` schema `1.0`; empty fixture context; live GitHub data queried on 2026-07-31
- Candidate source: `tmp/eval-runs/issue-196-l2-3-4/roadmap-generator/eval-001-timeline/with_skill/`
- Fresh baseline source: `tmp/eval-runs/issue-196-l2-3-4/roadmap-generator/eval-001-timeline/without_skill/`

## Latest Result

- Behavior result: **PASS**
- Coverage result: **PARTIAL**
- Overall result: PASS (partial coverage)

未覆盖场景：

- `phase_classification` 的 90 天以上 open dated milestone 分支未触发；live 数据只有逾期/30 天内与 31–90 天 milestone。
- `undated_semantic_inference` 的“无日期 milestone 可按 semver 匹配”分支未触发；6 个无日期 open milestone 都是非 semver 名称。无法匹配后列出并交用户确认的分支已触发。

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `phase_classification` | PASS | Q2/Q3 cutoff 按逾期或 30 天内归入当前冲刺，Q4 cutoff 按 31–90 天归入近期计划；没有捏造远期 milestone。 |
| `undated_semantic_inference` | PASS | 6 个非 semver、无日期 milestone 单列为“需维护者确认阶段”，没有自动归入“未排期”或虚构日期。 |
| `roadmap_artifacts` | PASS | 输出含 16 字符进度条、dated milestone Mermaid Gantt、issue checkbox 与 GitHub 链接。 |

## With Skill

- 严格用 `due_on` 分类有日期 milestone，并对无日期 milestone 进入语义推断路径。
- 对无法可靠匹配 semver 的 6 个 milestone 保留证据、逐项提出确认问题，没有使用固定“未排期”兜底。
- Backlog 截断为 20 条并保留总数；空 milestone、无 assignee、最近关闭 milestone 和未触发场景均显式说明。

## Fresh Without-Skill Baseline

- 同样正确处理了 dated milestone、进度、issue 链接和 Mermaid Gantt，基础路线图质量与 with-skill 接近。
- 但把 6 个无日期工程 milestone 直接归入“⚪ 未排期工程主题”，没有先按版本语义尝试匹配并把无法匹配项交用户确认，不满足新契约。
- Milestone 语义推断的区分度在本样本上主要来自“未匹配处理”：with-skill 遵守确认边界，baseline 使用了固定未排期兜底。由于 live 数据没有可匹配的无日期 semver milestone，本轮不能证明两者在成功语义匹配分支上的差异。

## Failures

- Behavior failure: none.
- Coverage gap: 90 天以上 dated milestone 与可匹配的无日期 semver milestone 均未出现。

## Next Steps

- 保留此 eval，后续 live 数据出现可匹配的无日期 semver milestone 时再观察成功推断分支。
- 不为补齐 coverage 人工制造 GitHub milestone 或日期。

## Runtime Artifact Policy

- 本轮 `with_skill`、fresh `without_skill`、transcript、final message 与生成的 roadmap 仅存于 `tmp/eval-runs/`。
- Git 只提交本 `comparison.md`；运行期产物不提交。
