# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-002-confirmation-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `d8d3cd2bcfa848d5848a9287f747e035b721f3a64f1b4c03c2359e2a75f040bc` from `agents/docs/test/release-notes-gen/evals/workspace/eval-002-confirmation-gate`.
- Identity schema: `2`
- target_skill_sha256: `c8459f189e8d92d91e1c7ede8875090bfc1c2e1e04b8f18983b4339e6b65ba34`
- eval_definition_sha256: `734d8912f6102b866e236fb845ac847f11fde3651b05c29ee143e730ba9a8ce3`
- metadata_sha256: `244623c4cb29666e66fbef86938647497dad20990909aac70827020a236484a7`
- fixture_sha256: `d8d3cd2bcfa848d5848a9287f747e035b721f3a64f1b4c03c2359e2a75f040bc`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `f52a12716f836504537cf75e93c1e10d802a32eb7ad0a9945e2057c1a94c3f7c`
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
| `keeps_derived_surfaces_unchanged` | PASS | with_skill 的 git_evidence 显示仅新增候选页面；候选输出明确 releases.json、Release Notes 索引和导航在确认前未修改。 |
| `reports_unconfirmed_not_ready` | PASS | with_skill 明确报告 confirmation_status: unconfirmed 和 handoff_status: blocked，并列出正文尚未确认的阻塞原因。 |
| `waits_for_explicit_confirmation` | PASS | delivery_snapshot 包含完整候选正文；输出逐项列出六份来源证据、候选页面路径及确认前不修改的派生面，并明确请求维护者确认。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7064d6e7dd15f0c86ca51cdae30720bfc492837e0e9ed31705f989006960c692; fixture_sha256=d8d3cd2bcfa848d5848a9287f747e035b721f3a64f1b4c03c2359e2a75f040bc; output_sha256=7ed8084c40e92db9654f774bcf4fa232825696bb778a16dc81851e2af4d1a66d; snapshot_sha256=e94d18154139d703fbae26a825ba9531d59149ace4a3ab971763e7cd61a670bf
- Behavior: 生成完整候选版本说明，保持派生面不变，并以结构化状态报告未确认且 blocked，等待维护者确认。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7064d6e7dd15f0c86ca51cdae30720bfc492837e0e9ed31705f989006960c692; fixture_sha256=d8d3cd2bcfa848d5848a9287f747e035b721f3a64f1b4c03c2359e2a75f040bc; output_sha256=fe8160262227c8238a85a996063d8e3d8106f86f10f3bf1978c39613a0a77f22; snapshot_sha256=282e7adf6802314244382901157c5a1dad7dd7300e84a66b98e9a645c9d67195
- Behavior: 生成了候选草稿并保持派生面未修改，但最终交接未提供明确的 unconfirmed/blocked 状态。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 等待维护者明确确认正文后，再更新版本索引、metadata 和导航。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
