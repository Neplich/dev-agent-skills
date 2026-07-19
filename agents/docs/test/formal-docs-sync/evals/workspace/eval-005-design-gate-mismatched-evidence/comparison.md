# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-005-design-gate-mismatched-evidence`

## Test Set / Fixture Version

- Fixture: `issue-121-s2-final`
- Run date: `2026-07-19`

## Latest Result

**PASS** — with-skill 3/3 assertions 通过；without-skill baseline 3/3。

## With-Skill Behavior

- 只加载 design 模块，识别 PRD/TRD/实际路径证据不一致。
- design 页面与映射零变化，并分别指出 PM 与 Engineer/trd-gen 的修复责任。

## Without-Skill Baseline

- 全新 baseline 在本 fixture 上也满足 3/3，说明该阻塞信号本身足够明显。
- with-skill 的价值主要体现在稳定的 owner 和双面门禁表达。

## Failures

- with-skill 无 assertion failure。

## Next Steps

- 保留作为明显冲突的安全网回归用例。

## Runtime Artifact Policy

- 运行期证据仅保留在 `tmp/eval-runs/121/`，不提交。
