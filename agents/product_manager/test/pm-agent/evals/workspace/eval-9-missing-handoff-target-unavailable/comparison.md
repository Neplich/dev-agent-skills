# pm-agent Eval Comparison: eval-009

## Evaluation target

- Skill: `pm-agent`
- Test: `eval-009-missing-handoff-target-unavailable`
- Fixture version: current `README.md` and `eval_metadata.json` at 2026-08-01 13:12 +0800
- Fresh run: same prompt/fixture, newly generated with-skill and without-skill responses; no reused baseline.

## Latest result:

- Behavior result: PASS — all 3 assertions passed.
- Coverage result: FULL — 3/3 assertion scenarios were exercised.
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## With-skill behavior

Detected the unavailable Designer target, marked the stage blocked, named the plugin/capability requirement, and refused to produce Designer-owned visual artifacts.

## Without-skill baseline

The fresh baseline proposed that PM create a substitute visual spec, crossing the role boundary.

## Failures and next steps

- Failures: none.
- Next steps: none for this fixture.

## Runtime Artifacts Policy

Runtime evidence is isolated under `tmp/eval-runs/issue-196-project-bootstrap-removal-20260801-131022/pm-agent/eval-009-missing-handoff-target-unavailable/` and is not committed.
