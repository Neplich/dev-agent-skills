# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-004-mapped-profile-retention`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb` from `agents/security/test/privacy-surface-mapper/evals/workspace/eval-004-mapped-profile-retention`.
- Fixture SHA-256: `ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb`
- Prompt SHA-256: `15781c686db28c8e23be7d15ddb44295e5640725a6c0d3e97e4814f9916ad62f`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `25bd4dbed66f3625883b2a2072dcd568eef569278521e1eac012e86f61347836`
- Skill overlay SHA-256: `840e4d3e20057f4834a3b010b4142d0e7be2f66540c525231dc34075db0dbbee`
- Judge schema SHA-256: `fe1f59786edfa4e3b7ee12601522d693ef12a42cdfce9b4a390ad6d7b95d03d2`
- Eval definition SHA-256: `8768d40f89a0835f8bc18dc793ab9c71861c190253ab19b6d21f19d51aa1ed50`
- Metadata SHA-256: `7059498df03f32583db887e25af006a8504ba7d72f9cb363375b4bcdb24efad6`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 候选输出列出了 change-map、required_docs 和目标文档，但锁定证据无法证明实际读取顺序或未遍历无关文档。 |
| `verifies_against_code` | FAIL | with_skill 明确未回到 profile-processing.yaml 核对 90 天配置，也未识别 30 天与 90 天冲突或评估影响。 |
| `treats_unverified_as_low_trust` | PASS | with_skill 明确将 unverified 文档视为低信任，未直接采信 30 天结论；但未完成后续配置核证。 |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | 候选输出因缺少 PM/Security handoff packet 而暂停；尚未确认改变正式文档事实，因此后续 pm-agent 分类和 issue 创建未被 exercised。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=15781c686db28c8e23be7d15ddb44295e5640725a6c0d3e97e4814f9916ad62f; fixture_sha256=ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb; output_sha256=07c8903598a8a460de0b0c61b1d871c10c354492383b03cb7050085505139ee7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别映射、required_docs 和 unverified 状态，但在读取配置并核对实际保留期限前暂停。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=15781c686db28c8e23be7d15ddb44295e5640725a6c0d3e97e4814f9916ad62f; fixture_sha256=ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb; output_sha256=903b476811e8537486e45292f2cc9f667c4b91318c7d5704b9f2fff4b3bc4b65; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成了配置与文档的字段、目的和保留期限对比，但未体现低信任处理或 PM 升级。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未完成配置核对，遗漏了 90 天实际保留期限与文档 30 天声明的关键冲突及合规影响。
- Next: 补充 PM 分类/交接后，回到 profile-processing.yaml 核实 90 天配置并评估与文档 30 天声明的冲突。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-004-mapped-profile-retention`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb` from `agents/security/test/privacy-surface-mapper/evals/workspace/eval-004-mapped-profile-retention`.
- Fixture SHA-256: `ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb`
- Prompt SHA-256: `15781c686db28c8e23be7d15ddb44295e5640725a6c0d3e97e4814f9916ad62f`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `25bd4dbed66f3625883b2a2072dcd568eef569278521e1eac012e86f61347836`
- Skill overlay SHA-256: `840e4d3e20057f4834a3b010b4142d0e7be2f66540c525231dc34075db0dbbee`
- Judge schema SHA-256: `fe1f59786edfa4e3b7ee12601522d693ef12a42cdfce9b4a390ad6d7b95d03d2`
- Eval definition SHA-256: `8768d40f89a0835f8bc18dc793ab9c71861c190253ab19b6d21f19d51aa1ed50`
- Metadata SHA-256: `7059498df03f32583db887e25af006a8504ba7d72f9cb363375b4bcdb24efad6`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | The locked report names the matched change-map entry and required document, but the locked evidence cannot prove read order or that unrelated documents were not read. |
| `verifies_against_code` | PASS | The delivered report directly identifies 90 days in src/privacy/profile-processing.yaml versus 30 days in profile-data.md, notes runtime behavior is unestablished, and assesses the resulting retention/compliance risk. |
| `treats_unverified_as_low_trust` | PASS | The delivered report identifies both artifacts as unverified and explicitly treats them as low-trust navigation, while expanding verification to configuration and repository evidence. |
| `escalates_fact_changing_conclusion_to_pm` | PASS | The delivered security report escalates the conclusion and evidence to pm-agent for classification and a PM-owned issue, while assigning the formal-document audit to Docs and not modifying docs/site/. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=15781c686db28c8e23be7d15ddb44295e5640725a6c0d3e97e4814f9916ad62f; fixture_sha256=ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb; output_sha256=f33a8ea782bc30a56c56cdbb41f09abc846bbcef3f41379034e2a329204011c7; snapshot_sha256=73a7d8800ff73e7cf89b5ef2662942afcddf249a9e77ebd202969d4f39654fa0
- Behavior: Produced the required privacy report, verified the 30/90-day discrepancy against the configuration, treated unverified documents as low trust, and escalated to pm-agent.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=15781c686db28c8e23be7d15ddb44295e5640725a6c0d3e97e4814f9916ad62f; fixture_sha256=ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb; output_sha256=4e75d5592205c6a1e0758e19c8a6758289a38aa430e471ca42d8cce2234583f4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provided an accurate prose comparison of fields, purpose, and the 30/90-day discrepancy, but did not produce the required security report or explicit PM escalation.
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
- Eval: `eval-004-mapped-profile-retention`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb` from `agents/security/test/privacy-surface-mapper/evals/workspace/eval-004-mapped-profile-retention`.
- Fixture SHA-256: `ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb`
- Prompt SHA-256: `15781c686db28c8e23be7d15ddb44295e5640725a6c0d3e97e4814f9916ad62f`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `25bd4dbed66f3625883b2a2072dcd568eef569278521e1eac012e86f61347836`
- Skill overlay SHA-256: `840e4d3e20057f4834a3b010b4142d0e7be2f66540c525231dc34075db0dbbee`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8768d40f89a0835f8bc18dc793ab9c71861c190253ab19b6d21f19d51aa1ed50`
- Metadata SHA-256: `7059498df03f32583db887e25af006a8504ba7d72f9cb363375b4bcdb24efad6`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | With-skill output refuses to inspect the repository and provides no result based on the mapped required document. The fixture maps src/privacy/profile-processing.yaml to docs/site/api/profile-data.md. |
| `verifies_against_code` | FAIL | With-skill output does not inspect or report the fixture's actual 90-day retention, the document's 30-day claim, or the resulting inconsistency. |
| `treats_unverified_as_low_trust` | FAIL | Although the output asks for prerequisites, it does not identify either required document's last_verified_version as unverified or perform expanded configuration verification. |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | The with-skill lane never reaches or confirms a conclusion changing the formal document's facts, so the required PM classification and issue-creation step cannot be evaluated from the locked evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=15781c686db28c8e23be7d15ddb44295e5640725a6c0d3e97e4814f9916ad62f; fixture_sha256=ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb; output_sha256=57edc1035f340e6a20222c9f4e0d1c16d208953a5e7981d248b1324999fe0b90; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Blocks on an unsupported prerequisite and provides no privacy-processing analysis or escalation deliverable.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=15781c686db28c8e23be7d15ddb44295e5640725a6c0d3e97e4814f9916ad62f; fixture_sha256=ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb; output_sha256=b22b01403a25dfcb5995fbb56b395a6966c9743363f8e23b4ca3ed7844e02f3d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Reads and compares the mapped documentation and configuration, identifies the 30-day versus 90-day conflict, but does not perform the required PM escalation.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill output omits the requested mapped-document review, configuration verification, retention conflict, and unverified-document treatment.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-004-mapped-profile-retention`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb` from `agents/security/test/privacy-surface-mapper/evals/workspace/eval-004-mapped-profile-retention`.
- Fixture SHA-256: `ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb`
- Prompt SHA-256: `15781c686db28c8e23be7d15ddb44295e5640725a6c0d3e97e4814f9916ad62f`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `25bd4dbed66f3625883b2a2072dcd568eef569278521e1eac012e86f61347836`
- Skill overlay SHA-256: `4e2d7a3ffa0fc7b4cc84f02f24df4e35de821cbc6e0c580a1427e37709efb43b`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8768d40f89a0835f8bc18dc793ab9c71861c190253ab19b6d21f19d51aa1ed50`
- Metadata SHA-256: `7059498df03f32583db887e25af006a8504ba7d72f9cb363375b4bcdb24efad6`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 锁定原始证据无法证明读取顺序或是否遍历了无关文档；候选输出仅呈现结果。 |
| `verifies_against_code` | PASS | with_skill 明确回到配置核对：文档为 30 天、配置为 90 天，并指出无法从仓库验证实际运行时行为及其隐私合规风险。 |
| `treats_unverified_as_low_trust` | PASS | with_skill 识别 change-map 和正式说明为 unverified，并结合配置及缺少可验证删除实现，未直接采信文档或拒绝读取。 |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | 候选输出表示需先补充 PM/Security 交接包及 feature_path、返回 PM 分类；后续创建 issue 和产出 Security 过程报告尚无法在缺少这些输入时完成。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=15781c686db28c8e23be7d15ddb44295e5640725a6c0d3e97e4814f9916ad62f; fixture_sha256=ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb; output_sha256=c5f21c92a23ba6ab8b1244c5ed6c8665a8185bd0aa77f7c07a508e434c0cb259; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确核对配置与正式说明，谨慎处理 unverified 和无法验证的运行时行为，并停在等待 PM/Security 交接信息的下一步。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=15781c686db28c8e23be7d15ddb44295e5640725a6c0d3e97e4814f9916ad62f; fixture_sha256=ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb; output_sha256=3befd516d6065a8a02a11b420c0323d758cd300267648ff6a676da5daf8fbd22; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别字段、目的及 30/90 天保留期限冲突，但未体现 PM 分类升级或交接流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补充 PM/Security 交接包和已确认的 feature_path，以完成 PM 分类、issue 创建及 Security 过程报告。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-004-mapped-profile-retention`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb` from `agents/security/test/privacy-surface-mapper/evals/workspace/eval-004-mapped-profile-retention`.
- Fixture SHA-256: `ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb`
- Prompt SHA-256: `15781c686db28c8e23be7d15ddb44295e5640725a6c0d3e97e4814f9916ad62f`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `25bd4dbed66f3625883b2a2072dcd568eef569278521e1eac012e86f61347836`
- Skill overlay SHA-256: `4e2d7a3ffa0fc7b4cc84f02f24df4e35de821cbc6e0c580a1427e37709efb43b`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8768d40f89a0835f8bc18dc793ab9c71861c190253ab19b6d21f19d51aa1ed50`
- Metadata SHA-256: `7059498df03f32583db887e25af006a8504ba7d72f9cb363375b4bcdb24efad6`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | With-skill output identifies the change map and required profile document, and manifests show only relevant documents, but locked evidence cannot prove read order or that unrelated documents were not traversed. |
| `verifies_against_code` | PASS | With-skill output correctly reports the YAML value of 90 days versus the document’s 30 days, identifies a 60-day conflict, and explains the privacy-policy, deletion-flow, and lifecycle-control impact. |
| `treats_unverified_as_low_trust` | PASS | With-skill output identifies both relevant documents as unverified, does not treat either retention value as runtime truth, and calls for verification against deletion tasks or storage TTL. |
| `escalates_fact_changing_conclusion_to_pm` | FAIL | The output recommends PM/engineering confirmation but provides no evidence of returning the conclusion and evidence to pm-agent for classification or creating an issue; no delivery artifact records such an escalation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=15781c686db28c8e23be7d15ddb44295e5640725a6c0d3e97e4814f9916ad62f; fixture_sha256=ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb; output_sha256=df7d19ca786791fb6312f81122815a962858ab60623997fd2ada7410e5190c04; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a careful semantic comparison, treats unverified documentation as low trust, and describes the compliance impact, but lacks evidence of the required pm-agent classification and issue creation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=15781c686db28c8e23be7d15ddb44295e5640725a6c0d3e97e4814f9916ad62f; fixture_sha256=ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb; output_sha256=8601c99850815bddb4bb05c05f6f1f0778ad2f499d4f16625d1710392856516b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies the fields, purpose, and 90-day versus 30-day retention conflict, but does not demonstrate the required PM escalation.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane omits evidence of pm-agent escalation, classification, and issue creation required when the conclusion changes a formal-document fact.
- Next: Record the pm-agent handoff/classification and created issue in the delivery evidence.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-004-mapped-profile-retention`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb` from `agents/security/test/privacy-surface-mapper/evals/workspace/eval-004-mapped-profile-retention`.
- Fixture SHA-256: `ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb`
- Prompt SHA-256: `15781c686db28c8e23be7d15ddb44295e5640725a6c0d3e97e4814f9916ad62f`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ce73f0c2e691c2e71d4792a4ff83efe02c3a6714b22fe5c3733a875118131db8`
- Skill overlay SHA-256: `cd8ee54ef003ea53bd486a0be35c70dcd1362f3fd307cff51efdedb756e33a7d`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8768d40f89a0835f8bc18dc793ab9c71861c190253ab19b6d21f19d51aa1ed50`
- Metadata SHA-256: `7059498df03f32583db887e25af006a8504ba7d72f9cb363375b4bcdb24efad6`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | With-skill output cites the YAML, change-map, and mapped profile-data document, and does not cite unrelated formal documents. |
| `verifies_against_code` | PASS | It reports the configured 90-day retention versus the documented 30 days, notes the 60-day discrepancy, and assesses the privacy risk while distinguishing configuration from unverified runtime behavior. |
| `treats_unverified_as_low_trust` | PASS | It identifies last_verified_version as unverified and calls for implementation or runtime verification rather than directly trusting or rejecting the documentation. |
| `escalates_fact_changing_conclusion_to_pm` | FAIL | The output does not return the changed conclusion and evidence to pm-agent, classify it, or create an issue; it only recommends confirming and synchronizing the values. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=15781c686db28c8e23be7d15ddb44295e5640725a6c0d3e97e4814f9916ad62f; fixture_sha256=ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb; output_sha256=1fe9ad815e8d31fbd5b0384483968676e9e5b98e40abc47185856d742eff63da; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Uses the mapped documents, verifies the configuration discrepancy, treats unverified metadata as low trust, and appropriately qualifies runtime uncertainty, but omits the required pm-agent escalation and issue creation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=15781c686db28c8e23be7d15ddb44295e5640725a6c0d3e97e4814f9916ad62f; fixture_sha256=ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb; output_sha256=697a7f34f92e8647973025c1c5057271a7265cbdac28723b973530f870f0d9b8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Identifies the 90-day versus 30-day discrepancy but says the actual value is undetermined and does not perform the required escalation.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill output omits the required pm-agent classification and issue creation when the conclusion changes a formal document fact.
- Next: Escalate the conclusion and evidence to pm-agent for classification and issue creation.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-004-mapped-profile-retention`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb` from `agents/security/test/privacy-surface-mapper/evals/workspace/eval-004-mapped-profile-retention`.
- Fixture SHA-256: `ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb`
- Prompt SHA-256: `15781c686db28c8e23be7d15ddb44295e5640725a6c0d3e97e4814f9916ad62f`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `32486beb9db21ed173f2083e3323014ff05de4963e7a8b1d84d40eb43ab3aa33`
- Skill overlay SHA-256: `874b129b045f44af288c1af739a4a66f07931a151f79399740585f1fce30c452`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8768d40f89a0835f8bc18dc793ab9c71861c190253ab19b6d21f19d51aa1ed50`
- Metadata SHA-256: `7059498df03f32583db887e25af006a8504ba7d72f9cb363375b4bcdb24efad6`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | With-skill output cites the change map, its required document, and the linked privacy configuration, with no unrelated formal documents presented. |
| `verifies_against_code` | FAIL | It correctly identifies the 30-day versus 90-day conflict and distinguishes configuration from runtime evidence, but does not evaluate the compliance impact using the configuration fact as required. |
| `treats_unverified_as_low_trust` | FAIL | The fixture marks last_verified_version as unverified, but the with-skill output never identifies or discusses this status. |
| `escalates_fact_changing_conclusion_to_pm` | FAIL | The output recommends confirmation and document synchronization but does not return the changed conclusion to pm-agent, classify it, or create an issue; it also provides no required Security process report. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=15781c686db28c8e23be7d15ddb44295e5640725a6c0d3e97e4814f9916ad62f; fixture_sha256=ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb; output_sha256=47389664dcf3785f4d2a4a1847a1f560943e6ded15f4203a7779d1c5bf53fc80; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Uses the change map and linked documents, accurately separates configuration declarations from runtime evidence, but omits unverified-status handling, compliance-impact evaluation, and required pm-agent issue escalation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=15781c686db28c8e23be7d15ddb44295e5640725a6c0d3e97e4814f9916ad62f; fixture_sha256=ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb; output_sha256=5ac6fbda5924bcde872bc30514dd09b5bd1ed9b0dbf4ffad3a06fcb53dac5b22; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly reports the field and purpose matches and identifies the 30-day versus 90-day retention conflict, but does not demonstrate the required unverified-document handling or pm-agent escalation.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- verifies_against_code: missing explicit compliance-impact evaluation grounded in the 90-day configuration.
- treats_unverified_as_low_trust: does not address last_verified_version: unverified.
- escalates_fact_changing_conclusion_to_pm: no pm-agent classification or issue creation, and no applicable Security process report.
- Next: Explicitly treat the unverified document as low trust and expand configuration-based verification.
- Next: State the compliance impact of the 90-day configured retention conflicting with the 30-day formal documentation.
- Next: Escalate the changed conclusion to pm-agent with classification and create the required issue.

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

# Eval Result: eval-004-mapped-profile-retention

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-004-mapped-profile-retention`
- Test case: Mapped Profile Data Retention
- Workspace: `workspace/eval-004-mapped-profile-retention`
- Natural user prompt:

> 请梳理 src/privacy/profile-processing.yaml 的个人资料处理面，重点核对收集字段、处理目的和删除后的保留期限。

- Expected artifact: 优先读取 change-map 命中的个人资料处理文档，再以配置核对保留期限；将 unverified 文档按最低信任处理并报告 30 天声明与 90 天配置事实的不一致。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/privacy-surface-mapper--eval-004-mapped-profile-retention/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `fe202006e2cd8c214b98b02eac15e2f5aa8a803e13a5f2bb5e302fccc9ac60ba`。
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
| `reads_mapped_docs_first`<br>命中 change-map 后优先读取个人资料 required_docs | FAIL | transcript 先读取 profile-processing.yaml，再读取接口文档和 change-map；未先反查 change-map 后优先读取 required_docs。 | FAIL | transcript 未读取 change-map 或 required_docs 文档。 |
| `verifies_against_code`<br>以处理配置核对删除后的保留期限 | PASS | transcript 回读配置并明确指出配置为 90 天、文档声称 30 天；candidate 以配置事实识别冲突并要求统一规则。 | FAIL | 仅报告配置中的 90 天，未读取或识别 required 文档中的 30 天冲突。 |
| `treats_unverified_as_low_trust`<br>将 unverified 隐私文档按最低信任处理 | PASS | candidate 明确识别文档 last_verified_version 为 unverified，并说明 30 天不能作为已核实有效规则，同时以配置进行核证。 | FAIL | 未读取文档元数据，未识别 unverified，也未扩大配置核证。 |
| `escalates_fact_changing_conclusion_to_pm`<br>改变正式文档事实的结论升级 | FAIL | 期限冲突改变正式 docs/site 文档事实，且契约要求回交 pm-agent 分类并创建 issue、产出 docs/security 报告；最终快照中仅有原始 fixture，没有报告、升级或 issue 证据。 | NOT EXERCISED | baseline 未读取正式文档，未形成改变正式文档事实的结论，故该触发条件未实际发生。 |

## With-Skill Behavior

发现配置与 unverified 文档的 90/30 天保留期限冲突，并完成字段、目的与配置核对；但未按 change-map 优先顺序读取文档，也未生成 Security 报告或回交 pm-agent 分类建 issue。

## Fresh Without-Skill Baseline

仅读取配置并总结 90 天，未读取 change-map、required_docs，也未识别文档冲突或 unverified 信任问题。

## Failures

- with-skill 未遵守 change-map → required_docs 的读取顺序。
- with-skill 未产出 Security-owned privacy-map 报告，也未按触发条件升级至 pm-agent 分类并创建 issue。

## Not Exercised

- 无。

## Next Steps

- 若补测，应检查 transcript 中 change-map 反查及 required_docs 优先读取顺序。
- 应在最终工作区核验 docs/security/{feature_path}/privacy-map.md、pm-agent 升级证据及 issue 创建结果。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` workspace 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
