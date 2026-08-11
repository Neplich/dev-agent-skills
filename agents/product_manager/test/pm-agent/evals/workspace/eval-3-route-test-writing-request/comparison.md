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
- Repository HEAD: `b385df5d17058a52081357c8a8480fc146c3d989`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ecf67dca8a2fd53bb0dd6d0a63750ba2716e88dc4af4f77176ea061260d64286`
- Skill overlay SHA-256: `2ed9fef9a54be8009ea156c857682ad7dd82c0e56e3463d3257fe74fe9c977ec`
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
| `request_type_validation` | PASS | with_skill 输出明确将 request_type 标为 validation，并将工作归类为验收覆盖/测试验证路径。 |
| `test_basis_first` | NOT_EXERCISED | with_skill 明确检查并记录 source_documents 为空、entry_basis 为 missing，指出缺少 PRD/TRD/验收基线并要求先补充；但原始证据中没有实际可确认的测试依据文件，因此该断言未完成执行。 |
| `qa_or_test_writer_handoff` | NOT_EXERCISED | with_skill 明确禁止在预期行为未确认前编写测试或继续下游执行，并将 PM 收集基线作为 next_action；由于预期尚未稳定，QA/Engineer/test-writer handoff 尚未发生。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3f7994fdecfb94451400a56972388597b7ae51d2d37508524058139c5273a4e3; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=5b2fe9b5bbcd053290c7a425d5e3712541bfada051ff4cd9f22d49e80749b15d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别为 validation，检查到测试依据缺失后安全阻断测试编写，并要求先收集异常行为与验收基线。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3f7994fdecfb94451400a56972388597b7ae51d2d37508524058139c5273a4e3; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=d539b9b1ae7a6d4496c2995cb7da1feefde78ab73f6f590beb08ddd9ada793aa; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 仅报告工作区为空并请求提供退款相关文件，未形成明确的 validation 路由或测试依据门禁。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 提供已确认的 PRD、TRD、IMPLEMENTATION_PLAN 或验收记录，以及异常场景、错误码、订单状态和预期结果。
- Next: 依据稳定且明确的预期再交接 QA 或 Engineer/test-writer。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
