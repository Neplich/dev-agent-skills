# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-004-greenfield-bootstrap-routing`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/idea-to-spec/workspace/iteration-2/eval-4-greenfield-bootstrap-routing`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `47f636262c26b6b99c860d59ef8342eebebbd60397f192a193020f82c13fa42c`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c0da2e0366232678672d0c64ce9fa764d3b78f3caaaa8493348af1a7e1cd00fe`
- Skill overlay SHA-256: `8f09b52303d9393824dd3e732e656dd74f7ac606a082939547181274986dfb2d`
- Judge schema SHA-256: `333e583cf4bb11484925925c3c083e2f295eb8670599a3d04a51d2b749c8668a`
- Eval definition SHA-256: `8e113c060d578c3d672e422d3214efcf8ef5f3dc4a4d591f825ce19450902064`
- Metadata SHA-256: `af73e5b9a9192eb83b6e3ca2d5cae73fe4fd2b14b49ac401fa1a5f606db4bd6c`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | FAIL | with_skill 明确说明工作区为空、无代码或既有文档影响，但未说明技术栈待定。 |
| `pm_first_lane` | PASS | 明确给出 `lane: greenfield-discovery`，表明走 PM-first 新项目需求收敛路径。 |
| `pm_first` | PASS | 未执行脚手架命令；明确先确认 MVP，再写入正式 PRD，并列出 DECISIONS.md。 |
| `assertion_4` | PASS | 明确列出待落地的 PRD.md、DECISIONS.md，并将确认 MVP 作为下一步。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47f636262c26b6b99c860d59ef8342eebebbd60397f192a193020f82c13fa42c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=c2c93c903b0b1e0dd689d8783d42b428cb8752791e0f49b0c145813471b8bc0c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别为空工作区并进入 greenfield-discovery，先收敛 MVP 决策，再落地 PRD/DECISIONS；未发生文件或工程初始化变更。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47f636262c26b6b99c860d59ef8342eebebbd60397f192a193020f82c13fa42c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=483f3f02ea5da52ea26dafbbbfe0b41da18344ef0220f3faa21884d986111eb8; snapshot_sha256=1599c104a33baf84bb6d93c664acf7b9cb50ac98d728f30936fe9657e3a91255
- Behavior: 直接生成并交付 docs/PRD.md，未初始化项目，但未明确采用 greenfield-discovery/PM-first 路径或先确认需求。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- assertion_1 未完整满足：缺少“技术栈待定”的明确说明。
- Next: 在空工作区检测结果中明确写出“技术栈待定”。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
