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
- Identity schema: `2`
- target_skill_sha256: `51c78b43ef29524223ad8cd1c217695feb08d840a69aa6efc0357d489d9b1808`
- eval_definition_sha256: `a7454ae2eccc665064a08c31fc99de3b8f0a596f72811f2e5035b12f267e9fe8`
- metadata_sha256: `be38b1b419460352b11de0cc1468d57c031f7575d697be3bf617760a456d47f3`
- fixture_sha256: `580131b9961f88dece682fec7455c21af018b400a3742eb37ae40114374aeae0`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `e42897afb6931d7065c6aa9ac71e607d574f057396cd3a30a0419c210f3be3cb`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `e54579ea27411964e085efe779b45a83156d8efbd3908b273d472904914675a2`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `7c8d16fe8d7e0a5fcf1eddfd898ed6359958f6d99fba9afbff4d4be1085a6bfd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `battlecard_fields` | PASS | With_skill 输出分别覆盖 Linear 与 Jira 的 Quick Overview、Their Pitch、Strengths、Weaknesses、Objection Handling、Landmines to Set、Landmines to Defuse、Win/Loss Themes，且包含目标客户、定价模型摘要和近期动态。 |
| `no_full_brief` | PASS | With_skill 输出保持为两份销售 battlecard，附加的 Our Position、Discovery Questions、Talk Track、POC Guidance 属于销售使用内容，未形成完整竞品 brief 的执行摘要、竞品画像全节、messaging gap 或机会/威胁/行动项章节。 |
| `evidence_boundary` | PASS | With_skill 明确标注研究日期 2026-08-06、来源记录链接，并将具体价格、企业控制、安全问卷、迁移成本等未确认内容标为“待验证”或“假设”，且未作确定性量化结论。 |
| `no_battlecard_offer` | PASS | With_skill 输出直接交付 battlecard 内容，没有询问是否需要创建 battlecard，也没有将其作为后续追加项。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e54579ea27411964e085efe779b45a83156d8efbd3908b273d472904914675a2; fixture_sha256=580131b9961f88dece682fec7455c21af018b400a3742eb37ae40114374aeae0; output_sha256=ce7666f6da33e9b0e7e3db023f520c8515f37b3d27392e960db38d9748a2f4ef; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成 Linear 与 Jira 两份结构完整、证据边界清晰的销售 battlecard。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e54579ea27411964e085efe779b45a83156d8efbd3908b273d472904914675a2; fixture_sha256=580131b9961f88dece682fec7455c21af018b400a3742eb37ae40114374aeae0; output_sha256=1daa68dfedc054bfc67a7a1f45b3ed3d583ba31609059d4d8792c9ba862e0beb; snapshot_sha256=c0ddb1c0d8c80fe01d39ef6b8df68cb1c865c83440969e8e0c42fd57bb3796db
- Behavior: 完成两份销售一页资料并标注假设/待验证，但呈现为较泛化的销售资料，未在最终输出中展示完整 battlecard 字段结构。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
