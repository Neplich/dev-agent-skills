# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-012-staged-metadata-rollback`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1013313f9177f2e4b64118a15325ba0a4da0ec26b6c32604368f1f754b57e620` from `agents/docs/test/docs-audit/evals/workspace/eval-012-staged-metadata-rollback`.
- Identity schema: `2`
- target_skill_sha256: `dafd53371901dfd724f88c70262b157e59494d29da1c613d0ef130564b6ff4f9`
- eval_definition_sha256: `885108a0e0e9ce48751816455b91da0ec400a08bb7d3a722984a36e4221d1938`
- metadata_sha256: `86b2ab0ad4bcb3fb98728ca8ff1375ff58d1094876353cbeafc325bf7593eb63`
- fixture_sha256: `1013313f9177f2e4b64118a15325ba0a4da0ec26b6c32604368f1f754b57e620`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `73f9308006ffa877e1ed5f74c8eef2e3a2b3222e98dd5485cfd0ba5e210de92a`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `4c059264a7527dcf6082f43bc5cacdf327f947505e6d5f9721fd10e71b64fdcb`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `7e61bd8eca6431729aee1f3be4656be0a4348119eb1218623bafd54cfaead2ab`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_non_content_candidate_drift` | FAIL | 候选引用了 staged.name-status 并识别删除、重命名和类型变化，但未覆盖 catalog-items.md 的 100644→100755 模式变化，也未明确覆盖其内容变化。 |
| `rejects_every_unauthorized_transformation` | FAIL | 输出阻塞了删除 release note、重命名、普通文件转符号链接及异常链接，但遗漏了 executable mode 变化和 catalog-items.md 的授权内容转换，未逐类覆盖全部越界项。 |
| `rechecks_committed_candidate_boundaries` | NOT_EXERCISED | 当前锁定证据没有已形成的 committed candidate 或 handoff；输出已将当前 staged 快照视为不可消费并要求重新启动审计，因此后续边界复核尚未发生。 |
| `rolls_back_only_the_failed_attempt` | NOT_EXERCISED | before/after 捕获只证明宿主状态未变，未证明隔离 attempt、本次草稿清理或误触状态恢复操作已实际执行；该后续清理步骤缺少运行时证据。 |
| `proves_host_state_restoration` | PASS | 输出给出 status、index diff、worktree diff 的 before/after 相同证据，并结合 trace 中 ref 未变化及相关路径身份一致，继续保持 blocked 而未暴露成功。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4c059264a7527dcf6082f43bc5cacdf327f947505e6d5f9721fd10e71b64fdcb; fixture_sha256=1013313f9177f2e4b64118a15325ba0a4da0ec26b6c32604368f1f754b57e620; output_sha256=5ba8373e71e62a268e3faf5da567e3bc4dabba0104bc41518d2972ea35635969; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确判定不能继续，识别证据哈希不一致、删除/重命名/符号链接等主要风险，并证明宿主捕获状态未变化；但遗漏 executable mode 与 catalog-items 内容变化。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4c059264a7527dcf6082f43bc5cacdf327f947505e6d5f9721fd10e71b64fdcb; fixture_sha256=1013313f9177f2e4b64118a15325ba0a4da0ec26b6c32604368f1f754b57e620; output_sha256=68e55b67eca9ada79dd7b25ca2d8202b6d261d91266f4caf5a7353e6e2205f0c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样判定阻塞并识别部分删除、重命名、符号链接和哈希问题，但遗漏更多边界细节；仅作基线对比。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- detects_non_content_candidate_drift
- rejects_every_unauthorized_transformation
- Next: 重新生成并校验完整 staged candidate，明确覆盖模式、内容、路径和对象类型边界。
- Next: 形成 committed candidate 与 handoff 后，重新验证同一授权边界并取得完整清理/恢复运行时证据。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
