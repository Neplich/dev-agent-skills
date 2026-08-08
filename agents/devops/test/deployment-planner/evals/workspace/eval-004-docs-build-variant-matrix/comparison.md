# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-004-docs-build-variant-matrix`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1133bdf01ec9b2682fe921196914971ab2c40caac0f63afd22f66198e7edede5` from `agents/devops/test/deployment-planner/evals/workspace/eval-004-docs-build-variant-matrix`.
- Fixture SHA-256: `1133bdf01ec9b2682fe921196914971ab2c40caac0f63afd22f66198e7edede5`
- Prompt SHA-256: `449e8afe22d56be4ea49871dccbdfe925565441c9990c7332f547cf304565087`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `6b7ee50b1667fd76ae49358cc3af5366a7e75afc33e7c444bb73e4e03310853a`
- Skill overlay SHA-256: `c38a517fc6ad0bdb4f779914676cb1e931bf2429f37f629f86b432a5c6adbb84`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4c14837e1c149db8fdda5fa172eb35b4e3c167d223226adbc87832c6a7126d6f`
- Metadata SHA-256: `ae56541ba154741dfb7ef84587ce065786aeb8ae82c4a282fa656aa8884b399e`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `enumerates_all_docs_variants` | PASS | with_skill 明确列出 Public、Internal 和 Preview 三个构建变体。 |
| `covers_deployment_unit_chain` | FAIL | with_skill 覆盖了构建目标、镜像、Compose、Helm/Kubernetes、健康检查和运行入口等部分，但未逐一核对 build context、静态资源入口、Deployment/Service/Ingress 或 Gateway、values 等要求的部署链路字段。 |
| `hands_units_to_cicd` | FAIL | with_skill 未为每个变体记录 integrated/alternative/deferred/blocked 处置，也未将确认的镜像单元交给 cicd-bootstrap。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=449e8afe22d56be4ea49871dccbdfe925565441c9990c7332f547cf304565087; fixture_sha256=1133bdf01ec9b2682fe921196914971ab2c40caac0f63afd22f66198e7edede5; output_sha256=d782e275b43a12b3bad87477755c9e1c0d9d21ceb0dc7ad0db29a3be10b7b98d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完整枚举三个变体并更明确标出缺口，但仍未满足完整部署单元核对和 CI/CD 交接要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=449e8afe22d56be4ea49871dccbdfe925565441c9990c7332f547cf304565087; fixture_sha256=1133bdf01ec9b2682fe921196914971ab2c40caac0f63afd22f66198e7edede5; output_sha256=0a241841f3e95274ac3311fcf54816f8f085c053026eb9b32a302b1671ce05b5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 枚举了三个变体并给出部分部署覆盖判断，但部署链路和 CI/CD 处置不完整。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 未完整覆盖每个变体要求的部署单元链路字段。
- 未记录规定的 CI/CD 处置状态或执行 cicd-bootstrap 交接。
- Next: None.

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

# Eval Result: eval-004-docs-build-variant-matrix

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-004-docs-build-variant-matrix`
- Test case: `docs-build-variant-matrix`
- Workspace: `agents/devops/test/deployment-planner/evals/workspace/eval-004-docs-build-variant-matrix`

## Latest Result

- Fresh run: `2026-08-07`（issue #238 严格隔离重跑）
- Model: `gpt-5.6-luna`，`model_reasoning_effort=medium`
- Isolation: baseline 使用随机顶层 root；完成后仅保存在内存快照并删除 root，随后才创建 with_skill root；with_skill root 删除后才创建独立 judge root。两条 lane 的原始 prompt、fixture snapshot、`HOME` 与 `CODEX_HOME` 值相同。
- Judge: 独立 fresh `codex exec`，读取实际产物、final、status 与工具轨迹，对照当前 assertions 判定；不采信 lane 自评。
- Behavior result: FAIL
- Coverage result: FULL
- Without-skill comparison: FAIL（仅作对照，不参与 durable Overall 组合）

Overall result: FAIL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Eval definition: `agents/devops/test/deployment-planner/evals/evals.json`
- Metadata: `agents/devops/test/deployment-planner/evals/workspace/eval-004-docs-build-variant-matrix/eval_metadata.json`
- Expected output: 逐一列出 Public、Internal 与 Preview 的 build/image/Compose/Helm/health/runtime 处置。
- Fixture: `evidence.md`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `enumerates_all_docs_variants` | PASS | PASS | with_skill 矩阵明确包含 public、internal、preview；without_skill 结论也逐一覆盖三者。 |
| `covers_deployment_unit_chain` | PASS | FAIL | with_skill 为每个变体提供了 build target、context、static entry、image、Compose、Kubernetes/Helm、health check、runtime entry 列，并对缺失证据标注“未记录”；without_skill 仅列出 Docker/Compose/Helm 覆盖，没有逐变体核对完整链路。 |
| `hands_units_to_cicd` | FAIL | FAIL | with_skill 给出 integrated/deferred/blocked 处置，但未明确将每个确认的镜像单元和变体矩阵交给 cicd-bootstrap；仅泛称后续交给 CI/CD 流程。without_skill 同样未进行该 handoff。 |

## With-Skill Behavior

- with_skill 成功枚举全部变体并建立了逐变体链路矩阵，所有断言均可评估，Coverage 为 FULL；但遗漏了向 cicd-bootstrap 明确移交确认镜像单元和变体矩阵，因此 durable Overall 为 FAIL。without_skill 仅作对照，存在链路覆盖与 handoff 缺口。
- Workspace changes: added: `docs/devops/documentation-site-deployment-variant-matrix.md`。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: 无文件变更。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill failures: `hands_units_to_cicd`。
- 所有当前 assertions 均已实际覆盖。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PASS（3/3）；issue #234 修复 eval 泄漏后，该结论被标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 按上表 with_skill failure 的共同根因建立后续修复项；本轮只记录结果，不修改 skill、eval 定义或 fixture。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
