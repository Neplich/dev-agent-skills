# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-004-docs-entry-access-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218` from `agents/devops/test/env-config-auditor/evals/workspace/eval-004-docs-entry-access-audit`.
- Fixture SHA-256: `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218`
- Prompt SHA-256: `d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a23a5206e5734d346e9cc05988abcd19e92dc09bd52f243173dd300d409a14ca`
- Skill overlay SHA-256: `cf962faf729c051cb7dfd2e1a6a7c8c9a1b7f9b67501cbf18f492cb32a84adc7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `7e8fed3827f899b24fa32a7e47350d1b61d93c36648369ee6fefd2624963c060`
- Metadata SHA-256: `3f77718e244c5e457dcf111e54d39609c8dbea3f2bea11e11380c41c91504669`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `audits_public_and_internal_access` | PASS | With_skill 分别覆盖了 staging/production 的 Public 与 Internal，并对 DNS、TLS、认证和网络限制列出已有证据或 unknown。 |
| `audits_runtime_environment_differences` | FAIL | With_skill 覆盖端口、探针、Service/Ingress、配置/Secret 引用及 staging/production 差异，但未明确核对或记录 Gateway values。 |
| `does_not_overclaim_missing_evidence` | PASS | With_skill 明确仅有 fixture 文档、没有独立运行时配置证据，并将无法验证的 DNS/TLS、探针、认证、网络、端口和引用记录为未知，未把文档声明推断为运行时事实。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=7c350d25c06076f923be90f2b845d7d82ef9d0b1362ec5917d3ef3b9fdd3ae1d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成只读审计，覆盖四个入口并谨慎区分文档声明与独立运行时证据，但遗漏 Gateway values。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=bd40cdcb9dbeba3f5e11fbdc5d5d854d3e8eb1869eba445f98ff723b47c0bc21; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 覆盖主要入口和部分未知项，但将 fixture 中的配置声明表述为已配置，证据边界较弱。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未覆盖 assertion audits_runtime_environment_differences 要求中的 Gateway values。
- Next: 补充 staging/production 各入口的 Gateway values 证据或明确记录其为 unknown。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-004-docs-entry-access-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218` from `agents/devops/test/env-config-auditor/evals/workspace/eval-004-docs-entry-access-audit`.
- Fixture SHA-256: `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218`
- Prompt SHA-256: `d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `672542b4c547ee15b5007c81b95d14b5fa65c727675122bbb5a233f553fe8ae7`
- Skill overlay SHA-256: `de10ec2dd3547ee5b7a57196d7f9e6584e3ffbd9e717a8e1c8e3b5506cd96520`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `7e8fed3827f899b24fa32a7e47350d1b61d93c36648369ee6fefd2624963c060`
- Metadata SHA-256: `3f77718e244c5e457dcf111e54d39609c8dbea3f2bea11e11380c41c91504669`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `audits_public_and_internal_access` | PASS | With-skill output covers Public and Internal for both staging and production, identifying DNS/TLS, authentication, network restriction, and unknown states where evidence is missing. |
| `audits_runtime_environment_differences` | FAIL | It covers ports/values, probes, Service, and Ingress, but does not address Gateway values or secret/config references. |
| `does_not_overclaim_missing_evidence` | FAIL | It correctly records unknowns and avoids inferring that missing authentication evidence means authentication is absent, but does not state that reachable endpoints or documented domains cannot prove integration, nor route landed validation facts to formal-docs-sync. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=d8c08b89e26552a7b719bff5f003c00bf742169538ba8f62c654b3f95f0da293; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a structured four-entry audit, distinguishes document claims from runtime evidence, and records missing evidence as unknown; it omits several explicitly required audit and handoff constraints.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=c87ff95f61a8cb78742c6155ac60495483a42ca9500299e7da5e112990fa1c60; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Broadly audits the four entry points and records unknowns, but similarly omits Gateway/secret-config checks and the endpoint/integration and formal-docs-sync constraints.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output omits Gateway values and secret/config references.
- The with_skill output omits the rule that reachable endpoints or documented domains do not prove integration and the formal-docs-sync handoff constraint.
- Next: Add explicit checks or unknowns for Gateway values and secret/config references.
- Next: State that endpoint/domain reachability is not integration proof and route only landed validation facts to formal-docs-sync.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-004-docs-entry-access-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218` from `agents/devops/test/env-config-auditor/evals/workspace/eval-004-docs-entry-access-audit`.
- Fixture SHA-256: `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218`
- Prompt SHA-256: `d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `30d88474014fd1654b2afdad809dd429177b5ede44673678193420a680992fce`
- Skill overlay SHA-256: `4a296e51a1a55fbed13be81dcfbf208640c3c058625400ff291752ea55bee7b8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `7e8fed3827f899b24fa32a7e47350d1b61d93c36648369ee6fefd2624963c060`
- Metadata SHA-256: `3f77718e244c5e457dcf111e54d39609c8dbea3f2bea11e11380c41c91504669`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `audits_public_and_internal_access` | PASS | With-skill output covers Staging/Production Public and Internal, addressing DNS/TLS for Public and authentication/network controls for Internal while marking unverifiable details unknown. |
| `audits_runtime_environment_differences` | FAIL | It covers ports, probes, Service/Ingress, values, and staging/production differences, but does not address Gateway values or secret/config references. |
| `does_not_overclaim_missing_evidence` | FAIL | It correctly marks missing runtime evidence unknown and avoids treating a documented domain as proof, but does not state that verified facts should be handed to formal-docs-sync. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=f8996466543df3d61c8bba9898f30925419d8d03cbef4bb0001a8decd6cba68b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Systematically covers all four entry categories, distinguishes document claims from runtime evidence, and identifies unknowns; it still omits Gateway, secret/config references, and the required formal-docs-sync handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=ed8724f3c94dcf934f57fcd8b6fd5b9ff5242f49f0ad9ad02ea55afe5551f2ef; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides broad read-only coverage and cautious evidence qualification, but omits the explicit formal-docs-sync handoff and also lacks Gateway and secret/config-reference coverage.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill output does not cover Gateway values or secret/config references.
- The with-skill output does not specify handing only landing/verification facts to formal-docs-sync.
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

# Eval Result: eval-004-docs-entry-access-audit

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-004-docs-entry-access-audit`
- Test case: `docs-entry-access-audit`
- Workspace: `agents/devops/test/env-config-auditor/evals/workspace/eval-004-docs-entry-access-audit`

## Latest Result

- Fresh run: `2026-08-07`（issue #238 严格隔离重跑）
- Model: `gpt-5.6-luna`，`model_reasoning_effort=medium`
- Isolation: baseline 使用随机顶层 root；完成后仅保存在内存快照并删除 root，随后才创建 with_skill root；with_skill root 删除后才创建独立 judge root。两条 lane 的原始 prompt、fixture snapshot、`HOME` 与 `CODEX_HOME` 值相同。
- Judge: 独立 fresh `codex exec`，读取实际产物、final、status 与工具轨迹，对照当前 assertions 判定；不采信 lane 自评。
- Behavior result: PASS
- Coverage result: FULL
- Without-skill comparison: FAIL（仅作对照，不参与 durable Overall 组合）

Overall result: PASS

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Eval definition: `agents/devops/test/env-config-auditor/evals/evals.json`
- Metadata: `agents/devops/test/env-config-auditor/evals/workspace/eval-004-docs-entry-access-audit/eval_metadata.json`
- Expected output: 逐环境报告 DNS/TLS、认证或网络限制、端口、探针、Ingress/Gateway、配置引用与未知项。
- Fixture: `evidence.md`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `audits_public_and_internal_access` | PASS | PASS | with_skill 逐行列出 Staging/Production 的 Public/Internal；Public 覆盖 DNS/TLS，Internal 覆盖认证与网络限制，并对缺失项标记 unknown。 |
| `audits_runtime_environment_differences` | PASS | FAIL | with_skill 覆盖探针、Service/Ingress、端口和值、staging/production 差异，并明确四个入口缺少 secret/config 引用证据；without_skill 未实际核对或明确记录 secret/config 引用。 |
| `does_not_overclaim_missing_evidence` | PASS | PASS | 两条 lane 均将不可检查的生产 TLS、探针、认证等标为 unknown，且明确域名或 Service 不足以证明安全/集成；with_skill 未声称已完成 formal-docs-sync。 |

## With-Skill Behavior

- with_skill 的三项断言均有实际、可评估证据，故行为 PASS、Coverage FULL，按 binding_result_model durable Overall 为 PASS。without_skill 作为对照在 secret/config 引用核对上缺失，判 baseline FAIL，但不影响 durable Overall。
- Workspace changes: 无文件变更。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: 无文件变更。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill 无 assertion failure。
- 所有当前 assertions 均已实际覆盖。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PASS（3/3）；issue #234 修复 eval 泄漏后，该结论被标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 保留当前回归用例；后续 skill、fixture 或断言变化时继续执行同等严格的 fresh paired run。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
