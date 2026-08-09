# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-005-mapped-search-security`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d` from `agents/security/test/appsec-checklist/evals/workspace/eval-005-mapped-search-security`.
- Fixture SHA-256: `fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d`
- Prompt SHA-256: `e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `812b371fc30792cb2b0cf8d96079b3244c95b93efab7638e085d4e955d6ea42c`
- Skill overlay SHA-256: `33e7e73c99fb4e7a6f2d6ab5104b8298fc067235a29614a6e32ee61035051666`
- Judge schema SHA-256: `fe1f59786edfa4e3b7ee12601522d693ef12a42cdfce9b4a390ad6d7b95d03d2`
- Eval definition SHA-256: `d863b13d3e997477097b1a2de108729923e21619e10b2847114ea312db1c1bc8`
- Metadata SHA-256: `44e3487a1b0a940b7bf23d73f980b7d71bd0be1a4d04a13c48606fd67383de8a`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 输出识别了 change-map、required_docs 及目标文档，但锁定证据没有证明实际读取顺序或是否遍历了无关文档。 |
| `verifies_against_code` | PASS | 明确指出代码将 query 直接插入 SQL，并识别其与文档所称 parameterized query 的不一致。 |
| `treats_unverified_as_low_trust` | PASS | 明确识别 last_verified_version 为 unverified，并将文档作为低信任导航，转而依据代码事实。 |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | 输出正确将下一步退回 pm-agent，但因缺少 handoff packet、feature_path 和 PM 分类，锁定证据不足以要求后续 issue 创建及 Security 过程报告。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de; fixture_sha256=fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d; output_sha256=27fd85a20be77b40f332ff5dd8f6699fc858a0a84c6694a542f409bb7e8bf99b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了文档映射、unverified 状态及代码与文档的安全事实冲突，并在缺少合法交接信息时退回 pm-agent；未继续执行无法授权或定位的后续升级步骤。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de; fixture_sha256=fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d; output_sha256=6c80f1ab9f16d3bf2c919839d4e75cd4b293f2f028ce382a64dd7be1d1edc3a9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 独立识别 SQL 注入风险及文档/代码不一致，并提出修复建议，但没有按 PM/Security 交接流程升级。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 由 pm-agent 补充合法 handoff packet、feature_path 和分类后，验证 issue 创建及 Security 过程报告。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
