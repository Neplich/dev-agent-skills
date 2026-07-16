# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-006-audit-no-version-anchor`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- Commit: `c05f689`

## Latest Result

**PASS** — with-skill 在无 tag/Release/显式锚时仍完成审计：报告回退命名 audit-{target-short-sha}.md、记录 version_anchor: unavailable、不写 last_verified_version、不发明版本也不借用外层仓库 tag。

## With-Skill Behavior

- 无锚行为完整：审计可执行但盖章被正确禁止，取得真实锚后再版本化审计的路径明确。
- 未触碰 releases.json。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 文档。
- baseline 结论一致且同样不盖章，但回退命名与锚不可用记录是 with-skill 的协议行为。

## Failures

- 无。

## Next Steps

- 保留本结果。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
