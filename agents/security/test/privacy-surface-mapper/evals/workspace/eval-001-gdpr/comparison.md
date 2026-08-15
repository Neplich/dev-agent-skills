# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-001-gdpr`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fc7c85721e9b7bd81a9ba3e487c8f00f57880deb91ce00e1ae1258884cc231db` from `agents/security/test/privacy-surface-mapper/evals/workspace/eval-001-gdpr`.
- Identity schema: `2`
- target_skill_sha256: `36470092bada7ef550e554a98c281f2fe94c427f5a20542e3fb5f13c69f3b496`
- eval_definition_sha256: `3e00fd5f68469b1dbad14f0a400fd8e41079d5a8aa0df077168fd2333bd41a39`
- metadata_sha256: `4d071b9edabea5e4f158bcdc27c2e5647782f2e593dd3fe3c48f455551d94297`
- fixture_sha256: `fc7c85721e9b7bd81a9ba3e487c8f00f57880deb91ce00e1ae1258884cc231db`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `46c6f10cb2ee094e0f2d9b8cf0d9d794ebc801a301eb97187a76e961b4e37fd0`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `da21f882704758587ca44f889b8ee407dbf02d8334de8546d9781960b0a34c12`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `04d179782a25ad87f73775d407c14368f4301d86a871528ca2b66e82792a813b`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `data_inventory` | PASS | 报告逐项列出姓名、邮箱、IP、User-Agent、用户 ID、行为事件，并追溯到注册代码、分析配置和处理目的。 |
| `sharing_and_retention` | PASS | 报告识别 ExampleAnalytics 共享、数据库与日志存储风险、明文邮箱/IP、供应商保障缺失及 retentionDays 为 null 的保留风险。 |
| `user_rights` | PASS | 报告检查并指出同意、访问、删除、导出和更正接口或流程均无实现证据，并提出覆盖第三方及备份的建议。 |
| `compliance_gaps` | PASS | 报告给出按优先级划分的合规缺口、数据最小化、同意、保留删除、供应商和用户权利整改建议。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=da21f882704758587ca44f889b8ee407dbf02d8334de8546d9781960b0a34c12; fixture_sha256=fc7c85721e9b7bd81a9ba3e487c8f00f57880deb91ce00e1ae1258884cc231db; output_sha256=b59036c74c84fbce66b195d21feafc3e96bfd968e551adaeb4d024e50d86dd7e; snapshot_sha256=751bfaba66cae05b89f8143976861e573dc020d2006191dcb247d0da63703fa6
- Behavior: 交付了结构化隐私处理面报告，基于代码、配置和文档证据覆盖数据清单、共享保留、用户权利及整改建议，并明确静态证据边界。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=da21f882704758587ca44f889b8ee407dbf02d8334de8546d9781960b0a34c12; fixture_sha256=fc7c85721e9b7bd81a9ba3e487c8f00f57880deb91ce00e1ae1258884cc231db; output_sha256=eeeb89008d738032aa9d2cb8119c5c2e288ec0806df4c092de3942284fa5529c; snapshot_sha256=66a352ebd5de17a173f8119a39623a08d69e11837083f605ff4ffe3231abbb6b
- Behavior: 新鲜基线同样交付了覆盖请求主题的隐私报告；作为比较上下文，未影响 with_skill 的独立判定。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
