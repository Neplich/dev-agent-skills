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
- target_skill_sha256: `a5e0bb043d61dbbb218e7d7efc08374e0d16a4d7aaa3b31817f2038830c90941`
- eval_definition_sha256: `885108a0e0e9ce48751816455b91da0ec400a08bb7d3a722984a36e4221d1938`
- metadata_sha256: `86b2ab0ad4bcb3fb98728ca8ff1375ff58d1094876353cbeafc325bf7593eb63`
- fixture_sha256: `1013313f9177f2e4b64118a15325ba0a4da0ec26b6c32604368f1f754b57e620`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `73f9308006ffa877e1ed5f74c8eef2e3a2b3222e98dd5485cfd0ba5e210de92a`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `4c059264a7527dcf6082f43bc5cacdf327f947505e6d5f9721fd10e71b64fdcb`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `d7e2242fcdf83209e6c0cb5ec9544aa009e79488a72f81ebd4bf387289fbabec`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_non_content_candidate_drift` | PASS | 候选输出引用并概述 staged.raw/name-status/summary/patch，覆盖 100755、120000、重命名、删除及新增符号链接，并指出对象哈希与路径语义，而非仅比较文本。 |
| `rejects_every_unauthorized_transformation` | PASS | 候选输出逐项列出六类候选变更，并以 blocked 结论处理模式变化、类型替换、重命名、删除及两个符号链接，没有将其降级为无害差异。 |
| `rechecks_committed_candidate_boundaries` | PASS | 候选明确指出 staged 结果不等于已提交、锚定、handoff 或 fast-forward，并要求重新生成完整候选审计记录。 |
| `rolls_back_only_the_failed_attempt` | NOT_EXERCISED | 锁定证据显示清理前后宿主状态完全相同；候选正确报告残留并要求保留、处置 staged/unstaged 路径，但没有可执行的清理运行时或交付快照来证明实际隔离回滚。 |
| `proves_host_state_restoration` | PASS | 候选覆盖 ref、宿主 status/index/worktree 记录及候选对象身份，并在无法证明恢复时维持 blocked、指出残留处置要求，没有宣称成功。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4c059264a7527dcf6082f43bc5cacdf327f947505e6d5f9721fd10e71b64fdcb; fixture_sha256=1013313f9177f2e4b64118a15325ba0a4da0ec26b6c32604368f1f754b57e620; output_sha256=02c25dae7a58367b88d9878c680f57f97f9b06817ff7d3a5b93c7d94aa2dae10; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确阻塞发布，识别候选的 Git 类型、模式、路径和对象风险，并拒绝把隔离 staged 证据当作最终 authority；宿主清理本身未执行。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4c059264a7527dcf6082f43bc5cacdf327f947505e6d5f9721fd10e71b64fdcb; fixture_sha256=1013313f9177f2e4b64118a15325ba0a4da0ec26b6c32604368f1f754b57e620; output_sha256=fd90f5b0bd78111fbbf261f297e170617cde4c0c458b946a0a0bf715f2af8cce; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样阻塞发布并识别主要候选风险，但证据边界和后续 authority/审计绑定说明较少；仅作 fresh baseline 对照。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 在获得必要运行时证据或确认后，单独执行并记录仅针对失败 attempt 的清理，再复核 ref、index、worktree 及相关路径身份。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
