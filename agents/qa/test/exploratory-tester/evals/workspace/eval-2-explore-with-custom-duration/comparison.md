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
- target_skill_sha256: `ad5f15f98798fd005013d9360ccfb1f546134b65d875e1399c704387da8bd759`
- eval_definition_sha256: `234873760fb9d0649d16f54118fbf0383fa2955b9451730f9429892d78a6d7e0`
- metadata_sha256: `4befffc2e8037477b9995f3ded3869d8476cd9a66637621d7f8e8d3fc8c6fed3`
- fixture_sha256: `58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `795b13efa8aba1d005ca8e2bf3be74790d6a011a9b79e7e9c3ef0bb4863b7e5d`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `95b19585ae663cfe50fef5d8a922d75ec357803535a13bbb323cdf9b1845fa29`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `1f8ea470403a23486f27834f156d91882ffb60f2aff635a7aa34b64347c884e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | 已交付包含目标 URL、5 分钟 timebox、探索 charter、改动面、环境信息及未验证前提的报告。 |
| `assertion_2` | PASS | 原始 trace 显示读取 TEST_SUITE.md、FLOW_INDEX.md、PRD、TRD、实现计划和环境资料；交付文件确认 feature-update 场景，并记录 cases/scripts/results/_reports 均无文件。 |
| `version_entry_and_subagent` | NOT_EXERCISED | 报告确认平台版本缺失即 blocked，并说明 harness、浏览器连接器和 Playwright 的入口顺序及选择理由；但实际 TC 未执行，subagent 执行未被独立证据验证。 |
| `assertion_3` | PASS | 报告区分 Observed issues、Suspicious but unconfirmed signals 和 Gaps not explored，并记录 DNS 网络错误及 toast/validation 风险。 |
| `assertion_4` | PASS | 交付报告包含实际 preflight/环境探测路径、curl DNS 失败证据、读取来源和覆盖范围，而非随机操作清单。 |
| `assertion_5` | PASS | 报告包含已知风险、明确的后续重跑步骤、优先级顺序及 bug-analyzer 交接所需证据建议。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=95b19585ae663cfe50fef5d8a922d75ec357803535a13bbb323cdf9b1845fa29; fixture_sha256=58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3; output_sha256=c386fd6401ab5086ac772c3b0a14f2cd34228bd274c084efb8fd76fac7c06e7c; snapshot_sha256=247a048c36b1300ffceeb6e0a580cf9873ccb17ddbd1bd6e48aaa434b1db9f78
- Behavior: 完成了结构化 preflight、charter、风险分层、阻塞证据和可交接报告，并更新 FLOW_INDEX.md；未执行 UI。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=95b19585ae663cfe50fef5d8a922d75ec357803535a13bbb323cdf9b1845fa29; fixture_sha256=58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3; output_sha256=3671382ea975f98782f65f5b4b7547df95c4eefad9b630d829169572cb7ba168; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 仅报告 DNS 阻塞和若干未判定项目，未提供完整 charter、改动面分析、入口判定、风险交接或交付文件。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 恢复 qa.example.test DNS 并提供平台版本。
- Next: 按已记录的 5 分钟 charter 重跑 UI 探索，并由 subagent 执行实际 TC。
- Next: 优先验证保存、取消/丢弃、未保存状态及 validation/toast precedence。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
