# Skill Eval Comparison

## Evaluation Target

- Skill: `env-config-auditor`
- Eval: `eval-004-docs-entry-access-audit`
- Review context: issue #162 fresh paired validation

## Test Set / Fixture Version

- Fixture: issue #162 scenario evidence in this workspace
- Validation date: 2026-07-22
- Execution cleanup: all declared runtime paths were absent from pristine scratch fixtures

## Latest Result

**PASS (3/3 assertions)** — fresh Codex subagent semantic review.

## With-Skill Behavior

- 四个环境/变体组合覆盖 DNS/TLS、Internal 控制、runtime resources 和 unknown，verified facts 才回 Docs。
- Candidate source: fresh `tmp/eval-runs/issue-162/with_skill/eval-004-docs-entry-access-audit/candidate-output.md`.

## Fresh Without-Skill Baseline

- PASS (3/3)；baseline 同样覆盖环境差异、unknown 与只读事实回传。
- The same prompt and pristine fixture were used; no historical baseline, target skill, Agent README, shared skill-map, old comparison, or with-skill output was used to compose it.

## Failures

- 无 assertion 失败；本 fixture 的区分度有限。
- No with-skill assertion failure or runner/credential blocker.

## Next Steps

- Keep this regression case; strengthen fixture ambiguity later where the baseline already passes.

## Runtime Artifact Policy

- Runtime candidates, copied fixtures, verdict, status, and diagnostics remain under `tmp/eval-runs/issue-162/` and are not committed.
- Only this durable comparison, eval definition, metadata, and fixture evidence are submitted.
