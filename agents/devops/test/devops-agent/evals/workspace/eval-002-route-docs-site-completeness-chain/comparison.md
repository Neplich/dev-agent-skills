# Skill Eval Comparison

## Evaluation Target

- Skill: `devops-agent`
- Eval: `eval-002-route-docs-site-completeness-chain`
- Review context: issue #162 fresh paired validation

## Test Set / Fixture Version

- Fixture: issue #162 scenario evidence in this workspace
- Validation date: 2026-07-22
- Execution cleanup: all declared runtime paths were absent from pristine scratch fixtures

## Latest Result

**PASS (3/3 assertions)** — fresh Codex subagent semantic review.

## With-Skill Behavior

- 接受 repo-wide N/A scope，按四段顺序路由，并保持 DevOps/Docs 与交付授权边界。
- Candidate source: fresh `tmp/eval-runs/issue-162/with_skill/eval-002-route-docs-site-completeness-chain/candidate-output.md`.

## Fresh Without-Skill Baseline

- PARTIAL (1/3)；接受 repo-wide scope，但未明确 formal-docs-sync 和 verified-only handoff。
- The same prompt and pristine fixture were used; no historical baseline, target skill, Agent README, shared skill-map, old comparison, or with-skill output was used to compose it.

## Failures

- baseline 缺精确下游目标与角色边界。
- No with-skill assertion failure or runner/credential blocker.

## Next Steps

- Keep this regression case; strengthen fixture ambiguity later where the baseline already passes.

## Runtime Artifact Policy

- Runtime candidates, copied fixtures, verdict, status, and diagnostics remain under `tmp/eval-runs/issue-162/` and are not committed.
- Only this durable comparison, eval definition, metadata, and fixture evidence are submitted.
