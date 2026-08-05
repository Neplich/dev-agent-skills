# pm-agent Eval Comparison: eval-016

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-016-route-document-structure-governance`
- Workspace: `workspace/eval-016-route-document-structure-governance`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current uncommitted workspace atop HEAD `5af2134`. The workspace includes the latest review fixes: reserved namespace parents (`repository-governance` / `agent-collaboration`) need no physical root PRD or parent-index update; approved moves have per-role owners and each owner uses `git mv` only for its own directory; child-PRD creation refreshes the complete parent index and also bumps the parent version, refreshes `last_updated`, and adds changelog; contract PRD/TRD use `related_issues` and include issue #197. The fixture itself remains one aligned level-1 `notification-center` PM PRD and Engineer TRD; Design, QA, DevOps, and Security roots are absent. The HTML includes the reserved-namespace and per-role-owner constraints, but the fixture contains no reserved namespace or actual move, so those are not separate positive assertion scenarios in this case.
- Fresh run: `2026-08-03 18:05:27 +0800`
- Runtime directory: `tmp/eval-runs/issue-197-evals-r8/eval-016/`
- Runtime HTML: `/private/var/folders/4g/9m0612cn1811btk7081t7ych0000gn/T/issue-197-eval016-r8.TCC3Ls/structure-governance-report.html`

## Latest result:

- Behavior result: PASS — all 5 assertions passed.
- Coverage result: FULL — 5/5 assertion scenarios were exercised; no `NOT EXERCISED` items.
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- `routes_to_structure_governance`: PASS — the primary route is explicitly `pm-agent -> idea-to-spec:structure-governance` with `request_type: document_structure_governance`, not `prd-iteration`, `feature-catalog`, or a downstream role agent.
- `read_only_audit`: PASS — the fixture scan did not modify, move, create, or delete repository documents. Only ignored runtime evidence and the repository-external HTML report were generated.
- `report_form`: PASS — the self-contained HTML was actually written to `/private/var/folders/4g/9m0612cn1811btk7081t7ych0000gn/T/issue-197-eval016-r8.TCC3Ls/structure-governance-report.html`, an actual `mktemp -d` path outside the repository. Its existence, external placement, required sections, and absence from the repository runtime directory were verified; the with-skill response supplies the conclusion summary and absolute path.
- `scope_six_role_dirs`: PASS — both the scan and HTML cover `docs/pm`, `docs/engineer`, `docs/design`, `docs/qa`, `docs/devops`, and `docs/security`; missing roots are limitations, not automatic defects.
- `structural_change_requires_confirmation`: PASS — later merge, split, or move work requires explicit confirmation and a separate `change_tier: major` flow; the audit executes none. The report assigns PM, Engineer, Design, QA, DevOps, and Security work to the required role owners and preserves the reserved-parent namespace exemption.

## With-Skill Behavior

The dispatcher classified the request as `document_structure_governance` and continued directly into the read-only structure-governance lane. The scan found one aligned feature node and two Markdown artifacts, treated four missing role roots as limitations, and reported zero confirmed overlong, orphan, sibling, duplicate, or cross-role drift findings. The report retains a missing explicit `related_prd` as an informational metadata observation rather than misclassifying it as an orphan. The external HTML contains scope, feature coverage, summary counts, evidence, no-change recommendation, approval checklist, reserved-parent exemption, per-role move ownership, parent PRD refresh rules, and archive/QA-history constraints.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and fixture without reading or applying `pm-agent`, `idea-to-spec`, Product Manager README, internal instructions, historical comparison, or prior runtime output. It preserved read-only semantics, addressed all six role roots, and required approval plus major handling for later structural changes. It failed `routes_to_structure_governance` because it named no repository-specific route and failed `report_form` because it returned only a Markdown summary without writing external HTML. Baseline result: 3/5 assertions passed.

## Judge Conclusion

The judge compared the current fixture, with-skill response, newly generated baseline, scan evidence, actual external HTML, and all five assertions. The specialized route, read-only boundary, six-root scope, and separate major confirmation gate are explicit. The HTML exists at the reported external path, contains every required report section, and is paired with a conversation conclusion summary. Behavior is PASS and Coverage is FULL. The baseline contrast isolates the skill's repository-specific route and actually written external report.

## Failures

- No with-skill assertion failures, unexercised assertions, or baseline-generation blockers.
- Baseline gaps: `routes_to_structure_governance` and `report_form` failed.

## Next Steps

- Keep this eval as regression coverage for routing, repository-external report placement, read-only/major separation, and six-role scope.
- Use separate fixture assertions if direct positive coverage is needed for a reserved namespace parent, an approved per-role `git mv`, parent PRD version/date/changelog refresh, or contract `related_issues` metadata.

## Runtime Artifacts Policy

- The with-skill response, scan evidence, newly generated baseline, and explicit judge record remain under `tmp/eval-runs/issue-197-evals-r8/eval-016/` and are not committed.
- The HTML report remains outside the repository at `/private/var/folders/4g/9m0612cn1811btk7081t7ych0000gn/T/issue-197-eval016-r8.TCC3Ls/structure-governance-report.html` and is not committed.
