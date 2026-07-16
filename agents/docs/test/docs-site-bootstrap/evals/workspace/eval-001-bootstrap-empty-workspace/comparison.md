# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-site-bootstrap`
- Eval: `eval-001-bootstrap-empty-workspace`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- Commit: `c05f689`

## Latest Result

**PASS** — with-skill 在显式 opt-in 下一次生成 35 个模板 + manifest（全部 created、与内嵌模板逐字节一致），回读验证通过并确认重复运行 zero-diff，全部写入限于 docs/site/。

## With-Skill Behavior

- 生成清单与磁盘文件、manifest 三方一致；frontmatter 7 字段合法。
- 明确说明写入授权来自显式 opt-in，完成后停下等待确认。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 文档。
- baseline 同样完成了 scaffold 生成，但清单完整性与 manifest 语义的核对组织较松散。

## Failures

- 无。

## Next Steps

- 保留本结果。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
