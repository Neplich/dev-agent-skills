# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-001-sync-feature-api`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- Branch fixture commit: `71bbb09`

## Latest Result

**PASS** — 最终隔离 fresh judge 对 5 条 assertions 全部判定 PASS。with-skill 仅更新 `docs/site/api/search.md`，从代码与 contract test 写入 `GET /api/search`、必填 `q`、可选 `limit` 和 400 `invalid_query`，保留 database 页面与人工 change-map 条目，并将更新页保持为 `last_verified_version: unverified`。

## With-Skill Behavior

- 按 handoff、Approved PRD、Confirmed TRD、实施计划、actual diff、路由、schema 和 contract test 限定为单页 API 同步。
- 旧 `POST /v1/find` 与 JSON body 声明被当前事实替换；页面补入 schema 与 contract test 的 `related_code`，且未猜写缺少实现证据的认证行为。
- `src/api/**` 映射原本已是稳定合并态，因此 change-map zero-diff；`plugins/manual/**` 的 required docs、trigger 和 exclude 完整保留。
- 明确 API-only MVP 边界，不声称 database、design、ops、product 或 release 文档已自动同步。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，使用相同原始 prompt 与 fixture，新生成且未接触 skill 文档或 Agent README。
- baseline 同样正确提取 API 路径、参数与错误，且保留 database 页面和人工 change-map。
- baseline 把 `last_verified_version` 擅自写为 `v0.9.0`，违反 sync 后等待审计的 `unverified` 契约；对 API-only MVP 边界也只从未改其他页面间接体现，未明确声明。

## Failures

- 无 assertion failure。
- 首个 judge 读取了当前 eval 目录外的 QA router、memory 和原 fixture，结论只保留为 tmp 诊断。最终 judge 使用复制到运行目录内的 pristine `fixture_snapshot`，明确禁止读取外部文件，并独立得到本次 5/5 PASS。
- 隔离 fixture 未安装 pytest/FastAPI，judge 未能重新执行 contract test；结论基于 actual diff、路由、schema、测试断言与产物的静态交叉核验。该限制不改变本 eval 的 assertion 结果。

## Next Steps

- 保留本结果；同步盖章规则、API-only 边界或 change-map 合并规则变化时重跑此 eval。

## Runtime Artifact Policy

- 本次 transcripts、workspace 副本、pristine fixture snapshot 和 verdicts 仅位于 `tmp/eval-runs/118/eval-001-sync-feature-api/`，不提交到 git。
