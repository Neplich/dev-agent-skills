# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-015-flat-hierarchy-migration-proposal`
- Review context: issue #225 fixture and eval definition

## Test Set / Fixture Version

- Fixture: six stable flat API pages across three confirmed feature domains, plus one new conversation-messages delivery
- Fixture version: issue #225 initial definition

## Latest Result

- Behavior result: BLOCKED
- Coverage result: BLOCKED
- Reason: eval 定义随 issue #225 新增，fresh Codex subagent validation 将在同一轮变更中由维护者侧执行后回填。

Overall result: BLOCKED

## With-Skill Behavior

- 待运行。

## Fresh Without-Skill Baseline

- 待运行。

## Failures

- fresh with-skill lane 与 fresh without-skill baseline 均尚未执行。

## Next Steps

- 由维护者侧使用同一 prompt 和 pristine fixture 执行 fresh Codex subagent validation，并回填两个 lane 的行为与 assertion 覆盖结论。

## Runtime Artifact Policy

- `with_skill/`、`without_skill/`、transcript、verdict、timing、diagnostics 与 `sync-report.md` 均为运行期产物，不提交到 git。
- 仅人工确认后的最新 `comparison.md` 作为 durable result 提交。
