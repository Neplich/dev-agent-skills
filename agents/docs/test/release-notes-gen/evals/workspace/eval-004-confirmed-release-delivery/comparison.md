# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-004-confirmed-release-delivery`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c11c4570536758cb911b613643632dd7b15e8b492fb6a5c6cb788342176462bf` from `agents/docs/test/release-notes-gen/evals/workspace/eval-004-confirmed-release-delivery`.
- Identity schema: `2`
- target_skill_sha256: `3da1a9a1466d6ecd43ed5c082adf803d01b5c2ca25dfee7a882fcc8113f7ce5c`
- eval_definition_sha256: `6ba71c78dee7f69b879178b4307965fc8b664b773fca948482dc1711c289b5ad`
- metadata_sha256: `2e15aaf06f83170c681a449f442bd9946bbef263dbea552644182da638b4addc`
- fixture_sha256: `c11c4570536758cb911b613643632dd7b15e8b492fb6a5c6cb788342176462bf`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `5f19f02b941db43659fbfb03cc28f127d2b4bbc556ed59290b7811c966f30dc8`
- Source lock SHA-256: `c58f04d32c2ca3a22aec96f7ee027af648da5971453d2a5553d7ab2cd9272551`
- Prompt SHA-256: `5d2eb8fee66e709ed28ba5aa53ac1e57295ed25d74500a43d924b8fbc434431e`
- Repository HEAD: `60a4b3602dc07f3f6683a8873529bbdba6f8d27d`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `9d7abf20333b60efc8aeaad2d302ecd422e44bb547e52f5a4d9623347a2b048b`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `delivers_confirmed_release_page` | PASS | 交付快照中的 v1.0.0 页面包含六类证据章节，frontmatter 合法，且 last_verified_version 为 unverified。 |
| `updates_derived_surfaces_after_confirmation` | PASS | 追踪显示正文确认后才写入页面、index 和 metadata；最终快照保留 v0.9.0、manualNote，并由宿主脚本生成导航。 |
| `passes_host_docs_checks` | PASS | runner trace 中 npm run test:docs 在正确站点上下文执行并通过：frontmatter、strict affected、version metadata 及 75 个测试均通过。 |
| `returns_complete_ready_handoff` | PASS | 最终输出包含 docs-agent:docs-audit / pre-tag、版本及确认来源、页面、检查、更新面、证据缺口、blockers、downstream_target 和 release_execution_authorized: false。 |
| `preserves_external_release_boundary` | PASS | git evidence 显示无提交、分支或 ref 变化；页面和 index 均保持 last_verified_version: unverified，且输出明确未创建 tag、GitHub Release、镜像或部署。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5d2eb8fee66e709ed28ba5aa53ac1e57295ed25d74500a43d924b8fbc434431e; fixture_sha256=c11c4570536758cb911b613643632dd7b15e8b492fb6a5c6cb788342176462bf; output_sha256=10e5318b6cda87c7acf5b187135b5860cdf51b211c6e3d822186ae3ebadefa5a; snapshot_sha256=58b153a241a08dc83475eb9093dea5e00bd7b5d48a23bc9a0cfb7b1ac13f1078
- Behavior: 完成确认后的站内 Release Notes 交付，真实 docs checks 通过，并返回边界明确的 ready handoff。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5d2eb8fee66e709ed28ba5aa53ac1e57295ed25d74500a43d924b8fbc434431e; fixture_sha256=c11c4570536758cb911b613643632dd7b15e8b492fb6a5c6cb788342176462bf; output_sha256=84da08ebad8c7749a347c6db31cb729cba68cad511ea5d7f0981107a5b96a175; snapshot_sha256=bc52004a92a388d75146f36455c79e0aa049445567caa489d4e4fba520b32047
- Behavior: 也完成了主要页面和派生面更新，但报告缺少完整 handoff，且存在不受 raw evidence 支持的构建声明。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
