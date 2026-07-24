# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-006-preserve-independent-hosting`
- Review context: issue #162 fresh paired validation

## Test Set / Fixture Version

- Fixture: issue #162 scenario evidence in this workspace
- Validation date: 2026-07-22
- Execution cleanup: all declared runtime paths were absent from pristine scratch fixtures

## Latest Result

**PASS (2/2 assertions)** — fresh Codex subagent semantic review.

## With-Skill Behavior

- 保留 not_applicable、证据、Public/Internal、维护者决定和下一 owner，有效时不生成 DevOps handoff。
- Candidate source: fresh `tmp/eval-runs/issue-162/with_skill/eval-006-preserve-independent-hosting/candidate-output.md`.

## Fresh Without-Skill Baseline

- PARTIAL (1/2)；保留独立托管决定但未使用稳定 not_applicable 状态。
- The same prompt and pristine fixture were used; no historical baseline, target skill, Agent README, shared skill-map, old comparison, or with-skill output was used to compose it.

## Failures

- baseline 缺少稳定跨角色状态。
- No with-skill assertion failure or runner/credential blocker.

## Next Steps

- Keep this regression case; strengthen fixture ambiguity later where the baseline already passes.

## Runtime Artifact Policy

- Runtime candidates, copied fixtures, verdict, status, and diagnostics remain under `tmp/eval-runs/issue-162/` and are not committed.
- Only this durable comparison, eval definition, metadata, and fixture evidence are submitted.
