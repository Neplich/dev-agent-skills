# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-001-route-formal-docs-sync`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991` from `agents/docs/test/docs-agent/evals/workspace/eval-001-route-formal-docs-sync`.
- Identity schema: `2`
- target_skill_sha256: `cf826e2e86ef193d8a7294a87c743dead6af892aefcc220dd56ae949fa5c3b40`
- eval_definition_sha256: `b7962cc5c7265d8b3c4f799e1e809f203d9b09d09c3950072c84712c7db0c562`
- metadata_sha256: `320948f19ccb8c159c24fdc827ddc592aac02ee3f64236dd9e4896bae8e4979e`
- fixture_sha256: `5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `d9120b553be3673816559c0b102ba0210980dbae3daaf9eeba42b66ee4308ec2`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `e48b238fe72b5801d36c88005426156c8c6d404e006c5bccb655f20f86d8f497`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `4a886ffdcb18b30d43dbd2f9ee95780d97f9d5daf71fdddfd34bccc37d3c110d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_to_formal_docs_sync` | PASS | with_skill 明确选择 `formal-docs-sync`，并标注为 Feature delivery；范围为搜索 API 当前状态，排除数据库、Ops、Release 文档。 |
| `preserves_handoff_context` | PASS | with_skill 保留并概述 `pm-handoff.md` 的变更级别、功能路径、PRD/TRD/实施计划、实现与合同测试证据、正式 API 页面及 change-map 输出范围和风险说明。 |
| `points_to_authoritative_gate` | PASS | with_skill 将后续核验和同步交给 `formal-docs-sync`，明确 Router 不修改文档；未暴露本地 SKILL.md 路径或复制完整同步协议。 |
| `stops_at_router_boundary` | PASS | with_skill 明确当前 Router 未修改任何文档；锁定 git evidence 显示工作区和 HEAD 均未变化。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e48b238fe72b5801d36c88005426156c8c6d404e006c5bccb655f20f86d8f497; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=41142d6db289aabbb51996e2ff5d63d9e4f84fcacefb583060849c4ffb2ce7b9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别已确认的 feature delivery，保留 handoff 上下文，将后续工作交给 formal-docs-sync，并停在 Router 边界等待确认。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e48b238fe72b5801d36c88005426156c8c6d404e006c5bccb655f20f86d8f497; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=d18f5250a4eea1815f5f4b3f08c9f55a8b4e0de79e1e52e81bd2b957759f4c53; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 将正式文档同步错误地阻塞在缺少源文档，并要求补齐 docs 或提供其他提交，未完成正确路由。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
