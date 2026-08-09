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
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
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
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
