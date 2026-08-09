# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `competitive-brief`
- Eval: `eval-002-battlecard-mode`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `580131b9961f88dece682fec7455c21af018b400a3742eb37ae40114374aeae0` from `agents/product_manager/test/competitive-brief/evals/workspace/eval-002-battlecard-mode`.
- Fixture SHA-256: `580131b9961f88dece682fec7455c21af018b400a3742eb37ae40114374aeae0`
- Prompt SHA-256: `e54579ea27411964e085efe779b45a83156d8efbd3908b273d472904914675a2`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `64a375a1a490fa251e9b252ef3a7787f55ca6a4fd08e5d401228a899b274ed39`
- Skill overlay SHA-256: `c1341cebf983202b3c2101489252c70818305b548c111af4817c833b2dd4164f`
- Judge schema SHA-256: `e42897afb6931d7065c6aa9ac71e607d574f057396cd3a30a0419c210f3be3cb`
- Eval definition SHA-256: `a7454ae2eccc665064a08c31fc99de3b8f0a596f72811f2e5035b12f267e9fe8`
- Metadata SHA-256: `be38b1b419460352b11de0cc1468d57c031f7575d697be3bf617760a456d47f3`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `battlecard_fields` | PASS | with_skill 输出分别为 Linear 和 Jira 两页结构化资料，均包含 Quick Overview、Their Pitch、Strengths、Weaknesses、Objection Handling、Landmines to Set、Landmines to Defuse、Win/Loss Themes。 |
| `no_full_brief` | PASS | 输出采用 battlecard 结构；虽含 Discovery Questions、Talk Track、POC Guidance 等销售使用内容，但没有完整竞品 brief 的执行摘要、messaging gap、机会/威胁等章节。 |
| `evidence_boundary` | PASS | 两家资料均标注 2026-08-06 研究日期和来源，并对定价、我方能力、企业控制、生态等未被材料确认的内容标注“待验证”或要求 POC 验证。 |
| `no_battlecard_offer` | PASS | 输出直接提供两家 battlecard，没有询问是否需要创建 battlecard，也未将其作为后续追加项。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e54579ea27411964e085efe779b45a83156d8efbd3908b273d472904914675a2; fixture_sha256=580131b9961f88dece682fec7455c21af018b400a3742eb37ae40114374aeae0; output_sha256=91cc3517c984d097ca8c48a9df8d46e0fa3f3a70d5ed4d88266f8327ffd18f50; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成 Linear 与 Jira 的结构化销售 battlecard，并明确区分已知信息与待验证内容。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e54579ea27411964e085efe779b45a83156d8efbd3908b273d472904914675a2; fixture_sha256=580131b9961f88dece682fec7455c21af018b400a3742eb37ae40114374aeae0; output_sha256=bafc548537f6e3314bc47a453c9f1d07ee8e528c660a024c18fa423911321659; snapshot_sha256=20d63c8919a61acd0e8c49734612182d7c73e90bfd5486ec4276eb62b7a23631
- Behavior: 提供了两份文件型竞争资料，覆盖部分销售话题并标注待验证，但未展示要求的完整 battlecard 字段结构。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
