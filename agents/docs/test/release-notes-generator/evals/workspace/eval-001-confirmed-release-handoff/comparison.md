# Skill Eval Comparison

## Evaluation Target

- Skill: `release-notes-generator`
- Eval: `eval-001-confirmed-release-handoff`

## Test Set / Fixture Version

- Fixture: R1 contract placeholder
- Scope: minimal structure required by `check_eval_contract.py`

## Latest Result

**NOT RUN** — R1 只建立契约检查强制要求的最小 eval 定义；完整 AI Hub-shaped
fixture、fresh with-skill、同 prompt 的 fresh without-skill baseline 与最终判定属于
R2，当前不声称 PASS、PARTIAL 或 BLOCKED。

## With-Skill Behavior

- 未执行。R2 将使用完整宿主规范、相邻版本页、release metadata、index、docs
  checks 和发布证据运行。

## Without-Skill Baseline

- 未执行。R2 必须使用与 with-skill 相同的 prompt 和 fixture 重新生成 baseline，
  不得复用历史结果。

## Failures

- 无运行失败；当前缺少 R2 完整 fixture 与 fresh validation 结果。

## Next Steps

- R2 完成 fixture、deterministic runner、fresh with-skill/without-skill validation，
  再以真实证据更新本文件。

## Runtime Artifact Policy

- 运行期产物只写入 `tmp/eval-runs/`，不提交 transcript、verdict、timing、
  diagnostics 或其他 runner 输出。
