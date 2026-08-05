# Eval Result: eval-002-route-docs-site-completeness-chain

## Evaluation Target

- Agent: `devops`
- Skill: `devops-agent`
- Eval: `eval-002-route-docs-site-completeness-chain`
- Test case: route-docs-site-completeness-chain
- Workspace: `workspace/eval-002-route-docs-site-completeness-chain`
- Review context: issue #196 L2-4 router single-source convergence

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: `pm-handoff.md` with a confirmed repo-wide documentation deployment packet, `N/A` feature scope, completeness evidence, and explicit delivery authorization boundary.
- Validation date: 2026-07-31.
- With-skill source: fresh candidate generated after reading `agents/devops/README.md`, `agents/devops/skills/devops-agent/SKILL.md`, `evals.json`, `eval_metadata.json`, and `pm-handoff.md`.
- Without-skill source: fresh candidate regenerated from the same prompt and fixture only, without reading or applying the DevOps Agent README, target skill, with-skill candidate, historical comparison, or prior baseline.

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL** (3/3 assertions exercised)
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertions

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_repo_wide_docs_handoff` | PASS | The with-skill result accepts deployment request type, `N/A` feature scope, and completeness evidence without returning for feature-path clarification. |
| `routes_dependency_order` | PASS | It states `deployment-planner -> cicd-bootstrap -> env-config-auditor -> docs-agent:formal-docs-sync` in dependency order. |
| `preserves_role_and_authority_boundaries` | PASS | It states that DevOps does not edit formal docs, only verified landed facts go to Docs, and the handoff does not authorize commit, push, image publication, or deployment. |

## With-Skill Behavior

The router recognizes the complete repo-wide documentation-site packet as the explicit exception allowed by its PM handoff gate. It preserves the `N/A` feature scope, routes the four-stage chain in dependency order, and keeps both the DevOps/Docs role boundary and delivery authority boundary explicit.

The L2-4 route table provides the deployment, CI/CD, and configuration-audit mappings without relying on a duplicated Routing Signals section. This explicit confirmed chain is not expanded from an underspecified request.

## Fresh Without-Skill Baseline

The fresh baseline accepts the repo-wide `N/A` scope, infers deployment followed by CI/CD and configuration review, and recognizes that routing does not authorize commit, push, image publication, or deployment.

It is less precise than the with-skill result: it does not name the exact four-stage specialist chain and does not explicitly state that DevOps must not edit formal documentation and may return only landed, verified operational facts to `docs-agent:formal-docs-sync`. It therefore provides useful general routing but does not meet two assertions in full.

## Failures

- No with-skill assertion failures.
- Baseline gap: exact dependency-chain identifiers and the verified-only DevOps-to-Docs role boundary.
- No assertion was marked `NOT EXERCISED`; all three behaviors were observable.
- No runtime, credential, or external-service blocker occurred.

## Next Steps

- Keep this eval as regression coverage for the confirmed repo-wide documentation-site handoff exception and exact dependency order.
- Continue checking that future router edits preserve the verified-only Docs handoff and do not imply delivery authorization.

## Runtime Artifact Policy

- Fresh paired evidence is stored only under `tmp/eval-runs/issue-196-l2-3-4/devops-agent/eval-002-route-docs-site-completeness-chain/`:
  - `with_skill.md`
  - `without_skill.md`
  - `judge.md`
- These scratch files are not committed.
- Runtime transcripts, candidates, verdicts, timing, status, diagnostics, and generated output directories must not be copied into the fixture workspace.
