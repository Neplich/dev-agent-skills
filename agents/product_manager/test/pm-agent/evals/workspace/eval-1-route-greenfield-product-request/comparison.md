# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-001-route-greenfield-product-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-1-route-greenfield-product-request`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `1cfd412fc44e8e1667cc3feab76a58474b6382f405680057b41b379032f76e0a`
- Skill overlay SHA-256: `8ddfbafd6ae3cf064836ded5fbaa7bcc8a3ab817df212a0b6c4ff355a78b12af`
- Judge schema SHA-256: `8e99b873e976898a8a9714405f69dce2d81e6c553f7d4c2b0a99b8b832eee831`
- Eval definition SHA-256: `4e776e14ac2c8d3f3aa33718b92238355ee2d15eab3267a50cdada6bb3d4a1de`
- Metadata SHA-256: `98a5616a9f22e4ba7d6ed10c98a36b572ccd9f5c0bfcfaf868ea982ef672635f`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `route_to_idea_to_spec` | PASS | with_skill 输出明确 selected_owner 为 pm-agent:idea-to-spec，lane 为 greenfield-discovery，并声明只做产品发现与范围收敛。 |
| `pm_first_guardrail` | PASS | with_skill 识别 project_status: empty，说明是全新产品，并明确 execution_boundary 为暂不写代码。git_evidence 显示无提交、无 diff、无工作区变更。 |
| `context_to_collect` | PASS | with_skill 提出了围绕首要用户与核心场景的高信息量问题，并要求用户从 A/B/C 或自定义描述中选择。 |
| `expected_pm_artifacts` | NOT_EXERCISED | 输出明确 durable_docs_pending 为 PRD/DECISIONS，且 confirmation_required: true；当前仍在等待首个发现问题的回答，未宣称发现完成或进入交接。 |
| `handoff_boundary` | NOT_EXERCISED | 当前仅提出首个产品发现问题，未发生设计或工程 handoff。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=81daf9f1651ef9c63b297497d5d050fce62b0ea3cae43322de19810ec5c5fca7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 准确路由至 PM 的 idea-to-spec/greenfield-discovery，识别空目录与 PM-first 边界，提出首个产品发现问题，未写代码或产出未确认的 PM 文档。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=ae1d073fb77880774c760f7b1dd6cabf97a53c9f8681ec4403192919eb919fd8; snapshot_sha256=aa804066ab6e23e323bfaca3f5c69abd4d27013a76b476a0d2152499e41b06ad
- Behavior: 基础行为也保持未写代码，但直接产出包含大量假设的产品简报和 backlog，再提出多个问题，较早宣称进入产品定义阶段。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 等待用户确认目标用户与核心场景后继续产品发现。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
