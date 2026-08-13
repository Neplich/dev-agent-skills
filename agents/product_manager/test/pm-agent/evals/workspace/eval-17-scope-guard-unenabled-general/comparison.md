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
- target_skill_sha256: `28ec452f7594200030ea15ffdc8d5edc9ae2298318457884574b818964824cf6`
- eval_definition_sha256: `39faf534f64b30c105514035f054d257cf0f525ae0bd7577eccde10c9d2a879b`
- metadata_sha256: `7cfea2e7966dabd576a859036c036835a1da1742b99340ebfcd2fcd73e56c60b`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `393b26839d6ecf3cc396518ba3c28e2288560436d96f6b3eb0b1794c2df40748`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `2c9610bcc27c8c480be3a4506b94682924ad1bb0ce1f3f95bfb12428326c37eb`
- Repository HEAD: `2f950c46c67111058957774f796ccf97ae616d36`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `8041f8266999d0ba9597ccc13e0354e28fcccb4a3b921ae9b5b9d1e08fe1da7b`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `rd_intent_enters_without_docs` | PASS | with_skill 输出明确将请求分类为 new_feature，选择 pm-agent:idea-to-spec，进入 greenfield-discovery，并说明先做需求收敛；runner_captured_trace 也记录了 PM 入口分类和后续 idea-to-spec 流程。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2c9610bcc27c8c480be3a4506b94682924ad1bb0ce1f3f95bfb12428326c37eb; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=b81f4f0bbf779f5b9e8e2afd369bf288527bd6f554a79b0d671e7f171147e33d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 面对空工作区和缺少 PRD、TRD、代码及 enable marker，进入 PM/idea-to-spec 的 greenfield-discovery，暂停工程实现并提出通知策略确认问题。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2c9610bcc27c8c480be3a4506b94682924ad1bb0ce1f3f95bfb12428326c37eb; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=45b37f6b0342b74a0f5ddcb660c7ca09a8507488a06029e9dc826a507e3f033e; snapshot_sha256=d9186a9dae5e425cdcbd718b3d5241f95c761de952d858d13d89cf01eda9a0e8
- Behavior: 直接实现并交付账单到期通知服务，未进入 PM 需求收敛流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
