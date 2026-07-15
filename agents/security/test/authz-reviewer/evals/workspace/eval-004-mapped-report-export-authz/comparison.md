# Consumption Regression Comparison

## Evaluation Target

- Skill: `authz-reviewer`
- Eval: `eval-004-mapped-report-export-authz`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

**PASS** — with-skill 核证出文档'仅 admin'与代码'admin+analyst'的权限分歧并评估越权影响，unverified 文档不被采信为权威策略，且无 feature_path 时不越权落档审查文档。

## With-Skill Behavior

- 命中映射文档后回权限代码核证角色清单，分歧以文档/代码/影响/可信度限制结构化输出。
- 权限设计意图正确交回负责人确认（可能是代码越权也可能是文档过期），并遵守 feature_path 门禁不擅自创建 docs/security 产物。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 权限分析质量高（含对象级授权与身份可信度风险），但分歧记录未按契约结构化，落档边界由临场判断。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
