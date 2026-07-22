# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-014-conditional-deployment-recheck`
- Review context: issue #162 fresh paired validation

## Test Set / Fixture Version

- Fixture: issue #162 scenario evidence in this workspace
- Validation date: 2026-07-22
- Execution cleanup: all declared runtime paths were absent from pristine scratch fixtures

## Latest Result

**PASS (2/2 assertions)** — fresh Codex subagent semantic review.

## With-Skill Behavior

- version-only 保持状态；build/runtime change 刷新共享状态，不建第二协议、不改部署资产。
- Candidate source: fresh `tmp/eval-runs/issue-162/with_skill/eval-014-conditional-deployment-recheck/candidate-output.md`.

## Fresh Without-Skill Baseline

- PARTIAL (1/2)；识别是否重检，但未声明共享协议与状态刷新契约。
- The same prompt and pristine fixture were used; no historical baseline, target skill, Agent README, shared skill-map, old comparison, or with-skill output was used to compose it.

## Failures

- baseline 缺共享协议复用语义。
- No with-skill assertion failure or runner/credential blocker.

## Next Steps

- Keep this regression case; strengthen fixture ambiguity later where the baseline already passes.

## Runtime Artifact Policy

- Runtime candidates, copied fixtures, verdict, status, and diagnostics remain under `tmp/eval-runs/issue-162/` and are not committed.
- Only this durable comparison, eval definition, metadata, and fixture evidence are submitted.
