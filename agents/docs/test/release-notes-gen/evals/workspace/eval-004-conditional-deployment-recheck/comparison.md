# Skill Eval Comparison

## Evaluation Target

- Skill: `release-notes-generator` → `release-notes-gen`（改名后新入口待重跑验证）
- Eval: `eval-004-conditional-deployment-recheck`
- Review context: issue #162 fresh paired validation

## Test Set / Fixture Version

- Fixture: issue #162 scenario evidence in this workspace
- Validation date: 2026-07-22
- Execution cleanup: all declared runtime paths were absent from pristine scratch fixtures

## Latest Result

- Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `skips_content_only_recheck` | PASS | PASS | with_skill 明确写出“Content-only…不触发部署级复核”；without_skill 写出“纯文案/错字变更：不影响运行时，无需部署”。 |
| `rechecks_material_release_surface` | FAIL | FAIL | 两条 lane 都识别出新增 Internal 导航会改变生成输出和启动路径；但 with_skill 仅说“需重新验证”，没有产出共享状态/检查复用证据；without_skill 仅分类为需要部署，也没有证明复用共享检查。两者均未复制新清单。 |

未满足断言（with/without 任一 FAIL）：``rechecks_material_release_surface``



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- content-only 保留状态；runtime change 复用唯一共享协议且不复制 checklist。
- Candidate source: fresh `tmp/eval-runs/issue-162/with_skill/eval-004-conditional-deployment-recheck/candidate-output.md`.

## Fresh Without-Skill Baseline

- PARTIAL (1/2)；识别触发差异，但未声明共享状态/协议复用。
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
