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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `762ea3248d76c5c9e715368b11ab616562bb9bdb0e2bd6a6aad38d47cc80b3af`
- Skill overlay SHA-256: `e369287042e128c8646e3e76c58b4eed6d4fabe0c3d6bf6826d377c5e25e82c9`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4c14837e1c149db8fdda5fa172eb35b4e3c167d223226adbc87832c6a7126d6f`
- Metadata SHA-256: `ae56541ba154741dfb7ef84587ce065786aeb8ae82c4a282fa656aa8884b399e`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `a6701d093076bc07d26c7e813151915b2b1a25f501428e58ba88c24bfe3d6c6e`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `enumerates_all_docs_variants` | PASS | With-skill matrix explicitly includes Public, Internal, and Preview. |
| `covers_deployment_unit_chain` | PASS | For every variant, the matrix addresses build target/context/static entry, image, Compose, Kubernetes/Helm resources, health check, and runtime entry, marking unsupported or undocumented items as blocked/unknown. |
| `hands_units_to_cicd` | NOT_EXERCISED | The candidate identifies missing image metadata and correctly states that confirmed image units cannot yet be handed to cicd-bootstrap; the locked evidence provides no later confirmation or runtime evidence enabling that handoff. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=449e8afe22d56be4ea49871dccbdfe925565441c9990c7332f547cf304565087; fixture_sha256=1133bdf01ec9b2682fe921196914971ab2c40caac0f63afd22f66198e7edede5; output_sha256=dfd058b47490363e1a6d7dc52e97fb4035143a7a8b5c81b91a12f592395cba8b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Enumerates all variants and provides a complete per-variant chain matrix, explicitly distinguishing documented coverage from blocked or missing evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=449e8afe22d56be4ea49871dccbdfe925565441c9990c7332f547cf304565087; fixture_sha256=1133bdf01ec9b2682fe921196914971ab2c40caac0f63afd22f66198e7edede5; output_sha256=bc9ec83702300e6bae81ed74f10ce490830e8d6a381366c5e981d032743e5a82; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Enumerates all three variants and identifies broad Docker/Compose/Helm coverage and gaps, but lacks the complete per-variant deployment-chain matrix.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide confirmed image-unit metadata and any required user/runtime confirmation, then evaluate the cicd-bootstrap handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `762ea3248d76c5c9e715368b11ab616562bb9bdb0e2bd6a6aad38d47cc80b3af`
- Skill overlay SHA-256: `e369287042e128c8646e3e76c58b4eed6d4fabe0c3d6bf6826d377c5e25e82c9`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4c14837e1c149db8fdda5fa172eb35b4e3c167d223226adbc87832c6a7126d6f`
- Metadata SHA-256: `ae56541ba154741dfb7ef84587ce065786aeb8ae82c4a282fa656aa8884b399e`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `enumerates_all_docs_variants` | PASS | With_skill matrix includes Public, Internal, and Preview. |
| `covers_deployment_unit_chain` | FAIL | It checks most chain elements, but does not explicitly assess Deployment/Service/Ingress or Gateway and values for each variant. |
| `hands_units_to_cicd` | FAIL | It records integrated/blocked dispositions, but does not hand confirmed image units to cicd-bootstrap; it explicitly says CI/CD handoff remains to be recorded separately. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=449e8afe22d56be4ea49871dccbdfe925565441c9990c7332f547cf304565087; fixture_sha256=1133bdf01ec9b2682fe921196914971ab2c40caac0f63afd22f66198e7edede5; output_sha256=8f8dcdcde790c12e572691878942183bf914501ddf29aaea910dc0703569b796; snapshot_sha256=5cf0b0f73c1333c55ab9ed829699446fed9d7b778b73fced655c5a082864c32d
- Behavior: Adds a detailed three-variant matrix and gap assessment, but omits explicit per-variant resource/value checks and cicd-bootstrap handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=449e8afe22d56be4ea49871dccbdfe925565441c9990c7332f547cf304565087; fixture_sha256=1133bdf01ec9b2682fe921196914971ab2c40caac0f63afd22f66198e7edede5; output_sha256=90a7561b9345d4adb5b681e832a1a4c46a14943ac45be91ccf4bbf5881c65ea1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Enumerates all three variants but provides a less complete deployment matrix and no CI/CD handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output does not explicitly cover Deployment/Service/Ingress or Gateway and values for every variant.
- The with_skill output does not hand confirmed image units to cicd-bootstrap.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `62de154d5d3bc35771dec755a7ec8baad854cbf6ae4dee4b16b30feea6be70e9`
- Skill overlay SHA-256: `630d9fd3b5fba61321b2f5f330c0da776d5a0a643b7a33930fe98ad6dda9f302`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4c14837e1c149db8fdda5fa172eb35b4e3c167d223226adbc87832c6a7126d6f`
- Metadata SHA-256: `ae56541ba154741dfb7ef84587ce065786aeb8ae82c4a282fa656aa8884b399e`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `enumerates_all_docs_variants` | PASS | with_skill 输出明确列出 public、internal、preview 三个构建变体，并在矩阵中逐一覆盖。 |
| `covers_deployment_unit_chain` | FAIL | 虽列出 Docker、Compose、Helm/Kubernetes 等单元，但未逐一核对每个变体的 build target/context/static entry、Deployment/Service/Ingress 或 Gateway、values、健康检查和运行入口。 |
| `hands_units_to_cicd` | FAIL | 未为每个变体记录 integrated/alternative/deferred/blocked 处置，也未将确认的镜像单元交给 cicd-bootstrap。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=449e8afe22d56be4ea49871dccbdfe925565441c9990c7332f547cf304565087; fixture_sha256=1133bdf01ec9b2682fe921196914971ab2c40caac0f63afd22f66198e7edede5; output_sha256=3497638230d2dcb2ab1fc35c7287fba04e3658c75dfec3cf57c23bceba296849; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 枚举了全部三个变体并细化部署单元矩阵，但缺少要求的逐项链路核对字段及 cicd-bootstrap 交接。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=449e8afe22d56be4ea49871dccbdfe925565441c9990c7332f547cf304565087; fixture_sha256=1133bdf01ec9b2682fe921196914971ab2c40caac0f63afd22f66198e7edede5; output_sha256=2ca4ee33a2d386bd72ed58692a272010110f8416d4bbd98d42829950e294639a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 枚举了 public、internal、preview，并比较了 Docker、Compose、Helm 覆盖；未覆盖 CICD 交接和完整链路字段。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- covers_deployment_unit_chain 未满足完整链路核对要求。
- hands_units_to_cicd 未满足处置分类和 cicd-bootstrap 交接要求。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
