# Consumption Regression Comparison

## Evaluation Target

- Skill: `dependency-risk-auditor`
- Eval: `eval-004-mapped-client-dependency`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

**PASS** — with-skill 识别清单 1.4.0、unverified 文档 2.1.0、公开 npm 最新 1.1.8 的三方版本矛盾，审计以制品来源确认为前提，无法确认时阻止发布。

## With-Skill Behavior

- 命中映射文档后核证依赖清单与公开源版本，unverified 文档版本不被采信为升级依据。
- 产出分级修复建议（P0 制品来源/SBOM 核验、P1 替换评估与文档修正），审计未修改文件。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 依赖分析质量同样很高（锁文件/SBOM/验收面完整），差异主要在消费路径未按 change-map 契约组织与分歧记录格式。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
