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
- Fixture SHA-256: `5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991`
- Prompt SHA-256: `898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `cf92649952a97be677cf5e900a4d9c793a6c0724813cf1fa3154f57e7d2c08f3`
- Skill overlay SHA-256: `5dbb8d8559bfab3926047aa028e19f362490751247c2142101cfd687fff5239e`
- Judge schema SHA-256: `d9120b553be3673816559c0b102ba0210980dbae3daaf9eeba42b66ee4308ec2`
- Eval definition SHA-256: `4f62b001057b225d1029a6284046afacf46248ad92aa43b0c065e0a0456b7450`
- Metadata SHA-256: `320948f19ccb8c159c24fdc827ddc592aac02ee3f64236dd9e4896bae8e4979e`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_to_formal_docs_sync` | PASS | with_skill 明确选择 `formal-docs-sync`，并将其识别为 feature-delivery 正式文档同步；未选择 bootstrap、release notes 或 audit。 |
| `preserves_handoff_context` | FAIL | with_skill 保留了功能路径、来源文档、同步范围、排除项、证据、目标 API 页面/change-map 及风险，但未完整保留 fixture 中的 feature、parent_feature、feature_level、feature_path_evidence 和 downstream_owner 等已提供字段。 |
| `points_to_authoritative_gate` | PASS | with_skill 明确由 `formal-docs-sync` 的 feature-delivery authoritative gate 接管，并声明 docs-agent 不执行同步或写入；未暴露本地 SKILL.md 路径，也未复制下游八步协议。 |
| `stops_at_router_boundary` | PASS | delivery_snapshot 为空，git head、分支、索引和工作区均未变化；输出明确声明本次不执行文档写入。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=dc8101a354f5e39d42d9eaa39fced274964938f89035d533098a46e356215819; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确路由至 formal-docs-sync 并停在 router 边界，但交接上下文不完整。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=b3a4d709f52fcabf8753145c4f213e35d9581a80a5550aee5188ee82cd6da5be; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了大部分交接信息，但错误地将请求路由至 `delivery` 文档能力。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未无损保留 pm-handoff.md 的全部已提供交接字段。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
