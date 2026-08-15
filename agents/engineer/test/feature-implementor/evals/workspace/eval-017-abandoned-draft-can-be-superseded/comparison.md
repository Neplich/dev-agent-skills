# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-017-abandoned-draft-can-be-superseded`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c0e7350515f9e8f3a166039b0e6d074b044f7918d0abfcaabf64ea0fd4ef53cb` from `agents/engineer/test/feature-implementor/evals/workspace/eval-017-abandoned-draft-can-be-superseded`.
- Identity schema: `2`
- target_skill_sha256: `248d30c2e10162217ecb1d6a0d7c66973ee945c6f2e9b7e4bf01a677aac7bc3c`
- eval_definition_sha256: `92bf4838a78758f537ca7650dd1be190ad947406f8ab40d6ace62d644c28dc37`
- metadata_sha256: `f9ca20298152f7ee141273d4d234041abb35178d98ecce2603f695eedfbc144d`
- fixture_sha256: `c0e7350515f9e8f3a166039b0e6d074b044f7918d0abfcaabf64ea0fd4ef53cb`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `a264d3282fcfebf29821ed24d8e702134594b3cc4be72cd72f03b0e03e92c160`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `9ebe9d873c66a07a5ecd0428e103d2f74136e9e17f4f22b79640f42f218d18ee`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `8002de5f5ec8cbba9c876b3fa5b95d04da373914039535f254ff8fce02f9cbab`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_unfinished_active_plan` | PASS | With-skill raw trace shows the existing implementation plan was read; the delivered plan records the fixed path, prior status Draft, and prior scope refund-reason-codes. |
| `detects_explicit_abandonment` | PASS | The delivered active plan and archive explicitly state that the unfinished refund reason-code round was abandoned and replaced, matching the maintainer’s explicit abandonment request. |
| `archives_as_superseded` | PASS | The locked archive snapshot has status Superseded, a non-empty superseded_reason, and preserves implementation_scope, archived_at, archive_approved_by, source_plan, and original metadata. |
| `links_replacement_plan` | PASS | The locked active-plan snapshot contains previous_plan_archive pointing to the same-feature archive, whose snapshot has feature_path payment-refund and status Superseded. |
| `waits_before_coding` | PASS | Git evidence shows only plan/archive documentation changes; the plan states Draft and awaiting maintainer confirmation, and the output explicitly blocks implementation until confirmation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9ebe9d873c66a07a5ecd0428e103d2f74136e9e17f4f22b79640f42f218d18ee; fixture_sha256=c0e7350515f9e8f3a166039b0e6d074b044f7918d0abfcaabf64ea0fd4ef53cb; output_sha256=02f590dbb5063804f978d4cab42af4ef5b6019994c60860641c7097aef54a528; snapshot_sha256=04b8add69e118eacf4fc4d7903cef7cce78ec2343ec131901e0778def207481f
- Behavior: Reads the unfinished plan, detects explicit abandonment, archives it as Superseded, creates and links a replacement Draft plan, and waits for confirmation before coding.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9ebe9d873c66a07a5ecd0428e103d2f74136e9e17f4f22b79640f42f218d18ee; fixture_sha256=c0e7350515f9e8f3a166039b0e6d074b044f7918d0abfcaabf64ea0fd4ef53cb; output_sha256=5f97f7fd0aa83cbe385f3fe20e3b209b83b3580ea1f3f4c353bb45bf0cada83b; snapshot_sha256=6aab714931c23cf3173da27a41bcaae18a2b1d1c434bad686eb199fa54b5ef8d
- Behavior: Switches the existing plan directly to Active and does not create the required Superseded archive or confirmation gate.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
