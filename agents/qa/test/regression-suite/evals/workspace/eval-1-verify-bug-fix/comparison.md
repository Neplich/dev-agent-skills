# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `regression-suite`
- Eval: `eval-001-verify-bug-fix`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308` from `agents/qa/test/regression-suite/evals/workspace/eval-1-verify-bug-fix`.
- Fixture SHA-256: `de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308`
- Prompt SHA-256: `c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8289acf8e27bfd57efcbcc6d726b9bfaa4df0b2cb5c60400d61eca4c6f8c65d4`
- Skill overlay SHA-256: `a284e7eb3465da68b2d3792a2435d75549c3a3732ed503ef22754fbfde0a19d1`
- Judge schema SHA-256: `2c18050b9a27d5dccf92b0604097b9078533d47105266364099eafbf3833aad8`
- Eval definition SHA-256: `8ca6ea4c46c7a5a2c854d9ff5def7ea0ec612ddbf9888a829e50de270f1b84c4`
- Metadata SHA-256: `732278c998a10f6e6333dc13e2fc4edfbaed96da1abb806d2dc29682a3a79f75`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | NOT_EXERCISED | 报告引用 BUG-001、PR-001，并沿用原始失败、期望行为及相邻风险界定范围；但读取先后顺序无法由锁定证据证明。 |
| `qa` | NOT_EXERCISED | 报告列出 TEST_SUITE.md、FLOW_INDEX.md、TC-001 case 和 script，并说明历史 results/_reports 不存在；但执行前读取顺序无法由锁定证据证明。 |
| `assertion_3` | NOT_EXERCISED | 报告明确将修复验证、原始失败复查和期望修复行为标为 blocked，但缺少运行时证据，实际修复行为未被执行验证。 |
| `assertion_4` | PASS | 报告按 feature-update 范围覆盖原始登录、无效凭据、锁定账户及共享序列化路径，未扩展为全量 active E2E。 |
| `alignment_version_archive` | FAIL | 报告确认 PRD/TRD/IMPLEMENTATION_PLAN 对齐并将平台版本标记为 blocked；但锁定交付物写入 _reports/test-reports...md，而非要求的 results/.../result.md 和 testcase.snapshot.md。 |
| `assertion_5` | PASS | 报告同时给出 blocked/not executed、evidence_confidence: low 和 release_recommendation: needs more verification，并避免宣称已就绪。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0; fixture_sha256=de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308; output_sha256=5198e500ae4b4a28514287628a899c53bfdec4e1fd9aa158b31d096e0d4c7201; snapshot_sha256=c39e88cdbcc366d6d1e3f05275e12ffe4cab6515926362358bf72c1c68d63a59
- Behavior: 生成了结构化的 BLOCKED 回归报告，明确范围、对齐门禁、证据置信度和发布建议，但未执行运行时验证，并产生了不符合归档要求的 _reports 文件。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0; fixture_sha256=de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308; output_sha256=631e63a478fcaa1cd01116641dcfbe9e3ec464049a5d7c560dc1de8b72d6d689; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样因缺少 package.json 和 QA_BASE_URL 无法执行验证；仅给出简要阻塞结论，未交付回归报告。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 回归报告被写入 _reports，而不是要求追加的 results/TC-NNN-<short-slug>/{platform-version}/result.md 和 testcase.snapshot.md。
- Next: 补齐可运行 harness 或配置 QA_BASE_URL。
- Next: 在声明的平台版本上执行原始登录、无效凭据和锁定账户路径。
- Next: 按要求将结果追加到 results/.../result.md 和 testcase.snapshot.md，保留历史结果。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
