# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-003-bug-report-conflicts-with-prd`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b9cb551f52561a96ecca0df5c9b20f04fdacfc0ec8b6db0f67266ab529420ef6` from `agents/engineer/test/debugger/evals/workspace/eval-003-bug-report-conflicts-with-prd`.
- Identity schema: `2`
- target_skill_sha256: `3f5fc52f5119888b420cf0815200bcffd4eec82b0638977ef69f000383c62d4a`
- eval_definition_sha256: `1b0128e389f23ce11fa7b4c38a0b662507e4f8c62e4b45bb6324446e6c6f6b76`
- metadata_sha256: `998b1102ce48b0144bf502fdc4b5b73963a99afa1878cf20966b9057cddc4e55`
- fixture_sha256: `b9cb551f52561a96ecca0df5c9b20f04fdacfc0ec8b6db0f67266ab529420ef6`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `a8bfc4df337c13eb13450fd2790a0adaaa6e985db2ba520873d18d41987ab63d`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `86a3ada212136d13171426579f0eb442cf8d67a9050df5093eea8ab964daf7e3`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `05db5d59515a04b12b590113c0f1e4b380c2726c0fb5b5aaa6e7524f0d28fe70`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_prd_conflict` | PASS | With-skill output classifies the request as a requirement change and states PRD requires archived to remain excluded from active, establishing the conflict with the requested behavior. |
| `hands_off_to_pm_update` | FAIL | It names pm-agent:idea-to-spec and says to update the PRD or product decision, but does not identify the required existing-project-update path. |
| `blocks_e2e_when_expectation_changes` | PASS | It explicitly says not to modify docs/qa/e2e and gates any new expectation on PRD/product decision update, TRD synchronization, and confirmed IMPLEMENTATION_PLAN. |
| `does_not_produce_repair_plan` | PASS | No code or tests were changed, no repair was claimed, and the output only describes gated future workflow steps rather than a concrete repair implementation plan. |
| `blocks_explicit_skip_override` | NOT_EXERCISED | The prompt does not explicitly ask to skip PRD alignment, so this override case is not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=86a3ada212136d13171426579f0eb442cf8d67a9050df5093eea8ab964daf7e3; fixture_sha256=b9cb551f52561a96ecca0df5c9b20f04fdacfc0ec8b6db0f67266ab529420ef6; output_sha256=f673876c6f3f621d83de1e7517f92c4be472d990178925924487bfd9adae44c5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies a product requirement change, preserves the PRD/TRD gate, and avoids mutation, but omits the required existing-project-update path in the PM handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=86a3ada212136d13171426579f0eb442cf8d67a9050df5093eea8ab964daf7e3; fixture_sha256=b9cb551f52561a96ecca0df5c9b20f04fdacfc0ec8b6db0f67266ab529420ef6; output_sha256=538b60a5438311731cd16d0bee8f51831b8913132708a25c314d1b44ac7bb066; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Recognizes the documented behavior and avoids direct repair, but provides only a general PRD-first recommendation without the required workflow gates and explicit handoff path.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The required existing-project-update handoff path is omitted.
- Next: Require the PM handoff to explicitly use pm-agent:idea-to-spec via the existing-project-update path.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
