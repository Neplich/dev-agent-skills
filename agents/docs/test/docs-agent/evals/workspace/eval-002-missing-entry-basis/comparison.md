# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-002-missing-entry-basis`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- 评估基线：`a273a00` 加本轮 issue #116 R2 working tree
- Harness：完整 router harness、fresh zero-skill baseline 与独立 judge

## Latest Result

**PASS（3/3 assertions）** — router 对模糊建站请求准确指出缺失的已确认宿主路径，不执行 bootstrap，并温和引导经 `pm-agent` 补齐入口。

## With-Skill Behavior

- `guides_to_pm_agent`：PASS。明确没有 PM packet、等效链或完整 specialist entry basis。
- `does_not_execute_bootstrap`：PASS。未创建 `docs/site/`、模板或 manifest；fixture 仅新增 candidate output。
- `names_missing_credentials`：PASS。指出“显式建站请求 + 已确认宿主仓库路径”可解锁 bootstrap entry basis。

## Without-Skill Baseline

- 来源：同 prompt/fixture 的本轮全新 baseline，不含 skill/README。
- baseline 只索要一般建站信息，未识别 PM gate 或最小 specialist entry basis。

## Failures

- 无 assertion failure；未发生任何下游写入。

## Next Steps

- 保留当前温和入口安全网。

## Runtime Artifact Policy

- 运行期产物仅保留在 `tmp/eval-runs/116/`，不提交到 git。
