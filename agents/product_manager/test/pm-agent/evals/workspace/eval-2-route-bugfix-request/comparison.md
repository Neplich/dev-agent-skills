# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-002-route-bugfix-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-2-route-bugfix-request`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `3622b3dfdb9bef50766ff22e70a5639483865b84fa39f8a64f027bc492debda1`
- Repository HEAD: `8813f864e743f7c83dc2e51e0b5add79f312e870`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0616a11ea39f978cac34906ca01c79a336316825183bb1897d900f056d8544f7`
- Skill overlay SHA-256: `4d4a580c5e7c36b9199abb80221829f90c900c96463581d7f87c6d7ccc538bd7`
- Judge schema SHA-256: `00a01c5f9432a18e723abe9a7b1a555e5a2a41dc2c36a101ed91497434d1c7f4`
- Eval definition SHA-256: `fe6d213ce4edb254dae39c5fefca87002824c8356e6ca05dfa6b8b92c57d378d`
- Metadata SHA-256: `163386e80d321ea48ddfd244853e278bc70ea13a08cdc68ac01f85bf3ba7240f`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `request_type_bug_report` | PASS | with_skill 输出明确包含 `request_type: bug_report`。 |
| `expectation_first` | NOT_EXERCISED | 工作区没有 PRD/TRD 或等价预期文档；候选输出的 `source_documents` 为空，并将补充已批准预期行为列为后续缺口。 |
| `debugger_handoff_after_confirmation` | NOT_EXERCISED | 未提供实际 debugger/Engineer handoff；且因预期文档缺失，入口被标记为 blocked/failed，执行边界禁止工程执行。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3622b3dfdb9bef50766ff22e70a5639483865b84fa39f8a64f027bc492debda1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=692f05e9dcd45ff16e6d292af33d5b58995e552ae7ba4bbf6bc30b03616ea4cc; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别为 bug report，并在缺少项目与预期证据时阻止工程执行。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3622b3dfdb9bef50766ff22e70a5639483865b84fa39f8a64f027bc492debda1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=a4a226af3fc3ee5f66ee6128730b0ff561c0c5c0d8c85f652fa944a1a328720b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 仅识别为空仓库并停止，未进行请求分类或预期确认流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补充项目源码及已批准的 PRD/TRD 或等价产品预期后，再确认实现偏差并决定是否 handoff。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
