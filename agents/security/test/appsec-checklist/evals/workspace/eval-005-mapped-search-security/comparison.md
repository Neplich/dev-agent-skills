# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-005-mapped-search-security`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d` from `agents/security/test/appsec-checklist/evals/workspace/eval-005-mapped-search-security`.
- Fixture SHA-256: `fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d`
- Prompt SHA-256: `e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `812b371fc30792cb2b0cf8d96079b3244c95b93efab7638e085d4e955d6ea42c`
- Skill overlay SHA-256: `33e7e73c99fb4e7a6f2d6ab5104b8298fc067235a29614a6e32ee61035051666`
- Judge schema SHA-256: `fe1f59786edfa4e3b7ee12601522d693ef12a42cdfce9b4a390ad6d7b95d03d2`
- Eval definition SHA-256: `d863b13d3e997477097b1a2de108729923e21619e10b2847114ea312db1c1bc8`
- Metadata SHA-256: `44e3487a1b0a940b7bf23d73f980b7d71bd0be1a4d04a13c48606fd67383de8a`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 输出识别了 change-map、required_docs 及目标文档，但锁定证据没有证明实际读取顺序或是否遍历了无关文档。 |
| `verifies_against_code` | PASS | 明确指出代码将 query 直接插入 SQL，并识别其与文档所称 parameterized query 的不一致。 |
| `treats_unverified_as_low_trust` | PASS | 明确识别 last_verified_version 为 unverified，并将文档作为低信任导航，转而依据代码事实。 |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | 输出正确将下一步退回 pm-agent，但因缺少 handoff packet、feature_path 和 PM 分类，锁定证据不足以要求后续 issue 创建及 Security 过程报告。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de; fixture_sha256=fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d; output_sha256=27fd85a20be77b40f332ff5dd8f6699fc858a0a84c6694a542f409bb7e8bf99b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了文档映射、unverified 状态及代码与文档的安全事实冲突，并在缺少合法交接信息时退回 pm-agent；未继续执行无法授权或定位的后续升级步骤。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de; fixture_sha256=fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d; output_sha256=6c80f1ab9f16d3bf2c919839d4e75cd4b293f2f028ce382a64dd7be1d1edc3a9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 独立识别 SQL 注入风险及文档/代码不一致，并提出修复建议，但没有按 PM/Security 交接流程升级。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 由 pm-agent 补充合法 handoff packet、feature_path 和分类后，验证 issue 创建及 Security 过程报告。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-005-mapped-search-security`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d` from `agents/security/test/appsec-checklist/evals/workspace/eval-005-mapped-search-security`.
- Fixture SHA-256: `fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d`
- Prompt SHA-256: `e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `812b371fc30792cb2b0cf8d96079b3244c95b93efab7638e085d4e955d6ea42c`
- Skill overlay SHA-256: `33e7e73c99fb4e7a6f2d6ab5104b8298fc067235a29614a6e32ee61035051666`
- Judge schema SHA-256: `fe1f59786edfa4e3b7ee12601522d693ef12a42cdfce9b4a390ad6d7b95d03d2`
- Eval definition SHA-256: `d863b13d3e997477097b1a2de108729923e21619e10b2847114ea312db1c1bc8`
- Metadata SHA-256: `44e3487a1b0a940b7bf23d73f980b7d71bd0be1a4d04a13c48606fd67383de8a`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 交付快照证明已识别并记录命中的 required_docs，但锁定证据无法证明实际读取顺序。 |
| `verifies_against_code` | PASS | 报告同时记录文档声称参数化查询与代码将 query 直接插入 LIKE SQL 字符串的不一致，并据代码事实判定 Critical SQL 注入风险。 |
| `treats_unverified_as_low_trust` | PASS | 报告明确指出 change-map 与 API 文档均为 last_verified_version: unverified，并将其作为低信任导航、扩大代码核证。 |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | 交付了 Security-owned 报告并明确要求交回 pm-agent 分类及创建 PM-owned issue；锁定证据未显示 PM-agent 运行或 issue 已创建，因此后续步骤未被实际行使。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de; fixture_sha256=fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d; output_sha256=8f8d2fa007af15583d7094ec6a90c9650f575a1d1f6e72fd1a5cf607918e9e75; snapshot_sha256=8ea56b3a53af2dec857f413dd2dc8ee611f8f3dcb0ddd4e9b61e69a00f4191e2
- Behavior: 准确识别文档与代码不一致及 Critical SQL 注入风险，生成了 Security 过程报告并给出 PM-agent 升级要求；未修改业务代码。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de; fixture_sha256=fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d; output_sha256=c26cf6f5f0254f1828af65660d63b48eba49262a88adc5c574455f7f45878db3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 独立输出了正确的 SQL 注入与文档不一致分析及修复建议，但没有交付 Security 过程报告或 PM-agent 升级证据。
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
- Eval: `eval-005-mapped-search-security`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d` from `agents/security/test/appsec-checklist/evals/workspace/eval-005-mapped-search-security`.
- Fixture SHA-256: `fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d`
- Prompt SHA-256: `e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `812b371fc30792cb2b0cf8d96079b3244c95b93efab7638e085d4e955d6ea42c`
- Skill overlay SHA-256: `33e7e73c99fb4e7a6f2d6ab5104b8298fc067235a29614a6e32ee61035051666`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `d863b13d3e997477097b1a2de108729923e21619e10b2847114ea312db1c1bc8`
- Metadata SHA-256: `44e3487a1b0a940b7bf23d73f980b7d71bd0be1a4d04a13c48606fd67383de8a`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 锁定证据没有交付快照或工具读取轨迹，无法证明读取顺序；with_skill 输出仅要求补充 handoff packet。 |
| `verifies_against_code` | FAIL | with_skill 未审查 src/api/search-handler.js，也未指出文档声称参数化查询而代码直接插值 query 的不一致。 |
| `treats_unverified_as_low_trust` | FAIL | fixture 中明确标注 last_verified_version: unverified，但 with_skill 未识别该状态，也未进行代码核证。 |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | with_skill 未形成改变正式文档事实的结论，亦无 issue 或 Security 过程报告交付；后续升级步骤尚未发生。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de; fixture_sha256=fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d; output_sha256=ddc2452680e55dbbd6fddeeffcdb1ec6aab691034e8c7a329ed961fcc5649403; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 以缺少预置 handoff packet 为由拒绝开始审查，未产出代码核对、unverified 信任评估或安全审查报告。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de; fixture_sha256=fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d; output_sha256=28fa95c967e7df140cdb63d799bc1fd3f03a813081d459c0c07260aae6276d7b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成了代码与文档的安全性对照，指出直接 SQL 插值、文档不一致及风险；未交付 PM 分类、issue 或 Security 报告。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未完成用户请求的代码与正式文档安全审查。
- with_skill 未识别代码直接插值与文档参数化查询声明之间的事实冲突。
- with_skill 未处理 required_docs 的 unverified 状态并扩大代码核证。
- Next: 读取 change-map 命中的 required_docs 和搜索处理器代码，完成安全结论，并按要求将改变正式文档事实的结论回交 pm-agent 分类、创建 issue，同时交付 Security-owned 过程报告。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-005-mapped-search-security`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d` from `agents/security/test/appsec-checklist/evals/workspace/eval-005-mapped-search-security`.
- Fixture SHA-256: `fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d`
- Prompt SHA-256: `e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `812b371fc30792cb2b0cf8d96079b3244c95b93efab7638e085d4e955d6ea42c`
- Skill overlay SHA-256: `5b2b2b7a3b96eded32c11959c382e7fa8aafb204f59c1c353154bae2cdaf9c71`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `d863b13d3e997477097b1a2de108729923e21619e10b2847114ea312db1c1bc8`
- Metadata SHA-256: `44e3487a1b0a940b7bf23d73f980b7d71bd0be1a4d04a13c48606fd67383de8a`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 输出确认了 change-map 命中和 required doc，但锁定证据无法证明实际读取顺序或未遍历无关文档。 |
| `verifies_against_code` | NOT_EXERCISED | 输出表示后续会核对代码；因缺少 handoff packet 和 feature_path，代码核对及风险结论尚未完成。 |
| `treats_unverified_as_low_trust` | PASS | 输出明确识别 last_verified_version: unverified，并说明该文档不能单独作为安全结论依据。 |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | 候选正确请求 pm-agent 提供 handoff packet，但正式事实变更结论、分类和 issue 创建尚未发生；后续步骤受缺失确认阻塞。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de; fixture_sha256=fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d; output_sha256=8d2de544757aae38eefe1521d38c635d38a06a95f21b30e562fd1f6993d0ca74; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 确认 change-map、required doc 及 unverified 状态，并正确暂停等待 pm-agent handoff；尚未完成代码核对、报告生成或升级。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de; fixture_sha256=fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d; output_sha256=16dd5ffb4500a6ae05cf264b53811d35a516ec166f7bd0d2963470382238099f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成代码与文档不一致的安全审查，指出直接 SQL 插值导致的注入风险，但未体现按 PM 流程升级 issue。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 获得 handoff packet 和 feature_path 后核对 search-handler.js 的查询构造并完成 AppSec 报告。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-005-mapped-search-security`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d` from `agents/security/test/appsec-checklist/evals/workspace/eval-005-mapped-search-security`.
- Fixture SHA-256: `fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d`
- Prompt SHA-256: `e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `812b371fc30792cb2b0cf8d96079b3244c95b93efab7638e085d4e955d6ea42c`
- Skill overlay SHA-256: `5b2b2b7a3b96eded32c11959c382e7fa8aafb204f59c1c353154bae2cdaf9c71`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `d863b13d3e997477097b1a2de108729923e21619e10b2847114ea312db1c1bc8`
- Metadata SHA-256: `44e3487a1b0a940b7bf23d73f980b7d71bd0be1a4d04a13c48606fd67383de8a`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `a6701d093076bc07d26c7e813151915b2b1a25f501428e58ba88c24bfe3d6c6e`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | Candidate identifies the change-map mapping and required API document, but locked raw evidence cannot prove the hidden read order. |
| `verifies_against_code` | PASS | With_skill output cites the handler code, identifies direct interpolation of query into SQL, contrasts it with the documented parameterized-query claim, and flags SQL-injection risk. |
| `treats_unverified_as_low_trust` | PASS | With_skill output notes both formal documents are marked last_verified_version: unverified and explicitly states they cannot override the code facts. |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | With_skill correctly pauses for missing PM/Security handoff data and directs the discrepancy back to pm-agent; issue creation cannot yet occur without the required confirmation/runtime handoff. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de; fixture_sha256=fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d; output_sha256=b3b4b5f57366bae172ecf30b9ba7b3fcfe69bf0ba6e72784376ef5e232caabc6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies the mapped documentation, unverified status, and code/document security discrepancy, then pauses pending required PM/Security handoff evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de; fixture_sha256=fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d; output_sha256=cfe45e52c4ea08db118a8115e8c189824d9e58d37622b5d7a7585f268acee3a2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produces a complete code/document discrepancy review and remediation suggestion, but does not address the required PM escalation workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the required PM/Security handoff packet and confirmed feature_path to exercise the formal escalation and issue-creation steps.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-005-mapped-search-security`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d` from `agents/security/test/appsec-checklist/evals/workspace/eval-005-mapped-search-security`.
- Fixture SHA-256: `fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d`
- Prompt SHA-256: `e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `812b371fc30792cb2b0cf8d96079b3244c95b93efab7638e085d4e955d6ea42c`
- Skill overlay SHA-256: `5b2b2b7a3b96eded32c11959c382e7fa8aafb204f59c1c353154bae2cdaf9c71`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `d863b13d3e997477097b1a2de108729923e21619e10b2847114ea312db1c1bc8`
- Metadata SHA-256: `44e3487a1b0a940b7bf23d73f980b7d71bd0be1a4d04a13c48606fd67383de8a`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | The output identifies the change-map and required API document, but locked evidence cannot prove read order or that unrelated formal documents were not traversed. |
| `verifies_against_code` | PASS | The output cites search-handler.js, identifies direct query interpolation without placeholders/parameters, contrasts it with the parameterized-query documentation claim, and assesses SQL injection risk from the code. |
| `treats_unverified_as_low_trust` | FAIL | The output contrasts documentation with code, but does not identify the required document's last_verified_version as unverified or explicitly state that this lowered trust and required expanded code verification. |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | The output states that no PM/Security handoff, PM PRD, or feature_path is available and therefore does not create a report; locked evidence does not establish the runtime prerequisites for PM classification and issue creation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de; fixture_sha256=fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d; output_sha256=885cc0d4f1ca10419e335bdac7987335bcb0534ba78a580d435761cc7bc9bb80; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies and demonstrates the SQL injection risk and documentation mismatch, but omits the document's unverified status and does not exercise the escalation workflow.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de; fixture_sha256=fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d; output_sha256=3f4915f74750bb8fb9d3b6dd1229fa46a69efb40efbef908b3e4db0ada43b024; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies direct SQL interpolation, documents the documentation/code mismatch, notes unverified documentation, and reports no mutation.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output omits the required identification and treatment of last_verified_version: unverified.​​​​
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-005-mapped-search-security`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d` from `agents/security/test/appsec-checklist/evals/workspace/eval-005-mapped-search-security`.
- Fixture SHA-256: `fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d`
- Prompt SHA-256: `e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8638f695ab2249699760b63a17b3618bf2d964d5ae466881f575505e2674bdaf`
- Skill overlay SHA-256: `7a46c5f912eabaa23dbb3c81db666071019107df43f45f25b7e8f552cbe709f8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `d863b13d3e997477097b1a2de108729923e21619e10b2847114ea312db1c1bc8`
- Metadata SHA-256: `44e3487a1b0a940b7bf23d73f980b7d71bd0be1a4d04a13c48606fd67383de8a`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | With-skill output cites the change map, identifies docs/site/api/user-search.md as required, and discusses only the mapped API document plus code. |
| `verifies_against_code` | PASS | It directly cites search-handler.js and identifies the mismatch between the documented parameterized query and actual direct interpolation of query into SQL. |
| `treats_unverified_as_low_trust` | PASS | It identifies last_verified_version as unverified and bases the security conclusion on the code rather than accepting the document declaration. |
| `escalates_fact_changing_conclusion_to_pm` | FAIL | It recommends updating the document but does not state that the changed conclusion must be returned to pm-agent for classification and issue creation, nor provide the required escalation evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de; fixture_sha256=fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d; output_sha256=e9f35be3e245d1182fdc22bab6eb05381b104ac3722a6e33c24cec4ed3046502; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly followed the mapped-document and code-verification requirements and treated the document as unverified, but omitted the required pm-agent escalation and issue-creation workflow.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de; fixture_sha256=fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d; output_sha256=235fcd1086cbf7edf74f2d3fac74da74ecde7cdfc0f438ce043dce4b3421d385; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identified the SQL injection, documentation/code mismatch, change-map requirement, and unverified document status, but did not address pm-agent escalation.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output omits mandatory escalation to pm-agent for classification and issue creation when correcting the formal documentation fact.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-005-mapped-search-security`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d` from `agents/security/test/appsec-checklist/evals/workspace/eval-005-mapped-search-security`.
- Fixture SHA-256: `fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d`
- Prompt SHA-256: `e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `095129ad5c17fd8974fdea44f1054ac02e7fa8f954b0e4a1a1d1a0ef185f9ce5`
- Skill overlay SHA-256: `5839d5cfe31d4e5dc5e9520f24a99b1147c97570ef1cc156eb90972408a49170`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `d863b13d3e997477097b1a2de108729923e21619e10b2847114ea312db1c1bc8`
- Metadata SHA-256: `44e3487a1b0a940b7bf23d73f980b7d71bd0be1a4d04a13c48606fd67383de8a`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill 输出引用并使用了 change-map 指定的 docs/site/api/user-search.md，且未引入无关正式文档。 |
| `verifies_against_code` | PASS | 明确将文档的参数化查询声明与 search-handler.js 中模板字符串直接拼接 query 的事实进行对照，并据代码事实判定 SQL 注入风险。 |
| `treats_unverified_as_low_trust` | PASS | 识别 last_verified_version 为 unverified，并将关键判断建立在代码核证上，而非直接采信文档。 |
| `escalates_fact_changing_conclusion_to_pm` | FAIL | 未提及将改变正式文档事实的结论和证据回交 pm-agent、创建 issue，或产出 docs/security/过程报告；仅建议更新文档。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de; fixture_sha256=fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d; output_sha256=9c9a7081c685ffd78b70eaf5a6f141a34dead9071d3474485c619d39d73e1a39; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确读取并核对映射文档、代码和 unverified 状态，准确判定风险；未执行或记录所需的 pm-agent 分类、issue 创建及升级证据产出。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de; fixture_sha256=fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d; output_sha256=0d3793321c55ef35dbed1153684f678a87c7913d2df74a46645a87bdab85615f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别代码与文档不一致及 SQL 注入风险，但未完成规定的 pm-agent 升级要求。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足改变正式文档事实后的 pm-agent 升级、issue 创建和升级证据产出要求。
- Next: 补充将结论与证据回交 pm-agent 分类、创建 issue，并产出 docs/security/过程报告的记录。

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

# Eval Result: eval-005-mapped-search-security

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-005-mapped-search-security`
- Test case: Mapped Search Security Documentation
- Workspace: `workspace/eval-005-mapped-search-security`
- Natural user prompt:

> 请审查 src/api/search-handler.js 的用户搜索安全性，重点检查查询参数如何进入数据查询，并给出证据、影响和修复建议。

- Expected artifact: 优先读取 change-map 命中的搜索 API 文档，再以代码核对查询构造；将 unverified 文档按最低信任处理并报告参数化声明与代码插值事实的不一致。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/appsec-checklist--eval-005-mapped-search-security/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `246474747e13b38824929dd18bb0b6743805302db0f636f44fbd4479602b83cc`。
- Lane isolation: 先完成并销毁全部 `without_skill` 独立顶层临时目录，再创建任何 `with_skill` 目录；每条 lane 使用独立的顶层临时 workspace、`HOME` 与 `CODEX_HOME`，不存在可供另一条 candidate 读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt 与相同初始 fixture；仅 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 skill，`without_skill` 未安装任何目标 skill。
- Evidence isolation: 所有 candidate 会话结束并删除各自临时根后，才将内存中的最终 workspace 快照与 transcript 持久化到 runtime root；candidate transcript 泄漏扫描未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、judge/verdict 或 expected output/assertion 脚手架。
- Judge: candidate 全部结束后，由第三个独立、只读的 fresh Codex 会话依据当前 assertions、两条 candidate 输出、transcript 与最终 workspace 快照判定。

## Latest Result

- Behavior result: **FAIL**（PASS 2 / FAIL 2 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: FAIL

## Historical Contract Note

上一份 durable comparison 基于 issue #234 修复前会向 baseline 泄漏规则的旧契约，因此标记为 `BLOCKED`。本轮使用当前无泄漏 prompt/fixture 重新生成两条 lane，未复用旧 baseline 或旧结论。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `reads_mapped_docs_first`<br>命中 change-map 后优先读取搜索 API required_docs | FAIL | transcript 显示先读取目标代码（item_3），随后在同一命令中先读 user-search.md、再读 change-map.yaml（item_5）；未按 change-map 反查后优先读取 required_docs。 | FAIL | transcript 未读取 change-map 后按 required_docs 顺序探索；先读代码，之后同一命令先读 API 文档再读 change-map。 |
| `verifies_against_code`<br>以处理器代码核对查询参数安全声明 | PASS | 候选结论明确引用 src/api/search-handler.js:1-2 的模板字符串直接插入 query，并指出其与文档所称参数化查询不一致。 | PASS | 候选结论明确核对 src/api/search-handler.js:2 的直接插值，并给出可形成恒真条件的输入示例。 |
| `treats_unverified_as_low_trust`<br>将 unverified 搜索文档按最低信任处理 | PASS | transcript 读取了文档的 last_verified_version: unverified；最终结论以代码事实为依据，未采信参数化声明，并扩大说明调用方、数据库适配层等尚未确认的范围。 | PASS | transcript 读取了文档的 last_verified_version: unverified；结论仍以代码中的直接 SQL 插值为核心证据，并将文档声明列为不一致。 |
| `escalates_fact_changing_conclusion_to_pm`<br>改变正式文档事实的结论升级 | FAIL | 结论明确改变了正式 API 文档关于参数化查询的事实，但最终工作区仅有源代码、change-map 和 API 文档，没有 docs/security/{feature_path}/appsec-checklist.md；transcript 也没有回交 pm-agent、分类或创建 issue 的证据。 | FAIL | 同样指出正式 API 文档与代码不一致，但最终工作区没有 Security-owned 报告，且无 PM 回交、分类或 issue 创建证据。 |

## With-Skill Behavior

发现代码与文档不一致及 SQL 注入风险，但未按契约完成 PM 升级、创建 issue 或产出 Security-owned 报告。

## Fresh Without-Skill Baseline

同样识别了代码中的直接 SQL 插值和文档不一致；未完成映射文档优先顺序及升级产物。

## Failures

- with-skill 未满足 mapped-doc 优先读取顺序。
- with-skill 在触发正式文档事实变更升级时未产出 Security 报告，也未回交 pm-agent 并创建 issue。

## Not Exercised

- 无。

## Next Steps

- 补充 docs/security/{feature_path}/appsec-checklist.md，并将代码/文档不一致及证据回交 pm-agent 分类和创建 issue。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` workspace 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
