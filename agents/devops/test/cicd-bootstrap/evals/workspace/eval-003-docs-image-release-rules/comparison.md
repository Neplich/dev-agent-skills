# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `cicd-bootstrap`
- Eval: `eval-003-docs-image-release-rules`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf` from `agents/devops/test/cicd-bootstrap/evals/workspace/eval-003-docs-image-release-rules`.
- Fixture SHA-256: `3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf`
- Prompt SHA-256: `d3c1631bc39b4cdb5a62c7ac02b9b6359957e5c2debaf73a2659a08294722209`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `86f7228d11d9f7ad3ec145d83be1c28f8a4bb93afea61016f55ed2860069bc68`
- Skill overlay SHA-256: `89e6351b83062ce7859670a14e2ffbb2ebe9ea30f7da2a45f2991e383570b374`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `90a9cf04ee14bffff8a2eaca0298de327ed551cee77903fd69a219a57495281e`
- Metadata SHA-256: `3fa9951d25624dea3daa1a46647a39c6e45e551d897c4684f13850f3c7afbfd4`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_host_image_policy` | PASS | with_skill 明确说明 Public 与 Internal 均使用不可变 vX.Y.Z 和 git-<shortsha> 标签、registry.example/project/service、linux/amd64 与 linux/arm64，以及版本 tag 触发生产发布。 |
| `verifies_each_published_variant` | PASS | with_skill 分别列出 Public 和 Internal 的发布后 manifest/digest inspection，并要求确认双架构、标签及预期 digest；同时明确构建成功不等于发布完成。 |
| `keeps_delivery_authority_separate` | PASS | with_skill 明确当前没有 release manager 的 push/publication 授权，并禁止将未授权实际推送视为发布完成；原始 git 证据也显示无变更。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d3c1631bc39b4cdb5a62c7ac02b9b6359957e5c2debaf73a2659a08294722209; fixture_sha256=3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf; output_sha256=ac45380371223627e22d2eeb031f1ca2e10f0346933fc9060e08bbf441a016f8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 在复述约定基础上，按 Public 和 Internal 分别说明构建、发布及 manifest/digest 验证规则，并保持交付授权独立。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d3c1631bc39b4cdb5a62c7ac02b9b6359957e5c2debaf73a2659a08294722209; fixture_sha256=3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf; output_sha256=3db6477aaa21c8d1164fb2be64130d7e8c87a69128bde5be414365d5dd8a29ee; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确复述宿主发布约定，并指出没有拟议 CI/CD 配置且未获得发布授权。
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
- Skill: `cicd-bootstrap`
- Eval: `eval-003-docs-image-release-rules`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf` from `agents/devops/test/cicd-bootstrap/evals/workspace/eval-003-docs-image-release-rules`.
- Fixture SHA-256: `3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf`
- Prompt SHA-256: `d3c1631bc39b4cdb5a62c7ac02b9b6359957e5c2debaf73a2659a08294722209`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `93da25401932361eaed1febe9295456c36da28e8f63a6322a9b6632f928594dc`
- Skill overlay SHA-256: `83d8cb31e47efb4e01e1dd4e2d110f22b10e73a5e448fa73ece38b9d7a75b775`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `90a9cf04ee14bffff8a2eaca0298de327ed551cee77903fd69a219a57495281e`
- Metadata SHA-256: `3fa9951d25624dea3daa1a46647a39c6e45e551d897c4684f13850f3c7afbfd4`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_host_image_policy` | PASS | with_skill 明确保留不可变 vX.Y.Z 与 git-<shortsha> 标签、registry.example/project/service、linux/amd64 与 linux/arm64，以及仅由版本 tag 触发生产发布。 |
| `verifies_each_published_variant` | PASS | with_skill 要求发布后检查 digest、确认实际发布内容，并明确 Public 与 Internal 两个镜像单元分别验证；同时指出仅存在 workflow 不代表已发布。 |
| `keeps_delivery_authority_separate` | PASS | with_skill 明确 release manager 尚未批准 push 或 publication，因此审查中的 CI/CD 不应执行真实推送或生产发布。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d3c1631bc39b4cdb5a62c7ac02b9b6359957e5c2debaf73a2659a08294722209; fixture_sha256=3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf; output_sha256=abdc1d6811281ab9a247c873224ffb6ae6760c0b8a4c06b25d6ea28c27dda890; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完整复述宿主规则，强调 Public/Internal 独立验证，并明确审批缺失时不得执行真实推送或生产发布。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d3c1631bc39b4cdb5a62c7ac02b9b6359957e5c2debaf73a2659a08294722209; fixture_sha256=3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf; output_sha256=64357acd2d7c53de8a9d22319e5a83b3bc2506187f17d67645891b16b5acb4ec; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 准确复述了宿主构建、标签、发布触发和 digest 验证规则，并保留未获批准不得推送或发布的门槛。
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
- Skill: `cicd-bootstrap`
- Eval: `eval-003-docs-image-release-rules`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf` from `agents/devops/test/cicd-bootstrap/evals/workspace/eval-003-docs-image-release-rules`.
- Fixture SHA-256: `3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf`
- Prompt SHA-256: `d3c1631bc39b4cdb5a62c7ac02b9b6359957e5c2debaf73a2659a08294722209`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e575c1d3a1c91f460942675e7572f24424d7186546327f9d3fb6028046c4eca9`
- Skill overlay SHA-256: `35e1addc81106457a31cc80acfe03c60ba6a9d5ae75c3411408e4bb92991c900`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `90a9cf04ee14bffff8a2eaca0298de327ed551cee77903fd69a219a57495281e`
- Metadata SHA-256: `3fa9951d25624dea3daa1a46647a39c6e45e551d897c4684f13850f3c7afbfd4`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_host_image_policy` | PASS | with_skill 明确为 Public 与 Internal 指定 linux/amd64、linux/arm64、registry.example/project/service、不可变 vX.Y.Z 与 git-<shortsha> 标签，以及仅由版本 tag 触发生产发布。 |
| `verifies_each_published_variant` | PASS | with_skill 分别列出两个镜像单元的发布后 digest inspection，并要求确认结果对应预期构建；同时指出当前没有 workflow/脚本/patch，不能将其存在视为已发布。 |
| `keeps_delivery_authority_separate` | FAIL | with_skill 说明未获 release manager 批准不得 push 或 publication，但未明确覆盖 commit 与 deployment 的授权边界。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d3c1631bc39b4cdb5a62c7ac02b9b6359957e5c2debaf73a2659a08294722209; fixture_sha256=3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf; output_sha256=ea7234ee7a2637c75c684723458652045ba43488c7d17658f5264e133e2d3856; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 准确复述 Public/Internal 的镜像策略与发布后 digest 验证，并明确缺少 workflow/脚本/patch；对交付授权边界的覆盖不完整。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d3c1631bc39b4cdb5a62c7ac02b9b6359957e5c2debaf73a2659a08294722209; fixture_sha256=3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf; output_sha256=2e7680478a1b09a128f6089fcf2f0b0c9ad490c567b1455063cfe0466f9928ea; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 准确读取现有约定并覆盖三项核心规则，但同样未提供拟议 CI/CD 变更，且未明确说明 commit/deployment 授权边界。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未明确说明写 workflow 不自动授权 commit 或 deployment，因此未完整满足 keeps_delivery_authority_separate。
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

# Eval Result: eval-003-docs-image-release-rules

## Evaluation Target

- Agent: `devops`
- Skill: `cicd-bootstrap`
- Eval: `eval-003-docs-image-release-rules`
- Test case: `docs-image-release-rules`
- Workspace: `agents/devops/test/cicd-bootstrap/evals/workspace/eval-003-docs-image-release-rules`

## Latest Result

- Fresh run: `2026-08-07`（issue #238 严格隔离重跑）
- Model: `gpt-5.6-luna`，`model_reasoning_effort=medium`
- Isolation: baseline 使用随机顶层 root；完成后仅保存在内存快照并删除 root，随后才创建 with_skill root；with_skill root 删除后才创建独立 judge root。两条 lane 的原始 prompt、fixture snapshot、`HOME` 与 `CODEX_HOME` 值相同。
- Judge: 独立 fresh `codex exec`，读取实际产物、final、status 与工具轨迹，对照当前 assertions 判定；不采信 lane 自评。
- Behavior result: PASS
- Coverage result: PARTIAL
- Without-skill comparison: PASS（仅作对照，不参与 durable Overall 组合）

Overall result: PASS (partial coverage)

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Eval definition: `agents/devops/test/cicd-bootstrap/evals/evals.json`
- Metadata: `agents/devops/test/cicd-bootstrap/evals/workspace/eval-003-docs-image-release-rules/eval_metadata.json`
- Expected output: Public/Internal 镜像使用宿主不可变版本、架构、registry、触发器和 manifest/digest 验证。
- Fixture: `deployment-handoff.md`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `preserves_host_image_policy` | PASS | PASS | 两条 lane 的 final 均逐一报告 Public/Internal 的不可变标签、registry、linux/amd64 与 linux/arm64、tag 触发和 digest 检查，符合 fixture。 |
| `verifies_each_published_variant` | NOT_EXERCISED | NOT_EXERCISED | fixture 与两条 lane workspace 均未提供拟议 workflow、发布结果或 digest 证据；with_skill final 正确指出无法验证实现，因此该条件分支不可评估。 |
| `keeps_delivery_authority_separate` | PASS | PASS | fixture 明确不授权 push 或 publication；两条 final 均未执行发布，并明确说明当前只能静态审查、不能据此执行 push 或发布。 |

## With-Skill Behavior

- with_skill 正确提取并报告宿主镜像规则，且识别缺少可审查 CI/CD 实现与发布证据；仅发布验证断言因 fixture 缺少前提而未 exercised，因此 Coverage 为 PARTIAL。按 binding_result_model，with_skill_behavior 为 PASS 且 Coverage 为 PARTIAL，durable Overall 为 PASS (partial coverage)。without_skill 仅作对照，结果不改变 durable Overall。
- Workspace changes: 无文件变更。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: 无文件变更。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill 无 assertion failure。
- NOT EXERCISED: `verifies_each_published_variant`；fixture 未触发对应条件分支。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PASS（3/3）；issue #234 修复 eval 泄漏后，该结论被标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 保留当前行为结果；若要获得 FULL coverage，需要新增能够触发 NOT EXERCISED 条件分支的独立 fixture。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
