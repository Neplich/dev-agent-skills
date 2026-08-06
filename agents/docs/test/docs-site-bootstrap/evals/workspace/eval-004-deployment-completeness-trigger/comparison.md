# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-site-bootstrap`
- Eval: `eval-004-deployment-completeness-trigger`
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
| `classifies_first_bootstrap_integrated` | PASS | PASS | 两条 `result.txt` 均依据 `evidence.md`，列出 Public/Internal、Docker、Tag CI、Compose、Helm、健康检查、TLS 和网络认证，并说明仅做只读核验、未重复执行发布部署。 |
| `asks_first_bootstrap_choice` | FAIL | FAIL | 两条产物均仅说“补齐”缺失的 Dockerfile、CI、Compose、Helm 配置，没有明确询问三选一：全部纳入、独立托管 `not_applicable`、暂缓并保留 blocker。 |
| `rechecks_rebootstrap_drift` | FAIL | FAIL | 两条产物都识别了 `.generated/internal` → `.generated/private` 的路径漂移，但没有判为 `partial`，也没有重新询问是否进入 PM → DevOps 补齐链路。 |
| `preserves_authorization_boundary` | PASS | PASS | 两条产物均明确“仅获准只读检查和文档修改”，且未执行或授权 push、镜像发布、部署；没有让 Docs 明确修改 Docker、CI/CD、Compose 或 Helm。 |

未满足断言（with/without 任一 FAIL）：``asks_first_bootstrap_choice``、``rechecks_rebootstrap_drift``



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 正确区分首次 integrated、首次 not_integrated、re-bootstrap partial 漂移，给出三选一和授权边界。
- Candidate source: fresh `tmp/eval-runs/issue-162/with_skill/eval-004-deployment-completeness-trigger/candidate-output.md`.

## Fresh Without-Skill Baseline

- BLOCKED (0/4)；识别事实但缺 durable commit trigger、稳定状态、完整三选一与 PM/DevOps 链路。
- The same prompt and pristine fixture were used; no historical baseline, target skill, Agent README, shared skill-map, old comparison, or with-skill output was used to compose it.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- baseline 缺少共享 closeout 协议。
- No with-skill assertion failure or runner/credential blocker.

## Next Steps

- Keep this regression case; strengthen fixture ambiguity later where the baseline already passes.

## Runtime Artifact Policy

- Runtime candidates, copied fixtures, verdict, status, and diagnostics remain under `tmp/eval-runs/issue-162/` and are not committed.
- Only this durable comparison, eval definition, metadata, and fixture evidence are submitted.
