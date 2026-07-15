# Consumption Regression Comparison

## Evaluation Target

- Skill: `appsec-checklist`
- Eval: `eval-005-mapped-search-security`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

**PASS** — with-skill 发现 Critical 级 SQL 注入（字符串插值），文档声称的参数化查询被核证为与代码不符的 unverified 声明，安全结论完全以代码为准。

## With-Skill Behavior

- 命中映射文档后以 search-handler.js 核证，拒绝把 unverified 文档的安全声明当作保证。
- 产出结构化安全报告：证据、攻击向量、影响上限、参数化修复方案与回归建议，未修改业务代码。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 同样发现注入与文档不符，安全判断合格，但证据组织为叙述式，未按契约形成结构化分歧记录。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
