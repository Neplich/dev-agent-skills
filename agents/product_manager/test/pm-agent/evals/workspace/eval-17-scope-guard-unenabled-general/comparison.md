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
- target_skill_sha256: `cec475406cc49b4c9cebbfe9c62f8f1a19fc3e7ced9282825f8f2930bab1478a`
- eval_definition_sha256: `39faf534f64b30c105514035f054d257cf0f525ae0bd7577eccde10c9d2a879b`
- metadata_sha256: `7cfea2e7966dabd576a859036c036835a1da1742b99340ebfcd2fcd73e56c60b`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `393b26839d6ecf3cc396518ba3c28e2288560436d96f6b3eb0b1794c2df40748`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `2c9610bcc27c8c480be3a4506b94682924ad1bb0ce1f3f95bfb12428326c37eb`
- Repository HEAD: `133a65e3c3b501be88257e9d3a557af4d5ccd242`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `5047311446f87e0c9eb6ef7577938db174e729f8d09b2851971cbb87a063bf63`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `rd_intent_enters_without_docs` | PASS | with_skill 明确将请求分类为 new_feature，selected_owner 为 idea-to-spec，next_action 为 PM 需求发现；同时记录 existing_docs/source_documents 为空，但未因此拒绝进入 PM。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2c9610bcc27c8c480be3a4506b94682924ad1bb0ce1f3f95bfb12428326c37eb; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=426b7f1a6fb1fbff6d88cba833df13cd8bb5cdf7a5760fd3866fdde38969792c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 在空工作区、无 PRD/TRD/代码时进入 PM 需求收敛，识别未决触发策略并请求用户确认。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2c9610bcc27c8c480be3a4506b94682924ad1bb0ce1f3f95bfb12428326c37eb; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=59f9f5b3643932c28e3bb33f9ed62f9d03ea958e7e254e7b40014f3c2c3f511a; snapshot_sha256=9b029c9517396a8d997df32dc9f96ebbad7b75f0821df65a9e256aa574e8afc8
- Behavior: 直接实现账单通知服务并写入代码，未进行 PM 需求收敛。仅作对比，不影响 with_skill 断言判定。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
