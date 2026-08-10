# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-003-route-release-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `aea5c9e95cc3674c80708ee78ba0276fef121e6d5652789edf0421371d054bf6` from `agents/docs/test/docs-agent/evals/workspace/eval-003-route-release-audit`.
- Fixture SHA-256: `aea5c9e95cc3674c80708ee78ba0276fef121e6d5652789edf0421371d054bf6`
- Prompt SHA-256: `099569afeec045caa3e4e020611c72b9def7b5897f52222810916bd2477fd230`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `cf92649952a97be677cf5e900a4d9c793a6c0724813cf1fa3154f57e7d2c08f3`
- Skill overlay SHA-256: `c7033e85898ff61111eb14edc47b25e717119ee79349d7af461390afc706db78`
- Judge schema SHA-256: `f4f786bd56d6a5cbcee24193816a462566a8caafb4c223ef38759bdf64ee0486`
- Eval definition SHA-256: `76669427412e6a3d2662bf813faa0ce4c31fa19c75739559cabe530efd5682a6`
- Metadata SHA-256: `d582bafa2b7d4e637ef2b4b71f14f435256d70c30e92f7097a43cd40dc9da750`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_equivalent_chain` | PASS | 将 release-entry.md 明确识别为等价确认链，并保留 v0.4.0 正式文档发版审计及其引用的 changelog、CI/pytest 与正式站点证据。 |
| `routes_docs_audit` | PASS | 明确选择 docs-audit，并传递 v0.4.0 scope、release-entry.md、changelog/CI/pytest 等 release evidence，同时将执行边界交给该 specialist。 |
| `references_audit_gate_only` | PASS | 明确声明仅路由至 docs-audit、停在 router 边界，且未暴露本地技能路径或复制 specialist 协议。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=099569afeec045caa3e4e020611c72b9def7b5897f52222810916bd2477fd230; fixture_sha256=aea5c9e95cc3674c80708ee78ba0276fef121e6d5652789edf0421371d054bf6; output_sha256=3c43a58c365018588d32e36c835808e4168a2b397667eee8b6e0de0d49133f21; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别等效确认链，选择 docs-audit，保留证据并停在路由边界。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=099569afeec045caa3e4e020611c72b9def7b5897f52222810916bd2477fd230; fixture_sha256=aea5c9e95cc3674c80708ee78ba0276fef121e6d5652789edf0421371d054bf6; output_sha256=05781409ba05350f340bb230f02357964ccb9cc92e16f5cef4abe3bba8b1f4a5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 未执行路由，转而进行正式文档审计并给出证据不足结论。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
