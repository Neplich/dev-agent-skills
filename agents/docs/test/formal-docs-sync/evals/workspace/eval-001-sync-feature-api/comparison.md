# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-001-sync-feature-api`

## Test Set / Fixture Version

- Fixture: `issue-121-s2-final`
- Run date: `2026-07-19`

## Latest Result

**PASS** — 最终 fresh judge 判定 with-skill 5/5 assertions 通过；without-skill baseline 4/5。

## With-Skill Behavior

- 仅加载 API 类型模块，按已确认范围同步 `docs/site/api/search.md` 与映射。
- 页面保持 `last_verified_version: unverified`，人工映射与无关页面未受影响。
- 宿主 `npm run test:docs` 真实通过。

## Without-Skill Baseline

- 同 prompt、同 pristine fixture 全新生成，未读取 Agent 或 skill 文档。
- baseline 完成 API 同步，但未建立五类型能力下的单类型 progressive-loading 边界。

## Failures

- with-skill 无 assertion failure。

## Next Steps

- 本结果可保留；skill、fixture 或断言变化时重新执行 fresh validation。

## Runtime Artifact Policy

- transcripts、workspace 副本与 judge verdict 仅位于 `tmp/eval-runs/121/`，不提交。
