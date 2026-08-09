# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-007-route-manual-gen`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8` from `agents/docs/test/docs-agent/evals/workspace/eval-007-route-manual-gen`.
- Fixture SHA-256: `7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8`
- Prompt SHA-256: `a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b04f0f833fdfe60f19dba4258110d7f6b0a3d6a6f2afb7034b0d3d883c30f83b`
- Skill overlay SHA-256: `91cbb2dfbc7f79ee3f298d858c1e3b0b986717f5b79fc8d2fb2d8be9f6762763`
- Judge schema SHA-256: `dfbcad96e39d7a0ba2503c7d345d86b54a6c9e1188ff1c09f99476b24380e820`
- Eval definition SHA-256: `11398fbb2de74bd454f6e9c88338b5fcf6dffb0fd21436f1f6c99eaff5b1117d`
- Metadata SHA-256: `31c2720a1114e612336c51527d7aae20dddb1f4e46b566ffffe4788d27952b8e`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_manual_entry_basis` | PASS | with_skill 明确接受 manual-handoff.md 中的显式 Manual Generation Handoff，并保留入口字段。 |
| `routes_manual_gen` | PASS | with_skill 明确选择 selected_specialist: manual-gen，未改派其他 specialist。 |
| `preserves_manual_handoff_context` | PASS | with_skill 保留 request_type、change_tier、feature_path、host_repository、manual_scope（以 confirmed_scope 表达）、evidence_sources、required_output 与 blockers_risks。 |
| `references_manual_gate_only` | PASS | with_skill 指向 manual-gen authoritative Entry Gate，并明确路由边界：不采集截图、不生成正文、不写入站点文件。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa; fixture_sha256=7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8; output_sha256=939dd18b83baa441759def73fa3c7dd6f61a8a6f186f5a8cfdb1e1e078d30ee8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别入口凭据，路由至 manual-gen，保留上下文并停在 specialist gate 边界。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa; fixture_sha256=7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8; output_sha256=7a4c0fe3c14ba2bee699b05fc90b52bc83fcba24072d04c4bc519c0d5cc615ea; snapshot_sha256=10e8c8a895c274312d91e87ca89f644f3c6f2e3099f8f6385e33d5417421d464
- Behavior: 直接生成并声明完成手册，产生 docs/site/manual/ 下的文件，未执行所需的 manual-gen 路由边界。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
