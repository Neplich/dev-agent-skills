# Skill Eval Comparison

## Evaluation Target

- Skill: `release-notes-generator`
- Eval: `eval-004-conditional-deployment-recheck`
- Review context: issue #162 fresh paired validation

## Test Set / Fixture Version

- Fixture: issue #162 scenario evidence in this workspace
- Validation date: 2026-07-22
- Execution cleanup: all declared runtime paths were absent from pristine scratch fixtures

## Latest Result

**PASS (2/2 assertions)** — fresh Codex subagent semantic review.

## With-Skill Behavior

- content-only 保留状态；runtime change 复用唯一共享协议且不复制 checklist。
- Candidate source: fresh `tmp/eval-runs/issue-162/with_skill/eval-004-conditional-deployment-recheck/candidate-output.md`.

## Fresh Without-Skill Baseline

- PARTIAL (1/2)；识别触发差异，但未声明共享状态/协议复用。
- The same prompt and pristine fixture were used; no historical baseline, target skill, Agent README, shared skill-map, old comparison, or with-skill output was used to compose it.

## Failures

- baseline 缺共享协议复用语义。
- No with-skill assertion failure or runner/credential blocker.

## Next Steps

- Keep this regression case; strengthen fixture ambiguity later where the baseline already passes.

## Runtime Artifact Policy

- Runtime candidates, copied fixtures, verdict, status, and diagnostics remain under `tmp/eval-runs/issue-162/` and are not committed.
- Only this durable comparison, eval definition, metadata, and fixture evidence are submitted.
