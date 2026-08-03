# pm-agent Eval Comparison: eval-016

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-016-route-document-structure-governance`
- Workspace: `workspace/eval-016-route-document-structure-governance`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current uncommitted workspace atop HEAD `82376b4`. It includes the review fixes that make `prd-iteration` derive direct child paths before using `child_features: N/A`, expand approved Engineer structure alignment to all affected TRD/API/ADR artifacts, hand active implementation plan alignment to `engineer-agent:feature-implementor`, and add the Implemented plan at `docs/engineer/repository-governance/feature-path-contract/IMPLEMENTATION_PLAN.md`. The eval fixture itself remains one aligned level-1 `notification-center` PM PRD and Engineer TRD; Design, QA, DevOps, and Security roots are absent.
- Fresh run: `2026-08-03 17:24:15 +0800`
- Runtime directory: `tmp/eval-runs/issue-197-evals-r6/eval-016/`
- Runtime HTML: `/private/tmp/issue-197-eval016-r6.G2ccXV/structure-governance-report.html`

## Latest result:

- Behavior result: PASS — all 5 assertions passed.
- Coverage result: FULL — 5/5 assertion scenarios were exercised; no `NOT EXERCISED` items.
- Overall result: PASS

## Assertion Results

- `routes_to_structure_governance`: PASS — the primary route is explicitly `pm-agent -> idea-to-spec:structure-governance` with `request_type: document_structure_governance`, not `prd-iteration`, `feature-catalog`, or a downstream role agent.
- `read_only_audit`: PASS — the fixture scan is read-only; no repository document was modified, moved, created, or deleted by the audit.
- `report_form`: PASS — a self-contained HTML report was actually created at `/private/tmp/issue-197-eval016-r6.G2ccXV/structure-governance-report.html`, outside the repository in the actual `mktemp -d` directory. File existence and all required report sections were verified, no HTML remains in the runtime directory, and the with-skill conversation output gives both the conclusion summary and absolute path.
- `scope_six_role_dirs`: PASS — the audit covers `docs/pm`, `docs/engineer`, `docs/design`, `docs/qa`, `docs/devops`, and `docs/security`; missing roots are reported as limitations rather than automatic findings.
- `structural_change_requires_confirmation`: PASS — any later merge, split, or move requires explicit user confirmation and a separate `change_tier: major` PM flow; the audit executes none. The report also states that affected Engineer TRD/API/ADR artifacts are aligned by Engineer and active plans by `engineer-agent:feature-implementor`.

## With-Skill Behavior

The dispatcher classified the request as `document_structure_governance` and continued into the read-only structure-governance lane. The scan found one aligned feature node and two artifacts, treated the PRD's derived `child_features: N/A` and the TRD's omission of that PRD-only field as consistent, recorded four missing role roots as limitations, and reported zero confirmed findings without inventing required mirrors. The actual HTML contains scope and limitations, role-aware feature tree, counts, evidence, recommendations, approval checklist, and the current execution constraints: dual-parent index updates for reparenting, `_legacy/**` exclusion, archive preservation, append-only QA history, full TRD/API/ADR Engineer alignment, and active implementation plan handoff to `feature-implementor`.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and fixture without applying `pm-agent`, `idea-to-spec`, the Product Manager README, internal instructions, historical comparison, or prior runtime output. It preserved read-only semantics, inspected all six role roots, and required separate approval and major handling for structural changes. It failed `routes_to_structure_governance` because it named no repository-specific route and failed `report_form` because it returned only a Markdown summary without creating repository-external HTML. Baseline result: 3/5 assertions passed.

## Judge Conclusion

The fresh judge compared the current fixture, with-skill response, newly generated baseline, actual external HTML, and all five semantic assertions. The internal route, read-only boundary, six-root scope, and separate major confirmation gate are explicit. The report file exists at the stated external path, includes every required section, and is paired with a conversation summary, so `report_form` is directly exercised. Therefore Behavior is PASS and Coverage is FULL.

## Failures

- No with-skill assertion failures, unexercised assertions, or baseline-generation blockers.
- Baseline gaps: `routes_to_structure_governance` and `report_form` failed.

## Next Steps

- Keep this eval as regression coverage for whole-tree routing, repository-external report placement, the read-only/major boundary, expanded Engineer artifact alignment, and active implementation plan ownership.

## Runtime Artifacts Policy

- The with-skill response, newly generated without-skill baseline, and explicit judge record remain under `tmp/eval-runs/issue-197-evals-r6/eval-016/` and are not committed.
- The HTML report remains outside the repository at `/private/tmp/issue-197-eval016-r6.G2ccXV/structure-governance-report.html` and is not committed.
