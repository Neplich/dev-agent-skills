# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-012-deployment-class-evidence-gap`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1de8258a9da58346af1c991b6a49dbec33d719a345dcdc2748bb8b2eeb45a0e0` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-012-deployment-class-evidence-gap`.
- Fixture SHA-256: `1de8258a9da58346af1c991b6a49dbec33d719a345dcdc2748bb8b2eeb45a0e0`
- Prompt SHA-256: `d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `79b2ff102fa24fa224c9f24f44f3e648a1ae7eb9a7a10e639d8675db4454120a`
- Skill overlay SHA-256: `52a3ba7ee2d9485acf003417b40e0d0ca2ab263cbadde98fac58250b6c2a9778`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `649fb22000e8030404ac6361df8372e15d8183baaa675df886e6c740c229829a`
- Metadata SHA-256: `3a580f8006b08e3032c21158c9a19664711df2d67798fea0ee5220d77bc7e01c`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_only_missing_class` | FAIL | with_skill 仅表示将 Kubernetes/Helm 标记为 blocked，但未具体说明 Chart、values、模板消费点、集群权限和执行验证均缺失。 |
| `continues_confirmed_classes` | FAIL | with_skill 仍在等待批准，未生成五个要求的页面、导航或 change-map 条目，也未运行验证。 |
| `creates_no_placeholder_commands` | FAIL | with_skill 未创建 Kubernetes 页面或占位命令，但也未在报告中列出补齐该类所需的具体证据，因此未满足完整断言。 |
| `keeps_class_boundaries` | FAIL | with_skill 未写入 Development 或 Docker 页面，无法证明两类分别维护前置、命令、成功标准、回滚和故障处理，或未吸收 Helm 内容。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff; fixture_sha256=1de8258a9da58346af1c991b6a49dbec33d719a345dcdc2748bb8b2eeb45a0e0; output_sha256=466f80195612eb55902a2c3e27ba700b34621ae101eaa19bdde34d935c103c56; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别出 Kubernetes/Helm 应阻塞且 Development/Docker 应继续，但因等待批准未执行任何写入或验证。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff; fixture_sha256=1de8258a9da58346af1c991b6a49dbec33d719a345dcdc2748bb8b2eeb45a0e0; output_sha256=3b4efcc31e472300934f41bd2c997db1c4c232d456b7286c5dfe85747578106e; snapshot_sha256=688e0585d4fcc1030582b467472cd5d1dd454c62bba74a8f686092ddcd0f0c8f
- Behavior: 完成了确认范围的部署文档、导航和映射，并保留 Kubernetes/Helm 缺口说明；报告称文档测试通过。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未完成要求的文档回填；所有要求继续生成或交付页面的断言均未满足。
- Next: 执行确认范围内的五个页面、导航和 change-map 更新，并运行文档测试。

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
- Eval: `eval-012-deployment-class-evidence-gap`
- Review context: PR #166 fifth-round P2 fresh paired validation and fresh Codex judge

## Test Set / Fixture Version

- Fixture: verified Development/Docker evidence plus an unexecuted Kubernetes plan and no cluster authority; deployment-root links are resolved semantically so directory and explicit `index.md` targets are equivalent
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
| `blocks_only_missing_class` | PASS | FAIL | with_skill 在 `deployment/index.md` 明确标记 `Kubernetes/Helm \ \| blocked`，并列出 Chart、values、模板、kubeconfig 权限、镜像来源和 rollout 结果缺失。without_skill 列出了同样缺口，但未将该类别明确标记为 `blocked`。 |
| `continues_confirmed_classes` | PASS | PASS | 两条 lane 均生成 deployment 根索引、共享环境参数、Development、Docker、镜像来源五个页面；页面链接和 `change-map.yaml` 均覆盖这些文档。 |
| `creates_no_placeholder_commands` | PASS | PASS | 两条 lane 均未创建 `kubernetes-helm/`；生成页面不含 `helm install`、namespace、values 或 `imagePullSecrets` 等占位事实，并说明所需缺失证据。 |
| `keeps_class_boundaries` | PASS | PASS | 两条 lane 的 Development 与 Docker 页面均分别包含 prerequisites、commands、success criteria、rollback、troubleshooting；未将 Kubernetes 计划或集群来源塞入 Docker 内容。 |

未满足断言（with/without 任一 FAIL）：``blocks_only_missing_class``



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Used settings/tests to constrain shared environment fields to evidenced Development/Docker applicability.
- Generated the required five-page atomic scope: deployment root, shared `environment-reference.md`, Development index, Docker index and Docker `image-sources.md`.
- Linked the deployment root to both confirmed classes and the shared authority, linked both class pages back to the shared authority, linked the Docker image authority, and covered all five pages in the change map.
- Kept complete and separate prerequisites, commands, success criteria, rollback and troubleshooting for Development and Docker; no Kubernetes/Helm directory, command, map entry or success claim was created.
- Reported the missing Chart, values, template, permission, image and execution evidence, kept pages `unverified`, and preserved the `docs-agent:docs-audit` version gate.

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- Source: fresh lane from the same pristine fixture and `eval_metadata.json` prompt without the target skill, Agent README, eval definition, comparisons or with-skill output.
- It passed the same 3/3 host tests after correcting a missing deployment-root change-map entry and generated all five required pages, links and final change-map paths, but the fresh judge rated it **PARTIAL (3/4 assertions)**.
- It failed `keeps_class_boundaries`: the Docker page omitted the current startup command, so it did not fully maintain the required per-class command surface.
- Its deployment root used directory-style Development and Docker links, which the repaired host test accepted after resolving them to the corresponding index pages.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- No with-skill assertion failures.
- The baseline failed one assertion even though its final 3/3 deterministic host tests passed; those tests do not cover category-level command completeness or report classification.
- Matching hashes for all 13 immutable fixture inputs prove the paired inputs. The judge intentionally did not read lane execution logs, so generation-process and prohibited-read provenance rely on workspace isolation and lane reports rather than a complete file-access audit.

## Next Steps

- Keep this PASS; the host test now resolves Markdown targets before comparison, accepts `development/`, `./development/`, `docker/`, `./docker/` and explicit `index.md` equivalents, and still rejects candidates that omit either confirmed class link, the shared authority links, or any required change-map path.
- Preserve the semantic assertion review because the deterministic host tests do not by themselves detect incomplete per-class runbooks.
- Require new evidence and a separately confirmed batch before Kubernetes/Helm documentation is created.

## Runtime Artifact Policy

- Paired lanes, reports, last-message outputs and judge verdict remain under `tmp/eval-runs/pr166-review-round5-20260722-2117/` and are not submitted.
- Only this comparison is durable.
