# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-003-mapped-doc-config-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5` from `agents/devops/test/env-config-auditor/evals/workspace/eval-003-mapped-doc-config-audit`.
- Fixture SHA-256: `d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5`
- Prompt SHA-256: `b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `30d88474014fd1654b2afdad809dd429177b5ede44673678193420a680992fce`
- Skill overlay SHA-256: `4a296e51a1a55fbed13be81dcfbf208640c3c058625400ff291752ea55bee7b8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `745b306831066bee2a7ff3a7b48abf881c1196cfdb1e28206ff9239f069e955c`
- Metadata SHA-256: `c5eaf2656d7227ecd689bf4922af4f6c541bc3cb4d63375292c5b605d7e8380c`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 输出引用了 change-map 和 runtime-config.md，但未提供可验证的读取顺序或目录遍历证据。 |
| `verifies_against_code` | PASS | 明确指出 runtime-config.md 声称 API_TOKEN optional，而 src/config/required.env 标记为 required，并记录了文档与代码不一致及无法证明运行时强制校验的风险。 |
| `treats_unverified_as_low_trust` | PASS | 识别 last_verified_version: unverified，并以代码配置定义作为 API_TOKEN 必填结论依据，没有仅凭文档判定覆盖完整。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956; fixture_sha256=d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5; output_sha256=ebabed1d0f513f44960c753cf927acd375e2a938d434c8a91e7379f3920a30d3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确核对映射文档、代码规则和 unverified 元数据，并区分配置定义层要求与运行时强制校验事实。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956; fixture_sha256=d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5; output_sha256=0c9912ae2a3917d8f33adabcf470bdc675fa33117ac45ddcfd491c9583ebedf1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别 API_TOKEN 为代码层面的必填项及文档冲突，但未明确说明无法证明运行时强制校验。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 提供工具调用或读取轨迹以验证映射文档优先读取及目录遍历范围。

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

# Eval Result: eval-003-mapped-doc-config-audit

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-003-mapped-doc-config-audit`
- Test case: `mapped-doc-config-audit`
- Workspace: `agents/devops/test/env-config-auditor/evals/workspace/eval-003-mapped-doc-config-audit`

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
- Eval definition: `agents/devops/test/env-config-auditor/evals/evals.json`
- Metadata: `agents/devops/test/env-config-auditor/evals/workspace/eval-003-mapped-doc-config-audit/eval_metadata.json`
- Expected output: 区分映射文档声明和代码配置事实的环境审计结论。
- Fixture: `src/config/required.env`, `docs/site/standards/change-map.yaml`, `docs/site/api/runtime-config.md`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | FAIL | with_skill 的读取命令顺序为 change-map、契约/skill-map、src/config/required.env、runtime-config.md；映射文档并未先于代码读取。without_skill 先读取 required.env，随后才读取文档。 |
| `verifies_against_code` | PASS | PASS | 两条 lane 均读取 required.env，确认 API_TOKEN = required，并识别文档中的 optional 冲突；with_skill 还明确记录了配置缺失风险。 |
| `treats_unverified_as_low_trust` | PASS | FAIL | with_skill 明确识别 last_verified_version: unverified，并以代码事实作为关键结论依据。without_skill 虽读取了该字段，但最终结论未识别或说明其最低信任影响。 |

## With-Skill Behavior

- with_skill 已核对文档与代码并正确判定 API_TOKEN 为必填，也正确处理 unverified；但未满足“先读取映射文档再回读代码”的严格读取顺序，因此 durable Overall 为 FAIL。Coverage 为 FULL。without_skill 作为对照同样未满足首读文档顺序，且未在结论中处理 unverified。
- Workspace changes: 无文件变更。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: 无文件变更。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill failures: `reads_mapped_docs_first`。
- 所有当前 assertions 均已实际覆盖。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PASS；issue #234 修复 eval 泄漏后，该结论被标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 按上表 with_skill failure 的共同根因建立后续修复项；本轮只记录结果，不修改 skill、eval 定义或 fixture。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
