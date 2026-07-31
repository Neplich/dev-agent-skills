# Skill Eval Comparison

## Evaluation Target

- Skill: `pm-agent`
- Eval: `eval-001-route-greenfield-product-request`
- Review context: issue #196 L2-4 fresh paired validation

## Test Set / Fixture Version

- Schema: `evals.json` v1.0; current prompt and fixture
- Validation date: 2026-07-31
- With-skill source: fresh Codex session `019fb589-672e-7bc0-95ff-2ada072730dd`
- Without-skill source: fresh isolated Codex session `019fb58b-f4fa-7232-abda-91612bafb9a3`; no skill, Agent README, assertions, with output, or prior comparison was provided

## Latest Result

- Latest result: PASS
- Behavior result: PASS (5/5 assertions)
- Coverage result: FULL (5/5 assertions exercised)
- Overall result: PASS

## With-Skill Behavior

Selected `idea-to-spec`, enforced the empty-workspace PM-first boundary, named the discovery context and PRD/BRD/DECISIONS outputs, and placed TRD/implementation after scope confirmation.

## Fresh Without-Skill Baseline

Also chose PM discovery first, but did not identify the canonical `idea-to-spec` route or the complete PM artifact/TRD ownership contract.

## Failures

- None.

## Next Steps

- Keep as a greenfield entry regression case.

## Runtime Artifacts Policy

- Paired runtime outputs stay under `tmp/eval-runs/issue-196-l2-3-4/pm-agent/eval-001-route-greenfield-product-request/` and are not committed.
