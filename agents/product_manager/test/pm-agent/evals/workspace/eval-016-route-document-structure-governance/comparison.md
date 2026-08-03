# pm-agent Eval Comparison: eval-016

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-016-route-document-structure-governance`
- Workspace: `workspace/eval-016-route-document-structure-governance`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current uncommitted workspace atop HEAD `65ec8f7`, including the current structure-governance role-boundary, reparenting dual-parent index, `_legacy` exclusion, and `child_features` fixes. The aligned level-1 `notification-center` PM PRD and Engineer TRD mirror the same path; Design, QA, DevOps, and Security roots are absent.
- Fresh run: `2026-08-03 16:57:47 +0800`
- Runtime directory: `tmp/eval-runs/issue-197-evals-r5/eval-016/`
- Runtime HTML: `/private/tmp/issue-197-eval016-r5.WmpXv9/structure-governance-report.html`

## Latest result:

- Behavior result: PASS — all 5 assertions passed.
- Coverage result: FULL — 5/5 assertion scenarios were exercised; no `NOT EXERCISED` items.
- Overall result: PASS

## Assertion Results

- `routes_to_structure_governance`: PASS — the primary route is explicitly `pm-agent -> idea-to-spec:structure-governance`, not `prd-iteration`, `feature-catalog`, or a downstream role agent.
- `read_only_audit`: PASS — the fixture scan is read-only; no repository document was modified, moved, created, or deleted.
- `report_form`: PASS — a self-contained HTML report was actually created in a repository-external `mktemp -d` directory. The file exists, required sections were verified, the repository contains no report body, and the with-skill response includes both a concise conclusion and the absolute path.
- `scope_six_role_dirs`: PASS — the audit covers `docs/pm`, `docs/engineer`, `docs/design`, `docs/qa`, `docs/devops`, and `docs/security`; missing roots are limitations rather than automatic defects.
- `structural_change_requires_confirmation`: PASS — any later merge, split, or move requires explicit user confirmation and a separate `change_tier: major` PM flow; none is executed by this audit.

## With-Skill Behavior

The dispatcher classified the request as `document_structure_governance` and continued into the read-only structure-governance lane. The scan found one aligned feature node with two artifacts, treated the PRD's `child_features` and the TRD's omission of that PRD-only field as consistent, recorded four missing role roots as limitations, and reported zero confirmed findings without inventing mandatory mirrors. The HTML also carries the current execution constraints: reparenting updates both old and new parent indexes, Engineer `_legacy/**` is excluded from active child nodes, archives remain archived, and QA history remains append-only.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and fixture without reading or applying `pm-agent`, `idea-to-spec`, the Product Manager README, internal instructions, historical comparison, or prior runtime output. It preserved read-only semantics, scanned all six role roots, and required confirmation plus separate major handling for later structural changes. It failed `routes_to_structure_governance` because no internal route was available and failed `report_form` because it returned only a Markdown summary without actually creating repository-external HTML. Baseline result: 3/5 assertions passed.

## Judge Conclusion

The fresh judge compared the with-skill output, newly generated baseline, fixture evidence, the actual HTML, and all five semantic assertions. The HTML existence, external location, required-section checks, and conversation summary make `report_form` directly exercised rather than inferred. All with-skill assertions passed, so Behavior is PASS and Coverage is FULL.

## Failures

- No with-skill assertion failures, unexercised assertions, or baseline-generation blockers.
- Baseline gaps: `routes_to_structure_governance` and `report_form` failed.

## Next Steps

- Keep this eval as regression coverage for whole-tree routing, repository-external report placement, and the read-only/major execution boundary.

## Runtime Artifacts Policy

- The with-skill response, newly generated without-skill baseline, and explicit judge record remain under `tmp/eval-runs/issue-197-evals-r5/eval-016/` and are not committed.
- The HTML report remains outside the repository at `/private/tmp/issue-197-eval016-r5.WmpXv9/structure-governance-report.html` and is not committed.
