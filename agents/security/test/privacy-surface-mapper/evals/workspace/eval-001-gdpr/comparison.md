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
- Fixture SHA-256: `fc7c85721e9b7bd81a9ba3e487c8f00f57880deb91ce00e1ae1258884cc231db`
- Prompt SHA-256: `da21f882704758587ca44f889b8ee407dbf02d8334de8546d9781960b0a34c12`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `25bd4dbed66f3625883b2a2072dcd568eef569278521e1eac012e86f61347836`
- Skill overlay SHA-256: `4894e45a78f6999eae63835919f4d9ac1eddcf0e15978742e5f90f2ebd544560`
- Judge schema SHA-256: `46c6f10cb2ee094e0f2d9b8cf0d9d794ebc801a301eb97187a76e961b4e37fd0`
- Eval definition SHA-256: `3e00fd5f68469b1dbad14f0a400fd8e41079d5a8aa0df077168fd2333bd41a39`
- Metadata SHA-256: `93577771a8ef98b760a14a69ae743909ae6d46791d7ed929dd703a6fc9855b54`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `data_inventory` | PASS | 报告逐项列出 name、email、IP、User-Agent、userId 和 account_created，并追溯到注册代码、分析配置及账号创建/产品分析目的。 |
| `sharing_and_retention` | PASS | 报告识别 ExampleAnalytics 接收的字段、默认开启和未要求同意的配置，并指出数据库、日志、分析服务、备份、地域、跨境、合同和保留期限证据缺失。 |
| `user_rights` | PASS | 报告检查并标明访问、删除、导出、可携带、更正及撤回/退出机制均未发现，且提出覆盖数据库、日志、分析副本和备份的改进要求。 |
| `compliance_gaps` | PASS | 报告给出高风险隐私缺口、合规影响、上线阻断项、责任团队和具体整改建议，包括同意、最小化、保留删除、供应商治理及用户权利流程。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=da21f882704758587ca44f889b8ee407dbf02d8334de8546d9781960b0a34c12; fixture_sha256=fc7c85721e9b7bd81a9ba3e487c8f00f57880deb91ce00e1ae1258884cc231db; output_sha256=e3e9ffac33237cabb68c687d5fee218241139da9829607fafef0f2182db6a1f9; snapshot_sha256=ccae304d4e43cbada741f44a9980aec427b414c97077d7ca8ab8a152b22eab99
- Behavior: 交付了有证据追溯的隐私处理面报告，完整覆盖数据清单、共享与保留、用户权利及整改建议。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=da21f882704758587ca44f889b8ee407dbf02d8334de8546d9781960b0a34c12; fixture_sha256=fc7c85721e9b7bd81a9ba3e487c8f00f57880deb91ce00e1ae1258884cc231db; output_sha256=ff836d9bf1a28a030e9c8f277ea7fbb91d91261f2488db128668bbbf5fc0fa8d; snapshot_sha256=3e437a8eb037808304c64bf5d40bd34019e3f9c8b6916e036ee21eaf822fc498
- Behavior: 同样交付了较完整的隐私处理面报告，作为 fresh baseline；with_skill 报告额外明确证据新鲜度、配置与运行时差异及责任边界。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
