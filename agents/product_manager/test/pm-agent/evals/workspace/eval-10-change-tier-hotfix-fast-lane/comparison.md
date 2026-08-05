# pm-agent Eval Comparison: eval-010

## Evaluation target

- Skill: `pm-agent`
- Test: `eval-010-change-tier-hotfix-fast-lane`
- Fixture version: current `README.md` and `eval_metadata.json` at 2026-08-01 13:12 +0800
- Fresh run: same prompt/fixture, newly generated with-skill and without-skill responses; no reused baseline.

## Latest result:

- Behavior result: PASS — all 3 assertions passed.
- Coverage result: FULL — 3/3 assertion scenarios were exercised.
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## With-skill behavior

Classified delivery/status plus `hotfix`, justified the single-evidence unchanged-expectation lane, allowed fast lane only after classification, and retained scope/source/verification evidence.

## Without-skill baseline

The fresh baseline allowed a quick submission but did not preserve the formal classification and evidence packet.

## Failures and next steps

- Failures: none.
- Next steps: none for this fixture.

## Runtime Artifacts Policy

Runtime evidence is isolated under `tmp/eval-runs/issue-196-project-bootstrap-removal-20260801-131022/pm-agent/eval-010-change-tier-hotfix-fast-lane/` and is not committed.
