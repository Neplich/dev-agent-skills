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
- Fixture SHA-256: `db76812ee462c1a8d89decf8e6fae581930c1406d7c6f72f3847172ed0bb02f3`
- Prompt SHA-256: `520c4aa6ac767af388d73d9adeec0eb6b05a688f692c19decf65da48e498c67e`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `d688e19912770823b0aab741fb33c331e4eee7536315cf3080fbad81ca1e904f`
- Skill overlay SHA-256: `23c53325cfb2472af1f3429b2df2775df9e696783ad43e4708f065dee64c71b7`
- Judge schema SHA-256: `fdb2fd9254bbcae4d1c5e9dd4a0df1a9be1ee48991c72d5d1ea96147641ed710`
- Eval definition SHA-256: `dc1b04424607a1675278b8e310c3f7b0da94f3cf1e857f037b9a6a8dbbf9482f`
- Metadata SHA-256: `2718def12280e05b73752266e8d3b39d6929d0781f7ca1aa2088b55bd4e38e9c`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_repo_wide_docs_handoff` | PASS | with_skill 明确识别 request_type: deployment、feature_path: N/A、全部文档变体目标及完整性证据，并未要求澄清 feature_path。 |
| `routes_dependency_order` | PASS | with_skill 明确列出 deployment-planner -> cicd-bootstrap -> env-config-auditor -> formal-docs-sync 的完整条件式顺序。 |
| `preserves_role_and_authority_boundaries` | PASS | with_skill 明确 DevOps 不修改正式文档，并指出 commit、push、镜像发布和实际部署均未获授权；交付给 Docs 的是已验证事实。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=520c4aa6ac767af388d73d9adeec0eb6b05a688f692c19decf65da48e498c67e; fixture_sha256=db76812ee462c1a8d89decf8e6fae581930c1406d7c6f72f3847172ed0bb02f3; output_sha256=4e1aed0748278587abd4d88c1a2cca0cb6839da7c297446f9c7fee5c8dccb51d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完整接受仓库级 handoff，按依赖顺序路由，并保持文档归属与交付授权边界。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=520c4aa6ac767af388d73d9adeec0eb6b05a688f692c19decf65da48e498c67e; fixture_sha256=db76812ee462c1a8d89decf8e6fae581930c1406d7c6f72f3847172ed0bb02f3; output_sha256=635449d1e01a11da4b427065cc2a442c82fa65b4df874e03195a6596780017a1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 基线也识别了部署范围和依赖，但采用较泛化的阶段规划，未给出技能链路中的明确角色路由。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
