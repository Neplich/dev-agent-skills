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
- Identity schema: `2`
- target_skill_sha256: `09e738dc9988190b7f79b8aac551bd1674e0642fae4817109cb4551b9f01f0cd`
- eval_definition_sha256: `ee85b4030fea85acc8c079589b9268be5087962ef495cf3e3194580abf721432`
- metadata_sha256: `8cbc4de235b64dc94f1f26425c852e96d8c8a43534bff26146b8ba13fd8eb92c`
- fixture_sha256: `bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `086365b086fd130d9ef17a34e69f11d6786884f09ea0525a080792033b47d5cb`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `147ea0edbf82c8ca9a07d9d6ff0b589da90d3fd96bbb89bae4f44faf26cc1243`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_status_unconfirmed` | PASS | 明确标记为 `suspected / needs more evidence`，并说明当前不足以确认缺陷、不可复现且非环境敏感结论。 |
| `separates_impact_from_confidence` | PASS | 分别记录低置信度与潜在影响，并说明严重度不代表事实确定性。 |
| `requests_decisive_evidence` | PASS | 提出补充复现步骤、预期/实际、环境版本，并收集截图/录屏、控制台、网络和 trace 等证据。 |
| `avoids_confirmed_bug_write` | PASS | 持久化文件位于 unresolved 路径，内容明确标为 suspected / needs more evidence，且要求确认前不得按已确认缺陷排期；未创建 GitHub issue 或 confirmed bug。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; output_sha256=b85fe33399c6751c72793e62d40e664183fd5a465aa762ea08a944993e6200ce; snapshot_sha256=fa607c377fb44cd81d812a65045e849c18bb0373f45e7de0d93a529601e6c2a6
- Behavior: 正确保持待补证状态，区分影响与置信度，提出决定性补证计划，并仅创建明确未确认的调查记录。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; output_sha256=01aaa78c3415929656f5a2d371071cf8a98b6899d346a9c9f885fe9ce21a2c8c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样保持未确认状态并提出补证建议；未创建持久化记录，作为 fresh baseline 对照。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
