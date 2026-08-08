# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `authz-reviewer`
- Eval: `eval-004-mapped-report-export-authz`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1673a8537015ccb78dccaef03358a444dd29e08496bc7a169f640fd43e0d756f` from `agents/security/test/authz-reviewer/evals/workspace/eval-004-mapped-report-export-authz`.
- Fixture SHA-256: `1673a8537015ccb78dccaef03358a444dd29e08496bc7a169f640fd43e0d756f`
- Prompt SHA-256: `37500482cb4ba2d8e25d4d03e2971e18b8768e627b3eb196fe101c177681427a`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5d96dce7dbfccf9a7b2e510ce571be9b1aa80472fabf9a5779117cb4e21d3b09`
- Skill overlay SHA-256: `89401c75c36dd79dd8bf55d1b0c23cbd794402b7f29f62d05ae9f27f5e25c3f9`
- Judge schema SHA-256: `fe1f59786edfa4e3b7ee12601522d693ef12a42cdfce9b4a390ad6d7b95d03d2`
- Eval definition SHA-256: `5b176c277f514c5c57cbc50df739c8bd53714adf02a29d091d0507fdcbd6bda5`
- Metadata SHA-256: `e90a93e1c6fa00dac24590e3594c181ac3d2710839dea31ce1c1f4375ebfd014`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 锁定原始证据只能确认 change-map 将该代码映射到 required_docs；无法证明候选实际遵循了“优先读取”的隐藏读取顺序。 |
| `verifies_against_code` | FAIL | 候选没有回到代码给出 analyst 实际可导出及其越权风险的结论，而是停止在等待交接信息。代码原始证据明确显示 admin 和 analyst 均可导出。 |
| `treats_unverified_as_low_trust` | PASS | 候选明确识别两份文档为 unverified、将其视为低信任且不单独据此下结论；但因交接信息缺失，后续代码核证尚未完成。 |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | 候选未形成改变正式文档事实的最终结论，因此触发 PM 分类并创建 issue 的条件尚未发生。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=37500482cb4ba2d8e25d4d03e2971e18b8768e627b3eb196fe101c177681427a; fixture_sha256=1673a8537015ccb78dccaef03358a444dd29e08496bc7a169f640fd43e0d756f; output_sha256=2fcbf7fd25ebc7bcd724d05ebd47d2aeaf9381d4a01ece66d37906e73b5010a1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确定位 change-map、required_docs 并降低 unverified 文档信任，但在交接信息缺失时停止，未完成核心代码授权审查。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=37500482cb4ba2d8e25d4d03e2971e18b8768e627b3eb196fe101c177681427a; fixture_sha256=1673a8537015ccb78dccaef03358a444dd29e08496bc7a169f640fd43e0d756f; output_sha256=cf1efe39d48e6fa8dc7ba5dc6ca082a7ca7192afc4df96095eb08cb80259923a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成了代码与文档对照，正确识别 admin/analyst 均可导出及文档不一致导致的越权风险，但未体现低信任文档处理和升级流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未提供代码核对后的实际可导出角色和越权风险结论。
- Next: 补齐或确认 PM/Security handoff packet 与 feature_path。
- Next: 回到 report-export-policy.js 核实授权结论，并在结论改变正式文档事实时交回 pm-agent 分类并创建 issue。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `authz-reviewer`
- Eval: `eval-004-mapped-report-export-authz`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1673a8537015ccb78dccaef03358a444dd29e08496bc7a169f640fd43e0d756f` from `agents/security/test/authz-reviewer/evals/workspace/eval-004-mapped-report-export-authz`.
- Fixture SHA-256: `1673a8537015ccb78dccaef03358a444dd29e08496bc7a169f640fd43e0d756f`
- Prompt SHA-256: `37500482cb4ba2d8e25d4d03e2971e18b8768e627b3eb196fe101c177681427a`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5d96dce7dbfccf9a7b2e510ce571be9b1aa80472fabf9a5779117cb4e21d3b09`
- Skill overlay SHA-256: `89401c75c36dd79dd8bf55d1b0c23cbd794402b7f29f62d05ae9f27f5e25c3f9`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `5b176c277f514c5c57cbc50df739c8bd53714adf02a29d091d0507fdcbd6bda5`
- Metadata SHA-256: `e90a93e1c6fa00dac24590e3594c181ac3d2710839dea31ce1c1f4375ebfd014`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | with_skill 正确要求先补充 PM/Security 交接上下文；因此尚未执行 change-map 或文档读取。 |
| `verifies_against_code` | NOT_EXERCISED | 尚未进入代码与授权结论核对步骤。 |
| `treats_unverified_as_low_trust` | NOT_EXERCISED | 尚未读取 required_docs 或核验其版本状态。 |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | 尚未形成改变正式文档事实的结论，因此升级与创建 issue 的后续步骤尚未发生。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=37500482cb4ba2d8e25d4d03e2971e18b8768e627b3eb196fe101c177681427a; fixture_sha256=1673a8537015ccb78dccaef03358a444dd29e08496bc7a169f640fd43e0d756f; output_sha256=ac3a7dce026b4e0286c360ab28c57034f7c073442b0f7b0ff94b81284bf357c9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别缺少必需交接上下文，正确暂停审查并要求先由 pm-agent 完成交接；后续审查步骤未执行。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=37500482cb4ba2d8e25d4d03e2971e18b8768e627b3eb196fe101c177681427a; fixture_sha256=1673a8537015ccb78dccaef03358a444dd29e08496bc7a169f640fd43e0d756f; output_sha256=2a53fb9d6b18b202c56761e09f54b46cee3b2afc98146f738bc791a51cb6cd72; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成了文档、change-map 与代码的授权核对，并识别 analyst 的越权风险，但未体现 unverified 文档信任处理或按要求升级。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 提供所要求的 PM/Security 交接包后，继续按 change-map、正式说明、代码与测试证据完成审查。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `authz-reviewer`
- Eval: `eval-004-mapped-report-export-authz`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1673a8537015ccb78dccaef03358a444dd29e08496bc7a169f640fd43e0d756f` from `agents/security/test/authz-reviewer/evals/workspace/eval-004-mapped-report-export-authz`.
- Fixture SHA-256: `1673a8537015ccb78dccaef03358a444dd29e08496bc7a169f640fd43e0d756f`
- Prompt SHA-256: `37500482cb4ba2d8e25d4d03e2971e18b8768e627b3eb196fe101c177681427a`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `3e242b2dbb704cb1d29797b016c5227b3a75736fa3d4f0739192f0fdee71f01f`
- Skill overlay SHA-256: `3de2c418f3c14f33d91cbef534093000d696ba99512436f5551d86e45d872cc9`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `5b176c277f514c5c57cbc50df739c8bd53714adf02a29d091d0507fdcbd6bda5`
- Metadata SHA-256: `e90a93e1c6fa00dac24590e3594c181ac3d2710839dea31ce1c1f4375ebfd014`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 候选输出确认命中 change-map 并定位 required_docs，但锁定证据无法证明实际读取顺序或未遍历无关文档。 |
| `verifies_against_code` | PASS | 明确指出文档声称仅 admin 可导出，而代码允许 admin 和 analyst，并据此评估 analyst 可能越权。 |
| `treats_unverified_as_low_trust` | FAIL | 未提及 required_docs 文档的 last_verified_version 为 unverified；虽回到代码核对，但遗漏了该关键信任状态。 |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | 候选正确执行了缺少 PM/Security 交接包时先退回 pm-agent 分类的下一步；创建 issue 和产出正式报告仍需缺失的确认或运行时证据。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=37500482cb4ba2d8e25d4d03e2971e18b8768e627b3eb196fe101c177681427a; fixture_sha256=1673a8537015ccb78dccaef03358a444dd29e08496bc7a169f640fd43e0d756f; output_sha256=65394fbec37f3a0ebefb8c42c9123e16e84222cfd9c0625c029b04e7603be435; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确定位映射、读取相关授权说明并回到代码核验，谨慎将 analyst 标为可能越权并等待 PM 确认；遗漏 unverified 信任状态。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=37500482cb4ba2d8e25d4d03e2971e18b8768e627b3eb196fe101c177681427a; fixture_sha256=1673a8537015ccb78dccaef03358a444dd29e08496bc7a169f640fd43e0d756f; output_sha256=d6b4db494b35328cc85add2b128af8489be136b9a803cb1606704a64026828eb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别代码与文档不一致及潜在越权，但建议直接修改代码，未体现 PM 分类升级门禁。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未识别 required_docs 的 last_verified_version 为 unverified。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `authz-reviewer`
- Eval: `eval-004-mapped-report-export-authz`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1673a8537015ccb78dccaef03358a444dd29e08496bc7a169f640fd43e0d756f` from `agents/security/test/authz-reviewer/evals/workspace/eval-004-mapped-report-export-authz`.
- Fixture SHA-256: `1673a8537015ccb78dccaef03358a444dd29e08496bc7a169f640fd43e0d756f`
- Prompt SHA-256: `37500482cb4ba2d8e25d4d03e2971e18b8768e627b3eb196fe101c177681427a`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `3e242b2dbb704cb1d29797b016c5227b3a75736fa3d4f0739192f0fdee71f01f`
- Skill overlay SHA-256: `3de2c418f3c14f33d91cbef534093000d696ba99512436f5551d86e45d872cc9`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `5b176c277f514c5c57cbc50df739c8bd53714adf02a29d091d0507fdcbd6bda5`
- Metadata SHA-256: `e90a93e1c6fa00dac24590e3594c181ac3d2710839dea31ce1c1f4375ebfd014`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 输出提到变更映射和命中文档，但锁定原始证据无法证明读取顺序或未遍历无关文档。 |
| `verifies_against_code` | PASS | 明确核对了 report-export-policy.js，识别 admin 与 analyst 均可导出，并据此判断与文档不一致及越权风险。 |
| `treats_unverified_as_low_trust` | FAIL | 未识别 required_docs 的 last_verified_version 为 unverified，也未明确说明因此扩大代码核证；虽引用了代码事实，但遗漏了该要求。 |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | 输出未呈现 pm-agent 分类、issue 创建或 Security 过程报告；锁定证据也没有交付或运行时证据可据此判定。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=37500482cb4ba2d8e25d4d03e2971e18b8768e627b3eb196fe101c177681427a; fixture_sha256=1673a8537015ccb78dccaef03358a444dd29e08496bc7a169f640fd43e0d756f; output_sha256=d452dcc296a20e6a5527a5b1ef3c2194c657545da5bde44293e17308a5db9b43; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确核对文档与代码并识别 analyst 越权风险；遗漏 unverified 元数据处理，升级流程未被证据练习。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=37500482cb4ba2d8e25d4d03e2971e18b8768e627b3eb196fe101c177681427a; fixture_sha256=1673a8537015ccb78dccaef03358a444dd29e08496bc7a169f640fd43e0d756f; output_sha256=53478c0be57a908a725e67b59655e5cd9f9e9008d00d1343acbbb89d93a80b47; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别代码允许 analyst 导出并判断存在越权风险，但同样未呈现 unverified 信任处理或升级动作。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未识别 required_docs 的 last_verified_version 为 unverified，也未说明按最低信任处理并扩大代码核证。
- Next: 补充明确说明 required_docs 为 unverified，并说明授权结论以代码核证为准。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `authz-reviewer`
- Eval: `eval-004-mapped-report-export-authz`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1673a8537015ccb78dccaef03358a444dd29e08496bc7a169f640fd43e0d756f` from `agents/security/test/authz-reviewer/evals/workspace/eval-004-mapped-report-export-authz`.
- Fixture SHA-256: `1673a8537015ccb78dccaef03358a444dd29e08496bc7a169f640fd43e0d756f`
- Prompt SHA-256: `37500482cb4ba2d8e25d4d03e2971e18b8768e627b3eb196fe101c177681427a`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0fb3bcf4b507247f482a2a4dba9d951bb407cd66a7a7b7801270374734e4b29d`
- Skill overlay SHA-256: `a5058c0e55b69c8360ce0ae93f04438f76cd73a75566cfde030e7cc6ed7b7266`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `5b176c277f514c5c57cbc50df739c8bd53714adf02a29d091d0507fdcbd6bda5`
- Metadata SHA-256: `e90a93e1c6fa00dac24590e3594c181ac3d2710839dea31ce1c1f4375ebfd014`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | With-skill output cites the change map and the mapped report-export document, with no unrelated formal documents used. |
| `verifies_against_code` | PASS | It cites report-export-policy.js, identifies that both admin and analyst satisfy the code condition, contrasts this with the admin-only document, and assesses analyst access as an authorization bypass. |
| `treats_unverified_as_low_trust` | FAIL | The output does not identify last_verified_version: unverified or explicitly apply a lowest-trust treatment to the document; the code check is present but the required unverified-status reasoning is absent. |
| `escalates_fact_changing_conclusion_to_pm` | FAIL | The output recommends changing the implementation but does not return the fact-changing conclusion and evidence to pm-agent, create an issue through pm-agent, or produce a Security process report. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=37500482cb4ba2d8e25d4d03e2971e18b8768e627b3eb196fe101c177681427a; fixture_sha256=1673a8537015ccb78dccaef03358a444dd29e08496bc7a169f640fd43e0d756f; output_sha256=b9eb1bf57bed709de4a17f94985398e7dfd1c9b88f30332aa98a1e820e0d7d68; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly used the mapped documentation and code to identify analyst over-permission and qualification around the missing download call site, but omitted explicit unverified-trust handling and pm-agent escalation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=37500482cb4ba2d8e25d4d03e2971e18b8768e627b3eb196fe101c177681427a; fixture_sha256=1673a8537015ccb78dccaef03358a444dd29e08496bc7a169f640fd43e0d756f; output_sha256=49eba0241db7a012b4a0bbffa5b94546dd3a64696b653b1de3cb6ee99d2e9c22; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identified the code/document authorization mismatch and risk, but did not demonstrate mapped-document-first review, unverified-document handling, or required pm-agent escalation.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output omits explicit handling of the mapped documents' unverified verification status.
- The with_skill output omits the mandatory pm-agent classification and issue-creation escalation for a conclusion that changes formal documentation facts.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `authz-reviewer`
- Eval: `eval-004-mapped-report-export-authz`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1673a8537015ccb78dccaef03358a444dd29e08496bc7a169f640fd43e0d756f` from `agents/security/test/authz-reviewer/evals/workspace/eval-004-mapped-report-export-authz`.
- Fixture SHA-256: `1673a8537015ccb78dccaef03358a444dd29e08496bc7a169f640fd43e0d756f`
- Prompt SHA-256: `37500482cb4ba2d8e25d4d03e2971e18b8768e627b3eb196fe101c177681427a`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `d2e4aec7daf8a1a3d4dd9129eb3c1a3dff6fda1cedda3583e17db51f3c77b01c`
- Skill overlay SHA-256: `93997287763bb5908bc9735f09115a4d8477c3badf934fbe6f43970bb3ecd156`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `5b176c277f514c5c57cbc50df739c8bd53714adf02a29d091d0507fdcbd6bda5`
- Metadata SHA-256: `e90a93e1c6fa00dac24590e3594c181ac3d2710839dea31ce1c1f4375ebfd014`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill 明确指出变更映射要求审查 docs/site/api/report-export.md，并引用该文档与代码；未显示遍历无关正式文档。 |
| `verifies_against_code` | PASS | with_skill 回到 report-export-policy.js，准确识别 admin 和 analyst 均可导出，并据此指出与文档不一致及越权风险。 |
| `treats_unverified_as_low_trust` | PASS | with_skill 识别并引用 change-map 中的 last_verified_version: unverified，同时以代码事实核验授权结论，而非直接采信或拒绝读取文档。 |
| `escalates_fact_changing_conclusion_to_pm` | FAIL | with_skill 识别了正式文档与代码事实不一致，但未要求将结论和证据回交 pm-agent 分类并创建 issue，也未产出 Security 自有过程报告作为升级证据。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=37500482cb4ba2d8e25d4d03e2971e18b8768e627b3eb196fe101c177681427a; fixture_sha256=1673a8537015ccb78dccaef03358a444dd29e08496bc7a169f640fd43e0d756f; output_sha256=d327c8e0954f9247a981b52b483efa9b6471c96695ef06a743dc8a7176bf8c67; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 准确完成文档与代码核对，识别 unverified 和越权风险；遗漏改变正式文档事实后的 pm-agent 分类、issue 创建及升级证据要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=37500482cb4ba2d8e25d4d03e2971e18b8768e627b3eb196fe101c177681427a; fixture_sha256=1673a8537015ccb78dccaef03358a444dd29e08496bc7a169f640fd43e0d756f; output_sha256=d1aa911055eb28c91e3393d9408daaed743d425c5ff57cc2f246576a0bd26477; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 准确识别 analyst 的实际导出权限及文档不一致，也识别 unverified；但未体现从 change-map 优先读取的过程或规定的 pm-agent 升级路径。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足 escalates_fact_changing_conclusion_to_pm：缺少 pm-agent 分类、issue 创建及必要的 Security 过程报告。
- Next: 补充将结论与证据回交 pm-agent 分类并创建 issue 的升级步骤，并明确不交给 docs-agent 或由 Security 自行创建 issue。

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

# Eval Result: eval-004-mapped-report-export-authz

## Evaluation Target

- Agent: `security`
- Skill: `authz-reviewer`
- Eval: `eval-004-mapped-report-export-authz`
- Test case: Mapped Report Export Authorization
- Workspace: `workspace/eval-004-mapped-report-export-authz`
- Natural user prompt:

> 请审查 src/access/report-export-policy.js 的报表导出授权逻辑，说明哪些角色可以导出以及是否存在越权风险。

- Expected artifact: 优先读取 change-map 命中的报表导出文档，再以代码核对角色权限；将 unverified 文档按最低信任处理并报告管理员专属声明与 analyst 可导出事实的不一致。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/authz-reviewer--eval-004-mapped-report-export-authz/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `9639cce1288a627343633a3f6f1cd38e62beaa58df89ae4e8eb5100e906b8a7f`。
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
| `reads_mapped_docs_first`<br>命中 change-map 后优先读取报表导出 required_docs | FAIL | transcript 先读取目标代码并进行广泛搜索，之后才读取 change-map 和命中文档，未按 change-map 反查后优先读取 required_docs。 | FAIL | transcript 先读取代码并进行全局搜索，之后才读取 change-map 和 required_docs。 |
| `verifies_against_code`<br>以授权策略代码核对可导出角色 | PASS | transcript 和 candidate 明确引用 report-export-policy.js:2，确认 admin 与 analyst 均可导出，并指出与文档仅允许 admin 的冲突。 | PASS | candidate 和 transcript 均明确核对代码，正确识别 admin、analyst 均被放行及其与文档的不一致。 |
| `treats_unverified_as_low_trust`<br>将 unverified 授权文档按最低信任处理 | PASS | transcript 读取到 change-map 与 required_docs 的 last_verified_version 为 unverified，且授权结论回到代码事实核验，没有拒绝读取或直接采信文档。 | PASS | transcript 读取并显示 unverified 元数据，同时以代码结论为主进行判断；虽未明确阐述信任等级，但未直接依赖文档替代代码核验。 |
| `escalates_fact_changing_conclusion_to_pm`<br>改变正式文档事实的结论升级 | FAIL | 已确认代码改变正式文档事实，但 candidate 未回交 pm-agent、未创建 issue 分类交接，最终工作区也没有 docs/security 过程报告或其他升级产物。 | FAIL | 同样识别了代码与正式文档冲突，但没有 PM 交接、issue 或 Security 过程报告产物。 |

## With-Skill Behavior

代码核验和文档不一致识别正确，但未遵守 change-map 优先读取顺序，也未完成 PM 升级、创建 Security 过程报告及 issue 分类交接。

## Fresh Without-Skill Baseline

独立 baseline 正确识别 admin/analyst 均可导出及文档冲突，但同样未完成映射优先顺序和升级产物。

## Failures

- with-skill 未按 change-map 优先读取命中文档。
- with-skill 未按契约将改变正式文档事实的结论升级至 pm-agent，也未创建要求的报告/issue 交接产物。

## Not Exercised

- 无。

## Next Steps

- 补充按 change-map 顺序执行的审查证据。
- 在最终工作区创建 Security 自有过程报告，并将文档事实冲突回交 pm-agent 分类及创建 issue。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` workspace 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
