# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-014-conditional-deployment-recheck`
- Review context: issue #162 fresh paired validation

## Test Set / Fixture Version

- Fixture: issue #162 scenario evidence in this workspace
- Validation date: 2026-07-22
- Execution cleanup: all declared runtime paths were absent from pristine scratch fixtures

## Latest Result

- Overall result: PASS (partial coverage)
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `PARTIAL`
- without_skill：Behavior `PASS` / Coverage `PARTIAL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| preserves_state_for_no_surface_change | NOT_EXERCISED | NOT_EXERCISED | 两条 lane 的 `evidence.md` 仅说明 `version-only` 只改 verification metadata、无构建或发布面变化；没有记录既有完整性状态被保留或重新检查后的状态。 |
| refreshes_shared_state_for_material_change | NOT_EXERCISED | NOT_EXERCISED | 两条 lane 仅记录 `build-target-change` 改变 `build:internal` 的生成产物和 runtime entry；没有共享检查复用、状态刷新、第二协议或部署资产未修改的实际产物证据。 |

本轮无 FAIL 断言。


**PASS (2/2 assertions)** — fresh Codex subagent semantic review.

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- version-only 保持状态；build/runtime change 刷新共享状态，不建第二协议、不改部署资产。
- Candidate source: fresh `tmp/eval-runs/issue-162/with_skill/eval-014-conditional-deployment-recheck/candidate-output.md`.

## Fresh Without-Skill Baseline

- PARTIAL (1/2)；识别是否重检，但未声明共享协议与状态刷新契约。
- The same prompt and pristine fixture were used; no historical baseline, target skill, Agent README, shared skill-map, old comparison, or with-skill output was used to compose it.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- baseline 缺共享协议复用语义。
- No with-skill assertion failure or runner/credential blocker.

## Next Steps

- Keep this regression case; strengthen fixture ambiguity later where the baseline already passes.

## Runtime Artifact Policy

- Runtime candidates, copied fixtures, verdict, status, and diagnostics remain under `tmp/eval-runs/issue-162/` and are not committed.
- Only this durable comparison, eval definition, metadata, and fixture evidence are submitted.
