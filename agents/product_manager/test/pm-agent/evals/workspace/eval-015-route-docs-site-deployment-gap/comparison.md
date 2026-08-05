# pm-agent Eval Comparison: eval-015

## Evaluation target

- Skill: `pm-agent`
- Test: `eval-015-route-docs-site-deployment-gap`
- Fixture version: current `evidence.md` and `eval_metadata.json` at 2026-08-01 13:12 +0800
- Fresh run: same prompt/fixture, newly generated with-skill and without-skill responses; no reused baseline.

## Latest result:

- Behavior result: PASS — all 3 assertions passed.
- Coverage result: FULL — 3/3 assertion scenarios were exercised.
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## With-skill behavior

Kept missing CI/Helm evidence at `unknown`, produced the confirmed repo-wide deployment packet with `N/A` fields and preserved evidence/risks, and routed the ordered DevOps chain before final fact-only Docs synchronization.

## Without-skill baseline

The fresh baseline recognized missing evidence and the broad DevOps-before-Docs order, but omitted the stable status semantics, exact packet fields, evidence preservation, and specialist chain.

## Failures and next steps

- Failures: none.
- Next steps: none for this fixture.

## Runtime Artifacts Policy

Runtime evidence is isolated under `tmp/eval-runs/issue-196-project-bootstrap-removal-20260801-131022/pm-agent/eval-015-route-docs-site-deployment-gap/` and is not committed.
