# pm-agent Eval Comparison: eval-014

## Evaluation target

- Skill: `pm-agent`
- Test: `eval-014-route-site-notes-and-github-release`
- Fixture version: current `README.md` and `eval_metadata.json` at 2026-08-01 13:12 +0800
- Fresh run: same prompt/fixture, newly generated with-skill and without-skill responses; no reused baseline.

## Latest result:

- Behavior result: PASS — all 4 assertions passed.
- Coverage result: FULL — 4/4 assertion scenarios were exercised.
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## With-skill behavior

Routed site notes to `docs-agent:release-notes-gen`, GitHub Release preview to PM `github-release-gen`, preserved site-ready and audit gates, and did not revive the old PM skill name.

## Without-skill baseline

The fresh baseline preserved generic ordering but did not identify the exact specialist names, ownership prohibitions, or audit gate.

## Failures and next steps

- Failures: none.
- Next steps: none for this fixture.

## Runtime Artifacts Policy

Runtime evidence is isolated under `tmp/eval-runs/issue-196-project-bootstrap-removal-20260801-131022/pm-agent/eval-014-route-site-notes-and-github-release/` and is not committed.
