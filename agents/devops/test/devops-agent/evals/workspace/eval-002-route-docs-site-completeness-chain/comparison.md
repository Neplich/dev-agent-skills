# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `devops-agent`
- Eval: `eval-002-route-docs-site-completeness-chain`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `db76812ee462c1a8d89decf8e6fae581930c1406d7c6f72f3847172ed0bb02f3` from `agents/devops/test/devops-agent/evals/workspace/eval-002-route-docs-site-completeness-chain`.
- Identity schema: `2`
- target_skill_sha256: `a1710c0451d41ab9797a4d66831dae37e5e82aa02c99f954ebc420b99e5a6387`
- eval_definition_sha256: `dc1b04424607a1675278b8e310c3f7b0da94f3cf1e857f037b9a6a8dbbf9482f`
- metadata_sha256: `2718def12280e05b73752266e8d3b39d6929d0781f7ca1aa2088b55bd4e38e9c`
- fixture_sha256: `db76812ee462c1a8d89decf8e6fae581930c1406d7c6f72f3847172ed0bb02f3`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `fdb2fd9254bbcae4d1c5e9dd4a0df1a9be1ee48991c72d5d1ea96147641ed710`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `520c4aa6ac767af388d73d9adeec0eb6b05a688f692c19decf65da48e498c67e`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `572a307aa700b74953743167f8c07df7db2ec9749bc028dad049129faf61f032`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_repo_wide_docs_handoff` | PASS | with_skill 明确接受 request_type: deployment、feature_path/feature/parent_feature/feature_level 为 N/A，并将范围识别为全部文档站变体；未退回 feature_path 澄清。 |
| `routes_dependency_order` | PASS | with_skill 明确给出 deployment-planner → cicd-bootstrap → env-config-auditor → docs-agent:formal-docs-sync 顺序，并要求最终 Docs 步骤只消费前三阶段已落地且验证的事实。 |
| `preserves_role_and_authority_boundaries` | PASS | with_skill 明确 DevOps 不修改正式文档，并声明 handoff 不预授权 commit、push、镜像发布或部署；最终同步仅使用已验证运维事实。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=520c4aa6ac767af388d73d9adeec0eb6b05a688f692c19decf65da48e498c67e; fixture_sha256=db76812ee462c1a8d89decf8e6fae581930c1406d7c6f72f3847172ed0bb02f3; output_sha256=a2495b65cc18af240d04271a2a3453071fb09f90e028b55a1e9476140d7d5a4c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确接受 repo-wide deployment handoff，保持完整依赖链路，并保留文档职责与交付授权边界；未发生仓库变更。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=520c4aa6ac767af388d73d9adeec0eb6b05a688f692c19decf65da48e498c67e; fixture_sha256=db76812ee462c1a8d89decf8e6fae581930c1406d7c6f72f3847172ed0bb02f3; output_sha256=5a91fff467039dd98742a5e05bacd46d77145dfb210bad075251052a186cae30; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了较宽泛的阶段式部署建议和事实回交清单，但未明确要求的技能级依赖链路。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
