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
