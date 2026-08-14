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
- target_skill_sha256: `af94ca4b38768885230f6271f3d4ae9e1b1be30fcd2f5bdf1098250b4ded0306`
- eval_definition_sha256: `b7962cc5c7265d8b3c4f799e1e809f203d9b09d09c3950072c84712c7db0c562`
- metadata_sha256: `320948f19ccb8c159c24fdc827ddc592aac02ee3f64236dd9e4896bae8e4979e`
- fixture_sha256: `5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `d9120b553be3673816559c0b102ba0210980dbae3daaf9eeba42b66ee4308ec2`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `e48b238fe72b5801d36c88005426156c8c6d404e006c5bccb655f20f86d8f497`
- Repository HEAD: `133a65e3c3b501be88257e9d3a557af4d5ccd242`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `cc06f7d0ec314789bbccd4de68e0c4e6f74c0821dbe36228153c86490ecf37d8`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_to_formal_docs_sync` | PASS | with_skill 输出明确将已完成实现后的请求选择为 `formal-docs-sync`，并排除其他文档专员；handoff 的 delivery/standard/search-api-query 背景与正式 API 同步范围一致。 |
| `preserves_handoff_context` | PASS | with_skill 输出保留了 `pm-handoff.md`、搜索 API 范围、实现 diff 与 contract tests、正式 API 页面及 change-map 输出等交接上下文，未要求逐字段复述。 |
| `points_to_authoritative_gate` | PASS | with_skill 输出明确后续由 `formal-docs-sync` 执行，并将文档修改与验证交给其权威入场门；未暴露本地 SKILL.md 路径或复制同步协议。 |
| `stops_at_router_boundary` | PASS | with_skill 输出声明本次仅完成路由与交接；锁定 git_evidence 显示 HEAD、分支及工作区均未变化，delivery_snapshot 为空。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e48b238fe72b5801d36c88005426156c8c6d404e006c5bccb655f20f86d8f497; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=ff4d4d55e5c29f36bc59d434c8e9b9b3c648aac02248516fc543197d7c41cd89; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确完成正式文档同步路由，保留交接上下文并停在 specialist 边界，未执行文档写入。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e48b238fe72b5801d36c88005426156c8c6d404e006c5bccb655f20f86d8f497; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=4aefc05eb9b92ef70db3b38fc1654e198da8457bf3473856e3029dda674d384d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了同步范围但未完成 specialist 路由，并因工作区缺少相关材料而要求补充输入；仅作基线对照。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
