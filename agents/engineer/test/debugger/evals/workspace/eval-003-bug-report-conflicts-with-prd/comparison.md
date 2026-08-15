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
- target_skill_sha256: `8f85dae9526c56f3d9c6b946dd90d2d85718bee6a272309b91713955601d3385`
- eval_definition_sha256: `1b0128e389f23ce11fa7b4c38a0b662507e4f8c62e4b45bb6324446e6c6f6b76`
- metadata_sha256: `998b1102ce48b0144bf502fdc4b5b73963a99afa1878cf20966b9057cddc4e55`
- fixture_sha256: `b9cb551f52561a96ecca0df5c9b20f04fdacfc0ec8b6db0f67266ab529420ef6`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `a8bfc4df337c13eb13450fd2790a0adaaa6e985db2ba520873d18d41987ab63d`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `86a3ada212136d13171426579f0eb442cf8d67a9050df5093eea8ab964daf7e3`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `3e75308618e40000064b1f17dc0f0b301f828ec4f2f128fc91b1ab1bc2382820`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_prd_conflict` | PASS | With-skill output identifies the request as requirement_change and states the user's desired archived inclusion conflicts with both PRD and TRD, which exclude archived from active. |
| `hands_off_to_pm_update` | PASS | With-skill output explicitly routes to pm-agent:idea-to-spec via existing-project-update, then orders PM PRD/decision update before engineer-agent:trd-gen TRD synchronization. |
| `blocks_e2e_when_expectation_changes` | PASS | With-skill output requires PRD/decision update, TRD synchronization, and confirmed IMPLEMENTATION_PLAN.md before any new E2E expectation is written. |
| `does_not_produce_repair_plan` | PASS | With-skill output does not modify files, update tests, claim a fix, or provide an implementation repair plan; it only states that a plan must be formed later after alignment. |
| `blocks_explicit_skip_override` | NOT_EXERCISED | The supplied user scenario does not explicitly request skipping PRD alignment, so this override condition is not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=86a3ada212136d13171426579f0eb442cf8d67a9050df5093eea8ab964daf7e3; fixture_sha256=b9cb551f52561a96ecca0df5c9b20f04fdacfc0ec8b6db0f67266ab529420ef6; output_sha256=8163f0966f4703958e2e9ae12b17279d25696b2a8b37fd7bc3da75235381dd68; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classifies the request as a requirement change, hands off through the PM update path, preserves the PRD/TRD/implementation-plan gate, and leaves the repository unchanged.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=86a3ada212136d13171426579f0eb442cf8d67a9050df5093eea8ab964daf7e3; fixture_sha256=b9cb551f52561a96ecca0df5c9b20f04fdacfc0ec8b6db0f67266ab529420ef6; output_sha256=64262158272854b1701b48d63bdba188ae560219cbc7b65e8b2b31c938a988bd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Recognizes the product-rule conflict and avoids mutation, but gives a more generic next step without the explicit PM handoff path and E2E gating sequence.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
