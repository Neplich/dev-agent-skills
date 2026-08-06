# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-011-deployment-three-class-backfill`
- Review context: issue #161 fresh paired rerun and fresh Codex judge

## Test Set / Fixture Version

- Fixture: issue #161 three-class deployment evidence set after template-consumer and recursive-link corrections
- Actual validation date: `2026-07-22`

## Latest Result

- Overall result: PASS
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `PARTIAL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `creates_three_class_page_tree` | PASS | PASS | 两条 lane 均生成完整 10 文件页面树；根索引分别提供三类部署导航（with: `docs/site/ops/deployment/index.md:12-21`；without: `.../index.md:12-19`）。 |
| `cross_checks_environment_reference` | PASS | FAIL | with 的环境表包含用途、类型/约束、必填性、默认值、安全示例、适用方式、Secret 属性和证据，并明确 `LEGACY_TIMEOUT` 未消费且已废弃（with: `environment-reference.md:12-22`）；without 仅列变量、必填性、默认值和使用方，未交叉记录 `.env.example`、测试证据或 `LEGACY_TIMEOUT`（without: `environment-reference.md:12-20`）。 |
| `separates_class_specific_contracts` | PASS | FAIL | with 为 Development、Docker、Kubernetes/Helm 分别提供前置、命令、成功标准、回滚和故障处理，并包含各自证据范围（with: 三类 `index.md` 及子页）；without 的 Development、Docker、Kubernetes 主页主要只有简短事实和导航，缺少完整类别合同（without: `development/index.md:10-12`、`docker/index.md:10-14`、`kubernetes-helm/index.md:10-14`）。 |
| `maps_each_class_atomically` | PASS | FAIL | with 的 `change-map.yaml` 将 `scripts/dev/**`、`Dockerfile`、`deploy/docker/**`、`deploy/helm/**` 及共享配置映射到完整页面树，并保留 `custom_owner_field`（with: `change-map.yaml:6-32`）；without 的映射只覆盖各类部分页面，未将 Docker/Helm/共享配置原子映射到根索引、环境参考和导航（without: `change-map.yaml:6-36`）。 |
| `runs_nested_docs_checks` | PASS | NOT_EXERCISED | 两条 lane 实际运行 `npm run test:docs` 均为 3/3，通过页面树、导航和内部链接检查；两者页面均保持 `last_verified_version: unverified`。但 with 结果明确等待 docs audit / 版本确认（with: `result.txt:7-10`），without 只有“测试 3/3”记录，没有 `docs-agent:docs-audit` handoff 证据（without: `result.txt:14`）。 |

未满足断言（with/without 任一 FAIL）：``cross_checks_environment_reference``、``separates_class_specific_contracts``、``maps_each_class_atomically``

基础设施说明：基础设施依赖缺失（`runs_nested_docs_checks`）→ 已转 NOT_EXERCISED；对应断言不构成 skill 行为回归。



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Cross-checked env examples, settings/tests, Compose, values and actual template consumers; treated `LEGACY_TIMEOUT` and unconsumed values explicitly instead of inventing runtime mappings.
- Kept Development, Docker and Kubernetes/Helm commands, images, rollback and troubleshooting separate; all class indexes link their authoritative child pages.
- Preserved unrelated/unknown map data, left pages `unverified`, and returned the `docs-agent:docs-audit` handoff blocked on a confirmed target version.

## Fresh Without-Skill Baseline

- Source: fresh lane from the same corrected pristine fixture and prompt; it did not read the target skill, Agent README, comparisons or with-skill output.
- It passed 3/3 structural tests, but its environment table omitted required contract fields, treated Helm `service.port` as `APP_PORT`, treated an unconsumed value as effective, and omitted the formal `docs-agent:docs-audit` handoff.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- No with-skill assertion failures.
- Runtime provenance used lane transcripts and reports; a separate immutable input manifest was not retained.

## Next Steps

- Keep this PASS and retain the stricter internal-link test and template-consumer evidence boundary.

## Runtime Artifact Policy

- Paired lanes, transcripts, reports, generated pages and judge verdict remain under `tmp/eval-runs/issue-161-rerun/` and are not submitted.
- Only this comparison is durable.
