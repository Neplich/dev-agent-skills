# pm-agent Eval Comparison: eval-016

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-016-route-document-structure-governance`
- Workspace: `workspace/eval-016-route-document-structure-governance`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current workspace atop HEAD `1b45144`; the `idea-to-spec` Phase 0 lane table and PRD `child_features` schema/reference contract are updated in the uncommitted workspace. This case contains an aligned `notification-center` PM PRD and Engineer TRD, with Design, QA, DevOps, and Security roots absent.
- Fresh run: `2026-08-03 15:26:21 +0800`
- Runtime directory: `tmp/eval-runs/issue-197-evals-r4/pm-agent/eval-016-route-document-structure-governance/`; the HTML report itself is outside the repository in the `mktemp -d` directory `/private/var/folders/4g/9m0612cn1811btk7081t7ych0000gn/T/eval-016-structure-governance-r4.Xx7WBH/`.

## Latest result:

- Behavior result: PASS — all 5 assertions passed.
- Coverage result: FULL — 5/5 assertion scenarios were exercised; no `NOT EXERCISED` items.
- Overall result: PASS

## Assertion Results

- `routes_to_structure_governance`: PASS — the primary route is explicitly `idea-to-spec:structure-governance`, not `prd-iteration`, `feature-catalog`, or a downstream role agent.
- `read_only_audit`: PASS — the response defines and performs the audit as read-only and reports that no repository document was modified.
- `report_form`: PASS — the self-contained HTML report exists at `/private/var/folders/4g/9m0612cn1811btk7081t7ych0000gn/T/eval-016-structure-governance-r4.Xx7WBH/structure-governance-report.html`, whose canonical path is below the active temporary root and outside the repository; the repository runtime directory contains no HTML file, and the conversation response contains a concise findings summary plus the absolute report path.
- `scope_six_role_dirs`: PASS — the audit explicitly covers `docs/pm`, `docs/engineer`, `docs/design`, `docs/qa`, `docs/devops`, and `docs/security`; missing roots are recorded as limitations rather than created or treated as automatic defects.
- `structural_change_requires_confirmation`: PASS — any merge, split, or move is deferred until explicit user confirmation and must then run separately as `change_tier: major`.

## With-Skill Behavior

The dispatcher classifies the request as `document_structure_governance` and immediately continues into the read-only structure-governance lane now listed in the public Phase 0 lane table. The completed fixture scan finds one aligned level-1 feature node with two artifacts, records four missing role roots as limitations, notes the absent `child_features` field only as a low-confidence next-update observation because the fixture has no child nodes, writes the required HTML into a repository-external directory created by `mktemp -d`, returns the conversation summary and absolute report path, and preserves the approval boundary for all structural changes.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and fixture without reading or applying the target skill, Product Manager README, internal instructions, or historical comparison. It performs a simple directory inventory and avoids modifying files, but it does not establish the stable structure-governance route, generate the required HTML report, define the six-role governance scan contract, or apply the confirmation-plus-major gate. It also treats absent role directories as candidates to add later, whereas the with-skill behavior explicitly records them as limitations rather than automatic defects.

## Failures

- No assertion failures, unexercised assertions, or baseline-generation blockers.
- No fixture or assertion defect was observed.

## Next Steps

- Keep this eval as regression coverage for whole-tree structure-governance routing, repository-external `mktemp -d` report placement, and the read-only/major execution boundary.

## Runtime Artifacts Policy

- Fresh with-skill response, newly generated without-skill baseline, and judge notes remain under `tmp/eval-runs/issue-197-evals-r4/pm-agent/eval-016-route-document-structure-governance/` and are not committed.
- The HTML report remains outside the repository at `/private/var/folders/4g/9m0612cn1811btk7081t7ych0000gn/T/eval-016-structure-governance-r4.Xx7WBH/structure-governance-report.html` and is not committed.
