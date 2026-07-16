# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-003-route-release-audit`

## Test Set / Fixture Version

- Fixture: `docs-audit-route-v2`
- Source update: audit routing enabled

## Latest Result

**NOT RUN** — 本轮只把 router eval 定义对齐到已启用的 `docs-audit` handoff；fresh with-skill / without-skill validation 留待 docs-audit eval 补齐时集中执行。

## With-Skill Behavior

- 预期保留等效 release 入口证据并选择 `docs-audit`。
- 预期只指向 specialist gate，不复制两层审计、三态或统一盖章协议。

## Without-Skill Baseline

- 本轮未生成新的 baseline；不得复用旧 blocked 场景的 baseline 作为当前 handoff 场景证据。

## Failures

- Fresh with-skill / without-skill validation 尚未执行。

## Next Steps

- 与 docs-audit 六组 fixture 一并运行 fresh validation，并把最新结论回填到本文件。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
