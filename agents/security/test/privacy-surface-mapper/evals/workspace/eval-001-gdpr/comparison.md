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
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
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
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `3e00fd5f68469b1dbad14f0a400fd8e41079d5a8aa0df077168fd2333bd41a39`
- Metadata SHA-256: `93577771a8ef98b760a14a69ae743909ae6d46791d7ed929dd703a6fc9855b54`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `data_inventory` | PASS | 报告逐项识别姓名、邮箱、IP、User-Agent、账号 ID 和行为事件，并记录注册代码、分析配置中的收集入口及处理目的。 |
| `sharing_and_retention` | PASS | 报告确认向 ExampleAnalytics 共享账号 ID、邮箱和 IP，并识别数据库、日志、分析供应商、备份等保留期限、删除和供应商治理缺口。 |
| `user_rights` | PASS | 报告检查访问、更正、删除、导出/可携带、同意撤回及其他权利，明确指出缺少接口、流程和验证证据。 |
| `compliance_gaps` | PASS | 报告给出高风险缺口、上线阻断项、责任团队、改进建议和关闭证据，覆盖同意、数据最小化、生命周期、用户权利及第三方治理。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=da21f882704758587ca44f889b8ee407dbf02d8334de8546d9781960b0a34c12; fixture_sha256=fc7c85721e9b7bd81a9ba3e487c8f00f57880deb91ce00e1ae1258884cc231db; output_sha256=fb12b3e2ad2beda98df91b2d5200853016f009f24e5edf8fe5c400e5580a19c6; snapshot_sha256=7f90fe01a4731d0bd7a81d66e257dea917ba5023a48318c603064e093b3cc491
- Behavior: Produced a detailed, evidence-qualified privacy map covering the requested processing surface and actionable compliance remediation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=da21f882704758587ca44f889b8ee407dbf02d8334de8546d9781960b0a34c12; fixture_sha256=fc7c85721e9b7bd81a9ba3e487c8f00f57880deb91ce00e1ae1258884cc231db; output_sha256=934260aeadb4d8c0bbd4d6940538fd1a9da7a6e2f115bf8dacc99ad8d00c4ef2; snapshot_sha256=971928ff91631fe38095de066487e10679822e1b8b81079a0cb4cfbc4537c870
- Behavior: Produced a comprehensive privacy-processing report with traceable inventory, sharing, retention, rights, and remediation coverage.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Skill overlay SHA-256: `4e2d7a3ffa0fc7b4cc84f02f24df4e35de821cbc6e0c580a1427e37709efb43b`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `3e00fd5f68469b1dbad14f0a400fd8e41079d5a8aa0df077168fd2333bd41a39`
- Metadata SHA-256: `93577771a8ef98b760a14a69ae743909ae6d46791d7ed929dd703a6fc9855b54`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `data_inventory` | PASS | With_skill report identifies name, email, IP, User-Agent, userId, and account_created data; traces registration and analytics entry points to source/config lines; and distinguishes stated versus inferred purposes. |
| `sharing_and_retention` | PASS | With_skill report identifies ExampleAnalytics as receiving userId, email, IP, and eventName, and flags missing vendor governance, retention rules, deletion linkage, backups, logs, and supplier copies. |
| `user_rights` | PASS | With_skill report checks access, deletion, export/portability, correction, consent withdrawal, and related implementation gaps, including third-party data coverage. |
| `compliance_gaps` | PASS | With_skill report provides prioritized privacy risks and concrete recommendations covering consent, minimization, retention/deletion, rights workflows, third-party governance, documentation, ownership, and release readiness. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=da21f882704758587ca44f889b8ee407dbf02d8334de8546d9781960b0a34c12; fixture_sha256=fc7c85721e9b7bd81a9ba3e487c8f00f57880deb91ce00e1ae1258884cc231db; output_sha256=cad80c97d0c2a8842cf77b5c63840f40b0ec570b082ae6ed422ea6f2b8ad8ebd; snapshot_sha256=4e0fcf318b181ce0282d8d63e5ef708eff495cd89b686b46343a96b7fbd6c7a4
- Behavior: Produced a more structured, evidence-qualified privacy map with field inventory, data flow, sharing, retention, rights, prioritized gaps, recommendations, and handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=da21f882704758587ca44f889b8ee407dbf02d8334de8546d9781960b0a34c12; fixture_sha256=fc7c85721e9b7bd81a9ba3e487c8f00f57880deb91ce00e1ae1258884cc231db; output_sha256=f2186bbec22938ac67bc0233cd42586f6bb9858311570cceb03fcdb80bfc2a9b; snapshot_sha256=c03420b8a19ea531378314760e68494eebaa7fbeb8b57ca04ed99057587cb5b2
- Behavior: Produced a detailed traceable privacy-processing report covering all requested areas and identified major launch risks.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `25bd4dbed66f3625883b2a2072dcd568eef569278521e1eac012e86f61347836`
- Skill overlay SHA-256: `4e2d7a3ffa0fc7b4cc84f02f24df4e35de821cbc6e0c580a1427e37709efb43b`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `3e00fd5f68469b1dbad14f0a400fd8e41079d5a8aa0df077168fd2333bd41a39`
- Metadata SHA-256: `93577771a8ef98b760a14a69ae743909ae6d46791d7ed929dd703a6fc9855b54`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `data_inventory` | PASS | With_skill identifies name, email, IP, User-Agent, user ID, and account_created, with collection paths, destinations, purposes, and traceable code/config/PRD evidence. |
| `sharing_and_retention` | PASS | With_skill identifies ExampleAnalytics sharing and flags undefined database, log, analytics, backup, and vendor retention/deletion controls. |
| `user_rights` | PASS | With_skill checks access, deletion, export, correction, restriction/opposition, consent, withdrawal, identity verification, and vendor propagation, identifying unsupported or missing mechanisms. |
| `compliance_gaps` | PASS | With_skill provides risk-rated gaps and actionable remediation covering consent, minimization, retention/deletion, vendor governance, rights workflows, logging, security, and release gates. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=da21f882704758587ca44f889b8ee407dbf02d8334de8546d9781960b0a34c12; fixture_sha256=fc7c85721e9b7bd81a9ba3e487c8f00f57880deb91ce00e1ae1258884cc231db; output_sha256=b48814d70384649910e6d1b19806cb9baf42cfed1b040101a561a6f8ba0cf1e8; snapshot_sha256=9bab60e851701b8836b53e50b8552f08ca358b0c462b96b3a4be8feac405b87f
- Behavior: Produced a more structured and explicitly traceable privacy map, clearly distinguishing confirmed evidence from unverified infrastructure/runtime facts and providing risk-rated remediation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=da21f882704758587ca44f889b8ee407dbf02d8334de8546d9781960b0a34c12; fixture_sha256=fc7c85721e9b7bd81a9ba3e487c8f00f57880deb91ce00e1ae1258884cc231db; output_sha256=b9822234f6dc0daaf027478c1cc6ea8f35e70b171a7e5feb0661b935138e2540; snapshot_sha256=745278897d7f986b7c3d120a87e6e0f335bc1b9284da3b64f1c88ddbfebb1dcb
- Behavior: Produced a substantive privacy processing-surface report with traceable inventory, sharing, retention, rights gaps, and remediation.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ce73f0c2e691c2e71d4792a4ff83efe02c3a6714b22fe5c3733a875118131db8`
- Skill overlay SHA-256: `cd8ee54ef003ea53bd486a0be35c70dcd1362f3fd307cff51efdedb756e33a7d`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `3e00fd5f68469b1dbad14f0a400fd8e41079d5a8aa0df077168fd2333bd41a39`
- Metadata SHA-256: `93577771a8ef98b760a14a69ae743909ae6d46791d7ed929dd703a6fc9855b54`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `data_inventory` | PASS | with_skill 输出列出姓名、邮箱、IP、User-Agent、用户 ID 和 account_created 事件，并追溯到 registration.js、analytics.json 和 PRD，说明了注册数据库及分析入口和处理目的。 |
| `sharing_and_retention` | PASS | with_skill 输出识别 ExampleAnalytics 接收的字段、默认开启及无需同意配置，并覆盖数据库、分析、日志和备份的保留期限、删除联动、供应商地域/DPA/分包商等缺口。 |
| `user_rights` | PASS | with_skill 输出逐项检查访问、更正、删除、导出、撤回/反对处理和告知，明确未发现相关接口或流程，并提出覆盖数据库、分析商、日志和备份的实现建议。 |
| `compliance_gaps` | PASS | with_skill 输出按 HIGH/MEDIUM 分级隐私风险，并给出默认关闭分析、数据最小化、保留删除、用户权利、供应商审查和安全控制等责任分工与整改建议。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=da21f882704758587ca44f889b8ee407dbf02d8334de8546d9781960b0a34c12; fixture_sha256=fc7c85721e9b7bd81a9ba3e487c8f00f57880deb91ce00e1ae1258884cc231db; output_sha256=cb3fac68b17622de04e3d585125a916b9eb2286df025e45942c7ba7d081d24bc; snapshot_sha256=c9494ccdde79e0d7af3bb3efbd717d3a2bbfc9e0032c8913719942d510408d4c
- Behavior: 生成结构化隐私处理面报告，结合原始代码和配置证据，明确区分已证实事实与未证实控制，并提出分级整改和上线判断。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=da21f882704758587ca44f889b8ee407dbf02d8334de8546d9781960b0a34c12; fixture_sha256=fc7c85721e9b7bd81a9ba3e487c8f00f57880deb91ce00e1ae1258884cc231db; output_sha256=9c895f42611264a1fdf0a4b22f3197e695c8d985244bec2cb11e5ccf4c8c1810; snapshot_sha256=73db2724b18a83290147e537bb819b601d57cbf796634857762e3a4b2157778e
- Behavior: 生成了较完整且可追溯的隐私处理面报告，覆盖数据清单、共享、保留、用户权利和整改建议。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `32486beb9db21ed173f2083e3323014ff05de4963e7a8b1d84d40eb43ab3aa33`
- Skill overlay SHA-256: `874b129b045f44af288c1af739a4a66f07931a151f79399740585f1fce30c452`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `3e00fd5f68469b1dbad14f0a400fd8e41079d5a8aa0df077168fd2333bd41a39`
- Metadata SHA-256: `93577771a8ef98b760a14a69ae743909ae6d46791d7ed929dd703a6fc9855b54`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `data_inventory` | PASS | with_skill 报告逐项识别 name、email、IP、userAgent、userId 和 account_created，并列出注册请求、数据库及分析事件入口、用途和 E1-E4 证据追溯。 |
| `sharing_and_retention` | PASS | 报告明确识别 ExampleAnalytics 接收 userId、原始 email、原始 IP，指出 retentionDays 为 null，并覆盖数据库、日志、备份及第三方删除和保留规则缺口。 |
| `user_rights` | PASS | 报告逐项检查访问、删除、导出、更正及分析撤回，均基于仓库证据标为未发现，并提出认证请求入口、级联处理、SLA 和验证要求。 |
| `compliance_gaps` | PASS | 报告按 P0/P1/P2 给出同意、最小化、第三方共享、保留删除、用户权利、数据清单一致性和安全控制缺口及整改建议。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=da21f882704758587ca44f889b8ee407dbf02d8334de8546d9781960b0a34c12; fixture_sha256=fc7c85721e9b7bd81a9ba3e487c8f00f57880deb91ce00e1ae1258884cc231db; output_sha256=c0f9c416268db45a892064bd4eea6c71029da5a69f63ff37318ecbf2d7d6d58b; snapshot_sha256=3eff6ad8944d083079cbd7879ea62f9f0b171560a28fb4c0334ed7b4b991479b
- Behavior: 生成结构化、带证据编号和来源行号的隐私处理面报告，完整覆盖四项要求，并明确区分已确认事实与证据缺失。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=da21f882704758587ca44f889b8ee407dbf02d8334de8546d9781960b0a34c12; fixture_sha256=fc7c85721e9b7bd81a9ba3e487c8f00f57880deb91ce00e1ae1258884cc231db; output_sha256=296395d919e41013c287a92a2d241c620589d1bef0391a8da21d23174510cdfc; snapshot_sha256=261f55e41528d6951d9718c506a4e945addf4fe894f858863f972dd85f32b3fa
- Behavior: 生成了内容完整的隐私处理面报告，覆盖数据清单、共享、保留、权利和整改建议，并声明未修改实现代码。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

# Eval Result: eval-001-gdpr

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-001-gdpr`
- Test case: GDPR Compliance Check
- Workspace: `workspace/eval-001-gdpr`
- Natural user prompt:

> pm-agent has completed entry classification and routed this confirmed `data-collection` security scope to privacy-surface-mapper. Use the PM handoff packet in workspace `PM_HANDOFF.md` and the confirmed source document `docs/pm/data-collection/PRD.md`. Map the personal data collection and check GDPR compliance.

- Expected artifact: Structured privacy surface map that identifies personal data, processing purpose, third-party sharing, user-rights gaps, and compliance risks.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/privacy-surface-mapper--eval-001-gdpr/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `364f34fef102662b30171eb4eaf54d781e387c635f07b6d450fd6bf48dadfdb6`。
- Lane isolation: 先完成并销毁全部 `without_skill` 独立顶层临时目录，再创建任何 `with_skill` 目录；每条 lane 使用独立的顶层临时 workspace、`HOME` 与 `CODEX_HOME`，不存在可供另一条 candidate 读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt 与相同初始 fixture；仅 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 skill，`without_skill` 未安装任何目标 skill。
- Evidence isolation: 所有 candidate 会话结束并删除各自临时根后，才将内存中的最终 workspace 快照与 transcript 持久化到 runtime root；candidate transcript 泄漏扫描未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、judge/verdict 或 expected output/assertion 脚手架。
- Judge: candidate 全部结束后，由第三个独立、只读的 fresh Codex 会话依据当前 assertions、两条 candidate 输出、transcript 与最终 workspace 快照判定。

## Latest Result

- Behavior result: **PASS**（PASS 4 / FAIL 0 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: PASS

## Historical Contract Note

上一份 durable comparison 基于 issue #234 修复前会向 baseline 泄漏规则的旧契约，因此标记为 `BLOCKED`。本轮使用当前无泄漏 prompt/fixture 重新生成两条 lane，未复用旧 baseline 或旧结论。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `data_inventory`<br>识别个人数据类型、收集入口和处理目的 | PASS | 最终 privacy-map.md 明确列出姓名、邮箱、IP、User-Agent/设备信息、用户 ID 和行为事件，并以 registration.js、PRD 和 analytics.json 为证据，说明收集入口及账号创建、运营安全和产品分析目的。 | PASS | 最终 PRIVACY_SURFACE_REPORT.md 明确列出个人数据、入口、证据和处理目的。 |
| `sharing_and_retention`<br>识别第三方共享、存储或保留相关风险 | PASS | 报告明确识别 ExampleAnalytics 第三方共享、共享字段和未记录的 DPA/子处理者/地区/跨境传输信息，并指出 retentionDays=null 及数据库、日志保留期限未定义。 | PASS | 报告明确识别 ExampleAnalytics 共享、提供方治理/传输缺口及无界分析保留和其他保留期限缺失。 |
| `user_rights`<br>检查访问、删除、导出或同意等用户权利支持情况 | PASS | 报告逐项检查访问、删除、纠正、可携带/导出，并补充限制、反对和撤回同意；明确说明未发现对应 endpoint、workflow 或分析侧传播机制。 | PASS | 报告逐项评估访问、纠正、删除、限制、反对、可携带和同意撤回支持，并给出未实现/未证明结论。 |
| `compliance_gaps`<br>给出隐私合规缺口和改进建议 | PASS | 报告明确指出默认启用分析且无需同意、目的/法律依据缺失、数据最小化不足、保留未定义、第三方治理与跨境证据缺失、权利流程缺失，并给出按 Engineer、DevOps、Security/Privacy 分工的整改建议。 | PASS | 报告系统列出 GDPR 控制缺口并提供分角色、分优先级的整改建议。 |

## With-Skill Behavior

with-skill 正确读取 handoff、PRD、源码和分析配置，创建了要求路径下的 privacy-map.md，并完整覆盖数据清单、共享/保留、用户权利及合规缺口与建议。

## Fresh Without-Skill Baseline

without-skill 也创建了内容充分的隐私报告，四项 assertion 均有明确证据通过；其报告文件名不同于 skill 契约要求，但不影响本轮 assertion 内容核验。

## Failures

- 无。

## Not Exercised

- 无。

## Next Steps

- 无。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` workspace 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
