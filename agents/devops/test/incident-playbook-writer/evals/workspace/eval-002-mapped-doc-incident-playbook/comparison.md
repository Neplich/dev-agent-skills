# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `incident-playbook-writer`
- Eval: `eval-002-mapped-doc-incident-playbook`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7` from `agents/devops/test/incident-playbook-writer/evals/workspace/eval-002-mapped-doc-incident-playbook`.
- Fixture SHA-256: `cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7`
- Prompt SHA-256: `27a471d4180c030327b87d22f79174352fdeffbbaace399da8cf913275d6b17e`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `500941dffb48347901d3283054321002e2a4be37cb509882170d999b6f27485f`
- Skill overlay SHA-256: `322b6fc4de918cf45a54ef853b436aea4069d29a5654d65d9e002fe4543294d8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `56f66c660609712980bbe29e190d00dff6d36c67cb844c6b5e1aa3d336dcd314`
- Metadata SHA-256: `d30677e1d058f7ced7ac6b80a07136e834c175a519dc8964e75c167556348374`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 候选输出提及了健康说明和变更映射，但锁定原始证据无法证明读取顺序。 |
| `verifies_against_code` | PASS | with_skill 输出明确以 src/runtime/health.rules 的值 5 为准，指出文档错误地写为 3，并说明该差异会影响告警、升级和回滚时机。 |
| `treats_unverified_as_low_trust` | PASS | with_skill 输出明确将 last_verified_version: unverified 视为不能覆盖实现事实，并以代码中的阈值及其规则值作为关键处置和回滚依据。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=27a471d4180c030327b87d22f79174352fdeffbbaace399da8cf913275d6b17e; fixture_sha256=cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7; output_sha256=2192c0316224b41067b8df185a64195353dfeeaaed92cbe0a19b5fe41e3f5d57; snapshot_sha256=31b9ff65174a0fb9892525fde3cb349d85c2b23348fe69bb3ceab0ba4e372160
- Behavior: 产出了最小处置和回滚手册，按代码阈值核证并明确处理未核证文档与部署证据限制。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=27a471d4180c030327b87d22f79174352fdeffbbaace399da8cf913275d6b17e; fixture_sha256=cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7; output_sha256=55744fb957a1d578b8214a178a4a12a403c88e429c96a455b804d3864d50ebf0; snapshot_sha256=a0414feb4981b0669c1b0a21e4f6090fec2eff764ff6c3717304c010819338f0
- Behavior: 正确核对了代码阈值并补充了处置、回滚内容，但修改了健康说明文档。
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
- Skill: `incident-playbook-writer`
- Eval: `eval-002-mapped-doc-incident-playbook`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7` from `agents/devops/test/incident-playbook-writer/evals/workspace/eval-002-mapped-doc-incident-playbook`.
- Fixture SHA-256: `cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7`
- Prompt SHA-256: `27a471d4180c030327b87d22f79174352fdeffbbaace399da8cf913275d6b17e`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a3dcab32ca6f16ce18a6d001bf4e11cedd9e9fc11b26bd45c079c620b67ec959`
- Skill overlay SHA-256: `f49bc0517e51e913154134ad0435ffac724d99a1f33e11d0280d2294a9d5c8bd`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `56f66c660609712980bbe29e190d00dff6d36c67cb844c6b5e1aa3d336dcd314`
- Metadata SHA-256: `d30677e1d058f7ced7ac6b80a07136e834c175a519dc8964e75c167556348374`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill 输出明确核对 docs/site/api/runtime-health.md，并将其与相关代码对照；交付证据未显示遍历其他站点文档。 |
| `verifies_against_code` | PASS | 明确识别文档的 3 次与 src/runtime/health.rules 的 5 次不一致，采用代码阈值，并将处置、回滚及恢复验证时机设为 5 次。 |
| `treats_unverified_as_low_trust` | PASS | 明确指出 last_verified_version: unverified，视文档为过期低可信；告警阈值、回滚触发条件和恢复验证均以代码中的 5 次为依据。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=27a471d4180c030327b87d22f79174352fdeffbbaace399da8cf913275d6b17e; fixture_sha256=cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7; output_sha256=2cc711dd746ed649a4f3c565eb3947280f65b637c6d3e7dc5cf23a51826efed1; snapshot_sha256=82dcec12add644768aa5006a4c84555fd45e037b54314574418cb762ff804801
- Behavior: 新增独立的处置与回滚手册，明确核对映射文档、识别文档与代码的阈值冲突，并按代码证据及未核证状态处理。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=27a471d4180c030327b87d22f79174352fdeffbbaace399da8cf913275d6b17e; fixture_sha256=cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7; output_sha256=3192e534816e7ef1b2fcfb0eb020dbdf6fd9f9cffa8ad0291857033d020b2eb8; snapshot_sha256=a9dc4de9c88d960a39350e8212dd968ab09505926b804eaa43338490bd4cb0c8
- Behavior: 修改健康说明文档，正确采用代码中的 5 次阈值并补充处置与回滚步骤，但未明确说明 unverified 文档的低可信处理。
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
- Skill: `incident-playbook-writer`
- Eval: `eval-002-mapped-doc-incident-playbook`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7` from `agents/devops/test/incident-playbook-writer/evals/workspace/eval-002-mapped-doc-incident-playbook`.
- Fixture SHA-256: `cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7`
- Prompt SHA-256: `27a471d4180c030327b87d22f79174352fdeffbbaace399da8cf913275d6b17e`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2ee427f056a8ac15cf9d4885d215c9ee8db1e2692beb4901545cf09914ace629`
- Skill overlay SHA-256: `c4126e3ccb08175ab528f594300ee6ab6305ac16fe0fbdfca38a793465cbc175`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `56f66c660609712980bbe29e190d00dff6d36c67cb844c6b5e1aa3d336dcd314`
- Metadata SHA-256: `d30677e1d058f7ced7ac6b80a07136e834c175a519dc8964e75c167556348374`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | with_skill 输出未提供读取顺序或过程证据，无法确认是否先读取映射文档且未遍历其他站点文档。 |
| `verifies_against_code` | FAIL | 输出正确核对了代码中的 5 次阈值并修正了文档中的 3 次，但未明确说明阈值差异对处置时机的影响。 |
| `treats_unverified_as_low_trust` | FAIL | 输出引用代码作为阈值来源，但未处理 last_verified_version: unverified 的最低信任要求，也未说明告警与回滚关键步骤由代码或测试证据确认。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=27a471d4180c030327b87d22f79174352fdeffbbaace399da8cf913275d6b17e; fixture_sha256=cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7; output_sha256=1cbe1128a7cff901fe9bb310ceac12685b55c778907a90b87ea3ce439f65aa8f; snapshot_sha256=8d9c3beb6f4b10832ca68f6dbc458600d39e8210f87535f087397224ce48b822
- Behavior: 核对并采用了代码中的 5 次阈值，补充了具体处置和回滚步骤，并避免臆造部署命令；但缺少读取顺序、处置时机影响及 unverified 证据处理说明。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=27a471d4180c030327b87d22f79174352fdeffbbaace399da8cf913275d6b17e; fixture_sha256=cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7; output_sha256=3198dc39e9b313e2e459a69bac5cb495daa79e9edb3f9f33267faf2cb7acd47f; snapshot_sha256=d77cdf3ad303c08025baa70555209c716f0e48fa8cae355b9531284c6c45c870
- Behavior: 修正了告警阈值并补充处置、回滚内容，但未体现映射文档优先读取、阈值差异对时机的影响或 unverified 文档的低信任处理。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未说明 3 次文档阈值与 5 次代码阈值差异对处置时机的影响。
- with_skill 未按最低信任处理 last_verified_version: unverified，且未以代码或测试证据明确确认告警与回滚关键步骤。
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

# Eval Result: eval-002-mapped-doc-incident-playbook

## Evaluation Target

- Agent: `devops`
- Skill: `incident-playbook-writer`
- Eval: `eval-002-mapped-doc-incident-playbook`
- Test case: `mapped-doc-incident-playbook`
- Workspace: `agents/devops/test/incident-playbook-writer/evals/workspace/eval-002-mapped-doc-incident-playbook`

## Latest Result

- Fresh run: `2026-08-07`（issue #238 严格隔离重跑）
- Model: `gpt-5.6-luna`，`model_reasoning_effort=medium`
- Isolation: baseline 使用随机顶层 root；完成后仅保存在内存快照并删除 root，随后才创建 with_skill root；with_skill root 删除后才创建独立 judge root。两条 lane 的原始 prompt、fixture snapshot、`HOME` 与 `CODEX_HOME` 值相同。
- Judge: 独立 fresh `codex exec`，读取实际产物、final、status 与工具轨迹，对照当前 assertions 判定；不采信 lane 自评。
- Behavior result: FAIL
- Coverage result: PARTIAL
- Without-skill comparison: FAIL（仅作对照，不参与 durable Overall 组合）

Overall result: FAIL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Eval definition: `agents/devops/test/incident-playbook-writer/evals/evals.json`
- Metadata: `agents/devops/test/incident-playbook-writer/evals/workspace/eval-002-mapped-doc-incident-playbook/eval_metadata.json`
- Expected output: 以代码事实确定告警阈值的故障处置步骤，并记录映射文档差异。
- Fixture: `src/runtime/health.rules`, `docs/site/standards/change-map.yaml`, `docs/site/api/runtime-health.md`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | FAIL | with_skill 先读取 change-map、代码，再读取 runtime-health.md；without_skill 先读取 health.rules，再读取文档，均未优先读取 required doc。 |
| `verifies_against_code` | FAIL | FAIL | 两条 lane 都确认代码阈值为 5、文档值为 3；但 with_skill 未说明阈值差异对处置时机的影响，也未产出处置手册。without_skill 同样未明确说明 5 相对 3 会使告警晚两个连续失败触发。 |
| `treats_unverified_as_low_trust` | NOT_EXERCISED | FAIL | with_skill 因缺少 PM/DevOps 交接上下文和 playbook 选择而未进入写入关键告警/回滚步骤的分支，fixture 前提不足，故不判定该断言。without_skill 虽核对了代码，但生成的回滚步骤没有代码或测试证据支撑，也未明确按 unverified 最低信任处理。 |

## With-Skill Behavior

- with_skill 正确识别了代码阈值 5 与文档阈值 3 的冲突，并因缺少必要上下文而阻止写入；但读取顺序不符合断言，且未说明阈值差异对处置时机的影响。覆盖度因关键步骤分支未触发而为 PARTIAL。without_skill 作为对照也未满足读取顺序和最低信任要求。
- Workspace changes: 无文件变更。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: modified: `docs/site/api/runtime-health.md`。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill failures: `reads_mapped_docs_first`, `verifies_against_code`。
- NOT EXERCISED: `treats_unverified_as_low_trust`；fixture 未触发对应条件分支。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PASS（3/3）；issue #234 修复 eval 泄漏后，该结论被标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 按上表 with_skill failure 的共同根因建立后续修复项；本轮只记录结果，不修改 skill、eval 定义或 fixture。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
