# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-001-sql-injection`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6` from `agents/security/test/appsec-checklist/evals/workspace/eval-001-sql-injection`.
- Fixture SHA-256: `ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6`
- Prompt SHA-256: `bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `812b371fc30792cb2b0cf8d96079b3244c95b93efab7638e085d4e955d6ea42c`
- Skill overlay SHA-256: `33e7e73c99fb4e7a6f2d6ab5104b8298fc067235a29614a6e32ee61035051666`
- Judge schema SHA-256: `01ca86a4951823e3b6c703072ce5be09764c747ae9938b66975b80e4d41e39dd`
- Eval definition SHA-256: `8fc30622b3de679ebf38da0b0fc7b8032d774fb8a425496383ba9ed0da1fdbb0`
- Metadata SHA-256: `c7304df99ba027e455b94ef86d8c2964c99813b4b7afb5bd532e0bf494b29d15`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `security_findings` | PASS | The with_skill report identifies SQL injection via direct interpolation of req.query.name into SQL at src/api/user-search.js:2-4. |
| `evidence_and_impact` | PASS | The report traces the HTTP parameter-to-database path and explains unauthorized directory reads plus conditional data modification, destruction, and availability impact. |
| `severity_rationale` | PASS | It assigns Critical severity and supports it with authenticated reachability, predicate manipulation, PRD violations, affected assets, and conditional driver/database impacts. |
| `remediation` | PASS | It recommends parameterized queries, validation, wildcard handling, least privilege, disabled multi-statements, and concrete regression tests. |
| `writes_protocol_shaped_security_report` | PASS | The locked delivery_snapshot contains docs/security/user-search/appsec-checklist.md with frontmatter including feature, feature_path, version, and date; an Executive Summary with finding count, severity distribution, and posture; and location, risk, remediation, and verification sections. Git evidence shows no other files changed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28; fixture_sha256=ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6; output_sha256=40f3a74ff0a24f1c3a1d683915259cd59c8fd2c6ab11f0800fe90dbd13e93135; snapshot_sha256=ad8b8df94941228c8b06201eaff840e6999e9fc43b36e88e87e3af37b903911c
- Behavior: Produced a protocol-shaped security report identifying the SQL injection with code evidence, impact, severity, remediation, and verification steps; no forbidden source or PM document mutations are evidenced.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28; fixture_sha256=ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6; output_sha256=fb6e859f5c9c3ba44d8dfee7f7d50b9f54c22fab3d07409cfe428ce58154a15b; snapshot_sha256=0e6e4c5a3dbc08dcc9a5b956562aeec158e242d1efb7a297a8fc16c20d0659fa
- Behavior: Identified the main SQL injection and additional wildcard/resource risks and delivered a report, but the locked report lacks the required frontmatter and Executive Summary protocol structure.
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
- Skill: `appsec-checklist`
- Eval: `eval-001-sql-injection`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6` from `agents/security/test/appsec-checklist/evals/workspace/eval-001-sql-injection`.
- Fixture SHA-256: `ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6`
- Prompt SHA-256: `bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `812b371fc30792cb2b0cf8d96079b3244c95b93efab7638e085d4e955d6ea42c`
- Skill overlay SHA-256: `33e7e73c99fb4e7a6f2d6ab5104b8298fc067235a29614a6e32ee61035051666`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8fc30622b3de679ebf38da0b0fc7b8032d774fb8a425496383ba9ed0da1fdbb0`
- Metadata SHA-256: `c7304df99ba027e455b94ef86d8c2964c99813b4b7afb5bd532e0bf494b29d15`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `security_findings` | PASS | with_skill 识别了直接 SQL 拼接导致的 SQL 注入，并说明了可能的越权读取及多语句配置相关风险。 |
| `evidence_and_impact` | PASS | 报告直接引用 src/api/user-search.js:2-4，说明受影响入口、用户目录数据读取影响、异常与潜在数据修改影响。 |
| `severity_rationale` | PASS | 报告将 SQL 注入评为 Critical，并基于未可信 HTTP 参数直接影响数据库语法及发布阻断要求给出依据。 |
| `remediation` | PASS | 报告提供了参数化查询、输入类型/长度/频率限制、LIKE 通配符处理及恶意输入回归验证等可执行建议。 |
| `writes_protocol_shaped_security_report` | PASS | delivery_snapshot 中的报告包含 feature、feature_path、version、date 等 frontmatter，含 Executive Summary、问题总数与风险分布、逐问题位置/风险/修复建议；git_evidence 显示仅新增安全报告，未修改应用或 PM 文档。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28; fixture_sha256=ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6; output_sha256=9effc5ea91a24385f29aefdaa34b2fc3a695ff9d82281f5ee9f77b101acba3a8; snapshot_sha256=498fc1456ecd7752f92ec6581b78b0e2415a71aefcae098d96e7fb199de86349
- Behavior: 识别 SQL 注入，提供代码证据、影响、Critical 分级依据和修复建议，并按协议落盘安全报告。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28; fixture_sha256=ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6; output_sha256=49f0b70f8a4b68c627764c679ac781f7019310d29cbcaa3cbada0f5fc9e14b02; snapshot_sha256=4d4f6e2fee67557b08e94edcd4300acb9f96fa4df1033e5ffa4c8d0be46c7185
- Behavior: 完成了安全发现和报告落盘，但交付报告缺少要求的协议 frontmatter 与 Executive Summary 分区。
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
- Skill: `appsec-checklist`
- Eval: `eval-001-sql-injection`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6` from `agents/security/test/appsec-checklist/evals/workspace/eval-001-sql-injection`.
- Fixture SHA-256: `ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6`
- Prompt SHA-256: `bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `812b371fc30792cb2b0cf8d96079b3244c95b93efab7638e085d4e955d6ea42c`
- Skill overlay SHA-256: `5b2b2b7a3b96eded32c11959c382e7fa8aafb204f59c1c353154bae2cdaf9c71`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8fc30622b3de679ebf38da0b0fc7b8032d774fb8a425496383ba9ed0da1fdbb0`
- Metadata SHA-256: `c7304df99ba027e455b94ef86d8c2964c99813b4b7afb5bd532e0bf494b29d15`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `security_findings` | PASS | 识别了 SQL 注入风险，并说明 LIKE 通配符、输入边界与结果限制问题。 |
| `evidence_and_impact` | PASS | 提供了 src/api/user-search.js:2-4 的输入到数据库证据链，并说明了目录数据泄露、查询语义改变和完整性/负载影响。 |
| `severity_rationale` | PASS | 将 SQL 注入评为 Critical，并结合越权读取、数据泄露及潜在多语句影响给出依据。 |
| `remediation` | PASS | 建议参数化查询、输入类型与长度校验、结果限制、LIKE 转义、认证复核和恶意输入回归测试，均具备可执行性。 |
| `writes_protocol_shaped_security_report` | PASS | 报告已写入 docs/security/user-search/appsec-checklist.md，包含 frontmatter、Executive Summary、风险等级分布、位置、风险解释和修复建议；git evidence 显示未修改其他文件。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28; fixture_sha256=ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6; output_sha256=499ec8bc94b1f900714611d7d7a673ed27260d793b43c44cfc6443a81b3f2d7c; snapshot_sha256=4bd24b69efea4e6e3bbf70bfa5477ce5abbfc645f5883d77884cac7f5f50cb24
- Behavior: 识别并分级 SQL 注入风险，提供代码证据、影响和修复建议，并按协议落盘完整安全报告。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28; fixture_sha256=ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6; output_sha256=325687b3bac7ec3fcec3071c8f62a041883a1449b52112d1bdca1c482805b326; snapshot_sha256=cdc0f4f51a9766171bc071c355408106521270f0a4f133d384f61730721061bf
- Behavior: 完成了较详细的安全审查并写入报告，但报告缺少协议要求的 frontmatter 和 Executive Summary 分区。
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
- Skill: `appsec-checklist`
- Eval: `eval-001-sql-injection`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6` from `agents/security/test/appsec-checklist/evals/workspace/eval-001-sql-injection`.
- Fixture SHA-256: `ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6`
- Prompt SHA-256: `bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `812b371fc30792cb2b0cf8d96079b3244c95b93efab7638e085d4e955d6ea42c`
- Skill overlay SHA-256: `5b2b2b7a3b96eded32c11959c382e7fa8aafb204f59c1c353154bae2cdaf9c71`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8fc30622b3de679ebf38da0b0fc7b8032d774fb8a425496383ba9ed0da1fdbb0`
- Metadata SHA-256: `c7304df99ba027e455b94ef86d8c2964c99813b4b7afb5bd532e0bf494b29d15`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `security_findings` | PASS | with_skill 报告识别了 req.query.name 直接拼接 SQL 导致的可利用 SQL 注入，并补充了通配符/异常输入风险。 |
| `evidence_and_impact` | PASS | 报告提供了 src/api/user-search.js:2-4 的代码位置和输入路径证据，并说明了未授权目录读取、数据库完整性/可用性及资源消耗影响。 |
| `severity_rationale` | PASS | 报告将 SQL 注入评为 Critical，并基于认证入口、用户可控 SQL 语法和数据库权限/驱动配置说明了判断依据。 |
| `remediation` | PASS | 报告提供了参数化查询、类型/长度校验、最小权限、LIKE 转义以及具体恶意输入回归验证步骤。 |
| `writes_protocol_shaped_security_report` | PASS | raw evidence 证明创建了 docs/security/user-search/appsec-checklist.md；文件含 feature、feature_path、version、date 等 frontmatter，含 Executive Summary、问题数量/等级分布/总体态势及逐问题位置、风险、影响、严重度依据和修复建议；PM、PRD、实现文件哈希未改变。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28; fixture_sha256=ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6; output_sha256=4387b997d3c94e29c9807d69441935afb3444948f73c584da64b85a018d0ccea; snapshot_sha256=e341edabdd92060c89ee27f2a723c0dcc2614c8e58998e965e210c4207bf9ea2
- Behavior: 创建了符合协议结构的安全报告，识别并论证 SQL 注入风险，提供影响、严重度依据、修复建议和验证步骤，且未修改应用代码或其他角色文档。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28; fixture_sha256=ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6; output_sha256=2ca91e9518c0423689b24d53f5be9787ca74634308bc06c0dd766020d8e036d6; snapshot_sha256=0e1be1ddca652aa41c2d5daae37458d05de5343d7f9c1bb56469f251d3064102
- Behavior: 创建了报告并识别主要 SQL 注入风险，同时覆盖了通配符和异常参数风险；其报告协议结构未按要求提供 frontmatter 与 Executive Summary。
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
- Skill: `appsec-checklist`
- Eval: `eval-001-sql-injection`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6` from `agents/security/test/appsec-checklist/evals/workspace/eval-001-sql-injection`.
- Fixture SHA-256: `ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6`
- Prompt SHA-256: `bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8638f695ab2249699760b63a17b3618bf2d964d5ae466881f575505e2674bdaf`
- Skill overlay SHA-256: `7a46c5f912eabaa23dbb3c81db666071019107df43f45f25b7e8f552cbe709f8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8fc30622b3de679ebf38da0b0fc7b8032d774fb8a425496383ba9ed0da1fdbb0`
- Metadata SHA-256: `c7304df99ba027e455b94ef86d8c2964c99813b4b7afb5bd532e0bf494b29d15`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `security_findings` | PASS | with_skill 报告识别了与代码和场景匹配的 SQL 注入、LIKE 通配符扩大结果集及资源耗尽风险。 |
| `evidence_and_impact` | PASS | 逐项引用了 src/api/user-search.js:2-6，并说明已认证入口、目录枚举、未授权读取和可用性影响。 |
| `severity_rationale` | PASS | F-001 标为高危并结合低攻击门槛和数据影响说明依据；F-002/F-003 标为中危并说明影响取决于资源、限流和目录规模。 |
| `remediation` | PASS | 提供了参数化查询、LIKE 转义、输入和结果限制、超时、限流、错误处理及回归验证步骤。 |
| `writes_protocol_shaped_security_report` | FAIL | 报告已落盘且未修改应用代码，但缺少要求的 frontmatter 和明确的 Executive Summary 分区；报告使用“结论”分区替代。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28; fixture_sha256=ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6; output_sha256=5cda06714ed8ae72f2aebb3fca6b7a1c0b28e612b9afa0409145afab89d94713; snapshot_sha256=988c4587f7b601bead006f4d4853e23fdc0a5ddc6c760ce724f936dd59c9fe71
- Behavior: 完成安全风险审查并写入报告，前三项内容要求满足；报告协议结构缺少 frontmatter 和 Executive Summary。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28; fixture_sha256=ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6; output_sha256=318e2e0cac2ec7b3125397afd9554943a5dae9d8004b97e25165e6d159050d9c; snapshot_sha256=5e792cf54ccf695ad63ca17d7972f9f4a2d1e020c914cb71100a14f58dba7597
- Behavior: 识别了主要风险并声称写入报告，内容较完整，但未作为 with_skill 断言判定依据。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 报告未按协议包含 frontmatter。
- with_skill 报告未包含 Executive Summary 分区。
- Next: 补充包含 feature、feature_path、version、date 等字段的 frontmatter。
- Next: 将结论内容重组为 Executive Summary，并包含问题总数、风险等级分布和总体态势。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-001-sql-injection`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6` from `agents/security/test/appsec-checklist/evals/workspace/eval-001-sql-injection`.
- Fixture SHA-256: `ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6`
- Prompt SHA-256: `bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `095129ad5c17fd8974fdea44f1054ac02e7fa8f954b0e4a1a1d1a0ef185f9ce5`
- Skill overlay SHA-256: `5839d5cfe31d4e5dc5e9520f24a99b1147c97570ef1cc156eb90972408a49170`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8fc30622b3de679ebf38da0b0fc7b8032d774fb8a425496383ba9ed0da1fdbb0`
- Metadata SHA-256: `c7304df99ba027e455b94ef86d8c2964c99813b4b7afb5bd532e0bf494b29d15`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `security_findings` | PASS | with_skill 报告识别了 SQL 注入和 LIKE 通配符/资源消耗风险，均与用户搜索查询参数进入 SQL 的场景匹配。 |
| `evidence_and_impact` | PASS | 报告引用 src/api/user-search.js:2-4，说明了输入路径、受影响入口，以及越权读取、数据暴露、资源消耗和可用性影响。 |
| `severity_rationale` | PASS | 报告明确将 SQL 注入评为高危、通配符与查询无边界评为中危，并解释了认证前提、利用成本、影响范围及数据库权限因素。 |
| `remediation` | PASS | 报告提供了参数化查询示例、通配符转义、输入限制、超时、结果上限、限流、最小权限和具体回归验证步骤。 |
| `writes_protocol_shaped_security_report` | FAIL | 报告路径正确且未修改其他角色文档，但内容缺少要求的 frontmatter（feature、feature_path、version、date 等字段）和 Executive Summary 分区，因此不符合 SKILL.md 协议结构。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28; fixture_sha256=ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6; output_sha256=e30db3cc1236bc6f68859ae56502099f75d44935b70ec2a3b0d9fd1d5caf2485; snapshot_sha256=84d9470e5de4416a58eee36e3dadfe85ee165a5c3c4cada0f9236f7d2f7d30b6
- Behavior: 完成了场景匹配的安全审查，覆盖 SQL 注入、通配符滥用、影响、严重度、修复和验证，但落盘报告未按要求包含 frontmatter 和 Executive Summary。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28; fixture_sha256=ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6; output_sha256=cff5df66b6e017173a70153f469db3b437365eb91dda07ff1d6cbb74619ebb4e; snapshot_sha256=55e1cd315ba10136a0b07c350c80b6d2ed2d967b34c3a09d82dc6668574893a1
- Behavior: 完成了较完整的安全审查并写入报告，内容覆盖风险、证据、影响、严重度、修复和验证；同样未展示协议要求的 frontmatter 与 Executive Summary。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 的落盘报告缺少协议要求的 frontmatter 和 Executive Summary 分区。
- Next: 在 docs/security/user-search/appsec-checklist.md 顶部补充 feature、feature_path、version、date 等 frontmatter，并新增包含问题总数、风险等级分布和总体态势的 Executive Summary 分区。

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

# Eval Result: eval-001-sql-injection

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-001-sql-injection`
- Test case: SQL Injection Vulnerability
- Workspace: `workspace/eval-001-sql-injection`
- Natural user prompt:

> pm-agent 已完成入口分类并路由至 appsec-checklist；PM handoff packet 见 workspace `PM_HANDOFF.md`，已确认 feature_path 为 `user-search`。Review the security of this user search API endpoint.

- Expected artifact: Structured application security checklist with prioritized findings, affected surfaces, evidence, impact, and remediation guidance.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/appsec-checklist--eval-001-sql-injection/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `5a1ccb91721f3d503cb9163a80457c474d68b0ce57a95930c83942362f24cb1a`。
- Lane isolation: 先完成并销毁全部 `without_skill` 独立顶层临时目录，再创建任何 `with_skill` 目录；每条 lane 使用独立的顶层临时 workspace、`HOME` 与 `CODEX_HOME`，不存在可供另一条 candidate 读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt 与相同初始 fixture；仅 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 skill，`without_skill` 未安装任何目标 skill。
- Evidence isolation: 所有 candidate 会话结束并删除各自临时根后，才将内存中的最终 workspace 快照与 transcript 持久化到 runtime root；candidate transcript 泄漏扫描未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、judge/verdict 或 expected output/assertion 脚手架。
- Judge: candidate 全部结束后，由第三个独立、只读的 fresh Codex 会话依据当前 assertions、两条 candidate 输出、transcript 与最终 workspace 快照判定。

## Latest Result

- Behavior result: **PASS**（PASS 5 / FAIL 0 / NOT EXERCISED 0）
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Historical Contract Note

上一份 durable comparison 保留的是增强前 4 条断言结果，并因新增第 5 条报告落盘断言而标记为 `BLOCKED`。本轮使用当前 5 条断言重新生成`with_skill` 与 `without_skill`，未复用旧 baseline 或旧结论。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `security_findings`<br>识别与场景匹配的应用安全风险，例如注入、认证绕过或 XSS | PASS | 报告明确识别了 src/api/user-search.js:2-4 的 SQL 注入，以及输入/结果无界导致的资源耗尽风险，且与 user-search 场景匹配。 | PASS | Baseline 报告同样明确识别 SQL 注入、认证/授权验证风险、资源耗尽和用户枚举风险。 |
| `evidence_and_impact`<br>说明证据、受影响入口和业务或安全影响 | PASS | 逐项提供 file:line 证据，并说明越权读取、数据泄露、潜在数据破坏、数据库/API 资源耗尽等影响。 | PASS | 逐项提供 file:line 证据，并说明数据读取、数据库完整性/可用性、枚举和拒绝服务影响。 |
| `severity_rationale`<br>给出严重度并说明判断依据 | PASS | 报告将 SQL 注入定为 Critical、资源限制问题定为 Medium，并结合可利用性、数据机密性、完整性和可用性说明依据。 | PASS | Baseline 对 SQL 注入定为 Critical、认证风险定为条件性 High、资源耗尽和枚举定为 Medium，并给出依据。 |
| `remediation`<br>提供具体、可执行的修复建议或验证步骤 | PASS | 报告建议参数化 SQL、输入校验、结果上限/分页、超时、限流、最小权限，并列出针对注入和异常输入的回归验证步骤。 | PASS | Baseline 提供参数化查询、认证授权、边界控制、限流/超时和具体测试验证步骤。 |
| `writes_protocol_shaped_security_report`<br>报告按 SKILL.md 协议结构落盘（frontmatter + Executive Summary 分区） | PASS | 最终快照存在 docs/security/user-search/appsec-checklist.md；报告含 feature、feature_path、version、date、last_updated frontmatter，Executive Summary 含问题总数、风险分布和总体态势，并有逐问题位置、风险和修复建议；其他角色文档未被修改。 | FAIL | 最终快照虽存在目标报告，但缺少 SKILL.md 要求的 YAML frontmatter 和 Executive Summary 分区，不能满足协议结构要求。 |

## With-Skill Behavior

With-skill 明确识别 SQL 注入和资源耗尽风险，提供了证据、影响、严重度依据及可执行修复/验证建议，并按协议生成了报告。

## Fresh Without-Skill Baseline

Without-skill 也识别主要风险并生成报告，但报告缺少契约要求的 frontmatter 和 Executive Summary 结构。

## Failures

- 无。

## Not Exercised

- 实际路由注册层的认证/授权是否缺失，fixture 未提供路由或中间件，因此仅能作为发布前验证项。
- XSS、命令注入、密码/会话、依赖漏洞和生产配置等分支未被当前最小 fixture 实际触发。

## Next Steps

- 补充路由、中间件、数据库连接配置和依赖清单后，复核认证授权、最小权限、多语句配置和依赖风险。
- 修复 SQL 参数化及输入/结果边界后执行恶意输入、授权和资源耗尽回归测试。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` workspace 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
