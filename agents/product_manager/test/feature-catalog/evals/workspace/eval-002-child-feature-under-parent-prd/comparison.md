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
- Fixture SHA-256: `e64d0dc500eb5720a57f43e64b9a52c75b87f674117c2e966a459db4cd412910`
- Prompt SHA-256: `d30a63f3453aaf3bd01618d870dc101f5d610329fec8c95cdf338a27c46a679e`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `272c84e241c5d52534922fccf2bc6732492a0d70c9f6e2ab8dc1eff2533f7b0c`
- Skill overlay SHA-256: `c7fd56e26e53c8ea32b598e8f4e06588e28aee376ed79eb9822ecf37e3099222`
- Judge schema SHA-256: `c03c0410b926db4903e624e0fe3e993a88d8b355caa51278c9f027aa7078ef66`
- Eval definition SHA-256: `381b074083537f3d71cb0a28bd3dbbcbf80ece8371ca5fba3a891d822f995603`
- Metadata SHA-256: `9511751d671a5ae5883161ea664a79cdce7fc89cb2e17e607a976174a239c8f6`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `parent_prd_context_read` | NOT_EXERCISED | The output references the existing order-management PRD and reuses its feature_path, but the locked output cannot prove the required read order. |
| `child_nested_under_parent` | PASS | It proposes order-management/refunds as a level-2 child of order-management, not a new top-level directory. |
| `feature_level_metadata` | PASS | It specifies parent_feature as order-management and feature_level as 2, matching the two path segments. |
| `handoff_packet_fields` | NOT_EXERCISED | The workflow pauses for user confirmation before generating the handoff packet, so the later packet-field requirement is not yet exercisable. |
| `no_bulk_prd` | PASS | No PRD or TRD was generated; subsequent PRD/DECISIONS work is directed to idea-to-spec and TRD generation to engineer-agent:trd-gen. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d30a63f3453aaf3bd01618d870dc101f5d610329fec8c95cdf338a27c46a679e; fixture_sha256=e64d0dc500eb5720a57f43e64b9a52c75b87f674117c2e966a459db4cd412910; output_sha256=4e9a6207537d263c4102d1fba62ddeabcbcc7740b4b6ab43c04944f9db438448; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies the refund feature as a nested level-2 feature and pauses for confirmation before handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d30a63f3453aaf3bd01618d870dc101f5d610329fec8c95cdf338a27c46a679e; fixture_sha256=e64d0dc500eb5720a57f43e64b9a52c75b87f674117c2e966a459db4cd412910; output_sha256=70ce617b495552b8939d808b6164a1334802f2caec4aa12033dce9ab24d7cfe0; snapshot_sha256=9457af2f83f3a465a71b79fd195f7ae23de910fb46d99f177ddade17b60e3ca8
- Behavior: Generated catalog and PRD files directly, including a refund PRD, without the confirmation gate.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain user confirmation, then evaluate the handoff packet fields from the subsequent output.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
