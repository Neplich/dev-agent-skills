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
- target_skill_sha256: `7f71c78ab97a67d477751886a8f46d8cfd865bac113be49568de86ccf5343ee9`
- eval_definition_sha256: `92bf4838a78758f537ca7650dd1be190ad947406f8ab40d6ace62d644c28dc37`
- metadata_sha256: `f9ca20298152f7ee141273d4d234041abb35178d98ecce2603f695eedfbc144d`
- fixture_sha256: `c0e7350515f9e8f3a166039b0e6d074b044f7918d0abfcaabf64ea0fd4ef53cb`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `a264d3282fcfebf29821ed24d8e702134594b3cc4be72cd72f03b0e03e92c160`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `9ebe9d873c66a07a5ecd0428e103d2f74136e9e17f4f22b79640f42f218d18ee`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `6ba93c2da62bbbed9ea41d72d153901f8e8bbbbad20322168e3cf7c265e800fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_unfinished_active_plan` | PASS | The with_skill trace shows the active IMPLEMENTATION_PLAN.md was read; the checkpoint records its path, status Draft, and pre-write scope refund-reason-codes. |
| `detects_explicit_abandonment` | PASS | The delivered checkpoint and archive record that the maintainer explicitly abandoned the unfinished refund reason-code round and select the superseded path. |
| `archives_as_superseded` | PASS | The locked archive snapshot has status Superseded, non-empty superseded_reason, implementation_scope, archived_at, archive_approved_by, source_plan, and preserved original metadata. |
| `links_replacement_plan` | PASS | The locked replacement plan contains previous_plan_archive pointing to the Superseded archive, with feature_path payment-refund matching the archive metadata. |
| `waits_before_coding` | PASS | The locked delivery contains only plan/archive changes, states no code was modified, and explicitly requires user confirmation before coding. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9ebe9d873c66a07a5ecd0428e103d2f74136e9e17f4f22b79640f42f218d18ee; fixture_sha256=c0e7350515f9e8f3a166039b0e6d074b044f7918d0abfcaabf64ea0fd4ef53cb; output_sha256=d6d7414fd3a5dbe0a6fd169a6ad96bb4d3409723f9093e0b64fa2a26d60295d8; snapshot_sha256=7a010c4e3b402518147dbf39c5209c5cc845fb69795584d3b2948233745edc93
- Behavior: Correctly read the unfinished plan, detected explicit abandonment, archived it as Superseded, linked the replacement plan, and paused before coding.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9ebe9d873c66a07a5ecd0428e103d2f74136e9e17f4f22b79640f42f218d18ee; fixture_sha256=c0e7350515f9e8f3a166039b0e6d074b044f7918d0abfcaabf64ea0fd4ef53cb; output_sha256=1af6460847ad8c512e6c2a9ffa93c1e5a44be1981dfdd9f43018c15e66b3271e; snapshot_sha256=5a0fd9dd2c0200a4b3902d0a02895accf0a5d98aea4ecf31f4cc1a7496d35f92
- Behavior: Fresh baseline updated the active Draft plan directly to the replacement scope without the required archive, replacement link, or confirmation gate.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
