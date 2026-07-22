# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-011-existing-site-deployment-recheck`
- Review context: issue #162 fresh paired validation

## Test Set / Fixture Version

- Fixture: issue #162 scenario evidence in this workspace
- Validation date: 2026-07-22
- Execution cleanup: all declared runtime paths were absent from pristine scratch fixtures

## Latest Result

**PASS (3/3 assertions)** — fresh Codex subagent semantic review.

## With-Skill Behavior

- 老站完整时保持 integrated 且不重放 DevOps；仅 Public 覆盖时判 partial 并只读返回 PM。
- Candidate source: fresh `tmp/eval-runs/issue-162/with_skill/eval-011-existing-site-deployment-recheck/candidate-output.md`.

## Fresh Without-Skill Baseline

- PARTIAL (2/3)；识别完整/部分覆盖，但直接建议 DevOps，未形成 PM repo-wide 回流。
- The same prompt and pristine fixture were used; no historical baseline, target skill, Agent README, shared skill-map, old comparison, or with-skill output was used to compose it.

## Failures

- baseline 未满足 PM 回流和完整角色边界。
- No with-skill assertion failure or runner/credential blocker.

## Next Steps

- Keep this regression case; strengthen fixture ambiguity later where the baseline already passes.

## Runtime Artifact Policy

- Runtime candidates, copied fixtures, verdict, status, and diagnostics remain under `tmp/eval-runs/issue-162/` and are not committed.
- Only this durable comparison, eval definition, metadata, and fixture evidence are submitted.
