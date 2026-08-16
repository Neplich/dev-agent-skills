# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-010-post-tag-match`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518` from `agents/docs/test/docs-audit/evals/workspace/eval-010-post-tag-match`.
- Identity schema: `2`
- target_skill_sha256: `dafd53371901dfd724f88c70262b157e59494d29da1c613d0ef130564b6ff4f9`
- eval_definition_sha256: `f4b575228474dd8bb2a93bb17a067f25252f9c293e1f78393d445c449385e8d2`
- metadata_sha256: `12f75879efa3cacf943ae19595239a747563947015e4033eed4ea7f4a51a5b47`
- fixture_sha256: `43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `f64d4542aa97d4b9bcd4bc655a5e70fec7d827a5ea9e9f63067fde8d7b819748`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `7e61bd8eca6431729aee1f3be4656be0a4348119eb1218623bafd54cfaead2ab`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `selects_pre_tag_authority_safely` | FAIL | with_skill 仅说明当前存在该 ref，未提供其实际解析的 commit/tree 或该 ref 下 handoff/audit 的读取结果；克隆侧证据充分。 |
| `proves_released_tree_binding` | FAIL | raw trace 证明两侧解析了 tag commit/tree，且克隆读取了 tag-tree 路径；但未锁定证明当前 tag tree 与 direct package tree 的比较结果，最终输出也未给出该绑定结论。 |
| `verifies_version_surfaces_from_release` | PASS | with_skill 明确从 tag tree 核验四个版本面，区分了 v1.2.0 与 1.2.0，并未把当前工作区作为成功证据。 |
| `requires_durable_post_tag_evidence` | PASS | with_skill 明确指出缺少独立 post-tag 结果持久化凭据，两个场景均保持 blocked，且未声称 release_verified。 |
| `preserves_upstream_release_artifacts` | PASS | with_skill 说明未修改现有 ref、tag 或发布记录；git_evidence 亦显示 HEAD、分支、refs 和工作区均未变化。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143; fixture_sha256=43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518; output_sha256=83991f7951e6ad13868321d2a555508e54b287064a9a86b5dfbf9e6f24f7493f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确完成 tag/clone 的多数只读核验并保持 blocked 与不可变性，但遗漏两项当前仓库 authority/tree-binding 的关键可见证据。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143; fixture_sha256=43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518; output_sha256=49a294f683514069075f268f18f35bd6cb4507bf3e15c96cb337a057c969b68b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 新鲜基线也完成了大部分 tag、版本面和不可变性判断，但将当前工作区描述为可完整复核，未识别同等严格的 authority 与持久化门槛。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未证明当前仓库 pre-tag authority 的实际 commit/tree 解析和 ref 下证据读取。
- with_skill 未证明当前 tag tree 与 direct package tree 的绑定比较。
- Next: 补充当前 refs/release-evidence/v1.2.0 的实际 commit/tree 解析及其 handoff/audit 读取结果。
- Next: 明确给出当前 tag tree 与 direct package tree 的比较结果。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
