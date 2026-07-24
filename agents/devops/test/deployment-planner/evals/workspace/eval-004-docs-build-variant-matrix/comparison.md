# Skill Eval Comparison

## Evaluation Target

- Skill: `deployment-planner`
- Eval: `eval-004-docs-build-variant-matrix`
- Review context: issue #162 fresh paired validation

## Test Set / Fixture Version

- Fixture: issue #162 scenario evidence in this workspace
- Validation date: 2026-07-22
- Execution cleanup: all declared runtime paths were absent from pristine scratch fixtures

## Latest Result

**PASS (3/3 assertions)** — fresh Codex subagent semantic review.

## With-Skill Behavior

- 矩阵覆盖 Public/Internal/Preview 及完整 deployment-unit 字段，逐变体处置并交 CI/CD。
- Candidate source: fresh `tmp/eval-runs/issue-162/with_skill/eval-004-docs-build-variant-matrix/candidate-output.md`.

## Fresh Without-Skill Baseline

- PARTIAL (1/3)；列出三个变体，但缺 context/static entry、K8s resources、values、health、runtime 与稳定处置。
- The same prompt and pristine fixture were used; no historical baseline, target skill, Agent README, shared skill-map, old comparison, or with-skill output was used to compose it.

## Failures

- baseline 部署单元矩阵不完整。
- No with-skill assertion failure or runner/credential blocker.

## Next Steps

- Keep this regression case; strengthen fixture ambiguity later where the baseline already passes.

## Runtime Artifact Policy

- Runtime candidates, copied fixtures, verdict, status, and diagnostics remain under `tmp/eval-runs/issue-162/` and are not committed.
- Only this durable comparison, eval definition, metadata, and fixture evidence are submitted.
