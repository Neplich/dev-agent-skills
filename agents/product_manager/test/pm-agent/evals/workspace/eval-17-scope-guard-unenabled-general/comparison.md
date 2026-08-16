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
- target_skill_sha256: `ed93e443692bf05e76aaa38c8a5b8faff57190219ed48b9335316584424e6eb9`
- eval_definition_sha256: `39faf534f64b30c105514035f054d257cf0f525ae0bd7577eccde10c9d2a879b`
- metadata_sha256: `7cfea2e7966dabd576a859036c036835a1da1742b99340ebfcd2fcd73e56c60b`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `393b26839d6ecf3cc396518ba3c28e2288560436d96f6b3eb0b1794c2df40748`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `2c9610bcc27c8c480be3a4506b94682924ad1bb0ce1f3f95bfb12428326c37eb`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `320ded3db25222eda1be26706a57ed0471cc438157b54925db0b045d15abf8e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `rd_intent_enters_without_docs` | PASS | with_skill output explicitly enters PM discovery, classifies the empty repository as greenfield-discovery, proposes MVP options, and asks for confirmation; it does not refuse PM entry because PRD/TRD/code/enable marker are absent. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2c9610bcc27c8c480be3a4506b94682924ad1bb0ce1f3f95bfb12428326c37eb; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=ce3332f57675bf571547005e2e677fd6175c8697e6c68d756c8785468377e4c8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes the billing-notification R&D request into PM discovery despite the empty repository and missing documentation, then requests the next product decision.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2c9610bcc27c8c480be3a4506b94682924ad1bb0ce1f3f95bfb12428326c37eb; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=ea36383db5663266b270ebc091bf53643290c725e943548d4d2288c697c194b8; snapshot_sha256=0d351f4f4275aa52caed00df535c435a831966b31a73827e4951ffbcf48e2b68
- Behavior: Fresh baseline skipped PM discovery and directly implemented a billing-notification module in the empty repository.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
