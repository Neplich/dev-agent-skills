# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-006-preserve-independent-hosting`
- Review context: issue #162 fresh paired validation

## Test Set / Fixture Version

- Fixture: issue #162 scenario evidence in this workspace
- Validation date: 2026-07-22
- Execution cleanup: all declared runtime paths were absent from pristine scratch fixtures

## Latest Result

- Overall result: PASS
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| preserves_not_applicable_evidence | PASS | FAIL | with_skill 的 `docs/site/DEPLOYMENT.md` 明确写出 `not_applicable`，引用 `../../evidence.md`，覆盖 Public/Internal 两个变体，并说明变化时进入 PM → DevOps → Docs 路由；without_skill 仅描述“不引入图片存储依赖”，未明确 `not_applicable`、证据路径或下一 owner。 |
| does_not_open_devops_handoff | PASS | PASS | with_skill 明确写出“DevOps handoff: not required”，仅在托管模型变化时重新路由；without_skill 也未生成 DevOps handoff，且当前证据确认静态托管仍有效。 |

未满足断言（with/without 任一 FAIL）：`preserves_not_applicable_evidence`



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 保留 not_applicable、证据、Public/Internal、维护者决定和下一 owner，有效时不生成 DevOps handoff。
- Candidate source: fresh `tmp/eval-runs/issue-162/with_skill/eval-006-preserve-independent-hosting/candidate-output.md`.

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- PARTIAL (1/2)；保留独立托管决定但未使用稳定 not_applicable 状态。
- The same prompt and pristine fixture were used; no historical baseline, target skill, Agent README, shared skill-map, old comparison, or with-skill output was used to compose it.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- baseline 缺少稳定跨角色状态。
- No with-skill assertion failure or runner/credential blocker.

## Next Steps

- Keep this regression case; strengthen fixture ambiguity later where the baseline already passes.

## Runtime Artifact Policy

- Runtime candidates, copied fixtures, verdict, status, and diagnostics remain under `tmp/eval-runs/issue-162/` and are not committed.
- Only this durable comparison, eval definition, metadata, and fixture evidence are submitted.
