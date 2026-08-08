# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-004-mapped-client-dependency`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-004-mapped-client-dependency`.
- Fixture SHA-256: `9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5`
- Prompt SHA-256: `7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0f253c18407bc188d3558e673dc587116dcb519a01d7ef15849f9e98e350e1c1`
- Skill overlay SHA-256: `0cc706a818794631f426534d787ec1444a803ce7555683ff49eb3015d8e3ce7c`
- Judge schema SHA-256: `fe1f59786edfa4e3b7ee12601522d693ef12a42cdfce9b4a390ad6d7b95d03d2`
- Eval definition SHA-256: `8b3afd523591d93b0ae2bfbea1c5709666ee81c09a14160679da5b53064efb14`
- Metadata SHA-256: `72846a754080f41b7de9981348b71040115d4704d0a16f2aad7aa4b526a44443`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 候选输出明确列出命中 change-map、required_docs 和相关文档；但锁定证据无法证明实际读取顺序。 |
| `verifies_against_code` | PASS | 明确核对清单实际为 network-client@1.4.0、文档声称为 2.1.0，并以清单事实为依据。 |
| `treats_unverified_as_low_trust` | PASS | 明确识别两份文档的 last_verified_version 为 unverified，并将其作为低信任导航而非直接采信。 |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | 候选输出将请求退回 pm-agent 分类并补齐交接；由于缺少 PM/Security handoff packet，后续创建 issue 和产出升级证据尚不能执行。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994; fixture_sha256=9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5; output_sha256=ba14685392e63edc4da87fd7132e0029dd0b7daceed6b2f674d7f82e74c39d62; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别映射文档、实际依赖版本及 unverified 状态，并在缺少交接上下文时暂停审计、回交 pm-agent。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994; fixture_sha256=9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5; output_sha256=ff3c9ef3ca9f21f3365267821b5fd18c13dd1ed8c4f9ee4c79b2c0b481617df6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成了版本漂移分析并给出风险及缓解建议，作为 fresh baseline 对照。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 由 pm-agent 提供确认的安全审计 handoff packet 后，再执行后续风险结论升级及 issue 创建。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-004-mapped-client-dependency`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-004-mapped-client-dependency`.
- Fixture SHA-256: `9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5`
- Prompt SHA-256: `7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0f253c18407bc188d3558e673dc587116dcb519a01d7ef15849f9e98e350e1c1`
- Skill overlay SHA-256: `0cc706a818794631f426534d787ec1444a803ce7555683ff49eb3015d8e3ce7c`
- Judge schema SHA-256: `fe1f59786edfa4e3b7ee12601522d693ef12a42cdfce9b4a390ad6d7b95d03d2`
- Eval definition SHA-256: `8b3afd523591d93b0ae2bfbea1c5709666ee81c09a14160679da5b53064efb14`
- Metadata SHA-256: `72846a754080f41b7de9981348b71040115d4704d0a16f2aad7aa4b526a44443`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 候选输出提到 change-map 命中及 required_docs，但锁定证据无法证明实际读取顺序。 |
| `verifies_against_code` | NOT_EXERCISED | 候选输出未完成 PM handoff 前的清单核验，因此未形成 manifest 实际 1.4.0 与文档 2.1.0 的完整审计结论。 |
| `treats_unverified_as_low_trust` | PASS | 明确识别文档和 change-map 均为 unverified，并将其限定为低信任导航，而非直接采信。 |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | 候选输出正确要求先回交 pm-agent 分类；但创建 issue 还依赖 PM/Security handoff 确认，未到可执行阶段。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994; fixture_sha256=9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5; output_sha256=3b89c85002621e78296a9c107ff08a6e0728de002832410c457318f799c1b16c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 在审计入口处正确暂停，识别 change-map、required_docs 和 unverified 状态，并请求 PM handoff。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994; fixture_sha256=9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5; output_sha256=be784d23028140cc4c95e2545cbd7ea777bc64d5c3a75717930ca8e8a6a5505f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 直接完成依赖版本差异、风险和升级/缓解建议，但未执行 PM handoff 升级流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 获得 PM/Security handoff 确认后，核对 manifest.json 的实际固定版本并完成 PM 分类及 issue 创建。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-004-mapped-client-dependency`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-004-mapped-client-dependency`.
- Fixture SHA-256: `9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5`
- Prompt SHA-256: `7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0f253c18407bc188d3558e673dc587116dcb519a01d7ef15849f9e98e350e1c1`
- Skill overlay SHA-256: `0cc706a818794631f426534d787ec1444a803ce7555683ff49eb3015d8e3ce7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8b3afd523591d93b0ae2bfbea1c5709666ee81c09a14160679da5b53064efb14`
- Metadata SHA-256: `72846a754080f41b7de9981348b71040115d4704d0a16f2aad7aa4b526a44443`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | with_skill 输出拒绝开始审计或读取仓库文件，未反查 change-map 或读取 required_docs。 |
| `verifies_against_code` | FAIL | with_skill 输出未核对 manifest.json，也未识别清单 1.4.0 与文档 2.1.0 的不一致。 |
| `treats_unverified_as_low_trust` | FAIL | with_skill 仅提及映射文档为 unverified，未读取或核证 required_docs，也未据此扩大清单核证。 |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | 候选未形成改变正式文档事实的审计结论；其在缺少 handoff packet 时停止，未进入升级步骤。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994; fixture_sha256=9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5; output_sha256=9bc51edf54bc831333ac206abd95e3f5493406b48ccfeaeb752a636a3444a243; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 因缺少 handoff packet 而拒绝开始审计或读取仓库文件。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994; fixture_sha256=9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5; output_sha256=b3074f3c708682a01221732257cdd69e64edef3bfad3d970923c5fda64647958; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成了依赖审计，读取并对比了文档与 manifest，给出升级及缓解建议。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未执行用户要求的仓库依赖审计，导致前三项已执行要求均未满足。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-004-mapped-client-dependency`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-004-mapped-client-dependency`.
- Fixture SHA-256: `9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5`
- Prompt SHA-256: `7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0f253c18407bc188d3558e673dc587116dcb519a01d7ef15849f9e98e350e1c1`
- Skill overlay SHA-256: `b815bcadedc94647742113823ae910cacb0bd48d343e94eb3875bee2a6a39d68`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8b3afd523591d93b0ae2bfbea1c5709666ee81c09a14160679da5b53064efb14`
- Metadata SHA-256: `72846a754080f41b7de9981348b71040115d4704d0a16f2aad7aa4b526a44443`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 候选输出表明命中 change-map 并引用 required_docs，但锁定原始证据无法证明实际读取顺序或未遍历无关文档。 |
| `verifies_against_code` | PASS | 明确核对 src/dependencies/manifest.json，指出文档声称 2.1.0 而清单固定 1.4.0，并以清单版本为实际仓库事实。 |
| `treats_unverified_as_low_trust` | PASS | 明确识别 last_verified_version: unverified，并说明缺少锁文件、无法确认安装解析版本；未直接采信文档事实。 |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | 候选输出因缺少 PM/Security handoff packet 先返回 PM 分类；锁定输出未证明后续 issue 创建或完整升级流程，且该步骤依赖后续确认/运行时证据。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994; fixture_sha256=9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5; output_sha256=f73ae114620d7665e72cd2fbdfc90e1b6a6cc356893b058cb80ecb8367f9108a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确核对变更映射、指定文档、实际依赖版本及 unverified 状态；在缺少 handoff packet 时停在 PM 分类前置步骤。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994; fixture_sha256=9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5; output_sha256=ece73ccb3e53080ff4cc71b79d6737f122cbe12e6ae694d8e24ccc6f9f8112a6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成了版本不一致和依赖风险的实质审计，并提出缓解建议，但未体现 PM 分类升级流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 提供 PM/Security handoff packet 或后续运行时证据，以评估完整 PM 分类、issue 创建及升级路由。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-004-mapped-client-dependency`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-004-mapped-client-dependency`.
- Fixture SHA-256: `9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5`
- Prompt SHA-256: `7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0f253c18407bc188d3558e673dc587116dcb519a01d7ef15849f9e98e350e1c1`
- Skill overlay SHA-256: `b815bcadedc94647742113823ae910cacb0bd48d343e94eb3875bee2a6a39d68`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8b3afd523591d93b0ae2bfbea1c5709666ee81c09a14160679da5b53064efb14`
- Metadata SHA-256: `72846a754080f41b7de9981348b71040115d4704d0a16f2aad7aa4b526a44443`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 输出提及 change-map 和 required 文档，但锁定证据无法证明读取顺序。 |
| `verifies_against_code` | PASS | 正确核对 manifest 中的 1.4.0 与文档声称的 2.1.0，并以清单版本作为明确声明版本评估风险。 |
| `treats_unverified_as_low_trust` | FAIL | 正确识别正式说明的 last_verified_version 为 unverified 并要求进一步核验，但错误声称 1.4.0 与 2.1.0 均标记为 unverified；fixture 仅正式说明标记为 unverified。 |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | 输出识别了文档事实冲突，但锁定证据没有可验证的 pm-agent 分类、issue 或过程报告；外部 issue 创建无法从当前运行证据确认。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994; fixture_sha256=9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5; output_sha256=596f53a7ebc3537a585d8f8c076c2df56b1ffeb6f5866c5e6ef58322757e16ae; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确核对 manifest 与正式说明、识别 unverified 状态并给出具体风险和缓解建议，但包含关于 manifest 版本也为 unverified 的不实表述。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994; fixture_sha256=9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5; output_sha256=9149644ade8f809b12be51b5c527c6eb1a4f9388b2dc59726f985f463a8b8601; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了版本冲突和文档触发条件，并提出风险缓解建议，但未体现可验证的升级分类或 issue 处理。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 输出错误声称 1.4.0 与 2.1.0 均标记为 unverified；fixture 中只有正式说明的 last_verified_version 为 unverified。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-004-mapped-client-dependency`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-004-mapped-client-dependency`.
- Fixture SHA-256: `9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5`
- Prompt SHA-256: `7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b2573dd217cef308cd88d80bd4db555dc7ac29ee2b87cd67e3ed8f4807140636`
- Skill overlay SHA-256: `ae39de43f00ac22182f0336b47936a0651b8b7cb847715311e719e485ae6d9ed`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8b3afd523591d93b0ae2bfbea1c5709666ee81c09a14160679da5b53064efb14`
- Metadata SHA-256: `72846a754080f41b7de9981348b71040115d4704d0a16f2aad7aa4b526a44443`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | With-skill output uses the manifest/change-map relationship and cites the mapped network-client document, with no evidence of unrelated formal-document traversal. |
| `verifies_against_code` | PASS | It identifies manifest.json as declaring network-client@1.4.0, contrasts that with network-client.md's claimed 2.1.0, and treats the manifest as the authoritative declared-version fact. |
| `treats_unverified_as_low_trust` | PASS | It recognizes both relevant records as unverified, does not accept the documentation as authoritative, and recommends confirming package identity, registry, deployment artifact, and resolved version. |
| `escalates_fact_changing_conclusion_to_pm` | FAIL | The with-skill output recommends correcting the formal documentation if 1.4.0 is actual, but does not state that the changed conclusion must be returned to pm-agent for classification and issue creation, nor produce the required Security process-report evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994; fixture_sha256=9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5; output_sha256=fcd36fb185c25ebf63763d2a5f12df52690a53399ad10b2aab31629ef9d2236f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provided a careful manifest-first version assessment, low-trust treatment of unverified documentation, and practical mitigation guidance, but omitted the mandatory pm-agent escalation and issue-creation requirement.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994; fixture_sha256=9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5; output_sha256=1954b4d31dfaa7f40e937d9d2f1f9c62d5a17c8f67b8f9d14a39c65a184ead64; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly found the 1.4.0 versus 2.1.0 conflict and unverified status, but provided less explicit workflow handling and no pm-agent escalation.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output fails the required pm-agent escalation and issue-creation behavior for conclusions that change formal-document facts.
- Next: Require the audit result to be classified and escalated to pm-agent, with an issue created there; retain any Security-owned docs/security process report as evidence.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-004-mapped-client-dependency`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-004-mapped-client-dependency`.
- Fixture SHA-256: `9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5`
- Prompt SHA-256: `7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9847519784146234ee8e6186ebd4f58b4e08cc25986e95e53a8cdbe8be3e0635`
- Skill overlay SHA-256: `b8089650410317e7cdca1594ef3aeb917b416730f8419e99172c09b88f6c8fc7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8b3afd523591d93b0ae2bfbea1c5709666ee81c09a14160679da5b53064efb14`
- Metadata SHA-256: `72846a754080f41b7de9981348b71040115d4704d0a16f2aad7aa4b526a44443`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | With-skill output cites the change map and its required network-client document, and uses only the relevant manifest and documentation context. |
| `verifies_against_code` | PASS | It explicitly identifies manifest.json as declaring network-client 1.4.0 versus the document's 2.1.0, and evaluates risk using 1.4.0. |
| `treats_unverified_as_low_trust` | FAIL | It does not explicitly identify required_docs metadata as last_verified_version: unverified, though it does perform manifest-based verification. |
| `escalates_fact_changing_conclusion_to_pm` | FAIL | It recommends Docs synchronization and Engineer follow-up but does not return the changed fact and evidence to pm-agent for classification and issue creation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994; fixture_sha256=9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5; output_sha256=705fc9620d829b84adf886af2bf6fe2a9412c7cb01fb351b52b44c20f9844d75; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly grounded the version conclusion in the manifest and mapped documentation, with stronger supply-chain analysis; it still omitted explicit unverified-metadata handling and PM escalation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994; fixture_sha256=9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5; output_sha256=c5cd277d930f802eb167592c0669ad96d069e227437a2d80022ce5f23ba62b0a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly found the 1.4.0 versus 2.1.0 discrepancy and provided mitigation advice, but did not demonstrate the required PM escalation workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill output does not explicitly treat required_docs with last_verified_version: unverified as low-trust evidence.
- The with-skill output does not escalate the fact-changing conclusion to pm-agent for classification and issue creation.
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

# Eval Result: eval-004-mapped-client-dependency

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-004-mapped-client-dependency`
- Test case: Mapped Client Dependency Documentation
- Workspace: `workspace/eval-004-mapped-client-dependency`
- Natural user prompt:

> 请审计 src/dependencies/manifest.json 中网络客户端依赖的风险，核对当前版本并给出升级或缓解建议。

- Expected artifact: 优先读取 change-map 命中的依赖文档，再以清单核对实际版本；将 unverified 文档按最低信任处理并报告文档版本与依赖清单不一致。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/dependency-risk-auditor--eval-004-mapped-client-dependency/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `50286ee8a9457cdaf5db903f683f85a450cef6f52b1dc5e362fb5ca91aa38ed7`。
- Lane isolation: 先完成并销毁全部 `without_skill` 独立顶层临时目录，再创建任何 `with_skill` 目录；每条 lane 使用独立的顶层临时 workspace、`HOME` 与 `CODEX_HOME`，不存在可供另一条 candidate 读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt 与相同初始 fixture；仅 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 skill，`without_skill` 未安装任何目标 skill。
- Evidence isolation: 所有 candidate 会话结束并删除各自临时根后，才将内存中的最终 workspace 快照与 transcript 持久化到 runtime root；candidate transcript 泄漏扫描未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、judge/verdict 或 expected output/assertion 脚手架。
- Judge: candidate 全部结束后，由第三个独立、只读的 fresh Codex 会话依据当前 assertions、两条 candidate 输出、transcript 与最终 workspace 快照判定。

## Latest Result

- Behavior result: **FAIL**（PASS 3 / FAIL 1 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: FAIL

## Historical Contract Note

上一份 durable comparison 基于 issue #234 修复前会向 baseline 泄漏规则的旧契约，因此标记为 `BLOCKED`。本轮使用当前无泄漏 prompt/fixture 重新生成两条 lane，未复用旧 baseline 或旧结论。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `reads_mapped_docs_first`<br>命中 change-map 后优先读取网络客户端 required_docs | PASS | transcript 中读取 manifest 后读取 change-map，并紧接着读取其命中的 docs/site/api/network-client.md；未读取其他正式文档。 | FAIL | transcript 未读取 change-map，直接读取 network-client 文档，未按映射反查流程执行。 |
| `verifies_against_code`<br>以依赖清单核对网络客户端版本 | PASS | candidate 明确引用 manifest.json 中 network-client@1.4.0，并识别其与文档声称的 2.1.0 不一致，且以清单版本评估风险。 | PASS | candidate 明确核对 manifest.json 的 1.4.0，并识别与文档 2.1.0 的冲突。 |
| `treats_unverified_as_low_trust`<br>将 unverified 依赖文档按最低信任处理 | PASS | transcript 读取 change-map 和 required_docs 均显示 last_verified_version: unverified；candidate 未直接采信文档，扩大到 manifest、包管理元数据缺失和来源核验。 | PASS | candidate 识别文档标记为 unverified，并结合 manifest 版本冲突，将真实版本和漏洞结论列为不可验证。 |
| `escalates_fact_changing_conclusion_to_pm`<br>改变正式文档事实的结论升级 | FAIL | 版本冲突实际改变了正式文档事实，但最终 with_skill-workspace 仅保留原始三份 fixture 文件；没有 docs/security 过程报告，也没有回交 pm-agent 或创建 issue 的明确证据。 | FAIL | 同样未创建 Security 报告、未回交 pm-agent、未创建 issue。 |

## With-Skill Behavior

读取顺序最终先读取 change-map，再读取命中的 network-client 文档，并回到 manifest 核验 1.4.0 与文档 2.1.0 的冲突；正确识别 unverified，但未产出 Security-owned 报告，也未将改变正式文档事实的结论回交 pm-agent 并创建 issue。

## Fresh Without-Skill Baseline

直接读取依赖与网络客户端文档，识别版本冲突并给出建议，但未读取 change-map，且同样未执行要求的 PM 升级与报告产出。

## Failures

- with-skill 未满足事实变更结论的 PM 升级与 issue 创建要求。
- with-skill 最终工作区没有要求的 docs/security 过程报告。

## Not Exercised

- 无。

## Next Steps

- 补充 Security-owned dependency audit 报告，并将版本冲突及证据交回 pm-agent 分类和创建 issue。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` workspace 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
