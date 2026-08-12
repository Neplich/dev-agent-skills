# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-002-user-rights`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8` from `agents/security/test/privacy-surface-mapper/evals/workspace/eval-002-user-rights`.
- Identity schema: `2`
- target_skill_sha256: `25bd4dbed66f3625883b2a2072dcd568eef569278521e1eac012e86f61347836`
- eval_definition_sha256: `ba5034d1b895bcb95cc9d848045b869189eec2c98d23c0a5d5ce381059a73047`
- metadata_sha256: `b655e3698222cf189fb740616c1df41fb5ccc3d4bf71526ca29a7ecf05ef368a`
- fixture_sha256: `2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `46c6f10cb2ee094e0f2d9b8cf0d9d794ebc801a301eb97187a76e961b4e37fd0`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `data_inventory` | PASS | 报告盘点了用户资料、订单、行为事件及会话元数据，说明了对应入口和处理目的，并标注未知项。 |
| `sharing_and_retention` | PASS | 报告识别了分析系统、第三方副本、缓存、备份及跨境传输的不确定性，指出缺少删除传播和保留期限策略，并给出整改建议。 |
| `user_rights` | PASS | 报告逐项检查了访问、导出、删除和更正权利，准确指出导出越权、导出不完整及删除不可追踪等问题。 |
| `compliance_gaps` | PASS | 报告给出了明确的隐私合规缺口、影响、责任归属和上线前整改与验证计划。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0; fixture_sha256=2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8; output_sha256=4122fc8f59dd8022a7ee4e39bd4375a784b6146a3a75aafeb73934d1ea80fc0c; snapshot_sha256=9a40e15bee9c345dcfadb12f6924b766acd3cf7bf51fcfe7bad6b5f3d259ae14
- Behavior: 生成并交付了完整的隐私处理面报告，覆盖数据盘点、数据流、用户权利、第三方共享、保留风险、影响和整改建议。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0; fixture_sha256=2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8; output_sha256=e651049403c141050f3db0d79a302d4c561934a29a4a6df0280f80fe5a39807b; snapshot_sha256=e9309385bd56ce2be7a8e776c70f7fead09cebe419b83eef7694dd33413d46be
- Behavior: 同样识别了主要安全缺口并交付了报告，但数据盘点、第三方共享和合规范围的结构化覆盖较少。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
