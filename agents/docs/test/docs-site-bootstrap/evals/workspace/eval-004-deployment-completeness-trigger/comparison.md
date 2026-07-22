# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-site-bootstrap`
- Eval: `eval-004-deployment-completeness-trigger`
- Review context: issue #162 fresh paired validation

## Test Set / Fixture Version

- Fixture: issue #162 scenario evidence in this workspace
- Validation date: 2026-07-22
- Execution cleanup: all declared runtime paths were absent from pristine scratch fixtures

## Latest Result

**PASS (4/4 assertions)** — fresh Codex subagent semantic review.

## With-Skill Behavior

- 正确区分首次 integrated、首次 not_integrated、re-bootstrap partial 漂移，给出三选一和授权边界。
- Candidate source: fresh `tmp/eval-runs/issue-162/with_skill/eval-004-deployment-completeness-trigger/candidate-output.md`.

## Fresh Without-Skill Baseline

- BLOCKED (0/4)；识别事实但缺 durable commit trigger、稳定状态、完整三选一与 PM/DevOps 链路。
- The same prompt and pristine fixture were used; no historical baseline, target skill, Agent README, shared skill-map, old comparison, or with-skill output was used to compose it.

## Failures

- baseline 缺少共享 closeout 协议。
- No with-skill assertion failure or runner/credential blocker.

## Next Steps

- Keep this regression case; strengthen fixture ambiguity later where the baseline already passes.

## Runtime Artifact Policy

- Runtime candidates, copied fixtures, verdict, status, and diagnostics remain under `tmp/eval-runs/issue-162/` and are not committed.
- Only this durable comparison, eval definition, metadata, and fixture evidence are submitted.
