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
- target_skill_sha256: `a37bf10fca64a8e15e6213ecdd45b65783814d307c78fd8d8ce6ab45b20effef`
- eval_definition_sha256: `39faf534f64b30c105514035f054d257cf0f525ae0bd7577eccde10c9d2a879b`
- metadata_sha256: `7cfea2e7966dabd576a859036c036835a1da1742b99340ebfcd2fcd73e56c60b`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `393b26839d6ecf3cc396518ba3c28e2288560436d96f6b3eb0b1794c2df40748`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `2c9610bcc27c8c480be3a4506b94682924ad1bb0ce1f3f95bfb12428326c37eb`
- Repository HEAD: `3f5e81c4837ef85284a7d5381575e40267796c92`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `6f4abf80e411dc3e6124c51093f07046c341195b1b2f0e9981a535c9960cb623`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `rd_intent_enters_without_docs` | PASS | with_skill 输出明确将请求路由至 `pm-agent:idea-to-spec`，标记为 `new_feature`，并开始需求收敛；同时说明工作区为空是待确认上下文，而非拒绝进入 PM。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2c9610bcc27c8c480be3a4506b94682924ad1bb0ce1f3f95bfb12428326c37eb; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=f5fe51606347181ae7ce95b4b10203fdddcfb15c05339a0ce28100c11720b021; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 进入 PM 需求收敛流程，识别缺少项目上下文，并提出账单来源这一项下一步确认。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2c9610bcc27c8c480be3a4506b94682924ad1bb0ce1f3f95bfb12428326c37eb; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=b6e9fc12e0660d7b2bd1b58af589f59ea1a6b50577599e4f0d919407b1fe4025; snapshot_sha256=caa3c317bb79188eb4b87a9aa6ef924fc04f63f7369d1a188eacf205a293417f
- Behavior: 直接实现账单通知模块并交付代码，未进入 PM 需求收敛流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
