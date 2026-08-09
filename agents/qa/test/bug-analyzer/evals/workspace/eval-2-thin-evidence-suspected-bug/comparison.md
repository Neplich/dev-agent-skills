# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-002-thin-evidence-suspected-bug`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266` from `agents/qa/test/bug-analyzer/evals/workspace/eval-2-thin-evidence-suspected-bug`.
- Fixture SHA-256: `bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266`
- Prompt SHA-256: `78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0d6c4b717279e8edddeea8100d93e004d25b98b502e0ca114092a3f0c007a52f`
- Skill overlay SHA-256: `4d1289a2f580cb07efcd85d24fb079acfc635807339f9469fa7653101393ff87`
- Judge schema SHA-256: `086365b086fd130d9ef17a34e69f11d6786884f09ea0525a080792033b47d5cb`
- Eval definition SHA-256: `ee85b4030fea85acc8c079589b9268be5087962ef495cf3e3194580abf721432`
- Metadata SHA-256: `8fd7c615ab5c3a7f7edc961336d40be79c05d55d0c11dd967998bbb2abd4e9d7`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_status_unconfirmed` | PASS | 明确分类为 `suspected / needs more evidence`，并说明不足以确认缺陷、不可复现或判断环境敏感。 |
| `separates_impact_from_confidence` | PASS | 交付记录分别列出低置信度、证据缺口与潜在数据丢失/可用性影响，未以严重度替代确定性。 |
| `requests_decisive_evidence` | PASS | 建议补采步骤、期望/实际结果、环境版本、频率，并收集截图/录屏、控制台、网络响应和服务端日志。 |
| `avoids_confirmed_bug_write` | PASS | 创建的文件明确标为待补证调查记录，并明确不应标记为 confirmed bug；没有创建 GitHub issue 或确认缺陷记录。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; output_sha256=ef508896975978f43f96586ace78912e13a2b6bcbe1fc995aa66c3c7ac8f48bf; snapshot_sha256=670d133ddc39593fc8bd405d41c54b273ed82cc81ff5b9bdb9c2b6ed82d10e5c
- Behavior: 保持反馈为低置信度的待补证调查，区分影响与证据强度，提出具体补证计划，并仅交付调查记录。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; output_sha256=bd7322ebfc2fb8bc98f8e75fec5733ab5e820011a6dc914e72fbcfc9164e230f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样保持未确认状态并提出补证建议，但未交付持久化调查记录。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
