# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `regression-suite`
- Eval: `eval-001-verify-bug-fix`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308` from `agents/qa/test/regression-suite/evals/workspace/eval-1-verify-bug-fix`.
- Fixture SHA-256: `de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308`
- Prompt SHA-256: `c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4e9403c0e6549024a79156a156c1294488d1a418598e88e3e9565298bc6bae6a`
- Skill overlay SHA-256: `1cec710f9ba01d04ab324671796616b09b6a6eae6465b286be839bfcc2fe92d7`
- Judge schema SHA-256: `2c18050b9a27d5dccf92b0604097b9078533d47105266364099eafbf3833aad8`
- Eval definition SHA-256: `8ca6ea4c46c7a5a2c854d9ff5def7ea0ec612ddbf9888a829e50de270f1b84c4`
- Metadata SHA-256: `732278c998a10f6e6333dc13e2fc4edfbaed96da1abb806d2dc29682a3a79f75`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill 先读取 BUG-001、PR-001，并据复现步骤、期望行为和共享序列化风险界定范围。 |
| `qa` | PASS | delivery_snapshot 记录 TEST_SUITE、FLOW_INDEX、case、script 及历史 results/_reports 均已读取或确认缺失；raw trace 也显示了对应读取命令。 |
| `assertion_3` | NOT_EXERCISED | 结果文件明确记录 original failure recheck、fixed behavior 和 verification status 为 blocked/not executed；实际运行因缺少 package.json 未能完成。 |
| `assertion_4` | PASS | 报告将场景标为 feature-update，并限定原始登录、直接影响路径及 invalid-credential、locked-account 相邻路径，未扩展为 release 全量回归。 |
| `alignment_version_archive` | PASS | 结果文件包含同路径 PRD/TRD/IMPLEMENTATION_PLAN 对齐门禁、已确认平台版本 v1.2.0-fix.1，并新增对应 result.md 与 testcase.snapshot.md，未覆盖历史结果。 |
| `assertion_5` | PASS | 结果文件和快照均包含 blocked run status、low evidence confidence 及 needs more verification release recommendation，未宣称可发布。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0; fixture_sha256=de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308; output_sha256=bbfd86a927f86bc8adad65be06949095fd06eea8116b79e92d5ba2287298035c; snapshot_sha256=4b60526dd8f8d32d5835f9cbf96e9e5405398adc4d9c9e4e477fb75446207d6f
- Behavior: 完成证据预检、对齐门禁、定向范围定义和可追溯阻塞归档；未虚构运行通过。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0; fixture_sha256=de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308; output_sha256=4f71f8506c8127b6a51a9a17380c934ee04efca4178d30f32d535a6d05e71dbb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别到运行环境缺失并给出阻塞结论，但未生成持久化回归归档或完整门禁记录。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 提供可运行的修复构建或恢复测试 harness 后，重跑原始登录、invalid-credential 和 locked-account 路径。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
