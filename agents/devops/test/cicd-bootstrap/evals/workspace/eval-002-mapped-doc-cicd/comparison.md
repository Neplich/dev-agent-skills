# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `cicd-bootstrap`
- Eval: `eval-002-mapped-doc-cicd`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b0f5ab103062d754c225176fd1995f4f428e9f29340584ac86077ed978dc1482` from `agents/devops/test/cicd-bootstrap/evals/workspace/eval-002-mapped-doc-cicd`.
- Fixture SHA-256: `b0f5ab103062d754c225176fd1995f4f428e9f29340584ac86077ed978dc1482`
- Prompt SHA-256: `08a3ffdcb2251091cdf30040590082a976faabcf76e7e71f7124b4bb2d5a5ba4`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e575c1d3a1c91f460942675e7572f24424d7186546327f9d3fb6028046c4eca9`
- Skill overlay SHA-256: `35e1addc81106457a31cc80acfe03c60ba6a9d5ae75c3411408e4bb92991c900`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `68a87fb5d229c5c451c4b7081adb9e28c9c2e68f2832958c12f8d53464b0ae13`
- Metadata SHA-256: `a6802835ad6096782cd89b2c4280b4422a56ff9be96ac885a939daae8583297c`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | with_skill 提及了 change-map、目标文档和代码，但未证明先读取 change-map 后读取目标文档，也未明确说明未遍历无关文档。 |
| `verifies_against_code` | FAIL | 正确采用代码中的 verify 并指出文档中的 test 不一致，但未说明错误命令对流水线的具体影响。 |
| `treats_unverified_as_low_trust` | FAIL | fixture 中两份相关文档均标记 last_verified_version: unverified，但 with_skill 输出未识别该状态，也未说明关键步骤需由代码或测试配置核证。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=08a3ffdcb2251091cdf30040590082a976faabcf76e7e71f7124b4bb2d5a5ba4; fixture_sha256=b0f5ab103062d754c225176fd1995f4f428e9f29340584ac86077ed978dc1482; output_sha256=c8ccbfdd848ff2b31d9313630a6e480435e5d07666c3d5fcd11f6dd48b18bebd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确给出 verify，依据代码指出文档中的 test 已过时，并提到变更映射；未充分证明映射文档优先读取，且遗漏未核证状态和错误命令影响。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=08a3ffdcb2251091cdf30040590082a976faabcf76e7e71f7124b4bb2d5a5ba4; fixture_sha256=b0f5ab103062d754c225176fd1995f4f428e9f29340584ac86077ed978dc1482; output_sha256=a619fc4463007143e0c6ccdad187d2171d973ced1def6df3947b6ff9a466974d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确给出 verify，指出文档使用 test 且与代码不一致，并提到变更映射；未处理未核证状态、错误命令影响或读取顺序。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足三个断言的完整要求。
- Next: None.

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

# Eval Result: eval-002-mapped-doc-cicd

## Evaluation Target

- Agent: `devops`
- Skill: `cicd-bootstrap`
- Eval: `eval-002-mapped-doc-cicd`
- Test case: `mapped-doc-cicd`
- Workspace: `agents/devops/test/cicd-bootstrap/evals/workspace/eval-002-mapped-doc-cicd`

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
- Eval definition: `agents/devops/test/cicd-bootstrap/evals/evals.json`
- Metadata: `agents/devops/test/cicd-bootstrap/evals/workspace/eval-002-mapped-doc-cicd/eval_metadata.json`
- Expected output: 以代码配置确认校验命令的 CI 建议，并报告映射文档与代码差异。
- Fixture: `src/build/pipeline.rules`, `docs/site/standards/change-map.yaml`, `docs/site/api/build-pipeline.md`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | FAIL | 两条 lane 都先读取 src/build/pipeline.rules，之后才读取 change-map 和 required doc，未满足 change-map → required doc → 回代码核验的要求。 |
| `verifies_against_code` | FAIL | FAIL | 两条 lane 最终均使用 verify 并识别文档中的 test 不一致；但未说明错误命令 test 对流水线的影响。with_skill 后续 rg 可视为再次核验代码，但合取要求仍因缺少影响说明而失败。 |
| `treats_unverified_as_low_trust` | FAIL | FAIL | 两条 lane 都读取到 last_verified_version: unverified，但没有明确将文档视为低信任，也没有证明所有关键 CI 步骤均由代码或测试配置核证。 |

## With-Skill Behavior

- with_skill 的三个合取断言均未完整满足，因此 with_skill_behavior 为 FAIL；所有断言均可评估，Coverage 为 FULL。without_skill 仅作对照，其 FAIL 不改变 durable Overall。
- Workspace changes: added: `.github/workflows/ci.yml`；modified: `docs/site/api/build-pipeline.md`。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: added: `.github/workflows/validation.yml`；modified: `docs/site/api/build-pipeline.md`。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill failures: `reads_mapped_docs_first`, `verifies_against_code`, `treats_unverified_as_low_trust`。
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
