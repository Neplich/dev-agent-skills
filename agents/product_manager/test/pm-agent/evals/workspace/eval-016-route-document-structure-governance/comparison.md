# pm-agent Eval Comparison: eval-016

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-016-route-document-structure-governance`
- Workspace: `workspace/eval-016-route-document-structure-governance`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current HEAD `5fcfa17`; aligned `notification-center` PM PRD and Engineer TRD, with Design, QA, DevOps, and Security roots absent.
- Fresh run: `2026-08-03 14:13:16 +0800`
- Runtime directory: `tmp/eval-runs/issue-197-evals/pm-agent/eval-016-route-document-structure-governance/`

## Latest result:

- Behavior result: PASS — all 5 assertions passed.
- Coverage result: FULL — 5/5 assertion scenarios were exercised; no `NOT EXERCISED` items.
- Overall result: PASS

## Assertion Results

- `routes_to_structure_governance`: PASS — the primary route is explicitly `idea-to-spec:structure-governance`, not `prd-iteration`, `feature-catalog`, or a downstream role agent.
- `read_only_audit`: PASS — the response defines and performs the audit as read-only and reports that no repository document was modified.
- `report_form`: PASS — a self-contained HTML report is written to the run-specific tmp directory outside durable fixture outputs, excluded from git, and the conversation response contains a concise findings summary and report path.
- `scope_six_role_dirs`: PASS — the audit explicitly covers `docs/pm`, `docs/engineer`, `docs/design`, `docs/qa`, `docs/devops`, and `docs/security`; missing roots are recorded as limitations rather than created or treated as automatic defects.
- `structural_change_requires_confirmation`: PASS — any merge, split, or move is deferred until explicit user confirmation and must then run separately as `change_tier: major`.

## With-Skill Behavior

The dispatcher classifies the request as `document_structure_governance` and immediately continues into the read-only structure-governance lane. The completed fixture scan finds one aligned feature node and two artifacts, records four missing role roots as limitations, produces the required runtime HTML plus conversation summary, and preserves the approval boundary for all structural changes.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and fixture without reading or applying the target skill, Product Manager README, internal instructions, or historical comparison. It performs a simple directory inventory and avoids modifying files, but it does not establish the stable structure-governance route, generate an HTML report in runtime tmp, define the six-role scan contract, or apply the confirmation-plus-major gate. It also loosely suggests filling every missing role directory, whereas the with-skill behavior correctly treats missing roots as limitations rather than automatic defects.

## Failures

- No assertion failures, unexercised assertions, or baseline-generation blockers.
- No fixture or assertion defect was observed.

## Next Steps

- Keep this eval as regression coverage for whole-tree structure-governance routing, runtime-report form, and the read-only/major execution boundary.

## Runtime Artifacts Policy

- Fresh with-skill response, newly generated without-skill baseline, judge notes, and the HTML report remain under `tmp/eval-runs/issue-197-evals/pm-agent/eval-016-route-document-structure-governance/` and are not committed.
