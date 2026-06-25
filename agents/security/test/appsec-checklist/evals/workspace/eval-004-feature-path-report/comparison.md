# Eval Result: eval-004-feature-path-report

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-004-feature-path-report`
- Test case: Feature Path Security Report
- Workspace: `workspace/eval-004-feature-path-report`
- Latest result: PASS - durable comparison coverage updated on 2026-06-25 for a real 4-level Security report path; no fresh model transcript or runtime output was generated in this worker pass.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: 4-level feature path `chat-interface/messages/history/search` with matching PM PRD, Engineer TRD, and implementation plan.
- 4+ fixture path: `chat-interface/messages/history/search`.
- Expected output: read same-path PM/Engineer documents and write `docs/security/chat-interface/messages/history/search/appsec-checklist.md` with feature path frontmatter, not `docs/security/history-search/appsec-checklist.md` or `docs/security/chat-interface/history-search/appsec-checklist.md`.

## Assertions

- PASS `uses_same_path_pm_engineer_docs`: must read the PRD, TRD, and implementation plan under `chat-interface/messages/history/search`.
- PASS `writes_nested_security_report`: must output the nested security report path and must not output a top-level or truncated `history-search` report.
- PASS `includes_feature_path_frontmatter`: report frontmatter must include `feature_path`, `parent_feature`, and `feature_level`.
- PASS `does_not_invent_feature_directory`: unclear or missing feature path input must return to PM/Engineer instead of creating a synonymous top-level directory.

## With Skill

- Expected with-skill behavior is to use the confirmed `feature_path`, read `docs/pm/{feature_path}/PRD.md`, read the matching Engineer TRD and implementation plan when architecture or release scope matters, and write `docs/security/{feature_path}/appsec-checklist.md`.
- The fixture supports the assertions: PM, TRD, and implementation plan all declare `feature_path: "chat-interface/messages/history/search"` with `parent_feature: "chat-interface/messages/history"` and `feature_level: "4"`; the TRD requires workspace-level authorization; `src/search.ts` includes a SQL string-concatenation risk that gives the AppSec review a concrete finding surface.
- Expected with-skill behavior is therefore to read the same-path PM/Engineer documents, produce frontmatter with `feature_path: chat-interface/messages/history/search`, `parent_feature: chat-interface/messages/history`, and `feature_level: 4`, and write `docs/security/chat-interface/messages/history/search/appsec-checklist.md` without creating `docs/security/history-search/appsec-checklist.md` or the older 2-level `docs/security/chat-interface/history-search/appsec-checklist.md`.

## Without Skill / Baseline
- Not run in this worker pass.
- High-level baseline contrast: a generic AppSec review may write a report under `docs/security/history-search/` or the older 2-level `docs/security/chat-interface/history-search/`, omit feature-path frontmatter, or lose the PM/Engineer source path needed for release traceability.

## Failures

- None in the durable eval definition, fixture, and assertion alignment reviewed on 2026-06-25.

## Next Steps

- Keep this eval as issue #37 coverage for 4-level Security feature-path reports and required feature-path frontmatter.
- Future transcript or runner diagnostics, if executed, should be kept as runtime artifacts and summarized here only after review.

## Runtime Artifacts Policy

- This validation used direct review of the skill docs, Agent README, `evals.json`, and fixture workspace. No runtime transcript, generated output directory, verdict file, timing file, diagnostics, or `comparison.auto.md` was created or committed.
