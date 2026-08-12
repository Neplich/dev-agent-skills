# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-003-route-test-writing-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-3-route-test-writing-request`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `3f7994fdecfb94451400a56972388597b7ae51d2d37508524058139c5273a4e3`
- Repository HEAD: `33a503192c752d6227de1bc0d8d8a2e78e31cdf5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8b87fb93cdb85ecb0436a61b1aedfcf9c8b41c4cd8f9eff41c412a3196c1d245`
- Skill overlay SHA-256: `56390e18f057b654978938889dac7daf0263eaaf39d741419b573d12bff2c198`
- Judge schema SHA-256: `4bea92cb3e04f7ad6bcf4e0dcdb3aa7c06af7bec325a6bea731363f44bd4e944`
- Eval definition SHA-256: `4c0ee7c09752627d6057c1ccc0d45cb292b19c1428b51ca9513725150029cf5a`
- Metadata SHA-256: `48e1e31078cfd6a23e5c1bdb5481d8f4c6428eb757f9b42750f6377a78297239`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `request_type_validation` | PASS | with_skill 明确将请求分类为 `request_type: validation`。 |
| `test_basis_first` | NOT_EXERCISED | 工作区缺少 PRD、TRD、实现和验收记录；with_skill 明确将 `source_documents` 置空并要求补齐测试依据，因此该后续步骤未被执行。 |
| `qa_or_test_writer_handoff` | NOT_EXERCISED | 由于测试依据和预期行为均缺失，with_skill 将入口标记为 blocked，并拒绝下游 QA 交接；该步骤尚无法执行。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3f7994fdecfb94451400a56972388597b7ae51d2d37508524058139c5273a4e3; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=9a9aca1b3438b98f7317114d77202a071b076a16d0136918aef95214cab81c32; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确完成 validation 分类，识别测试依据缺失并阻止未经依据的测试规划、实现和 QA 交接。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3f7994fdecfb94451400a56972388597b7ae51d2d37508524058139c5273a4e3; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=6221d665bbc354152a42aab4a24a7ab2f98488dd8b62f4f6018cd86792804f95; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 仅报告空仓库并请求补充项目代码，未进行请求类型分类或测试依据/交接路由。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 提供订单退款源码、测试目录及批准的 PRD、TRD 或既有验收记录。
- Next: 补齐并确认稳定预期后，再交接 QA 或 test-writer。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
