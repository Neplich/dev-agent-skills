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
- Repository HEAD: `e2d0e3e00078c297194828182b4d6445ecbb492d`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c658e8351498435bd5246b692fbf8a3a6d40caa45d6998b37785e6522243068b`
- Skill overlay SHA-256: `6e906e23fd0805526cda111a5e2e74eb02ce2f72534b3e384e90b10a34160090`
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
| `routes_to_structure_governance` | PASS | With_skill output selects `pm-agent:idea-to-spec:structure-governance`; raw trace also records the structure-governance lane and loading of the corresponding governance instructions. |
| `read_only_audit` | PASS | The output states `execution_boundary: 仅审计和报告，不修改仓库文件` and `仓库文档未被修改`; locked git evidence shows unchanged HEAD, branch, status, index, and worktree. |
| `report_form` | PASS | Raw trace records creation of `/tmp/structure-governance.RINm7L/structure-governance-report.html` with verification; the with_skill output provides the runtime HTML path and a findings summary. Locked git evidence shows no repository changes. |
| `scope_six_role_dirs` | PASS | The with_skill routing scope names all six role roots, the audit report lists all six scan roots, and the raw trace command checks each root while explicitly recording the four missing roots as limitations. |
| `structural_change_requires_confirmation` | PASS | No structural mutation or merge/split/move execution occurred. The output recommends no structural action, while the report’s later constraints require user confirmation and `change_tier: major` for any approved future structural implementation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78a9ed4a2ff6af194b93c81277958547f5a87533a70b2aa14e43822f139e54d3; fixture_sha256=1a6d7fa4c22a394f3c854eef7a25f4d0cf2e6b4ecd7c7a3d3bf15d295d6e43f8; output_sha256=64c5232c4223e4afe67acd1feecf80a29fac96393467a2cbbb0ae05cc2256468; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routed the request to structure governance, performed a read-only six-role audit, produced the runtime HTML report path and summary, and preserved the repository.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78a9ed4a2ff6af194b93c81277958547f5a87533a70b2aa14e43822f139e54d3; fixture_sha256=1a6d7fa4c22a394f3c854eef7a25f4d0cf2e6b4ecd7c7a3d3bf15d295d6e43f8; output_sha256=77d2db87eedd2175280ef30829fee7878becb2951fc467eb7163db405e43acc1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline produced a basic two-role Markdown summary, omitted the required HTML runtime report and six-role governance routing/coverage.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
