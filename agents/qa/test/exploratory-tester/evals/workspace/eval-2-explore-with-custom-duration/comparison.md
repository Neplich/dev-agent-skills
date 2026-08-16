# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-002-explore-with-custom-duration`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3` from `agents/qa/test/exploratory-tester/evals/workspace/eval-2-explore-with-custom-duration`.
- Identity schema: `2`
- target_skill_sha256: `a0ccbf8ef4a1c709d054888b55b087565575c66027bff8bd5b33273b116324d3`
- eval_definition_sha256: `234873760fb9d0649d16f54118fbf0383fa2955b9451730f9429892d78a6d7e0`
- metadata_sha256: `4befffc2e8037477b9995f3ded3869d8476cd9a66637621d7f8e8d3fc8c6fed3`
- fixture_sha256: `58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `795b13efa8aba1d005ca8e2bf3be74790d6a011a9b79e7e9c3ef0bb4863b7e5d`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `95b19585ae663cfe50fef5d8a922d75ec357803535a13bbb323cdf9b1845fa29`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `649841709df98de32c59aff088c94eff0d9bbe6820d42c21a8e49cd3cf9838cb`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | 交付报告包含 5 分钟 charter、目标 URL、changed surface、环境信息及未验证前提。 |
| `assertion_2` | PASS | 报告记录已读取 TEST_SUITE.md、FLOW_INDEX.md 及不存在的 cases、scripts、历史结果，并确认 feature-update；未创建 TC/script 是因为没有可执行场景。 |
| `version_entry_and_subagent` | NOT_EXERCISED | 报告确认平台版本缺失并将执行标记为 blocked，同时记录了 harness → browser connector → Playwright 顺序及 subagent 默认规则；但没有实际 TC 执行或 subagent 委派。 |
| `assertion_3` | PASS | 交付报告明确分为 Observed issues（无确认问题）、Suspicious but unconfirmed signals 和 Gaps not explored。 |
| `assertion_4` | PASS | 报告包含 charter、实际 URL 检查路径、DNS 错误、读取的文档和未覆盖项，提供了可追溯 evidence references。 |
| `assertion_5` | PASS | 报告记录 toast 可能遮盖校验错误的风险，并给出恢复 DNS、记录版本、重跑路径及升级条件。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=95b19585ae663cfe50fef5d8a922d75ec357803535a13bbb323cdf9b1845fa29; fixture_sha256=58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3; output_sha256=342ec6332620f7232cf6d90b119d1e25d62980a07bb393a217b07bed50b6b21f; snapshot_sha256=01baa3d439b7d785a899f80dd20cadf29fc525fa6fc3f99b53c56359a8227796
- Behavior: 完成了结构化预检、范围章程、风险分层和交接产物；在执行前因环境与版本门禁阻塞。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=95b19585ae663cfe50fef5d8a922d75ec357803535a13bbb323cdf9b1845fa29; fixture_sha256=58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3; output_sha256=b714d08424b0b2e3dba58133614d480977bef4d02592d4ef4611dbb0bea85ce1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 仅报告环境不可达和无法执行，未提供结构化 charter、完整 preflight 入口决策或交接文件。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 恢复 QA URL 的 DNS/可达性。
- Next: 记录浏览器/platform 版本并按既定入口顺序重新执行 5 分钟探索。
- Next: 执行保存、取消、未保存状态、校验与 toast 路径；仅在可复现时升级风险。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
