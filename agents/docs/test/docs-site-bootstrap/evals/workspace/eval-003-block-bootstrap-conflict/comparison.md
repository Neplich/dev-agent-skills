# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-site-bootstrap`
- Eval: `eval-003-block-bootstrap-conflict`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- Commit: `c05f689`

## Latest Result

**PASS** — with-skill 对宿主定制的 standards/index.md 给出完整冲突清单并 blocked，提供 kept-as-is / 覆盖 / 显式合并三选项，用户选择前不写入任何冲突路径。

## With-Skill Behavior

- 冲突清单完整（含全部缺失目标分类），不部分覆盖、不格式化宿主内容。
- kept-as-is 语义与 manifest 登记规则表述一致。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 文档。
- baseline 同样阻断并给出三选项（仓库冲突契约的等价行为），差异在 manifest 状态机与 bootstrap 协议的显式引用。

## Failures

- 无。

## Next Steps

- 保留本结果。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
