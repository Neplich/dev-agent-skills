# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-016-route-document-structure-governance`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1a6d7fa4c22a394f3c854eef7a25f4d0cf2e6b4ecd7c7a3d3bf15d295d6e43f8` from `agents/product_manager/test/pm-agent/evals/workspace/eval-016-route-document-structure-governance`.
- Fixture SHA-256: `1a6d7fa4c22a394f3c854eef7a25f4d0cf2e6b4ecd7c7a3d3bf15d295d6e43f8`
- Prompt SHA-256: `78a9ed4a2ff6af194b93c81277958547f5a87533a70b2aa14e43822f139e54d3`
- Repository HEAD: `d96f213470acb77cb92c1af637626260d3e55b45`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c978d115fb1b50ceb3f80a0d77c450574e05667bd8252ef5b6e8b67105206fa2`
- Skill overlay SHA-256: `5b89d6a3c235a107cde8314b908b32dbfa76d6dc330906b48f74091d88e9019d`
- Judge schema SHA-256: `c8400122a967de4e5b8b409bbe920fe16ec946724a3aa7d4b3077b3582a3f2f0`
- Eval definition SHA-256: `ba37454a106688e9f5f2e2586231a60f2093e364612eb14bfa53540c9e2d1589`
- Metadata SHA-256: `fe53b448dd4fd2693ceb179d875dd617b7b717601fc7d9d3214cab940b4cdef7`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_to_structure_governance` | PASS | with_skill 输出明确将 selected_owner 设为 idea-to-spec:structure-governance。 |
| `read_only_audit` | PASS | 输出声明“只读审计”、execution_boundary 为未修改仓库，并有 git 无变更证据。 |
| `report_form` | PASS | 输出提供运行期 /tmp HTML 报告路径；git evidence 显示未提交或产生 git 变更，并在对话中给出摘要。 |
| `scope_six_role_dirs` | PASS | 输出及 HTML 报告明确扫描 docs/pm、engineer、design、qa、devops、security，并将缺失目录记录为限制。 |
| `structural_change_requires_confirmation` | PASS | 输出明确不执行移动、拆分或补建；报告中的后续约束要求获批结构实施使用 change_tier: major。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78a9ed4a2ff6af194b93c81277958547f5a87533a70b2aa14e43822f139e54d3; fixture_sha256=1a6d7fa4c22a394f3c854eef7a25f4d0cf2e6b4ecd7c7a3d3bf15d295d6e43f8; output_sha256=a6c04804faa2b2272a99f72fe962bf0871b93492c3e6320d552d0b990fd75a57; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确路由到结构治理，执行只读六角色目录审计，生成运行期 HTML 报告并避免结构变更。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78a9ed4a2ff6af194b93c81277958547f5a87533a70b2aa14e43822f139e54d3; fixture_sha256=1a6d7fa4c22a394f3c854eef7a25f4d0cf2e6b4ecd7c7a3d3bf15d295d6e43f8; output_sha256=85262a89377939958ed8f3e91d11aaeee368c5055aec0fc1904e0f674aeda049; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 仅检查 PM 和 Engineer，遗漏四个角色目录及治理路由、HTML 报告和变更边界要求。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
