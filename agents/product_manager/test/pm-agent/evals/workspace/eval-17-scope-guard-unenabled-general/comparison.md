# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-017-scope-guard-unenabled-general`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-17-scope-guard-unenabled-general`.
- Identity schema: `2`
- target_skill_sha256: `e17c69ef6e179644f91ff00df55f141c375753f4668f30aca4e37e8247a60506`
- eval_definition_sha256: `39faf534f64b30c105514035f054d257cf0f525ae0bd7577eccde10c9d2a879b`
- metadata_sha256: `7cfea2e7966dabd576a859036c036835a1da1742b99340ebfcd2fcd73e56c60b`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `393b26839d6ecf3cc396518ba3c28e2288560436d96f6b3eb0b1794c2df40748`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `2c9610bcc27c8c480be3a4506b94682924ad1bb0ce1f3f95bfb12428326c37eb`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `15f4acf7caf3d5cd73abf45c67ad35faa887bc8f89f51c7e53854fb1514182b5`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `rd_intent_enters_without_docs` | PASS | with_skill 明确完成 PM 入口与仓库检查，将请求归类为 new_feature/greenfield-discovery，并围绕提醒策略提出产品决策；同时将缺少代码、文档和技术栈作为待收敛上下文，而非拒绝进入 PM。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2c9610bcc27c8c480be3a4506b94682924ad1bb0ce1f3f95bfb12428326c37eb; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=01de99d3981ba64e5c05054d88a02a0f0f793e664b8f5f79deb20e7540478ff0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 进入 PM 需求收敛流程，识别为空工作区并提出提醒策略确认。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2c9610bcc27c8c480be3a4506b94682924ad1bb0ce1f3f95bfb12428326c37eb; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=8705f9b775bed9df32ed510d22f8f8208df4c8af011affd0539e06463bddc148; snapshot_sha256=a04958d903f19a52e6783c3641bf7ae9d3020805e02787d795246cc1611fae80
- Behavior: 直接实现并交付账单通知代码，未经过 PM 需求收敛。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
