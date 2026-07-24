# Skill Eval Comparison

## Evaluation Target

- Skill: `pm-agent`
- Eval: `eval-015-route-docs-site-deployment-gap`
- Review context: issue #162 fresh paired validation

## Test Set / Fixture Version

- Fixture: issue #162 scenario evidence in this workspace
- Validation date: 2026-07-22
- Execution cleanup: all declared runtime paths were absent from pristine scratch fixtures

## Latest Result

**PASS (3/3 assertions)** — fresh Codex subagent semantic review.

## With-Skill Behavior

- unknown 阶段不误判；补证并确认后生成 N/A feature scope 的 repo-wide deployment packet 与完整有序链。
- Candidate source: fresh `tmp/eval-runs/issue-162/with_skill/eval-015-route-docs-site-deployment-gap/candidate-output.md`.

## Fresh Without-Skill Baseline

- PARTIAL (1/3)；阻塞 unknown，但缺结构化 packet 字段、formal-docs-sync 收尾和 verified-only 约束。
- The same prompt and pristine fixture were used; no historical baseline, target skill, Agent README, shared skill-map, old comparison, or with-skill output was used to compose it.

## Failures

- baseline 缺 packet contract 与完整 ordered chain。
- No with-skill assertion failure or runner/credential blocker.

## Next Steps

- Keep this regression case; strengthen fixture ambiguity later where the baseline already passes.

## Runtime Artifact Policy

- Runtime candidates, copied fixtures, verdict, status, and diagnostics remain under `tmp/eval-runs/issue-162/` and are not committed.
- Only this durable comparison, eval definition, metadata, and fixture evidence are submitted.
