# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-008-deployment-ops-upgrade`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `79929cac2d8a0cd7566617f637009899090f1d90d4639070d26aca346f9cfe79` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-008-deployment-ops-upgrade`.
- Fixture SHA-256: `79929cac2d8a0cd7566617f637009899090f1d90d4639070d26aca346f9cfe79`
- Prompt SHA-256: `47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `79b2ff102fa24fa224c9f24f44f3e648a1ae7eb9a7a10e639d8675db4454120a`
- Skill overlay SHA-256: `52a3ba7ee2d9485acf003417b40e0d0ca2ab263cbadde98fac58250b6c2a9778`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `7fe3c7ecf4038349101f98fb6f2ef19330f01c150bee2276a165994129650157`
- Metadata SHA-256: `77c250a8dd394ec8e7b47c067343be0f3108a736b624b4ce31343031983a7685`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_executed_deployment_evidence` | PASS | with_skill 文档以 Compose、执行结果和环境差异为依据，记录 exit 0、healthy、HTTP 200/ok，并明确未执行 Kubernetes/Helm。 |
| `writes_current_ops_upgrade_rollback` | PASS | Docker 页面记录启动、v1.4.2 升级、/healthz HTTP 200/ok 标准及 v1.4.1 回滚后检查；镜像页记录默认镜像和 pull 证据。 |
| `does_not_promote_plan_to_current_state` | PASS | 明确 Kubernetes/Helm 仅为未执行计划、当前不支持，未提供可执行现状命令。 |
| `writes_current_deployment_tree_atomically` | PASS | 四个新页面均为 last_verified_version: unverified；链接、change-map 四页覆盖及既有 exclude 均存在，git 状态显示未修改无关页面。 |
| `runs_ops_host_checks_and_handoffs` | FAIL | 输出仅称文档测试 76/76 通过，同时明确 strict affected check 因 committed base 不确定而阻塞；未提供真实 npm run test:docs 全量通过证据，也未记录 handoff docs-agent:docs-audit。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=79929cac2d8a0cd7566617f637009899090f1d90d4639070d26aca346f9cfe79; output_sha256=9019016a19653f70cb0818aeb5e6f3cc93ebaf6db66cb471f86a75ad35c0adba; snapshot_sha256=9f689dddc4182913439d236cbbca27832d0c3bc43d265ebab1272a9c8c7ce287
- Behavior: 部署文档内容、证据边界、链接和未支持范围处理正确；测试链存在 strict check 阻塞，且缺少要求的 docs-agent handoff。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=79929cac2d8a0cd7566617f637009899090f1d90d4639070d26aca346f9cfe79; output_sha256=9768149d6b06621cf21cc988d9ca817dbd59dcc5e065d9c8b58fc93f69ba3c3f; snapshot_sha256=a16dd31eb47aa5618662b03b7fe95dd8688c6fb88834581c0e166daead3572b4
- Behavior: 正确概述了部署文档内容和范围，但未提供宿主检查或 handoff 证据，且页面版本元数据为 v1.4.2。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未证明 npm run test:docs 全量通过，并未执行或记录 docs-agent:docs-audit handoff。
- Next: 完成并记录 npm run test:docs 通过结果，再执行 docs-agent:docs-audit handoff。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge package, verdict, timing, and diagnostics remain under ignored `tmp/eval-runs/` or short-lived CI artifacts and are not committed.
- This durable comparison retains only the reviewable summary and superseded history.

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
- Eval: `eval-008-deployment-ops-upgrade`
- Review context: PR #166 second-round P2 fresh paired validation and fresh Codex judge

## Test Set / Fixture Version

- Fixture: current deployment-verification evidence set with confirmed `ops/deployment/` Docker page tree, shared environment reference, Ops navigation, and `deploy/**` change-map scope
- Evidence set: confirmed deployment handoff, TRD surface, `.env.example`, Compose configuration, executed deployment results, environment differences, and future-only Kubernetes/Helm plan
- Actual validation date: `2026-07-22`

## Latest Result

- Behavior result: `PASS`（with）/ `PASS`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `PARTIAL`（with）/ `PARTIAL`（without）— 依赖缺失导致宿主检查与 handoff 未执行
- Overall result: BLOCKED
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `PARTIAL`
- without_skill：Behavior `PASS` / Coverage `PARTIAL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| uses_executed_deployment_evidence | PASS | PASS | 两条 lane 均以 `deploy/compose.yaml` 和 `.eval/deployment-results.md` 为依据，记录 development/staging 启动 exit 0、healthy、`/healthz` HTTP 200 及回滚结果；页面正文明确引用这些文件（with：`deployment/index.md:39-49`；without：`deployment/index.md:28-30`）。 |
| writes_current_ops_upgrade_rollback | PASS | PASS | 两条 lane 均记录 Compose 启动/升级、`/healthz` 200、回滚到 `v1.4.1` 并复查健康状态；镜像页记录默认 `registry.example/ai-hub:v1.4.2`（with：`docker/image-sources.md:21-44`；without：`docker/image-sources.md:16-27`）。 |
| does_not_promote_plan_to_current_state | PASS | PASS | 两条 lane 都明确 Kubernetes/Helm 只有未执行计划，不作为当前支持路径（with：`deployment/index.md:21-24`；without：`deployment/index.md:24-26`）。 |
| writes_current_deployment_tree_atomically | PASS | PASS | 两条 lane 均生成四个要求页面，Ops、部署根页和 Docker 页有对应链接；`deploy/**` change-map 覆盖四页并保留 `deploy/examples/**` exclude；新页面均为 `last_verified_version: unverified`，未新增 product/design/database/release-notes 文件。 |
| runs_ops_host_checks_and_handoffs | NOT_EXERCISED | NOT_EXERCISED | 两条 lane 的 `npm run test:docs` 都因缺少 `fast-glob` 未启动完成，后置 handoff 因而未执行；这是 runner 依赖阻塞，不是 skill 行为失败。 |

未触发断言：`runs_ops_host_checks_and_handoffs`。

基础设施阻塞说明：依赖缺失（fast-glob 等）；对应断言不构成 skill 行为回归。



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

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

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

- 安装锁定依赖后重新执行 paired eval 与独立 judge；宿主检查和 handoff 成功前保持 `BLOCKED`。
- On a future rerun, use absolute `--output-last-message` paths per lane so both transcript summaries remain available to the judge.

## Runtime Artifact Policy

- Pristine input, paired lane outputs, reports, dependencies, CLI streams, transcript summary, and judge verdict remain under `tmp/eval-runs/issue-161-review-round2-20260722-2002/` and are not submitted.
- Only this comparison is durable; no generated formal page, report, transcript, verdict, `node_modules`, or diagnostics file is committed.
