# pm-agent Eval Comparison: eval-016

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-016-route-document-structure-governance`
- Workspace: `workspace/eval-016-route-document-structure-governance`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: final uncommitted workspace atop HEAD `1e3eac4`. The aligned level-1 `notification-center` PM PRD includes `child_features: "N/A"`; the Engineer TRD mirrors the same path and correctly omits this PRD-only field, while Design, QA, DevOps, and Security roots are absent.
- Fresh run: `2026-08-03 15:56:54 +0800`
- Runtime directory: `tmp/eval-runs/issue-197-selfreview/final/eval-016/`
- Runtime HTML: `/private/tmp/issue-197-eval016-final.7kzYb4/structure-governance-report.html`

## Latest result:

- Behavior result: PASS — all 5 assertions passed.
- Coverage result: FULL — 5/5 assertion scenarios were exercised; no `NOT EXERCISED` items.
- Overall result: PASS

## Assertion Results

- `routes_to_structure_governance`: PASS — the primary route is explicitly `pm-agent -> idea-to-spec:structure-governance`, not `prd-iteration`, `feature-catalog`, or a downstream role agent.
- `read_only_audit`: PASS — the fixture scan is read-only and no repository document is modified, moved, created, or deleted.
- `report_form`: PASS — a self-contained HTML report was actually created by using `mktemp -d`; its canonical absolute path is outside the repository, the file exists, all required sections were verified, the repository contains no `structure-governance-report.html`, and the response contains a concise summary plus the absolute path.
- `scope_six_role_dirs`: PASS — the audit covers `docs/pm`, `docs/engineer`, `docs/design`, `docs/qa`, `docs/devops`, and `docs/security`; missing roots are limitations rather than automatic defects.
- `structural_change_requires_confirmation`: PASS — any later merge, split, or move requires explicit user confirmation and a separate `change_tier: major` PM flow.

## With-Skill Behavior

The dispatcher classifies the request as `document_structure_governance` and continues into the read-only structure-governance lane. The scan finds one aligned feature node with two artifacts, treats the PRD's `child_features` and the TRD's omission of that PRD-only field as consistent, records four missing role roots as limitations, and reports zero confirmed findings without inventing mandatory mirrors. It writes and verifies the required repository-external HTML, returns the summary and path, and preserves the approval boundary for all structural changes.

## Fresh Without-Skill Baseline

The baseline was newly regenerated after the final skill change in an isolated context from the same prompt and fixture without reading or applying `pm-agent`, `idea-to-spec`, the Product Manager README, internal instructions, historical comparison, or prior runtime output. It passed routing, read-only, six-role scope, and confirmation/major assertions, and its fixture conclusions matched the with-skill scan. It failed `report_form`: it described the desired runtime HTML but did not create one and correctly refused to claim a nonexistent path. Baseline result: 4/5 assertions passed.

## Failures

- No with-skill assertion failures, unexercised assertions, or baseline-generation blockers.
- Fresh baseline gap: `report_form` FAIL because no HTML artifact was produced.

## Next Steps

- Keep this eval as regression coverage for whole-tree routing, repository-external `mktemp -d` report placement, and the read-only/major execution boundary.

## Runtime Artifacts Policy

- Fresh with-skill response, newly regenerated without-skill baseline, and self-check notes remain under `tmp/eval-runs/issue-197-selfreview/final/eval-016/` and are not committed.
- The HTML report remains outside the repository at `/private/tmp/issue-197-eval016-final.7kzYb4/structure-governance-report.html` and is not committed.
