# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-003-route-release-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c4a69775f21689d655afd993fc0db7c357209ede650d2394be50a3f72bd824b5` from `agents/docs/test/docs-agent/evals/workspace/eval-003-route-release-audit`.
- Identity schema: `2`
- target_skill_sha256: `023cc6d8aa109db6ff7dcd662df567ae4f0c79dddb66dfe7bcf6f1eb91d20f39`
- eval_definition_sha256: `6d6a401b76741386ad3f6aee549b3bfaa2f477f4ced9973b14647dc8b591096b`
- metadata_sha256: `d582bafa2b7d4e637ef2b4b71f14f435256d70c30e92f7097a43cd40dc9da750`
- fixture_sha256: `c4a69775f21689d655afd993fc0db7c357209ede650d2394be50a3f72bd824b5`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `f4f786bd56d6a5cbcee24193816a462566a8caafb4c223ef38759bdf64ee0486`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `099569afeec045caa3e4e020611c72b9def7b5897f52222810916bd2477fd230`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `d7e2242fcdf83209e6c0cb5ec9544aa009e79488a72f81ebd4bf387289fbabec`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_equivalent_chain` | PASS | with_skill 明确将 release-entry.md 识别为等效正式文档审计入口链，并保留 release scope、v0.4.0/v0.3.0 锚点、范围、changelog、release evidence 和审计请求。 |
| `routes_docs_audit` | PASS | with_skill 明确选择 docs-audit，交付 v0.4.0 正式文档审计，并在交接内容中保留版本范围、changelog、站点 release notes 及相关 release evidence。 |
| `references_audit_gate_only` | PASS | with_skill 明确说明路由层不执行审计、不写入报告或版本元数据；仅要求后续由 docs-audit 按其协议执行，未暴露 SKILL.md 路径或复制内部审计层协议。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=099569afeec045caa3e4e020611c72b9def7b5897f52222810916bd2477fd230; fixture_sha256=c4a69775f21689d655afd993fc0db7c357209ede650d2394be50a3f72bd824b5; output_sha256=2cd5391674b9c6ed836bd2ec1b372e0f5b99af12243fa2d178d48a3c88226205; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别等效确认链，正确路由至 docs-audit，并停在等待用户确认的下一步。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=099569afeec045caa3e4e020611c72b9def7b5897f52222810916bd2477fd230; fixture_sha256=c4a69775f21689d655afd993fc0db7c357209ede650d2394be50a3f72bd824b5; output_sha256=6e470865076fb9b0c843a7b385fc7a879553c928380da01bb51c32d5eff25f41; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 将入口声明误判为无法复核的发版审计对象，未完成所需路由；仅作基线对比。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
