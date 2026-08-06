# Eval Result: roadmap-no-dates

## Evaluation Target

- Skill: `roadmap-gen`
- Eval: `eval-003-no-dates`
- Prompt: 为 `golang/go` 生成项目路线图
- Test set / fixture version: `evals.json` schema `1.0`; empty fixture context; live GitHub data queried on 2026-07-31
- Candidate source: `tmp/eval-runs/issue-196-l2-3-4/roadmap-gen/eval-003-no-dates/with_skill/`
- Fresh baseline source: `tmp/eval-runs/issue-196-l2-3-4/roadmap-gen/eval-003-no-dates/without_skill/`

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `semantic_classification` | PASS | Patch milestones `Go1.25.13`/`Go1.26.6` 归入近期交付，当前 minor `Go1.27`、下一 minor `Go1.28` 和明显超出当前范围的 `Go1.29` 分层；非 semver milestones 单列交维护者确认。 |
| `no_fake_dates` | PASS | 文档明确不生成日期型 Mermaid Gantt，也没有为无日期版本 milestone 虚构截止日。 |
| `release_blockers` | PASS | Live 命中的 `release-blocker` issues 在对应 milestone 顶部以“🚨 发布阻塞项”突出，并保留 issue 链接。 |

## With Skill

- 用 semver 与当前开放版本关系推断 patch、当前/后续 minor 和远期版本，不依赖被移除的固定 Go 映射表。
- 无法仅靠 semver 匹配的 milestone 进入维护者确认清单；两个 2099 哨兵日期 milestone 也明确标注其非真实发布时间语义。
- 不生成无依据的 Gantt；release blockers、进度、assignee、closed milestones 和 backlog 均保留 live 证据。

## Fresh Without-Skill Baseline

- Baseline 也把维护版 `Go1.25.13`/`Go1.26.6`、当前 `Go1.27`、下一版本 `Go1.28`、远期 `Go1.29` 组织成 P0/P1/P2，并且没有虚构日期。
- 因此在本轮核心“milestone 语义推断”上，baseline 与 with-skill 基本持平，区分度不足；不能把通用模型已经具备的版本规划能力粉饰为 skill 独有收益。
- With-skill 的可见增益主要是更明确的 semver 推断理由、无法匹配项的用户确认边界，以及逐条突出 live `release-blocker`；baseline 对 blockers 多为目标性描述，没有同等完整地列出命中实体。

## Failures

- None.
- 内化度观察：语义推断本身没有形成强区分；本 eval 主要验证契约执行正确性，而不是证明 skill 相对 baseline 的显著优势。

## Next Steps

- 保留此 eval 作为无日期、语义推断和 release-blocker 的回归门禁。
- 后续评审继续关注 baseline 是否持续与 with-skill 持平；若长期无区分，应把它作为 skill 精简或 assertion 重构的决策证据。

## Runtime Artifact Policy

- 本轮 `with_skill`、fresh `without_skill`、transcript、final message 与生成的 roadmap 仅存于 `tmp/eval-runs/`。
- Git 只提交本 `comparison.md`；运行期产物不提交。
