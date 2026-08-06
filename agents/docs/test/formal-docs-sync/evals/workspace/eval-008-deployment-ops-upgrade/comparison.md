# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-008-deployment-ops-upgrade`
- Review context: PR #166 second-round P2 fresh paired validation and fresh Codex judge

## Test Set / Fixture Version

- Fixture: current deployment-verification evidence set with confirmed `ops/deployment/` Docker page tree, shared environment reference, Ops navigation, and `deploy/**` change-map scope
- Evidence set: confirmed deployment handoff, TRD surface, `.env.example`, Compose configuration, executed deployment results, environment differences, and future-only Kubernetes/Helm plan
- Actual validation date: `2026-07-22`

## Latest Result

- Overall result: BLOCKED
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| uses_executed_deployment_evidence | PASS | PASS | 两条 lane 均以 `deploy/compose.yaml` 和 `.eval/deployment-results.md` 为依据，记录 development/staging 启动 exit 0、healthy、`/healthz` HTTP 200 及回滚结果；页面正文明确引用这些文件（with：`deployment/index.md:39-49`；without：`deployment/index.md:28-30`）。 |
| writes_current_ops_upgrade_rollback | PASS | PASS | 两条 lane 均记录 Compose 启动/升级、`/healthz` 200、回滚到 `v1.4.1` 并复查健康状态；镜像页记录默认 `registry.example/ai-hub:v1.4.2`（with：`docker/image-sources.md:21-44`；without：`docker/image-sources.md:16-27`）。 |
| does_not_promote_plan_to_current_state | PASS | PASS | 两条 lane 都明确 Kubernetes/Helm 只有未执行计划，不作为当前支持路径（with：`deployment/index.md:21-24`；without：`deployment/index.md:24-26`）。 |
| writes_current_deployment_tree_atomically | PASS | PASS | 两条 lane 均生成四个要求页面，Ops、部署根页和 Docker 页有对应链接；`deploy/**` change-map 覆盖四页并保留 `deploy/examples/**` exclude；新页面均为 `last_verified_version: unverified`，未新增 product/design/database/release-notes 文件。 |
| runs_ops_host_checks_and_handoffs | FAIL | FAIL | 两条 lane 的 `result.txt` 都明确记载完整 `npm run test:docs` 因 `fast-glob` 依赖不完整而阻塞；未发现成功测试结果或 `docs-agent:docs-audit` handoff 产物。该断言要求“真实通过”并完成 handoff，因此不是 NOT_EXERCISED。 |

未满足断言（with/without 任一 FAIL）：`runs_ops_host_checks_and_handoffs`

基础设施阻塞说明：；依赖缺失（fast-glob 等）；对应断言不构成 skill 行为回归。



## Assertions
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `uses_executed_deployment_evidence`: PASS. Current claims came from `deploy/compose.yaml`, `.env.example`, recorded command exits and health results, and confirmed environment differences rather than the TRD or plan alone.
- `writes_current_ops_upgrade_rollback`: PASS. The Docker runbook records development/staging startup, the `v1.4.2` pull and upgrade, `/healthz` HTTP 200 success, and rollback to `v1.4.1`; `docker/image-sources.md` owns the image coordinates and evidence boundary.
- `does_not_promote_plan_to_current_state`: PASS. Kubernetes/Helm remains an unsupported, unexecuted plan with no page or placeholder command.
- `writes_current_deployment_tree_atomically`: PASS. All four required pages exist and link to their authorities; the existing Ops navigation and `deploy/**` mapping cover them while preserving `deploy/examples/**`; all new pages remain `unverified`, and unrelated sections are unchanged.
- `runs_ops_host_checks_and_handoffs`: PASS. The judge reran `npm run test:docs` in both lanes, each exiting `0` with 76/76 tests; the with-skill report hands off to `docs-agent:docs-audit` without executing deployment and blocks version stamping until a maintainer confirms `target_release_version`.

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Used `doc_type: ops` throughout the deployment tree and produced the full environment-reference contract: type, requiredness, default, constraints, applicable class, safe example, sensitivity, activation timing, and evidence.
- Classified Development as out-of-scope, Docker as supported, and Kubernetes/Helm as unsupported; it also named missing image provenance, architecture, authentication, offline-source, logging, and data-check evidence without inventing commands.
- Kept the legacy single-page shape absent and treated the four pages, internal links, Ops navigation, and change map as one confirmed atomic scope.
- Preserved the formal `docs-agent:docs-audit` gate: missing confirmed release context leaves the handoff blocked and all pages `last_verified_version: unverified`.

## Fresh Without-Skill Baseline

- Source: a fresh lane copied from the same pristine input and run with the same `eval_metadata.json` prompt; it was instructed not to read the target skill, Agent README, eval definitions, comparison, with-skill output, or historical runs.
- The baseline also generated the four-page tree, recorded the executed Docker upgrade and rollback, excluded Kubernetes/Helm, and passed 76/76 tests.
- It was weaker than the skill lane: the root used `doc_type: landing`, the environment table omitted the complete ops contract fields, deployment-class and missing-evidence reporting was unstructured, and the `docs-agent:docs-audit` handoff did not explicitly enforce the maintainer-confirmed-version blocked state.

## Positioning Against Eval-011/012/013

- Eval-008 remains the deployment-verification regression for synchronizing already executed Docker upgrade facts into the current page tree; it no longer accepts `docs/site/ops/ai-hub-upgrade.md`.
- Eval-011 covers a full three-class existing-system backfill, eval-012 covers class-local blocking when Kubernetes/Helm evidence is missing, and eval-013 covers atomic migration from an existing aggregate deployment page.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- No with-skill assertion failures.
- The `codex exec` lane streams and reports were generated and judged, but the with-skill last-message transcript path was resolved outside its intended lane and was overwritten by the baseline run. This reduces transcript-level provenance but does not change the file-level same-input proof, independent test reruns, or assertion result.
- The strong confirmed fixture lets the baseline satisfy the five core assertions, so this eval demonstrates correctness more strongly than skill-versus-baseline discrimination.

## Next Steps

- Keep this PASS and retain eval-008 as the focused executed-Docker-upgrade deployment-verification regression.
- On a future rerun, use absolute `--output-last-message` paths per lane so both transcript summaries remain available to the judge.

## Runtime Artifact Policy

- Pristine input, paired lane outputs, reports, dependencies, CLI streams, transcript summary, and judge verdict remain under `tmp/eval-runs/issue-161-review-round2-20260722-2002/` and are not submitted.
- Only this comparison is durable; no generated formal page, report, transcript, verdict, `node_modules`, or diagnostics file is committed.
