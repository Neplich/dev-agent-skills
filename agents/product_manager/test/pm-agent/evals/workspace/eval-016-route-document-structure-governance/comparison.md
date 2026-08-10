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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `1cfd412fc44e8e1667cc3feab76a58474b6382f405680057b41b379032f76e0a`
- Skill overlay SHA-256: `8ddfbafd6ae3cf064836ded5fbaa7bcc8a3ab817df212a0b6c4ff355a78b12af`
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
| `routes_to_structure_governance` | PASS | with_skill 的 Routing decision 明确 selected_owner 为 idea-to-spec:structure-governance。 |
| `read_only_audit` | PASS | with_skill 明确声明只读边界，且 git evidence 显示无修改、无提交、无工作树差异。 |
| `report_form` | PASS | 原始工具证据显示 HTML 写入 /tmp/structure-governance.../structure-governance-report.html 并通过非空检查；对话中提供了报告链接和结论摘要。 |
| `scope_six_role_dirs` | PASS | with_skill 的报告和原始证据明确覆盖 docs/pm、docs/engineer、docs/design、docs/qa、docs/devops、docs/security，并记录后四者缺失为扫描限制。 |
| `structural_change_requires_confirmation` | PASS | with_skill 未执行结构变更，并明确要求实际拆分、移动或补齐前先确认，后续按 change_tier: major 进入流程。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78a9ed4a2ff6af194b93c81277958547f5a87533a70b2aa14e43822f139e54d3; fixture_sha256=1a6d7fa4c22a394f3c854eef7a25f4d0cf2e6b4ecd7c7a3d3bf15d295d6e43f8; output_sha256=e014d8d81799e2062f0ed329eb2702a06a9ebaed7a3f3e6379e6800f6ae73df5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确路由至结构治理，完成六角色范围的只读审计，生成运行期 HTML 报告并提供摘要；未执行结构变更。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78a9ed4a2ff6af194b93c81277958547f5a87533a70b2aa14e43822f139e54d3; fixture_sha256=1a6d7fa4c22a394f3c854eef7a25f4d0cf2e6b4ecd7c7a3d3bf15d295d6e43f8; output_sha256=b24055c8f81353917780fdc0569945e9d870c31125623208a95164ff2d19bc88; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了仅覆盖实际存在的 PM/Engineer 两角色的普通文本检查报告，未展示结构治理路由或运行期 HTML 交付。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
