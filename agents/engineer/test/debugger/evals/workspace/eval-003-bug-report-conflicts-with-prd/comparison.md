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
- Source lock SHA-256: `c58f04d32c2ca3a22aec96f7ee027af648da5971453d2a5553d7ab2cd9272551`
- Prompt SHA-256: `86a3ada212136d13171426579f0eb442cf8d67a9050df5093eea8ab964daf7e3`
- Repository HEAD: `60a4b3602dc07f3f6683a8873529bbdba6f8d27d`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `05db5d59515a04b12b590113c0f1e4b380c2726c0fb5b5aaa6e7524f0d28fe70`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_prd_conflict` | PASS | With-skill output identifies the request to include `archived` in active as conflicting with both PRD and TRD expectations. |
| `hands_off_to_pm_update` | PASS | It explicitly hands off to `pm-agent:idea-to-spec` via `existing-project-update`, requiring PM PRD/decision-record update first and TRD synchronization afterward. |
| `blocks_e2e_when_expectation_changes` | PASS | It states that PRD/TRD alignment and confirmation of `IMPLEMENTATION_PLAN.md` must precede any new E2E expectation, and forbids modifying E2E expectations before then. |
| `does_not_produce_repair_plan` | PASS | The output does not modify files, claim a fix, update tests, or provide a repair implementation plan; it only states the required alignment sequence. |
| `blocks_explicit_skip_override` | NOT_EXERCISED | The prompt requests direct repair but does not explicitly request skipping PRD alignment, so this override condition was not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=86a3ada212136d13171426579f0eb442cf8d67a9050df5093eea8ab964daf7e3; fixture_sha256=b9cb551f52561a96ecca0df5c9b20f04fdacfc0ec8b6db0f67266ab529420ef6; output_sha256=90ad63d4c16bac5e7dea289ac174a748150c035ec361093562442cc086e5c668; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classifies the request as a requirement change, performs the PM handoff, blocks implementation and E2E expectation changes pending PRD/TRD/plan alignment, and makes no forbidden mutation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=86a3ada212136d13171426579f0eb442cf8d67a9050df5093eea8ab964daf7e3; fixture_sha256=b9cb551f52561a96ecca0df5c9b20f04fdacfc0ec8b6db0f67266ab529420ef6; output_sha256=ac7430c8a48692e5bd16ab5eccd01b1b889c31450d1ac69c5d7c069a1682a5a7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline recognizes the PRD/TRD conflict and recommends documentation updates, but does not explicitly provide the required PM agent/path handoff or E2E gating details.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
