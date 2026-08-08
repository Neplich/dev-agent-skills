# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-003-mapped-doc-deployment`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471` from `agents/devops/test/deployment-planner/evals/workspace/eval-003-mapped-doc-deployment`.
- Fixture SHA-256: `beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471`
- Prompt SHA-256: `40b086c239ff14f46936633adeb5d9079306a48046e93c803af236ab43d646d6`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `762ea3248d76c5c9e715368b11ab616562bb9bdb0e2bd6a6aad38d47cc80b3af`
- Skill overlay SHA-256: `e369287042e128c8646e3e76c58b4eed6d4fabe0c3d6bf6826d377c5e25e82c9`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `3a6f0e2dac2acec4b2146c1f3b14a82dc89e2d78da9249fb55fda45906586c82`
- Metadata SHA-256: `d4f866ac92cff8803e8f120ce38631fed1d054cce30a482192275834ed6880bf`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 锁定的原始证据未能证明文件读取顺序或是否遍历了无关站点文档。 |
| `verifies_against_code` | PASS | with_skill 输出明确以 src/runtime/server.conf 的 listen_port = 8081 为依据，指出文档原写 8080 已过时，并建议暴露及映射 8081。 |
| `treats_unverified_as_low_trust` | PASS | with_skill 将代码配置作为运行时事实来源，未盲信 last_verified_version: unverified 的文档端口，并据此排除 8080。 |
| `omits_unselected_targets` | PASS | with_skill 仅产出 deploy/docker/README.md 容器部署建议；原始变更证据中没有 deploy/local 或 deploy/helm 资产。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=40b086c239ff14f46936633adeb5d9079306a48046e93c803af236ab43d646d6; fixture_sha256=beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471; output_sha256=0232171802eaf06c8d1196253682a9050e7be4c7aad93a7c3a169bd45e46cf60; snapshot_sha256=c24f95dca8dcdc7684cf63de952c5f7489171bf17eba4bbc7e96058f21e414ee
- Behavior: 正确以代码核证 8081，说明 8080 差异及部署影响，仅生成容器化部署建议；读取顺序无法从证据确认。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=40b086c239ff14f46936633adeb5d9079306a48046e93c803af236ab43d646d6; fixture_sha256=beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471; output_sha256=3c2e76d3e2b9bce150df00c18c7bfdfba56eb99b7986c6043adcd94d0c7d5623; snapshot_sha256=736f13cfbe211f52d0610e91bdbfe39c9ad0651c8337ad06dfe23d08afb368b1
- Behavior: 正确核对了 8081 端口并更新运行时文档，但未提供完整的目标限定证据。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-003-mapped-doc-deployment`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471` from `agents/devops/test/deployment-planner/evals/workspace/eval-003-mapped-doc-deployment`.
- Fixture SHA-256: `beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471`
- Prompt SHA-256: `40b086c239ff14f46936633adeb5d9079306a48046e93c803af236ab43d646d6`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `62de154d5d3bc35771dec755a7ec8baad854cbf6ae4dee4b16b30feea6be70e9`
- Skill overlay SHA-256: `630d9fd3b5fba61321b2f5f330c0da776d5a0a643b7a33930fe98ad6dda9f302`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `3a6f0e2dac2acec4b2146c1f3b14a82dc89e2d78da9249fb55fda45906586c82`
- Metadata SHA-256: `d4f866ac92cff8803e8f120ce38631fed1d054cce30a482192275834ed6880bf`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | The with_skill output cites the change map and the specifically mapped runtime document, with no unrelated site-document traversal or references. |
| `verifies_against_code` | PASS | It cites server.conf showing listen_port = 8081, identifies the document's conflicting 8080, and recommends EXPOSE/mapping 8081 while explaining the impact. |
| `treats_unverified_as_low_trust` | PASS | The output treats the conflicting documentation as non-authoritative and bases the deployment port on the code configuration. |
| `omits_unselected_targets` | PASS | The output contains only container/Docker deployment guidance and produces no deploy/local or deploy/helm assets. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=40b086c239ff14f46936633adeb5d9079306a48046e93c803af236ab43d646d6; fixture_sha256=beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471; output_sha256=542718c2805987d1d5f8b05a3032e66880b837993d860da6cc3345429641f75a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Used the mapped runtime documentation alongside code evidence, prioritized the code-configured port 8081, explained the 8080 discrepancy, and limited guidance to container deployment.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=40b086c239ff14f46936633adeb5d9079306a48046e93c803af236ab43d646d6; fixture_sha256=beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471; output_sha256=43bdb750c722cb703ca18073310b1ee7603eeaae84ef5e8f6f8473688d615680; snapshot_sha256=f09bb7e714f02f386f596f61347aaae2c411c90309d604f9bb87a4d03bca044d
- Behavior: Correctly selected port 8081 and modified the runtime documentation, but did not demonstrate change-map-first handling or explicitly address the document's unverified status.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-003-mapped-doc-deployment`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471` from `agents/devops/test/deployment-planner/evals/workspace/eval-003-mapped-doc-deployment`.
- Fixture SHA-256: `beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471`
- Prompt SHA-256: `40b086c239ff14f46936633adeb5d9079306a48046e93c803af236ab43d646d6`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `6b7ee50b1667fd76ae49358cc3af5366a7e75afc33e7c444bb73e4e03310853a`
- Skill overlay SHA-256: `c38a517fc6ad0bdb4f779914676cb1e931bf2429f37f629f86b432a5c6adbb84`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `3a6f0e2dac2acec4b2146c1f3b14a82dc89e2d78da9249fb55fda45906586c82`
- Metadata SHA-256: `d4f866ac92cff8803e8f120ce38631fed1d054cce30a482192275834ed6880bf`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | The with_skill output shows the mapped document was updated, but provides no evidence of read order or whether unrelated site documents were skipped. |
| `verifies_against_code` | PASS | The with_skill output identifies 8081 as the configured runtime port, contrasts it with the document's 8080, and recommends exposing, publishing, health-checking, and routing to 8081. |
| `treats_unverified_as_low_trust` | PASS | The deployment parameter is aligned with the fixture's source configuration (listen_port = 8081), rather than relying on the document's unverified 8080 claim. |
| `omits_unselected_targets` | PASS | The with_skill delivery evidence contains only the runtime documentation change; no deploy/local or deploy/helm assets were generated. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=40b086c239ff14f46936633adeb5d9079306a48046e93c803af236ab43d646d6; fixture_sha256=beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471; output_sha256=9bee7f4e9f8a548b9e69b99e92a791e5766566a20858cf40e6a508a1fc813f12; snapshot_sha256=f78bc66b98718859ee09f08ff419e8e1feafa840ab78d46fb270acc19b82bf80
- Behavior: Correctly reconciled the unverified document's 8080 with source-configured 8081, documented container deployment implications, and generated no unselected deployment assets.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=40b086c239ff14f46936633adeb5d9079306a48046e93c803af236ab43d646d6; fixture_sha256=beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471; output_sha256=d44679aeaf145f579232e46d5ebb26db9669458b7b665030d0d3a1509154a80f; snapshot_sha256=0094aad31abf3c56957943851010d719b8f167720a45aa4f653afd6cd6b97449
- Behavior: Reached the correct 8081 recommendation but modified the mapped documentation with a more extensive Dockerfile and run-command proposal.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
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

# Eval Result: eval-003-mapped-doc-deployment

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-003-mapped-doc-deployment`
- Test case: `mapped-doc-deployment`
- Workspace: `agents/devops/test/deployment-planner/evals/workspace/eval-003-mapped-doc-deployment`

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
- Metadata: `agents/devops/test/deployment-planner/evals/workspace/eval-003-mapped-doc-deployment/eval_metadata.json`
- Expected output: 基于映射文档定位、以代码配置确认端口的部署建议和文档差异记录。
- Fixture: `src/runtime/server.conf`, `docs/site/standards/change-map.yaml`, `docs/site/api/runtime-server.md`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | FAIL | with_skill 首个执行命令只读取 skill 与 server.conf，未先读取 change-map 命中的 docs/site/api/runtime-server.md；without_skill 先读 server.conf，之后才读取文档，并进行了无关文件遍历。 |
| `verifies_against_code` | PASS | PASS | 两条 lane 均读取 src/runtime/server.conf，确认 8081；with_skill final 明确指出文档 8080 与代码 8081 不一致，并按 8081 给出容器发布建议。 |
| `treats_unverified_as_low_trust` | PASS | PASS | 关键端口以 src/runtime/server.conf 的 8081 为准，而非盲用文档中的 8080；两条 lane 均识别并处理了该差异。 |
| `omits_unselected_targets` | PASS | PASS | with_skill 仅给出容器化建议，未生成 deploy/local 或 deploy/helm 资产；status 显示无文件变更。without_skill 也未生成这些未选择目标。 |

## With-Skill Behavior

- with_skill 覆盖全部断言，但未遵守命中文档优先读取顺序，因此 durable Overall 为 FAIL。without_skill 仅作对照，亦因读取顺序不符合断言而判 FAIL。
- Workspace changes: 无文件变更。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: modified: `docs/site/api/runtime-server.md`。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill failures: `reads_mapped_docs_first`。
- 所有当前 assertions 均已实际覆盖。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PASS（4/4）；issue #234 修复 eval 泄漏后，该结论被标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 按上表 with_skill failure 的共同根因建立后续修复项；本轮只记录结果，不修改 skill、eval 定义或 fixture。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
