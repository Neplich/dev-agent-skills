# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-003-feature-path-missing-plan-blocked`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc` from `agents/qa/test/qa-agent/evals/workspace/eval-3-feature-path-missing-plan-blocked`.
- Identity schema: `2`
- target_skill_sha256: `67401f0f5ce98032f224aebfb24715fe0d3d5f8bc92ca57ff320d37e3d49c72a`
- eval_definition_sha256: `ec357d7e216245f12726027da14d7981d249bcac4a9eff1a2ed19f5ffc8af4f2`
- metadata_sha256: `aa798ca118679678c2fef882d4726badd357a387202dcb387aceaa4b86696bd0`
- fixture_sha256: `39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `7c827cee8609863280607c031efdc95a92d32b851664d68126eccd9d66c1f27a`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `094ec5b09f42125c7ea3b42f7f8365ddf4bd40bef6652060cfeb7ff368908608`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `91245fb0d1aab0b640cd99927d1845139d30d7b5d4db55c73139dce82b7a7bde`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_same_feature_path` | PASS | 原始 trace 显示读取同路径 PRD、TRD、FLOW_INDEX 和 TEST_SUITE；最终交接明确使用 feature_path `account/profile/preferences` 并保留 QA 功能树路径。 |
| `specialist_gate_pointer` | PASS | 最终交接指定 `spec-based-tester` 为 downstream_owner，并明确缺少同路径 `IMPLEMENTATION_PLAN.md`，因此不能执行 E2E；同时声明 router 不创建、修改或运行 E2E 资产。 |
| `keeps_single_route` | PASS | 仅选择了一个最窄 route：`spec-based-tester`；trace 未显示并行调用、下游执行或实现修复。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=094ec5b09f42125c7ea3b42f7f8365ddf4bd40bef6652060cfeb7ff368908608; fixture_sha256=39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc; output_sha256=c585d42cb10a02bae03eecbbcc7b999ffb838d61cf5a8d69c9518b702dd49e83; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别为文档化验收，选择单一的 spec-based-tester 路由，保留 feature_path、同路径材料和 QA 功能树，并指出实施计划缺失导致无法执行。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=094ec5b09f42125c7ea3b42f7f8365ddf4bd40bef6652060cfeb7ff368908608; fixture_sha256=39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc; output_sha256=601383512a6ac1c68031f0f9e3c3d4677432759fa18e817050de700b992e388a; snapshot_sha256=774e299147f9dcd3cb9766cfde25c4057deaa9530150269fdb037056c1982f5d
- Behavior: 更新了 QA 测试套件和流程索引，但自行进行了 E2E 资产整理并报告执行阻塞，未体现 specialist 路由门禁。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补齐并确认 IMPLEMENTATION_PLAN.md 后交由 spec-based-tester 继续验证。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
