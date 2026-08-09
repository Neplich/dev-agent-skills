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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `25bd4dbed66f3625883b2a2072dcd568eef569278521e1eac012e86f61347836`
- Skill overlay SHA-256: `840e4d3e20057f4834a3b010b4142d0e7be2f66540c525231dc34075db0dbbee`
- Judge schema SHA-256: `46c6f10cb2ee094e0f2d9b8cf0d9d794ebc801a301eb97187a76e961b4e37fd0`
- Eval definition SHA-256: `3e00fd5f68469b1dbad14f0a400fd8e41079d5a8aa0df077168fd2333bd41a39`
- Metadata SHA-256: `93577771a8ef98b760a14a69ae743909ae6d46791d7ed929dd703a6fc9855b54`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `data_inventory` | PASS | 交付报告逐项识别姓名、邮箱、IP、User-Agent、userId、事件名及其注册/分析入口和账号创建、分析等目的。 |
| `sharing_and_retention` | PASS | 报告确认向 ExampleAnalytics 共享 userId、邮箱、IP 和事件名，并指出内部库、日志、分析端及备份的保留期限、删除联动和供应商治理缺口。 |
| `user_rights` | PASS | 报告检查并明确指出访问、删除、导出、纠正及分析同意撤回/退出机制均未被实现或证明。 |
| `compliance_gaps` | PASS | 报告提供按优先级分类的同意、最小化、保留删除、第三方治理、权利流程和安全控制整改建议。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=da21f882704758587ca44f889b8ee407dbf02d8334de8546d9781960b0a34c12; fixture_sha256=fc7c85721e9b7bd81a9ba3e487c8f00f57880deb91ce00e1ae1258884cc231db; output_sha256=1ca4c84c17c3b386731103da8eb2ef7e1221538c2c073700b58ae8195e3b1b80; snapshot_sha256=8d3ffae122a336e0cb9ec3298f5e6297364889beca6f5b428e311d7b3c28e637
- Behavior: 生成并交付结构化隐私处理面报告，覆盖数据清单、共享保留、用户权利和整改建议，未修改业务代码。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=da21f882704758587ca44f889b8ee407dbf02d8334de8546d9781960b0a34c12; fixture_sha256=fc7c85721e9b7bd81a9ba3e487c8f00f57880deb91ce00e1ae1258884cc231db; output_sha256=6618a6dcdf176f01e149a9c0b5f4a2fefce5f90c6227a6e8612aa854db879098; snapshot_sha256=068c3ea9a97b6772a640dfe57de486512cb440fb7cd8b89eb8fde1af054113d2
- Behavior: 同样生成隐私处理面报告并覆盖主要审查范围，作为基线对照。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
