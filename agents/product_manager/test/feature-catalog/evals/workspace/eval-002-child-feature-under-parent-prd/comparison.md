# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-002-child-feature-under-parent-prd`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `e64d0dc500eb5720a57f43e64b9a52c75b87f674117c2e966a459db4cd412910` from `agents/product_manager/test/feature-catalog/evals/workspace/eval-002-child-feature-under-parent-prd`.
- Identity schema: `2`
- target_skill_sha256: `7440f3be22fb3254e3abf20bcd1c6ebca9f2fdee2fae7f710cc03af349b94250`
- eval_definition_sha256: `381b074083537f3d71cb0a28bd3dbbcbf80ece8371ca5fba3a891d822f995603`
- metadata_sha256: `9511751d671a5ae5883161ea664a79cdce7fc89cb2e17e607a976174a239c8f6`
- fixture_sha256: `e64d0dc500eb5720a57f43e64b9a52c75b87f674117c2e966a459db4cd412910`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `c03c0410b926db4903e624e0fe3e993a88d8b355caa51278c9f027aa7078ef66`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `d30a63f3453aaf3bd01618d870dc101f5d610329fec8c95cdf338a27c46a679e`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `855b39267bf29cb8319dc4bcf28cd88b5cba0ad0d7279c117acb672b2cd4540b`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `parent_prd_context_read` | PASS | Locked with_skill trace shows a command reading docs/pm/order-management/PRD.md before the candidate states and reuses feature_path order-management. |
| `child_nested_under_parent` | PASS | The candidate proposes order-management/refunds as a level-2 child under order-management, not a parallel top-level feature. |
| `feature_level_metadata` | PASS | The candidate output explicitly gives parent_feature: order-management and feature_level: 2, matching the two-segment path. |
| `handoff_packet_fields` | NOT_EXERCISED | The candidate correctly stops at the confirmation gate; the later handoff packet cannot yet be produced without maintainer confirmation, so this assertion is not exercised. |
| `no_bulk_prd` | PASS | No PRD/TRD content is generated. The next steps explicitly route PM documents to idea-to-spec and the engineering TRD to engineer-agent:trd-gen. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d30a63f3453aaf3bd01618d870dc101f5d610329fec8c95cdf338a27c46a679e; fixture_sha256=e64d0dc500eb5720a57f43e64b9a52c75b87f674117c2e966a459db4cd412910; output_sha256=db78f87c05b125844821cf1e7fc321e12ed9fce17a4a6baead1f1e243163750b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Read the parent PRD, proposed a correctly nested refund feature with consistent metadata, stopped for confirmation, and described the downstream spec/TRD handoffs.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d30a63f3453aaf3bd01618d870dc101f5d610329fec8c95cdf338a27c46a679e; fixture_sha256=e64d0dc500eb5720a57f43e64b9a52c75b87f674117c2e966a459db4cd412910; output_sha256=c6e6dfec1f4723b39e8ceb53a6cdc54267d0b8fbfbd8608908d08e63f062db4f; snapshot_sha256=82208bba18143467a3b305a7b0d41bd0809b12c45e7678f18346f8509a5b0150
- Behavior: Produced catalog and refund PRD files immediately, but did not demonstrate the confirmation-gated handoff contract.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain maintainer confirmation, then evaluate the generated handoff packet fields.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
