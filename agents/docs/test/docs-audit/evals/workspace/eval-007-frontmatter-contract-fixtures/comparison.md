# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-007-frontmatter-contract-fixtures`

## Test Set / Fixture Version

- Fixture: `frontmatter-contract-v1`
- Contract: `agents/docs/skills/docs-agent/_internal/_shared/frontmatter-contract.md`

## Latest Result

**PENDING** — pending fresh validation；将在 B2 使用同一 prompt 和 fixture 重新生成 with-skill 与 without_skill baseline 后给出结论。

## With-Skill Behavior

- Pending fresh validation（B2 执行）。

## Without-Skill Baseline

- Pending fresh validation（B2 执行），不得复用历史 baseline。

## Failures

- 尚未执行模型 eval，当前无可报告的行为判定。

## Next Steps

- 在 B2 执行 fresh subagent validation，并用本次新生成的 baseline 更新此文件。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
