# pm-agent Eval Comparison: eval-016

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-016-route-document-structure-governance`
- Workspace: `workspace/eval-016-route-document-structure-governance`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current uncommitted workspace atop HEAD `74c3b26`. The workspace includes the review fixes that exclude `implementation-plans/archive/**` and `_legacy/**` from active overlong/L2b governance evidence, make child-PRD generation reconcile the parent `child_features` index from the complete direct-child set, and synchronize `related_prd` plus other applicable `related_*` path fields during approved Engineer structure changes. The fixture itself remains one aligned level-1 `notification-center` PM PRD and Engineer TRD; Design, QA, DevOps, and Security roots are absent. The report directly applies the new archive/legacy exclusion rule, but the fixture contains no such files, so exclusion of a positive archived/legacy sample is not an independent assertion scenario in this case.
- Fresh run: `2026-08-03 17:44:54 +0800`
- Runtime directory: `tmp/eval-runs/issue-197-evals-r7/eval-016/`
- Runtime HTML: `/private/var/folders/4g/9m0612cn1811btk7081t7ych0000gn/T/issue-197-eval016-r7.BdxVLc/structure-governance-report.html`

## Latest result:

- Behavior result: PASS — all 5 assertions passed.
- Coverage result: FULL — 5/5 assertion scenarios were exercised; no `NOT EXERCISED` items.
- Overall result: PASS

## Assertion Results

- `routes_to_structure_governance`: PASS — the primary route is explicitly `pm-agent -> idea-to-spec:structure-governance` with `request_type: document_structure_governance`, not `prd-iteration`, `feature-catalog`, or a downstream role agent.
- `read_only_audit`: PASS — the fixture scan was read-only; no repository document was modified, moved, created, or deleted by the audit. Only the requested ignored scratch notes and repository-external report were produced.
- `report_form`: PASS — a self-contained HTML report was actually created at `/private/var/folders/4g/9m0612cn1811btk7081t7ych0000gn/T/issue-197-eval016-r7.BdxVLc/structure-governance-report.html`, inside the actual repository-external `mktemp -d` directory. File existence, external placement, required sections, and absence of HTML from the repository runtime directory were verified; the with-skill conversation response gives both the conclusion summary and absolute path.
- `scope_six_role_dirs`: PASS — the scan and HTML explicitly cover `docs/pm`, `docs/engineer`, `docs/design`, `docs/qa`, `docs/devops`, and `docs/security`; missing roots are limitations rather than automatic findings.
- `structural_change_requires_confirmation`: PASS — any later merge, split, or move requires explicit user confirmation and a separate `change_tier: major` PM flow; the audit executes none. The report also preserves archive/legacy semantics and names `related_prd` plus other applicable `related_*` fields for later approved Engineer alignment.

## With-Skill Behavior

The dispatcher classified the request as `document_structure_governance` and continued directly into the read-only structure-governance lane. The actual fixture scan found one aligned feature node and two Markdown artifacts, treated the four missing role roots as limitations, and reported zero confirmed overlong, orphan, sibling, duplicate, or cross-role drift findings. A missing explicit `related_prd` on the fixture TRD was retained as a low-severity metadata completeness observation rather than misreported as an orphan or path conflict. The external HTML includes scope and exclusions, role-aware feature coverage, summary counts, detailed evidence, a no-change recommendation, approval checks, and current execution constraints including complete parent-index reconciliation, `related_*` synchronization, and archive/legacy exclusion.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and fixture without reading or applying `pm-agent`, `idea-to-spec`, the Product Manager README, internal instructions, the historical comparison, or prior runtime output. It preserved read-only semantics, inspected all six role roots, and required separate approval and major handling for structural changes. It failed `routes_to_structure_governance` because it named no repository-specific route and failed `report_form` because it returned only a Markdown summary without creating repository-external HTML. Baseline result: 3/5 assertions passed.

## Judge Conclusion

The fresh judge compared the current fixture, with-skill conversation response, newly generated baseline, actual external HTML, scan evidence, and all five assertions. The specialized route, read-only boundary, six-root scope, and separate major confirmation gate are explicit. The HTML exists at the stated external path, contains every required report section, and is paired with a conclusion summary. Therefore Behavior is PASS and Coverage is FULL. The baseline contrast isolates the skill's two material increments: repository-specific routing and an actually written external HTML report.

## Failures

- No with-skill assertion failures, unexercised assertions, or baseline-generation blockers.
- Baseline gaps: `routes_to_structure_governance` and `report_form` failed.

## Next Steps

- Keep this eval as regression coverage for whole-tree routing, repository-external report placement, the read-only/major boundary, and six-role scope.
- If direct positive coverage of archive/legacy exclusion is required, add a separate fixture containing over-500-line files below `implementation-plans/archive/**` and `_legacy/**`; this case's required five assertions are fully covered without such a sample.

## Runtime Artifacts Policy

- The with-skill response, scan evidence, newly generated without-skill baseline, and explicit judge record remain under `tmp/eval-runs/issue-197-evals-r7/eval-016/` and are not committed.
- The HTML report remains outside the repository at `/private/var/folders/4g/9m0612cn1811btk7081t7ych0000gn/T/issue-197-eval016-r7.BdxVLc/structure-governance-report.html` and is not committed.
