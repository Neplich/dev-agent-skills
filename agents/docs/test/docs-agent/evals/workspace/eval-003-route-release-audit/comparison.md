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
- Repository HEAD: `fecf485e8e3dcaf191b2b221d9cccbddfdea0b72`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `cf92649952a97be677cf5e900a4d9c793a6c0724813cf1fa3154f57e7d2c08f3`
- Skill overlay SHA-256: `85c4ae0a1d58505c4a23c34e6f9116aed81a09b4b6270e3ce148424084f6c7e0`
- Judge schema SHA-256: `f4f786bd56d6a5cbcee24193816a462566a8caafb4c223ef38759bdf64ee0486`
- Eval definition SHA-256: `76669427412e6a3d2662bf813faa0ce4c31fa19c75739559cabe530efd5682a6`
- Metadata SHA-256: `d582bafa2b7d4e637ef2b4b71f14f435256d70c30e92f7097a43cd40dc9da750`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_equivalent_chain` | FAIL | with_skill 输出称 `release-entry.md` 仅提供“部分等效 release chain”，并错误地要求额外的 maintainer target version；未将 fixture 中已确认的 scope、version tag、changelog、release evidence 与 audit request 整体识别为等效入口。 |
| `routes_docs_audit` | PASS | with_skill 明确选择 `docs-audit`，并列出 v0.4.0 审计范围及 release-entry/changelog/evidence 上下文，停止执行实际审计并安排后续交给该 specialist。 |
| `references_audit_gate_only` | FAIL | with_skill 明确写出 `docs-audit` 和 router 边界，但同时暴露并展开 previous-tag、base-ref、target version 及审计阶段 gate 等下游细节，超出仅引用 specialist gate 的要求。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=099569afeec045caa3e4e020611c72b9def7b5897f52222810916bd2477fd230; fixture_sha256=aea5c9e95cc3674c80708ee78ba0276fef121e6d5652789edf0421371d054bf6; output_sha256=fb6e1de263218c090742df6dd7ca6ae06b2788e79d6a4875998b13d7ebf5c416; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确选择 docs-audit 并停止在路由边界，但错误地将已确认入口判为不完整，并泄露下游 gate 细节。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=099569afeec045caa3e4e020611c72b9def7b5897f52222810916bd2477fd230; fixture_sha256=aea5c9e95cc3674c80708ee78ba0276fef121e6d5652789edf0421371d054bf6; output_sha256=6d9cca4c65cc695dd9d2d66bd99297108b47acbe268895ca54b1251460bea76d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 将请求当作实际文档审计，输出审计阻塞结论和材料补齐建议，未进行 specialist 路由。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未接受 fixture 已确认的完整等效 release chain。
- with_skill 暴露了 docs-audit 的 base/target 等下游审计门槛细节。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
