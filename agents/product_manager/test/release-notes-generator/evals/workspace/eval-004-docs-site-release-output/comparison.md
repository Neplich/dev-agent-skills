# Consumption Regression Comparison

## Evaluation Target

- Skill: `release-notes-generator`
- Eval: `eval-004-docs-site-release-output`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

**PASS** — with-skill 在站点存在时把发布说明写入 docs/site/release-notes/ 并保留 docs/changelog/ 版本归档与根索引，未虚构 PR/贡献者，另按契约结构化报告了陈旧 API 文档分歧。

## With-Skill Behavior

- 显式按 skill 与消费契约执行：发布说明落站点目录、归档留原契约路径、站点索引同步更新。
- 发现 docs/site/api/releases.md 仍停留 v1.3.0 且 unverified，按分歧证据记录而未顺带修改，保持精准变更边界。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 也把发布说明写入了站点目录并保留归档（fixture 中站点目录的存在自然引导了该行为），但未产出契约格式的分歧证据。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
