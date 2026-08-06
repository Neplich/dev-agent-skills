# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-014-existing-site-deployment-recheck`
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
| reports_existing_site_integrated | PASS | PASS | with_skill 的 `result.txt` 报告 Site A Public/Internal 构建、镜像、Compose/Helm、健康检查和访问控制“证据显示完整”；without_skill 报告 Site A“部署完整”，均列出证据且未重复执行 DevOps。 |
| detects_partial_variant_coverage | PASS | PASS | 两条 lane 均明确列出 Site B：Public 有 Docker/tag workflow/Compose/Helm，Internal 缺少镜像任务、启动拓扑等，并判定为部分完整。 |
| returns_gap_to_pm_read_only | FAIL | FAIL | 两条 lane 均声明只读且未修改 Dockerfile、workflow、Compose 或 Helm；但均未询问或明确返回“由 pm-agent 生成 repo-wide deployment handoff”。 |

未满足断言（with/without 任一 FAIL）：`returns_gap_to_pm_read_only`



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 老站完整时保持 integrated 且不重放 DevOps；仅 Public 覆盖时判 partial 并只读返回 PM。
- Candidate source: fresh `tmp/eval-runs/issue-162/with_skill/eval-014-existing-site-deployment-recheck/candidate-output.md`.

## Fresh Without-Skill Baseline

- PARTIAL (2/3)；识别完整/部分覆盖，但直接建议 DevOps，未形成 PM repo-wide 回流。
- The same prompt and pristine fixture were used; no historical baseline, target skill, Agent README, shared skill-map, old comparison, or with-skill output was used to compose it.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- baseline 未满足 PM 回流和完整角色边界。
- No with-skill assertion failure or runner/credential blocker.

## Next Steps

- Keep this regression case; strengthen fixture ambiguity later where the baseline already passes.

## Runtime Artifact Policy

- Runtime candidates, copied fixtures, verdict, status, and diagnostics remain under `tmp/eval-runs/issue-162/` and are not committed.
- Only this durable comparison, eval definition, metadata, and fixture evidence are submitted.
