# Skill Eval Comparison

## Evaluation Target

- Skill: `pm-agent`
- Eval: `eval-013-change-tier-hotfix-e2e-direct-path`
- Review context: issue #196 L2-4 fresh paired validation

## Test Set / Fixture Version

- Schema: `evals.json` v1.0; current prompt and fixture
- Validation date: 2026-07-31
- Sources: fresh with-skill session `019fb589-672e-7bc0-95ff-2ada072730dd`; fresh isolated baseline session `019fb58b-f4fa-7232-abda-91612bafb9a3`

## Latest Result

- Latest result: FAIL
- Behavior result: FAIL (2/3 assertions)
- Coverage result: FULL (3/3 assertions exercised)
- Overall result: FAIL

## With-Skill Behavior

Correctly limited hotfix QA/E2E to directly affected paths, required execution results and evidence, and did not demand the full suite. It did not explicitly require recording blocked checks.

## Fresh Without-Skill Baseline

Matched the same two passing behaviors and likewise omitted blocked-check recording; there is no meaningful assertion-level differentiation in this run.

## Failures

- FAIL `evidence_still_required`: verification evidence and results were named, but “any blocked checks” was not explicitly recorded.

## Next Steps

- Tighten the skill output or fixture so hotfix QA closeout explicitly records blocked checks.

## Runtime Artifacts Policy

- Runtime outputs remain in `tmp/eval-runs/issue-196-l2-3-4/pm-agent/eval-013-change-tier-hotfix-e2e-direct-path/` and are not committed.
