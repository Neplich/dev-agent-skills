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
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
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
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
