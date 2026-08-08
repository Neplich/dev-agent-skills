# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-011-deployment-three-class-backfill`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `4d8408c1113f0b188f486ff52a1805928dda107a5b4bcef41d15ff086a7d524c` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-011-deployment-three-class-backfill`.
- Fixture SHA-256: `4d8408c1113f0b188f486ff52a1805928dda107a5b4bcef41d15ff086a7d524c`
- Prompt SHA-256: `bed66a02e7102d84cc8988d8318b854a858b57d12888f0168cc60650b6d45cd2`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `79b2ff102fa24fa224c9f24f44f3e648a1ae7eb9a7a10e639d8675db4454120a`
- Skill overlay SHA-256: `52a3ba7ee2d9485acf003417b40e0d0ca2ab263cbadde98fac58250b6c2a9778`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `75d9816433885deaa537c3684a33cbf77a210bf3435c193880901b7467aafb6d`
- Metadata SHA-256: `bb3778b5e21b04d8e648f9284877b0cbdf7e072e8deab05774e592a881557e0f`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_three_class_page_tree` | PASS | With-skill snapshot contains the required 10-page tree, and the root page provides status, selection guidance, and navigation. |
| `cross_checks_environment_reference` | FAIL | The table covers the three active variables with the requested fields, but LEGACY_TIMEOUT is only mentioned in prose rather than being recorded as an individual parameter row. |
| `separates_class_specific_contracts` | FAIL | The class pages are separated and include prerequisites, commands, success criteria, rollback, and troubleshooting, but the Docker page does not document network or migration boundaries/handling required by the assertion. |
| `maps_each_class_atomically` | PASS | The snapshot maps the requested code globs to class pages, retains the unrelated src/product entry and custom_owner_field, and includes the page and change-map updates. |
| `runs_nested_docs_checks` | NOT_EXERCISED | The candidate claims npm run test:docs passed, but the supplied raw fixture does not include the host test script or an independently verifiable execution result. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bed66a02e7102d84cc8988d8318b854a858b57d12888f0168cc60650b6d45cd2; fixture_sha256=4d8408c1113f0b188f486ff52a1805928dda107a5b4bcef41d15ff086a7d524c; output_sha256=a3212f4528fce4b5ede58911a157d257ea03f3352b3527f92146ece6c03dceae; snapshot_sha256=da35c6f32b5cd06d85ebc2534582220c56163f4446257293cb2d0b3510f227af
- Behavior: Produced a detailed three-class documentation tree with stronger source tracing and explicit uncertainty handling, but omitted the LEGACY_TIMEOUT table row and Docker network/migration coverage; docs-check execution is not independently verifiable.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bed66a02e7102d84cc8988d8318b854a858b57d12888f0168cc60650b6d45cd2; fixture_sha256=4d8408c1113f0b188f486ff52a1805928dda107a5b4bcef41d15ff086a7d524c; output_sha256=697eb3ad6eee117765fc4e4a4efb6807b25a4400a491fd15b86c93181079e5c1; snapshot_sha256=5a1eb13e46334dd8fe1c2b5fe4cdbe7b4a7c3489af955b483c86655df78aaed1
- Behavior: Produced the requested page tree and change-map entries, but with less granular cross-source documentation and weaker evidence-boundary handling.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- Environment reference does not record LEGACY_TIMEOUT as an individual table entry.
- Docker class documentation omits required network and migration coverage.
- Next: Add a LEGACY_TIMEOUT row with its status and evidence.
- Next: Document Docker network and migration behavior or explicitly record their absence in the confirmed evidence.
- Next: Provide the host docs-test script or captured test output for independent verification.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

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
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `creates_three_class_page_tree` | PASS | PASS | 两条 lane 均生成完整 10 文件页面树；根索引分别提供三类部署导航（with: `docs/site/ops/deployment/index.md:12-21`；without: `.../index.md:12-19`）。 |
| `cross_checks_environment_reference` | PASS | FAIL | with 的环境表包含用途、类型/约束、必填性、默认值、安全示例、适用方式、Secret 属性和证据，并明确 `LEGACY_TIMEOUT` 未消费且已废弃（with: `environment-reference.md:12-22`）；without 仅列变量、必填性、默认值和使用方，未交叉记录 `.env.example`、测试证据或 `LEGACY_TIMEOUT`（without: `environment-reference.md:12-20`）。 |
| `separates_class_specific_contracts` | PASS | FAIL | with 为 Development、Docker、Kubernetes/Helm 分别提供前置、命令、成功标准、回滚和故障处理，并包含各自证据范围（with: 三类 `index.md` 及子页）；without 的 Development、Docker、Kubernetes 主页主要只有简短事实和导航，缺少完整类别合同（without: `development/index.md:10-12`、`docker/index.md:10-14`、`kubernetes-helm/index.md:10-14`）。 |
| `maps_each_class_atomically` | PASS | FAIL | with 的 `change-map.yaml` 将 `scripts/dev/**`、`Dockerfile`、`deploy/docker/**`、`deploy/helm/**` 及共享配置映射到完整页面树，并保留 `custom_owner_field`（with: `change-map.yaml:6-32`）；without 的映射只覆盖各类部分页面，未将 Docker/Helm/共享配置原子映射到根索引、环境参考和导航（without: `change-map.yaml:6-36`）。 |
| `runs_nested_docs_checks` | PASS | FAIL | 两条 lane 实际运行 `npm run test:docs` 均为 3/3，通过页面树、导航和内部链接检查；两者页面均保持 `last_verified_version: unverified`。但 with 结果明确等待 docs audit / 版本确认（with: `result.txt:7-10`），without 只有“测试 3/3”记录，没有 `docs-agent:docs-audit` handoff 证据（without: `result.txt:14`）。 |

未满足断言（with/without 任一 FAIL）：``cross_checks_environment_reference``、``separates_class_specific_contracts``、``maps_each_class_atomically``、``runs_nested_docs_checks``



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Cross-checked env examples, settings/tests, Compose, values and actual template consumers; treated `LEGACY_TIMEOUT` and unconsumed values explicitly instead of inventing runtime mappings.
- Kept Development, Docker and Kubernetes/Helm commands, images, rollback and troubleshooting separate; all class indexes link their authoritative child pages.
- Preserved unrelated/unknown map data, left pages `unverified`, and returned the `docs-agent:docs-audit` handoff blocked on a confirmed target version.

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

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
