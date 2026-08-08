# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-002-user-rights`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8` from `agents/security/test/privacy-surface-mapper/evals/workspace/eval-002-user-rights`.
- Fixture SHA-256: `2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8`
- Prompt SHA-256: `f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `25bd4dbed66f3625883b2a2072dcd568eef569278521e1eac012e86f61347836`
- Skill overlay SHA-256: `840e4d3e20057f4834a3b010b4142d0e7be2f66540c525231dc34075db0dbbee`
- Judge schema SHA-256: `46c6f10cb2ee094e0f2d9b8cf0d9d794ebc801a301eb97187a76e961b4e37fd0`
- Eval definition SHA-256: `ba5034d1b895bcb95cc9d848045b869189eec2c98d23c0a5d5ce381059a73047`
- Metadata SHA-256: `b655e3698222cf189fb740616c1df41fb5ccc3d4bf71526ca29a7ecf05ef368a`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `data_inventory` | PASS | 交付的 privacy-map.md 列出账号资料、订单/交易元数据、产品行为事件及账号生命周期数据，并说明 /me、/data-export、DELETE /me 的入口、处理目的和当前处理情况。 |
| `sharing_and_retention` | PASS | 报告识别了分析副本、备份、缓存、日志及第三方处理者/跨境传输的不确定性，并指出缺少保留期限、法律依据、加密和删除传播证据。 |
| `user_rights` | PASS | 报告分别评估了访问、导出、删除和更正权；准确指出导出越权且不完整、删除仅软删除且不可追踪，并提出身份绑定、异步交付、删除编排和状态查询等整改建议。 |
| `compliance_gaps` | PASS | 报告给出明确的隐私与安全合规缺口、影响、上线阻断项及分工明确的整改建议，覆盖授权、完整性、删除传播、保留例外、安全交付、审计和限流。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0; fixture_sha256=2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8; output_sha256=cedd912f4b2e22b67f408be14767275c658a7257752f5f67d67c38961428f209; snapshot_sha256=5d014ee8694828c0ceef86ee40d2a17442cf3da876485a7437866e60ef574d8c
- Behavior: 交付了符合要求的 Security-owned 隐私处理面报告，覆盖数据范围、访问、删除、导出、共享/保留风险、影响和整改建议；未修改业务实现。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0; fixture_sha256=2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8; output_sha256=ff512bbd9085747910ebee2c646efaa94cb0a47f4c5fc4826d9ec850b0592085; snapshot_sha256=6dbbbbf946997fcd245284a53a849200f069de9409c98d6b5c499adab2a05eb9
- Behavior: 同样交付了结构化安全审查报告，覆盖主要越权、删除、导出和响应安全缺口；作为对比基线，其报告较少展开数据清单和用户权利映射。
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
- Eval: `eval-002-user-rights`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8` from `agents/security/test/privacy-surface-mapper/evals/workspace/eval-002-user-rights`.
- Fixture SHA-256: `2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8`
- Prompt SHA-256: `f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `25bd4dbed66f3625883b2a2072dcd568eef569278521e1eac012e86f61347836`
- Skill overlay SHA-256: `840e4d3e20057f4834a3b010b4142d0e7be2f66540c525231dc34075db0dbbee`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ba5034d1b895bcb95cc9d848045b869189eec2c98d23c0a5d5ce381059a73047`
- Metadata SHA-256: `b655e3698222cf189fb740616c1df41fb5ccc3d4bf71526ca29a7ecf05ef368a`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `data_inventory` | PASS | with_skill 的 privacy-map.md 明确列出用户记录、订单、产品行为事件及软删除记录，并说明各自的收集/使用入口与目的。 |
| `sharing_and_retention` | PASS | with_skill 的报告专门分析了保留期限、法律留置、备份、缓存、分析供应商、处理商和第三方传播，并将缺少证据的内容标为 unverified，提出核实与删除传播建议。 |
| `user_rights` | PASS | with_skill 检查了 /me 访问、/data-export 导出、/me 删除及更正权利，指出越权导出、导出缺少行为事件、删除仅软删除等问题。 |
| `compliance_gaps` | PASS | with_skill 给出了阻断上线的隐私与安全缺口、影响、整改建议、验收要求及后续责任分派。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0; fixture_sha256=2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8; output_sha256=0c542250540c603dd538c2edc9dad16a012cb456ca013d01b2b2a5b868c9a201; snapshot_sha256=9f595722679104ad7e31e4481ef63a5e4558dbaa136574210e3fed57dea34814
- Behavior: 交付了结构化隐私处理面报告，系统覆盖数据清单、数据流、用户权利、第三方共享、保留风险、合规缺口及整改建议。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0; fixture_sha256=2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8; output_sha256=d66ac5b886a72eb3acc3f7ba2662c8ed86f40ddd2a6f77b86d0a77265cdd2508; snapshot_sha256=252ae250bb4f50555b7e5b981742e6c284c29e4e15ab9c9e5b7062132a4f5923
- Behavior: 提供了较完整的安全审查，识别 IDOR、软删除不完整、认证和导出安全控制缺口，并交付结构化报告。
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
- Eval: `eval-002-user-rights`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8` from `agents/security/test/privacy-surface-mapper/evals/workspace/eval-002-user-rights`.
- Fixture SHA-256: `2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8`
- Prompt SHA-256: `f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `25bd4dbed66f3625883b2a2072dcd568eef569278521e1eac012e86f61347836`
- Skill overlay SHA-256: `4e2d7a3ffa0fc7b4cc84f02f24df4e35de821cbc6e0c580a1427e37709efb43b`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ba5034d1b895bcb95cc9d848045b869189eec2c98d23c0a5d5ce381059a73047`
- Metadata SHA-256: `b655e3698222cf189fb740616c1df41fb5ccc3d4bf71526ca29a7ecf05ef368a`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `data_inventory` | PASS | with_skill 报告识别了用户资料、订单/交易元数据、行为事件和会话身份，列出了 /me、/data-export、/me 删除入口及其用途，并指出字段范围未验证、原始用户记录可能过度暴露。 |
| `sharing_and_retention` | PASS | with_skill 报告覆盖分析副本、第三方处理方/子处理方、跨境传输、备份、保留期限及法定保留例外，并明确这些控制在现有材料中无法验证及其风险。 |
| `user_rights` | PASS | with_skill 报告逐项评估访问、导出、删除和更正能力，准确指出导出 IDOR、行为数据缺失、删除仅更新主库且无状态追踪，并提出认证、完整导出和端到端删除建议。 |
| `compliance_gaps` | PASS | with_skill 报告给出了发布阻断结论、风险影响和分优先级整改建议，包括身份绑定、完整数据目录、异步安全导出、可重试删除工作流、保留策略、审计和权利测试。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0; fixture_sha256=2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8; output_sha256=9a6355c2997d344b67552f8007b3f21454c09d2bc8e3f3fb64f9c6abd3e4ce70; snapshot_sha256=328b4a83186a6241b3c0a21159a20250de3438bf381f862b69c870121e0afc05
- Behavior: 生成了结构化隐私处理面报告，系统覆盖数据清单、数据流、第三方共享、保留、用户权利、风险影响和发布门槛；未修改实现代码。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0; fixture_sha256=2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8; output_sha256=4dd41f9b4184840dbecd2a6c30bebbf79054da15c1022aafbc5884017b380b99; snapshot_sha256=f1c544f85bb654fb3fab4765891603d1c66b63e40dcc99882bdf7db17be93c6e
- Behavior: 识别了主要越权导出、删除传播、导出完整性、安全交付、认证和保留期限问题，并提供整改建议。
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
- Eval: `eval-002-user-rights`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8` from `agents/security/test/privacy-surface-mapper/evals/workspace/eval-002-user-rights`.
- Fixture SHA-256: `2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8`
- Prompt SHA-256: `f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `25bd4dbed66f3625883b2a2072dcd568eef569278521e1eac012e86f61347836`
- Skill overlay SHA-256: `4e2d7a3ffa0fc7b4cc84f02f24df4e35de821cbc6e0c580a1427e37709efb43b`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ba5034d1b895bcb95cc9d848045b869189eec2c98d23c0a5d5ce381059a73047`
- Metadata SHA-256: `b655e3698222cf189fb740616c1df41fb5ccc3d4bf71526ca29a7ecf05ef368a`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `data_inventory` | PASS | with_skill 报告识别了账号资料、订单与交易元数据、产品行为事件及会话身份标识，并列出代码位置、收集/处理目的及未证实项。 |
| `sharing_and_retention` | PASS | with_skill 报告识别了分析系统、第三方副本、缓存、备份等数据面风险，并指出缺少第三方删除传播、留存期限、法定保留例外及供应商 SLA 证据。 |
| `user_rights` | PASS | with_skill 报告逐项检查了访问、导出、删除、更正、限制处理、反对和撤回同意，并准确说明已实现范围及缺口。 |
| `compliance_gaps` | PASS | with_skill 报告给出了隐私与安全合规缺口、影响、责任归属和具体整改建议，包括身份绑定、字段最小化、删除编排、留存政策、审计和安全交付。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0; fixture_sha256=2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8; output_sha256=f43a7e86b6983b2f6c7ded57a8bde37aeb8257d4200268f9de70c475e86fc164; snapshot_sha256=883a618eb15cee295b71cb73ff040e1cac7cf9f5afcda3669a9536d12fd4605d
- Behavior: 生成结构化隐私处理面报告，覆盖数据清单、数据流、用户权利、共享与留存风险、合规缺口及整改建议。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0; fixture_sha256=2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8; output_sha256=83124b2e3e440e5933ae3f0d6397f4b5df0b0e428d2a0248b341bbdf6e3ecf14; snapshot_sha256=052dc6fe76764c2092c88b0aa7f0049cc21551be0f8bbe873d0b2830254e738a
- Behavior: 识别了主要越权、删除传播、导出完整性和安全控制缺口，并生成了报告。
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
- Eval: `eval-002-user-rights`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8` from `agents/security/test/privacy-surface-mapper/evals/workspace/eval-002-user-rights`.
- Fixture SHA-256: `2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8`
- Prompt SHA-256: `f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ce73f0c2e691c2e71d4792a4ff83efe02c3a6714b22fe5c3733a875118131db8`
- Skill overlay SHA-256: `cd8ee54ef003ea53bd486a0be35c70dcd1362f3fd307cff51efdedb756e33a7d`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ba5034d1b895bcb95cc9d848045b869189eec2c98d23c0a5d5ce381059a73047`
- Metadata SHA-256: `b655e3698222cf189fb740616c1df41fb5ccc3d4bf71526ca29a7ecf05ef368a`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `data_inventory` | PASS | with_skill 明确列出账号资料、订单与交易元数据、产品行为事件，关联 /me、/data-export、DELETE /me 及数据库/分析接口，并说明访问、导出、删除等处理目的。 |
| `sharing_and_retention` | PASS | with_skill 识别了分析供应商、第三方副本、缓存、队列、备份等传播/存储风险，并指出缺少供应商删除确认、保留期限、法定保留范围及匿名化策略。 |
| `user_rights` | PASS | with_skill 检查了访问、导出、删除和可携带性，准确指出会话身份越权、行为数据遗漏、删除传播与状态追踪缺失，并补充更正权未见实现及 CSRF/重新认证等控制缺口。 |
| `compliance_gaps` | PASS | with_skill 给出了上线阻断结论、风险影响和具体整改建议，覆盖授权、数据完整性、删除工作流、第三方副本、安全交付、审计、限流、保留策略及测试验收。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0; fixture_sha256=2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8; output_sha256=5f86367a2c5420d810864ec0d322b743403ff6ce1da76b975d510c9440cb9cc1; snapshot_sha256=ed0757bbb53096a0fbe4f6120bcf4474ae05e942e881257beaefb0de02b8b265
- Behavior: 在覆盖主要安全缺口的基础上，结构化梳理数据范围、处理目的、数据流、权利状态、第三方/保留风险和整改验收建议，证据边界表述清晰。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0; fixture_sha256=2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8; output_sha256=20dbe7d7ce9e6724199f648285fefb282400f439ff5837bf38732b67e950faa4; snapshot_sha256=a5335ed81c2ca785c448ab18aa0a8b506a3c08964a2e82308d76b75e72901ba2
- Behavior: 识别了越权导出、删除不完整、导出不安全、认证契约、CSRF、字段白名单等主要问题，并提供了较完整的报告。
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
- Eval: `eval-002-user-rights`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8` from `agents/security/test/privacy-surface-mapper/evals/workspace/eval-002-user-rights`.
- Fixture SHA-256: `2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8`
- Prompt SHA-256: `f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `32486beb9db21ed173f2083e3323014ff05de4963e7a8b1d84d40eb43ab3aa33`
- Skill overlay SHA-256: `874b129b045f44af288c1af739a4a66f07931a151f79399740585f1fce30c452`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ba5034d1b895bcb95cc9d848045b869189eec2c98d23c0a5d5ce381059a73047`
- Metadata SHA-256: `b655e3698222cf189fb740616c1df41fb5ccc3d4bf71526ca29a7ecf05ef368a`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `data_inventory` | PASS | With_skill identifies user profiles, orders/transaction metadata, analytics events, and additional data in sessions, tokens, logs, backups, and caches; it maps collection/read paths and purposes. |
| `sharing_and_retention` | PASS | With_skill identifies analytics systems, third-party processors, caches, backups, logs, and retention/legal-hold gaps, with deletion propagation and expiry recommendations. |
| `user_rights` | PASS | With_skill evaluates access, export, deletion, and rectification support, including session binding, incomplete export scope, deletion propagation, status tracking, CSRF, and token revocation. |
| `compliance_gaps` | PASS | With_skill provides concrete privacy/security gaps, impacts, remediation steps, and a pre-launch acceptance checklist. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0; fixture_sha256=2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8; output_sha256=0eeed96e8c196777ee6814b71de4f864d24b1f4e17b8ffac6ff10031fe523917; snapshot_sha256=40d35781ced0f5bf2a9a6b98bbca9126bbd26953c255647e4fe3626a9dd4a7b2
- Behavior: Structured privacy-surface review maps data categories and flows, evaluates user rights and sharing/retention risks, and provides evidence-backed compliance gaps and remediation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0; fixture_sha256=2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8; output_sha256=ba6800663a1eb268339c3c50cdd805529789f7637b59076506cf902f7185177f; snapshot_sha256=61a3e4e2d227e03e03035ba48e06c64d076e39b4287e74c84eaab23884d5baf0
- Behavior: Fresh baseline identifies major authorization, export completeness, deletion propagation, delivery, error handling, audit, retention, and rate-limit gaps, but gives less explicit data inventory and privacy-surface mapping.
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

# Eval Result: eval-002-user-rights

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-002-user-rights`
- Test case: User Rights Implementation
- Workspace: `workspace/eval-002-user-rights`
- Natural user prompt:

> pm-agent has completed entry classification and routed this confirmed `user-rights` security scope to privacy-surface-mapper. Use the PM handoff packet in workspace `PM_HANDOFF.md` and the confirmed source document `docs/pm/user-rights/PRD.md`. Check if user rights (access, deletion, export) are implemented.

- Expected artifact: Structured privacy surface map that identifies personal data, processing purpose, third-party sharing, user-rights gaps, and compliance risks.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/privacy-surface-mapper--eval-002-user-rights/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `51099ecfc1cc6407a2a8395e70e437687a8d984b7702e62660481c6549a657be`。
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
| `data_inventory`<br>识别个人数据类型、收集入口和处理目的 | PASS | 报告明确识别用户资料、订单/交易元数据、分析行为事件及备份副本，并列出收集/处理入口和目的；最终快照存在 privacy-map.md。 | PASS | PRIVACY_SURFACE_REPORT.md 明确列出用户资料、订单、行为事件及相关数据范围，并说明处理上下文。 |
| `sharing_and_retention`<br>识别第三方共享、存储或保留相关风险 | PASS | 报告识别 analytics 为下游接收方、备份为内部副本，并明确缺少传输/供应商信息、保留期限、删除传播和法定保留策略。 | PASS | 报告识别 analytics、后台任务和备份中的数据副本，并明确删除传播、保留期限和法定保留处理缺口。 |
| `user_rights`<br>检查访问、删除、导出或同意等用户权利支持情况 | PASS | 报告逐项核验 access、export、deletion，并以 src/api/user-rights.js 行号说明 session 身份、userId 越权、数据不完整、软删除及无传播/追踪。 | PASS | 报告逐项评估 /me、/data-export 和 DELETE /me，准确指出访问部分实现、导出越权且不完整、删除仅软删除。 |
| `compliance_gaps`<br>给出隐私合规缺口和改进建议 | PASS | 报告包含 CRITICAL/HIGH/MEDIUM 风险、GDPR/CCPA 影响及 Engineer/DevOps/Product Legal 分工的具体整改建议。 | PASS | 报告包含风险评级、PRD 验收缺口及工程、DevOps 的具体修复建议。 |

## With-Skill Behavior

已按 PM handoff 和 PRD 核验代码，并在最终快照创建了符合契约的 docs/security/user-rights/privacy-map.md。报告覆盖数据范围、入口、目的、共享/保留风险、用户权利状态及整改建议。

## Fresh Without-Skill Baseline

Baseline 也创建了结构化隐私报告并覆盖四项断言，作为对照不影响 with-skill 判定。

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
